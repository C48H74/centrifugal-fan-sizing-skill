# Manual de ingeniería — extractores centrífugos

Revisión 2.0 · 13/10/2026 · Guía y método de cálculo; no es certificado de conformidad.

## 1. Funcionamiento

El gas entra al rodete cerca del eje. Los álabes giratorios transfieren energía mecánica al gas, que sale hacia la periferia con componentes radial y tangencial de velocidad. La carcasa recoge el caudal y puede recuperar parte de la energía de velocidad como presión estática. El motor aporta potencia al eje; cojinetes, transmisión y accionamiento influyen en la frontera de potencia especificada.

La relación ideal de Euler es Δh₀ = u₂Cθ₂ − u₁Cθ₁, siendo u la velocidad periférica y Cθ la componente tangencial absoluta del gas. Explica la transferencia de energía; deslizamiento, incidencia, fugas, recirculación y fricción reducen el rendimiento real. No dimensiona un rodete fabricable solo con Q y presión. Para análisis de baja presión, P_aire ≈ QΔpt. Una relación de presiones alta o cambios importantes de densidad exigen método compresible y revisión del fabricante.

Álabes inclinados/curvados hacia atrás o perfil aerodinámico son candidatos para gas limpio y eficiencia alta; la contaminación puede excluir perfiles huecos/aerodinámicos. Diseños radiales pueden servir para partículas según carga, abrasión y limpieza. Álabes hacia delante tienen curvas propias de presión/potencia y riesgos de sobrecarga. Son criterios de cribado, no reglas universales. Exigir límites del material, giro, temperatura y partículas para la construcción propuesta.

## 2. Definir la aplicación

Distinguir ventilación de confort, extracción de proceso, extracción localizada, transporte neumático, extracción de humo de emergencia y atmósferas explosivas. Un punto de funcionamiento no garantiza control de contaminantes. La captura depende del impulso/flotabilidad de la fuente, cerramiento, distancia, corrientes cruzadas y aire de reposición. Acordar aceptación con higiene ocupacional. HSE HSG258 y ACGIH orientan el diseño; no son automáticamente ley en todos los países.

Registrar identificación, proceso, país/emplazamiento, altitud, modos normales/anormales, redundancia, horas y disponibilidad. Para gas: composición, presión absoluta, temperaturas mínima/normal/máxima, humedad y densidad. Para sólidos: distribución granulométrica, concentración, adherencia, abrasión y combustibilidad. Propiedades combustibles desconocidas son pendientes, no evidencia de ausencia de riesgo.

Registrar caudal real/de referencia y todos los estados de referencia. Por conservación de masa, Q_real = Q_ref·ρ_ref/ρ_real. Para el mismo gas ideal, Q_real/Q_ref = (T_real/T_ref)(p_ref/p_real), con temperaturas/presiones absolutas y corrección de compresibilidad si procede. Aclarar base húmeda/seca. No duplicar fugas ya incluidas en el caudal.

## 3. Fronteras de presión

En una sección definida, p_total = p_estática + p_velocidad, con p_velocidad ≈ ρv²/2 en el modelo de baja velocidad. Presión total del ventilador es total de salida menos total de entrada. Presión estática del ventilador, según la convención de ensayo referenciada, es su presión total menos presión de velocidad a la salida; no es simplemente la diferencia de lecturas estáticas. Identificar planos y categoría de instalación.

Categorías A/B/C/D: libre/libre, entrada libre/salida conductada, entrada conductada/salida libre y conductada/conductada. Adoptar categoría del método de ensayo y clasificación del fabricante. Curva de otra configuración puede no representar la instalación.

Construir balance de presión total entre fronteras explícitas. En extracción ambiente-ambiente con velocidades de frontera despreciables, cubrir pérdidas disipativas y energía cinética no recuperada de descarga una sola vez. Para depósitos distintos o equipos presurizados añadir requisito real de contorno. En chimeneas calientes evaluar flotabilidad por densidades del gas/ambiente; no aplicar indiscriminadamente penalización líquida ρgΔz a todo conducto de gas sin definir referencia. Convertir a presión estática del ventilador con sección real de salida y convención de clasificación.

