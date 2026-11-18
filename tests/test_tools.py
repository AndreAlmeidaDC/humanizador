"""Casos sintéticos de preservação Unicode e geração do prompt portátil."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


audit_unicode = load_script("audit_unicode")
build_prompt = load_script("build_prompt")


class UnicodeAuditTests(unittest.TestCase):
    def run_cli(self, *arguments, data=None):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts/audit_unicode.py"), *arguments],
            input=data, capture_output=True, check=False,
        )

    def test_empty_and_plain_text(self):
        for text in ("", "Texto sintético em português.\nSegunda linha."):
            with self.subTest(text=text):
                report = audit_unicode.audit_text(text)
                self.assertEqual(report["total_codepoints"], len(text))
                self.assertEqual(report["total_flagged_codepoints"], 0)
                self.assertEqual(report["findings"], [])

    def test_exact_counts_and_no_plaintext_in_report(self):
        text = "CONTEUDO_SINTETICO_PRIVADO\u200b\u200b\u00a0\ufeff"
        report = audit_unicode.audit_text(text)
        counts = {item["codepoint"]: item["count"] for item in report["findings"]}
        self.assertEqual(counts, {"U+00A0": 1, "U+200B": 2, "U+FEFF": 1})
        self.assertEqual(report["total_flagged_codepoints"], 4)
        self.assertNotIn("CONTEUDO_SINTETICO_PRIVADO", json.dumps(report))
        self.assertTrue(all(item["action"] == "review" for item in report["findings"]))

    def test_file_bytes_preserved_for_legitimate_sequences(self):
        # Família com ZWJ, bandeira com tags, variação matemática, CJK e persa.
        text = "👩\u200d👩\u200d👧\u200d👦 🏴\U000e0067\U000e0062\U000e0065\U000e006e\U000e0067\U000e007f ∪\ufe00 一\U000e0100 می\u200cروم\r\n"
        raw = text.encode("utf-8")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "synthetic.txt"
            path.write_bytes(raw)
            result = self.run_cli("--input", str(path))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(path.read_bytes(), raw)
        report = json.loads(result.stdout)
        self.assertEqual(report["total_codepoints"], len(text))
        counts = {item["codepoint"]: item["count"] for item in report["findings"]}
        self.assertEqual(counts["U+200D"], 3)
        self.assertEqual(counts["U+200C"], 1)
        self.assertEqual(counts["U+FE00"], 1)
        self.assertEqual(counts["U+E0100"], 1)
        self.assertEqual(counts["U+E0067"], 2)
        self.assertEqual(counts["U+E007F"], 1)

    def test_bom_and_separators_are_not_silently_discarded(self):
        result = self.run_cli(data="\ufeffA\r\nB\u2028C\u2029".encode("utf-8"))
        self.assertEqual(result.returncode, 0)
        report = json.loads(result.stdout)
        self.assertEqual(report["total_codepoints"], 8)
        self.assertEqual(report["total_flagged_codepoints"], 3)

    def test_non_utf8_fails_without_echoing_input(self):
        result = self.run_cli(data=b"synthetic-secret\xff")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, b"")
        self.assertIn(b"UTF-8", result.stderr)
        self.assertNotIn(b"synthetic-secret", result.stderr)

    def test_missing_input_is_error_not_empty_success(self):
        with tempfile.TemporaryDirectory() as directory:
            result = self.run_cli("--input", str(Path(directory) / "absent.txt"))
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, b"")

    def test_review_inventory_covers_required_ranges(self):
        text = "\u061c\u180e\u202a\u202e\u2066\u2069\ufe0f\U000e01ef\U000e0001\u2060\u00ad\u2009\u200a\u202f"
        report = audit_unicode.audit_text(text)
        self.assertEqual(report["total_flagged_codepoints"], len(text))
        self.assertEqual(report["distinct_flagged_codepoints"], len(text))


class PromptBuildTests(unittest.TestCase):
    CORE = "---\nname: humanizador\ndescription: Synthetic test.\n---\n\n# Humanizador 4.0.0\n\n## Origin version check\n\nFetch upstream.\n\nAutor: André Almeida  \nLicença: MIT\n\n## Papel\nPreservar o sentido.\n"

    def run_cli(self, root, *arguments):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts/build_prompt.py"), "--root", str(root), *arguments],
            capture_output=True, check=False,
        )

    def test_strip_only_technical_metadata_and_keep_author(self):
        result = build_prompt.strip_skill_metadata(self.CORE)
        self.assertNotIn("name: humanizador", result)
        self.assertNotIn("Origin version check", result)
        self.assertNotIn("Fetch upstream.", result)
        self.assertIn("Autor: André Almeida", result)
        self.assertIn("Licença: MIT", result)
        self.assertIn("## Papel\nPreservar o sentido.", result)

    def test_example_heading_inside_fence_is_not_removed(self):
        text = "# Exemplo\n```markdown\n## Origin version check\nExemplo literal.\n```\n## Papel\nEditorial.\n"
        self.assertEqual(build_prompt.strip_skill_metadata(text), text)

    def test_heading_inside_version_check_fence_is_not_boundary(self):
        text = "# Título\n## Origin version check\n~~~text\n## Exemplo de seção\n~~~\nAinda técnico.\n## Papel\nEditorial.\n"
        result = build_prompt.strip_skill_metadata(text)
        self.assertNotIn("Ainda técnico", result)
        self.assertNotIn("Exemplo de seção", result)
        self.assertIn("## Papel\nEditorial.", result)

    def test_module_order_and_exclusion_of_operational_references(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "SKILL.md").write_text(self.CORE, encoding="utf-8")
            (root / "references").mkdir()
            for filename in ("visual", "unicode", "texto", "version-check", "sources", "research"):
                (root / "references" / f"{filename}.md").write_text(f"# Fixture {filename}\nConteúdo sintético.", encoding="utf-8")
            result = build_prompt.render_prompt(root)
            self.assertLess(result.index("# Fixture texto"), result.index("# Fixture visual"))
            self.assertLess(result.index("# Fixture visual"), result.index("# Fixture unicode"))
            for excluded in ("version-check", "sources", "research"):
                self.assertNotIn(f"# Fixture {excluded}", result)
            self.assertIn("Selecionar somente os módulos pertinentes", result)

    def test_check_never_writes_and_detects_drift(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "SKILL.md"
            source.write_text(self.CORE, encoding="utf-8")
            output = root / "HUMANIZADOR.md"
            result = self.run_cli(root, "--check")
            self.assertEqual(result.returncode, 1)
            self.assertFalse(output.exists())
            self.assertEqual(self.run_cli(root).returncode, 0)
            generated = output.read_bytes()
            self.assertEqual(self.run_cli(root, "--check").returncode, 0)
            source.write_text(self.CORE + "\nRegra nova.\n", encoding="utf-8")
            self.assertEqual(self.run_cli(root, "--check").returncode, 1)
            self.assertEqual(output.read_bytes(), generated)

    def test_broken_frontmatter_fails_without_replacing_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "SKILL.md").write_text("---\nname: humanizador\n", encoding="utf-8")
            output = root / "HUMANIZADOR.md"
            output.write_bytes(b"preserve this synthetic file")
            self.assertEqual(self.run_cli(root).returncode, 2)
            self.assertEqual(output.read_bytes(), b"preserve this synthetic file")


if __name__ == "__main__":
    unittest.main()
