---
title: "Primeiros relatos de uso de criptografia"
type: research
status: concluida
created: 2026-11-19
post: "[[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/post]]"
---

> [!tldr] TL;DR
> - O "primeiro caso" depende do que conta como criptografia. Os casos egípcio e mesopotâmico são **escrita incomum**: a meta não era esconder a mensagem.
> - A descrição mais antiga e explícita de **cifra para sigilo** que achamos é grega: Eneias, o Tático (c. 360 a.C.), troca vogais por pontos.
> - Heródoto (séc. V a.C.) traz os casos clássicos de **esteganografia**: escravo tatuado, tábua de cera.
> - A **cítala** espartana só é descrita como cifra uns 500 anos depois, por Plutarco. Há quem a chame de mito (Kelly, 1998).
> - A **criptoanálise** nasce com Al-Kindi (c. 850 d.C.). O manuscrito só foi redescoberto nos anos 1980.

## Pergunta

Quais são os primeiros relatos de uso de criptografia na história?
Para cada um: fonte primária, quem datou e interpretou, e em que categoria cai.

## Três categorias

| Categoria | O que é | Exemplo |
|---|---|---|
| **Criptografia** (cifra ou código) | A mensagem fica visível, mas ilegível sem a chave | César trocando A por D |
| **Esteganografia** | A mensagem fica escondida; quem vê não sabe que ela existe | Texto sob a cera de uma tábua |
| **Escrita incomum** | Sinais raros ou trocados, sem meta de sigilo | Hieróglifos "enigmáticos" no Egito |

- Esteganografia: "concealing a message within another message, an image, or an object, without giving any outward sign that a secret message is hidden in it" (esconder uma mensagem dentro de outra mensagem, imagem ou objeto, sem sinal externo de que ela existe).[^diep-def]
- Criptografia: "securing communication not by concealing but by enciphering a text" (proteger a comunicação não escondendo, mas cifrando o texto).[^diep-def]
- As duas palavras são neologismos. Nenhuma era usada na Antiguidade.[^diep-def]

## Resposta curta

- **Egito, c. 1900 a.C.** Kahn abre a história da criptologia com a tumba de Khnumhotep II, "the earliest known deliberate transformation of a writing" (a mais antiga transformação deliberada da escrita conhecida).[^cia]
  - Egiptólogos chamam esse fenômeno de "escrita enigmática". Para eles, "criptografia" é rótulo errado: a escrita "is not directed at 'hiding' any denotational contents" (não visa "esconder" conteúdo nenhum).[^stauder]
  - Não achamos fonte egiptológica que confirme sinais incomuns na inscrição de Khnumhotep II. A afirmação depende de Kahn (ver Em aberto).
- **Mesopotâmia, tabuleta de esmalte.** Data do séc. XVII a.C. na edição de 1936.[^gadd] O museu que a expôs dá c. 1400–1200 a.C.[^isaw]
  - Diepenbroek repete a leitura de que seria uma receita **cifrada** de 1500 a.C., mas lembra que o motivo pode ter sido mágico, não comercial.[^diep-meso]
  - O trecho da edição de 1936 que conseguimos ler não fala em cifra.[^gadd]
- **Bíblia hebraica, Atbash.** "Sheshach" (ששך) em Jr 25:26 e 51:41 vira "Babel" (בבל) trocando a primeira letra do alfabeto pela última.[^jr25][^jr51][^isbe]
  - Em Jr 51:41, "Sheshach" e "Babilônia" aparecem **no mesmo versículo**.[^jr51] Ou seja: não há segredo nenhum ali.
  - A Septuaginta (tradução grega) omite a palavra nas duas passagens. Parte dos críticos acha que ela é acréscimo posterior.[^isbe]
- **Heródoto, séc. V a.C.** Dois casos de **esteganografia**, não de cifra:
  - Histieu raspa a cabeça de um escravo, tatua a mensagem e espera o cabelo crescer.[^her5]
  - Demarato escreve na madeira de uma tábua e cobre com cera.[^her7]
- **Eneias, o Tático, c. 360 a.C.** Capítulo inteiro sobre mensagens secretas.[^eneias]
  - A maioria é esteganografia: furinhos sobre letras de um livro qualquer.[^eneias]
  - Mas em 31.30-31 ele troca **vogais por pontos**. Isso já é substituição de letras, ou seja, cifra.[^eneias]
