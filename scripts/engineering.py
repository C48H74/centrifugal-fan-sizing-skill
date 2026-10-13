"""Auditable single-path fan/system screening. SI units, Python standard library.

Not a certification, parallel-network solver, compressible-flow solver or rotor designer.
System curve uses Darcy factors frozen at design flow. Fan curve is piecewise linear.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

VERSION = '2.0.0'

def number(value, name, minimum=0.0, strict=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f'{name}: expected a numeric value')
    if not math.isfinite(value) or value < minimum or (strict and value == minimum):
        raise ValueError(f'{name}: invalid range or non-finite value')
    return float(value)

def positive(value, name):
    return number(value, name, strict=True)

def eta(value, name):
    value = positive(value, name)
    if value > 1:
        raise ValueError(f'{name}: efficiency must be <= 1')
    return value

def keys(obj, allowed, required, name):
    if not isinstance(obj, dict):
        raise ValueError(f'{name}: expected object')
    unknown = set(obj)-set(allowed)
    missing = set(required)-set(obj)
    if unknown or missing:
        raise ValueError(f'{name}: unknown keys {sorted(unknown)}, missing keys {sorted(missing)}')

def friction_factor(reynolds, relative_roughness):
    re = positive(reynolds, 'Re')
    rr = number(relative_roughness, 'relative roughness')
    if rr >= 0.05:
        raise ValueError('Relative roughness >= 0.05: outside supported screening range')
    if re < 2300:
        return 64/re, 'laminar 64/Re'
    if re < 4000:
        raise ValueError('Transitional flow 2300 <= Re < 4000: no automatic friction factor')
    # Solve Colebrook for x = 1/sqrt(f), fixed-point iteration.
    x = 7.0
    for _ in range(100):
        nxt = -2*math.log10(rr/3.7 + 2.51*x/re)
        if abs(nxt-x) < 1e-12:
            return 1/nxt**2, 'Colebrook, Darcy'
        x = nxt
    raise ValueError('Colebrook did not converge')

def duct_loss(q, rho, mu, segment):
    keys(segment, ['id','length_m','diameter_m','roughness_m','K_sum','source'],
         ['id','length_m','diameter_m','roughness_m','K_sum','source'], 'segment')
    if not isinstance(segment['source'], str) or not segment['source'].strip():
        raise ValueError('Segment source/assumption must be recorded')
    d = positive(segment['diameter_m'], 'diameter_m')
    length = number(segment['length_m'], 'length_m')
    roughness = number(segment['roughness_m'], 'roughness_m')
    kval = number(segment['K_sum'], 'K_sum')
    area = math.pi*d*d/4
    velocity = q/area
    re = rho*velocity*d/mu
    f, method = friction_factor(re, roughness/d)
    dynamic = rho*velocity*velocity/2
    straight = f*length/d*dynamic
    fittings = kval*dynamic
    return dict(id=segment['id'], source=segment['source'], area_m2=area,
                velocity_ms=velocity, reynolds=re, darcy_factor=f, method=method,
                velocity_pressure_Pa=dynamic, straight_loss_Pa=straight,
                fitting_loss_Pa=fittings, total_loss_Pa=straight+fittings)

def prepare_curve(curve, target_rho, basis):
    keys(curve, ['source','evidence','basis','reference_density_kgm3',
                'reference_speed_rpm','operating_speed_rpm','points'],
         ['source','evidence','basis','reference_density_kgm3',
          'reference_speed_rpm','operating_speed_rpm','points'], 'fan_curve')
    if curve['basis'] != basis:
        raise ValueError('Fan and system pressure bases differ')
    if curve['evidence'] not in ['illustrative','manufacturer_supplied']:
        raise ValueError('curve evidence must be illustrative or manufacturer_supplied')
    if not isinstance(curve['source'], str) or not curve['source'].strip():
        raise ValueError('Curve source required')
    reference_rho = positive(curve['reference_density_kgm3'], 'reference density')
    nref = positive(curve['reference_speed_rpm'], 'reference speed')
    n = positive(curve['operating_speed_rpm'], 'operating speed')
    ratio_n, ratio_rho = n/nref, target_rho/reference_rho
    points = []
    if not isinstance(curve['points'], list) or len(curve['points']) < 2:
        raise ValueError('At least two curve points required')
    for row in curve['points']:
        keys(row,['flow_m3s','pressure_Pa','shaft_power_kW'],
             ['flow_m3s','pressure_Pa','shaft_power_kW'],'curve point')
        q = number(row['flow_m3s'],'curve flow')*ratio_n
        dp = number(row['pressure_Pa'],'curve pressure')*ratio_rho*ratio_n**2
        power = positive(row['shaft_power_kW'],'curve shaft power')*ratio_rho*ratio_n**3
        if q*dp/1000/power > 1+1e-9:
            raise ValueError('Curve implies efficiency above 100%')
        if points and q <= points[-1]['flow_m3s']:
            raise ValueError('Curve flows must be strictly increasing in supplied order')
        points.append(dict(flow_m3s=q,pressure_Pa=dp,shaft_power_kW=power))
    for left, right in zip(points, points[1:]):
        q0,q1=left['flow_m3s'],right['flow_m3s']
        mp=(right['pressure_Pa']-left['pressure_Pa'])/(q1-q0)
        bp=left['pressure_Pa']-mp*q0
        mw=1000*(right['shaft_power_kW']-left['shaft_power_kW'])/(q1-q0)
        bw=1000*left['shaft_power_kW']-mw*q0
        candidates=[q0,q1]
        if mp<0:
            vertex=-(bp-mw)/(2*mp)
            if q0<vertex<q1:candidates.append(vertex)
        if any(mp*q*q+(bp-mw)*q-bw>1e-6 for q in candidates):
            raise ValueError('Interpolated curve implies efficiency above 100%')
    return points

def intersections(points, constant, coefficient):
    """All roots within supplied intervals of fan(q) - (constant + k*q²)."""
    found=[]
    for left,right in zip(points,points[1:]):
        ql,qr=left['flow_m3s'],right['flow_m3s']
        slope=(right['pressure_Pa']-left['pressure_Pa'])/(qr-ql)
        intercept=left['pressure_Pa']-slope*ql
        # k*q² - slope*q + constant - intercept = 0
        if coefficient == 0:
            if slope == 0:
                if math.isclose(intercept,constant,abs_tol=1e-9):
                    raise ValueError('Coincident fan and system curves: non-unique continuum')
                continue
            roots=[(constant-intercept)/slope]
        else:
            disc=slope*slope-4*coefficient*(constant-intercept)
            if disc < -1e-9:
                continue
            disc=max(disc,0)
            # Stable quadratic evaluation avoids cancellation for small roots.
            b=-slope
            z=-0.5*(b+math.copysign(math.sqrt(disc),b))
            roots=([z/coefficient,(constant-intercept)/z] if z else [0.0])
        for q in sorted(roots):
            if q < ql-1e-9 or q > qr+1e-9 or q <= 0:
                continue
            q=max(ql,min(q,qr))
            if any(abs(q-r['flow_m3s']) < 1e-8 for r in found):
                continue
            fraction=(q-ql)/(qr-ql)
            power=left['shaft_power_kW']+fraction*(right['shaft_power_kW']-left['shaft_power_kW'])
            dp=constant+coefficient*q*q
            residual_slope=slope-2*coefficient*q
            found.append(dict(flow_m3s=q,flow_m3h=q*3600,pressure_Pa=dp,
                shaft_power_kW=power,compatible_efficiency=q*dp/(1000*power),
                fan_minus_system_slope=residual_slope,
                local_slope_screen='restoring' if residual_slope<0 else 'non-restoring or tangent',
                note='Slope screening does not prove dynamic stability; vendor validation required'))
    return sorted(found,key=lambda x:x['flow_m3s'])

def analyze(data):
    keys(data,['case_id','evidence','flow_m3h','density_kgm3','viscosity_Pas',
        'pressure_basis','constant_pressure_Pa','segments','components',
        'fan_efficiency','efficiency_basis','drive_efficiency','motor_efficiency',
        'vfd_efficiency','motor_margin_fraction','fan_curve'],
        ['case_id','evidence','flow_m3h','density_kgm3','viscosity_Pas',
         'pressure_basis','constant_pressure_Pa','segments','components',
         'fan_efficiency','efficiency_basis'], 'case')
    if data['evidence'] not in ['illustrative','project_supplied']:
        raise ValueError('case evidence must be illustrative or project_supplied')
    if not isinstance(data['case_id'],str) or not data['case_id'].strip():
        raise ValueError('case_id must be a nonempty string')
    basis=data['pressure_basis']
    if basis not in ['total','static'] or basis!=data['efficiency_basis']:
        raise ValueError('Matching total/static pressure and efficiency bases required')
    q=positive(data['flow_m3h'],'flow_m3h')/3600
    rho=positive(data['density_kgm3'],'density_kgm3')
    mu=positive(data['viscosity_Pas'],'viscosity_Pas')
    constant=number(data['constant_pressure_Pa'],'constant pressure')
    if not isinstance(data['segments'],list) or not isinstance(data['components'],list):
        raise ValueError('segments and components must be lists')
    losses=[duct_loss(q,rho,mu,s) for s in data['segments']]
    components=[]
    for c in data['components']:
        keys(c,['id','reference_loss_Pa','reference_flow_m3s','reference_density_kgm3','source'],
             ['id','reference_loss_Pa','reference_flow_m3s','reference_density_kgm3','source'],'component')
        if not isinstance(c['source'],str) or not c['source'].strip():
            raise ValueError('Component source/assumption required')
        dp=number(c['reference_loss_Pa'],'reference loss')
        qref=positive(c['reference_flow_m3s'],'reference flow')
        rhoref=positive(c['reference_density_kgm3'],'reference density')
        loss=dp*(q/qref)**2*(rho/rhoref)
        components.append(dict(id=c['id'],source=c['source'],loss_Pa=loss,
            law='assumed quadratic at fixed condition; verify equipment curve'))
    identifiers=[s['id'] for s in losses]+[c['id'] for c in components]
    if any(not isinstance(i,str) or not i.strip() for i in identifiers) or len(set(identifiers))!=len(identifiers):
        raise ValueError('Segment/component IDs must be unique nonempty strings')
    quadratic_loss=sum(s['total_loss_Pa'] for s in losses)+sum(c['loss_Pa'] for c in components)
    dp=constant+quadratic_loss
    if dp<=0:
        raise ValueError('Required pressure must be positive')
    e=eta(data['fan_efficiency'],'fan efficiency')
    drive=eta(data.get('drive_efficiency',1),'drive efficiency')
    air=q*dp/1000
    shaft=air/e
    motor=shaft/drive
    electrical=None
    if 'vfd_efficiency' in data and 'motor_efficiency' not in data:
        raise ValueError('VFD electrical estimate also requires motor efficiency')
    if 'motor_efficiency' in data:
        electrical=motor/(eta(data['motor_efficiency'],'motor efficiency')*
                          eta(data.get('vfd_efficiency',1),'VFD efficiency'))
    margin=number(data.get('motor_margin_fraction',0),'motor margin')
    result=dict(version=VERSION,case_id=data['case_id'],evidence=data['evidence'],
        release_status='PRELIMINARY — NOT FOR PURCHASE OR CONSTRUCTION',
        basis=basis,flow_m3s=q,density_kgm3=rho,segments=losses,components=components,
        system_curve=dict(constant_Pa=constant,quadratic_Pa_per_m3s_squared=quadratic_loss/q**2,
                          assumption='Darcy factors frozen at design flow; all variable equipment losses quadratic'),
        design=dict(pressure_Pa=dp,pressure_mmH2O=dp/9.80665,air_power_kW=air,
                    shaft_power_kW=shaft,motor_mechanical_at_duty_kW=motor,
                    electrical_at_duty_kW=electrical),
        limitations=['Single circular-duct series path only; no parallel branches',
         'Steady low-pressure incompressible screening; user must verify applicability',
         'No automatic capture, explosion protection, acoustic, structural or code compliance validation',
         'No manufacturer authenticity check; evidence labels are user declarations'])
    if 'fan_curve' in data:
        points=prepare_curve(data['fan_curve'],rho,basis)
        roots=intersections(points,constant,quadratic_loss/q**2)
        maxpower=max(p['shaft_power_kW'] for p in points)
        result['fan']=dict(source=data['fan_curve']['source'],evidence=data['fan_curve']['evidence'],
            corrected_points=points,intersections=roots,
            maximum_sampled_shaft_power_kW=maxpower,
            motor_screen_mechanical_kW=maxpower/drive*(1+margin),
            margin_fraction=margin,
            envelope_note='Bounded sampled curve only; manufacturer must confirm full allowed envelope and maxima')
        if not roots:
            result['limitations'].append('No intersection inside supplied curve; extrapolation prohibited')
        if len(roots)>1:
            result['limitations'].append('Multiple intersections; no automatic operating point selection')
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    try:
        raw=args.input.read_bytes()
        data=json.loads(raw.decode('utf-8-sig'),parse_constant=lambda v: (_ for _ in ()).throw(ValueError(f'Invalid JSON constant {v}')))
        result=analyze(data)
        result['input_sha256']=hashlib.sha256(raw).hexdigest()
        text=json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
        if args.output:
            args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(text,encoding='utf-8')
        else:
            print(text,end='')
    except (ValueError,TypeError,KeyError,OSError,ArithmeticError) as exc:
        parser.exit(2,f'Input/calculation error: {exc}\n')

if __name__=='__main__':
    main()
