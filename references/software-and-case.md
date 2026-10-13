# Software scope, reproducibility and portfolio case

Version 2.0.0 · Inputs/outputs in SI and English · Python 3 standard library for numerical calculations.

## What each program does

`scripts/calcular.py` is the original single-duty estimator: Q, pressure conversion, compatible efficiency, shaft/motor power and optional circular duct diameter. Portuguese aliases remain supported.

`scripts/engineering.py` reads one JSON case. It computes losses along a single series path of circular ducts, including Darcy friction (laminar or Colebrook turbulent) and local K values. Equipment losses use an explicitly assumed quadratic flow/density law. The system curve freezes Darcy factors at design flow; it is an engineering approximation, not an exact network model. A nonnegative constant pressure term may be added.

The fan curve consists of ascending flow samples with pressure and shaft power at a declared density/speed and pressure basis. Correction applies homologous fan laws. Pressure and power are piecewise linearly interpolated. Every analytical intersection with the quadratic system is returned, including two roots in one interval or a tangent root. Extrapolation is prohibited; no intersection and multiple intersections require review. The local slope test is not a dynamic stability certification. The largest sampled power is the maximum of the piecewise-linear model, not necessarily the true maximum between manufacturer's measurements or outside the supplied interval.

Unknown fields, incompatible bases, non-finite/nonpositive physical inputs, invalid efficiencies, duplicate equipment IDs, non-increasing curve flows, transitional Reynolds number and energetically impossible interpolated fan data are rejected. A declared source is required for ducts/equipment/curve; the software cannot verify its authenticity. Users must verify low-pressure incompressible applicability, topology, loss conventions and applicable mechanical limits. It does not automatically select a commercial motor.

Not implemented: parallel-flow balancing, rectangular-duct friction, compressible flow, hood capture sizing, psychrometrics, particle deposition, true filter loading laws, dynamic instability, rotor design, sound propagation, vibration prediction, FEI, regulatory compliance or professional approval. No runtime dependency is needed for calculations; optional Matplotlib is needed only to reproduce graphs.

## Reproduce

```bash
python scripts/calcular.py --flow-m3h 12000 --pressure 180 --unit mmca --pressure-basis total --efficiency-basis total --efficiency 0.72
python scripts/engineering.py examples/industrial-case.json --output examples/industrial-case-results.json
python scripts/build_case.py
python -m unittest discover -s tests -v
```

Optional charts: install `matplotlib` in your chosen environment, then rerun `build_case.py`. Scripts are run from repository root. The result records numerical method version and SHA-256 of the exact input bytes. Keep input, output, vendor files and human review together; a hash proves file identity, not engineering correctness.

## Case 1 — supplied publication example

The original 12,000 m³/h and 180 mmH₂O example gives 1,765.197 Pa, 5.88399 kW air power and 8.172208 kW shaft power only if the 72% total efficiency matches total pressure. It contains no surveyed duct network or certified fan curve. See [the audited source example](example-and-sources.md). It establishes a power estimate, not a selected product.

## Case 2 — constructed industrial scenario

**Case ID CF-CASE-002-ILLUSTRATIVE.** Every geometry, K, equipment loss, efficiency and fan curve below is a training assumption, not a customer installation, delivered project or manufacturer guarantee. The publication images are illustrative AI artwork. Do not present this as commissioned commercial experience.

Actual flow is 12,000 m³/h, density 1.20 kg/m³ and viscosity 1.81×10⁻⁵ Pa·s. D-01: 20 m circular duct, 0.65 m diameter, roughness 0.15 mm, ΣK = 2.0. D-02: 10 m, 0.60 m, same roughness, ΣK = 1.5. Assumed losses at duty: hood 150 Pa, dirty filter 850 Pa, silencer 120 Pa; unrecovered 0.60 m free-discharge velocity pressure 83.3919 Pa is included once. Ambient-to-ambient total-pressure boundaries are assumed. All variable losses are quadratic, with friction factors frozen at the duty.

| Quantity | Result |
| --- | ---: |
| D-01 velocity / Darcy f / loss | 10.0453 m/s / 0.01590076 / 150.71094 Pa |
| D-02 velocity / Darcy f / loss | 11.7893 m/s / 0.01595170 / 147.25860 Pa |
| Required total pressure at design Q | 1,501.36147 Pa = 153.09626 mmH₂O |
| System coefficient K | 135.1225319 Pa/(m³/s)² |
| Air power at design Q | 5.004538 kW |
| Shaft power assuming ηt = 0.72 | 6.950748 kW |
| Motor mechanical output at duty, ηdrive = 0.97 | 7.165719 kW |
| Electrical input at duty, ηmotor = 0.92 and ηVFD = 0.97 | 8.029717 kW |

The synthetic fan data are defined at 1,500 rpm and 1.20 kg/m³. Flow samples 1/2/3/4/5 m³/s have total pressures 2400/2200/1900/1350/650 Pa and shaft powers 5/7/8.5/9.5/10 kW. These values are not a real product and do not validate an impeller diameter or maximum safe speed.

The dirty-system intersection is **12,527.06 m³/h at 1,636.14 Pa**, with **8.97974 kW shaft power** and a derived **63.4022% total efficiency**. That efficiency comes from the synthetic pressure/power curve, rather than the earlier assumed 72%. Do not combine the estimated duty-point power with the curve-based operating point. Flow is about 4.39% above the nominal target; acceptance cannot be inferred because no project tolerance was specified.

Maximum sampled shaft power is 10 kW. With assumed 97% transmission efficiency and a deliberately declared 10% project screening margin, the motor mechanical screen is 11.34021 kW. This is not a selected motor or a normative margin; confirm the full operating envelope, commercially available rating, derating, acceleration and vendor limits. Simply picking the next rating without those checks does not close selection.

## Sensitivities

| Assumed scenario | Operating Q m³/h | Total Pa | Shaft kW | Meaning |
| --- | ---: | ---: | ---: | --- |
| Dirty filter, base | 12,527.06 | 1,636.14 | 8.97974 | Constructed base case |
| Clean filter: 400 Pa at design Q | 13,944.20 | 1,419.64 | 9.37339 | Lower resistance increases flow and power on this curve |
| Denser gas: 1.40 kg/m³ | 12,528.77 | 1,908.53 | 10.47692 | Higher density raises pressure/power; slight Q change comes from recalculated f |
| Speed +10%: 1,650 rpm | 13,779.77 | 1,979.73 | 11.95203 | Approximate similarity only; mechanical speed permission not established |

The clean-filter example illustrates a motor-overload check, not a universal trend for every impeller. The 10% speed change increases homologous power by 1.1³ = 1.331. The density case also updates Reynolds-dependent duty friction before freezing its new system curve.

Numerical records: [input](../examples/industrial-case.json), [results](../examples/industrial-case-results.json), [sensitivity CSV](../examples/sensitivity.csv). [Engineering chart](../assets/engineering/case-curves.png) uses deterministic plotting, not AI-generated numerical curves.

## Acceptance and limitations of this case

Arithmetic, method invariants and failure modes are covered by automated tests. This is software verification within its stated model; it is not validation against an independent certified fan test. Normative applicability remains open because there is no project jurisdiction/date/product or licensed clause review. Capture effectiveness, material suitability, acoustic limits, vibration, hazard classification, rotor structural integrity, motor starting and FAT/SAT are not demonstrated.

Portfolio claim permitted: “Developed a multilingual, traceable preliminary fan-sizing workflow with standards applicability guidance, tested numerical tools and an explicitly synthetic industrial case.” Claim not supported: “Designed and certified an industrial fan compliant with all international regulations.”
