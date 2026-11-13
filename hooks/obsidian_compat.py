"""Render Obsidian-authored Markdown the same way Obsidian does.

The notes in this repository are written in Obsidian (CommonMark-ish) but built
with Python-Markdown, whose block parser is stricter in ways readers notice:

1. **A list may not start on the line right after a paragraph.**
   CommonMark lets a bullet list interrupt a paragraph, so Obsidian shows

       硬件的组成部分：
       - 输入设备

   as a paragraph followed by a list.  Python-Markdown folds both lines into one
   paragraph and prints the ``- `` as literal text.  The same happens after a
   fenced code block, after a blockquote (``> ...``) and when the list type
   changes (``1. ...`` followed by ``- ...``).  We insert the blank line that
   Obsidian implies.

2. **Nested items may be indented by a tab, or by any number of spaces.**
   Obsidian only asks that a child be indented more than its parent, so notes mix
   tabs, two, three, four and eight spaces - sometimes within a single list.
   Python-Markdown accepts exactly one step size (``mdx_truly_sane_lists``'s
   ``nested_indent``) and folds every item indented differently into its parent
   as literal text.  We rewrite each list marker to a canonical four-space step,
   leaving the indentation of the outermost item untouched.

3. **A blockquote may not continue a list item.**
   Obsidian closes the item and starts a sibling ``<blockquote>``; Python-Markdown
   instead appends the quote to the ``<li>``, so it renders indented inside the
   bullet.  A blockquote indented less than the list's content column cannot
   belong to an item, so we insert the blank line again.  A quote indented as far
   as the item's content column really does belong to the item, and is left alone.

   The same applies to a callout written one tab deep in an item: the callouts
   plugin turns it into ``!!! tip`` at that indentation, which Python-Markdown
   only recognises when a block starts there.

A fourth, smaller difference: Obsidian accepts ``1)`` as an ordered-list marker,
Python-Markdown only understands ``1.``.  The marker is rewritten when the item
really becomes a list, because the rendered ``<ol>`` is the same either way.

Anything Obsidian itself shows as plain text is left alone: a marker indented a
full tab below a paragraph, one followed by a non-breaking space, or an ordered
item that does not start at 1 below a paragraph line.  Every rewrite only touches
list markers outside fenced code blocks, and the result is idempotent, so running
it on every page of every build is safe.
"""

from __future__ import annotations

import re

try:  # MkDocs >= 1.4 sorts event handlers by this priority.
    from mkdocs.plugins import event_priority
except ImportError:  # pragma: no cover - older MkDocs, run in registration order
    def event_priority(priority: float):
        def decorator(func):
            return func

        return decorator


#: A list marker plus the whitespace that must follow it.
ITEM_RE = re.compile(r"^(?P<indent>[ \t]*)(?P<marker>[-*+]|\d+[.)])(?P<space>[ \t]+)")

#: Leading blockquote markers (``>``, ``> >``, ...), kept with their own spacing.
BLOCKQUOTE_RE = re.compile(r"^(?P<prefix>[ ]{0,3}(?:>[ ]?)+)(?P<inner>.*)$")

#: A fenced code block delimiter.
FENCE_RE = re.compile(r"^[ \t]*(?P<fence>`{3,}|~{3,})")

#: An admonition header (``!!! note``).
ADMONITION_RE = re.compile(r"^[ \t]*!{3}")

#: An Obsidian callout header (``> [!TIP]``), optionally indented into a list item.
CALLOUT_RE = re.compile(r"^[ \t]*>[ ]?\[!")

#: Constructs that already end a paragraph in Python-Markdown, so a list needs no
#: blank line in front of them.  Blockquotes are handled separately, and a table
#: row counts as ordinary text here, because a list after it ends the table.
BLOCK_START_RE = re.compile(
    r"""^[ \t]*(
        \#{1,6}[ \t]                     # ATX heading
      | !{3}                             # admonition
      | ([-*_])([ \t]*\2){2,}[ \t]*$     # horizontal rule
    )""",
    re.VERBOSE,
)

#: Python-Markdown expands tabs to four columns, so use the same width here.
TAB_WIDTH = 4
#: Indentation step of the rendered (normalised) list.
STEP = 4


