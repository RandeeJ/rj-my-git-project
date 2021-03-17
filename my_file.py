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

# -------------MERGING FEATURE BRANCHES TO MASTER BRANCH--------

git branch #to see what branch you are on
git checkout -b readme-styling
git branch
# edit Readme
git add Readme.md
git commit -m "Updated Readme"
git status
git checkout main
git merge readme-styling

#---------------------------------------

