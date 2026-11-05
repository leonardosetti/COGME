---
id: drafts-refac-prompt
title: Considerre aglutinar as seguintes informações
version: '1.0'
class: conhecimento
status: active
owner: agent-project-analyst
derived-from:
- docs/conhecimento/drafts/refac-prompt.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- drafts
- docs
- normalizado
---
# Considerre aglutinar as seguintes informações

Não descartar redação já considerada acima -- vamos enriquecer alguns pontos da redação sugerida:

## PARTE A — Auditoria Crítica: Inconsistências Detectadas e Soluções Ótimas

Auditoria cruzada da Seção 4 v1.0 contra a base documental vigente (TAP v3 congelado, OKB v3.0 + Aditivo, Glossário v3.1, Integração v2.0, Escopo v1.1, Cronograma v1.2, ADRs 001–004). 9 achados, sendo 2 críticos, 4 médios e 3 baixos.

### A.2 — Achados Médios

| #  | Achado                                                                                                                                                                                                      | Localização v1.0 | Conflito                                                         | Solução Ótima                                                                                                                                                                                                                                                  |
| -- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| M1 | **Fase N1.4 ausente nas referências de EAP** — §4.2 e §4.5.2 citam apenas N4.4 (Auditoria de Licenças), mas o TAP §4 inclui N1.4 (Política de Licenciamento FOSS) como fase aderente           | §4.2, §4.5.2     | Incompletude de rastreabilidade EAP                              | Adicionar N1.4 como fonte canônica da política de licenciamento; N4.4 como execução da auditoria                                                                                                                                                              |
| M2 | **Whitelist de licenças incompleta** — §4.5.1 não inclui PSF (Python Software Foundation License), mas a ADR-001 declara Python 3.11 (PSF) como base da stack                                     | §4.5.1            | Stack canônica (ADR-001) usa licença não listada na whitelist | Adicionar PSF e Public Domain (SQLite) à whitelist; referenciar ADR-001 como fonte canônica da stack aprovada                                                                                                                                                   |
| M3 | **Fronteira com Qualidade (Área 5) não delimitada** — §4.5.2 detalha 5 passos do processo de auditoria de licenças, que pode ser reivindicado pelo Plano de Qualidade como controle de qualidade | §4.5.2            | Risco de invasão de escopo entre Áreas 4 e 5                   | Incluir nota de delimitação: Custos governa conformidade FOSS (prevenção de custos); Qualidade governa testes e ferramentas (REQ-08 a REQ-10). Auditoria de licenças é compartilhada, mas whitelist/blacklist e gatilhos de conformidade pertencem a Custos |
| M4 | **Premissa P9 ausente na abertura** — §4.1 cita P2 e P6, mas não P9 (separação ontológica TAP ≠ EAP ≠ PDCA), que fundamenta o regime de freeze                                                | §4.1              | Inconsistência com Cronograma v1.2 (que cita P9 na abertura)    | Adicionar P9 à frase de abertura                                                                                                                                                                                                                                 |

### A.3 — Achados Baixos

| #  | Achado                                                                                                                              | Localização v1.0 | Conflito              | Solução Ótima                                                                                                                |
| -- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------ | --------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| B1 | **FIG-2 (Dashboard) marcada como "opcional"** — status ambíguo; o Glossário §14 diz "SIMPLIFICAR" para Custos             | §4.4, Parte C     | Indecisão documental | Promover de "opcional" para "excluída" com justificativa GMV; GitHub Dependency Graph já fornece a funcionalidade nativamente |
| B2 | **Seção 4.3 lista "Reserva de Gerenciamento"** — redundante com TAP §11, mas não viola nenhuma regra                     | §4.3              | Redundância menor    | Manter (completude formal da linha de base); sem alteração                                                                    |
| B3 | **NC-C2 (fronteira com Escopo N4.4)** — redação atual é funcional mas poderia ser mais precisa sobre a relação com N1.4 | §4.10             | Clareza               | Absorver na nova NC-C1 (delimitação de áreas)                                                                                |

