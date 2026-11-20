---
title: "Resumo — Normas internacionais de segurança da informação"
type: resumo-fontes
updated: 2026-11-19
---

# Normas internacionais de segurança da informação

## 1991 · ITSEC, Information Technology Security Evaluation Criteria v1.2

- **Autor/órgão:** França, Alemanha, Países Baixos e Reino Unido; publicado pela Comissão das Comunidades Europeias · **Tipo:** norma (critérios de avaliação) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-internacionais/1991-itsec]] · **Original:** https://wiretapped.mirrorservice.org/info/reference/cesg-publications/Information-Technology-Security-Evaluation-Criteria.pdf
- **Do que trata:** critérios comuns europeus para avaliar e certificar a segurança de produtos e sistemas de TI.
- **Conteúdo:**
  - Define segurança de TI por três itens: "confidentiality - prevention of the unauthorised disclosure of information"; integridade (evitar modificação não autorizada); disponibilidade (evitar retenção não autorizada de informação ou recursos).
  - Harmoniza critérios nacionais anteriores (CESG e "Green Book" no Reino Unido, ZSIEC na Alemanha, "Blue-White-Red Book" na França), mantendo compatibilidade com o TCSEC ("Orange Book") dos EUA.
  - O alvo da avaliação (TOE) tem uma "security target" com objetivos, ameaças e funções de segurança.
  - Separa funcionalidade de garantia. Sugere oito categorias de funções (identificação e autenticação, controle de acesso, responsabilização, auditoria, reuso de objeto, exatidão, confiabilidade do serviço, troca de dados) e dez classes de exemplo.
  - A garantia tem duas partes: eficácia (inclui força dos mecanismos: básica, média, alta) e correção (níveis E0 a E6).
  - Capítulos: escopo, funcionalidade, eficácia, correção, resultados da avaliação e glossário.

## 1991 · CCITT/ITU-T X.800, Security Architecture for OSI

- **Autor/órgão:** CCITT (hoje ITU-T), Study Group VII · **Tipo:** norma (recomendação técnica) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-internacionais/1991-itu-x800]] · **Original:** https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-X.800-199103-I!!PDF-E&type=items
- **Do que trata:** arquitetura de segurança para a comunicação entre sistemas abertos (modelo OSI).
- **Conteúdo:**
  - Aprovada em 22/03/1991. Alinhada tecnicamente à ISO 7498-2. Trata só da segurança no caminho da comunicação, não dentro dos sistemas.
  - Glossário com dezenas de termos. Ex.: confidencialidade é "the property that information is not made available or disclosed to unauthorized individuals, entities, or processes"; disponibilidade e integridade de dados também são definidas.
  - Cinco grupos de serviços: autenticação, controle de acesso, confidencialidade de dados (inclui confidencialidade por campo e de fluxo de tráfego), integridade de dados e não repúdio.
  - Mecanismos: cifração, assinatura digital, controle de acesso, integridade de dados, troca de autenticação, preenchimento de tráfego, controle de roteamento e notarização.
  - Mostra em qual das sete camadas OSI cada serviço pode ficar. Inclui gestão de segurança.
  - Anexo A: segurança é "minimizing the vulnerabilities of assets and resources". Cita leis de "data protection" como uma das motivações.

## 1992 · OCDE, Guidelines for the Security of Information Systems

- **Autor/órgão:** Conselho da OCDE (OECD/LEGAL/0271) · **Tipo:** norma (recomendação internacional, não vinculante) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-internacionais/1992-oecd-guidelines-security]] · **Original:** https://legalinstruments.oecd.org/public/doc/329/329.en.pdf
- **Do que trata:** diretrizes para que países-membros protejam sistemas de informação, nos setores público e privado.
- **Conteúdo:**
  - Parte das diretrizes de privacidade da OCDE (1980) e da declaração sobre fluxo transfronteiriço de dados (1985).
  - Define dado, informação, sistema de informação e os três atributos. Ex.: confidencialidade é "the characteristic of data and information being disclosed only to authorised persons, entities and processes at authorised times and in the authorised manner".
  - Objetivo: proteger quem depende dos sistemas contra danos por "failures of availability, confidentiality, and integrity".
  - Nove princípios: responsabilização, conscientização, ética, multidisciplinaridade, proporcionalidade, integração, tempestividade, reavaliação e democracia.
  - Implementação: leis e padrões, educação, meios de reparação, troca de informação e cooperação internacional. Revisão a cada cinco anos.

## 2002 · OCDE, Guidelines for the Security of Information Systems and Networks

- **Autor/órgão:** Conselho da OCDE (OECD/LEGAL/0312) · **Tipo:** norma (recomendação internacional, não vinculante) · **Idioma:** inglês
- **Cópia:** [[posts/a-saga-do-programador-que-so-queria-resolver-o-problema-ofuscacao-de-dados/pesquisa/fontes/seguranca-normas-internacionais/2002-oecd-guidelines-security-networks]] · **Original:** https://legalinstruments.oecd.org/public/doc/116/116.en.pdf
- **Do que trata:** substitui as diretrizes de 1992 e propõe uma "culture of security" para todos os participantes.
- **Conteúdo:**
  - Adotada em 25/07/2002. Base da Resolução 57/239 da ONU. Revogada em 2015 e substituída pela recomendação sobre gestão de risco de segurança digital.
  - Justifica a troca pela internet, pela conexão permanente e pela interdependência entre redes.
  - Nove princípios: conscientização, responsabilidade, resposta, ética, democracia, avaliação de risco, projeto e implementação seguros, gestão de segurança e reavaliação.
  - O princípio da democracia cita a confidencialidade da comunicação e a "appropriate protection of personal information".
  - Não traz definições formais de confidencialidade, integridade e disponibilidade.
