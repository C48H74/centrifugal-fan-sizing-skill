# Calculator / Calculadora

## English

Run with Python 3; no third-party dependencies. Flow is actual inlet m³/h; efficiency is a fraction, not percent. Pressure and efficiency bases must match. Optional drive efficiency defaults to 1; motor efficiency enables electrical input estimation without VFD losses. Duct velocity estimates a circular duct, not an impeller. JSON uses English field names. The filename and Portuguese argument aliases are retained for compatibility.

```bash
python scripts/calcular.py --flow-m3h 12000 --pressure 180 --unit mmca --pressure-basis total --efficiency-basis total --efficiency 0.72 --duct-velocity 10
```

Options: `--flow-m3h`, `--pressure`, `--unit Pa|mmca`, `--pressure-basis total|static`, `--efficiency-basis total|static`, `--efficiency`, `--drive-efficiency`, `--motor-efficiency`, `--duct-velocity`.

Expected: 3.333333 m³/s; 1765.197 Pa; air power 5.88399 kW; shaft power 8.172208 kW; circular duct diameter 0.651470 m. Final fan/motor selection requires curves and the full operating envelope.

## Português

Executar com Python 3, sem dependências externas. Vazão real na entrada em m³/h; eficiência em fração, não porcentagem. Bases de pressão e eficiência devem coincidir. Eficiência de transmissão opcional assume 1; eficiência do motor permite estimar potência elétrica sem perdas do inversor. Velocidade de duto estima duto circular, não rotor. Campos JSON em inglês. Nome do arquivo e aliases portugueses preservados por compatibilidade.

```bash
python scripts/calcular.py --vazao-m3h 12000 --pressao 180 --unidade mmca --base-pressao total --base-eficiencia total --eficiencia 0.72 --velocidade-duto 10
```

Aliases: `--vazao-m3h`, `--pressao`, `--unidade`, `--base-pressao`, `--base-eficiencia`, `--eficiencia`, `--eta-transmissao`, `--eta-motor`, `--velocidade-duto`; `estatica` equivale a `static`.

Resultado esperado: 3,333333 m³/s; 1.765,197 Pa; potência no ar 5,88399 kW; no eixo 8,172208 kW; diâmetro do duto circular 0,651470 m. Seleção final de ventilador/motor exige curvas e todo o envelope operacional.

## Español

Ejecutar con Python 3, sin dependencias externas. Caudal real de entrada en m³/h; rendimiento en fracción, no porcentaje. Bases de presión y rendimiento deben coincidir. Rendimiento opcional de transmisión supone 1; rendimiento del motor permite estimar potencia eléctrica sin pérdidas del variador. Velocidad del conducto estima conducto circular, no rodete. Campos JSON en inglés. Nombre del archivo y alias portugueses conservados por compatibilidad. Utilizar las opciones inglesas del primer ejemplo.

Opciones: caudal `--flow-m3h`; presión `--pressure`; unidad `--unit Pa|mmca`; bases `--pressure-basis total|static` y `--efficiency-basis total|static`; rendimiento `--efficiency`; transmisión `--drive-efficiency`; motor `--motor-efficiency`; velocidad del conducto `--duct-velocity`.

Resultado esperado: 3,333333 m³/s; 1.765,197 Pa; potencia al aire 5,88399 kW; al eje 8,172208 kW; diámetro del conducto circular 0,651470 m. Selección final de ventilador/motor exige curvas y todo el rango operativo.