def _leading_whitespace(text: str) -> str:
    return text[: len(text) - len(text.lstrip(" \t"))]


def _indent_width(prefix: str) -> int:
    return len(prefix.expandtabs(TAB_WIDTH))


def _can_interrupt_paragraph(marker: str) -> bool:
    """Whether this item may start a list directly below a paragraph line.

    CommonMark only allows an *ordered* list to interrupt a paragraph when it
    starts at 1; a bullet list may always interrupt one.  Following the same rule
    keeps a stray ``2)`` from turning into a list Obsidian would show as text.
    """
    return not marker[:1].isdigit() or marker[0] == "1"


class _Level:
    """Bookkeeping for one blockquote depth."""

    __slots__ = (
        "items",
        "pending_text",
        "last_item",
        "in_paragraph",
        "admonition_indent",
        "in_list_block",
        "list_block_col",
    )

    def __init__(self) -> None:
        # Indent widths of the items enclosing the current one, outermost first.
        self.items: list[int] = []
        # Whether the previous line may be continued by a list (a paragraph).
        self.pending_text = False
        # (kind, level) of the previous list item, or None.
        self.last_item: tuple[str, int] | None = None
        # True while a run of "items" is really plain paragraph text, so every
        # marker in it must stay exactly as written.
        self.in_paragraph = False
        # Indentation of the current admonition body, or None.  Inside one, an
        # indented block is content rather than an indented code block.
        self.admonition_indent: int | None = None
        # True while the current block contains a list, with the content column
        # of that list's outermost item.  A blockquote indented less than that
        # column cannot belong to the item, so it ends the list.
        self.in_list_block = False
        self.list_block_col: int | None = None


