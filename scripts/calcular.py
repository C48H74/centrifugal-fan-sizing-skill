"""Preliminary sizing; manufacturer curves required. Standard library only."""
import argparse
import json
import math

def positive(value):
    x = float(value)
    if not math.isfinite(x) or x <= 0:
        raise argparse.ArgumentTypeError('Enter a finite number greater than zero.')
    return x

def efficiency(value):
    x = positive(value)
    if x > 1:
        raise argparse.ArgumentTypeError('Efficiency must be greater than 0 and at most 1 (e.g. 0.72).')
    return x

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--flow-m3h', '--vazao-m3h', dest='vazao_m3h', type=positive, required=True)
    p.add_argument('--pressure', '--pressao', dest='pressao', type=positive, required=True)
    p.add_argument('--unit', '--unidade', dest='unidade', choices=['Pa', 'mmca'], required=True)
    p.add_argument('--pressure-basis', '--base-pressao', dest='base_pressao', choices=['total', 'static', 'estatica'], required=True)
    p.add_argument('--efficiency-basis', '--base-eficiencia', dest='base_eficiencia', choices=['total', 'static', 'estatica'], required=True)
    p.add_argument('--efficiency', '--eficiencia', dest='eficiencia', type=efficiency, required=True)
    p.add_argument('--drive-efficiency', '--eta-transmissao', dest='eta_transmissao', type=efficiency, default=1)
    p.add_argument('--motor-efficiency', '--eta-motor', dest='eta_motor', type=efficiency)
    p.add_argument('--duct-velocity', '--velocidade-duto', dest='velocidade_duto', type=positive)
    a = p.parse_args()
    a.base_pressao = 'static' if a.base_pressao == 'estatica' else a.base_pressao
    a.base_eficiencia = 'static' if a.base_eficiencia == 'estatica' else a.base_eficiencia
    if a.base_pressao != a.base_eficiencia:
        p.error('Pressure and efficiency must use the same basis.')
    q = a.vazao_m3h / 3600
    dp = a.pressao * (9.80665 if a.unidade == 'mmca' else 1)
    ar = q * dp / 1000
    eixo = ar / a.eficiencia
    motor = eixo / a.eta_transmissao
    r = dict(status='preliminary sizing; verify manufacturer curve and operating envelope',
             basis=a.base_pressao, flow_m3s=q, pressure_Pa=dp,
             air_power_kW=ar, shaft_power_kW=eixo,
             motor_mechanical_power_at_duty_kW=motor)
    if a.eta_motor:
        r['electrical_power_without_vfd_kW'] = motor / a.eta_motor
    if a.velocidade_duto:
        r['duct_area_m2'] = q / a.velocidade_duto
        r['circular_duct_diameter_m'] = math.sqrt(4*q/(math.pi*a.velocidade_duto))
    print(json.dumps(r, ensure_ascii=False, indent=2, allow_nan=False))

if __name__ == '__main__':
    main()
