---
title: "Quem definiu os pilares da segurança da informação (tríade CIA)?"
type: research
status: concluida
created: 2026-11-19
post: "[[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/post]]"
---

> [!tldr] TL;DR
> - Ninguém "inventou" a tríade de uma vez. As três ideias aparecem juntas, com outros nomes, em relatórios militares dos EUA: Ware (1970) e Anderson (1972).
> - Saltzer e Schroeder (1975) deram a forma clássica: liberação, modificação e negação de uso não autorizadas. Eles não usam as palavras "confidencialidade" e "disponibilidade".
> - A frase com as três palavras juntas aparece numa publicação do NBS (atual NIST) de 1977. É a mais antiga que localizei e conferi.
> - A sigla "CIA" e a palavra "tríade" não têm dono confirmado. Os candidatos são Steve Lipner (c. 1986) e John McCumber (1991). Nenhum dos dois foi confirmado na fonte original.
> - Virou definição normativa entre 1991 e 2002 (ITSEC, X.800, OCDE, FISMA). No Brasil, desde o Decreto 3.505/2000, a lista oficial tem quatro itens: disponibilidade, integridade, confidencialidade e autenticidade. Em 2000 tinha também o não repúdio.

## Pergunta

Quem definiu os pilares da segurança da informação (confidencialidade, integridade e disponibilidade, a "tríade CIA")? Quem cunhou o termo? Quando viraram norma? Como evoluíram?

## Resposta curta

**1. As ideias nasceram juntas, sem os nomes atuais (1970–1975).**

- O Ware Report (1970) já fala em resistir a "accidental disclosures, internal subversion, and denial of use to legitimate users"[^1].
  Tradução: "revelações acidentais, subversão interna e negação de uso a usuários legítimos".
- O mesmo relatório pede que o sistema "must not deny service to users"[^1] e fala em preservar "the integrity of their data and their programs"[^1].
- O Anderson Report (1972, vol. II) lista três formas de interferência[^2]:
  - "gain of information by an unauthorized user" (obter informação sem autorização);
  - "denial of information to an authorized user" (negar informação a quem tem direito);
  - "falsification of information to authorized users" (falsificar a informação).
- Saltzer e Schroeder (1975) escrevem as três categorias que hoje lemos como C, I e A[^3]:
  - "Unauthorized information release" (liberação não autorizada);
  - "Unauthorized information modification" (modificação não autorizada);
  - "Unauthorized denial of use" (negação de uso não autorizada).
- Eles atribuem a divisão a "security specialists (e.g., Anderson [6])"[^3]. A referência [6] é um capítulo de J. Anderson de 1973 no *Advances in Computers*. Não é o relatório de 1972[^4].

**2. As três palavras juntas: NBS, 1977.**

- O relatório de uma sessão do workshop do NBS de março de 1977 define[^5]:
  > "Computer Security — The protection of system data and resources from accidental and deliberate threats to confidentiality, integrity, and availability."

  Tradução: "Segurança computacional: a proteção dos dados e recursos do sistema contra ameaças acidentais e deliberadas à confidencialidade, à integridade e à disponibilidade."
- O autor é o grupo da sessão "Post Processing Audit Tools and Techniques" (A. J. Neumann, N. Statland e R. D. Webb). O texto é um relatório de consenso, p. 11-4[^5].
- Não é norma: é a ata de um workshop, publicada pelo governo dos EUA.

**3. A palavra "tríade" e a sigla "CIA": sem dono confirmado.**

- McCumber (1991) escreve "The triad of critical information characteristics"[^6]. Para ele, C, I e A são "three critical characteristics of information". Ele cita Pfleeger (1989) como fonte e usa "confidentiality" no lugar do "secrecy" dela[^6].
- Rick Howard (2025) conversou com McCumber. Segundo esse relato, McCumber diz que a ideia "was in the air" e que aprendeu o conceito com Steve LaFountain. Howard então o "nomeia" originador da frase[^21]. É uma conversa relatada num blog, não um documento.
- A Wikipedia atribui a sigla "CIA" a Steve Lipner, por volta de 1986, citando van der Ham (2021)[^25]. Não consegui abrir o artigo. A atribuição fica **não confirmada**.
- Ainda segundo Howard, a sigla se popularizou no fim dos anos 1990, com o CBK do CISSP (1997). Ele mesmo diz que isso é lembrança e crença sua ("I believe")[^21].

