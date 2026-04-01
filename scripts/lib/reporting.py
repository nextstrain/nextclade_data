import json
import os
import sys
from collections import defaultdict
from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from typing import IO, Any

from .reporting_model import DefectFinding, ReportingEvent, Severity


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SEVERITY_ORDER = [
  Severity.ERROR,
  Severity.WARNING,
  Severity.NOTICE,
  Severity.INFO,
  Severity.DEBUG,
]


@dataclass
class RunReport:
  events: list[ReportingEvent] = field(default_factory=list)
  defects: list[DefectFinding] = field(default_factory=list)
  datasets_scanned: set[str] = field(default_factory=set)

  def add_event(self, event: ReportingEvent) -> None:
    self.events.append(event)
    if event.dataset_path:
      self.datasets_scanned.add(event.dataset_path)

  def add_defect(self, defect: DefectFinding) -> None:
    self.defects.append(defect)
    self.datasets_scanned.add(defect.dataset_path)
    self.events.append(defect.to_event())

  def severity_counts(self) -> dict[Severity, int]:
    counts = {severity: 0 for severity in SEVERITY_ORDER}
    for defect in self.defects:
      counts[defect.severity] += 1
    return counts

  def defects_by_dataset(self) -> dict[str, list[DefectFinding]]:
    grouped: dict[str, list[DefectFinding]] = defaultdict(list)
    for defect in self.defects:
      grouped[defect.dataset_path].append(defect)
    return dict(grouped)

  def total_findings(self) -> int:
    return len(self.defects)

  def error_count(self) -> int:
    return sum(1 for defect in self.defects if defect.severity == Severity.ERROR)


class Reporter:
  def __init__(self, stdout: IO[str] | None = None, stderr: IO[str] | None = None):
    self.stdout = stdout or sys.stdout
    self.stderr = stderr or sys.stderr
    self.use_github_actions = bool(os.environ.get("GITHUB_ACTIONS"))
    self.step_summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    self.report_jsonl_path: str | None = None
    self.report = RunReport()
    self._renderers: list[_BaseRenderer] = []
    self._refresh_renderers()

  def configure(
    self,
    report_jsonl_path: str | None = None,
    step_summary_path: str | None = None,
    use_github_actions: bool | None = None,
  ) -> None:
    if use_github_actions is not None:
      self.use_github_actions = use_github_actions
    if step_summary_path is not None:
      self.step_summary_path = step_summary_path
    self.report_jsonl_path = report_jsonl_path
    self._refresh_renderers()

  def reset(self) -> None:
    self._close_renderers()
    self.report = RunReport()
    self._refresh_renderers()

  def info(self, message: str, **fields: Any) -> None:
    self._emit_event("log_message", Severity.INFO, message, **fields)

  def notice(self, message: str, **fields: Any) -> None:
    self._emit_event("log_message", Severity.NOTICE, message, **fields)

  def warning(self, message: str, **fields: Any) -> None:
    self._emit_event("log_message", Severity.WARNING, message, **fields)

  def error(self, message: str, **fields: Any) -> None:
    self._emit_event("log_message", Severity.ERROR, message, **fields)

  def debug(self, message: str, **fields: Any) -> None:
    self._emit_event("log_message", Severity.DEBUG, message, **fields)

  def stage_start(self, stage: str) -> None:
    self._emit_event("stage_started", Severity.INFO, stage, stage=stage, title=stage)

  def stage_finish(self, stage: str, status: str = "ok") -> None:
    self._emit_event(
      "stage_finished",
      Severity.INFO,
      f"{stage} ({status})",
      stage=stage,
      title=stage,
      details={"status": status},
    )

  @contextmanager
  def stage(self, stage: str):
    self.stage_start(stage)
    try:
      yield
      self.stage_finish(stage, "ok")
    except Exception:
      self.stage_finish(stage, "error")
      raise

  def dataset_start(self, dataset_path: str) -> None:
    self._emit_event(
      "dataset_started",
      Severity.INFO,
      dataset_path,
      dataset_path=dataset_path,
      title=dataset_path,
    )

  def dataset_finish(self, dataset_path: str, status: str = "ok") -> None:
    self._emit_event(
      "dataset_finished",
      Severity.INFO,
      f"{dataset_path} ({status})",
      dataset_path=dataset_path,
      title=dataset_path,
      details={"status": status},
    )

  def command_started(self, command: str, visible: bool = False) -> None:
    self._emit_event(
      "command_started",
      Severity.INFO,
      command,
      title="command",
      details={"command": command, "visible": visible},
    )

  def command_finished(
    self,
    command: str,
    returncode: int,
    stdout: str,
    stderr: str,
    visible: bool = False,
  ) -> None:
    severity = Severity.ERROR if returncode != 0 else Severity.INFO
    self._emit_event(
      "command_finished",
      severity,
      command,
      title="command",
      details={
        "command": command,
        "returncode": returncode,
        "stdout_preview": _preview(stdout),
        "stderr_preview": _preview(stderr),
        "visible": visible,
      },
    )

  def report_defect(self, defect: DefectFinding) -> None:
    self.report.add_defect(defect)
    for renderer in self._renderers:
      renderer.handle_event(defect.to_event())

  def write_outputs(self) -> None:
    for renderer in self._renderers:
      renderer.finalize(self.report)
    self._close_renderers()

  def error_count(self) -> int:
    return self.report.error_count()

  def _emit_event(
    self,
    event_type: str,
    severity: Severity,
    message: str,
    **fields: Any,
  ) -> None:
    event = ReportingEvent(event_type=event_type, severity=severity, message=message, **fields)
    self.report.add_event(event)
    for renderer in self._renderers:
      renderer.handle_event(event)

  def _refresh_renderers(self) -> None:
    self._close_renderers()
    if self.use_github_actions:
      self._renderers = [_GithubActionsRenderer(self.stdout, self.step_summary_path)]
    else:
      self._renderers = [_TerminalRenderer(self.stdout, self.stderr)]
    if self.report_jsonl_path:
      self._renderers.append(_JsonlRenderer(self.report_jsonl_path))

  def _close_renderers(self) -> None:
    for renderer in self._renderers:
      renderer.close()
    self._renderers = []


