# Engineering calculator input contract

The executable example is [industrial-case.json](../examples/industrial-case.json). JSON keys use English and SI units. Unknown keys are rejected to catch misspellings and implicit unit changes. The program supports one circular-duct series path, not a full branched installation. Project metadata, norms, limits and approvals belong in the dossier, not unrecognized JSON fields.

| Field | Type / unit | Requirement |
| --- | --- | --- |
| case_id | string | Stable project/case identifier |
| evidence | illustrative or project_supplied | Declaration only; does not authenticate the inputs |
| flow_m3h | positive number, actual inlet m³/h | User must convert normalized/wet-dry basis first |
| density_kgm3 | positive number | Service density; not water density |
| viscosity_Pas | positive number | Dynamic viscosity at service condition, not kinematic viscosity |
| pressure_basis / efficiency_basis | total or static | Must match; conversion is not inferred |
| constant_pressure_Pa | nonnegative number | Explicit fixed boundary requirement; negative buoyancy contribution needs separate engineering treatment |
| segments | array, may be empty | Every listed segment carries the same actual Q and density in this single-path model |
| components | array, may be empty | Fixed-condition equipment losses with declared quadratic law |
| fan_efficiency | fraction >0 and ≤1 | Assumed duty-point efficiency, not automatically the curve-derived efficiency |
| drive_efficiency | optional fraction | Defaults to 1; mechanical drive losses |
| motor_efficiency | optional fraction | Enables electrical input estimate |
| vfd_efficiency | optional fraction | Requires motor_efficiency; absent means no additional VFD loss in electrical estimate |
| motor_margin_fraction | optional nonnegative number | Defaults to zero; applied only to sampled-curve envelope screen, never a normative default |
| fan_curve | optional object | Enables curve intersection; absence leaves only duty estimates |

Every segment requires `id`, `length_m`, `diameter_m`, `roughness_m`, `K_sum`, `source`. Length/roughness/K are nonnegative; diameter is positive. Relative roughness must be below 0.05 for the supported screening model. Source must explain coefficient/geometry origin or explicitly declare an assumption. IDs across segments/components must be unique nonempty strings. K uses that segment's velocity pressure; convert a source coefficient if its reference section differs.

Every component requires `id`, `reference_loss_Pa`, `reference_flow_m3s`, `reference_density_kgm3`, `source`. Loss is nonnegative and reference flow/density positive. The program applies Δp = Δpref(Q/Qref)²(ρ/ρref). Do not enter a real filter that does not follow this law without explicitly accepting the approximation or calculating it outside the tool. Do not enter the same outlet kinetic loss in both K and an equipment component.

The curve requires `source`, `evidence` (illustrative/manufacturer_supplied), `basis`, `reference_density_kgm3`, `reference_speed_rpm`, `operating_speed_rpm` and `points`. Each point requires nonnegative `flow_m3s` and `pressure_Pa`, positive `shaft_power_kW`. Flows are strictly increasing. The basis must match the system. The tool checks thermodynamic plausibility of sampled and interpolated values, not manufacturer authenticity, safe RPM or accuracy. Record vendor document revision, rating arrangement and limits in the dossier.

## Interpretation and release

The `design` block uses the assumed fan efficiency at the specified design Q. The `fan.intersections` block uses interpolated shaft power and derives compatible efficiency at the calculated operating point. These are distinct calculations. `motor_screen_mechanical_kW` uses the maximum sampled/interpolated envelope, transmission and declared margin; it is not a selected commercial motor. No-result/multiple-result conditions are reported for human review. The release status remains preliminary regardless of supplied evidence labels.

## Português

Chaves JSON em inglês/SI; campos desconhecidos são rejeitados. O modelo admite um caminho em série com dutos circulares e mesma vazão/densidade; não resolve ramais. `flow_m3h` é vazão real de entrada; converter normalização/base úmida-seca antes. `density_kgm3` é densidade do gás; `viscosity_Pas` é viscosidade dinâmica. Bases `total|static` de pressão/eficiência coincidem. Pressão constante não negativa; contribuição negativa de empuxo requer tratamento externo.

