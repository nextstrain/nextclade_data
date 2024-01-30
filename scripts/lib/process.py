import subprocess


def run(command, none_if_empty=False, error_if_empty=False, ignore_errors=False, custom_error_msg=None, stdin=None,
        verbose=False):
  if verbose:
    print(command)

  res = subprocess.run(command, shell=True, check=False, capture_output=True, text=True, input=stdin)

  message = str(res.stderr) or str(res.stdout) or custom_error_msg
  message = f"\n  Message: {message}" if message else ''

  if not ignore_errors and (res.returncode != 0 or res.stderr):
    raise ValueError(
      f"The external process failed:\n  Command: {command}\n  Return code: {res.returncode}{message}")
  stdout = res.stdout.strip()
  if len(stdout) == 0:
    if none_if_empty:
      return None
    if error_if_empty:
      raise ChildProcessError(
        f"Received empty output, while expected non-empty:\n  Command: {command}\n  Return code: {res.returncode}"
        f"{message}")
    return ""
  return stdout
