import logging
import os
import re
import sys
from pathlib import Path

PROJECT_ROOT_STR = str(Path(__file__).resolve().parent.parent.parent)


def _colors_enabled() -> bool:
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("GITHUB_ACTIONS"):
        return True
    return sys.stderr.isatty()


class _ColorFormatter(logging.Formatter):
    GREY = "\033[90m"
    RESET = "\033[0m"
    LEVEL_COLORS = {
        logging.DEBUG: "\033[36m",     # cyan
        logging.INFO: "\033[32m",      # green
        logging.WARNING: "\033[33m",   # yellow
        logging.ERROR: "\033[31m",     # red
        logging.CRITICAL: "\033[35m",  # magenta
    }

    def __init__(self, use_colors: bool):
        super().__init__()
        self._use_colors = use_colors
        # Match absolute paths, optionally followed by :line or :line:col
        self._path_pattern = re.compile(
            re.escape(PROJECT_ROOT_STR) + r"/([^\s:]+(?::\d+(?::\d+)?)?)"
        )

    def _transform_paths(self, message: str) -> str:
        if self._use_colors:
            return self._path_pattern.sub(
                lambda m: f"{self.GREY}{m.group(1)}{self.RESET}", message
            )
        return self._path_pattern.sub(r"\1", message)

    def format(self, record: logging.LogRecord) -> str:
        message = self._transform_paths(record.getMessage())
        if self._use_colors:
            color = self.LEVEL_COLORS.get(record.levelno, "")
            return f"{color}{record.levelname}{self.RESET}: {message}"
        return f"{record.levelname}: {message}"


def _setup_logger() -> logging.Logger:
    logger = logging.getLogger("rebuild")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(_ColorFormatter(_colors_enabled()))
    logger.addHandler(handler)

    return logger


logger = _setup_logger()
