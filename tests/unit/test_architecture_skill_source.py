"""Semantic source checks for the isolated architecture-audit skill."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = ROOT / "skills" / "playbook-steward-architecture"
SKILL = SKILL_DIR / "SKILL.md"
REFERENCES = (
    SKILL_DIR / "references" / "repository-mapping.md",
    SKILL_DIR / "references" / "findings-and-improvement.md",
)


class ArchitectureSkillSourceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.skill_text = SKILL.read_text(encoding="utf-8")
        self.reference_text = "\n".join(
            reference.read_text(encoding="utf-8") for reference in REFERENCES
        )
        self.all_text = f"{self.skill_text}\n{self.reference_text}"

    def test_frontmatter_is_minimal_and_names_the_skill(self) -> None:
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", self.skill_text, re.DOTALL)
        self.assertIsNotNone(frontmatter)
        lines = frontmatter.group(1).splitlines()
        self.assertEqual([line.split(":", 1)[0] for line in lines], ["name", "description"])
        self.assertEqual(lines[0], "name: playbook-steward-architecture")
        self.assertRegex(lines[1], r'^description: ".+"$')

    def test_runtime_links_are_local_and_exist(self) -> None:
        links = re.findall(r"\[[^]]+\]\(([^)]+)\)", self.skill_text)
        for required_link in (
            "references/repository-mapping.md",
            "references/findings-and-improvement.md",
        ):
            with self.subTest(required_link=required_link):
                self.assertIn(required_link, links)
        for link in links:
            self.assertFalse(link.startswith(("http:", "https:", "/")))
            target = (SKILL.parent / link).resolve()
            self.assertTrue(target.is_relative_to(SKILL_DIR.resolve()))
            self.assertTrue(target.is_file())

    def test_metadata_disables_implicit_invocation(self) -> None:
        metadata = (SKILL_DIR / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertIn('display_name: "Playbook Steward Architecture"', metadata)
        self.assertIn('short_description: "Assess Ansible repository architecture"', metadata)
        self.assertIn("$playbook-steward-architecture", metadata)
        self.assertIn("allow_implicit_invocation: false", metadata)

    def test_content_covers_required_architecture_assessment(self) -> None:
        for concept in (
            "repository type",
            "entry points",
            "responsibility ownership",
            "variable leakage",
            "collection dependencies",
            "duplicated task sequences",
            "execution-environment",
            "best practice",
            "staged improvement plan",
        ):
            with self.subTest(concept=concept):
                self.assertIn(concept, self.all_text.lower())

    def test_content_excludes_specialist_scope(self) -> None:
        exclusions = re.search(
            r"^## Exclusions\n\n(.*?)(?=^## |\Z)",
            self.skill_text,
            re.MULTILINE | re.DOTALL,
        )
        self.assertIsNotNone(exclusions)
        self.assertIn("This skill does not:", exclusions.group(1))
        for excluded in (
            "AAP",
            "AWX",
            "EDA",
            "Windows",
            "network",
            "cloud",
            "Kubernetes",
            "compliance architecture",
        ):
            with self.subTest(excluded=excluded):
                self.assertIn(excluded, exclusions.group(1))

    def test_skill_has_no_monolith_dependency_or_forbidden_structure(self) -> None:
        self.assertNotIn("skill/playbook-steward", self.skill_text)
        expected_files = {
            "SKILL.md",
            "agents/openai.yaml",
            "references/repository-mapping.md",
            "references/findings-and-improvement.md",
        }
        actual_files = {
            path.relative_to(SKILL_DIR).as_posix()
            for path in SKILL_DIR.rglob("*")
            if path.is_file()
        }
        self.assertEqual(actual_files, expected_files)


if __name__ == "__main__":
    unittest.main()
