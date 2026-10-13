# Manual de engenharia — exaustores centrífugos

Revisão 2.0 · 13/10/2026 · Orientação e método de cálculo; não é certificado de conformidade.

## 1. Como funciona

O gás entra no rotor próximo ao eixo. As pás em rotação transferem energia mecânica ao gás, que sai para a periferia com componentes radial e tangencial de velocidade. A carcaça coleta a vazão e pode recuperar parte da energia de velocidade como pressão estática. O motor fornece potência ao eixo; mancais, transmissão e acionamento influenciam a fronteira de potência especificada.

A relação ideal de Euler é Δh₀ = u₂Cθ₂ − u₁Cθ₁, em que u é a velocidade periférica e Cθ a componente tangencial absoluta do gás. Ela explica a transferência de energia; escorregamento, incidência, vazamentos, recirculação e atrito reduzem o desempenho real. Não dimensiona um rotor fabricável apenas com Q e pressão. Para análise preliminar de baixa pressão, P_ar ≈ QΔpt. Relação de pressões elevada ou variação importante de densidade exige método compressível apropriado e revisão do fabricante.

Rotores de pás inclinadas/curvadas para trás ou perfil aerofólio são candidatos para gás limpo e eficiência elevada; contaminação pode inviabilizar aerofólios. Rotores radiais podem atender partículas, conforme carga, abrasão e limpeza reais. Pás curvadas para frente possuem curvas próprias de pressão/potência e riscos de sobrecarga. São critérios de triagem, não regras universais. Exigir limites de material, rotação, temperatura e transporte de partículas da construção proposta.

## 2. Definir a aplicação

Distinguir ventilação de conforto, extração de processo, ventilação local exaustora (VLE), transporte pneumático, extração emergencial de fumaça e atmosferas explosivas. Um ponto de operação não garante controle de contaminantes. A captação depende de momento/empuxo da fonte, enclausuramento, distância, correntes cruzadas e reposição de ar. Definir com higiene ocupacional o critério de aceitação. HSE HSG258 e ACGIH são referências úteis; suas orientações não são automaticamente lei em todos os países.

A base de projeto registra tag, processo, país/local, altitude, modos normais/anormais, redundância, horas e disponibilidade. Para o gás: composição, pressão absoluta, temperaturas mínima/normal/máxima, umidade e densidade. Para sólidos: distribuição granulométrica, concentração, aderência, abrasão e combustibilidade. Propriedades combustíveis desconhecidas são pendências, não prova de serviço sem risco.

Registrar vazão real e de referência e todos os estados de referência. Por conservação de massa, Q_real = Q_ref·ρ_ref/ρ_real. Para o mesmo gás ideal, Q_real/Q_ref = (T_real/T_ref)(p_ref/p_real), com temperaturas/pressões absolutas e correção de compressibilidade quando necessária. Esclarecer base úmida/seca. Não adicionar vazamento a uma vazão que já o inclui.

## 3. Fronteiras de pressão

Numa seção definida, p_total = p_estática + p_velocidade, sendo p_velocidade ≈ ρv²/2 no modelo de baixa velocidade. Pressão total do ventilador é total na saída menos total na entrada. Pressão estática do ventilador, na convenção de ensaio referenciada, é pressão total do ventilador menos pressão de velocidade na saída; não equivale simplesmente à diferença das leituras estáticas. Identificar planos de entrada/saída e categoria de instalação.

Categorias A/B/C/D correspondem a livre/livre, entrada livre/saída dutada, entrada dutada/saída livre e dutada/dutada. Adotar a categoria da norma de ensaio e do fabricante. Curva de catálogo para outra configuração pode não representar a instalação.

Montar balanço de pressão total entre fronteiras explícitas. Para exaustão ambiente-ambiente com velocidades desprezíveis nas fronteiras, cobrir perdas dissipativas, incluindo uma vez a energia cinética não recuperada na descarga. Para reservatórios diferentes ou equipamento pressurizado, incluir requisito real de contorno. Em chaminés quentes, avaliar empuxo pelas densidades do gás/ambiente; não impor indiscriminadamente penalidade ρgΔz de líquido a todo duto gasoso sem definir referência de pressão. Converter para pressão estática do ventilador com a seção real de saída e convenção de classificação.