- **Cítala espartana.** Fita enrolada num bastão. Desenrolada, as letras ficam fora de ordem: é uma **cifra de transposição**.[^plut]
  - O evento (Lisandro chamado de volta) é do fim do séc. V a.C. A primeira descrição completa é de Plutarco, fim do séc. I ou início do II d.C.[^diep-plut]
- **Políbio, livro X.** Tabela de 5×5 letras para **sinalizar com tochas** à distância.[^pol] Não era para esconder nada. O uso como cifra ("quadrado de Políbio") é posterior.
- **César e Augusto (séc. I a.C.).** Suetônio: César trocava cada letra pela quarta seguinte (D por A).[^suet-jul] Augusto, pela seguinte (B por A), e usava AA para X.[^suet-aug]
  - Aulo Gélio confirma que as cartas de César tinham troca de letras combinada, mas não diz qual era a troca.[^gelio]
- **Índia, Kama Sutra.** "mlecchita-vikalpāḥ" está na lista das 64 artes (1.3.15).[^gretil] Burton traduz: "The art of understanding writing in cypher" (a arte de entender a escrita cifrada).[^ks3]
  - A obra é datada entre os séc. I e VI d.C. Os métodos de cifra só aparecem no comentário *Jayamangala*, dos séc. X a XIII.[^ks-intro]
- **Al-Kindi, c. 850 d.C.** *Risalah fi Istikhraj al-Mu'amma* (Tratado sobre decifrar mensagens criptografadas). É o texto de criptologia mais antigo que existe.[^suwaiyel]
  - Descreve a **análise de frequência**: contar as letras de um texto comum e comparar com o texto cifrado.[^ycart]
  - É o primeiro registro de **criptoanálise**, não de criptografia.

## Linha do tempo

| Data (quem datou) | Caso | Categoria | Fonte primária | Fonte |
|---|---|---|---|---|
| c. 1900 a.C. (Kahn) | Tumba de Khnumhotep II, Beni Hasan | Escrita incomum | Inscrição da tumba (não consultada) | [^cia][^stauder] |
| séc. XVII a.C. (Gadd e Thompson, 1936) · c. 1400–1200 a.C. (ISAW) · 1500 a.C. (Diepenbroek) | Tabuleta BM 120960, receita de esmalte/vidro | Disputada: cifra ou escrita técnica/mágica | A tabuleta | [^gadd][^isaw][^diep-meso] |
| séc. VII a.C. (West, via Diepenbroek) | Arquíloco cita a *skytale* | Bastão de mensageiro, sem cifra descrita | Arquíloco, fr. 185 | [^diep-kelly] |
| fim do séc. VII ou séc. VI a.C. ⚠️ | Atbash: Sheshach = Babel; Leb-kamai | Cifra (troca de letras), sem meta de sigilo | Jr 25:26; 51:1; 51:41 | [^jr25][^jr51][^isbe] |
| fim do séc. VI a.C. ⚠️ (revolta jônia) | Histieu tatua a cabeça do escravo | Esteganografia | Heródoto 5.35 | [^her5] |
| c. 480 a.C. (Diepenbroek) | Demarato e a tábua de cera | Esteganografia | Heródoto 7.239 | [^her7][^diep-480] |
| fim do séc. V a.C. (evento) · fim do séc. I/início do II d.C. (relato) | Cítala de Lisandro | Cifra de transposição (disputada) | Plutarco, *Lisandro* 19.5-7 | [^plut][^diep-plut] |
| c. 360 a.C. (Diepenbroek; último evento citado: 360 a.C.) | Mensagens secretas; vogais por pontos | Esteganografia + cifra | Eneias, o Tático, cap. 31 | [^eneias][^diep-480] |
| séc. II a.C. ⚠️ | Tabela 5×5 para tochas | Sinalização (código de transmissão) | Políbio X 45.6-12 | [^pol] |
| séc. I a.C. (relato do séc. II d.C. ⚠️) | Cifras de César e Augusto | Cifra de substituição | Suetônio, *Júlio* 56.6; *Augusto* 88 | [^suet-jul][^suet-aug] |
| séc. II d.C. ⚠️ | Cartas de César, cítala, Asdrúbal, Histieu | Resumo erudito de cifra e esteganografia | Aulo Gélio, *Noites Áticas* 17.9 | [^gelio] |
| séc. I–VI d.C. (Burton) | *mlecchita-vikalpa* nas 64 artes | Cifra (citada, não descrita) | *Kama Sutra* 1.3.15 | [^gretil][^ks3][^ks-intro] |
| c. 850 d.C. (Al-Suwaiyel) | Tratado de Al-Kindi | Criptoanálise | Manuscrito (Istambul ⚠️) | [^suwaiyel][^ycart][^tayeb] |

