---
title: "Dados pessoais na LGPD, no ECA Digital e na HIPAA"
type: research
status: concluida
created: 2026-11-19
post: "[[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/post]]"
---

> [!tldr] TL;DR
> - "PII" é termo do governo dos EUA (NIST/OMB). A LGPD fala em **dado pessoal**. A HIPAA, em **PHI** (*individually identifiable health information*).
> - LGPD: dado pessoal é **qualquer** informação de pessoa identificada **ou identificável**. Não há lista de campos. Há o rol de **sensíveis** (art. 5º, II) e o regime de **criança e adolescente** (art. 14).
> - ECA Digital (Lei 15.211/2025, em vigor desde 17/03/2026) **não define dado pessoal**: remete à LGPD. O que ele acrescenta são **proibições de uso** (perfilamento para publicidade, reuso de dado de verificação de idade).
> - HIPAA é a única com **lista fechada**: os 18 identificadores do Safe Harbor (45 CFR 164.514(b)(2)). Mas só vale para *covered entities* e *business associates*.
> - Hash não resolve sozinho: a ANPD (estudo preliminar) admite hash unidirecional como anonimização; o Grupo do Artigo 29 e o HHS dizem que hash sem chave é reversível ou identificador.

## Pergunta

Quais são os dados pessoais definidos pela LGPD, pelo ECA Digital e pela HIPAA?

Para cada lei: o termo usado, a definição literal, as categorias especiais, o que conta como anonimizado e a lista concreta, quando existe.

## Resposta curta

### O termo de cada norma

| Norma | Termo | Onde |
|---|---|---|
| LGPD (Brasil) | dado pessoal · dado pessoal sensível · dado anonimizado | art. 5º, I, II e III[^1] |
| ECA Digital (Brasil) | não define; usa "dados pessoais" da LGPD | arts. 2º, 3º e 7º[^2] |
| HIPAA (EUA) | *health information* · *individually identifiable health information* · *protected health information* (PHI) | 42 U.S.C. § 1320d(4) e (6)[^8]; 45 CFR 160.103[^9] |
| NIST SP 800-122 (EUA, governo federal) | *personally identifiable information* (PII) | seção 2.1, p. 2-1[^12] |

> [!warning] "PII" não é termo da LGPD nem da HIPAA
> O NIST usa a definição da OMB (governo federal dos EUA)[^12]. No post, use "dado pessoal" para o Brasil e "PHI" para saúde nos EUA.

### LGPD (Lei 13.709/2018)

**Definições (art. 5º)**[^1]

> "I - dado pessoal: informação relacionada a pessoa natural identificada ou identificável;"

> "II - dado pessoal sensível: dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural;"

> "III - dado anonimizado: dado relativo a titular que não possa ser identificado, considerando a utilização de meios técnicos razoáveis e disponíveis na ocasião de seu tratamento;"

> "XI - anonimização: utilização de meios técnicos razoáveis e disponíveis no momento do tratamento, por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo;"

**O que isso quer dizer para o dev**

- Não há lista de campos. Basta a informação se ligar a alguém **identificável**[^1].
- Exemplos dados pela ANPD (estudo preliminar, p. 7)[^7]:
  - **identificador direto**: nome completo, CPF;
  - **identificador indireto** ("quase-identificador"): nacionalidade, idade, raça, CEP, características fenotípicas, endereço IP.
- Dado que **revela** um sensível também entra no regime do art. 11 (art. 11, § 1º)[^1].
- Dados usados para **perfil comportamental** podem ser dado pessoal, se a pessoa for identificada (art. 12, § 2º)[^1].

**Anonimizado e pseudonimizado**

- Anonimizado **não é** dado pessoal. Exceção: quando a anonimização é revertida com "meios próprios" ou "com esforços razoáveis, puder ser revertido" (art. 12, caput)[^1].
- O razoável se mede por "custo e tempo necessários para reverter", "tecnologias disponíveis" e "meios próprios" (art. 12, § 1º)[^1].
- Pseudonimização (art. 13, § 4º)[^1]:

  > "a pseudonimização é o tratamento por meio do qual um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo, senão pelo uso de informação adicional mantida separadamente pelo controlador em ambiente controlado e seguro."

