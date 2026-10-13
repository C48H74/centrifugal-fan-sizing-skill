# Exemplo auditado e fontes

Dados fornecidos: Q = 12.000 m³/h; pressão = 180 mmca; eficiência total adotada = 0,72; densidade = 1,20 kg/m³; temperatura = 20 °C. Para fechar este exemplo, assumir explicitamente que a pressão é TOTAL. Se for estática, obter eficiência estática ou a pressão total correspondente.

Q = 3,333333 m³/s; Δpt = 1.765,197 Pa; P_ar = 5,88399 kW; P_eixo = 8,17221 kW. Os valores originais de 1.766 Pa e 8,2 kW são arredondamentos próximos. Não multiplicar novamente pela densidade: ela participa das perdas e correções de curvas, não é fator adicional em Q·Δp.

Com v_duto = 10 m/s, hipótese ilustrativa: A = 0,33333 m²; D_duto = 0,65147 m. Não é dimensionamento do olho do rotor. Com D_rotor = 0,40 m e u₂ = 40 m/s adotados: n = 1.909,86 rpm; isso não comprova pressão, eficiência nem compatibilidade com a entrada calculada. A expressão Q = 2πr₂b₂C_r2 estima continuidade na periferia do rotor, não diâmetro da descarga da carcaça. A imagem mistura esse D₂ estimado com outro rotor adotado; não reproduzir como projeto fechado.

Para a mesma vazão e eficiência compatível de 72%, 50 mmca implica 2,27006 kW no eixo; 300 mmca implica 13,62035 kW. Eficiência real varia com o ponto. Motor final depende da curva de potência, transmissão, envelope e partida; 8,17 kW no ponto não valida automaticamente motor de 10 kW.

Com componente constante nulo, a curva ilustrativa pelo ponto é Δp = 158,86773·Q² (Q em m³/s, pressão em Pa). Só usar como modelo assumido, não como curva medida do sistema.

## Fontes primárias consultadas em 13/10/2026

- AMCA, Straightening Out Fan Curves: https://www.amca.org/educate/articles-and-technical-papers/amca-inmotion-articles/straightening-out-fan-curves.html — bases de pressão, curvas e variáveis da seleção.
- Greenheck, Introduction to Fan Selection: https://content.greenheck.com/public/DAMProd/Original/10002/FanFundamentals.pdf — fundamentos e leis dos ventiladores.
- Greenheck, What goes into motor sizing?: https://www.greenheck.com/resources/blog/what-goes-into-motor-sizing — potência absorvida e seleção do motor.

Essas referências orientam o método; não constituem certificação do exemplo ou seleção de fabricante.
