from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Severity(str, Enum):
  DEBUG = "debug"
  INFO = "info"
  NOTICE = "notice"
  WARNING = "warning"
  ERROR = "error"

  def rank(self) -> int:
    order = {
      Severity.ERROR: 0,
      Severity.WARNING: 1,
      Severity.NOTICE: 2,
      Severity.INFO: 3,
      Severity.DEBUG: 4,
    }
    return order[self]

  def label(self) -> str:
    return self.value.upper()


@dataclass(frozen=True)
class ReportingEvent:
  event_type: str
  severity: Severity
  message: str
  title: str | None = None
  stage: str | None = None
  dataset_path: str | None = None
  filepath: str | None = None
  line: int | None = None
  column: int | None = None
  code: str | None = None
  details: dict[str, Any] = field(default_factory=dict)

  def to_dict(self) -> dict[str, Any]:
    return {
      "type": self.event_type,
      "severity": self.severity.value,
      "message": self.message,
      "title": self.title,
      "stage": self.stage,
      "dataset_path": self.dataset_path,
      "filepath": self.filepath,
      "line": self.line,
      "column": self.column,
      "code": self.code,
      "details": self.details,
    }


@dataclass(frozen=True)
class DefectFinding:
  severity: Severity
  code: str
  title: str
  problem: str
  impact: str
  dataset_path: str
  filepath: str
  line: int | None = None
  column: int | None = None
  json_path: str | None = None
  migration: str | None = None
  recommended_action: str | None = None
  upstream_action: str | None = None
  source: str = "dataset-validator"
  details: dict[str, Any] = field(default_factory=dict)

  def message(self) -> str:
    parts = [f"{self.problem}.", f"{self.impact}."]
    if self.migration:
      parts.append(f"Run {self.migration}.")
    if self.recommended_action:
      parts.append(f"{self.recommended_action}.")
    if self.upstream_action:
      parts.append(f"{self.upstream_action}.")
    return " ".join(parts)

  def to_event(self) -> ReportingEvent:
    return ReportingEvent(
      event_type="defect_found",
      severity=self.severity,
      title=self.title,
      message=self.message(),
      dataset_path=self.dataset_path,
      filepath=self.filepath,
      line=self.line,
      column=self.column,
      code=self.code,
      details={
        "problem": self.problem,
        "impact": self.impact,
        "migration": self.migration,
        "json_path": self.json_path,
        "recommended_action": self.recommended_action,
        "upstream_action": self.upstream_action,
        "source": self.source,
        **self.details,
      },
    )