- ⚠️ A LGPD não diz, com essas palavras, que pseudonimizado continua pessoal. É inferência: o controlador reverte com meio próprio, e isso cai na exceção do art. 12. A ANPD vai no mesmo sentido: "pseudonimização não é o mesmo que anonimização" (estudo preliminar, p. 28)[^7].
- A ANPD também diz: "A anonimização não é para sempre" e "Criptografia típica não é anonimização" (p. 28)[^7].

**Categorias especiais**

| Categoria | Regra | Fonte |
|---|---|---|
| Sensível | Só nas hipóteses do art. 11 (consentimento específico e destacado, ou as alíneas do inciso II) | art. 11[^1] |
| Saúde | Vedado compartilhar para vantagem econômica, salvo exceções; operadora de plano não pode usar para seleção de risco | art. 11, §§ 4º e 5º[^1] |
| Criança e adolescente | "em seu melhor interesse"; para **criança**, consentimento específico e em destaque de um dos pais (§ 1º) | art. 14[^1] |

- Quem é criança? A LGPD não define. O ECA (Lei 8.069/1990), art. 2º[^4]: criança é "a pessoa até doze anos de idade incompletos, e adolescente aquela entre doze e dezoito anos de idade."
- A ANPD fixou que dado de criança e adolescente pode usar **qualquer** base do art. 7º ou 11, "desde que observado e prevalecente o seu melhor interesse" (Enunciado CD/ANPD nº 1/2023)[^5].
- Dado de criança **não é** dado sensível pelo texto da lei. O relator do Enunciado na ANPD escreveu que o rol do art. 5º, II, "que considero taxativo", não inclui "categoria de titulares" (voto, p. 5)[^6].

### ECA Digital (Lei 15.211/2025)

**Dados da norma (conferidos no texto do Planalto)**[^2]

| Item | Valor |
|---|---|
| Número e data | Lei nº 15.211, de 17 de setembro de 2025 |
| Nome | Estatuto Digital da Criança e do Adolescente |
| Vigência | 17 de março de 2026 (art. 41-A, na redação da Lei nº 15.352/2026; antes, MP 1.319/2025 dava "seis meses após a data de sua publicação") |
| Decreto regulamentador | Decreto nº 12.880, de 18 de março de 2026, em vigor na publicação (art. 54)[^3] |
| Quem regula e fiscaliza | ANPD (Decreto 12.880, art. 1º, parágrafo único)[^3] |

**Define dado pessoal?** Não.

- O art. 2º define 12 termos (produto de TI, perfilamento, rede social, supervisão parental etc.). Nenhum é "dado pessoal"[^2].
- Criança e adolescente: usa o art. 2º do ECA de 1990 (art. 2º, § 1º)[^2].
- Privacidade e proteção de dados: "nos termos definidos nas Leis nºs 8.069 [...] e 13.709 [...] (Lei Geral de Proteção de Dados Pessoais)" (art. 3º)[^2].

**O que ele acrescenta (regras de uso, não novas categorias)**[^2]

- **Alcance amplo**: vale para produto "direcionado a crianças e a adolescentes **ou de acesso provável por eles**" (art. 1º).
- **Perfilamento** (art. 2º, V): "qualquer forma de tratamento de dados pessoais [...] para avaliar certos aspectos de uma pessoa natural [...]".
- **Proibido** perfilamento para publicidade a criança e adolescente, inclusive com "análise emocional" (art. 22).
- **Proibido** perfil comportamental para publicidade com dados pessoais, "inclusive daqueles obtidos nos processos de verificação de idade, bem como de dados grupais e coletivos" (art. 26).
- **Dado de verificação de idade**: "poderão ser utilizados unicamente para essa finalidade" (art. 13).
- **Sinal de idade por API**: minimização; "vedado qualquer compartilhamento contínuo, automatizado e irrestrito" (art. 12, § 1º).
- **Privacidade por padrão**: "configuração no modelo mais protetivo disponível" (art. 7º).

**O que o Decreto 12.880/2026 detalha**[^3]

- "sinal de idade": credencial que atesta idade ou faixa "sem revelar dados pessoais adicionais" (art. 2º, VI).
- "aferição de idade" pode usar "análise documental, biométrica e de padrões de uso" (art. 2º, IV).
- Na aferição de idade (art. 24): minimização (IV), segurança (VII) e "vedação à rastreabilidade da identidade e do histórico de acessos, solicitações e verificações" (VIII).

### HIPAA (EUA)

**Definições**