## 4. Conductos y accesorios

Por tramo tabular caudal, forma, área, diámetro hidráulico, longitud, rugosidad, densidad y viscosidad dinámica. Área circular = πD²/4; diámetro hidráulico rectangular = 2ab/(a+b). Usar diámetro hidráulico para fricción no permite reutilizar coeficientes circulares en cualquier accesorio rectangular.

v = Q/A; Re = ρvDh/μ. Flujo circular laminar plenamente desarrollado: f_Darcy = 64/Re. Turbulento circular: resolver Colebrook, 1/√f = −2log₁₀[ε/(3,7D) + 2,51/(Re√f)]. Transición requiere criterio justificado o revisión. Δp_f = f(L/Dh)ρv²/2; Δp_accesorios = ΣKρv²/2. Vincular cada K a geometría, reparto de caudal y sección de velocidad de referencia. Darcy es cuatro veces Fanning.

Usar datos licenciados ASHRAE o ensayos/datos validados del proveedor; registrar identificador, edición, geometría y velocidad de referencia. En transiciones separar pérdida irreversible de presión total y recuperación estática. En ramificaciones resolver continuidad y presiones comunes; no sumar ramales paralelos como serie. Aportar solución de red o limitar análisis al recorrido crítico declarado. Incluir campana, flexibles, compuertas, silenciadores, separadores, filtros y terminal según servicio.

Elegir velocidades por transporte, deposición, erosión, ruido y energía, no por regla arbitraria de 10 m/s. Verificar por separado clase de presión, espesor, refuerzos, soportes, expansión y cargas; el cálculo aerodinámico no diseña estructuralmente conductos.

## 5. Curva del sistema y márgenes

Aproximación fija: Δp_sistema = Δp₀ + KQ². Constante puede representar presión fija del proceso. Fricción varía con Reynolds; filtros pueden ser no cuadráticos y depender de carga. Construir curvas limpia, normal y sucia con datos de equipos. Otra posición de compuerta o configuración de ramales es otra curva, no solo otro punto.

Efectos de instalación: remolino en entrada, codo próximo al ventilador, perfil distorsionado, desarrollo insuficiente de descarga y obstrucciones. Revisar disposición antes de añadir presión. Aplicar método AMCA 201 o evaluación del proveedor con geometría/velocidad declaradas; no añadir porcentaje universal ni duplicar efectos.

Registro de márgenes: incertidumbre, ensuciamiento, fugas, capacidad futura y motor necesitan razón, frontera y responsable. Mostrar casos nominal y extremos. Más caudal puede perjudicar ciertas capturas, aumentar ruido o sobrecargar motor; más presión no asegura caudal útil.

## 6. Selección con evidencia

Obtener selección completa en gas real: modelo, diámetro del rodete, álabes, giro, categoría, caudal, base de presión, potencia al eje, base de rendimiento, espectro sonoro y límites. Verificar listado certificado de familia/clasificación exacta; pertenencia del fabricante o logotipo no certifican todos los productos.

Cruzar curvas compatibles. Respetar rango estable y separación de pérdida aerodinámica/surge indicada por fabricante. Pendiente negativa de presión de ventilador menos sistema es cribado local cuasiestacionario restaurador, no prueba dinámica. Identificar múltiples intersecciones. No extrapolar ni asumir que rendimiento máximo siempre es punto aceptable.

Mismo rodete y puntos homólogos: Q ∝ n, Δp ∝ ρn², P_eje ∝ ρn³ aproximadamente. A giro fijo, presión/potencia escalan con densidad; caudal volumétrico real homólogo permanece aproximadamente constante. Recortes y grandes cambios de giro exigen validación; semejanza geométrica puede fallar. Revisar velocidad segura y resonancias antes de aumentar frecuencia del variador.

## 7. Potencia y motor