**4. Quando virou definição normativa.**

| Ano  | Documento                                                                 | O que define                                                                                                             |
| ---- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 1991 | ITSEC (critérios harmonizados de França, Alemanha, Holanda e Reino Unido) | "IT security means" confidencialidade, integridade e disponibilidade, cada uma como prevenção de algo "unauthorised"[^7] |
| 1991 | CCITT X.800 (alinhada à ISO 7498-2)                                       | Define disponibilidade, confidencialidade e integridade de dados. Define também o serviço de não repúdio[^8]             |
| 1992 | Diretrizes da OCDE                                                        | Objetivo da segurança: proteger contra "failures of availability, confidentiality, and integrity"[^9]                    |
| 1995 | NIST SP 800-12                                                            | Segurança computacional preserva "integrity, availability and confidentiality"[^13]                                      |
| 2000 | Decreto 3.505 (Brasil)                                                    | Objetivo: assegurar confidencialidade, integridade, autenticidade, não repúdio e disponibilidade[^15]                    |
| 2002 | FISMA (lei federal dos EUA), 44 U.S.C. § 3542                             | "information security" garante integridade, confidencialidade e disponibilidade[^10]                                     |
| 2004 | FIPS 199                                                                  | Usa os três objetivos da FISMA para classificar o impacto (baixo, moderado, alto)[^12]                                   |
| hoje | 44 U.S.C. § 3552(b)(3)                                                    | Mesmo texto da FISMA 2002, renumerado[^11]                                                                               |

- A FISMA põe autenticidade e não repúdio **dentro** da integridade: "integrity [...] includes ensuring information nonrepudiation and authenticity"[^10][^11].
- A ISO/IEC 27000 define segurança da informação como preservação de confidencialidade, integridade e disponibilidade. Uma nota diz que outras propriedades "can also be involved": autenticidade, responsabilização (*accountability*), não repúdio e confiabilidade[^26]. A norma é paga. Não li o texto oficial.

**5. Extensões.**

- **Brasil: quatro pilares, não três.** Em 2000, o Decreto 3.505 lista cinco itens: "a confidencialidade, a integridade, a autenticidade, o não-repúdio e a disponibilidade"[^15]. A IN GSI/PR 01/2008 fica com quatro: disponibilidade, integridade, confidencialidade e autenticidade, cada uma definida[^16]. Os Decretos 9.637/2018 e 12.572/2025 (PNSI) repetem os quatro[^18][^19].
- **Não repúdio.** É formalizado como serviço de segurança na X.800, em 1991: "proof of origin" e "proof of delivery"[^8].
- **Hexad de Parker.** Donn Parker propôs seis elementos: confidencialidade, posse ou controle, integridade, autenticidade, disponibilidade e utilidade. A proposta saiu num paper de 1995[^24] e no livro *Fighting Computer Crime* (1998)[^23]. Não li nenhum dos dois: são protegidos. A lista dos seis vem de fontes secundárias[^21][^22].
- **Leitura acadêmica.** Samonas e Coss (2014) resumem as camadas: anos 1970 = CIA; anos 1980 = + autenticidade e não repúdio; anos 1990 = + correção da especificação; anos 2000 = + responsabilidade, integridade das pessoas, confiança, ética e identidade. Eles concluem que tudo cabe dentro das três letras originais[^20].

## Linha do tempo