- *Individually identifiable health information* (42 U.S.C. § 1320d(6))[^8]:

  > "any information, including demographic information collected from an individual, that— (A) is created or received by a health care provider, health plan, employer, or health care clearinghouse; and (B) relates to the past, present, or future physical or mental health or condition of an individual, the provision of health care to an individual, or the past, present, or future payment for the provision of health care to an individual, and— (i) identifies the individual; or (ii) with respect to which there is a reasonable basis to believe that the information can be used to identify the individual."

  Tradução: "qualquer informação, inclusive dado demográfico coletado do indivíduo, que (A) é criada ou recebida por prestador de saúde, plano de saúde, empregador ou *clearinghouse*; e (B) se refere à saúde física ou mental passada, presente ou futura, à prestação de cuidado ou ao pagamento por ele, e (i) identifica o indivíduo; ou (ii) para a qual há base razoável para crer que pode ser usada para identificá-lo."

- *Protected health information* (45 CFR 160.103)[^9]: é a informação acima, "transmitted by electronic media", "maintained in electronic media" ou "in any other form or medium".
  Tradução: "transmitida por meio eletrônico", "mantida em meio eletrônico" ou "em qualquer outra forma ou meio".
- **Fora da PHI** (160.103, item 2)[^9]: registros escolares da FERPA; registros de emprego mantidos pela entidade como empregadora; pessoa falecida há mais de 50 anos.
- **Quem está sujeito**: *covered entity* (plano de saúde, *clearinghouse*, prestador que transmite dado de saúde eletronicamente) e *business associate*[^9]. App de saúde que não é nenhum desses fica fora da HIPAA (inferência da definição; ver "Em aberto").

**Desidentificação (45 CFR 164.514)**[^10]

- Padrão (a): não é PHI a informação que não identifica e para a qual "there is no reasonable basis to believe that the information can be used to identify an individual" ("não há base razoável para crer que pode identificar alguém").
- Dois caminhos (b):
  1. **Expert Determination** (b)(1): especialista conclui que o risco é "very small" ("muito pequeno") e documenta. O HHS diz que não há número fixo para "very small" (guia, seção 2.3, p. 10)[^11].
  2. **Safe Harbor** (b)(2): remover os 18 identificadores **e** não ter "actual knowledge" ("conhecimento efetivo") de que o resto identifica.
- Código de reidentificação (c)(1): "is not derived from or related to information about the individual" ("não é derivado nem relacionado a informação sobre o indivíduo").

**Os 18 identificadores do Safe Harbor** (164.514(b)(2)(i), do indivíduo, de parentes, empregadores ou moradores da casa)[^10]

| # | Identificador | Detalhe |
|---|---|---|
| A | Nomes | |
| B | Subdivisão geográfica menor que estado | Rua, cidade, condado, CEP (ZIP). Exceção: 3 primeiros dígitos do ZIP se a área tiver mais de 20.000 pessoas; senão, "000" |
| C | Elementos de data (menos o ano) | Nascimento, internação, alta, óbito. Idade acima de 89 vira "90 ou mais" |
| D | Telefone | |
| E | Fax | |
| F | E-mail | |
| G | SSN (equivale ao CPF) | |
| H | Número de prontuário | |
| I | Número de beneficiário do plano | |
| J | Número de conta | |
| K | Número de certificado ou licença | |
| L | Identificador de veículo e placa | |
| M | Identificador e serial de dispositivo | |
| N | URL | |
| O | Endereço IP | |
| P | Biometria (digital, voz) | |
| Q | Foto de rosto inteiro e imagens comparáveis | |
| R | Qualquer outro número, característica ou código único | Salvo o código do item (c) |

**Como o HHS lê a lista**[^11]

- Parte de identificador também identifica: iniciais ou "the last four digits of a Social Security number" não passam (seção 3.2, p. 25).
- Hash sem chave é identificador: "a code derived from a secure hash function without a secret key (e.g., 'salt') would be considered an identifying element" (seção 3.5, p. 26).
  Tradução: "um código derivado de função de hash segura sem chave secreta (ex.: 'sal') seria considerado elemento identificador".
- Hash com chave só pelo caminho do especialista, "provided the keys associated with such functions are not disclosed" ("desde que as chaves não sejam reveladas") (seção 2.9, p. 22).
- Texto livre conta: "an identifier listed in the Safe Harbor standard must be removed regardless of its location in a record" ("deve ser removido onde quer que esteja no registro") (seção 3.10, p. 29).
- Risco zero não existe: "Although the risk is very small, it is not zero" (p. 6).