def normalize(markdown: str) -> str:
    """Rewrite list indentation and add the blank lines Obsidian implies."""
    levels: dict[int, _Level] = {}
    out: list[str] = []
    previous_depth = 0
    previous_blank = True
    fence: tuple[str, int, int] | None = None  # (fence char, length, depth)

    def state(depth: int) -> _Level:
        return levels.setdefault(depth, _Level())

    for line in markdown.split("\n"):
        quote = BLOCKQUOTE_RE.match(line)
        if quote:
            prefix, inner = quote.group("prefix"), quote.group("inner")
            depth = prefix.count(">")
        else:
            prefix, inner, depth = "", line, 0
        level = state(depth)
        indent = _leading_whitespace(inner)
        item = ITEM_RE.match(inner)

        # ---- fenced code blocks are copied verbatim -----------------------
        fence_match = FENCE_RE.match(inner)
        if fence is not None:
            char, length, fence_depth = fence
            if (
                fence_match
                and depth == fence_depth
                and fence_match.group("fence")[0] == char
                and len(fence_match.group("fence")) >= length
            ):
                fence = None
                # The fence ends a block, so a list may follow it immediately.
                ended = state(fence_depth)
                ended.pending_text = True
                ended.last_item = None
                ended.in_paragraph = False
                ended.in_list_block = False
                ended.list_block_col = None
                previous_blank = False
            out.append(line)
            previous_depth = depth
            continue
        if fence_match:
            fence = (fence_match.group("fence")[0], len(fence_match.group("fence")), depth)
            level.pending_text = False
            level.last_item = None
            level.in_paragraph = False
            level.in_list_block = False
            level.list_block_col = None
            out.append(line)
            previous_depth, previous_blank = depth, False
            continue

        # ---- blank lines ---------------------------------------------------
        if not inner.strip():
            out.append(line)
            level.pending_text = False
            level.last_item = None
            level.in_paragraph = False
            level.in_list_block = False
            level.list_block_col = None
            # A blank line is a block boundary for Python-Markdown, so nesting
            # has to be measured from the next list's own outermost item again.
            level.items.clear()
            previous_depth, previous_blank = depth, True
            continue

        # ---- a blockquote that ends a list item ----------------------------
        # Obsidian closes the item and starts a sibling ``<blockquote>``, while
        # Python-Markdown appends the quote to the ``<li>``.  A quote indented as
        # far as the item's content column really does belong to the item.
        if depth > previous_depth:
            list_level = state(previous_depth)
            quote_indent = len(prefix) - len(prefix.lstrip(" "))
            if list_level.in_list_block and quote_indent < (list_level.list_block_col or 0):
                out.append(("> " * min(previous_depth, depth)).rstrip())
                previous_blank = True  # the quote starts its own block now

        # ---- an indented callout inside a list item ------------------------
        # ``> [!TIP]`` written one tab deep belongs to the item above it.  The
        # callouts plugin turns it into ``!!! tip`` at that indentation, which
        # Python-Markdown cannot recognise unless a block starts there, so insert
        # the boundary Obsidian implies.
        if (
            item is None
            and not previous_blank
            and level.in_list_block
            and _indent_width(indent) >= TAB_WIDTH
            and CALLOUT_RE.match(inner)
        ):
            out.append("")
            # The line starts a new block, exactly like a real blank line.
            level.pending_text = False
            level.last_item = None
            level.in_paragraph = False
            level.in_list_block = False
            level.list_block_col = None
            level.items.clear()
            previous_blank = True

        if item is None:
            # ---- ordinary content -----------------------------------------
            out.append(line)
            if level.admonition_indent is not None and _indent_width(indent) < level.admonition_indent:
                level.admonition_indent = None
            if _indent_width(indent) == 0:
                # A fresh block at the inner margin ends whatever list came before.
                level.items.clear()
                level.pending_text = not BLOCK_START_RE.match(inner)
            else:
                level.pending_text = True
            if ADMONITION_RE.match(inner):
                level.admonition_indent = _indent_width(indent) + TAB_WIDTH
            level.last_item = None
            level.in_paragraph = False
            previous_depth, previous_blank = depth, False
            continue

        # ---- a list item ---------------------------------------------------
        width = _indent_width(indent)
        marker = item.group("marker")
        kind = "ol" if marker[:1].isdigit() else "ul"

        while level.items and width < level.items[-1]:
            level.items.pop()
        if not level.items or width > level.items[-1]:
            level.items.append(width)
        nesting = len(level.items) - 1
        new_width = level.items[0] + STEP * nesting
        new_indent = " " * new_width

        separate = False
        swallowed = False
        if not previous_blank:
            if level.in_paragraph and depth == previous_depth:
                # Part of a run that is really paragraph text: keep it verbatim.
                swallowed = True
            elif depth != previous_depth:
                separate = True  # a blockquote started or ended here
            elif level.pending_text:
                if _can_interrupt_paragraph(marker):
                    separate = True
                else:
                    # Obsidian keeps this line inside the paragraph, as does
                    # Python-Markdown: leave the marker exactly as written.
                    swallowed = True
            if (
                not swallowed
                and level.last_item
                and level.last_item[0] != kind
                and nesting <= level.last_item[1]
            ):
                separate = True  # ``1.`` followed by ``-`` starts a new list
            if separate and new_width >= TAB_WIDTH and level.admonition_indent is None:
                # A block opening a full tab deeper than its container margin is
                # an *indented code block* to Python-Markdown, not a list, and
                # Obsidian keeps such a line inside the paragraph as well.
                separate = False
                swallowed = True
        if separate:
            if depth != previous_depth:
                # Put the blank line at the outer level, so the blockquote the
                # previous line belonged to really ends (or starts) here.
                out.append(("> " * min(previous_depth, depth)).rstrip())
            else:
                out.append(prefix.rstrip())

        # Python-Markdown only understands ``1.``, Obsidian accepts ``1)`` too.
        # Rewrite the marker whenever the item really becomes a list, so that a
        # ``1)`` sitting inside a paragraph keeps its original spelling.
        if marker.endswith(")") and not swallowed:
            marker = marker[:-1] + "."
        out.append(prefix + new_indent + marker + inner[item.end("marker"):])
        level.pending_text = False
        level.last_item = (kind, nesting)
        level.in_paragraph = swallowed
        level.in_list_block = True
        if nesting == 0:
            level.list_block_col = new_width + len(marker) + len(item.group("space"))
        previous_depth, previous_blank = depth, False

    return "\n".join(out)


@event_priority(100)  # before the other on_page_markdown handlers
def on_page_markdown(markdown, **kwargs):  # noqa: D401 - MkDocs hook signature
    """Entry point used by MkDocs."""
    return normalize(markdown)
