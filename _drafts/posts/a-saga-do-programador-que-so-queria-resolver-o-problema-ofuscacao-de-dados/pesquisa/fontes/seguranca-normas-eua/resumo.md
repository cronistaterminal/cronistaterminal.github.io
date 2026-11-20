---
title: "Resumo — Normas dos EUA de segurança da informação"
type: resumo-fontes
updated: 2026-11-19
---

# Normas dos EUA de segurança da informação

## 1991 · McCumber, Information Systems Security: A Comprehensive Model

- **Autor/órgão:** Capt. John R. McCumber (Joint Staff); publicado como anexo da NSTISSI nº 4011 · **Tipo:** artigo (anexo de norma) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/1991-mccumber-nstissi-4011]] · **Original:** https://os.ecci.ucr.ac.cr/ci0122/Temas/Semana-02/McCumberAX.pdf
- **Do que trata:** propõe um modelo de segurança da informação independente de tecnologia, em forma de cubo.
- **Conteúdo:**
  - Extraído dos anais da 14ª National Computer Security Conference (out. 1991). Diz que a base é a informação, não a tecnologia.
  - Primeiro eixo: os três estados da informação, com a analogia da água (líquido, gelo, vapor): "transmitted, stored, or processed".
  - Segundo eixo: três características críticas: confidencialidade, integridade e disponibilidade. Chama o conjunto de "the triad of critical information characteristics".
  - Integridade vai além do controle de acesso: "that quality of information that identifies how closely the data represent reality". Disponibilidade é o contrapeso entre segurança e utilidade.
  - Terceiro eixo: medidas de segurança em três camadas: tecnologia; política e prática; educação, treinamento e conscientização.
  - O cubo tem 27 células. Serve para projetar, avaliar e escrever política, e aceita deixar uma vulnerabilidade só "conhecida" se o custo de proteger for maior que a perda.

## 1995 · NIST SP 800-12, The NIST Handbook

- **Autor/órgão:** Barbara Guttman e Edward A. Roback, NIST · **Tipo:** relatório técnico (manual) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/1995-nist-sp-800-12]] · **Original:** https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-12.pdf
- **Do que trata:** manual introdutório de segurança de computadores para quem cuida de sistemas sensíveis no governo federal.
- **Conteúdo:**
  - Arquivado em 2017; substituído pela Revisão 1. Tem 272 páginas e só aconselha, sem fixar requisitos.
  - Define computer security como proteção para preservar "the integrity, availability and confidentiality of information system resources".
  - Divide integridade em integridade de dados e de sistema. Diz que a definição "has been, and continues to be, the subject of much debate".
  - Oito princípios (ex.: segurança apoia a missão, deve ser custo-efetiva, é limitada por fatores sociais) e papéis e ameaças comuns, incluindo ameaças à privacidade.
  - Controles em três partes: gerenciais (política, programa, risco, ciclo de vida, garantia), operacionais (pessoal, contingência, incidentes, treinamento, suporte, segurança física) e técnicos (autenticação, controle de acesso lógico, trilhas de auditoria, criptografia).
  - Fecha com um exemplo de análise de risco num sistema fictício (HGA).

## 2002 · Public Law 107-347 (E-Government Act; Título III = FISMA)

- **Autor/órgão:** Congresso dos EUA · **Tipo:** lei · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/2002-fisma-pl-107-347]] · **Original:** https://www.govinfo.gov/content/pkg/PLAW-107publ347/pdf/PLAW-107publ347.pdf
- **Do que trata:** lei de governo eletrônico; o Título III é a Federal Information Security Management Act (FISMA).
- **Conteúdo:**
  - Cinco títulos: governo eletrônico na OMB, serviços eletrônicos (inclui disposições de privacidade, seção 208), segurança da informação, orçamento e proteção de informação estatística confidencial (CIPSEA).
  - O §3542 define information security: proteger contra "unauthorized access, use, disclosure, disruption, modification, or destruction".
  - Nessa definição, a integridade inclui "nonrepudiation and authenticity" e a confidencialidade inclui "means for protecting personal privacy and proprietary information".
  - O Diretor da OMB supervisiona as políticas das agências e reporta ao Congresso todo ano.
  - Cada agência mantém um programa com avaliação de risco, políticas, treinamento, testes ao menos anuais e plano de correção, sob um responsável sênior de segurança.
  - Prevê avaliação independente anual, centro federal de incidentes e papel do NIST na criação de padrões.

