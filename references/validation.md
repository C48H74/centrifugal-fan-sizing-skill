# Validation and evidence record — revision 2.0

Date: 2026-10-13. This record separates numerical software verification from engineering validation and statutory conformity.

Executed locally: **25 automated tests passed**, root skill structural validation passed, and the synthetic case/results/sensitivity plots were reproduced. This result describes this revision's local verification; it is not a third-party certification or a claim that unexecuted future revisions pass. The repository CI also runs the regression suite and reproduces the case on its configured Python matrix; check the actual workflow result before claiming a remote pass.

## Verification scope

The automated suite checks the supplied 180 mmH₂O example, Portuguese CLI compatibility, invalid efficiency and mismatched bases; laminar friction; Colebrook residual; an independently hand-calculated segment; analytical curve roots, multiple roots and tangency; no extrapolation; speed/density similarity; motor power boundaries and envelope margin; invalid physical inputs, unknown fields, duplicate IDs and impossible curve efficiencies; local documentation targets and translation coverage.

Run `python -m unittest discover -s tests -v`. The numerical case is reproduced with `python scripts/engineering.py examples/industrial-case.json --output examples/industrial-case-results.json`; the input hash accompanies results. The optional graph builder reproduces sensitivity values and PNG/PDF figures. The root SKILL.md is also checked using the Codex skill-creator structural validator. Translation files do not carry independent skill frontmatter, avoiding duplicate skill discovery.

## Evidence limits

- Numerical verification establishes behavior for the tested cases and stated approximations; it is not an independent certified fan-test comparison.
- Engineering chart was visually inspected for labels, units, intersections and power boundary. Publication photographs are AI-generated illustrations and cannot prove a product's construction or performance.
- Standards identifiers/scopes were checked against official ISO/AMCA/IEC sources. Full licensed clause review, tolerances, national adoption and project applicability remain project tasks.
- EU legal references include 2024/1834 and amendment 2025/2481; official consolidated text was accessed, while some EUR-Lex requests encountered an access-verification page. Project reviewers must use the current official complete text and corrigenda, not a search excerpt, for a legal decision.
- No real manufacturer, customer site, signed approval, FAT/SAT, hazardous-area study or exposure-control measurement is represented by the synthetic case.

## Company adoption criteria

Assign an engineering owner and reviewer. Obtain controlled licensed standards, approved design data and authentic vendor curves. Confirm whether the single-path numerical model fits the job; use a validated network or compressible solver when it does not. Agree guarantees/tolerances and test methods, then perform project-specific validation and human approval. Keep deviations, input/output hashes and as-built evidence under document control.

This package may support engineering studies and portfolio demonstration. It does not authorize procurement or construction automatically or claim universal regulatory compliance.

## Português

Registro de 13/10/2026: separar verificação numérica de validação de engenharia/conformidade. Testes cobrem exemplo de 180 mmca, aliases PT, rejeição de entradas/bases/eficiências inválidas, atrito laminar/Colebrook, trecho manual, raízes analíticas/múltiplas/tangentes, ausência de extrapolação, semelhança de rotação/densidade, fronteiras de potência/envelope e links/traduções. Executar comando acima; resultados do case registram hash. Validador estrutural da skill também utilizado. Traduções sem frontmatter independente evitam descoberta duplicada.

Gráfico inspecionado visualmente; imagens IA não comprovam construção/desempenho. Catálogos ISO/AMCA/IEC conferidos, mas cláusulas licenciadas/limites/adoções/aplicabilidade são tarefas do projeto. Referências UE incluem emenda 2025/2481; algumas consultas EUR-Lex encontraram verificação de acesso, por isso decisões legais exigem texto completo oficial atualizado/retificações. Case não representa fabricante/cliente real, aprovação assinada, FAT/SAT, área classificada ou medição ocupacional.

Empresa deve designar dono/revisor, obter normas licenciadas/dados aprovados/curvas autênticas, confirmar modelo ou usar solver de rede/compressível apropriado, acordar garantias e ensaios, validar projeto e aprovar humanamente. Controlar desvios, hashes e as-built. Pacote apoia estudos/portfólio, sem liberação automática de compra/construção ou conformidade universal.

## Español

Registro de 13/10/2026: separar verificación numérica de validación de ingeniería/conformidad. Pruebas cubren ejemplo de 180 mmH₂O, alias PT, entradas/bases/rendimientos inválidos, fricción laminar/Colebrook, tramo manual, raíces analíticas/múltiples/tangentes, no extrapolación, semejanza giro/densidad, fronteras potencia/rango y enlaces/traducciones. Ejecutar comando anterior; resultados registran hash. Validador estructural también utilizado. Traducciones sin frontmatter independiente evitan descubrimiento duplicado.

Gráfico inspeccionado visualmente; imágenes IA no prueban construcción/rendimiento. Catálogos ISO/AMCA/IEC revisados; cláusulas licenciadas/límites/adopciones/aplicabilidad son tareas del proyecto. Referencias UE incluyen enmienda 2025/2481; algunas consultas EUR-Lex mostraron verificación de acceso, por lo que decisiones legales requieren texto completo oficial vigente/correcciones. Caso no representa fabricante/cliente real, aprobación firmada, FAT/SAT, área clasificada o medición ocupacional.

Empresa debe asignar propietario/revisor, obtener normas licenciadas/datos aprobados/curvas auténticas, confirmar modelo o usar solver de red/compresible adecuado, acordar garantías/ensayos, validar proyecto y aprobar humanamente. Controlar desviaciones, hashes y as-built. Paquete apoya estudios/portafolio, sin autorización automática de compra/construcción o conformidad universal.
