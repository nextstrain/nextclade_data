import json
import unittest
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.lib.reporting import PROJECT_ROOT, Reporter
from scripts.lib.reporting_model import DefectFinding, Severity


class TestReporting(unittest.TestCase):
  def test_reporting_terminal_and_jsonl_summary_counts_findings(self) -> None:
    stdout = StringIO()
    stderr = StringIO()

    with TemporaryDirectory() as tmp_dir:
      report_path = Path(tmp_dir) / "report.jsonl"
      reporter = Reporter(stdout=stdout, stderr=stderr)
      reporter.configure(use_github_actions=False, report_jsonl_path=str(report_path))

      with reporter.stage("Validate datasets"):
        reporter.info("Starting validation")
        reporter.report_defect(
          DefectFinding(
            severity=Severity.NOTICE,
            code="schema.unknown_property",
            title="Schema notice",
            problem="Unknown property 'qc.extraField'",
            impact="Property is ignored by dataset validation",
            dataset_path="nextstrain/test/all",
            filepath="data/nextstrain/test/all/pathogen.json",
            line=12,
            column=3,
            recommended_action="Remove the property or rename it to a supported field",
          )
        )
        reporter.report_defect(
          DefectFinding(
            severity=Severity.WARNING,
            code="schema.misplaced_attribute",
            title="Dataset defect",
            problem="Top-level 'deprecated' should be in 'attributes.deprecated'",
            impact="Field may not be read correctly by Nextclade",
            dataset_path="nextstrain/test/all",
            filepath="data/nextstrain/test/all/pathogen.json",
            line=18,
            column=3,
            migration="migrations/migrate_017_unify_attributes.py",
          )
        )

      reporter.write_outputs()

      stdout_text = stdout.getvalue()
      stderr_text = stderr.getvalue()
      jsonl_lines = [json.loads(line) for line in report_path.read_text(encoding="utf-8").splitlines()]
      summary = jsonl_lines[-1]

      self.assertIn("[stage] Validate datasets", stdout_text)
      self.assertIn(
        "[summary] datasets=1 findings=2 notices=1 warnings=1 errors=0",
        stdout_text,
      )
      self.assertIn(
        "[warning] nextstrain/test/all data/nextstrain/test/all/pathogen.json:18:3 schema.misplaced_attribute",
        stderr_text,
      )
      self.assertEqual("summary", summary["type"])
      self.assertEqual(2, summary["findings_total"])
      self.assertEqual(1, summary["severity_counts"]["notice"])
      self.assertEqual(1, summary["severity_counts"]["warning"])
      self.assertEqual(0, summary["severity_counts"]["error"])

  def test_reporting_github_actions_annotations_and_summary(self) -> None:
    stdout = StringIO()
    stderr = StringIO()

    with TemporaryDirectory() as tmp_dir:
      summary_path = Path(tmp_dir) / "summary.md"
      reporter = Reporter(stdout=stdout, stderr=stderr)
      reporter.configure(use_github_actions=True, step_summary_path=str(summary_path))

      with reporter.stage("Validate datasets"):
        reporter.report_defect(
          DefectFinding(
            severity=Severity.NOTICE,
            code="schema.unknown_property",
            title="Schema notice",
            problem="Unknown property 'qc.extraField'",
            impact="Property is ignored by dataset validation",
            dataset_path="nextstrain/test/all",
            filepath=str(PROJECT_ROOT / "data/nextstrain/test/all/pathogen.json"),
            line=12,
            column=5,
            recommended_action="Remove the property or rename it to a supported field",
          )
        )
        reporter.report_defect(
          DefectFinding(
            severity=Severity.ERROR,
            code="schema.renamed_field",
            title="Dataset defect",
            problem="Field 'qc.frameShifts.ignoreFrameShifts' was renamed to 'ignoredFrameShifts'",
            impact="Frame shift exclusions not applied",
            dataset_path="nextstrain/test/all",
            filepath=str(PROJECT_ROOT / "data/nextstrain/test/all/pathogen.json"),
            line=24,
            column=5,
            migration="migrations/migrate_010_rename_ignore_frame_shifts.py",
          )
        )

      reporter.write_outputs()

      gha_text = stdout.getvalue()
      summary_text = summary_path.read_text(encoding="utf-8")

      self.assertIn("::group::Validate datasets", gha_text)
      self.assertIn(
        "::notice file=data/nextstrain/test/all/pathogen.json,line=12,col=5,title=Schema notice::Unknown property 'qc.extraField'. Property is ignored by dataset validation. Remove the property or rename it to a supported field.",
        gha_text,
      )
      self.assertIn(
        "::error file=data/nextstrain/test/all/pathogen.json,line=24,col=5,title=Dataset defect::Field 'qc.frameShifts.ignoreFrameShifts' was renamed to 'ignoredFrameShifts'. Frame shift exclusions not applied. Run migrations/migrate_010_rename_ignore_frame_shifts.py.",
        gha_text,
      )
      self.assertIn("Findings: **2**. Notices: **1**. Warnings: **0**. Errors: **1**.", summary_text)
      self.assertIn("| NOTICE | schema.unknown_property |", summary_text)
      self.assertIn("| ERROR | schema.renamed_field |", summary_text)


if __name__ == "__main__":
  unittest.main()
