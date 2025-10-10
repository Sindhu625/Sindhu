* What Are Conflicts in Git?



A conflict happens when two or more people (or branches) change the same part of a file, and Git doesn’t know which change to keep.



Example:



You and your teammate both edit main.py, line 10 differently.



When you try to merge or pull, Git says:



CONFLICT (content): Merge conflict in main.py



Git pauses the merge and asks you to manually fix the conflicting lines.



* What Is a Git Rollback?



A rollback means undoing changes — going back to a previous state in your repo.



Here are a few common rollback commands:



Command:



git restore <file>



git reset --soft <commit>	



git reset --hard <commit>	



git revert <commit>



Purpose	Example:



Undo changes in a file (before committing)	



Undo commits but keep changes staged	



Undo commits and delete changes	



Create a new commit that undoes a previous one



Example:



git restore main.py



git reset --soft HEAD~1



git reset --hard HEAD~1



git revert abc1234

