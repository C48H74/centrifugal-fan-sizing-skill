# Dimensionar exaustor centrífugo

O inglês é o idioma principal. Responder no idioma solicitado pelo usuário; usar inglês quando não especificado. Esta é a tradução da [skill principal](../../SKILL.md), não uma skill independente.

Entregar cálculo rastreável, distinguindo dados fornecidos, hipóteses e seleção comprovada por catálogo. Não transformar estimativas de diâmetro ou rotação em equipamento validado.

## Dados e base de cálculo

Identificar aplicação, gás, contaminantes, partículas, corrosão, temperatura mínima/normal/máxima, pressão absoluta/altitude, densidade e umidade quando relevantes. Confirmar vazão real na entrada do ventilador versus vazão normalizada; converter pela conservação de massa usando as condições de referência declaradas.

Registrar vazões mínima/normal/máxima, simultaneidade e critério de captação. Para calcular captação, solicitar geometria da coifa, posição da fonte e critério documentado de velocidade de captura; não impor uma velocidade genérica para todos os contaminantes.

Obter comprimentos, diâmetros, rugosidade, acessórios e respectivos K, equipamentos, filtros limpos/sujos, chaminé e condições de descarga. Pedir somente os dados que bloqueiam a próxima decisão; continuar o cálculo preliminar com hipóteses claramente marcadas.

Confirmar se a pressão requerida é estática ou total e a base da eficiência. ηt = Q·Δpt/P_eixo; ηs = Q·p_fan_estatica/P_eixo. Não usar pressão estática com eficiência total. Na definição AMCA, pressão estática do ventilador = pressão total do ventilador menos pressão de velocidade na saída; não confundir automaticamente com diferença das pressões estáticas entre bocais. Ler a configuração de ensaio e a base das curvas.

## Cálculo

- Q [m³/s] = Q [m³/h]/3600; 1 mmca convencional = 9,80665 Pa. A densidade da água está implícita nessa unidade, não usar densidade do ar na conversão.
- A = Q/v; duto circular D = sqrt(4Q/(πv)); velocidade e diâmetro devem atender transporte de partículas, ruído, espaço e perda. Esse D é diâmetro de duto, não do rotor nem automaticamente do olho de entrada.
- Para gás ideal seco: ρ = p_abs/(R_específico·T_K), R_ar = 287,05 J/(kg·K). Não aplicar R_ar a outro gás; considerar umidade/compressibilidade quando relevante.
- Por trecho: v = Q/A; Re = ρvDh/μ; Δp_f = f_Darcy·L/Dh·ρv²/2; Δp_local = ΣK·ρv²/2. Declarar fonte de f e K; não confundir fator Darcy com Fanning.
- Somar perdas e requisitos de contorno ao longo do caminho crítico; em paralelo resolver distribuição e equilíbrio de pressões, não somar perdas dos ramos como se fossem série. Incluir efeitos de instalação e filtros nas condições previstas. Evitar dupla contagem de pressão de velocidade/descarga e margens.
- Curva simplificada: Δp_sistema(Q) = Δp_constante + K_sistema Q² para resistências quadráticas aproximadamente constantes; filtros e controles podem exigir curvas próprias. Não forçar a curva pela origem quando existir componente constante.
- P_ar [kW] = Q·Δp/1000; P_eixo = P_ar/η na base compatível. P_mec_motor = P_eixo/η_transmissão; P_elétrica = P_mec_motor/(η_motor·η_inversor), quando aplicável. Não dividir pela eficiência do motor para escolher sua potência mecânica nominal.
- Selecionar potência nominal pela maior potência absorvida no envelope permitido, perdas de transmissão, condições ambientais, partida e margem justificada. Não somar fatores arbitrários repetidos. Não afirmar que 10 kW é tamanho comercial universal.

Usar [calculadora](../../scripts/calcular.py) para conversões, potência preliminar e diâmetro de duto opcional. O script exige a base de pressão e de eficiência; não calcula curvas nem escolhe equipamento.

