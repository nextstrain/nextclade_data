import shlex
from os import getcwd
from typing import List, Union

from .logger import logger
from .process import run
from .string import quote


def prepare_paths_args(paths: str | list[str] | None = None):
  paths = paths or getcwd()
  return ' '.join(quote([paths] if isinstance(paths, str) else paths))


def get_lines(s: str):
  lines = s.split("\n")
  lines = map(str.strip, lines)
  return iter(filter(len, lines))


def git_get_dirty_files(dirs: str | list[str] | None = None):
  dirs = dirs or getcwd()
  lines = get_lines(run(f"git status --untracked --porcelain -- {prepare_paths_args(dirs)}"))
  return iter(map(lambda line: line.split(" ")[1], lines))


def git_dir_is_clean(dirs: str | list[str] | None = None):
  dirs = dirs or getcwd()
  return len(list(git_get_dirty_files(dirs))) == 0


def git_get_initial_commit_hash():
  return run("git rev-list --max-parents=0 HEAD")


def git_get_current_commit_hash(branch: str = "HEAD", short=False):
  short_flag = "--short" if short else ""
  return run(f"git rev-parse {short_flag} '{branch}'", error_if_empty=True)


def git_get_modified_files(
  from_revision: str | None = None,
  to_revision: str | None = None,
  dirs: Union[str, List[str]] | None = None
):
  dirs = dirs or getcwd()
  from_revision = from_revision or git_get_initial_commit_hash()
  to_revision = to_revision or git_get_current_commit_hash()
  return get_lines(
    run(f"git diff --name-only '{from_revision}' '{to_revision}' -- {prepare_paths_args(dirs)}")
  )


def git_check_tag(tag: str):
  try:
    return run(f"git check-ref-format 'tags/{tag}'")
  except Exception as e:
    raise ValueError(
      f"Invalid git tag format: '{tag}'. See: https://git-scm.com/docs/git-check-ref-format") from e


def git_add_all():
  return run("git add -A")


def git_commit(commit_message: str):
  try:
    run(f"git commit -q -m {shlex.quote(commit_message)}")
  except ValueError as e:
    if "nothing to commit, working tree clean" in str(e):
      logger.info("nothing to commit, working tree clean")
    else:
      raise e


def git_push():
  run("git push -q")


def git_pull():
  run("git pull -q")


def git_commit_all(commit_message: str):
  git_add_all()
  git_commit(commit_message)
  return git_get_current_commit_hash()


def git_commit_and_push(commit_message):
  commit_hash = git_commit_all(commit_message)
  git_push()
  return commit_hash


def github_create_release(repo: str, version: str, commit_hash: str, release_notes: str, files=None):
  if files is None:
    files = []
  files = " ".join(shlex.quote(f) for f in files)
  run(
    f"""
    gh release create \
      {shlex.quote(version)} \
      --repo {shlex.quote(repo)} \
      --title {shlex.quote(version)} \
      --target {shlex.quote(commit_hash)} \
      --notes-file - \
      {files}
    """,
    stdin=release_notes
  )
