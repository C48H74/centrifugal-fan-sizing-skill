# Engineering manual — centrifugal exhaust fans

Revision 2.0 · 2026-10-13 · Engineering guidance and calculation method, not a conformity certificate.

## 1. How a centrifugal fan works

Gas enters the impeller near the shaft axis. Rotating blades transfer mechanical energy to the gas, which leaves the impeller toward the periphery with radial and tangential velocity components. The casing collects the flow and can recover part of its velocity energy as static pressure. The motor supplies shaft power; bearings, transmission and the drive affect the power boundary used in a specification.

The ideal Euler turbomachinery relation is Δh₀ = u₂Cθ₂ − u₁Cθ₁, with u the blade peripheral speed and Cθ the absolute tangential gas velocity. It explains energy transfer; real slip, incidence, leakage, recirculation and friction reduce performance. It does not determine a manufacturable impeller from Q and pressure alone. For low-pressure screening, P_air ≈ QΔpt. A large pressure ratio or significant density change requires the appropriate compressible method and vendor review, rather than silently extending this approximation.

Backward-inclined/backward-curved or airfoil impellers are candidates for efficient clean-gas service; contamination may make an airfoil unsuitable. Radial designs can be candidates for particulate service, subject to actual loading, abrasion and cleaning needs. Forward-curved impellers have their own pressure/power characteristics and overload risks. These are screening considerations, not universal selection rules. Require the supplier's material, speed, temperature and particle-handling limits for the proposed construction.

## 2. Define the task before calculating

Distinguish comfort ventilation, process extraction, local exhaust ventilation (LEV), pneumatic transport, emergency smoke extraction and explosive-atmosphere service. A fan duty is not a contaminant-control guarantee. Hood capture depends on source momentum/buoyancy, enclosure, distance, cross-drafts and make-up air. Define an exposure-control acceptance criterion with the occupational hygienist. HSE HSG258 and ACGIH design guidance are useful references; their guidance is not automatically the law in every jurisdiction.

The design basis records tag, process, site/country, altitude, normal/abnormal modes, redundancy, service hours and required availability. For the gas, record composition, pressure absolute, minimum/normal/maximum temperature, humidity and density; for solids, particle size distribution, loading, stickiness, abrasion and combustible characteristics. Unknown combustible properties are unresolved inputs, not evidence of a non-hazardous service.

Record actual versus reference volumetric flow and every reference state. From mass conservation, Q_actual = Q_ref·ρ_ref/ρ_actual. For the same ideal-gas composition, Q_actual/Q_ref = (T_actual/T_ref)(p_ref/p_actual), with absolute temperatures and pressures and a compressibility correction when necessary. Clarify wet/dry gas basis. Do not add a leakage allowance to airflow already including it.

## 3. Pressure boundaries and a consistent energy balance

At a defined section, p_total = p_static + p_velocity, with p_velocity ≈ ρv²/2 for the low-speed model. Fan total pressure is outlet total pressure minus inlet total pressure. Fan static pressure, under the referenced fan-test convention, is fan total pressure minus fan outlet velocity pressure; this is different from simply subtracting the two static readings. Label inlet/outlet test planes and installation category.

Installation categories A/B/C/D refer respectively to free/free, free inlet/ducted outlet, ducted inlet/free outlet and ducted/ducted arrangements. Use the category in the chosen test standard and manufacturer rating. A catalog curve for a different arrangement may not represent the installed system.

Build a total-pressure balance between explicit boundaries. For ambient-to-ambient exhaust with negligible boundary velocities, the fan must cover dissipative losses, including unrecovered discharge kinetic energy once. For different reservoirs or pressurized equipment add the actual boundary requirement. For hot vertical stacks evaluate buoyancy from gas and ambient density profiles; do not apply a liquid-style elevation penalty ρgΔz to every ambient gas duct without defining the pressure reference. Convert to fan static pressure only using the actual outlet reference and rating convention.

## 4. Ducts and fittings

For each segment, tabulate flow, shape, area, hydraulic diameter, length, roughness, density and dynamic viscosity. A circular area is πD²/4; a rectangular hydraulic diameter is 2ab/(a+b). Hydraulic diameter is a modeling choice for friction, not permission to reuse circular fitting coefficients for any rectangular fitting.

Calculate v = Q/A and Re = ρvDh/μ. For fully developed circular laminar flow f_Darcy = 64/Re. For turbulent circular flow, solve Colebrook: 1/√f = −2log₁₀[ε/(3.7D) + 2.51/(Re√f)]. Transitional flow is uncertain: document a justified approach or request engineering review. Then Δp_f = f(L/Dh)ρv²/2 and Δp_fittings = ΣKρv²/2. Match each K to its source geometry, flow split and reference velocity section. Darcy is four times Fanning.

Use licensed ASHRAE fitting data or validated supplier/test data; record fitting ID, edition, geometry and reference velocity. For a transition, separate irreversible total-pressure loss from static-pressure recovery. For branch junctions, solve continuity and common pressure constraints; do not add losses across parallel branches. Provide a network solution or restrict the calculation to a declared critical path. Include hood entry, flexible connections, dampers, silencers, separators, filters and stack terminal as appropriate.

Select duct velocities from contaminant transport, deposition, erosion, noise and energy constraints, not from an arbitrary 10 m/s rule. Confirm duct pressure class, wall design, stiffening, supports, expansion and external loads separately; aerodynamic sizing is not duct structural design.

## 5. System curve, uncertainty and operating modes

A fixed-condition approximation is Δp_system = Δp₀ + KQ². The constant term can represent a fixed process pressure. Friction factors change with Reynolds number; filters may have nonquadratic and loading-dependent behavior. Build clean, normal and dirty curves from equipment data. A damper position or a changed branch configuration defines another system curve, not merely another point on the same curve.