| Data | Fato | Fonte |
|---|---|---|
| 11 fev. 1970 | Ware Report (Defense Science Board, publicado pela RAND): revelação acidental, subversão, negação de uso; "integrity" de dados e programas | [^1] |
| out. 1972 | Anderson Report, vol. II, apêndice IV, pp. 91–92: obter, negar e falsificar informação | [^2] |
| 1973 | J. Anderson, "Information security in a multi-user computer environment" (*Advances in Computers*, v. 12). Não lido; citado por Saltzer e Schroeder | [^4] |
| set. 1975 | Saltzer e Schroeder: liberação, modificação e negação de uso não autorizadas | [^3] |
| mar./out. 1977 | Workshop do NBS (Miami Beach), publicado como SP 500-19: "confidentiality, integrity, and availability" | [^5] |
| c. 1986 | Steve Lipner teria cunhado "CIA" (**não confirmado**) | [^25] |
| mar. 1991 | CCITT X.800: definições e serviço de não repúdio | [^8] |
| 28 jun. 1991 | ITSEC v1.2: "IT security means" C, I, A | [^7] |
| out. 1991 | McCumber: "triad of critical information characteristics" | [^6] |
| 26 nov. 1992 | OCDE: diretrizes de segurança de sistemas de informação (substituídas em 2002) | [^9][^27] |
| 1995 | Parker: paper com os seis elementos (não lido) | [^24] |
| out. 1995 | NIST SP 800-12 (*NIST Handbook*) | [^13] |
| 1998 | Parker, *Fighting Computer Crime* (não lido) | [^23] |
| 13 jun. 2000 | Decreto 3.505: C, I, autenticidade, não repúdio, D | [^15] |
| 17 dez. 2002 | FISMA (Lei Pública 107-347, título III), 44 U.S.C. § 3542 | [^10] |
| fev. 2004 | FIPS 199 | [^12] |
| 13 jun. 2008 | IN GSI/PR 01/2008: D, I, C, autenticidade | [^16] |
| jun. 2017 | NIST SP 800-12 Rev. 1 | [^14] |
| 26 dez. 2018 | Decreto 9.637 (PNSI) | [^18] |
| 27 maio 2020 | IN GSI/PR 01/2020 revoga a IN 01/2008 (art. 23, I) | [^17] |
| 4 ago. 2025 | Decreto 12.572 (nova PNSI) revoga o 9.637 | [^19][^18] |

## Divergências

| Tema | Fonte A diz | Fonte B diz | Nota |
|---|---|---|---|
| Primeira aparição do conceito | Samonas e Coss: o Anderson Report (1972) "identified the following three categories" e citam o texto de liberação, modificação e negação[^20] | O texto que eles citam é de Saltzer e Schroeder (1975)[^3]. O Anderson de 1972 fala em "gain / denial / falsification"[^2]. Saltzer e Schroeder citam o Anderson de **1973**, não o de 1972[^4] | Confiei nas primárias. A ideia já está no Anderson de 1972 e até no Ware de 1970[^1], mas a redação famosa é de 1975 |
| Saltzer e Schroeder usam C, I e A? | Samonas e Coss: os "basic principles" de 1975 "include the triad of confidentiality, integrity and availability"[^20] | Howard (via Jennifer Reed): o paper não usa a frase nem os termos[^21]. Na cópia lida, "integrity" aparece no sentido de **confiabilidade** contra falhas acidentais (nota 3 do paper)[^3] | A primária confirma Howard: as categorias são as mesmas, as palavras não |
| Quando as três foram juntadas | NBS SP 500-19 (1977) já define "computer security" com as três palavras[^5] | TechTarget: "By 1998, people were using the three concepts together as the CIA triad"[^22] | A primária de 1977 derruba "1998" como primeira junção. 1998 pode valer para a **popularização da sigla**, não do conceito |
| Datação de cada pilar | TechTarget: confidencialidade em 1976 (estudo da Força Aérea); integridade em 1987 (Clark e Wilson); disponibilidade em 1988[^22] | As três já aparecem juntas em 1970–1977[^1][^2][^3][^5] | TechTarget não cita fonte para as datas. Não verifiquei o estudo de 1976 nem Clark e Wilson. Parece cronologia de **modelos formais** (Bell-LaPadula, Clark-Wilson), não da ideia |
| Quem cunhou "CIA"/"tríade" | Wikipedia: Steve Lipner, c. 1986, citando van der Ham (2021)[^25] | Howard: McCumber (1991) foi o primeiro a publicar "triad"; McCumber diz que aprendeu com Steve LaFountain[^21][^6] | Nenhuma das duas foi confirmada. Só a palavra "triad" em McCumber 1991 está verificada na primária |
| Lugar da autenticidade e do não repúdio | FISMA: dentro da integridade[^10] | Brasil: autenticidade é pilar próprio[^16][^19]; em 2000, o não repúdio também[^15]. ISO 27000: "outras propriedades" que podem estar envolvidas[^26] | Não é erro de ninguém: são escolhas de enquadramento. Samonas e Coss classificam ambas como parte da integridade[^20] |
| Parker e a frase "CIA triad" | TechTarget: Parker "broadened the CIA triad to a hexad" em 1998[^22] | Howard: Parker "never mentions the phrase 'CIA Triad'" no livro[^21] | Livro não lido (protegido). Fica em aberto |