**Atenção: *limited data set* ainda é PHI** (164.514(e)(2))[^10]. Ele tira 16 identificadores diretos, mas pode manter cidade, estado, ZIP e datas. Só serve para pesquisa, saúde pública ou operações, com acordo de uso de dados.

**Categorias especiais na HIPAA**

- A própria PHI já é a categoria "saúde". Nas definições lidas (160.103 e 164.514), não há categoria separada para dado de criança[^9][^10].

### PII no NIST SP 800-122 (referência dos EUA)

> "any information about an individual maintained by an agency, including (1) any information that can be used to distinguish or trace an individual's identity, such as name, social security number, date and place of birth, mother's maiden name, or biometric records; and (2) any other information that is linked or linkable to an individual, such as medical, educational, financial, and employment information." (seção 2.1, p. 2-1)[^12]

Tradução: "qualquer informação sobre um indivíduo mantida por um órgão, incluindo (1) qualquer informação que possa ser usada para distinguir ou rastrear a identidade de alguém, como nome, número do seguro social, data e local de nascimento, nome de solteira da mãe ou registros biométricos; e (2) qualquer outra informação ligada ou ligável a um indivíduo, como dados médicos, educacionais, financeiros e de emprego."

- O NIST também diz que **parte** do SSN (primeiros ou últimos dígitos) costuma ser PII, por ser "nearly unique" ("quase único") (nota 21, p. 2-2)[^12].

### Por que "quase-identificador" importa

- Sweeney (2000): 87% da população dos EUA era provavelmente única só por {ZIP de 5 dígitos, gênero, data de nascimento}, com dados do Censo de 1990 (p. 2)[^14].
- Golle (2006) refez a conta: 61% (1990) e 63% (2000) (p. 2)[^15]. Ver Divergências.
- A ANPD cita o estudo de Sweeney como exemplo de "combinações únicas" (estudo preliminar, p. 7)[^7].

### Quadro comparativo para o dev

| Pergunta | LGPD | ECA Digital | HIPAA |
|---|---|---|---|
| Termo | dado pessoal | (o da LGPD) | IIHI / PHI |
| Escopo | Qualquer tratamento de dado de pessoa natural | Produto de TI para criança/adolescente **ou de acesso provável** | Só *covered entity* e *business associate* |
| Tem lista de campos? | Não. Critério: identificado ou identificável | Não | Sim, para desidentificar: 18 identificadores |
| Categoria especial | Sensível (rol do art. 5º, II); criança e adolescente (art. 14) | Criança e adolescente; dado de verificação de idade | Toda PHI é de saúde |
| Anonimizado sai da lei? | Sim, se não reversível com esforço razoável | (o da LGPD) | Sim, se desidentificado por (b)(1) ou (b)(2) |
| Pseudonimizado sai da lei? | Não (inferência do art. 12 + art. 13, § 4º) | (o da LGPD) | *Limited data set* continua PHI |
| Hash resolve? | Divergente (ver abaixo) | — | Sem chave: não. Com chave: só via especialista |
| Proibição de uso específica | Saúde para seleção de risco (art. 11, § 5º) | Perfilamento para publicidade; reuso do dado de idade | — |

**Campo a campo** (síntese desta pesquisa; não é regra de nenhuma lei)

| Campo | LGPD | HIPAA (Safe Harbor) | Sugestão para obfuscar |
|---|---|---|---|
| Nome | Identificador direto[^7] | A | Remover ou trocar por pseudônimo aleatório |
| CPF / SSN | Identificador direto[^7] | G | Remover. "Últimos 4 dígitos" não basta[^11][^12] |
| E-mail, telefone | Pessoal (identificável) | D, F | Remover ou mascarar |
| Endereço, CEP | Quase-identificador[^7] | B (ZIP só 3 dígitos, se > 20 mil hab.) | Generalizar (cidade/UF) |
| Data de nascimento | Quase-identificador (idade)[^7] | C (só o ano; > 89 vira "90+") | Faixa etária ou só o ano |
| IP | Quase-identificador[^7] | O | Truncar ou remover |
| ID de dispositivo, URL | Pessoal se ligável | M, N | Remover |
| Foto de rosto, digital, voz | **Sensível** (biométrico)[^1] | P, Q | Não guardar a matéria-prima, se der |
| Saúde, raça, religião, sexualidade, sindicato, política | **Sensível**[^1] | É a própria PHI (saúde) | Separar, restringir acesso, cifrar |
| Conta bancária, dado financeiro | Pessoal, **não** sensível pelo rol (divergente)[^16] | J (número de conta) | Tratar como crítico: pode revelar sensível[^16] |
| Idade de criança / sinal de idade | Criança (art. 14); ECA Digital art. 13[^2] | — | Usar só para verificar idade; nunca para perfil |
| Logs de comportamento | Pessoal se formar perfil de identificado (art. 12, § 2º)[^1] | — | Agregar; com criança, não usar para publicidade[^2] |
| Texto livre (observação, chat) | Pode conter qualquer um acima | Conta como PHI[^11] | Varrer antes de exportar |

