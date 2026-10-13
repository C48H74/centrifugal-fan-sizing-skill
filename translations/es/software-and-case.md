# Software, reproducción y caso de portafolio

Versión 2.0.0 · Entradas/salidas SI en inglés · Biblioteca estándar Python 3 para cálculos.

## Programas y límites

`scripts/calcular.py` estima punto único: conversiones, rendimiento compatible, potencia eje/motor y diámetro circular opcional. Conserva alias portugueses.

`scripts/engineering.py` lee JSON de un recorrido en serie, conductos circulares, fricción Darcy (laminar o Colebrook turbulento) y K locales. Equipos usan ley cuadrática declarada de caudal/densidad. Curva congela factores de fricción en caudal de diseño: aproximación, no red exacta. Admite término constante no negativo.

Curva de ventilador: muestras de caudal creciente, presión/potencia al eje, densidad/giro y base de presión. Corregir con leyes homólogas e interpolar presión/potencia linealmente por intervalos. Devolver todas las intersecciones analíticas con sistema cuadrático, incluso dos en un intervalo y tangencia. No extrapolar; ausencia/multiplicidad exige revisión. Pendiente no certifica estabilidad dinámica. Mayor potencia muestreada es máximo del modelo lineal, no necesariamente máximo real entre medidas o fuera del intervalo.

Rechazar campos desconocidos, bases incompatibles, valores físicos no finitos/no positivos, rendimientos inválidos, IDs duplicados, caudales no crecientes, Reynolds transitorio y curvas interpoladas imposibles energéticamente. Exigir fuentes de conductos/equipos/curva; no verifica autenticidad. Usuario revisa baja presión/incompresibilidad, topología, convenciones y límites mecánicos. No selecciona motor comercial automáticamente.

No implementa redes paralelas, fricción rectangular, compresibilidad, diseño de captura, psicrometría, deposición, carga real de filtros, inestabilidad dinámica, rodete, propagación sonora, vibración predictiva, FEI, conformidad o aprobación profesional. Cálculos sin dependencias externas; Matplotlib opcional para gráficos.

## Reproducción

Ejecutar desde raíz:

```bash
python scripts/calcular.py --flow-m3h 12000 --pressure 180 --unit mmca --pressure-basis total --efficiency-basis total --efficiency 0.72
python scripts/engineering.py examples/industrial-case.json --output examples/industrial-case-results.json
python scripts/build_case.py
python -m unittest discover -s tests -v
```

Para gráficos instalar Matplotlib en entorno elegido y repetir `build_case.py`. Resultado registra versión y SHA-256 de bytes de entrada. Archivar entrada/salida, documentos de fabricante y revisión humana juntos; hash demuestra identidad, no corrección técnica.

## Caso 1 — ejemplo suministrado

12.000 m³/h y 180 mmH₂O dan 1.765,197 Pa, 5,88399 kW al aire y 8,172208 kW al eje si rendimiento total del 72% corresponde a presión total. No hay red levantada ni curva certificada. Ver [ejemplo revisado](example-and-sources.md). Demuestra estimación de potencia, no producto seleccionado.

## Caso 2 — escenario industrial construido

**CF-CASE-002-ILLUSTRATIVE.** Geometrías, K, pérdidas, rendimientos y curva son supuestos didácticos, no instalación de cliente, proyecto entregado o garantía de fabricante. Imágenes son ilustraciones IA; no presentar como experiencia comercial puesta en marcha.

Caudal real 12.000 m³/h; densidad 1,20 kg/m³; viscosidad 1,81×10⁻⁵ Pa·s. D-01: 20 m, diámetro 0,65 m, rugosidad 0,15 mm, ΣK = 2,0. D-02: 10 m, 0,60 m, misma rugosidad, ΣK = 1,5. Pérdidas supuestas: campana 150 Pa; filtro sucio 850 Pa; silenciador 120 Pa; velocidad de descarga libre 0,60 m = 83,3919 Pa incluida una vez. Balance ambiente-ambiente de presión total. Pérdidas variables cuadráticas y fricción congelada en diseño.

