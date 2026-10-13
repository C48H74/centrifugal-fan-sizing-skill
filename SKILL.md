---
name: dimensionar-exaustor-centrifugo
description: Prepare traceable centrifugal fan engineering studies, duct losses, curve-based selection, standards applicability and procurement/commissioning dossiers. Use for industrial design reviews and technical cases; certification and impeller manufacture require project-specific specialist evidence.
---

# Centrifugal exhaust fan sizing

English is the primary skill language. Respond in the requested language; default to English when unspecified. Full translations: [Português](translations/pt/SKILL.md), [Español](translations/es/SKILL.md). These are translations of this skill, not independent skills. Apply the same technical criteria in all languages.

Provide traceable calculations separating supplied data, assumptions and manufacturer-verified selection. Estimated diameters or speeds do not establish a validated fan.

## Professional workflow and required reading

Revision 2.0 — international technical basis with separate EU/Brazil applicability. This skill supports company engineering workflows; it does not autonomously certify products or approve construction.

- For every engineering study read the [engineering manual](references/engineering-manual.md), [standards register](references/standards-register.md) and the applicable section of the [jurisdiction annex](references/jurisdiction-annex.md). These explain physics, method, scope and evidence; use licensed adopted standards for clause-level decisions.
- For software or a reproducible case read [software scope and worked case](references/software-and-case.md) and [input contract EN/PT/ES](references/input-contract.md). Use `scripts/engineering.py` only within its explicit single-path model; label supplied synthetic curves as illustrative.
- For vendor inquiry, procurement or commissioning use the [project dossier](templates/project-dossier.md), including data sheet, applicability matrix, bid comparison, inspection/test plan and release checklist.
- Full technical documents and dossier translations are linked from the [Portuguese](translations/pt/SKILL.md) and [Spanish](translations/es/SKILL.md) entrypoints. Keep numerical definitions, evidence status and limitations equivalent when translating.

Separate stages: conceptual estimate; preliminary engineering; vendor inquiry; purchase release; as-built verification. Progress calculations with explicit assumptions, but do not release procurement/construction with unresolved mandatory requirements or missing vendor limits. Assign preparer/checker/approver fields to real responsible people; never fabricate signatures, credentials, certified curves or clause compliance. A portfolio case must identify whether it is simulated or a real documented delivery.

Normative evidence levels: catalog verified, public method reviewed, project adopted, licensed clause verified. Record identifier/edition/amendments, applicability trigger, clause when actually reviewed, evidence, responsible owner and closure. Never treat a standards bibliography, test-method statement, CE motor or an assumed efficiency as proof of assembly conformity.


## Inputs and calculation basis

Identify application, gas, contaminants, particles, corrosion, minimum/normal/maximum temperatures, absolute pressure/altitude, density and relevant humidity. Distinguish actual inlet airflow from normalized airflow; convert by mass conservation with stated reference conditions.

Record minimum/normal/maximum flows, simultaneous demand and capture criteria. For hood capture, obtain hood geometry, source position and a documented capture-velocity criterion; do not impose one generic velocity for all contaminants.

Obtain lengths, diameters, roughness, fittings and K values, equipment, clean/dirty filters, stack and discharge conditions. Ask only for data blocking the next decision; continue preliminary calculations with explicit assumptions.

Confirm static versus total pressure and efficiency basis: ηt = Q·Δpt/P_shaft; ηs = Q·p_fan_static/P_shaft. Never combine static pressure with total efficiency. Under AMCA definitions, fan static pressure equals fan total pressure minus outlet velocity pressure; it is not automatically the static-pressure difference between connections. Check test configuration and curve basis.

## Calculations

- Q [m³/s] = Q [m³/h]/3600; 1 conventional mmH₂O (mmca) = 9.80665 Pa. Water density is implicit; do not use air density in this conversion.
- A = Q/v; circular duct D = sqrt(4Q/(πv)). Check particle transport, noise, space and losses. This is duct diameter, not impeller diameter or automatically inlet-eye diameter.
- Dry ideal gas: ρ = p_abs/(R_specific·T_K); R_air = 287.05 J/(kg·K). Do not use R_air for another gas; account for humidity/compressibility when relevant.
- Each segment: v = Q/A; Re = ρvDh/μ; Δp_f = f_Darcy·L/Dh·ρv²/2; Δp_local = ΣK·ρv²/2. State f and K sources; distinguish Darcy from Fanning factors.
- Sum losses and boundary requirements along the critical path. For parallel branches solve flow distribution and pressure balance, rather than summing branch losses in series. Include installation effects and expected filter conditions. Avoid double-counting velocity/discharge pressure and margins.
- Simplified system curve: Δp_system(Q) = Δp_constant + K_system Q² for approximately fixed quadratic resistances. Filters and controls may require separate curves. Do not force the curve through zero when a constant component exists.
- P_air [kW] = Q·Δp/1000; P_shaft = P_air/η on compatible bases. P_motor_mechanical = P_shaft/η_drive; P_electrical = P_motor_mechanical/(η_motor·η_VFD), where applicable. Do not divide by motor efficiency to select rated mechanical output.
- Select motor rating from maximum absorbed power over the permitted envelope, drive losses, ambient conditions, starting requirements and a justified margin. Avoid repeated arbitrary factors. Do not claim 10 kW is a universal commercial rating.

Use [scripts/calcular.py](scripts/calcular.py) for conversions, preliminary power and optional duct diameter. It requires pressure and efficiency bases; it does not calculate curves or select equipment. English CLI and JSON fields are the primary interface; Portuguese aliases remain supported. See [calculator instructions EN/PT/ES](references/calculator.md).

## Curves and selection

Obtain manufacturer curves specifying model, impeller, speed, density, installation, pressure and power. Correct to service conditions. For the same impeller and homologous points, approximately Q₂/Q₁ = n₂/n₁; Δp₂/Δp₁ = (ρ₂/ρ₁)(n₂/n₁)²; P₂/P₁ = (ρ₂/ρ₁)(n₂/n₁)³, assuming similar efficiency. These laws do not guarantee performance outside manufacturer limits or for arbitrary impeller trimming.

Find the fan/system intersection on matching pressure/density bases. Check stability, efficiency, maximum power, speed/tip-speed limits, materials, temperature, noise, vibration, maintenance and control method. Label charts without actual data 'illustrative'. Without manufacturer curves, report 'preliminary sizing', with model, impeller and speed unresolved.

Geometry: u₂ = πD₂n/60 only relates tip speed, impeller diameter and rotation. Q = 2πr₂b₂C_r2 approximates impeller continuity, including blockage if applicable; it does not determine casing discharge diameter. Impeller design requires velocity triangles, slip, losses and structural/balance verification. Airflow and pressure alone do not validate an impeller.

## Deliverables and sources

Provide inputs/units/origins, assumptions, equations/results, segment losses when available, operating point, separate shaft/motor/electrical powers, outstanding information and acceptance criteria. Address flammable gas or combustible dust using application-specific current references; never invent compliance.

Read [example and sources](references/example-and-sources.md) for the 12,000 m³/h case and issues in the supplied image. Verify official sources and applicable editions for current selection or normative requirements. Use manufacturer curves/manuals as equipment evidence.