### A.4 — Auditoria de Invasão de Escopo entre Áreas (implacável)

| Conteúdo                                        | Tentação de inclusão         | Decisão                                                          | Justificativa                            |
| ------------------------------------------------ | ------------------------------- | ----------------------------------------------------------------- | ---------------------------------------- |
| Critérios de aceite de testes (coverage ≥ 80%) | Duplicar como métrica de custo | **Excluído**                                               | Pertence ao Plano de Qualidade (Área 5) |
| DoR/DoD detalhado                                | Replicar gates                  | **Excluído** — apenas referenciado                        | Pertence ao Escopo §2.6                 |
| EVM (SPI/CPI/VAC)                                | Incluir como métrica           | **Excluído** — declarado LEGADO                           | Integração §1.6.2; ADR-003            |
| Auditoria de licenças (procedimento)            | Detalhar checklist              | **Parcial** — governança aqui (§4.5), execução em N4.4 | Fronteira delimitada na nova NC-C1       |
| RACI de auditoria                                | Incluir matriz                  | **Excluído**                                               | Pertence ao Plano de Recursos (M2)       |
| Curva S / Histograma de custos                   | Incluir gráficos               | **Excluído**                                               | Inaplicável (orçamento zero)           |

**Nenhuma inconsistência residual bloqueante após aplicação das soluções. Procedo à redação integral v1.1.**

---

## PARTE B — Redação Integral Revisada (v1.1)

**Canonicidade e regime de freeze:** O TAP encontra-se em regime de freeze desde o início do planejamento (última versão: 18/09/2026); não é objeto de revisão ao longo do ciclo, em conformidade com seu status ontológico (Premissa P9; Glossário §11; PMBOK® 6ª §4.1, dicionário). Divergências de leitura são tratadas exclusivamente como Notas de Contexto neste plano (§4.10).

**Trade-off declarado:** Abre-se mão da formalidade de estimativa/orçamento em favor de auditoria contínua de conformidade FOSS, alinhado ao Princípio "Foco em Valor" (PMBOK 7ª) e à Restrição TAP §11.

## 4.2 Abordagem de Gerenciamento de Custos

O gerenciamento de custos do COGME opera em três camadas de prevenção:

| Camada               | Objeto                           | Mecanismo de Controle                                       | Fonte Canônica   |
| -------------------- | -------------------------------- | ----------------------------------------------------------- | ----------------- |
| **Preventiva** | Seleção de stack e ferramentas | ADR-001 + Fase N4.1 (Seleção e Validação da Stack FOSS) | ADR-001; EAP N4.1 |
| **Normativa**  | Política de licenciamento       | Whitelist/blacklist de licenças (§4.5.1)                  | EAP N1.4          |
| **Detectiva**  | Auditoria de licenças           | Fase N4.4 (Auditoria de Licenças) + checklist OSI-approved | EAP N4.4          |

**Regra de ouro:** Nenhuma ferramenta, biblioteca, API ou serviço pode ser incorporado ao projeto sem: (1) verificação de licença OSI-approved (whitelist §4.5.1); (2) confirmação de plano gratuito suficiente para o MVP acadêmico; (3) registro na ADR-001 ou em ADR específica (se mudança de stack).

## 4.4 Estratégias de Medição e Controle

Dada a inaplicabilidade de EVM (ADR-003; Integração §1.6.2), o controle de custos opera por **métricas de conformidade**:

| Métrica                             | Fórmula/Definição                                        | Meta               | Frequência     | Responsável            |
| ------------------------------------ | ----------------------------------------------------------- | ------------------ | --------------- | ----------------------- |
| **% Dependências Auditadas**  | (Dependências com licença verificada / Total) × 100      | 100%               | Por commit (CI) | Pipeline GitHub Actions |
| **Desvios de Licenciamento**   | Nº de dependências com licença não-OSI ou incompatível | 0                  | Contínuo       | GP                      |
| **Custo Financeiro Acumulado** | Soma de todos os gastos realizados                          | R$ 0,00            | Semanal         | GP (self-report)        |
| **Alternativas FOSS Mapeadas** | Nº de ferramentas críticas com ≥1 alternativa FOSS       | ≥2 por ferramenta | M2              | Equipe                  |