Installation effects include inlet swirl, an elbow close to the inlet, distorted approach flow, inadequate discharge development and obstructions. Evaluate layout before adding pressure. Use an applicable AMCA 201 method or vendor assessment with its geometry and velocity basis; never add an unexplained universal percentage or count an effect twice.

Keep a margin register: uncertainty, fouling, leakage, future capacity and motor allowance each need a reason, boundary and owner. Show nominal and bounding cases. More airflow can reduce capture quality in some arrangements, increase noise or overload the motor; more pressure does not guarantee useful flow.

## 6. Select using evidence

Obtain the full vendor selection at the actual gas condition: model, impeller diameter, blade type, speed, installation category, flow, pressure basis, absorbed shaft power, efficiency basis, sound spectrum and operating limits. Verify the applicable certification listing for the exact family/rating; a manufacturer's membership or logo does not establish certification of every product.

Intersect compatible fan/system curves. Review stall/surge avoidance and the stable range designated by the vendor. A negative slope of fan pressure minus system pressure is a useful local quasi-steady restoring screen, not a dynamic stability proof. Identify multiple intersections. Do not extrapolate outside supplied curves or infer that peak efficiency is always an acceptable operating point.

For unchanged impeller and homologous operation, Q ∝ n, Δp ∝ ρn² and P_shaft ∝ ρn³ approximately. At a fixed speed, pressure and power scale with density while actual volumetric flow at a homologous point remains approximately unchanged. Impeller trimming and large speed changes require manufacturer validation; similar geometry assumptions may fail. Check maximum safe speed and mechanical resonances before increasing VFD frequency.

## 7. Power chain and motor duty

P_air = QΔp/1000 in kW. Divide by compatible fan efficiency for shaft power. Divide by transmission efficiency for motor mechanical output. Divide that by motor and VFD efficiencies for electrical input. If the quoted efficiency already covers motor/drive losses, do not divide again. Use load-dependent efficiencies for energy estimates where available.

The motor is selected from maximum required mechanical output over the allowable envelope, not just duty-point shaft power. Include cold dense gas, clean-filter high flow, maximum VFD speed, starting/acceleration torque, inertia, start frequency, ambient/altitude derating, enclosure, cooling at low speed and drive compatibility. T_motor ≥ T_load + J_equivalent·dω/dt; acceleration time must also satisfy motor/drive thermal limits. A service factor is not a universal continuous overload allowance. Supplier confirmation is required for bearings, belts, coupling and critical speeds.

Annual energy = Σ(P_electrical,i·hours_i). Life-cycle comparisons use identical duty schedules, tariffs, maintenance boundaries and discount assumptions. Do not apply the cube law to an entire installation with fixed pressure or changing efficiency without checking the actual system.

## 8. Noise, vibration and mechanical interfaces

Sound power Lw is a source property; sound pressure Lp depends on distance, directivity, room, attenuation and reflections. Request octave/one-third-octave data and the test method for inlet, outlet and casing paths. Combine independent sound levels logarithmically, 10log₁₀Σ10^(Li/10). A dB(A) value without location and operating condition is not a valid workplace guarantee.

Specify fan application category, mounting rigidity, measurement positions, RMS/peak convention, frequency band and factory/site conditions before applying a vibration limit. Obtain limits from the adopted licensed standard and contract; no universal mm/s or balance grade is built into this skill. Review foundation, soft foot, alignment, isolators, duct forces, thermal movement, access, guarding and lifting points. Balance quality does not by itself guarantee low installed vibration.

## 9. Special services and release conditions

For explosion hazards, require hazardous-area classification, gas/dust group, temperature limits, ignition-risk assessment and protection strategy by competent specialists. An Ex motor alone does not make the fan assembly suitable. Spark-resistant fan construction is not automatically explosion-proof or ATEX-compliant. Filters/collectors may introduce separate explosion-isolation or venting requirements. For smoke control, corrosive, high-temperature, toxic or nuclear service, open a dedicated standards review rather than claiming general ventilation compliance covers it.

Use the [standards register](standards-register.md) and [EU/Brazil annex](jurisdiction-annex.md). The licensed adopted standards and contract are needed for clause-level checks and numerical acceptance limits. No document here grants CE/Ex marking, ART or engineering approval.

## 10. Procurement, testing and commissioning

Apply the [project dossier template](../templates/project-dossier.md). Before purchase, close critical inputs, guarantees, operating envelope, material compatibility, test method, tolerances, measurement uncertainty and deviations. Specify who supplies instruments, who witnesses testing and how disputes are resolved. Agree acceptance before seeing results.

FAT reviews configuration, dimensions, rotation, guarding, certificates, balance/vibration, motor/drive data and contracted aerodynamic/acoustic tests. SAT verifies installed geometry, alignment, anchoring, controls, interlocks, speed, airflow and pressure at defined planes, electrical input, vibration and capture effectiveness. Record filter state, temperature, density, damper positions and simultaneous demands; otherwise comparison with the guarantee is ambiguous.

Instrument calibration is traceable; pressure taps/traverses must suit the selected method and flow profile. For independent relative uncertainties, u(P_shaft)/P_shaft ≈ sqrt[(uQ/Q)²+(uΔp/Δp)²+(uη/η)²]; this is a first-order estimate, not a substitute for the standard's uncertainty analysis. Tolerances, uncertainty and design margin are different concepts. Do not subtract regulatory verification tolerances from a product design requirement.

Release as conceptual, preliminary, for vendor inquiry, approved for purchase, or as-built only when evidence supports that status. Record preparer, checker, approver, revision, input hashes, unresolved items and closure authority. Never populate human approvals automatically.