P_aire = QΔp/1000 en kW. Dividir por rendimiento compatible del ventilador para eje; por transmisión para salida mecánica del motor; después por motor/variador para entrada eléctrica. Si el rendimiento ya incluye motor/accionamiento, no dividir otra vez. Usar rendimientos por carga cuando existan.

Elegir motor por máxima salida mecánica requerida en rango permitido, no solo punto nominal. Incluir gas frío/denso, filtro limpio con alto caudal, giro máximo VFD, par de arranque/aceleración, inercia, frecuencia de arranques, reducción por ambiente/altitud, protección, refrigeración a baja velocidad y compatibilidad. T_motor ≥ T_carga + J_equivalente·dω/dt; aceleración debe cumplir límites térmicos. Factor de servicio no es permiso universal de sobrecarga continua. Fabricante confirma cojinetes, correas, acoplamiento y velocidades críticas.

Energía anual = Σ(P_eléctrica,i·horas_i). Comparar ciclo de vida con mismo perfil, tarifas, mantenimiento y descuento. No aplicar ley cúbica a toda instalación con presión fija o rendimiento variable sin comprobar sistema real.

## 8. Ruido, vibración e interfaces

Potencia sonora Lw caracteriza la fuente; presión sonora Lp depende de distancia, directividad, recinto, atenuación y reflexiones. Pedir octavas/tercios y método para entrada, salida y carcasa. Sumar fuentes independientes con 10log₁₀Σ10^(Li/10). dB(A) sin posición/condición no garantiza ruido ocupacional.

Definir categoría, rigidez, posiciones, RMS/pico, banda y condiciones fábrica/campo antes del límite de vibración. Tomar valores del texto licenciado adoptado/contrato; la skill no fija mm/s o grado universal. Revisar cimentación, pie cojo, alineación, aisladores, fuerzas de conductos, dilatación, acceso, resguardos e izado. Equilibrado solo no garantiza baja vibración instalada.

## 9. Servicios especiales

Para explosión exigir clasificación de área, grupo gas/polvo, temperaturas, evaluación de ignición y protección por especialistas competentes. Motor Ex solo no hace adecuado el conjunto. Construcción antichispa no es automáticamente a prueba de explosión ni conforme ATEX. Filtros/colectores pueden necesitar aislamiento/alivio propios. Humo, corrosión, alta temperatura, toxicidad o nuclear exigen revisión específica.

Aplicar [registro normativo](standards-register.md) y [anexos UE/Brasil](jurisdiction-annex.md). Textos licenciados y contrato son necesarios para cláusulas y límites numéricos. Ningún documento concede marcado CE/Ex, ART o aprobación de ingeniería.

## 10. Compra, ensayos y puesta en servicio

Usar [plantilla de expediente](project-dossier.md). Antes de compra cerrar entradas críticas, garantías, rango, materiales, método, tolerancias, incertidumbre y desviaciones. Definir instrumentos, testigos y resolución de disputas. Acordar aceptación antes de resultados.

FAT revisa configuración, dimensiones, giro, resguardos, certificados, equilibrado/vibración, motor/accionamiento y pruebas aerodinámicas/acústicas contratadas. SAT verifica geometría instalada, alineación, anclaje, control, enclavamientos, giro, caudal/presión en planos definidos, entrada eléctrica, vibración y captura. Registrar filtro, temperatura, densidad, compuertas y demandas simultáneas para comparar garantía.

Calibración trazable; tomas/barridos deben adecuarse al método/perfil. Incertidumbres relativas independientes: u(P_eje)/P_eje ≈ sqrt[(uQ/Q)²+(uΔp/Δp)²+(uη/η)²]. Es aproximación de primer orden, no sustituye análisis normativo. Tolerancia, incertidumbre y margen son distintos. No descontar tolerancia regulatoria de verificación del requisito de diseño.

Emitir conceptual, preliminar, consulta a proveedor, autorizado para compra o as-built solo según evidencia. Registrar autor, revisor, aprobador, revisión, hashes, pendientes y autoridad de cierre. No completar aprobaciones humanas automáticamente.
