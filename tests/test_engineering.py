"""Numerical invariants and failure modes; run python -m unittest discover -s tests -v."""
import copy
import importlib.util
import json
import math
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('engineering',ROOT/'scripts/engineering.py')
eng=importlib.util.module_from_spec(spec)
spec.loader.exec_module(eng)

class EngineeringTests(unittest.TestCase):
    def setUp(self):
        self.case=json.loads((ROOT/'examples/industrial-case.json').read_text(encoding='utf-8'))

    def test_laminar(self):
        self.assertAlmostEqual(eng.friction_factor(1000,0)[0],0.064)

    def test_colebrook_residual(self):
        f,_=eng.friction_factor(100000,0.0002)
        residual=1/math.sqrt(f)+2*math.log10(0.0002/3.7+2.51/(100000*math.sqrt(f)))
        self.assertLess(abs(residual),1e-10)

    def test_transition_rejected(self):
        with self.assertRaises(ValueError):eng.friction_factor(3000,0)

    def test_segment_hand_calculation(self):
        s=dict(id='hand',length_m=2,diameter_m=0.1,roughness_m=0,K_sum=2,source='test')
        rho,mu,v=1,0.001,1
        q=math.pi*0.1**2/4*v
        r=eng.duct_loss(q,rho,mu,s)
        self.assertAlmostEqual(r['total_loss_Pa'],(0.64*20+2)*0.5)

    def test_analytical_intersection(self):
        points=[dict(flow_m3s=0,pressure_Pa=100,shaft_power_kW=1),dict(flow_m3s=10,pressure_Pa=0,shaft_power_kW=2)]
        roots=eng.intersections(points,0,1)
        self.assertEqual(len(roots),1)
        self.assertAlmostEqual(roots[0]['flow_m3s'],(-10+math.sqrt(500))/2)

    def test_multiple_roots_inside_one_interval(self):
        points=[dict(flow_m3s=0,pressure_Pa=0,shaft_power_kW=1),dict(flow_m3s=4,pressure_Pa=16,shaft_power_kW=2)]
        roots=eng.intersections(points,3,1)
        self.assertEqual([round(r['flow_m3s'],8) for r in roots],[1,3])

    def test_no_extrapolation(self):
        points=[dict(flow_m3s=0,pressure_Pa=100,shaft_power_kW=1),dict(flow_m3s=1,pressure_Pa=90,shaft_power_kW=2)]
        self.assertEqual(eng.intersections(points,0,1),[])

    def test_tangent_root_once(self):
        points=[dict(flow_m3s=0,pressure_Pa=0,shaft_power_kW=1),dict(flow_m3s=4,pressure_Pa=16,shaft_power_kW=2)]
        roots=eng.intersections(points,4,1)
        self.assertEqual(len(roots),1)
        self.assertAlmostEqual(roots[0]['flow_m3s'],2)

    def test_duplicate_identifiers_rejected(self):
        self.case['components'][0]['id']='D-01'
        with self.assertRaises(ValueError):eng.analyze(self.case)

    def test_speed_similarity(self):
        curve=copy.deepcopy(self.case['fan_curve'])
        base=eng.prepare_curve(curve,1.2,'total')
        curve['operating_speed_rpm']=1650
        scaled=eng.prepare_curve(curve,1.2,'total')
        for a,b in zip(base,scaled):
            self.assertAlmostEqual(a['flow_m3s']*1.1,b['flow_m3s'])
            self.assertAlmostEqual(a['pressure_Pa']*1.1**2,b['pressure_Pa'])
            self.assertAlmostEqual(a['shaft_power_kW']*1.1**3,b['shaft_power_kW'])

    def test_interior_efficiency_rejected(self):
        curve=copy.deepcopy(self.case['fan_curve'])
        curve['points']=[dict(flow_m3s=0,pressure_Pa=10000,shaft_power_kW=1),dict(flow_m3s=10,pressure_Pa=0,shaft_power_kW=1)]
        with self.assertRaises(ValueError):eng.prepare_curve(curve,1.2,'total')

    def test_basis_mismatch(self):
        self.case['efficiency_basis']='static'
        with self.assertRaises(ValueError):eng.analyze(self.case)

    def test_unknown_unit_field_rejected(self):
        self.case['density']=1.2
        with self.assertRaises(ValueError):eng.analyze(self.case)

    def test_nonfinite_rejected(self):
        for invalid in [float('nan'),float('inf'),-1,True]:
            with self.subTest(invalid=invalid):
                self.case['density_kgm3']=invalid
                with self.assertRaises(ValueError):eng.analyze(self.case)

    def test_curve_efficiency_rejected(self):
        self.case['fan_curve']['points'][2]['shaft_power_kW']=0.1
        with self.assertRaises(ValueError):eng.analyze(self.case)

    def test_density_similarity(self):
        original=eng.analyze(self.case)
        self.case['density_kgm3']=0.6
        corrected=eng.prepare_curve(self.case['fan_curve'],0.6,'total')
        base=original['fan']['corrected_points']
        for a,b in zip(base,corrected):
            self.assertAlmostEqual(a['flow_m3s'],b['flow_m3s'])
            self.assertAlmostEqual(a['pressure_Pa']/2,b['pressure_Pa'])
            self.assertAlmostEqual(a['shaft_power_kW']/2,b['shaft_power_kW'])

    def test_motor_uses_envelope_and_mechanical_output(self):
        r=eng.analyze(self.case)
        self.assertAlmostEqual(r['fan']['motor_screen_mechanical_kW'],10/0.97*1.10)
        self.assertAlmostEqual(r['design']['motor_mechanical_at_duty_kW'],r['design']['shaft_power_kW']/0.97)
        self.assertAlmostEqual(r['design']['electrical_at_duty_kW'],r['design']['motor_mechanical_at_duty_kW']/0.92/0.97)

    def test_root_pressure_balance(self):
        r=eng.analyze(self.case)
        self.assertEqual(len(r['fan']['intersections']),1)
        root=r['fan']['intersections'][0]
        q=root['flow_m3s']
        self.assertAlmostEqual(root['pressure_Pa'],r['system_curve']['constant_Pa']+r['system_curve']['quadratic_Pa_per_m3s_squared']*q*q)
        self.assertEqual(root['local_slope_screen'],'restoring')

if __name__=='__main__':unittest.main()