## Curvas e seleção

Obter curva do fabricante com modelo, rotor, rotação, densidade, instalação, pressão e potência. Corrigir para as condições de serviço. Para o mesmo rotor e pontos homólogos, aproximadamente Q₂/Q₁ = n₂/n₁; Δp₂/Δp₁ = (ρ₂/ρ₁)(n₂/n₁)²; P₂/P₁ = (ρ₂/ρ₁)(n₂/n₁)³, assumindo eficiência semelhante. Não usar leis de semelhança como garantia fora da faixa do fabricante ou para corte arbitrário do rotor.

Encontrar interseção entre curva do ventilador e sistema, na mesma base de pressão/densidade. Verificar estabilidade, eficiência, potência máxima, limites de rotação/velocidade periférica, materiais, temperatura, ruído, vibração, manutenção e método de controle. Gráficos sem dados reais devem dizer “ilustrativo”. Sem curva, concluir “pré-dimensionamento”, com modelo, rotor e rotação pendentes.

Para geometria: u₂ = πD₂n/60 apenas relaciona velocidade periférica, rotor e rotação. Q = 2πr₂b₂C_r2 é continuidade aproximada no rotor, com bloqueio se aplicável; não fornece diâmetro do bocal de saída. Projeto do rotor exige triângulos de velocidades, escorregamento, perdas e verificação estrutural/balanceamento. Não derivar um rotor validado apenas de vazão e pressão.

## Entrega e fontes

Entregar tabela de entradas/unidades/origens, hipóteses, equações e resultados, perdas por trecho quando disponíveis, ponto de operação, potência no eixo/motor/elétrica separadas, pendências e critérios para aceitação. Tratar requisitos especiais de gás inflamável ou poeira combustível conforme aplicação e referências vigentes, sem inventar conformidade.

Ler [exemplo e fontes](example-and-sources.md) para o exemplo de 12.000 m³/h e erros da imagem fornecida. Verificar fontes oficiais e edição aplicável para requisitos normativos ou seleção atual; usar curva e manual do fabricante como evidência do equipamento.

A interface principal da calculadora usa argumentos e campos JSON em inglês; os aliases portugueses continuam disponíveis. Ver [instruções EN/PT/ES](../../references/calculator.md).


## Fluxo profissional — revisão 2.0

Base internacional com anexos separados UE/Brasil. Apoia engenharia empresarial; não certifica produto nem aprova construção automaticamente.

Para todo estudo, ler [manual de engenharia](engineering-manual.md), [registro normativo](standards-register.md) e [anexo de jurisdição](jurisdiction-annex.md). Para cláusulas e limites, usar textos licenciados adotados. Para cálculos reproduzíveis, ler [software e case](software-and-case.md) e [contrato de entrada EN/PT/ES](../../references/input-contract.md). Usar `scripts/engineering.py` apenas no modelo explícito de caminho único; identificar curvas sintéticas como ilustrativas. Para consulta/compra/comissionamento, usar [dossiê](project-dossier.md), com folha de dados, matriz, propostas, inspeções/ensaios e checklist. Preservar equivalência técnica/evidências/limitações nas traduções.

Separar conceitual, preliminar, consulta, compra e as-built. Continuar cálculos com hipóteses explícitas, mas não liberar compra/construção com requisitos obrigatórios ou limites do fornecedor pendentes. Elaborador/verificador/aprovador devem ser pessoas responsáveis reais; não inventar assinatura, credencial, curva certificada ou conformidade de cláusula. Case distingue simulação de entrega real documentada.

Evidência normativa: catálogo verificado, método público revisado, adotada no projeto, cláusula licenciada verificada. Registrar identificação/edição/emendas, gatilho, cláusula conferida, evidência, responsável e fechamento. Bibliografia, menção de método, motor CE ou eficiência suposta não comprovam conformidade do conjunto.