⚠️ = datação convencional, não conferida numa fonte capturada.

## Citações das fontes primárias

**Plutarco, *Lisandro* 19.6-7** (trad. Perrin, 1916):[^plut]
> "they write what they wish on the parchment, just as it lies wrapped about the 'scytale'; and when they have written their message, they take the parchment off, and send it, without the piece of wood, to the commander. He, when he has received it, cannot other get any meaning of it, — since the letters have no connection, but are disarranged, — unless he takes his own 'scytale'"

Tradução: "escrevem o que querem no pergaminho, do jeito que ele está enrolado na cítala; escrita a mensagem, tiram o pergaminho e o enviam, sem o pedaço de madeira, ao comandante. Ele, ao recebê-lo, não consegue tirar sentido algum, porque as letras não têm ligação e estão fora de ordem, a menos que pegue a sua própria cítala."

**Suetônio, *Júlio* 56.6** (trad. Rolfe):[^suet-jul]
> "if he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out. If anyone wishes to decipher these, and get at their meaning, he must substitute the fourth letter of the alphabet, namely D, for A, and so with the others."

Tradução: "se tinha algo confidencial a dizer, escrevia em cifra, isto é, mudando a ordem das letras do alfabeto de modo que não se pudesse ler palavra alguma. Quem quiser decifrá-las e chegar ao sentido deve trocar a quarta letra do alfabeto, D, por A, e assim com as demais."

**Suetônio, *Augusto* 88** (trad. Rolfe):[^suet-aug]
> "Whenever he wrote in cipher, he wrote B for A, C for B, and the rest of the letters on the same principle, using AA for X."

Tradução: "Quando escrevia em cifra, punha B no lugar de A, C no lugar de B, e as outras letras pelo mesmo princípio, usando AA para X."

**Aulo Gélio, *Noites Áticas* 17.9.3** (latim):[^gelio]
> "Erat autem conventum inter eos clandestinum de commutando situ litterarum, ut in scripto quidem alia aliae locum et nomen teneret, sed in legendo locus cuique suus et potestas restitueretur"

Tradução livre (desta pesquisa): "Havia entre eles um acordo secreto de trocar a posição das letras: na escrita, uma ocupava o lugar e o nome da outra; na leitura, cada uma voltava ao seu lugar e ao seu valor."

**Eneias, o Tático, 31.1 e 31.30** (trad. Illinois Greek Club):[^eneias]
> "In regard to secret messages, there are all sorts of ways of sending them, but a private arrangement must be previously made between the sender and the receiver."

Tradução: "Quanto às mensagens secretas, há todo tipo de modo de enviá-las, mas é preciso um acordo prévio e privado entre quem envia e quem recebe."

> "It should be arranged in advance to express the vowels by dots, and whatever the number of each vowel happens to be, so many dots are to be placed in the writing."

Tradução: "Deve-se combinar antes que as vogais sejam expressas por pontos: quantos forem o número de cada vogal, tantos pontos se põem na escrita."

**Heródoto 5.35** (trad. Macaulay, 1890):[^her5]
> "shaved off the hair of the most faithful of his slaves, and having marked his head by pricking it, waited till the hair had grown again"

Tradução: "raspou o cabelo do mais fiel de seus escravos e, tendo marcado a cabeça dele com picadas, esperou até o cabelo crescer de novo."

**Heródoto 7.239** (trad. Macaulay, 1890):[^her7]
> "he took a folding tablet and scraped off the wax which was upon it, and then he wrote the design of the king upon the wood of the tablet, and having done so he melted the wax and poured it over the writing"

Tradução: "pegou uma tábua dobrável, raspou a cera que havia nela, escreveu o plano do rei na madeira e, feito isso, derreteu a cera e a derramou sobre a escrita."