class _BaseRenderer:
  def handle_event(self, event: ReportingEvent) -> None:
    raise NotImplementedError

  def finalize(self, report: RunReport) -> None:
    return None

  def close(self) -> None:
    return None


class _TerminalRenderer(_BaseRenderer):
  def __init__(self, stdout: IO[str], stderr: IO[str]):
    self.stdout = stdout
    self.stderr = stderr

  def handle_event(self, event: ReportingEvent) -> None:
    if event.event_type == "stage_started":
      self._write_stdout(f"[stage] {event.stage}")
      return

    if event.event_type == "log_message":
      self._write_message(event)
      return

    if event.event_type == "command_started" and event.details.get("visible"):
      self._write_stdout(f"[command] {event.details['command']}")
      return

    if event.event_type == "command_finished" and (
      event.details.get("visible") or event.details.get("returncode", 0) != 0
    ):
      returncode = event.details.get("returncode", 0)
      prefix = "error" if returncode != 0 else "command"
      target = self.stderr if returncode != 0 else self.stdout
      target.write(f"[{prefix}] {event.details['command']} (rc={returncode})\n")
      target.flush()
      return

    if event.event_type == "defect_found":
      self._write_defect(event)

  def finalize(self, report: RunReport) -> None:
    if not report.defects:
      return

    counts = report.severity_counts()
    self._write_stdout("")
    self._write_stdout("[summary] dataset defects")
    self._write_stdout(
      "[summary] "
      f"datasets={len(report.datasets_scanned)} findings={report.total_findings()} "
      f"notices={counts[Severity.NOTICE]} warnings={counts[Severity.WARNING]} errors={counts[Severity.ERROR]}"
    )

    for dataset_path in sorted(report.defects_by_dataset().keys()):
      defects = sorted(
        report.defects_by_dataset()[dataset_path],
        key=lambda defect: (defect.severity.rank(), defect.filepath, defect.line or 0, defect.code),
      )
      self._write_stdout(f"[dataset] {dataset_path}")
      for defect in defects:
        location = _format_location(defect.filepath, defect.line, defect.column)
        self._write_stdout(
          f"  [{defect.severity.value}] {location} {defect.code} {defect.problem}"
        )

  def _write_message(self, event: ReportingEvent) -> None:
    message = f"[{event.severity.value}] {event.message}"
    if event.severity in {Severity.WARNING, Severity.ERROR}:
      self.stderr.write(message + "\n")
      self.stderr.flush()
      return
    self._write_stdout(message)

  def _write_defect(self, event: ReportingEvent) -> None:
    location = _format_location(event.filepath, event.line, event.column)
    message = f"[{event.severity.value}] {event.dataset_path} {location} {event.code} {event.details['problem']}"
    target = self.stderr if event.severity in {Severity.WARNING, Severity.ERROR} else self.stdout
    target.write(message + "\n")
    target.flush()

  def _write_stdout(self, message: str) -> None:
    self.stdout.write(message + "\n")
    self.stdout.flush()