## 4. Dutos e acessórios

Por trecho, tabular vazão, forma, área, diâmetro hidráulico, comprimento, rugosidade, densidade e viscosidade dinâmica. Área circular = πD²/4; diâmetro hidráulico retangular = 2ab/(a+b). Usar diâmetro hidráulico para atrito não autoriza aplicar coeficientes circulares a qualquer acessório retangular.

v = Q/A; Re = ρvDh/μ. Em escoamento circular laminar plenamente desenvolvido, f_Darcy = 64/Re. Em turbulento circular, resolver Colebrook: 1/√f = −2log₁₀[ε/(3,7D) + 2,51/(Re√f)]. Transição exige método justificado ou revisão. Δp_f = f(L/Dh)ρv²/2; Δp_acessórios = ΣKρv²/2. Vincular cada K à geometria, divisão de vazão e seção de velocidade de referência da fonte. Darcy é quatro vezes Fanning.

Usar dados licenciados ASHRAE ou ensaios/dados validados do fornecedor; registrar identificação, edição, geometria e velocidade de referência. Em transições, separar perda irreversível de pressão total de recuperação estática. Em derivações, resolver continuidade e pressões comuns; não somar ramais paralelos em série. Fornecer solução da rede ou restringir a análise a um caminho crítico declarado. Incluir coifa, conexões flexíveis, dampers, silenciadores, separadores, filtros e terminal conforme aplicação.

Escolher velocidades por transporte, deposição, erosão, ruído e energia, não por regra arbitrária de 10 m/s. Verificar separadamente classe de pressão, espessura, reforços, suportes, expansão e cargas externas; cálculo aerodinâmico não dimensiona estruturalmente o duto.

## 5. Curva do sistema e margens

Aproximação de condição fixa: Δp_sistema = Δp₀ + KQ². Parcela constante pode representar pressão fixa do processo. Fatores de atrito variam com Reynolds; filtros podem ter comportamento não quadrático e dependente de carregamento. Construir curvas limpa, normal e suja com dados dos equipamentos. Outra posição de damper ou configuração de ramais define outra curva, não apenas outro ponto da mesma curva.

Efeitos de instalação incluem redemoinho na entrada, curva próxima ao bocal, perfil distorcido, desenvolvimento insuficiente na descarga e obstruções. Revisar arranjo antes de adicionar pressão. Usar método aplicável AMCA 201 ou avaliação do fornecedor com geometria/velocidade declaradas; não adicionar percentual universal sem justificativa nem contar duas vezes.

Manter registro de margens: incerteza, incrustação, vazamento, capacidade futura e motor precisam de razão, fronteira e responsável. Mostrar casos nominal e extremos. Mais vazão pode prejudicar determinadas captações, aumentar ruído ou sobrecarregar motor; mais pressão não garante vazão útil.

## 6. Seleção com evidência

Obter seleção completa nas condições reais: modelo, diâmetro do rotor, pás, rotação, categoria de instalação, vazão, base de pressão, potência absorvida no eixo, base de eficiência, espectro sonoro e limites. Verificar listagem de certificação da família/classificação exata; associação do fabricante ou logotipo não certifica todos os produtos.

Cruzar curvas compatíveis. Respeitar faixa estável e afastamento de estol/surge declarados pelo fabricante. Inclinação negativa da diferença entre pressão do ventilador e sistema é triagem local quase estacionária restauradora, não prova de estabilidade dinâmica. Identificar múltiplas interseções. Não extrapolar curvas nem supor que máxima eficiência é sempre ponto aceitável.

Mesmo rotor e pontos homólogos: Q ∝ n, Δp ∝ ρn², P_eixo ∝ ρn³, aproximadamente. Em rotação fixa, pressão/potência variam com densidade; vazão volumétrica real homóloga permanece aproximadamente constante. Corte do rotor e grandes mudanças de rotação exigem validação; semelhança geométrica pode falhar. Verificar rotação segura e ressonâncias antes de elevar frequência do inversor.

## 7. Potência e motor

