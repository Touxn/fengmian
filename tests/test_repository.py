from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "fengmian"


class RepositoryTests(unittest.TestCase):
    def test_plugin_manifest(self) -> None:
        manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text())
        self.assertEqual(manifest["name"], "fengmian")
        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(manifest["skills"], "./skills/")

    def test_skill_frontmatter(self) -> None:
        text = (SKILL / "SKILL.md").read_text()
        self.assertTrue(text.startswith("---\n"))
        self.assertIn("\nname: fengmian\n", text)
        self.assertIn("\ndescription:", text)

    def test_references_exist(self) -> None:
        text = (SKILL / "SKILL.md").read_text()
        paths = re.findall(r"`(references/[^`]+\.md)`", text)
        self.assertGreaterEqual(len(paths), 6)
        for relative in paths:
            self.assertTrue((SKILL / relative).is_file(), relative)

    def test_no_sensitive_or_machine_local_content(self) -> None:
        forbidden = (
            "/" + "Users" + "/",
            "/" + "private" + "/",
            "person" + "-reference",
            "Work" + "Buddy",
            "Cloud" + "Base",
            "腾" + "讯",
            "秋" + "芝",
            "tou" + "xn",
        )
        suffixes = {".md", ".json", ".yaml", ".yml", ".py", ".svg", ".txt"}
        for path in ROOT.rglob("*"):
            if path == Path(__file__) or not path.is_file() or path.suffix.lower() not in suffixes:
                continue
            text = path.read_text(errors="replace")
            for value in forbidden:
                self.assertNotIn(value, text, f"{value!r} found in {path}")

    def test_no_raster_or_font_assets(self) -> None:
        forbidden = {".jpg", ".jpeg", ".png", ".webp", ".ttf", ".otf", ".ttc"}
        found = [path for path in ROOT.rglob("*") if path.suffix.lower() in forbidden]
        self.assertEqual(found, [])

    def test_dimension_checker(self) -> None:
        width, height = 3, 2
        raw = b"".join(b"\x00" + b"\x00\x00\x00" * width for _ in range(height))

        def chunk(kind: bytes, data: bytes) -> bytes:
            payload = kind + data
            return (
                len(data).to_bytes(4, "big")
                + payload
                + (zlib.crc32(payload) & 0xFFFFFFFF).to_bytes(4, "big")
            )

        png = (
            b"\x89PNG\r\n\x1a\n"
            + chunk(b"IHDR", width.to_bytes(4, "big") + height.to_bytes(4, "big") + b"\x08\x02\x00\x00\x00")
            + chunk(b"IDAT", zlib.compress(raw))
            + chunk(b"IEND", b"")
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "test.png"
            path.write_bytes(png)
            result = subprocess.run(
                [
                    sys.executable,
                    str(SKILL / "scripts" / "check_png_dimensions.py"),
                    str(path),
                    "--width",
                    str(width),
                    "--height",
                    str(height),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("3x2", result.stdout)


if __name__ == "__main__":
    unittest.main()
