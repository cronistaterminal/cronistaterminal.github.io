---
title: "Resumo — Anonimização de dados"
type: resumo-fontes
updated: 2026-11-19
---

# Anonimização de dados

## 2000 · Sweeney: dados demográficos simples identificam pessoas

- **Autor/órgão:** Latanya Sweeney (Carnegie Mellon University, Data Privacy Working Paper 3) · **Tipo:** artigo (working paper) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-anonimizacao/2000-sweeney-simple-demographics]] · **Original:** https://dataprivacylab.org/projects/identifiability/paper1.pdf
- **Do que trata:** mede, com dados resumidos do Censo de 1990 dos EUA, quantas pessoas têm combinações únicas de poucos dados demográficos.
- **Conteúdo:**
  - Resultado principal: 87% da população (216 de 248 milhões) é "likely" única por {CEP de 5 dígitos, gênero, data de nascimento}. Com cidade no lugar do CEP, são 53%. Com condado, 18%.
  - Ao trocar data de nascimento por mês e ano, cai para 3,7%. Só com o ano, 0,04%. Com faixa de 2 anos de idade, 0,01%.
  - Demonstração de ligação (*linking*): por 20 dólares, comprou a lista de eleitores de Cambridge (MA). Ela tem nome, endereço, CEP, nascimento e gênero. Com isso, mostra como cruzá-la com dados hospitalares "sem identificadores".
  - Exemplos de Illinois: CEPs com pouquíssimas pessoas de um perfil. Exemplo: só duas mulheres negras numa cidade.
  - Método: trata cada combinação de atributos como "quase-identificador". Conta as combinações possíveis contra a população de cada área, usando o princípio da casa dos pombos (*pigeonhole*). Os experimentos vão de B a L, por estado e para o país todo.
  - Discussão: valores raros dentro do próprio conjunto (diagnóstico, profissão, idade fora do padrão) também identificam. Exemplo: o único paciente com mais de 45 anos num hospital pediátrico.

## 2006 · Golle: revisitando a unicidade dos dados demográficos

- **Autor/órgão:** Philippe Golle (Palo Alto Research Center), WPES '06 (ACM) · **Tipo:** artigo · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-anonimizacao/2006-golle-uniqueness-demographics]] · **Original:** https://crypto.stanford.edu/~pgolle/papers/census.pdf
- **Do que trata:** refaz o estudo de Sweeney com o Censo de 2000 e mede o grau de anonimato, não só a unicidade.
- **Conteúdo:**
  - Dados: tabela PCT12 (sexo por idade) do Censo 2000, para 3.219 condados e 33.233 áreas de CEP (ZCTAs). Supõe nascimentos distribuídos por igual nos dias do ano.
  - Resultado: 63,3% são únicos por {gênero, CEP, data de nascimento} em 2000 e 61% em 1990. Sweeney tinha achado 87%. Com condado, 14,8%.
  - Não explica a diferença com certeza, por falta de detalhes do método de Sweeney. Levanta uma hipótese: o Censo de 1990 não tabula dados por CEP com idade fina.
  - Mede o anonimato em escala até *k-anonymous*. Exemplo: com condado, 43,6% da população fica num grupo de 5 pessoas ou menos.
  - O risco é quase uniforme dos 0 aos 50 anos e sobe rápido depois dos 50. Acima de 60, 63% ficam em grupos de 5 ou menos (por condado).
  - Com só o ano de nascimento, a unicidade cai para 0,2% (CEP). Com ano e mês, para 4,2%.

## 2014 · Grupo do Artigo 29: Parecer 05/2014 sobre técnicas de anonimização (WP216)