## Para o post

**Frases seguras:**

- "Os três pilares não têm um inventor. Eles saíram de relatórios militares dos EUA no começo dos anos 1970."
- "Em 1975, Saltzer e Schroeder resumiram o problema em três ameaças: alguém lê o que não devia, alguém muda o que não devia, alguém impede você de usar o que é seu."
- "A frase 'confidencialidade, integridade e disponibilidade' já aparece num documento do governo americano em 1977."
- "No Brasil, a política oficial fala em quatro pilares: disponibilidade, integridade, confidencialidade e autenticidade."
- "Nos EUA, a lei põe autenticidade e não repúdio dentro da integridade."

**Armadilhas (mitos comuns):**

- "A tríade CIA foi criada em 1998." Falso para o conceito. 1998 é, no máximo, a época em que a sigla se popularizou (não confirmado).
- "Saltzer e Schroeder definiram confidencialidade, integridade e disponibilidade." Eles descrevem as três ameaças, sem esses nomes.
- "O Anderson Report definiu 'unauthorized information release...'." Esse texto é de Saltzer e Schroeder (1975).
- "Steve Lipner cunhou a sigla CIA." Só pista (Wikipedia). Não use como fato.
- "CIA" não tem relação com a agência de inteligência. Por isso alguns autores escrevem "AIC".
- Ordem das letras: os EUA (FISMA) listam I, C, A; o Brasil, D, I, C, A; a OCDE, A, C, I. Não há ordem "oficial".

**Gancho para o ângulo do post:** o dev que só queria resolver o problema usa os três pilares sem saber. Mascarar dados é **confidencialidade**. Não corromper o dado ao mascarar é **integridade**. Não derrubar o sistema no processo é **disponibilidade**.

## Em aberto

- **Sigla "CIA" e Steve Lipner.** O artigo de van der Ham (2021) é acesso aberto (CC BY-SA), mas o repositório e a ACM bloquearam o acesso automatizado. Ler à mão: <https://doi.org/10.1145/3442445>.
- **Primeiro uso impresso de "CIA triad".** Não localizei. Candidatos: materiais do CISSP/CBK (1997–1999), segundo Howard[^21].
- **Hexad de Parker.** Conferir no livro de 1998 o capítulo "Six Essential Foundation Elements", com página, e se ele usa a frase "CIA triad".
- **ISO/IEC 27000.** Conferir no texto oficial o número da definição e a lista exata da nota. Desde quando a definição existe? A linhagem BS 7799 (1995) e ISO/IEC 17799 (2000) não foi verificada.
- **FISMA 2002.** Pista não verificada: a mesma definição teria saído antes, no título X do Homeland Security Act (Lei Pública 107-296, nov. 2002). Também não verifiquei se o Computer Security Act de 1987 já usava os três termos.
- **Afirmações da TechTarget** (1976, Força Aérea; 1987, Clark-Wilson; 1988, disponibilidade). Não verificadas na fonte.
- **Glossário do GSI.** A Portaria GSI/PR nº 93/2021 define autenticidade e não repúdio, mas não localizei o texto oficial no DOU.
- **NSTISSI nº 4011.** A cópia do texto de McCumber é o anexo dessa instrução. A data da instrução não consta na cópia. O original de 1991 está nos anais da 14th National Computer Security Conference, pp. 328–337 (segundo Howard[^21]).

## Fontes

