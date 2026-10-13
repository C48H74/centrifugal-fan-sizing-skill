# Software, reprodução e case de portfólio

Versão 2.0.0 · Entradas/saídas SI em inglês · Biblioteca padrão Python 3 para cálculos.

## Programas e limites

`scripts/calcular.py` estima ponto único: conversões, eficiência compatível, potência eixo/motor e diâmetro circular opcional. Preserva aliases portugueses.

`scripts/engineering.py` lê JSON de um único caminho em série, com dutos circulares, atrito Darcy (laminar ou Colebrook turbulento) e K locais. Equipamentos usam lei quadrática declarada de vazão/densidade. Curva do sistema congela fatores de atrito na vazão de projeto: aproximação, não rede exata. Admite pressão constante não negativa.

Curva do ventilador: amostras com vazão crescente, pressão e potência no eixo, densidade/rotação e base de pressão. Corrigir por leis homólogas e interpolar pressão/potência linearmente por intervalos. Retornar todas as interseções analíticas com sistema quadrático, inclusive duas no mesmo intervalo e tangência. Proibir extrapolação; ausência/multiplicidade exige revisão. Teste de inclinação não certifica estabilidade dinâmica. Maior potência amostrada é máximo do modelo linear, não necessariamente máximo real entre medidas ou fora do intervalo.

Rejeitar campos desconhecidos, bases incompatíveis, valores físicos não finitos/não positivos, eficiências inválidas, IDs duplicados, vazões não crescentes, Reynolds de transição e curvas interpoladas energeticamente impossíveis. Fontes de dutos/equipamentos/curva são exigidas; autenticidade não é verificada. Usuário verifica baixa pressão/incompressibilidade, topologia, convenções e limites mecânicos. Não seleciona motor comercial automaticamente.

Não implementa rede paralela, atrito retangular, compressibilidade, dimensionamento de captação, psicrometria, deposição, carregamento real de filtro, instabilidade dinâmica, rotor, propagação sonora, previsão de vibração, FEI, conformidade ou aprovação profissional. Cálculos não precisam de dependências externas; Matplotlib é opcional para gráficos.

## Reprodução

Executar da raiz do repositório:

```bash
python scripts/calcular.py --flow-m3h 12000 --pressure 180 --unit mmca --pressure-basis total --efficiency-basis total --efficiency 0.72
python scripts/engineering.py examples/industrial-case.json --output examples/industrial-case-results.json
python scripts/build_case.py
python -m unittest discover -s tests -v
```

Para gráficos, instalar Matplotlib no ambiente escolhido e repetir `build_case.py`. Resultado registra versão do método e SHA-256 dos bytes de entrada. Arquivar entrada, saída, documentos do fornecedor e revisão humana juntos; hash comprova identidade, não correção de engenharia.

## Case 1 — exemplo fornecido

12.000 m³/h e 180 mmca resultam em 1.765,197 Pa, 5,88399 kW no ar e 8,172208 kW no eixo se eficiência total de 72% corresponder à pressão total. Não há rede levantada nem curva certificada. Ver [exemplo auditado](example-and-sources.md). Comprova estimativa de potência, não produto selecionado.

## Case 2 — cenário industrial construído

**CF-CASE-002-ILLUSTRATIVE.** Geometrias, K, perdas, eficiências e curva são hipóteses didáticas, não instalação de cliente, projeto entregue ou garantia do fabricante. Imagens são ilustrações IA; não apresentar como experiência comercial comissionada.

Vazão real 12.000 m³/h; densidade 1,20 kg/m³; viscosidade 1,81×10⁻⁵ Pa·s. D-01: 20 m, diâmetro 0,65 m, rugosidade 0,15 mm, ΣK = 2,0. D-02: 10 m, 0,60 m, mesma rugosidade, ΣK = 1,5. Perdas supostas no ponto: coifa 150 Pa; filtro sujo 850 Pa; silenciador 120 Pa; energia de velocidade da descarga livre 0,60 m = 83,3919 Pa, incluída uma vez. Balanço ambiente-ambiente em pressão total. Perdas variáveis quadráticas e atrito congelado no ponto.