class _GithubActionsRenderer(_BaseRenderer):
  def __init__(self, stdout: IO[str], step_summary_path: str | None):
    self.stdout = stdout
    self.step_summary_path = step_summary_path
    self.group_stack: list[str] = []

  def handle_event(self, event: ReportingEvent) -> None:
    if event.event_type == "stage_started":
      self._write_line(f"::group::{_escape_message(event.stage or event.message)}")
      self.group_stack.append(event.stage or event.message)
      return

    if event.event_type == "stage_finished":
      if self.group_stack:
        self.group_stack.pop()
        self._write_line("::endgroup::")
      return

    if event.event_type == "log_message":
      self._write_line(f"[{event.severity.value}] {event.message}")
      return

    if event.event_type == "command_started" and event.details.get("visible"):
      self._write_line(f"[command] {event.details['command']}")
      return

    if event.event_type == "command_finished" and (
      event.details.get("visible") or event.details.get("returncode", 0) != 0
    ):
      returncode = event.details.get("returncode", 0)
      self._write_line(f"[command] {event.details['command']} (rc={returncode})")
      return

    if event.event_type == "defect_found":
      self._write_annotation(event)

  def finalize(self, report: RunReport) -> None:
    while self.group_stack:
      self.group_stack.pop()
      self._write_line("::endgroup::")

    if self.step_summary_path:
      with open(self.step_summary_path, "a", encoding="utf-8") as summary_file:
        summary_file.write(_render_markdown_summary(report))

  def _write_annotation(self, event: ReportingEvent) -> None:
    if event.severity not in {Severity.NOTICE, Severity.WARNING, Severity.ERROR}:
      self._write_line(f"[{event.severity.value}] {event.message}")
      return

    props = {}
    if event.filepath:
      props["file"] = _relative_path(event.filepath)
    if event.line is not None:
      props["line"] = str(event.line)
    if event.column is not None:
      props["col"] = str(event.column)
    if event.title:
      props["title"] = event.title
    props_str = ",".join(f"{key}={_escape_property(val)}" for key, val in props.items())
    command = event.severity.value
    prefix = f"::{command}"
    if props_str:
      prefix += f" {props_str}"
    prefix += "::"
    self._write_line(prefix + _escape_message(event.message))

  def _write_line(self, message: str) -> None:
    self.stdout.write(message + "\n")
    self.stdout.flush()


class _JsonlRenderer(_BaseRenderer):
  def __init__(self, path: str):
    self.file = open(path, "w", encoding="utf-8")

  def handle_event(self, event: ReportingEvent) -> None:
    self.file.write(json.dumps(event.to_dict(), ensure_ascii=False) + "\n")
    self.file.flush()

  def finalize(self, report: RunReport) -> None:
    summary = {
      "type": "summary",
      "datasets_scanned": len(report.datasets_scanned),
      "findings_total": report.total_findings(),
      "severity_counts": {
        severity.value: count for severity, count in report.severity_counts().items()
      },
      "error_count": report.error_count(),
    }
    self.file.write(json.dumps(summary, ensure_ascii=False) + "\n")
    self.file.flush()

  def close(self) -> None:
    self.file.close()


def _relative_path(filepath: str | None) -> str | None:
  if filepath is None:
    return None
  path = Path(filepath)
  if not path.is_absolute():
    return filepath
  try:
    return str(path.resolve().relative_to(PROJECT_ROOT))
  except ValueError:
    return str(path)


def _format_location(filepath: str | None, line: int | None, column: int | None) -> str:
  relative = _relative_path(filepath)
  if relative is None:
    return "(no-file)"
  if line is None:
    return relative
  if column is None:
    return f"{relative}:{line}"
  return f"{relative}:{line}:{column}"


def _preview(text: str, max_len: int = 400) -> str:
  if len(text) <= max_len:
    return text
  return text[: max_len - 3] + "..."


def _escape_property(value: str) -> str:
  return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A").replace(":", "%3A").replace(",", "%2C")


def _escape_message(value: str) -> str:
  return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def _render_markdown_summary(report: RunReport) -> str:
  if not report.defects:
    return ""

  counts = report.severity_counts()
  lines = [
    "## Dataset Validation Results",
    "",
    f"Datasets scanned: **{len(report.datasets_scanned)}**",
    "",
    f"Findings: **{report.total_findings()}**. Notices: **{counts[Severity.NOTICE]}**. Warnings: **{counts[Severity.WARNING]}**. Errors: **{counts[Severity.ERROR]}**.",
    "",
    "| Severity | Code | Dataset | File | Problem | Impact | Migration |",
    "|----------|------|---------|------|---------|--------|-----------|",
  ]

  sorted_defects = sorted(
    report.defects,
    key=lambda defect: (defect.severity.rank(), defect.dataset_path, defect.filepath, defect.line or 0, defect.code),
  )
  for defect in sorted_defects:
    filepath = _relative_path(defect.filepath) or ""
    line = f":{defect.line}" if defect.line is not None else ""
    migration = defect.migration or ""
    lines.append(
      "| "
      f"{defect.severity.label()} | "
      f"{_escape_markdown(defect.code)} | "
      f"{_escape_markdown(defect.dataset_path)} | "
      f"{_escape_markdown(filepath + line)} | "
      f"{_escape_markdown(defect.problem)} | "
      f"{_escape_markdown(defect.impact)} | "
      f"{_escape_markdown(migration)} |"
    )

  lines.extend(
    [
      "",
      "Run migration scripts locally where applicable.",
      "",
    ]
  )
  return "\n".join(lines)


def _escape_markdown(value: str) -> str:
  return value.replace("|", "\\|")


reporter = Reporter()
