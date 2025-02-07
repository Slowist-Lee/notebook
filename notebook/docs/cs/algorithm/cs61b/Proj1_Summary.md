## Preface
This project is all about ==just recycle== …… actually it's not difficult since you have the test points here.

## 1. is it empty or full or ... ?
Since the document warns us only to design the vertical movement, let's consider what situation can **a single column** be in.
if it's empty? we don't need to do any actions. just skip it. since i want to use `for` loop, i just design "if not empty", do something.

## 2. for a single cell? take the 1st '2' for e.g.

| 1st | 2nd | 3th | 4th |
| --- | --- | --- | --- |
| 2   | 0   | 2   | 2   |
considering the '2' located in the 1st space.
for the element, it will traverse the following element $\rightarrow$ until……
- firstly, it's not null.
then it compares.
- if the next element is '2' as well -> merge into 4
- not: stay in the cell before it.

the progress in my mind could be →
1. traverse the following cell from self, until the last empty cell, which located in $[n]$
2. compare
3. if same, score increases & move to $[n+1]$. else, move to $[n]$

>now u see, the program behind merge is slightly different from just move to another position. so! you can code two different functions to complete the whole move.
## 3. special occasions

now there're some special occasions.
### 3.1 on the side?
we only consider the move inside the board. what if it is on the side?






