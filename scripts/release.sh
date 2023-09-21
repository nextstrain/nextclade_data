# If you have forks, make sure to set `git config --global checkout.defaultRemote origin`
# Make sure that you local machine has the latest changes from the remote server
git pull --all

git checkout release
git merge staging release --ff-only
git push origin release

# Switch away from the release branch to avoid accidental commits later
git checkout staging

