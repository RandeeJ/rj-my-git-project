After a git pull

#-------- ABOVE IS A TEST ----- 

mkdir [folder name]
cd [folder name]
touch [file name]
git init #to create a git repository
ls #to see all files
ls -la #to see all hidden files
git status
git add [file name (python file)]
git status #to see updated addition
git commit -m "Initial commit"
git status
#on github, create new repository and copy second set of codes, then run
#should now see local file on github

#------------

CREATING A README FILE

touch README.md #md means markdown
git status
git add . #updates everything
git status
git commit -m "Add 'filename' file to repository"
git push

#-------------

TROUBLESHOOTING

git push origin main --force #forcing a git push
<<<<<<< Updated upstream
#another change
=======

#everytime you create a commit, you are storing a version.

git checkout -b stash-demo
git status
git checkout main
git status
git checkout .
git status
git checkout stash-demo
git status
git stash
git log
git checkout main
git checkout stash-demo
git stash list
git stash show
get stash clear
>>>>>>> Stashed changes


git status
git pull
git status
git add .
git commit -m "Added new python function"
git fetch
git status
git branch
git status
git merge origin/main
git status
git push

#-----------------------------------

#once you merge a branch, get rid of it

git branch
git checkout -b branch branch-to-remove
git add .
git commit -m "updated readme"
git push -u origin branch-to-remove
git checkout main
git branch -d branch-to-remove
git branch
git pull
git push origin --delete branch-to-remove

#--------------------------------------------
#merge conflicts
#when you and another team member have worked on the same lines of code and how to work through the merge conflict

#changes made to git hub files
# changes made to local files
git status
git add .
git commit -m "Updated readme and python script"
git fetch origin
git status
#determine which code you want to eliminate/keep & save
git merge origin/main
git status
git add .
git commit -m "fixed merge conflicts"
git push


#-------------------------------------------
# git will keep track of changes to existing files 
git status
git diff my_file.py #shows changes
git diff README.md #shows changes
git status
git checkout . #reverts back to file state before recent changes
git status
touch my_bad_file.py
#edit/add content in my_bad_file.py
git status
git checkout . #will not work for my_bad_file
git status
rm my_bad_file #to remove file!
git status

#---------------------------------------
#fixing a mistake from past versions
#can tell system to revert back to previous version

cp my_file.py demo_file.py
git log
git checkout [commit code for README taken from log] -- README.md
git status
rm demo_file.py
git add .
git commit -m "Reverted back to [commit code] for README.md"
git push

# -------------------------------------
# viewing code from a previous version