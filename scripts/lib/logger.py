from .reporting import reporter


class _LoggerAdapter:
  def debug(self, message: str) -> None:
    reporter.debug(message)

  def info(self, message: str) -> None:
    reporter.info(message)

  def warning(self, message: str) -> None:
    reporter.warning(message)

  def error(self, message: str) -> None:
    reporter.error(message)


logger = _LoggerAdapter()
