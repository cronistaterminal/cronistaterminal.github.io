+++
title = 'A saga do programador que só queria resolver o problema: Ofuscação de dados'
slug = 'a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados-tb04'
date = 2026-11-19
draft = false
num = '0000'
epoca = 'c. 1900 a.C.–2026'
tldr = 'De hieróglifos esquisitos à LGPD: por que a gente esconde informação, e como o dev resolve o bug sem saber de quem é o dado?'
tldr_long = 'Desde que existe língua, alguém quer esconder alguma coisa. Passo pelo Egito, pela Mesopotâmia e por Eneias, o Tático, chego na Enigma e nos pilares da segurança - até a LGPD aparecer com a pergunta: como eu resolvo o problema sem saber quem é o usuário?'
tags = ['seguranca', 'criptografia', 'lgpd', 'python']
+++

## Uma leve INTRODUÇÃO


Me atrevo a dizer que, muito provavelmente, a partir do momento em que a língua se desenvolve e as primeiras sociedades se formam, surge a necessidade de esconder informação. Talvez alguém tenha achado uma árvore especialmente cheia de frutos e não queira compartilhar, talvez alguém saiba de um lugar melhor de caça. De qualquer forma, em algum momento, o ser humano sentiu a necessidade de esconder coisas de outros humanos.

Isso gera um problema, não é? Afinal, eu não quero que a tribo vizinha saiba onde pegamos tantos peixes, mas ao mesmo tempo quero poder falar sobre para quem eu quiser. Como fazemos isso?

Inventando códigos: Talvez, em vez de eu falar norte, eu fale "onde o sol se perde", indicando proximidade a uma montanha que tampa o sol, ou talvez eu simplesmente chame de "lugar sagrado".

O problema com o que é transmitido apenas verbalmente é que as palavras se perdem. Mas, quando escrevemos, elas passam a ter a capacidade de atravessar gerações e gerações.

## Criptografia através das eras

