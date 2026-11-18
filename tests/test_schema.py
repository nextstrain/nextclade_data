import unittest

from scripts.lib.schema import parse_workflow_repo


def readme_with_workflow(value: str) -> str:
  return (
    "# Dataset\n\n"
    "| Key      | Value |\n"
    "| -------- | ----- |\n"
    "| name     | Example virus |\n"
    f"| workflow | {value} |\n"
    "| authors  | [Example Lab](https://github.com/example-lab) |\n"
  )


class TestParseWorkflowRepo(unittest.TestCase):
  def test_returns_repo_of_workflow_url_with_subdirectory(self) -> None:
    readme = readme_with_workflow("https://github.com/nextstrain/measles/tree/main/nextclade")
    self.assertEqual(parse_workflow_repo(readme), "nextstrain/measles")

  def test_returns_repo_of_autolink(self) -> None:
    readme = readme_with_workflow("<https://github.com/hodcroftlab/nextclade-yellow-fever>")
    self.assertEqual(parse_workflow_repo(readme), "hodcroftlab/nextclade-yellow-fever")

  def test_returns_repo_of_markdown_link(self) -> None:
    readme = readme_with_workflow("[github.com/nextstrain/rsv](https://github.com/nextstrain/rsv)")
    self.assertEqual(parse_workflow_repo(readme), "nextstrain/rsv")

  def test_strips_git_suffix(self) -> None:
    readme = readme_with_workflow("https://github.com/enterovirus-phylo/nextclade_d68.git")
    self.assertEqual(parse_workflow_repo(readme), "enterovirus-phylo/nextclade_d68")

  def test_returns_none_when_readme_has_no_workflow_row(self) -> None:
    readme = "# Dataset\n\n| name | Example virus |\n| authors | [Example Lab](https://github.com/example-lab) |\n"
    self.assertIsNone(parse_workflow_repo(readme))

  def test_returns_none_when_workflow_is_not_on_github(self) -> None:
    readme = readme_with_workflow("https://gitlab.com/example-lab/pipeline")
    self.assertIsNone(parse_workflow_repo(readme))


if __name__ == "__main__":
  unittest.main()