| Grandeza | Resultado |
| --- | ---: |
| D-01 velocidade / f Darcy / perda | 10,0453 m/s / 0,01590076 / 150,71094 Pa |
| D-02 velocidade / f Darcy / perda | 11,7893 m/s / 0,01595170 / 147,25860 Pa |
| Pressão total na vazão de projeto | 1.501,36147 Pa = 153,09626 mmca |
| Coeficiente do sistema | 135,1225319 Pa/(m³/s)² |
| Potência no ar | 5,004538 kW |
| No eixo supondo ηt = 0,72 | 6,950748 kW |
| Mecânica do motor, ηtransmissão = 0,97 | 7,165719 kW |
| Elétrica, ηmotor = 0,92; ηVFD = 0,97 | 8,029717 kW |

Curva sintética a 1.500 rpm e 1,20 kg/m³: vazões 1/2/3/4/5 m³/s, pressões totais 2400/2200/1900/1350/650 Pa, potências eixo 5/7/8,5/9,5/10 kW. Não é produto real; não valida rotor nem rotação segura.

Interseção com sistema sujo: **12.527,06 m³/h a 1.636,14 Pa**, **8,97974 kW no eixo**, eficiência total derivada **63,4022%**. Essa eficiência vem da curva sintética, não dos 72% anteriormente supostos. Não combinar potência estimada do ponto nominal com operação obtida da curva. Vazão aproximadamente 4,39% acima do alvo; não há aceitação automática sem tolerância de projeto.

Maior potência amostrada 10 kW. Com transmissão suposta de 97% e margem de triagem declarada de 10%, requisito mecânico de triagem = 11,34021 kW. Não é motor selecionado nem margem normativa; confirmar envelope integral, tamanho comercial, redução ambiental, aceleração e limites. Escolher tamanho seguinte sem esses exames não encerra seleção.

## Sensibilidades

| Hipótese | Q operacional m³/h | Pa totais | kW eixo | Interpretação |
| --- | ---: | ---: | ---: | --- |
| Filtro sujo, base | 12.527,06 | 1.636,14 | 8,97974 | Caso construído |
| Filtro limpo: 400 Pa no Q nominal | 13.944,20 | 1.419,64 | 9,37339 | Menor resistência aumenta vazão/potência nesta curva |
| Gás mais denso: 1,40 kg/m³ | 12.528,77 | 1.908,53 | 10,47692 | Pressão/potência maiores; pequena mudança Q decorre de f recalculado |
| Rotação +10%: 1.650 rpm | 13.779,77 | 1.979,73 | 11,95203 | Apenas semelhança; permissão mecânica não comprovada |

Filtro limpo demonstra verificação de sobrecarga, não tendência universal. +10% de rotação aumenta potência homóloga por 1,1³ = 1,331. Caso de densidade recalcula atrito no ponto antes de congelar nova curva.

Arquivos: [entrada](../../examples/industrial-case.json), [resultados](../../examples/industrial-case-results.json), [CSV](../../examples/sensitivity.csv), [gráfico determinístico](../../assets/engineering/case-curves.png). Curvas numéricas não são geradas por IA.

## Aceitação e alegações

Testes cobrem aritmética, invariantes e falhas do modelo; não validam contra ensaio certificado independente. Aplicabilidade normativa permanece aberta sem jurisdição/data/produto e cláusulas licenciadas. Não demonstrados: captação, materiais, acústica, vibração, áreas classificadas, estrutura do rotor, partida e FAT/SAT.

Alegação sustentada: “Desenvolvi fluxo multilíngue rastreável de pré-dimensionamento com orientação normativa, ferramentas testadas e case industrial explicitamente sintético.” Não sustentada: “Projetei e certifiquei ventilador conforme todas as regulamentações internacionais.”