**Gatilhos de ação corretiva:**

- `% Dependências Auditadas` < 100% → bloqueio de merge até auditoria concluída
- `Desvios de Licenciamento` > 0 → remoção imediata + `change-request`
- `Custo Financeiro Acumulado` > R$ 0,00 → reembolso imediato + lição aprendida

## 4.7 Premissas e Restrições Aplicáveis

**Premissas:** P2 (FOSS absoluto) — fundamenta §4.5; P6 (hardware adequado) — fundamenta §4.3 (sem cloud paga); P9 (separação ontológica) — fundamenta o regime de freeze (§4.10); PA-C1 (Free Tier sustentável) — APIs e serviços gratuitos permanecem disponíveis.

**Restrições:** TAP §8 (orçamento nulo; proibição de aquisições pagas) — fundamenta §4.3; TAP §11 (linha de base R$ 0,00) — fundamenta §4.1 e §4.4; TAP §3 (Inovação FOSS) — fundamenta §4.5.

## 4.8 Condições de Fracasso e Escalation

Derivadas do TAP §3.3, com distinção entre gatilhos de alerta preventivo (internos) e condições formais de fracasso (TAP):

| Tipo                        | Gatilho                                     | Limiar         | Ação                                        | Base         |
| --------------------------- | ------------------------------------------- | -------------- | --------------------------------------------- | ------------ |
| **Alerta preventivo** | Dependências não-OSI detectadas           | > 5%           | Auditoria emergencial + substituição ≤ 48h | GP (interno) |
| **Fracasso formal**   | Dependências incompatíveis com FOSS       | > 30%          | Condição de não sucesso do projeto         | TAP §3.3.e  |
| **Alerta preventivo** | Custo financeiro > R$ 0,00                  | Qualquer valor | Reembolso imediato + lição aprendida        | GP (interno) |
| **Alerta preventivo** | Dependência crítica sem alternativa FOSS  | 1 ocorrência  | Redução de escopo + ADR ≤ 72h              | GP + CCB     |
| **Fracasso formal**   | Falha na auditoria em 2 marcos consecutivos | 2 marcos       | Revisão de processo + treinamento            | GP           |

**Nota de reconciliação (NC-C2):** O limiar de 5% é um gatilho de alerta preventivo interno, mais restritivo que a condição formal de fracasso do TAP §3.3.e (30%). A intenção é detectar desvios precocemente, permitindo ação corretiva antes que o limiar formal seja atingido. Trade-off: maior rigor operacional em troca de margem de segurança.

## 4.9 Declaração de Rastreabilidade

| Seção                  | Origem no TAP                           | Domínio PMBOK 7ª           | Processo PMBOK 6ª      |
| ------------------------ | --------------------------------------- | ---------------------------- | ----------------------- |
| 4.1 (Propósito; freeze) | §11 + §8 + Premissa P9                | Planejamento + Entrega       | 7.1                     |
| 4.2 (Abordagem)          | §3 (Inovação) + §8 + EAP N1.4, N4.1 | Abordagem de Desenvolvimento | 7.1                     |
| 4.3 (Linha de Base)      | §11 (Orçamento Zero)                  | Planejamento                 | 7.3                     |
| 4.4 (Métricas)          | §3 (Métricas) + §11 + ADR-003        | Medição                    | 7.4 (substituição)    |
| 4.5 (Conformidade FOSS)  | §3 (Inovação) + §8 + ADR-001        | Entrega                      | 8.3 (controle aplicado) |
| 4.6 (Mudanças)          | §3.3 + §10 + Integração §1.7       | Incerteza                    | 4.6 + 7.4               |
| 4.8 (Fracasso)           | §3.3.e (30%) + §3.2.b                 | Incerteza + Entrega          | 7.4                     |

**Verificação:** 100% das seções possuem rastreabilidade a ao menos uma premissa, restrição ou objetivo SMART do TAP.
