```ad-warning
the lab is mainly about managing the environment
so some details will be written down in the note!
```


### 1. How to run the `java` codes?

For example, to run `HelloWorld.java`, we'd type the command `javac HelloWorld.java` into the terminal, followed by the command `java HelloWorld`. The result would look something like this:

```
$ javac HelloWorld.java
$ java HelloWorld
Hello World! 
```

### 2 Git_Exercise

`url:https://sp18.datastructur.es/materials/lab/lab1/lab1`

```bash
PS D:\MyRepository\cs61b\cs61b_W1> mkdir lab1-checkoff


    目录: D:\MyRepository\cs61b\cs61b_W1


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          2024/8/2     10:45                lab1-checkoff


PS D:\MyRepository\cs61b\cs61b_W1> cd lab1-checkoff
PS D:\MyRepository\cs61b\cs61b_W1\lab1-checkoff> git init .
Initialized empty Git repository in D:/MyRepository/cs61b/cs61b_W1/lab1-checkoff/.git/
PS D:\MyRepository\cs61b\cs61b_W1\lab1-checkoff> code 61b.txt
PS D:\MyRepository\cs61b\cs61b_W1\lab1-checkoff> git add 61b.txt
PS D:\MyRepository\cs61b\cs61b_W1\lab1-checkoff> git commit -m "Add 61b.txt"
[master (root-commit) 937e0db] Add 61b.txt
 1 file changed, 1 insertion(+)
 create mode 100644 61b.txt
PS D:\MyRepository\cs61b\cs61b_W1\lab1-checkoff> code 61c.txt
PS D:\MyRepository\cs61b\cs61b_W1\lab1-checkoff> code 61b.txt
PS D:\MyRepository\cs61b\cs61b_W1\lab1-checkoff> git add 61c.txt 61b.txt
PS D:\MyRepository\cs61b\cs61b_W1\lab1-checkoff> git commit -m "Update 61b.txt and add 61c.txt"
[master 9cc17d2] Update 61b.txt and add 61c.txt
 2 files changed, 2 insertions(+), 1 deletion(-)
 create mode 100644 61c.txt
PS D:\MyRepository\cs61b\cs61b_W1\lab1-checkoff> code 61b.txt
PS D:\MyRepository\cs61b\cs61b_W1\lab1-checkoff> git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   61b.txt

no changes added to commit (use "git add" and/or "git commit -a")
PS D:\MyRepository\cs61b\cs61b_W1\lab1-checkoff> git log
commit 9cc17d22271bf48edc6e8dcfa219889505df348f (HEAD -> master)
Author: Slowist Lee <3230103034@zju.edu.cn>
Date:   Fri Aug 2 10:50:38 2024 +0800

    Update 61b.txt and add 61c.txt

commit 937e0db2abaef821b10affca3e83a561292f327e
Author: Slowist Lee <3230103034@zju.edu.cn>
Date:   Fri Aug 2 10:48:16 2024 +0800

    Add 61b.txt
```

### Submitting to Gradescope

1. Add your assignment directory using `git add`. For example, for Lab 1, from your repo root (`sp24-***`) you would use `git add lab01`. From the assignment directory, you could use `git add .`.
2. Commit the files using `git commit -m "<commit message here>"`. The commit message is required. For example, `git commit -m "Finished Lab 1"`.
3. Push your code to your remote repository with `git push origin main`.
4. Open the assignment on Gradescope. Select Github, then your `sp24-s***` repository and the `main` branch, then submit your assignment. You will receive a confirmation email, and the autograder will run automatically.

Gradescope will use the latest version of your code from Github. **If you think that Gradescope isn’t grading the right code, check that you have added, committed, and pushed with `git status`.**


### Problems:

- `git clone` create a new directory which is named the same as the remote repository itself.  So after cloning it, make sure to `cd cs61b` instead of adding branches in the original vault.
the fatal message could be:
![alt text](image-2.png)

