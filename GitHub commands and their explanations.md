GitHub commands and their explanations



* Basic Commands

1.git init                 → Create new repository  

2\.git clone <url>          → Copy repo from GitHub  

3\.git status               → Check repo status  

4\.git add <file> / .       → Stage file(s)  

5\.git commit -m "msg"      → Save changes  

6\.git log                  → View commit history  



* Branching

1.git branch               → List branches  

2\.git branch <name>        → Create new branch  

3\.git checkout <name>      → Switch branch  

4\.git checkout -b <name>   → Create + switch branch  

5\.git merge <branch>       → Merge branch  

6\.git branch -d <name>     → Delete branch  



* Remote (GitHub)

1.git remote add origin <url>  → Connect to GitHub repo  

2\.git push -u origin <branch>  → Push code first time  

3\.git push                     → Push updates  

4\.git pull                     → Get updates from GitHub  

5\.git fetch                    → Download updates only  



* Undo / Reset

1.git restore <file>       → Undo changes in file  

2\.git reset <file>         → Unstage file  

3\.git reset --hard         → Undo all changes (dangerous)  

4\.git revert <commit>      → Undo specific commit  



* Config

1.git config --global user.name "Name"  

2.git config --global user.email "Email"  

3.git config --list        → Show settings  