Criptografia para programadores é de fácil entendimento, mas se a gente olha pela ótica da **história**, tudo fica mais estranho e cinzento: Se considerarmos transformação da escrita e "escrita incomum" como uma ação criptográfica, o caso mais antigo que encontrei foi relatado por [David Kahn](https://en.wikipedia.org/wiki/David_Kahn_(writer)) no livro *The Codebreakers - The Story of Secret Writing* (Tradução livre: *Os Decifradores - A História da Escrita Secreta*): A tumba de [Khnumhotep II](https://en.wikipedia.org/wiki/Khnumhotep_II) continha hieróglifos alterados que dificultavam seu entendimento[^kahn]. Nada indica, no entanto, que a intenção era esconder o significado da escrita[^stauder]. De forma lúdica, sinto muita semelhança com as gírias e os memes da nossa era.

{{< figure src="posts/a-saga-do-programador-que-so-queria-resolver-o-problema-obfuscacao-de-dados/khnumhotep-ii-hieroglifos.jpg"
    alt="Pintura na parede da tumba de Khnumhotep II: um homem de manto estampado carrega um íbex, ao lado de hieróglifos pintados em vermelho e preto."
    cap="Detalhe de pintura da tumba de Khnumhotep II, em Beni Hasan (c. 1900 a.C.), só para ilustrar: estes não são os hieróglifos alterados citados por Kahn. Foto: Macquarie University, domínio público, via Wikimedia Commons." >}}

Se assumirmos que a criptografia tem como objetivo esconder o seu conteúdo, **desconsiderando o intuito de proteger o conteúdo**, podemos olhar para a Mesopotâmia do séc. XVII a.C.[^gadd] - [Gadd](https://en.wikipedia.org/wiki/C._J._Gadd) e [Thompson](https://en.wikipedia.org/wiki/Reginald_Campbell_Thompson) publicaram uma tabuleta com uma receita de esmalte que, mais tarde, foi lida como texto "cifrado" por outros pesquisadores, como [Caubet](https://www.idref.fr/026772639)[^caubet] e [Mollin](https://orcid.org/0000-0002-8750-883X)[^mollin], todavia Diepenbroek, ao citar essa leitura, alerta para o viés do entendimento, apontando que o intuito pode ser ritualístico e não segurança[^diep-meso].

Mas se a gente juntar intuito e técnica, no caso cifras, o mais antigo que encontrei foi o do grego [Eneias, o Tático](https://en.wikipedia.org/wiki/Aeneas_Tacticus), que descreve em seu livro *Sobre a defesa de posições fortificadas* (Original: *Poliorkētiká*, Πολιορκητικά) uma cifra que troca vogais por pontos, escondendo sua mensagem original[^eneias]. Escolhi ignorar a Cítala de [Lisandro](https://en.wikipedia.org/wiki/Lysander) (fim do séc. V a.C.)[^plutarco] devido à disputa sobre se é apenas mito ou realidade comprovada[^kelly].

## Batemos numa pedra até ela soltar faíscas e pensar. E agora?

Quando falamos de criptografia na computação, é impossível não falar da Enigma. Um feito de engenharia mecânica e elétrica da Alemanha que mudou como o mundo enxergava criptografia. Não muito tempo depois teríamos computadores, processos e tecnologias especializadas que vieram como consequência da existência da Enigma.

{{< figure src="posts/a-saga-do-programador-que-so-queria-resolver-o-problema-obfuscacao-de-dados/enigma-bundesarchiv.jpg"
    alt="Foto em preto e branco: mãos digitando no teclado de uma máquina Enigma, com as letras das teclas e do painel de lâmpadas à mostra."
    cap="Auxiliar de comunicações da força aérea alemã operando uma Enigma, c. 1943. Foto: Bundesarchiv, Bild 183-2007-0705-502, CC BY-SA 3.0 DE." >}}

Mas conforme essas máquinas deixam de ser armas de guerra e passam a ser tanto produto como meio de produção, começamos a ter a necessidade de cifrar dados - seja porque só algumas pessoas podem ter acesso, porque outros sistemas vão ter acesso, ou seja porque a legislação passou a padronizar o seu uso. O *Ware Report* (1970), de [Willis Ware](https://en.wikipedia.org/wiki/Willis_Ware), já cita "[resistir a] revelações acidentais, subversão interna e negação de uso a usuários legítimos"[^ware] (orig: *[resist] accidental disclosures, internal subversion, and denial of use to legitimate users*). Mas somente no começo dos anos 1990 temos a definição dos famosos Pilares da Segurança, documentados inicialmente (pelo menos no que consegui encontrar) pelo [ITSEC](https://en.wikipedia.org/wiki/Information_Technology_Security_Evaluation_Criteria).

> Neste contexto, segurança de TI significa:
>
> - confidencialidade: prevenção da revelação não autorizada de informação;
> - integridade: prevenção da modificação não autorizada de informação;
> - disponibilidade: prevenção da retenção não autorizada de informação ou de recursos.[^itsec]

(orig: *In this context, IT security means, confidentiality - prevention of the unauthorised disclosure of information; integrity - prevention of the unauthorised modification of information; availability - prevention of the unauthorised withholding of information or resources.*)

Esses pilares são o dominó inicial para chegarmos na nossa Lei Geral de Proteção de Dados, de 2018[^lgpd].

Mas um problema surge: Como eu, desenvolvedor, sem saber os dados de uma pessoa, posso resolver os problemas do meu sistema?

## Máscara das Mil Faces

> Em vez de desaparecer, o vampiro que emprega este poder pode se fazer passar por um estranho qualquer, alguém comum na área. Diferentemente de outros poderes de Ofuscação, este permite que seu usuário interaja e se comunique com aqueles que ele encontra.[^vampiro]

A LGPD, no art. 5º, I[^lgpd], define que, independentemente da informação, se ela pode ser usada para identificar um usuário único, ela deve ser protegida.

Todavia, pensa: Como eu posso saber que um problema está acontecendo com um usuário se eu não sei quem é esse usuário?

Não vou falar de observabilidade, NDAs e entendimentos legais e homologados. Vou focar aqui na técnica de ofuscação.

Segundo o Michaelis, ofuscação significa:

> **ofuscação**: Ato ou efeito de ofuscar(-se); ofuscamento.
>
> **ofuscar**: Fazer perder o brilho; impedir de ver ou ser visto; encobrir(-se), escurecer(-se), anuviar(-se).[^michaelis]

Na minha vida profissional, o que mais facilitou foi com certeza a ofuscação dos dados em um ambiente isolado. Na prática: um banco de dados protegido, sem acesso humano, em produção é replicado tendo seus dados alterados, inclusive *ids* e informações financeiras, para um ambiente de troubleshooting/homologação. Esse banco é recriado todos os dias. O desenvolvedor/suporte recebe o ticket, que contém já o id ofuscado (que foi calculado automaticamente).

Se considerarmos um ambiente simplificado *serverless*, nada impede também que, ao receber um chamado, o próprio sistema dispare o gatilho e adicione os dados no ambiente de troubleshooting, diminuindo o custo e a carga deste ambiente. Deve haver um segredo, um acordo entre os ambientes, mas que seja impossível você chegar de volta a uma pessoa em produção.

E os pilares estão todos aí: ninguém vê o dado real (**confidencialidade**), quem investiga nunca altera o dado de produção (**integridade**) e o suporte não pesa no banco de produção (**disponibilidade**).

Isolamento de responsabilidades é a chave. Para um sistema, é mais importante o que ele faz com uma pessoa do que quem é esta pessoa.

{{< diagrama src="posts/a-saga-do-programador-que-so-queria-resolver-o-problema-obfuscacao-de-dados/fluxo-ofuscacao.svg" >}}

1. A aplicação grava os dados no banco de produção.
2. O banco de produção envia um gatilho (um evento, não um trigger de banco).
3. A função serverless recebe o gatilho e ofusca os dados.
4. Os dados ofuscados são salvos no banco de troubleshooting.

E se olharmos para a ofuscação do banco, podemos pensar da seguinte forma neste pseudocódigo python exemplificando a ofuscação do id e do valor.

```python
import hashlib
import hmac
from decimal import Decimal

SEGREDO: bytes = ler_segredo("ofuscacao")


def ofuscar_id(id_original: int) -> str:
    return hmac.new(SEGREDO, str(id_original).encode(), hashlib.sha256).hexdigest()[:16]


def ofuscar_valor(id_original: int, valor: Decimal) -> Decimal:
    fator = Decimal(int(ofuscar_id(id_original), 16) % 100 + 50) / 100
    return (valor * fator).quantize(Decimal("0.01"))


def ao_receber_gatilho(evento: Evento) -> None:
    registro = evento.dados
    banco_troubleshooting.salvar(
        id=ofuscar_id(registro.id),
        cliente_id=ofuscar_id(registro.cliente_id),
        valor=ofuscar_valor(registro.id, registro.valor),
        status=registro.status,
    )
```

Por fim, a premissa prevalece: Desde o começo dos tempos o segredo não está em impedir que leiam, é garantir que só as pessoas corretas entendam.


[^kahn]: KAHN, David. *The Codebreakers: The Story of Secret Writing*. Macmillan, 1967,
    cap. 2. Citado via PINEAU, Roger. Resenha de *The Codebreakers*. *Studies in
    Intelligence*, v. 12, n. 3, 1968. Disponível em
    [cia.gov](https://www.cia.gov/resources/csi/static/Review-The-Codebreakers.pdf).

[^stauder]: STAUDER, Andréas. "Introduction". In: KLOTZ, David; STAUDER, Andréas (ed.).
    *Enigmatic Writing in the Egyptian New Kingdom I*. 2020, p. 1–5. Disponível em
    [web.archive.org](https://web.archive.org/web/20240909060622/https://archiv.ub.uni-heidelberg.de/propylaeumdok/5400/1/Stauder_Introduction_Enigmatic_Writing.pdf).

[^gadd]: GADD, C. J.; THOMPSON, R. Campbell. "A Middle-Babylonian Chemical Text".
    *Iraq*, v. 3, n. 1, 1936, p. 87–96. Disponível em
    [cambridge.org](https://cambridge.org/core/journals/iraq/article/middlebabylonian-chemical-text/F4B01DC7752095019833F30BE77CD2BD).

[^caubet]: CAUBET, Annie. "Vitreous Materials". In: ARUZ, J.; BENZEL, K.; EVANS, J. (ed.).
    *Beyond Babylon: Art, Trade, and Diplomacy in the Second Millennium B.C.* New York:
    The Metropolitan Museum of Art; New Haven: Yale University Press, 2008, p. 419–434
    (leitura como cifra na p. 421). Citado via DIEPENBROEK, 2020, p. 53, nota 82.

[^mollin]: MOLLIN, Richard A. *Codes: The Guide to Secrecy From Ancient to Modern Times*.
    Boca Raton: Chapman & Hall/CRC, 2005, p. 5. Citado via DIEPENBROEK, 2020, p. 53,
    nota 82.

[^diep-meso]: DIEPENBROEK, Martine L. M. *Myths and Histories of the Spartan scytale*.
    Tese (Doutorado) — Universidade de Bristol, 2020, § 1.1, p. 52–53. Disponível em
    [research-information.bris.ac.uk](https://research-information.bris.ac.uk/ws/files/263833703/Myths_and_Histories_of_the_Spartan_scytale_29_11_2020.pdf).

[^eneias]: ENEIAS, O TÁTICO. *Sobre a defesa de posições fortificadas*, 31.30–31.
    Trad. Illinois Greek Club, 1928. Disponível em
    [penelope.uchicago.edu](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Aeneas_Tacticus/E*.html).

[^plutarco]: PLUTARCO. *Vida de Lisandro*, 19.4–7. Trad. Bernadotte Perrin, 1916.
    Disponível em
    [penelope.uchicago.edu](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives/Lysander*.html).

[^kelly]: DIEPENBROEK, Martine L. M. *Myths and Histories of the Spartan scytale*.
    Tese (Doutorado) — Universidade de Bristol, 2020, p. 23–24, sobre KELLY, Thomas.
    "The Myth of the Skytale". *Cryptologia*, v. 22, n. 3, 1998, p. 244–260.
    Disponível em
    [research-information.bris.ac.uk](https://research-information.bris.ac.uk/ws/files/263833703/Myths_and_Histories_of_the_Spartan_scytale_29_11_2020.pdf).

[^ware]: WARE, Willis H. (ed.). *Security Controls for Computer Systems: Report of
    Defense Science Board Task Force on Computer Security*. RAND, R-609, 1970, p. vi.
    Disponível em
    [csrc.nist.gov](https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ware70.pdf).

[^itsec]: FRANÇA; ALEMANHA; PAÍSES BAIXOS; REINO UNIDO. *Information Technology
    Security Evaluation Criteria (ITSEC)*, v. 1.2, 28 jun. 1991, § 0.2. Disponível em
    [wiretapped.mirrorservice.org](https://wiretapped.mirrorservice.org/info/reference/cesg-publications/Information-Technology-Security-Evaluation-Criteria.pdf).

[^lgpd]: BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de
    Dados Pessoais (LGPD). Disponível em
    [planalto.gov.br](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm).

[^vampiro]: *Vampiro: A Máscara*. 5. ed. Livro básico, p. 262. Edição brasileira de
    *Vampire: The Masquerade 5th Edition*, White Wolf, 2018.

[^michaelis]: MICHAELIS. "Ofuscação" e "ofuscar". *Michaelis — Dicionário Brasileiro
    da Língua Portuguesa*. Melhoramentos, on-line. Disponível em
    [michaelis.uol.com.br](https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro/ofusca%C3%A7%C3%A3o/)
    e [michaelis.uol.com.br](https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro/ofuscar/).
