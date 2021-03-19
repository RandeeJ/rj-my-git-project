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
