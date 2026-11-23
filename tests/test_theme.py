import json
import unittest
from pathlib import Path

import tinycss2


ROOT = Path(__file__).resolve().parents[1]
STYLESHEET = (ROOT / "theme.css").read_text(encoding="utf-8")


def contrast(first, second):
    def luminance(color):
        channels = [int(color[index:index + 2], 16) / 255 for index in (1, 3, 5)]
        linear = [
            channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
            for channel in channels
        ]
        return sum(component * weight for component, weight in zip(linear, (0.2126, 0.7152, 0.0722)))

    darker, lighter = sorted((luminance(first), luminance(second)))
    return (lighter + 0.05) / (darker + 0.05)


class ThemeTest(unittest.TestCase):
    def setUp(self):
        self.rules = {}
        for rule in tinycss2.parse_stylesheet(STYLESHEET, skip_comments=True, skip_whitespace=True):
            self.assertEqual(rule.type, "qualified-rule")
            selector = tinycss2.serialize(rule.prelude).strip()
            declarations = tinycss2.parse_declaration_list(
                rule.content, skip_comments=True, skip_whitespace=True
            )
            for declaration in declarations:
                self.assertEqual(declaration.type, "declaration", selector)
            self.rules[selector] = {
                declaration.name: tinycss2.serialize(declaration.value).strip()
                for declaration in declarations
            }

    def test_heading_spacing_matches_in_reading_and_editing(self):
        for view in (".markdown-rendered", ".markdown-source-view"):
            variables = {
                name: value
                for selector, declarations in self.rules.items()
                if view in [part.strip() for part in selector.split(",")]
                for name, value in declarations.items()
            }
            for level in range(1, 7):
                with self.subTest(view=view, heading=level):
                    self.assertEqual(variables.get(f"--h{level}-line-height"), "1.25")
        for selector, declarations in self.rules.items():
            if selector.startswith(".markdown-rendered") and "line-height" in declarations:
                self.fail("Use Obsidian's heading variables so user snippets can override them.")

    def test_list_markers_follow_obsidian_colors_and_states(self):
        self.assertEqual(self.rules["body"].get("--list-marker-color"), "var(--text-muted)")
        for selector, declarations in self.rules.items():
            if ".list-bullet" in selector:
                self.assertNotIn("background-color", declarations, selector)

    def test_note_text_and_list_marker_contrast_in_both_modes(self):
        for mode in ("light", "dark"):
            colors = self.rules[f"body.theme-{mode}"]
            background = colors["--background-primary"]
            for role in ("--text-normal", "--text-muted", "--link-color", "--link-external-color"):
                with self.subTest(mode=mode, role=role):
                    self.assertGreaterEqual(contrast(colors[role], background), 4.5)

    def test_source_version_matches_manifest(self):
        version = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))["version"]
        self.assertRegex(version, r"^\d+\.\d+\.\d+$")
        self.assertIn(f"Readable Typography {version}.", STYLESHEET.splitlines()[0])
        self.assertIn(f"Source version {version}.", (ROOT / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