## Divergências

| Tema | Fonte A diz | Fonte B diz | Nota |
|---|---|---|---|
| Rol de sensíveis (art. 5º, II) é fechado? | Castro, Mano e Baronovsky (2021): rol fechado; "parece não restar dúvidas ou haver dissenso na doutrina"[^16]. Relator do Enunciado na ANPD: "que considero taxativo"[^6] | Dalese (2021): os exemplos "não se mostram taxativos"; apoia-se no art. 11, § 1º e em inferência por Big Data[^17] | A ANPD não fixou isso em norma. O voto é opinião do relator. A frase "sem dissenso" é refutada pela própria existência de Dalese. O art. 11, § 1º amplia o **regime** a dado que **revela** sensível, sem mudar o rol |
| Dado financeiro é sensível? | Texto da LGPD: não está no rol[^1]. Castro et al.: não é, mas propõem a categoria "dados críticos" (fora da lei)[^16] | Dalese: rol aberto permitiria incluir casos não previstos[^17] | Para o post: "não é sensível pela letra da lei; pode revelar sensível" |
| Art. 14: só consentimento para dado de criança? | Corrente (i): consentimento dos pais como única base. Era o entendimento do parecer da Comissão Especial do PL 4060/2012 (citado no voto, p. 4)[^6]. Corrente (ii): dado de criança equiparado a sensível, só bases do art. 11[^6] | Enunciado CD/ANPD nº 1/2023: qualquer base dos arts. 7º ou 11, com melhor interesse[^5]. Lefosse: discussão "superada"[^18] | Vence o Enunciado por ser ato da autoridade. O consentimento do § 1º continua exigido **quando** a base for consentimento |
| Hash unidirecional anonimiza? | ANPD, estudo preliminar (Apêndice I, f): algoritmos "de hash" com processamento unidirecional "atendem os requisitos da anonimização, desde que os dados cifrados sejam úteis" (p. 22 e 28)[^7] | Grupo do Art. 29 (WP216, 2014): pseudonimização "is not a method of anonymisation"; hash do número de identidade nacional se reverte por força bruta (p. 20)[^13]. HHS: hash sem chave é identificador (p. 26)[^11] | O texto da ANPD é **estudo preliminar** de consulta pública, não norma. Não achei versão final do guia (ver "Em aberto"). Para dev: CPF tem espaço pequeno (~10⁹ valores), então hash sem chave cai em força bruta |
| Reidentificação: só meios próprios ou também de terceiros? | LGPD art. 12, § 1º: "a utilização exclusiva de meios próprios"[^1]. ANPD, Apêndice I (b): "recursos tecnológicos próprios do agente" (p. 28)[^7] | ANPD, § 52: avaliar também "a atuação de outras pessoas ou entidades que, com meios e esforços razoáveis, podem reidentificar" (p. 16)[^7] | Tensão dentro do mesmo estudo. O § 52 lê o caput do art. 12 ("com esforços razoáveis, puder ser revertido") como aberto a terceiros |
| Unicidade por {CEP, gênero, nascimento} | Sweeney (2000): 87% da população dos EUA (Censo 1990)[^14] | Golle (2006): 61% (1990) e 63% (2000); "we can not explain this discrepancy"[^15] | Golle é revisado (ACM WPES'06); Sweeney é *working paper*. Os dois concordam que poucos atributos identificam muita gente |

## Para o post

**Frases seguras**

- "A LGPD não traz uma lista de campos pessoais. Basta a informação apontar para alguém identificável."[^1]
- "O ECA Digital não redefine dado pessoal; ele proíbe usos, como o perfil para publicidade e o reuso do dado de verificação de idade."[^2]
- "A HIPAA é a única das três com lista: os 18 identificadores do Safe Harbor. E mesmo removendo os 18, você não pode saber que o resto identifica."[^10]
- "Para a ANPD, anonimização não é para sempre."[^7]
- "Pseudonimizar reduz risco, mas o dado continua pessoal." (inferência da LGPD; ANPD e WP29 no mesmo sentido)[^1][^7][^13]

**Armadilhas (mitos comuns)**

- "PII é o termo da LGPD." Não: PII vem do governo dos EUA[^12].
- "CPF é dado sensível." Não pelo rol. É identificador direto[^1][^7].
- "Dado de criança é dado sensível." Não pela letra da lei; o regime é o do art. 14 e do ECA Digital[^6].
- "Criptografei, então anonimizei." A ANPD diz que criptografia típica é pseudonimização[^7].
- "Fiz hash do CPF, está anonimizado." Divergente na ANPD; não para WP29 e HHS[^7][^11][^13].
- "Mostro só os 4 últimos dígitos." HHS e NIST: parte do identificador ainda identifica[^11][^12].
- "Tirei os 18 campos da HIPAA, pronto." Falta o texto livre e o "actual knowledge"[^10][^11].
- "Minha app de saúde segue a HIPAA." Só se for *covered entity* ou *business associate*[^9].
- "Meu produto não é para criança, o ECA Digital não me pega." Vale também para produto "de acesso provável" por criança[^2].

**Gancho para a saga do dev**

- Login com biometria? É dado sensível. A base costuma ser o art. 11, II, "g" (prevenção à fraude na autenticação)[^1].

## Em aberto

- **Guia final de anonimização da ANPD**: só achei o estudo preliminar v1.0 (dez. 2023) e a minuta de 2024. Busca de 19/11/2026 não mostrou versão final. Conferir na página de publicações da ANPD.
- **Versão do estudo preliminar**: o PDF diz "Versão 1.0 Dezembro/2023", mas a nota 19 cita acesso em "26 jan. 2026" (p. 14)[^7]. O arquivo pode ter sido trocado sem mudar a versão.
- **Vigência original do ECA Digital**: notícias dizem que o prazo inicial era de um ano. O texto do Planalto mostra só "Art. 41. (VETADO)" e os dois art. 41-A[^2]. Não conferi a mensagem de veto.
- **Regulamentos da ANPD sobre o ECA Digital**: o Decreto 12.880 manda a ANPD regulamentar aferição de idade, segurança por padrão e mais[^3]. Não li as "orientações preliminares" de aferição de idade (mar. 2026).
- **App de saúde fora da HIPAA**: nos EUA, o que cobre esses apps (FTC, leis estaduais) não foi pesquisado. Pista, não fato.
- **Criança na lei dos EUA**: COPPA não foi pesquisada. Pista, não fato.
- **NIST SP 800-122**: não confirmei se há revisão em andamento; a versão lida é a de abril de 2010.
- **eCFR 160.103 hoje**: a definição de *public health* aparece no texto atual. Não conferi se veio da regra de saúde reprodutiva de 2024 nem o efeito de decisões judiciais sobre ela. Não afeta as definições usadas aqui.

## Fontes

[^1]: Brasil. *Lei nº 13.709, de 14 de agosto de 2018 (LGPD)*, texto compilado. 2018. Tipo: primária. Original: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm> · Wayback: <https://web.archive.org/web/20261111213350/https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-brasil-leis/2018-lgpd-lei-13709]] · Acessado em 2026-11-19.
[^2]: Brasil. *Lei nº 15.211, de 17 de setembro de 2025 (Estatuto Digital da Criança e do Adolescente)*, texto compilado. 2025. Tipo: primária. Original: <https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15211.htm> · Wayback: <https://web.archive.org/web/20261109202746/https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/lei/l15211.htm> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-brasil-leis/2025-eca-digital-lei-15211]] · Acessado em 2026-11-19.
[^3]: Brasil. *Decreto nº 12.880, de 18 de março de 2026* (regulamenta a Lei 15.211/2025). 2026. Tipo: primária. Original: <https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/d12880.htm> · Wayback: <https://web.archive.org/web/20261109194858/https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/Decreto/D12880.htm> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-brasil-leis/2026-decreto-12880]] · Acessado em 2026-11-19.
[^4]: Brasil. *Lei nº 8.069, de 13 de julho de 1990 (Estatuto da Criança e do Adolescente)*, art. 2º. 1990. Tipo: primária. Original: <https://www.planalto.gov.br/ccivil_03/leis/l8069.htm> · Wayback: <https://web.archive.org/web/20261110140127/http://www.planalto.gov.br/ccivil_03/leis/l8069.htm> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-brasil-leis/1990-eca-lei-8069]] · Acessado em 2026-11-19.
[^5]: ANPD, Conselho Diretor. *Enunciado CD/ANPD nº 1, de 22 de maio de 2023*. DOU de 24/05/2023, seção 1, p. 129. Tipo: primária. Original: <https://www.in.gov.br/en/web/dou/-/enunciado-cd/anpd-n-1-de-22-de-maio-de-2023-485306934> · Wayback: <https://web.archive.org/web/20231105025624/https://www.in.gov.br/en/web/dou/-/enunciado-cd/anpd-n-1-de-22-de-maio-de-2023-485306934> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-brasil-anpd-doutrina/2023-anpd-enunciado-cd-1]] · Acessado em 2026-11-19.
[^6]: Sabbat, Arthur Pereira (Diretor relator, ANPD). *Voto nº 12/2023 — Circuito Deliberativo nº 11/2023* (minuta do Enunciado sobre o art. 14 da LGPD). 2023. Tipo: primária (voto de diretor; opinião do relator). Páginas do PDF: 4 e 5. Original: <https://www.gov.br/anpd/pt-br/assuntos/deliberacoes-do-conselho-diretor/cds-ano-2023/cd-11-2023-votos.pdf/@@display-file/file> · Wayback: <https://web.archive.org/web/20261008033319/https://www.gov.br/anpd/pt-br/assuntos/deliberacoes-do-conselho-diretor/cds-ano-2023/cd-11-2023-votos.pdf/@@display-file/file> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-brasil-anpd-doutrina/2023-anpd-cd-11-voto-criancas]] · Acessado em 2026-11-19.
[^7]: ANPD. *Estudo preliminar: Anonimização e Pseudonimização para a proteção de dados pessoais*. Versão 1.0, dez. 2023 (documento de consulta pública, sem caráter normativo). Tipo: primária (posição técnica preliminar da autoridade). Páginas do PDF citadas no texto. Original: <https://www.gov.br/anpd/pt-br/assuntos/regulacao/agenda-regulatoria-1/cp-estudo-preliminar_anonimizacao_e_pseudon.pdf/@@display-file/file> · Wayback: sem snapshot no Wayback (Save Page Now falhou duas vezes) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-anonimizacao/2023-anpd-estudo-anonimizacao]] · Acessado em 2026-11-19.
[^8]: Estados Unidos. *42 U.S.C. § 1320d — Definitions*. United States Code, ed. 2023 (GPO). Tipo: primária. Original: <https://www.govinfo.gov/content/pkg/USCODE-2023-title42/html/USCODE-2023-title42-chap7-subchapXI-partC-sec1320d.htm> · Wayback: <https://web.archive.org/web/20261119140901/https://www.govinfo.gov/content/pkg/USCODE-2023-title42/html/USCODE-2023-title42-chap7-subchapXI-partC-sec1320d.htm> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-eua-hipaa/1996-hipaa-42-usc-1320d]] · Acessado em 2026-11-19.
[^9]: Estados Unidos. *45 CFR § 160.103 — Definitions*. eCFR, "up to date as of 11/17/2026". Tipo: primária. Original: <https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160/subpart-A/section-160.103> · Wayback: <https://web.archive.org/web/20261109075326/https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160/subpart-A/section-160.103> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-eua-hipaa/2000-hipaa-45-cfr-160-103]] · Acessado em 2026-11-19.
[^10]: Estados Unidos. *45 CFR § 164.514 — Other requirements relating to uses and disclosures of protected health information*. eCFR, "up to date as of 11/17/2026". Tipo: primária. Original: <https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514> · Wayback: <https://web.archive.org/web/20260810053651/https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-eua-hipaa/2000-hipaa-45-cfr-164-514]] · Acessado em 2026-11-19.
[^11]: HHS, Office for Civil Rights. *Guidance Regarding Methods for De-identification of Protected Health Information in Accordance with the HIPAA Privacy Rule*. 26 nov. 2012. Tipo: primária (guia oficial do regulador). Páginas do PDF citadas no texto. Original: <https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/understanding/coveredentities/De-identification/hhs_deid_guidance.pdf> · Wayback: <https://web.archive.org/web/20261012225108/https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/understanding/coveredentities/De-identification/hhs_deid_guidance.pdf> (snapshot antigo; hhs.gov devolve 403 a cliente automatizado, e a cópia foi baixada deste snapshot) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-eua-hipaa/2012-hhs-deid-guidance]] · Acessado em 2026-11-19.
[^12]: McCallister, Erika; Grance, Tim; Scarfone, Karen (NIST). *SP 800-122: Guide to Protecting the Confidentiality of Personally Identifiable Information (PII)*. Abr. 2010. Tipo: primária (norma técnica do governo dos EUA). Original: <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-122.pdf> · Wayback: <https://web.archive.org/web/20261116190940/https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-122.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-eua-hipaa/2010-nist-sp-800-122]] · Acessado em 2026-11-19.
[^13]: Article 29 Data Protection Working Party. *Opinion 05/2014 on Anonymisation Techniques (WP216)*. Adotada em 10 abr. 2014. Tipo: primária (parecer oficial do órgão europeu; referência para a UE, não para o Brasil). Página do PDF: 20. Original: <https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf> · Wayback: <https://web.archive.org/web/20261113161557/https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-anonimizacao/2014-art29-wp216-anonimizacao]] · Acessado em 2026-11-19.
[^14]: Sweeney, Latanya. *Simple Demographics Often Identify People Uniquely*. Carnegie Mellon University, Data Privacy Working Paper 3, 2000. Tipo: primária (estudo original; *working paper*, sem revisão por pares). Original: <https://dataprivacylab.org/projects/identifiability/paper1.pdf> · Wayback: <https://web.archive.org/web/20261117211753/https://dataprivacylab.org/projects/identifiability/paper1.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-anonimizacao/2000-sweeney-simple-demographics]] · Acessado em 2026-11-19.
[^15]: Golle, Philippe. *Revisiting the Uniqueness of Simple Demographics in the US Population*. WPES'06 (ACM), 2006. Tipo: primária (estudo original, publicado em workshop da ACM). Original: <https://crypto.stanford.edu/~pgolle/papers/census.pdf> · Wayback: <https://web.archive.org/web/20261116055811/https://crypto.stanford.edu/~pgolle/papers/census.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-anonimizacao/2006-golle-uniqueness-demographics]] · Acessado em 2026-11-19.
[^16]: Castro, Dayane Marciano de Oliveira; Mano, Janini Nogueira D'Alessandro; Baronovsky, Thainá. *Dados pessoais bancários são considerados dados sensíveis para a LGPD?* Migalhas, 18 ago. 2021. Tipo: secundária (artigo de opinião de advogadas). Original: <https://www.migalhas.com.br/depeso/350335/dados-pessoais-bancarios-sao-considerados-dados-sensiveis-para-a-lgpd> · Wayback: <https://web.archive.org/web/20251215023737/https://www.migalhas.com.br/depeso/350335/dados-pessoais-bancarios-sao-considerados-dados-sensiveis-para-a-lgpd> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-brasil-anpd-doutrina/2021-castro-et-al-dados-bancarios-sensiveis]] · Acessado em 2026-11-19.
[^17]: Dalese, Pedro. *Os dados pessoais sensíveis na era do Big Data*. Migalhas, 3 mar. 2021. Tipo: secundária (artigo de opinião). Original: <https://www.migalhas.com.br/depeso/341100/os-dados-pessoais-sensiveis-na-era-do-big-data> · Wayback: <https://web.archive.org/web/20261119140819/https://www.migalhas.com.br/depeso/341100/os-dados-pessoais-sensiveis-na-era-do-big-data> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-brasil-anpd-doutrina/2021-dalese-sensiveis-big-data]] · Acessado em 2026-11-19.
[^18]: Lefosse Advogados. *ANPD publica enunciado sobre o tratamento de dados pessoais de crianças e adolescentes*. 26 maio 2023. Tipo: secundária (alerta de escritório de advocacia). Original: <https://lefosse.com/noticias/alerta/anpd-publica-enunciado-sobre-o-tratamento-de-dados-pessoais-de-criancas-e-adolescentes/> · Wayback: <https://web.archive.org/web/20261119141326/https://lefosse.com/noticias/alerta/anpd-publica-enunciado-sobre-o-tratamento-de-dados-pessoais-de-criancas-e-adolescentes/> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-brasil-anpd-doutrina/2023-lefosse-enunciado-anpd-criancas]] · Acessado em 2026-11-19.