- **Autor/órgão:** Grupo de Trabalho do Artigo 29 (órgão consultivo europeu de proteção de dados) · **Tipo:** parecer · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-anonimizacao/2014-art29-wp216-anonimizacao]] · **Original:** https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2014/wp216_en.pdf
- **Do que trata:** analisa a eficácia e os limites das técnicas de anonimização à luz da Diretiva 95/46/CE.
- **Conteúdo:**
  - Base legal: o Considerando 26 exclui o dado anônimo da proteção e manda considerar "all the means likely reasonably to be used" pelo controlador ou por terceiros. A anonimização deve ser irreversível e é ela mesma um tratamento posterior.
  - Três riscos medem uma técnica:
    - Singularização (*singling out*): isolar o registro de alguém.
    - Ligação (*linkability*): ligar registros da mesma pessoa.
    - Inferência: deduzir um atributo a partir de outros.
  - Técnicas analisadas, com garantias, erros comuns e falhas:
    - Randomização: ruído, permutação, privacidade diferencial.
    - Generalização: agregação, k-anonimidade, l-diversidade, t-proximidade.
    - Casos citados: AOL e Netflix.
  - Seção 4: pseudonimização "is not a method of anonymisation", apenas reduz a ligação. Tipos:
    - Criptografia com chave.
    - *Hash* simples: força bruta e tabelas pré-calculadas revertem.
    - *Hash* com sal: ainda pode ser revertido "with reasonable means".
    - *Hash* com chave secreta.
    - Criptografia determinística ou *hash* com chave apagada.
    - Tokenização: comum no setor financeiro, para números de cartão.
  - Tabela 6: nenhuma técnica elimina com certeza os três riscos. Pseudonimização e *hash*/tokenização deixam singularização e ligação.
  - Recomendações: decidir caso a caso, combinar técnicas, definir contexto e finalidade, e reavaliar o risco residual com frequência. O anexo é uma introdução técnica à randomização e à generalização.

## 2023 · ANPD: estudo preliminar sobre anonimização e pseudonimização

- **Autor/órgão:** ANPD (Autoridade Nacional de Proteção de Dados) · **Tipo:** guia (estudo preliminar, v1.0, dez. 2023) · **Idioma:** pt-br
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-anonimizacao/2023-anpd-estudo-anonimizacao]] · **Original:** https://www.gov.br/anpd/pt-br/assuntos/regulacao/agenda-regulatoria-1/cp-estudo-preliminar_anonimizacao_e_pseudon.pdf/@@display-file/file
- **Do que trata:** orienta agentes de tratamento sobre anonimização e pseudonimização na LGPD. Tem base no art. 12, § 3º.
- **Conteúdo:**
  - Estrutura:
    - Conceitos e glossário.
    - Aspectos jurídicos.
    - Processo de anonimização.
    - Processo de pseudonimização.
    - Considerações finais.
    - Quatro apêndices: esclarecimentos, caderno de técnicas, métricas de risco e estudos de caso.
  - Identificador direto identifica sozinho (ex.: nome completo, CPF). O indireto, ou "quase-identificador", identifica em combinação (ex.: CEP, idade, raça, IP). Cita os 87% de Sweeney.
  - "A anonimização não reduz a probabilidade de reidentificação de um conjunto de dados a zero". "Esforços razoáveis" (art. 12) é conceito jurídico indeterminado: pesa custo, tempo, tecnologia e meios próprios. Cita nota técnica sobre os microdados do INEP.
  - Processo baseado em risco, em 4 etapas:
    1. Definir o Risco de Reidentificação Aceitável (RRA).
    2. Aplicar as técnicas.
    3. Medir o Risco de Reidentificação Mensurado (RRM), com "métrica contextual" (k-anonimização, l-diversidade, t-proximidade).
    4. Comparar: se o RRM for maior que o RRA, recomeçar.
  - Pseudonimização: troca de identificadores por pseudônimo, com informação adicional guardada à parte. Proteção limitada, distinta da anonimização. Útil para *privacy by design*, compartilhamento e minimização.
  - Caderno de técnicas, com exemplos em tabela (inclusive CPF mascarado `***.222.222-**`):
    - Ruído, generalização, mascaramento, permutação, supressão.
    - Desfoque gaussiano, pixelização, substituição por contador.
    - Função *hash*, encriptação.
  - Três estudos de caso: localização agregada de celulares, dados clínicos para pesquisa e dados educacionais.
