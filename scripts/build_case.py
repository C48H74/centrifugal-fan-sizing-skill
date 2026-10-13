"""Reproduce the illustrative case, sensitivity table and publication-quality plots."""
import copy
import csv
import hashlib
import json
from pathlib import Path
from engineering import analyze

ROOT=Path(__file__).resolve().parents[1]

def main():
    path=ROOT/'examples/industrial-case.json'
    raw=path.read_bytes()
    case=json.loads(raw)
    result=analyze(case)
    result['input_sha256']=hashlib.sha256(raw).hexdigest()
    (ROOT/'examples/industrial-case-results.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    variants=[('Dirty filter, base',copy.deepcopy(case))]
    clean=copy.deepcopy(case)
    clean['components'][1]['id']='FILTER-CLEAN'
    clean['components'][1]['reference_loss_Pa']=400
    variants.append(('Clean filter, assumed 400 Pa',clean))
    dense=copy.deepcopy(case);dense['density_kgm3']=1.4
    variants.append(('Denser gas, assumed 1.40 kg/m3',dense))
    fast=copy.deepcopy(case);fast['fan_curve']['operating_speed_rpm']=1650
    variants.append(('Speed +10%, screening only',fast))
    rows=[]
    for label,variant in variants:
        r=analyze(variant)
        for point in r['fan']['intersections']:
            rows.append(dict(scenario=label,flow_m3h=point['flow_m3h'],pressure_Pa=point['pressure_Pa'],
                shaft_power_kW=point['shaft_power_kW'],compatible_efficiency=point['compatible_efficiency'],
                motor_screen_mechanical_kW=r['fan']['motor_screen_mechanical_kW']))
    with (ROOT/'examples/sensitivity.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    # Plotting is optional; numerical analyses above use only the standard library.
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print('Numerical outputs generated. Install matplotlib to reproduce plots.')
        return
    folder=ROOT/'assets/engineering';folder.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
    fig,axes=plt.subplots(1,2,figsize=(13,5),layout='constrained')
    points=result['fan']['corrected_points']
    xs=[p['flow_m3s'] for p in points]
    axes[0].plot([x*3600 for x in xs],[p['pressure_Pa'] for p in points],color='#d48310',lw=2,label='Synthetic fan curve')
    for label,variant in variants[:2]:
        r=analyze(variant);k=r['system_curve']['quadratic_Pa_per_m3s_squared'];c=r['system_curve']['constant_Pa']
        grid=[i/100 for i in range(100,501)]
        axes[0].plot([q*3600 for q in grid],[c+k*q*q for q in grid],lw=2,label=label)
        for pt in r['fan']['intersections']:
            axes[0].scatter([pt['flow_m3h']],[pt['pressure_Pa']],s=55,zorder=5)
    axes[0].set(xlabel='Actual airflow (m³/h)',ylabel='Fan total pressure (Pa)',title='Operating point: illustrative data')
    axes[0].legend(fontsize=9);axes[0].grid(alpha=.2)
    axes[1].plot([q*3600 for q in xs],[p['shaft_power_kW'] for p in points],lw=2,color='#155c82',label='Synthetic shaft-power curve')
    pt=result['fan']['intersections'][0]
    axes[1].scatter([pt['flow_m3h']],[pt['shaft_power_kW']],color='#d48310',s=60,label='Dirty-filter operating point')
    axes[1].set(xlabel='Actual airflow (m³/h)',ylabel='Absorbed shaft power (kW)',title='Power envelope must be checked')
    axes[1].legend(fontsize=9);axes[1].grid(alpha=.2)
    fig.suptitle('CF-CASE-002 — synthetic training case, NOT manufacturer performance',fontsize=13,weight='bold')
    fig.savefig(folder/'case-curves.png',dpi=180)
    fig.savefig(folder/'case-curves.pdf')
    plt.close(fig)
    print('Case results, sensitivity CSV and PNG/PDF plots generated.')

if __name__=='__main__':main()
