# Git  

!!! abstract  
    记录一些自己在使用`git`过程中的新发现!  

## Gitignore

指路-> https://gitbook-tw.translate.goog/chapters/using-git/ignore?_x_tr_sl=auto&_x_tr_tl=zh-CN&_x_tr_hl=zh-CN&_x_tr_pto=wapp  


```bash
# 檔案名稱 .gitignore

# 忽略 secret.yml 檔案
secret.yml

# 忽略 config 目錄下的 database.yml 檔案
config/database.yml

# 忽略所有 db 目錄下附檔名是 .sqlite3 的檔案
/db/*.sqlite3

# 忽略所有附檔名是 .tmp 的檔案
*.tmp

# 當然你要忽略自己也可以，只是通常不會這麼做
# .gitignore
```
### 原来已经提交，但现在删除的处理方式

>Git 忽略文件是基于当前的状态，而 `.gitignore` 只会忽略**尚未被 Git 跟踪的文件**。如果 `.obsidian` 目录之前已经被 `git add` 并提交过，它会被 Git 继续跟踪，即使你在 `.gitignore` 中添加了它。因此，`.gitignore` 只是告诉 Git 忽略新的文件或文件夹，但它不会影响已经在版本控制中的文件。

-  **移除 `.obsidian` 目录的跟踪**
你可以使用 `git rm --cached` 命令来将 `.obsidian` 目录从 Git 的版本控制中移除，但保留本地的文件。

```bash
git rm -r --cached .obsidian
```
- 意思是：  
   - `-r`：递归移除 `.obsidian` 目录。
   - `--cached`：仅从 Git 的索引（即版本控制）中移除文件，而不删除本地文件。

- **提交更改**
移除 `.obsidian` 后，你需要提交这个更改到 Git 仓库。

```bash
git commit -m "Remove .obsidian directory from version control"
```

- **推送到远端仓库**  
将更改推送到远程仓库，以便远程仓库也同步移除 `.obsidian` 目录。

```bash
git push
```

- **确认 `.obsidian` 被正确忽略**  
确保 `.gitignore` 文件中已经添加了 `.obsidian`，并且该目录不会再被添加到 Git 跟踪中。你可以查看 `.gitignore` 是否包含以下内容：

```gitignore
.obsidian/
```

如果 `.gitignore` 中已经有了 `.obsidian`，那在执行了上述操作后，它就会被 Git 忽略，不会再被提交。


- `.obsidian` 目录在添加到 Git 后，即使你将其添加到 `.gitignore` 中，它仍然会被 Git 跟踪。你需要使用 `git rm --cached` 来移除它的版本控制。
- 通过 `git commit` 和 `git push` 来将这个更改同步到远程仓库。
- 确保 `.gitignore` 文件中正确地忽略 `.obsidian` 目录，以防止它以后再次被跟踪。

这样，你就能确保 `.obsidian` 目录从远端仓库中删除，但仍然保留在本地。

## Multiple Users

- 问题：每次推送Github都要我选择用户，太麻烦  
- 解决方式：[here](https://github.com/git-ecosystem/git-credential-manager/blob/main/docs/multiple-users.md)  

## Warning 解释/处理

### 1. LF will be replaced by CRLF

碰到了如下`warning`:
```bash
warning: in the working copy of '...', LF will be replaced by CRLF the next time Git touches it
```

解释：

LF (Line Feed) 和 CRLF (Carriage Return + Line Feed) 是两种常见的换行符。  
LF 是 Linux 和 macOS 系统中使用的换行符（\n）。  
CRLF 是 Windows 系统使用的换行符（\r\n）。  
Git 会根据操作系统的不同，自动处理换行符，确保跨平台协作时不会出现换行符不一致的问题。  