[^1]: Willis H. Ware (ed.). *Security Controls for Computer Systems (U): Report of Defense Science Board Task Force on Computer Security* (RAND R-609). 11 fev. 1970. Conclusão 2, p. vi; Parte A, p. 1; p. 11; Parte C, p. 26. Tipo: primária. Original: <https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ware70.pdf> · Wayback: <https://web.archive.org/web/20261014064846/https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ware70.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-origens/1970-ware-security-controls]] · Acessado em 2026-11-19.
[^2]: James P. Anderson. *Computer Security Technology Planning Study*, vol. II (ESD-TR-73-51). Out. 1972. Apêndice IV, pp. 91–92. Tipo: primária. Original: <https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ande72.pdf> · Wayback: <https://web.archive.org/web/20261111140900/https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ande72.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-origens/1972-anderson-planning-study-v2]] · Acessado em 2026-11-19.
[^3]: Jerome H. Saltzer e Michael D. Schroeder. "The Protection of Information in Computer Systems". *Proceedings of the IEEE* 63(9), set. 1975. Seção I.A.1 ("General Observations") e nota 3. Versão HTML no site do autor (MIT). Tipo: primária. Original: <https://web.mit.edu/Saltzer/www/publications/protection/Basic.html> · Wayback: <https://web.archive.org/web/20261115222658/https://web.mit.edu/Saltzer/www/publications/protection/Basic.html> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-origens/1975-saltzer-schroeder-protection]] · Acessado em 2026-11-19.
[^4]: Saltzer e Schroeder, 1975. Lista de referências: [6] J. Anderson, "Information security in a multi-user computer environment", *Advances in Computers* v. 12, 1973; [95] Anderson Report, 1972; [96] Ware Report, 1970, "(Classified confidontial.)" [sic]. Tipo: primária. Original: <https://web.mit.edu/Saltzer/www/publications/protection/References.html> · Wayback: <https://web.archive.org/web/20260823230840/https://web.mit.edu/Saltzer/www/publications/protection/References.html> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-origens/1975-saltzer-schroeder-referencias]] · Acessado em 2026-11-19.
[^5]: Zella G. Ruthberg e Robert G. McKenzie (eds.). *Audit and Evaluation of Computer Security*. NBS Special Publication 500-19. Out. 1977. Sessão "Post Processing Audit Tools and Techniques" (A. J. Neumann, N. Statland e R. D. Webb), pp. 11-3 e 11-4. Tipo: primária. Original: <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nbsspecialpublication500-19.pdf> · Wayback: <https://web.archive.org/web/20261109190544/https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nbsspecialpublication500-19.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-origens/1977-nbs-sp-500-19]] · Acessado em 2026-11-19.
[^6]: John R. McCumber. "Information Systems Security: A Comprehensive Model". 14th National Computer Security Conference, out. 1991. Reproduzido como anexo da NSTISSI nº 4011; seção "Critical Information Characteristics". Cópia hospedada por curso da Universidad de Costa Rica. Tipo: primária. Original: <https://os.ecci.ucr.ac.cr/ci0122/Temas/Semana-02/McCumberAX.pdf> · Wayback: <https://web.archive.org/web/20251206214619/https://os.ecci.ucr.ac.cr/ci0122/Temas/Semana-02/McCumberAX.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/1991-mccumber-nstissi-4011]] · Acessado em 2026-11-19.
[^7]: *Information Technology Security Evaluation Criteria (ITSEC)*, v. 1.2. 28 jun. 1991. Parágrafo 0.2 e definições 6.9, 6.15 e 6.41. Cópia em espelho de publicações do CESG. Tipo: primária. Original: <https://wiretapped.mirrorservice.org/info/reference/cesg-publications/Information-Technology-Security-Evaluation-Criteria.pdf> · Wayback: sem snapshot no Wayback (o Save Page Now falhou duas vezes) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-internacionais/1991-itsec]] · Acessado em 2026-11-19.
[^8]: CCITT (atual ITU-T). *Recommendation X.800: Security Architecture for Open Systems Interconnection for CCITT Applications*. Genebra, 1991 (aprovada em 22 mar. 1991). Itens 3.3.11, 3.3.16, 3.3.21, 3.3.44 e 5.2.5. Tipo: primária. Original: <https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-X.800-199103-I!!PDF-E&type=items> · Wayback: <https://web.archive.org/web/20260905191334/https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-X.800-199103-I!!PDF-E&type=items> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-internacionais/1991-itu-x800]] · Acessado em 2026-11-19.
[^9]: OCDE. *Recommendation of the Council concerning Guidelines for the Security of Information Systems* (OECD/LEGAL/0271). Adotada em 26 nov. 1992 [C(92)188/FINAL], segundo a recomendação de 2002 que a substituiu[^27]. Seções III e IV. Tipo: primária. Original: <https://legalinstruments.oecd.org/public/doc/329/329.en.pdf> · Wayback: sem snapshot no Wayback (o Save Page Now falhou duas vezes) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-internacionais/1992-oecd-guidelines-security]] · Acessado em 2026-11-19.
[^10]: Estados Unidos. *Public Law 107-347* (E-Government Act of 2002), título III (Federal Information Security Management Act), sec. 301, 44 U.S.C. § 3542(b)(1). 17 dez. 2002. 116 Stat. 2947. Tipo: primária. Original: <https://www.govinfo.gov/content/pkg/PLAW-107publ347/pdf/PLAW-107publ347.pdf> · Wayback: <https://web.archive.org/web/20261112105459/https://www.govinfo.gov/content/pkg/PLAW-107publ347/pdf/PLAW-107publ347.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/2002-fisma-pl-107-347]] · Acessado em 2026-11-19.
[^11]: Estados Unidos. *44 U.S.C. § 3552 — Definitions*, (b)(3). United States Code, edição de 2024 (GPO). Tipo: primária. Original: <https://www.govinfo.gov/content/pkg/USCODE-2024-title44/html/USCODE-2024-title44-chap35-subchapII-sec3552.htm> · Wayback: <https://web.archive.org/web/20261119141917/https://www.govinfo.gov/content/pkg/USCODE-2024-title44/html/USCODE-2024-title44-chap35-subchapII-sec3552.htm> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/2014-usc-44-3552]] · Acessado em 2026-11-19.
[^12]: NIST. *FIPS PUB 199: Standards for Security Categorization of Federal Information and Information Systems*. Fev. 2004. Tipo: primária. Original: <https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf> · Wayback: <https://web.archive.org/web/20261116113055/https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.199.pdf> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/2004-fips-199]] · Acessado em 2026-11-19.
[^13]: NIST. *SP 800-12: An Introduction to Computer Security: The NIST Handbook*. Out. 1995. Seção 1.4 ("Important Terminology"). Tipo: primária. Original: <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-12.pdf> · Wayback: <https://web.archive.org/web/20261117191828/https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-12.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/1995-nist-sp-800-12]] · Acessado em 2026-11-19.
[^14]: NIST. *SP 800-12 Rev. 1: An Introduction to Information Security*. Jun. 2017. Seção 1.4; definições retiradas da CNSSI 4009 (2015). Tipo: primária. Original: <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-12r1.pdf> · Wayback: <https://web.archive.org/web/20261115000403/https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-12r1.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/2017-nist-sp-800-12r1]] · Acessado em 2026-11-19.
[^15]: Brasil. *Decreto nº 3.505, de 13 de junho de 2000*. Institui a Política de Segurança da Informação nos órgãos e entidades da APF. Art. 2º, II; art. 3º, I; art. 4º, VIII. Revogado pelo Decreto nº 9.637/2018. Tipo: primária. Original: <https://www.planalto.gov.br/ccivil_03/decreto/d3505.htm> · Wayback: <https://web.archive.org/web/20261003220250/http://www.planalto.gov.br/ccivil_03/decreto/d3505.htm> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-brasil/2000-decreto-3505]] · Acessado em 2026-11-19.
[^16]: Brasil. GSI/PR. *Instrução Normativa nº 1, de 13 de junho de 2008*. Art. 2º, II a VI. Texto reproduzido pelo Normas Brasil (cópia oficial no portal do GSI não localizada). Tipo: primária. Original: <https://www.normasbrasil.com.br/norma/instrucao-normativa-1-2008_76883.html> · Wayback: <https://web.archive.org/web/20261119141708/https://www.normasbrasil.com.br/norma/instrucao-normativa-1-2008_76883.html> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-brasil/2008-in-gsi-01]] · Acessado em 2026-11-19.
[^17]: Brasil. GSI/PR. *Instrução Normativa nº 1, de 27 de maio de 2020* (consolidada). Art. 23, I, revoga a IN 01/2008. Tipo: primária. Original: <https://www.gov.br/gsi/pt-br/seguranca-da-informacao-e-cibernetica/legislacao/copy_of_IN01_consolidada.pdf> · Wayback: <https://web.archive.org/web/20261004090801/https://www.gov.br/gsi/pt-br/seguranca-da-informacao-e-cibernetica/legislacao/copy_of_IN01_consolidada.pdf> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-brasil/2020-in-gsi-01]] · Acessado em 2026-11-19.
[^18]: Brasil. *Decreto nº 9.637, de 26 de dezembro de 2018*. Institui a Política Nacional de Segurança da Informação. Arts. 1º e 2º, IV. Revogado pelo Decreto nº 12.572/2025. Tipo: primária. Original: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/D9637.htm> · Wayback: <https://web.archive.org/web/20261030082750/https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/D9637.htm> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-brasil/2018-decreto-9637]] · Acessado em 2026-11-19.
[^19]: Brasil. *Decreto nº 12.572, de 4 de agosto de 2025*. Institui a Política Nacional de Segurança da Informação. Art. 1º. Tipo: primária. Original: <https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/Decreto/D12572.htm> · Wayback: <https://web.archive.org/web/20261110140307/https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12572.htm> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-brasil/2025-decreto-12572]] · Acessado em 2026-11-19.
[^20]: Spyridon Samonas e David Coss. "The CIA Strikes Back: Redefining Confidentiality, Integrity and Availability in Security". *Journal of Information System Security* 10(3): 21–45. 2014. pp. 23–25 (história) e 28–29 (tabelas 2 e 3). Tipo: secundária (periódico acadêmico). Original: <https://jissec.org/Contents/V10/N3/jissec-v10n3-samonas-p21-ci> · Wayback: não arquivado · Cópia: não disponível (protegido; vendido pela revista) · Acessado em 2026-11-19.
[^21]: Rick Howard. "Part I: Is the CIA Triad Dead?". *Diffuser* (Substack), 10 nov. 2025. Tipo: secundária (ensaio de especialista, com relato de conversa). Original: <https://diffuser.substack.com/p/is-the-cia-triad-dead> · Wayback: <https://web.archive.org/web/20261119141838/https://diffuser.substack.com/p/is-the-cia-triad-dead> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-triade-analises/2025-howard-cia-triad-dead]] · Acessado em 2026-11-19.
[^22]: Wesley Chai e Cameron Hashemi-Pour. "What is the CIA triad (confidentiality, integrity and availability)?". *TechTarget*, 21 dez. 2023. Seção de história. Tipo: terciária (obra de referência). Original: <https://www.techtarget.com/whatis/definition/Confidentiality-integrity-and-availability-CIA> · Wayback: <https://web.archive.org/web/20261026052729/https://www.techtarget.com/whatis/definition/Confidentiality-integrity-and-availability-CIA> (snapshot antigo: o Save Page Now falhou) · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-triade-analises/2023-techtarget-cia-triad]] · Acessado em 2026-11-19.
[^23]: Donn B. Parker. *Fighting Computer Crime: A New Framework for Protecting Information*. Wiley, 1998. ISBN 978-0-471-16378-7. Capítulo "Six Essential Foundation Elements" (página não conferida). Tipo: primária. **Não lido.** Cópia: não disponível (protegido).
[^24]: Donn B. Parker. "A New Framework for Information Security to Avoid Information Anarchy". In: *Information Security — the Next Decade* (IFIP), 1995, pp. 153–164. DOI: <https://doi.org/10.1007/978-0-387-34873-5_13>. Tipo: primária. **Não lido** (acesso fechado). Cópia: não disponível (protegido).
[^25]: Jeroen van der Ham. "Toward a Better Understanding of 'Cybersecurity'". *Digital Threats: Research and Practice* 2(3), art. 18, 2021. DOI: <https://doi.org/10.1145/3442445>. Tipo: secundária. **Não lido**: é acesso aberto (CC BY-SA), mas o site bloqueou o acesso automatizado. A atribuição a Lipner chegou via Wikipedia ("CIA triad"), que serve só de pista. Cópia: não disponível (não obtida).
[^26]: ISO/IEC. *ISO/IEC 27000: Information security management systems — Overview and vocabulary*. Definição de "information security" e nota. Tipo: primária. Norma paga: citada sem cópia. **Texto oficial não conferido**: definição e nota vistas só em reproduções secundárias (busca de 2026-11-19). Cópia: não disponível (protegido).
[^27]: OCDE. *Recommendation of the Council concerning Guidelines for the Security of Information Systems and Networks — Towards a Culture of Security* (2002). Preâmbulo: substitui a recomendação de 26 nov. 1992 [C(92)188/FINAL]. Tipo: primária. Original: <https://legalinstruments.oecd.org/public/doc/116/116.en.pdf> · Wayback: <https://web.archive.org/web/20261031023854/https://legalinstruments.oecd.org/public/doc/116/116.en.pdf> · Cópia: [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-internacionais/2002-oecd-guidelines-security-networks]] · Acessado em 2026-11-19.
