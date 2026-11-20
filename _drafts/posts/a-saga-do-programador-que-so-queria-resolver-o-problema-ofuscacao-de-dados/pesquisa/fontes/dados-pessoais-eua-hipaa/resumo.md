---
title: "Resumo — Dados pessoais nos EUA: HIPAA e PII"
type: resumo-fontes
updated: 2026-11-19
---

# Dados pessoais nos EUA: HIPAA e PII

## 1996 · 42 U.S.C. § 1320d (definições da HIPAA)

- **Autor/órgão:** Congresso dos EUA (US Code, ed. 2023, GPO) · **Tipo:** lei (artigo de definições) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-eua-hipaa/1996-hipaa-42-usc-1320d]] · **Original:** https://www.govinfo.gov/content/pkg/USCODE-2023-title42/html/USCODE-2023-title42-chap7-subchapXI-partC-sec1320d.htm
- **Do que trata:** as definições da parte "Administrative Simplification", criada pela HIPAA (Pub. L. 104-191, de 1996).
- **Conteúdo:**
  - Nove definições:
    - *code set*;
    - *health care clearinghouse* (processadora de dados de saúde);
    - *health care provider* (prestador de saúde);
    - *health information* (informação de saúde);
    - *health plan* (plano de saúde);
    - *individually identifiable health information* (informação de saúde identificável);
    - *standard*;
    - *standard setting organization*;
    - *operating rules*.
  - (4) *Health information*: qualquer informação, oral ou registrada, criada ou recebida por prestador, plano, empregador, escola etc. Ela se relaciona à saúde, à assistência ou ao pagamento da assistência de um indivíduo.
  - (6) *Individually identifiable health information*: inclui dados demográficos. É a informação que "identifies the individual" ou sobre a qual há "a reasonable basis to believe that the information can be used to identify the individual".
  - (5) *Health plan*: lista os tipos (planos coletivos, seguradoras, HMOs, Medicare, Medicaid, programas militares e de veteranos etc.).
  - As notas trazem o histórico de emendas (2001, 2009, 2010) e o propósito do subtítulo.

## 2000 · 45 CFR 160.103 (definições da regra de privacidade)

- **Autor/órgão:** HHS (eCFR, atualizado até 17/11/2026) · **Tipo:** regulamento · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-eua-hipaa/2000-hipaa-45-cfr-160-103]] · **Original:** https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-160/subpart-A/section-160.103
- **Do que trata:** o glossário que vale para todo o subcapítulo C (as regras de privacidade, segurança e transações da HIPAA).
- **Conteúdo:**
  - Lista alfabética com cerca de 50 termos (*disclosure*, *use*, *workforce*, *genetic information*, *reproductive health care* etc.).
  - *Covered entity* (entidade coberta): plano de saúde, *clearinghouse* e prestador que transmite informação de saúde por meio eletrônico.
  - *Business associate* (associado de negócio): quem cria, recebe, guarda ou transmite PHI em nome de uma entidade coberta. Inclui subcontratados. A definição traz exceções.
  - *Individually identifiable health information*: subconjunto da informação de saúde, com dados demográficos, que identifica a pessoa ou permite identificá-la com base razoável.
  - *Protected health information* (PHI): essa informação identificável, em qualquer meio. Ficam fora os registros escolares (FERPA), os registros de emprego e os dados de quem morreu há mais de 50 anos.

## 2000 · 45 CFR 164.514 (desidentificação e outros requisitos)

- **Autor/órgão:** HHS (eCFR, atualizado até 17/11/2026) · **Tipo:** regulamento · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-eua-hipaa/2000-hipaa-45-cfr-164-514]] · **Original:** https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514
- **Do que trata:** requisitos para usar e divulgar PHI. O foco é a desidentificação (*de-identification*).
- **Conteúdo:**
  - (a) Informação que não identifica a pessoa, e sem base razoável para crer que possa identificá-la, não é informação identificável.
  - (b) Dois caminhos:
    - (1) Determinação por especialista: alguém com conhecimento estatístico conclui que o risco é "very small" e documenta o método.
    - (2) *Safe harbor*: remover 18 identificadores (nome, geografia menor que estado, datas exceto o ano, telefone, e-mail, SSN, IP, biometria, foto do rosto etc.) e não ter "actual knowledge" de que o resto identifica.
  - Regra do CEP: mantêm-se os 3 primeiros dígitos se a área tiver mais de 20.000 pessoas. Se não tiver, vira 000. Idades acima de 89 anos são agrupadas.
  - (c) Reidentificação: pode-se usar um código para reidentificar. Mas ele não pode ser derivado de dados da pessoa, nem usado para outro fim, nem ter o mecanismo revelado.
  - (d) "Minimum necessary": limitar acesso, divulgação e pedido de PHI ao mínimo necessário.
  - (e) *Limited data set*: tira 16 identificadores diretos. Só serve para pesquisa, saúde pública ou operações, com acordo de uso de dados (*data use agreement*). Ainda há (f) captação de recursos, (g) subscrição de seguro e (h) verificação de identidade.