**Políbio X 45.6-7** (trad. Paton):[^pol]
> "The most recent method, devised by Cleoxenus and Democleitus and perfected by myself [...] We take the alphabet and divide it into five parts, each consisting of five letters."

Tradução: "O método mais recente, criado por Cleoxeno e Demócrito e aperfeiçoado por mim [...] Pegamos o alfabeto e o dividimos em cinco partes, de cinco letras cada."

**Jeremias 51:41** (JPS 1917):[^jr51]
> "אֵיךְ נִלְכְּדָה שֵׁשַׁךְ [...] אֵיךְ הָיְתָה לְשַׁמָּה בָּבֶל" — "How is Sheshach taken! [...] How is Babylon become an astonishment"

Tradução: "Como foi tomada Sheshach! [...] Como se tornou Babilônia um espanto."

**Al-Kindi** (trad. inglesa de Mrayati et al., 2002, p. 124, citada por Ycart):[^ycart]
> "count the number of each of its letters. We mark the most frequent letter 'first', the second most frequent 'second' [...] Then we go back to the message we want to cryptanalyse [...] searching for the most frequent symbol of the cryptogram and we regard it as being the same letter we have marked 'first'"

Tradução: "contar quantas vezes aparece cada letra. Marcamos a mais frequente como 'primeira', a segunda mais frequente como 'segunda' [...] Depois voltamos à mensagem que queremos decifrar [...] procuramos o símbolo mais frequente do criptograma e o tomamos pela mesma letra que marcamos como 'primeira'."

## Divergências

| Tema | Fonte A diz | Fonte B diz | Nota |
|---|---|---|---|
| Khnumhotep II conta como criptografia? | Kahn: "earliest known deliberate transformation of a writing" (via resenha da CIA)[^cia] | Stauder: "criptografia" é "technically a misnomer"; a escrita enigmática não visa esconder.[^stauder] Polis e Seyr: rótulo mais adequado é "enigmatic".[^polis] Diepenbroek: a troca de sinais buscava prestígio mágico, não sigilo.[^diep-meso] | Kahn fala em "transformação", não em segredo (⚠️ T3: lembrança do livro, não conferida). Critério: os egiptólogos são especialistas e mais recentes. **Não conta como cifra.** |
| Data da tabuleta de esmalte | Séc. XVII a.C., pelo reinado de Gulkishar (Gadd e Thompson, 1936)[^gadd] | c. 1400–1200 a.C. (ISAW/NYU)[^isaw]; 1500 a.C. (Diepenbroek, citando Caubet e Mollin)[^diep-meso] | A edição de 1936 é a primária. O museu segue datação mais recente (fonte não lida). Sem desempate. |
| A tabuleta é "cifrada"? | Diepenbroek (via Caubet 2008 e Mollin 2005): receita cifrada para proteger informação[^diep-meso] | A mesma Diepenbroek: o motivo pode ser mágico.[^diep-meso] O extrato de 1936 não menciona cifra.[^gadd] | **Não confirmado** em fonte primária acessível. |
| Sheshach é Atbash? | Leitura padrão: cifra de Babel; o Targum traduz por "Babel"[^isbe] | Delitzsch: nome de um bairro babilônico; Cheyne: acréscimo de editores tardios; a Septuaginta omite[^isbe] | Mesmo como Atbash, 51:41 nomeia Babilônia junto.[^jr51] **Troca de letras sim; sigilo não.** |
| A cítala era cifra? | Plutarco e Gélio descrevem cifra de transposição[^plut][^gelio] | Kelly (1998): o sentido principal é "bastão"; é "ironic" achar que espartanos mandavam mensagens secretas (via Diepenbroek)[^diep-kelly] | Diepenbroek (2020) defende o uso cifrado.[^diep-kelly] A descrição mais antiga é ~500 anos posterior.[^diep-plut] **Divergência aberta.** |
| "Quadrado de Políbio" é cifra? | Uso moderno: cifra | Políbio: sinal de fogo para mandar qualquer mensagem à distância[^pol] | Na fonte, é sinalização. A meta era clareza, não segredo. |
| Qual a troca de César? | Suetônio: quarta letra (D por A)[^suet-jul] | Gélio: troca combinada entre eles, sem dizer qual[^gelio] | Gélio cita um comentário de Probo sobre o tema, perdido. Suetônio é o único com o deslocamento. |
| Quando nasce a criptoanálise? | Resenha da CIA (1968), resumindo Kahn: árabes "in the seventh century"[^cia] | Al-Suwaiyel: Kahn se apoiou em al-Qalqashandi (1412); o tratado de Al-Kindi (c. 850) só veio à tona com os manuscritos publicados em 1987[^suwaiyel] | A data de Al-Kindi é a mais documentada hoje. O "séc. VII" da resenha não bate com nenhuma outra fonte. |
| Quem usou cifra para sigilo primeiro? | Kasten: os egípcios (via Diepenbroek)[^diep-meso] | Diepenbroek: gregos (espartanos) e romanos; Egito e Mesopotâmia não deixaram cifra feita para sigilo[^diep-meso] | Diepenbroek admite que provas podem ter se perdido. |

