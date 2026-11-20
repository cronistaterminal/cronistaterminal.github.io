---
title: "Resumo — Origens da segurança de computadores"
type: resumo-fontes
updated: 2026-11-19
---

# Origens da segurança de computadores

## 1970 · Ware Report, Security Controls for Computer Systems

- **Autor/órgão:** Willis H. Ware (presidente), Task Force on Computer Security do Defense Science Board; publicado pela RAND Corporation · **Tipo:** relatório técnico · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-origens/1970-ware-security-controls]] · **Original:** https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ware70.pdf
- **Do que trata:** relatório ao Departamento de Defesa dos EUA sobre como proteger informação classificada em computadores de uso compartilhado (time-sharing).
- **Conteúdo:**
  - Classificado como CONFIDENTIAL na origem. Diz ser "the first attempt to codify the principles and details" do problema.
  - Conclusão central: "Providing satisfactory security controls in a computer system is in itself a system design problem". Só software não basta.
  - A tecnologia da época protege um ambiente fechado (usuários com credencial, linhas protegidas), mas não um ambiente aberto.
  - Três tipos de vulnerabilidade: revelação acidental, penetração deliberada (passiva, como grampo; ativa, como "trap-doors") e ataque físico.
  - Partes: natureza do problema, política (pessoal, rótulos de segurança, certificação), recomendações técnicas (hardware, software, controle de acesso, terminais, linhas) e controle administrativo. O apêndice especifica um sistema multinível automatizado.
  - Pede pesquisa em cifração dentro do computador, certificação e apagamento seguro de mídia magnética ("sanitization or degaussing").

## 1972 · Anderson Report, Computer Security Technology Planning Study, Vol. II

- **Autor/órgão:** James P. Anderson e painel (apêndices de E. Nelson, C. Weissman, B. Peters, E. L. Glaser e S. Lipner), para a Electronic Systems Division da Força Aérea dos EUA · **Tipo:** relatório técnico · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-origens/1972-anderson-planning-study-v2]] · **Original:** https://csrc.nist.gov/files/pubs/conference/1998/10/08/proceedings-of-the-21st-nissc-1998/final/docs/early-cs-papers/ande72.pdf
- **Do que trata:** plano de desenvolvimento para a Força Aérea obter computação multinível segura e de uso aberto.
- **Conteúdo:**
  - Volume II, com os detalhes do plano. Problema: sistemas com dados de vários níveis de sigilo, usados por pessoas sem a mesma credencial, e cada vez mais ligados em rede.
  - Ameaça principal: o "malicious user", um usuário do próprio sistema que tenta furar os controles. Executivos monolíticos e grandes demais não podem ser validados.
  - Defesa: controle de acesso ao sistema, mecanismo de autorização e execução controlada de programas ("controlled sharing").
  - Propõe o "Reference Monitor", que valida toda referência de um programa contra o que o usuário pode acessar. Sua implementação deve ser "tamper proof", "always be invoked" e "small enough to be subject to analysis and tests".
  - Plano: modelo formal de segurança, kernel de segurança, protótipo, terminal seguro, concentrador cripto e cifração de arquivos. Também soluções provisórias e pesquisa exploratória.
  - Apêndices sobre técnicas de penetração, estado da arte, bancos de dados, controles de procedimento e tendências da Força Aérea.

## 1975 · Saltzer e Schroeder, The Protection of Information in Computer Systems (Seção I)

- **Autor/órgão:** Jerome H. Saltzer e Michael D. Schroeder (MIT) · **Tipo:** artigo · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-origens/1975-saltzer-schroeder-protection]] · **Original:** https://web.mit.edu/Saltzer/www/publications/protection/Basic.html
- **Do que trata:** princípios básicos para proteger informação em computadores usados por várias pessoas ao mesmo tempo.
- **Conteúdo:**
  - Separa os termos. Privacidade: "a socially defined ability of an individual (or organization) to determine whether, when, and to whom personal (or organizational) information is to be released". Segurança: técnicas que controlam quem usa ou modifica. Proteção: controle do acesso de programas à informação.
  - O artigo não trata da privacidade em si, mas dos mecanismos que ajudam a alcançá-la.
  - Três categorias de violação: "unauthorized information release", "unauthorized information modification" e "unauthorized denial of use". O intruso pode ser um usuário legítimo.
  - Cinco níveis de proteção: sem proteção, tudo ou nada, compartilhamento controlado, controles programados pelo usuário e "strings on information" (controle depois da liberação).
  - Oito princípios de projeto: economia de mecanismo, padrão seguro na falha, mediação completa, projeto aberto, separação de privilégio, menor privilégio, menor mecanismo comum e aceitabilidade psicológica. Mais dois da segurança física: fator de trabalho e registro de comprometimento.
  - Parte B (bases técnicas): máquina virtual isolada, autenticação e informação compartilhada.

## 1975 · Saltzer e Schroeder, The Protection of Information in Computer Systems (Referências)

- **Autor/órgão:** Jerome H. Saltzer e Michael D. Schroeder (MIT); nota de OCR de Norm Hardy (1997) · **Tipo:** página web (lista de referências do artigo) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-origens/1975-saltzer-schroeder-referencias]] · **Original:** https://web.mit.edu/Saltzer/www/publications/protection/References.html
- **Do que trata:** as cerca de 100 referências do artigo, na ordem da primeira citação.
- **Conteúdo:**
  - Cada referência indica a seção do artigo em que aparece. "SFR" marca as sugestões de leitura adicional.
  - As primeiras, citadas na definição de privacidade, são livros de privacidade: Westin (*Privacy and Freedom*, 1967), Miller (*The Assault on Privacy*, 1971) e o relatório do HEW (*Records, Computers, and the Rights of Citizens*, 1973).
  - Seguem textos de Ware, Anderson e Martin sobre segurança, e manuais de sistemas da época (CTSS, Multics, TENEX, UNIX).
  - O texto vem de OCR. Há erros de digitação visíveis em alguns títulos.

## 1977 · NBS SP 500-19, Audit and Evaluation of Computer Security

- **Autor/órgão:** Zella G. Ruthberg (NBS) e Robert G. McKenzie (GAO), editores; National Bureau of Standards · **Tipo:** relatório técnico (anais de workshop) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-origens/1977-nbs-sp-500-19]] · **Original:** https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nbsspecialpublication500-19.pdf
- **Do que trata:** anais de um workshop (Miami Beach, março de 1977) sobre auditoria e avaliação de segurança de computadores.
- **Conteúdo:**
  - O workshop foi apoiado pelo GAO e fez parte do grupo TG-15 do programa FIPS. Tem 256 páginas, com relatórios de consenso de dez sessões.
  - Partes: normas de auditoria interna, qualificação e treinamento, administração de segurança (com a Privacy Act de 1974 e a lei alemã), ambientes de sistema, controles administrativos e físicos, integridade de programa e de dado, comunicações e ferramentas de auditoria.
  - A Parte III define computer security pelos controles que garantem exatidão e confiabilidade dos dados, proteção dos ativos e economia e eficiência da operação.
  - A Parte VI usa três componentes de auditoria: acesso, exatidão ("accuracy") e disponibilidade. Avalia cada controle com nota de 1 a 10 em cada um.
  - A Parte XI define: "Computer Security —The protection of system data and resources from accidental and deliberate threats to confidentiality, integrity, and availability."
