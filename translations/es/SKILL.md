# Dimensionamiento de extractores centrífugos

Traducción de la [skill principal](../../SKILL.md). Aplicar para predimensionamiento, selección mediante curvas y revisión de cálculos; fabricar el rodete exige diseño aerodinámico y mecánico específico. Inglés es el idioma principal; responder en el idioma solicitado, o en inglés si no se especifica. Esta traducción no es una skill independiente.

Entregar cálculos trazables, separando datos suministrados, hipótesis y selección verificada por fabricante. Diámetros y velocidades estimados no validan un ventilador.

## Datos y base de cálculo

Identificar aplicación, gas, contaminantes, partículas, corrosión, temperaturas mínima/normal/máxima, presión absoluta/altitud, densidad y humedad relevante. Distinguir caudal real de entrada y normalizado; convertir por conservación de masa con condiciones de referencia declaradas.

Registrar caudales mínimo/normal/máximo, simultaneidad y criterio de captación. Para campanas obtener geometría, posición de la fuente y criterio documentado de velocidad de captura; no imponer una velocidad genérica para todos los contaminantes.

Obtener longitudes, diámetros, rugosidad, accesorios y K, equipos, filtros limpios/sucios, chimenea y descarga. Pedir solo datos que bloqueen la siguiente decisión; continuar con hipótesis explícitas.

Confirmar presión estática o total y base del rendimiento: ηt = Q·Δpt/P_eje; ηs = Q·p_ventilador_estatica/P_eje. No combinar presión estática con rendimiento total. Según AMCA, presión estática del ventilador = presión total menos presión de velocidad a la salida; no es automáticamente diferencia de presiones estáticas entre conexiones. Revisar ensayo y base de curvas.

## Cálculos

- Q [m³/s] = Q [m³/h]/3600; 1 mmH₂O convencional (mmca) = 9,80665 Pa. Densidad del agua implícita; no usar densidad del aire para convertir.
- A = Q/v; conducto circular D = sqrt(4Q/(πv)). Verificar transporte de partículas, ruido, espacio y pérdidas. Es diámetro del conducto, no del rodete ni automáticamente del ojo de entrada.
- Gas ideal seco: ρ = p_abs/(R_específico·T_K); R_aire = 287,05 J/(kg·K). No usar R_aire para otro gas; considerar humedad/compresibilidad cuando corresponda.
- Por tramo: v = Q/A; Re = ρvDh/μ; Δp_f = f_Darcy·L/Dh·ρv²/2; Δp_local = ΣK·ρv²/2. Declarar fuentes de f y K; distinguir Darcy de Fanning.
- Sumar pérdidas y condiciones de contorno en recorrido crítico. En paralelo resolver reparto de caudales y equilibrio de presiones; no sumar ramales como serie. Incluir efectos de instalación y filtros previstos. Evitar doble contabilización de presión de velocidad/descarga y márgenes.
- Curva simplificada: Δp_sistema(Q) = Δp_constante + K_sistema Q² para resistencias cuadráticas aproximadamente constantes. Filtros/controles pueden necesitar curvas propias. No forzar paso por origen con componente constante.
- P_aire [kW] = Q·Δp/1000; P_eje = P_aire/η con bases compatibles. P_motor_mecanica = P_eje/η_transmisión; P_eléctrica = P_motor_mecanica/(η_motor·η_variador), cuando corresponda. No dividir por rendimiento del motor para elegir potencia mecánica nominal.
- Elegir potencia nominal por máxima potencia absorbida en rango permitido, transmisión, ambiente, arranque y margen justificado. Evitar factores arbitrarios repetidos. No afirmar que 10 kW es potencia comercial universal.

Usar [calculadora](../../scripts/calcular.py) para conversiones, potencia preliminar y diámetro opcional del conducto. Exige bases de presión y rendimiento; no calcula curvas ni selecciona equipos. Interfaz principal en inglés con alias portugueses. Ver [instrucciones EN/PT/ES](../../references/calculator.md).

## Curvas y selección

Obtener curvas del fabricante con modelo, rodete, velocidad, densidad, instalación, presión y potencia. Corregir a servicio. Para el mismo rodete y puntos homólogos: Q₂/Q₁ = n₂/n₁; Δp₂/Δp₁ = (ρ₂/ρ₁)(n₂/n₁)²; P₂/P₁ = (ρ₂/ρ₁)(n₂/n₁)³, aproximadamente y con rendimiento similar. No garantizar prestaciones fuera de límites del fabricante ni para recortes arbitrarios del rodete.

Encontrar intersección ventilador/sistema con bases compatibles de presión/densidad. Revisar estabilidad, rendimiento, potencia máxima, límites de giro/velocidad periférica, materiales, temperatura, ruido, vibración, mantenimiento y control. Rotular gráficos sin datos reales como ilustrativos. Sin curvas, concluir predimensionamiento, con modelo, rodete y velocidad pendientes.

Geometría: u₂ = πD₂n/60 solo relaciona velocidad periférica, diámetro y giro. Q = 2πr₂b₂C_r2 aproxima continuidad en rodete, incluyendo bloqueo si corresponde; no determina diámetro de descarga de carcasa. Rodete requiere triángulos de velocidades, deslizamiento, pérdidas y verificación estructural/equilibrado. Caudal y presión solos no validan rodete.

## Entrega y fuentes

Entregar entradas/unidades/orígenes, hipótesis, ecuaciones/resultados, pérdidas por tramo cuando existan, punto de funcionamiento, potencias de eje/motor/eléctrica separadas, pendientes y aceptación. Tratar gases inflamables/polvo combustible con referencias vigentes específicas; no inventar conformidad.

Leer [ejemplo y fuentes](example-and-sources.md) para caso 12.000 m³/h y problemas de imagen. Verificar fuentes oficiales y ediciones aplicables para selección actual y requisitos normativos. Usar curvas/manuales del fabricante como evidencia del equipo.