## Para o post

Frases seguras:

- "Os primeiros registros de escrita 'transformada' são egípcios, de quase 4 mil anos. Mas a meta era impressionar, não esconder."
- "Heródoto conta como se escondia uma mensagem no couro cabeludo de um escravo. Isso é esteganografia: esconder que a mensagem existe."
- "Por volta de 360 a.C., um manual grego de defesa de cidades já ensinava a trocar vogais por pontos."
- "Segundo Suetônio, César trocava cada letra pela terceira seguinte: A virava D."
- "A primeira técnica para **quebrar** cifras, contar letras, está num tratado árabe do séc. IX, de Al-Kindi."

Armadilhas:

- "Os egípcios inventaram a criptografia": os egiptólogos rejeitam o rótulo.
- "A cítala foi a primeira máquina de cifra": a descrição é ~500 anos posterior e o uso é disputado.
- "Políbio criou uma cifra": ele criou um sistema de sinalização.
- "O Atbash da Bíblia escondia o nome da Babilônia": no mesmo versículo, a Babilônia aparece com todas as letras.
- "O Kama Sutra ensina cifras": ele só lista a arte; os métodos estão num comentário medieval.
- Gancho do post: o dev que "só queria resolver o problema" faz o que fazia César. Trocar letras por regra fixa é ofuscar, não cifrar com segurança. Al-Kindi já quebrava isso no séc. IX.

## Em aberto

- **Khnumhotep II:** não achamos egiptólogo que aponte sinais incomuns na Grande Inscrição de Beni Hasan. Falta ler Kahn, *The Codebreakers*, cap. 2 ("The First 3,000 Years"), com página. Também Lloyd (1992), "The Great Inscription of Khnumḥotpe II at Beni Hasan".
- **Tabuleta BM 120960:** falta a fonte que diz que ela usa sinais raros de propósito. Kahn e Caubet (2008) são os candidatos. O artigo de 1936 está atrás de paywall.
- **Kelly (1998), "The Myth of the Skytale"**, *Cryptologia* 22(3), p. 244-260: citado só via Diepenbroek. Artigo protegido, não lido.
- **Al-Kindi:** cota do manuscrito em Istambul (Süleymaniye?) não confirmada. Al-Kadi (1992), *Cryptologia* 16(2), p. 97-126, não foi lido.
- **Al-Khalil (séc. VIII)** e um *Kitab al-Mu'amma* perdido: pista de memória (T3), sem fonte.
- **Heródoto 7.239:** há quem considere o capítulo um acréscimo posterior (T3, não verificado).
- **Datas marcadas com ⚠️** na linha do tempo: convencionais, sem fonte capturada.
- **Yashodhara:** os nomes das cifras do comentário (*kautiliya*, *muladeviya*) vieram de busca terciária. Não conferidos no comentário.

## Fontes

