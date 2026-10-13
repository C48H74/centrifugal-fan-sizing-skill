# Audited example and sources

Inputs: Q = 12,000 m³/h; pressure = 180 mmH₂O; assumed total efficiency = 0.72; density = 1.20 kg/m³; temperature = 20 °C. Explicitly assume TOTAL pressure. If static, obtain static efficiency or corresponding total pressure.

Q = 3.333333 m³/s; Δpt = 1,765.197 Pa; P_air = 5.88399 kW; P_shaft = 8.17221 kW. Original values 1,766 Pa and 8.2 kW are close rounded values. Density affects losses/curve corrections; do not multiply by density again in Q·Δp.

Illustrative duct velocity 10 m/s gives A = 0.33333 m², D_duct = 0.65147 m; this does not validate the impeller eye. Assumed D_impeller = 0.40 m and u₂ = 40 m/s give n = 1,909.86 rpm, without proving pressure, efficiency or inlet compatibility. Q = 2πr₂b₂C_r2 describes approximate impeller peripheral continuity, not casing discharge diameter. The supplied image mixes this estimated D₂ with another assumed impeller; do not reproduce it as a completed design.

At the same flow and compatible efficiency of 72%, 50 mmH₂O requires 2.27006 kW at the shaft; 300 mmH₂O requires 13.62035 kW. Actual efficiency changes with operating point. Motor selection depends on power curve, drive, operating envelope and starting; 8.17 kW at one point does not automatically validate a 10 kW motor.

With zero constant component, an illustrative system curve through this point is Δp = 158.86773·Q² (Q in m³/s, pressure in Pa). This is an assumed model, not measured system data.

## Primary sources consulted on 2026-10-13

- [AMCA: Straightening Out Fan Curves](https://www.amca.org/educate/articles-and-technical-papers/amca-inmotion-articles/straightening-out-fan-curves.html): pressure bases, curves and selection variables.
- [Greenheck: Introduction to Fan Selection](https://content.greenheck.com/public/DAMProd/Original/10002/FanFundamentals.pdf): fundamentals and fan laws.
- [Greenheck: What goes into motor sizing?](https://www.greenheck.com/resources/blog/what-goes-into-motor-sizing): absorbed power and motor selection.

These sources support the method; they do not certify this example or establish a manufacturer selection. Translations: [PT](../translations/pt/example-and-sources.md), [ES](../translations/es/example-and-sources.md).
