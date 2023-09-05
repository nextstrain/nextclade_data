# If you have forks, make sure to set `git config --global checkout.defaultRemote origin`
# Make sure that you local machine has the latest changes from the remote server
git pull --all

# Don't use below while we use staging for v3
# # Switch to release branch
# git checkout staging

# # Fast-forward release branch to master locally
# git merge master staging --ff-only

# # Push release branch to the remote server
# git push origin staging

git checkout release
git merge staging release --ff-only
git push origin release

# Switch away from the release branch to avoid accidental commits later
git checkout staging