Trechos: `id`, `length_m`, `diameter_m`, `roughness_m`, `K_sum`, `source`; dimensões e fontes conforme tabela inglesa. Comprimento/rugosidade/K não negativos, diâmetro positivo, rugosidade relativa <0,05. IDs únicos; K usa pressão de velocidade do próprio trecho. Componentes: `id`, `reference_loss_Pa`, `reference_flow_m3s`, `reference_density_kgm3`, `source`. Lei Δp = Δpref(Q/Qref)²(ρ/ρref); perda não negativa, Qref/ρref positivos. Filtro não quadrático exige aceitação explícita da aproximação ou cálculo externo. Não duplicar energia de descarga.

`fan_efficiency` suposta no ponto; `drive_efficiency` opcional assume 1. `motor_efficiency` habilita elétrica; `vfd_efficiency` exige eficiência do motor e, quando ausente, não adiciona perda VFD. `motor_margin_fraction` assume zero, só afeta triagem do envelope e não é margem normativa. `fan_curve` opcional contém fonte, evidência, base, densidade, rotação referência/operação e pontos de Q/pressão/potência no eixo. Q cresce; pressão/Q não negativos, potência positiva. Verifica plausibilidade, não autenticidade/rotação segura. Registrar revisão do fornecedor, arranjo e limites no dossiê. `case_id` identifica caso e `evidence` declara origem.

Bloco `design` usa eficiência suposta na vazão especificada; `fan.intersections` usa potência da curva e deriva eficiência operacional. Não misturá-los. Triagem mecânica do motor usa máximo do envelope fornecido, transmissão/margem; não seleciona tamanho comercial. Ausência/multiplicidade exige revisão. Status sempre preliminar, independentemente dos rótulos de evidência.

## Español

Claves JSON en inglés/SI; campos desconocidos rechazados. Modelo de un recorrido en serie con conductos circulares y mismo caudal/densidad; no ramales. `flow_m3h` es caudal real de entrada; convertir normalización/base húmeda-seca previamente. `density_kgm3` es densidad del gas; `viscosity_Pas`, viscosidad dinámica. Bases `total|static` de presión/rendimiento coinciden. Presión constante no negativa; flotabilidad negativa requiere tratamiento externo.

Tramos: `id`, `length_m`, `diameter_m`, `roughness_m`, `K_sum`, `source`, según tabla inglesa. Longitud/rugosidad/K no negativos, diámetro positivo, rugosidad relativa <0,05. IDs únicos; K usa presión de velocidad del tramo. Componentes: `id`, `reference_loss_Pa`, `reference_flow_m3s`, `reference_density_kgm3`, `source`. Ley Δp = Δpref(Q/Qref)²(ρ/ρref); pérdida no negativa, Qref/ρref positivos. Filtro no cuadrático necesita aceptación explícita de aproximación o cálculo externo. No duplicar energía de descarga.

`fan_efficiency` supuesta en diseño; `drive_efficiency` opcional supone 1. `motor_efficiency` habilita electricidad; `vfd_efficiency` exige rendimiento del motor y, ausente, no añade pérdida VFD. `motor_margin_fraction` supone cero, solo cribado de rango y no margen normativo. `fan_curve` opcional contiene fuente, evidencia, base, densidad, giro de referencia/operación y puntos Q/presión/potencia al eje. Q creciente; Q/presión no negativos, potencia positiva. Comprueba plausibilidad, no autenticidad/giro seguro. Registrar revisión, configuración y límites del proveedor en expediente. `case_id` identifica caso y `evidence` declara origen.

`design` usa rendimiento supuesto al caudal especificado; `fan.intersections` usa potencia de curva y deriva rendimiento operativo. No mezclarlos. Cribado mecánico del motor usa máximo del rango suministrado, transmisión/margen; no selecciona tamaño comercial. Ausencia/multiplicidad exige revisión. Estado siempre preliminar, independientemente de evidencia declarada.
