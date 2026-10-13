from pathlib import Path
import re
import unittest

ROOT=Path(__file__).resolve().parents[1]

class PackageTests(unittest.TestCase):
    def test_local_markdown_targets(self):
        for file in ROOT.rglob('*.md'):
            if '.git' in file.parts:continue
            for target in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf-8-sig')):
                if '://' in target or target.startswith('#'):continue
                with self.subTest(file=str(file.relative_to(ROOT)),target=target):
                    self.assertTrue((file.parent/target.split('#')[0]).exists())

    def test_translation_coverage(self):
        for lang in ['pt','es']:
            for name in ['SKILL.md','engineering-manual.md','standards-register.md',
                         'jurisdiction-annex.md','project-dossier.md','software-and-case.md','example-and-sources.md']:
                self.assertTrue((ROOT/'translations'/lang/name).is_file())

if __name__=='__main__':unittest.main()