## 2004 · FIPS PUB 199, Standards for Security Categorization

- **Autor/órgão:** NIST, Computer Security Division · **Tipo:** norma (padrão federal) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/2004-fips-199]] · **Original:** https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.199.pdf
- **Do que trata:** padrão para classificar informação e sistemas federais pelo impacto de uma falha de segurança.
- **Conteúdo:**
  - Atende a uma tarefa da FISMA. Não vale para informação classificada nem para sistemas de segurança nacional.
  - Usa os três objetivos da FISMA e define a perda de cada um. Ex.: "A loss of confidentiality is the unauthorized disclosure of information."
  - Três níveis de impacto: baixo (limitado), moderado (sério) e alto (severo ou catastrófico). Nota: dano a indivíduos inclui perda de privacidade.
  - Fórmula: SC = {(confidencialidade, impacto), (integridade, impacto), (disponibilidade, impacto)}. "Não aplicável" só vale para confidencialidade de um tipo de informação.
  - Para o sistema, vale o maior impacto entre os tipos de informação que ele guarda ("high water mark").
  - Cinco exemplos, como informação pública em site e um sistema SCADA de usina.

## 2014 · 44 U.S.C. § 3552, Definitions

- **Autor/órgão:** Congresso dos EUA (US Code, edição 2024, via GPO) · **Tipo:** lei (artigo do código) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/2014-usc-44-3552]] · **Original:** https://www.govinfo.gov/content/pkg/USCODE-2024-title44/html/USCODE-2024-title44-chap35-subchapII-sec3552.htm
- **Do que trata:** definições do subcapítulo de segurança da informação do Título 44, em vigor hoje.
- **Conteúdo:**
  - Incluída pela Pub. L. 113-283 (FISMA 2014). Substitui os antigos §3532 e §3542.
  - Define information security como proteção contra acesso, uso, divulgação, interrupção, modificação ou destruição não autorizados, para garantir integridade (com não repúdio e autenticidade), confidencialidade (com privacidade pessoal) e disponibilidade.
  - Define "incident": algo que ameaça, sem autorização legal, "the integrity, confidentiality, or availability of information or an information system".
  - Define "binding operational directive", sistema de segurança nacional, tecnologia da informação e comunidade de inteligência.

## 2017 · NIST SP 800-12 Rev. 1, An Introduction to Information Security

- **Autor/órgão:** Michael Nieles, Kelley Dempsey e Victoria Yan Pillitteri, NIST · **Tipo:** relatório técnico (manual) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-eua/2017-nist-sp-800-12r1]] · **Original:** https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-12r1.pdf
- **Do que trata:** revisão do manual de 1995, agora chamado de introdução à segurança da informação.
- **Conteúdo:**
  - Tem 101 páginas, baseadas na FISMA 2014. Troca "computer security" por "information security".
  - Usa as definições do glossário CNSSI 4009. Ex.: information security protege contra acesso, uso, divulgação, interrupção, modificação ou destruição não autorizados "in order to ensure confidentiality, integrity, and availability".
  - Atualiza a base legal (FISMA 2002 e 2014, OMB A-130) e lista as publicações ligadas (FIPS 199 e 200, SP 800-30, 800-37, 800-53, 800-60 e outras).
  - Traz oito elementos de segurança, papéis e responsabilidades (do executivo de risco ao usuário) e exemplos de ameaças intencionais e não intencionais.
  - Depois cobre: Risk Management Framework (categorizar, selecionar, implementar, avaliar, autorizar, monitorar), garantia, operações, criptografia e as 20 famílias de controles da SP 800-53.