P_ar = QΔp/1000 em kW. Dividir por eficiência compatível do ventilador para potência no eixo; por eficiência da transmissão para saída mecânica do motor; depois por eficiências do motor/inversor para entrada elétrica. Se uma eficiência já inclui motor/acionamento, não dividir novamente. Usar eficiências por carga quando disponíveis.

Selecionar motor pela maior saída mecânica exigida no envelope permitido, não só potência no ponto. Incluir gás frio/denso, filtro limpo com vazão elevada, máxima rotação VFD, torque de partida/aceleração, inércia, frequência de partidas, redução por ambiente/altitude, proteção, refrigeração em baixa rotação e compatibilidade do acionamento. T_motor ≥ T_carga + J_equivalente·dω/dt; tempo de aceleração deve respeitar limites térmicos. Fator de serviço não é autorização universal de sobrecarga contínua. Fabricante confirma mancais, correias, acoplamento e rotações críticas.

Energia anual = Σ(P_elétrica,i·horas_i). Comparar ciclo de vida com mesmo perfil, tarifas, manutenção e desconto. Não aplicar lei cúbica a toda instalação com pressão fixa ou eficiência variável sem verificar o sistema real.

## 8. Ruído, vibração e interfaces

Potência sonora Lw é propriedade da fonte; pressão sonora Lp depende de distância, diretividade, ambiente, atenuação e reflexão. Pedir bandas de oitava/terço e método para entrada, saída e carcaça. Somar fontes independentes por 10log₁₀Σ10^(Li/10). dB(A) sem posição/condição não garante ruído ocupacional.

Definir categoria de aplicação, rigidez de montagem, posições, convenção RMS/pico, banda e condições fábrica/campo antes de aplicar limite de vibração. Obter valores no texto licenciado adotado/contrato; esta skill não impõe mm/s nem grau universal. Revisar fundação, pé manco, alinhamento, isoladores, cargas dos dutos, dilatação, acesso, proteções e içamento. Balanceamento não garante sozinho baixa vibração instalada.

## 9. Serviços especiais

Para explosão, exigir classificação de área, grupo de gás/poeira, limites de temperatura, avaliação de fontes de ignição e proteção por especialistas competentes. Motor Ex sozinho não torna conjunto adequado. Construção antifaísca não é automaticamente à prova de explosão nem conforme ATEX. Coletores/filtros podem exigir isolamento ou alívio próprios. Fumaça, corrosão, alta temperatura, toxicidade e nuclear exigem revisão específica.

Aplicar [registro normativo](standards-register.md) e [anexos UE/Brasil](jurisdiction-annex.md). Textos licenciados adotados e contrato são necessários para cláusulas e limites numéricos. Nenhum documento concede marcação CE/Ex, ART ou aprovação de engenharia.

## 10. Compra, ensaios e comissionamento

Usar [modelo de dossiê](project-dossier.md). Antes da compra, fechar entradas críticas, garantias, envelope, materiais, método, tolerâncias, incerteza e desvios. Definir instrumentos, testemunho e resolução de disputa. Acordar aceitação antes dos resultados.

FAT verifica configuração, dimensões, sentido de giro, proteções, certificados, balanceamento/vibração, motor/acionamento e ensaios aerodinâmicos/acústicos contratados. SAT verifica geometria instalada, alinhamento, fixação, controles, intertravamentos, rotação, vazão/pressão em planos definidos, entrada elétrica, vibração e captação. Registrar filtro, temperatura, densidade, dampers e demandas simultâneas para comparar com garantia.

Calibração deve ser rastreável; tomadas/travessias devem atender método e perfil. Para incertezas relativas independentes, u(P_eixo)/P_eixo ≈ sqrt[(uQ/Q)²+(uΔp/Δp)²+(uη/η)²]. É estimativa de primeira ordem, não substitui análise normativa. Tolerância, incerteza e margem são diferentes. Não subtrair tolerância regulatória de verificação do requisito de projeto.

Emitir como conceitual, preliminar, consulta a fornecedor, liberado para compra ou as-built somente conforme evidência. Registrar elaborador, verificador, aprovador, revisão, hashes, pendências e autoridade de fechamento. Não preencher aprovações humanas automaticamente.