| Magnitud | Resultado |
| --- | ---: |
| D-01 velocidad / f Darcy / pérdida | 10,0453 m/s / 0,01590076 / 150,71094 Pa |
| D-02 velocidad / f Darcy / pérdida | 11,7893 m/s / 0,01595170 / 147,25860 Pa |
| Presión total al caudal de diseño | 1.501,36147 Pa = 153,09626 mmH₂O |
| Coeficiente del sistema | 135,1225319 Pa/(m³/s)² |
| Potencia al aire | 5,004538 kW |
| Al eje suponiendo ηt = 0,72 | 6,950748 kW |
| Mecánica del motor, ηtransmisión = 0,97 | 7,165719 kW |
| Eléctrica, ηmotor = 0,92; ηVFD = 0,97 | 8,029717 kW |

Curva sintética a 1.500 rpm y 1,20 kg/m³: caudales 1/2/3/4/5 m³/s, presiones totales 2400/2200/1900/1350/650 Pa, potencias eje 5/7/8,5/9,5/10 kW. No es producto real; no valida rodete ni giro seguro.

Intersección del sistema sucio: **12.527,06 m³/h a 1.636,14 Pa**, **8,97974 kW al eje**, rendimiento total derivado **63,4022%**. Proviene de curva sintética, no del 72% supuesto. No combinar potencia estimada del punto nominal con operación obtenida por curva. Caudal 4,39% por encima del objetivo; sin tolerancia de proyecto no hay aceptación automática.

Mayor potencia muestreada 10 kW. Transmisión supuesta 97% y margen declarado de cribado 10% dan 11,34021 kW mecánicos. No es motor seleccionado ni margen normativo; confirmar rango completo, tamaño comercial, reducción ambiental, aceleración y límites. Elegir tamaño siguiente sin revisar no cierra selección.

## Sensibilidades

| Hipótesis | Q operativo m³/h | Pa totales | kW eje | Significado |
| --- | ---: | ---: | ---: | --- |
| Filtro sucio, base | 12.527,06 | 1.636,14 | 8,97974 | Caso construido |
| Filtro limpio: 400 Pa al Q nominal | 13.944,20 | 1.419,64 | 9,37339 | Menor resistencia aumenta caudal/potencia en esta curva |
| Gas más denso: 1,40 kg/m³ | 12.528,77 | 1.908,53 | 10,47692 | Mayor presión/potencia; pequeño cambio Q por f recalculado |
| Giro +10%: 1.650 rpm | 13.779,77 | 1.979,73 | 11,95203 | Solo semejanza; autorización mecánica no demostrada |

Filtro limpio ilustra revisión de sobrecarga, no tendencia universal. +10% giro aumenta potencia homóloga por 1,1³ = 1,331. Caso de densidad recalcula fricción nominal antes de congelar nueva curva.

Archivos: [entrada](../../examples/industrial-case.json), [resultados](../../examples/industrial-case-results.json), [CSV](../../examples/sensitivity.csv), [gráfico determinista](../../assets/engineering/case-curves.png). Curvas numéricas no generadas por IA.

## Aceptación y afirmaciones

Pruebas cubren aritmética, invariantes y fallos del modelo; no validan frente a ensayo certificado independiente. Aplicabilidad normativa pendiente sin jurisdicción/fecha/producto y cláusulas licenciadas. No demostrados: captura, materiales, acústica, vibración, áreas clasificadas, estructura del rodete, arranque y FAT/SAT.

Afirmación sustentada: “Desarrollé flujo multilingüe trazable de predimensionamiento con orientación normativa, herramientas probadas y caso industrial explícitamente sintético.” No sustentada: “Diseñé y certifiqué ventilador conforme a todas las regulaciones internacionales.”