[^cia]: Roger Pineau. *The Codebreakers: The Story of Secret Writing by David Kahn* (resenha). Studies in Intelligence 12(3), 1968, CIA. Tipo: secundária (resume Kahn, 1967). Original: <https://www.cia.gov/resources/csi/static/Review-The-Codebreakers.pdf> · Wayback: <https://web.archive.org/web/20250208033739/https://www.cia.gov/resources/csi/static/Review-The-Codebreakers.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-panorama/1968-cia-resenha-the-codebreakers]] · Acessado em 2026-11-19. Livro resenhado: David Kahn, *The Codebreakers*, 1967, cap. 2. Cópia: não disponível (protegido); página não conferida.
[^stauder]: Andréas Stauder. "Introduction". Em D. Klotz e A. Stauder (eds.), *Enigmatic Writing in the Egyptian New Kingdom I*, 2020, p. 1-5 (citação na p. 3). Tipo: secundária (acadêmica). Original: <https://archiv.ub.uni-heidelberg.de/propylaeumdok/5400/1/Stauder_Introduction_Enigmatic_Writing.pdf> · Wayback: <https://web.archive.org/web/20240909060622/https://archiv.ub.uni-heidelberg.de/propylaeumdok/5400/1/Stauder_Introduction_Enigmatic_Writing.pdf> (original fora do ar; cópia baixada do Wayback) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-egito-mesopotamia/2020-stauder-enigmatic-writing-intro]] · Acessado em 2026-11-19.
[^polis]: Stéphane Polis e Philipp Seyr. "Enigmatic Texts from Deir el-Medina". *Revue d'Égyptologie* 73, 2022. Tipo: secundária (acadêmica). Original: <https://orbi.uliege.be/bitstream/2268/301682/1/Polis_Seyr_RdE_73.pdf> · Wayback: <https://web.archive.org/web/20261119141523/https://orbi.uliege.be/bitstream/2268/301682/1/Polis_Seyr_RdE_73.pdf> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-egito-mesopotamia/2022-polis-seyr-enigmatic-texts]] · Acessado em 2026-11-19.
[^diep-def]: Martine L. M. Diepenbroek. *Myths and Histories of the Spartan scytale*. Tese de doutorado, Universidade de Bristol, 2020, p. 15-16 ("Working definitions"). Tipo: secundária (acadêmica). Original: <https://research-information.bris.ac.uk/ws/files/263833703/Myths_and_Histories_of_the_Spartan_scytale_29_11_2020.pdf> · Wayback: <https://web.archive.org/web/20240909223016/https://research-information.bris.ac.uk/ws/files/263833703/Myths_and_Histories_of_the_Spartan_scytale_29_11_2020.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-grecia-roma/2020-diepenbroek-scytale-bristol]] · Acessado em 2026-11-19.
[^diep-meso]: Diepenbroek, 2020, § 1.1, p. 52-53 (Egito e Mesopotâmia; Kasten e Mollin). Tipo: secundária. Mesmos links e cópia de [^diep-def].
[^diep-kelly]: Diepenbroek, 2020, p. 23-24 (resumo e citações de Kelly 1998, p. 245, e West 1988, p. 42). Tipo: secundária. Mesmos links e cópia de [^diep-def].
[^diep-plut]: Diepenbroek, 2020, § 2.3.10 (Plutarco, fim do séc. I/início do II d.C.: "the first complete description of the scytale"). Tipo: secundária. Mesmos links e cópia de [^diep-def].
[^diep-480]: Diepenbroek, 2020: Demarato "around 480 BCE" (cap. 2) e "Aeneas Tacticus (How to Survive under Siege, ca. 360 BCE)" (Apêndice 1). Tipo: secundária. Mesmos links e cópia de [^diep-def].
[^gadd]: C. J. Gadd e R. Campbell Thompson. "A Middle-Babylonian Chemical Text". *Iraq* 3(1), 1936, p. 87-96. DOI 10.2307/4241587. Tipo: primária (edição do texto), lida só no extrato da p. 87. Original: <https://cambridge.org/core/journals/iraq/article/middlebabylonian-chemical-text/F4B01DC7752095019833F30BE77CD2BD> · Wayback: <https://web.archive.org/web/20261119141003/https://www.cambridge.org/core/journals/iraq/article/abs/middlebabylonian-chemical-text/F4B01DC7752095019833F30BE77CD2BD> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-egito-mesopotamia/1936-gadd-thompson-texto-quimico-iraq]] (só a página do artigo; texto integral protegido) · Acessado em 2026-11-19.
[^isaw]: ISAW/NYU. "Cuneiform Tablet" (receita de vidro vermelho, BM 1929,0715.1), exposição *Ishtar Gate*. Tipo: terciária (ficha de museu). Original: <https://isaw.nyu.edu/exhibitions/ishtar-gate/objects/tablet-glass-recipe-red> · Wayback: <https://web.archive.org/web/20240727100528/https://isaw.nyu.edu/exhibitions/ishtar-gate/objects/tablet-glass-recipe-red/> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-egito-mesopotamia/sd-isaw-tabuleta-receita-vidro-vermelho]] · Acessado em 2026-11-19.
[^jr25]: *Jeremias* 25:26, texto massorético e trad. JPS 1917. Tipo: primária. Original: <https://mechon-mamre.org/p/pt/pt1125.htm> · Wayback: <https://web.archive.org/web/20260523013331/https://mechon-mamre.org/p/pt/pt1125.htm> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-biblia/0600ac-mechon-mamre-jeremias-25-jps-1917]] · Acessado em 2026-11-19.
[^jr51]: *Jeremias* 51:1 e 51:41, texto massorético e trad. JPS 1917. Tipo: primária. Original: <https://mechon-mamre.org/p/pt/pt1151.htm> · Wayback: <https://web.archive.org/web/20260523010615/https://mechon-mamre.org/p/pt/pt1151.htm> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-biblia/0600ac-mechon-mamre-jeremias-51-jps-1917]] · Acessado em 2026-11-19.
[^isbe]: Horace J. Wolf. "Sheshach". *International Standard Bible Encyclopedia*, 1915. Tipo: terciária (referência, domínio público). Original: <https://www.biblestudytools.com/encyclopedias/isbe/sheshach.html> · Wayback: <https://web.archive.org/web/20261119141555/https://www.biblestudytools.com/encyclopedias/isbe/sheshach.html> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-biblia/1915-isbe-sheshach]] · Acessado em 2026-11-19.
[^her5]: Heródoto. *Histórias* V, 35. Trad. G. C. Macaulay, 1890. Tipo: primária. Original: <https://sacred-texts.com/book/the-history-of-herodotus/30-5> · Wayback: <https://web.archive.org/web/20261119141031/https://sacred-texts.com/book/the-history-of-herodotus/30-5> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-grecia-roma/0430ac-herodoto-historias-5-30-macaulay-1890]] · Acessado em 2026-11-19.
[^her7]: Heródoto. *Histórias* VII, 239. Trad. G. C. Macaulay, 1890. Tipo: primária. Original: <https://sacred-texts.com/book/the-history-of-herodotus/230> · Wayback: <https://web.archive.org/web/20261119142625/https://sacred-texts.com/book/the-history-of-herodotus/230> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-grecia-roma/0430ac-herodoto-historias-7-230-macaulay-1890]] · Acessado em 2026-11-19.
[^eneias]: Eneias, o Tático. *Sobre a defesa de posições fortificadas*, cap. 31 (1-3; 30-31). Trad. Illinois Greek Club, Loeb (a página cita a edição de 1928). Tipo: primária. Original: <https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Aeneas_Tacticus/E*.html> · Wayback: sem snapshot (o Save Page Now devolveu 403 para o site) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-grecia-roma/0360ac-eneias-tatico-cap-21-31-loeb]] · Acessado em 2026-11-19.
[^plut]: Plutarco. *Vida de Lisandro* 19.4-7. Trad. B. Perrin, Loeb, 1916. Tipo: primária. Original: <https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives/Lysander*.html> · Wayback: sem snapshot (o Save Page Now devolveu 403 para o site) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-grecia-roma/0100-plutarco-vida-de-lisandro-perrin-1916]] · Acessado em 2026-11-19.
[^pol]: Políbio. *Histórias* X, 43-47 (citação de 45.6-12). Trad. W. R. Paton, Loeb. Tipo: primária. Original: <https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Polybius/10*.html> · Wayback: sem snapshot (o Save Page Now devolveu 403 para o site) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-grecia-roma/0150ac-polibio-historias-10-paton-1925]] · Acessado em 2026-11-19.
[^suet-jul]: Suetônio. *Vida do Divino Júlio* 56.6. Trad. J. C. Rolfe, Loeb, 1914. Tipo: primária. Original: <https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/12Caesars/Julius*.html> · Wayback: sem snapshot (o Save Page Now devolveu 403 para o site) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-grecia-roma/0121-suetonio-vida-de-julio-rolfe-1914]] · Acessado em 2026-11-19.
[^suet-aug]: Suetônio. *Vida do Divino Augusto* 88. Trad. J. C. Rolfe, Loeb, 1914. Tipo: primária. Original: <https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/12Caesars/Augustus*.html> · Wayback: sem snapshot (o Save Page Now devolveu 403 para o site) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-grecia-roma/0121-suetonio-vida-de-augusto-rolfe-1914]] · Acessado em 2026-11-19.
[^gelio]: Aulo Gélio. *Noites Áticas* 17.9, texto latino. Tipo: primária. Original: <https://penelope.uchicago.edu/Thayer/L/Roman/Texts/Gellius/17*.html> (a tradução inglesa do livro XVII dava 404) · Wayback: sem snapshot (o Save Page Now devolveu 403 para o site) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-grecia-roma/0180-aulo-gelio-noites-aticas-17-latim]] · Acessado em 2026-11-19.
[^gretil]: Vātsyāyana. *Kāmasūtra* 1.3.15, texto sânscrito (GRETIL, CC BY-NC-SA 4.0). Tipo: primária. Original: <https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_vAtsyAyana-kAmasUtra.htm> · Wayback: <https://web.archive.org/web/20261119141907/https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/html/sa_vAtsyAyana-kAmasUtra.htm> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-india/0300-gretil-kamasutra-sanscrito]] · Acessado em 2026-11-19.
[^ks3]: *Kama Sutra*, parte I, cap. III (as 64 artes). Trad. R. Burton e F. F. Arbuthnot, 1883. Tipo: primária (tradução). Original: <https://sacred-texts.com/book/the-kama-sutra-of-vatsyayana/chapter-iii-on-the-study-of-the-sixty-four-arts> · Wayback: <https://web.archive.org/web/20261119142157/https://sacred-texts.com/book/the-kama-sutra-of-vatsyayana/chapter-iii-on-the-study-of-the-sixty-four-arts> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-india/0300-kama-sutra-burton-1883-cap-3]] · Acessado em 2026-11-19.
[^ks-intro]: *Kama Sutra*, introdução dos tradutores (Burton e Arbuthnot, 1883): datação de Vatsyayana (séc. I–VI d.C.) e do comentário *Jayamangala* (séc. X–XIII). Tipo: secundária. Original: <https://sacred-texts.com/book/the-kama-sutra-of-vatsyayana/introduction> · Wayback: <https://web.archive.org/web/20261119142657/https://sacred-texts.com/book/the-kama-sutra-of-vatsyayana/introduction> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-india/1883-kama-sutra-burton-introducao]] · Acessado em 2026-11-19.
[^suwaiyel]: Mohammed I. Al-Suwaiyel. "Arab Origins of Cryptology". Muslim Heritage, 2018. Tipo: secundária (divulgação; autor ligado à edição KACST dos manuscritos). Original: <https://muslimheritage.com/arab-origins-of-cryptology/> · Wayback: <https://web.archive.org/web/20260711045702/https://muslimheritage.com/arab-origins-of-cryptology/> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-mundo-arabe/2018-al-suwaiyel-origens-arabes-criptologia]] · Acessado em 2026-11-19.
[^ycart]: Bernard Ycart. "Letter counting: a stem cell for Cryptology, Quantitative Linguistics, and Statistics". *Historiographia Linguistica* 40(3), 2013, p. 303-329 (preprint arXiv 1211.6847). Cita Al-Kindi pela trad. de Mrayati et al. (2002, p. 124). Tipo: secundária (acadêmica). Original: <https://arxiv.org/pdf/1211.6847> · Wayback: <https://web.archive.org/web/20261119141600/https://arxiv.org/pdf/1211.6847> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-mundo-arabe/2013-ycart-letter-counting]] · Acessado em 2026-11-19.
[^tayeb]: Tariq Al-Tayeb. "Al-Kindi, Cryptography, Code Breaking and Ciphers". Muslim Heritage, 2003. Tipo: terciária (divulgação; nascimento de Al-Kindi c. 800, em Kufa). Original: <https://muslimheritage.com/al-kindi-cryptography/> · Wayback: <https://web.archive.org/web/20261119141807/https://muslimheritage.com/al-kindi-cryptography/> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/cripto-mundo-arabe/2003-al-tayeb-al-kindi-criptografia]] · Acessado em 2026-11-19.
