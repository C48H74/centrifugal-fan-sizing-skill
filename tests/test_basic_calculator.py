import json
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT=Path(__file__).resolve().parents[1]/'scripts/calcular.py'

class BasicCalculatorTests(unittest.TestCase):
    def command(self):
        return [sys.executable,str(SCRIPT),'--flow-m3h','12000','--pressure','180','--unit','mmca',
                '--pressure-basis','total','--efficiency-basis','total','--efficiency','0.72']

    def test_publication_example(self):
        r=json.loads(subprocess.check_output(self.command()))
        self.assertAlmostEqual(r['pressure_Pa'],1765.197)
        self.assertAlmostEqual(r['shaft_power_kW'],8.172208333333334)

    def test_invalid_efficiency(self):
        cmd=self.command();cmd[-1]='72'
        self.assertNotEqual(subprocess.run(cmd,capture_output=True).returncode,0)

    def test_mismatched_bases(self):
        cmd=self.command();cmd[cmd.index('--efficiency-basis')+1]='static'
        self.assertNotEqual(subprocess.run(cmd,capture_output=True).returncode,0)

    def test_portuguese_compatibility(self):
        cmd=[sys.executable,str(SCRIPT),'--vazao-m3h','12000','--pressao','180','--unidade','mmca',
             '--base-pressao','estatica','--base-eficiencia','estatica','--eficiencia','0.72']
        r=json.loads(subprocess.check_output(cmd))
        self.assertEqual(r['basis'],'static')
        self.assertAlmostEqual(r['shaft_power_kW'],8.172208333333334)

if __name__=='__main__':unittest.main()
