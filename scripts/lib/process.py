import subprocess

from .reporting import reporter


def run(command, none_if_empty=False, error_if_empty=False, ignore_errors=False, custom_error_msg=None, stdin=None,
        verbose=False):
  reporter.command_started(command, visible=verbose)

  res = subprocess.run(command, shell=True, check=False, capture_output=True, text=True, input=stdin)
  reporter.command_finished(command, res.returncode, res.stdout.strip(), res.stderr.strip(), visible=verbose)

  if not ignore_errors and res.returncode != 0:
    message = res.stderr.strip() or res.stdout.strip() or custom_error_msg or ''
    detail = f"\n  Message: {message}" if message else ''
    raise ValueError(
      f"The external process failed:\n  Command: {command}\n  Return code: {res.returncode}{detail}")
  stdout = res.stdout.strip()
  if len(stdout) == 0:
    if none_if_empty:
      return None
    if error_if_empty:
      err_detail = res.stderr.strip() or custom_error_msg or ''
      err_msg = f"\n  Message: {err_detail}" if err_detail else ''
      raise ChildProcessError(
        f"Received empty output, while expected non-empty:\n  Command: {command}\n  Return code: {res.returncode}"
        f"{err_msg}")
    return ""
  return stdout