## 2010 · NIST SP 800-122 (proteção da confidencialidade de PII)

- **Autor/órgão:** NIST (Erika McCallister, Tim Grance, Karen Scarfone) · **Tipo:** guia · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-eua-hipaa/2010-nist-sp-800-122]] · **Original:** https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-122.pdf
- **Do que trata:** recomendações baseadas em risco para proteger a confidencialidade de PII. O público principal são as agências federais dos EUA.
- **Conteúdo:**
  - Estrutura:
    - Introdução e o que é PII.
    - Níveis de impacto de confidencialidade.
    - Salvaguardas.
    - Resposta a incidentes.
    - Anexos com cenários, FAQ, *Fair Information Practices* e glossário.
  - Definição de PII (versão do GAO a partir de memorandos do OMB): "(1) any information that can be used to distinguish or trace an individual's identity [...]; and (2) any other information that is linked or linkable to an individual".
  - Recomendações:
    - Identificar toda a PII da organização.
    - Minimizar coleta e retenção.
    - Classificar a PII em impacto baixo, moderado ou alto.
    - Aplicar salvaguardas conforme o nível.
    - Ter plano de resposta a incidentes.
  - Fatores de impacto: identificabilidade, quantidade, sensibilidade do campo, contexto de uso, obrigação legal, acesso e localização.
  - 4.2.3: desidentificar é remover ou mascarar PII ("masked or obfuscated") até não haver base razoável para identificar. É possível reidentificar por código ou pseudônimo guardado em outro sistema. Cita o *hash* como técnica comum, com ressalva para a HIPAA.
  - 4.2.4: anonimizar é desidentificar sem código de reidentificação. Técnicas: generalização, supressão, ruído, troca (*swapping*) e substituição pela média. Dado anonimizado é útil para testar sistemas.

## 2012 · HHS/OCR: guia de desidentificação de PHI

- **Autor/órgão:** HHS, Office for Civil Rights (com contribuição de Bradley Malin) · **Tipo:** guia · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/dados-pessoais-eua-hipaa/2012-hhs-deid-guidance]] · **Original:** https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/understanding/coveredentities/De-identification/hhs_deid_guidance.pdf
- **Do que trata:** explica, em perguntas e respostas, os dois métodos da HIPAA para desidentificar: determinação por especialista e *safe harbor*. Foi exigido pela Lei HITECH e se baseia num workshop de 2010.
- **Conteúdo:**
  - Seção 1 (visão geral): PHI, entidades cobertas e o padrão do § 164.514.
  - Seção 2 (especialista):
    - Não há número universal para risco "very small". Depende do destinatário e do contexto.
    - Princípios de risco: replicabilidade, disponibilidade e distinguibilidade.
    - Fluxo iterativo: avaliar, mitigar, reavaliar.
  - Mitigação: supressão, generalização (ex.: CEP de 5 para 3 dígitos, idade em faixas) e perturbação. Cita a k-anonimidade como modelo de proteção.
  - 2.9: um código derivado de PHI (ex.: *hash*) pode estar num conjunto desidentificado, se um especialista aprovar e as chaves não forem reveladas. Não se exige acordo de uso de dados (2.10).
  - Seção 3 (*safe harbor*):
    - Lista os 17 prefixos de CEP de 3 dígitos que viram 000 (Censo 2000).
    - Mostra datas proibidas.
    - Diz o que é "outro identificador único".
    - Define "actual knowledge" com exemplos (ex.: profissão "former president of the State University").
    - Trata de texto livre.
  - Termina com glossário.
