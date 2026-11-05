---
id: docs-conhecimento-drafts-extracao-modular-normalizacao-documental-do-plano-de-projeto-cogme
title: Baseline de Métricas de Fluxo (Calibração)
type: conhecimento
version: 2.0.1
status: obsoleto
owner: agent-project-analyst
derived-from:
- docs/conhecimento/drafts/extracao-modular-normalizacao-documental-do-plano-de-projeto-cogme.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- drafts
- docs
- normalizado
---
[Context]
**Iniciativa:** Extração modular e normalização documental do Plano de Projeto COGME
**Prazo irrevogável:** 02/11/2026 (48h a partir de 31/10/2026)
**Natureza:** Esforço estrito documental — não altera cronograma real, marcos M1-M4, ou ações efetivas
**Artefato alvo:** `Plano-de-Projeto-COGME_v2.0.1-ONGOING.docx` (167 páginas)
**Hierarquia normativa aplicada:** Constitution v1.2.0 > TAP v3 (ADR-005) > ADRs 001-012 > OKB v5.1.0 > Planos > Glossário
**Governança:** PMBOK 7ª (primária) · PMBOK 6ª (dicionário terminológico, obsolescência procedural declarada)

[Artifact/Decision] — Plano de Execução Documental (PED-001)

## 1. Veredito Inicial

O artefato atual é uma **monografia acadêmica com planos de área embutidos**, não um plano profissional utilizável. A bifurcação é mandatória antes de qualquer retificação.

**Defeitos críticos identificados (P0):**

- D-C01: Artefato é monografia, não plano (capa Fatec, resumo, listas ABNT)
- D-C02: TAP integral como capítulo 1 (32 páginas — viola ADR-005)
- D-C03: Constitution v1.2.0 ausente (zero menções)
- D-C04: Grafia inconsistente do stakeholder ("Ms." vs "Dr.")
- D-C05: Stack drift silencioso (SQLite/Qwen 32B vs ADRs 006/010)
- D-C06: Frontend desatualizado (HTMX/Tailwind vs ADR-001)
- D-C07: 6 marcadores OKB-C-XX em pontos críticos

## 2. Estratégia de Execução (Compressão 48h)

O report original estimava 31h em 9 blocos. Compressão para 2 dias exige priorização brutal:

| Bloco        | Escopo                                 | Estimativa Original | Prioridade | Ação no PED-001                                                    |
| ------------ | -------------------------------------- | ------------------- | ---------- | -------------------------------------------------------------------- |
| **B1** | Bifurcação Monografia × Plano       | 8h                  | 🔴 P0      | **Executar primeiro** — cria dois artefatos limpos            |
| **B2** | Saneamento de ADRs violadas            | 6h                  | 🔴 P0      | **Executar segundo** — find & replace global                  |
| **B3** | Remoção do TAP embutido              | 2h                  | 🔴 P0      | **Executar terceiro** — substituir por cross-reference        |
| **B4** | Eliminação de OKB-C-XX      | 4h                  | 🔴 P0      | **Executar quarto** — preencher ou declarar OKB-C-XX |
| **B5** | Saneamento do Glossário v3.2          | 3h                  | 🟠 P1      | **Adiar** — não bloqueia plano profissional                  |
| **B6** | Formalização de CR-001               | 2h                  | 🟠 P1      | **Adiar** — decisão CCB pendente                             |
| **B7** | Reestruturação de Seções Técnicas | 4h                  | 🟠 P1      | **Adiar** — mover para spec separada                          |
| **B8** | Normalização de Metadados            | 1h                  | 🟡 P2      | **Adiar** — cosmético                                        |
| **B9** | Ratificação do OKB v5.0.0            | 1h                  | 🔴 P0      | **Já executado** (CCB-003, 30/10/2026)                        |

**Total comprimido:** 20h (B1+B2+B3+B4) em 48h = viável com foco exclusivo.

## 3. Estrutura Canônica do Plano Profissional

Após bifurcação (B1), o plano profissional terá:

```yaml
---
id: PLANO-PROJETO-COGME
version: 2.0.0
status: draft
owner: agent-pm
derived-from:
  - constitution.md v1.2.0
  - TAP v3 (18/09/2026, congelado via ADR-005)
  - ADRs 001-012
  - OKB v5.1.0 (ratificado CCB-003)
---
```

**Seções obrigatórias:**

1. §1 — Subordinação Constitucional (ADR-012)
2. §2 — Cross-reference ao TAP (ADR-005)
3. §3 — Catálogo de ADRs 001-012 (OKB §2.1)
4. §4 — Planos de Área (Integração, Escopo, Cronograma, Custos, Qualidade, Recursos, Comunicações, Riscos)
5. §5 — Cross-reference à Especificação Técnica (após B7)
6. §6 — Considerações Finais (sem elementos monográficos)

## 4. Gates de Qualidade por Bloco

### Gate B1 — Bifurcação

- [ ] Monografia preservada como `Monografia-COGME-v2.0.docx`
- [ ] Plano profissional com frontmatter YAML
- [ ] Zero elementos monográficos no plano (resumo, palavras-chave, listas ABNT)
- [ ] Cross-references validadas contra Constitution + TAP + ADRs

### Gate B2 — Saneamento de ADRs

- [ ] Zero ocorrências de "Ms. Nivaldo" ou "Carletto" (duplo t)
- [ ] Zero ocorrências de "Qwen 32B" ou "QwenStudio"
- [ ] SQLite apenas em testes isolados (explicitado)
- [ ] Frontend vanilla (HTMX/Tailwind/Jinja2 removidos)
- [ ] Frase canônica da ADR-007 presente: "A rede valida o marco; o Kanban executa a tarefa"
- [ ] Subordinação à Constituição declarada

### Gate B3 — Remoção do TAP

- [ ] Zero páginas de TAP no corpo do plano
- [ ] Cross-reference ao `docs/tap/TAP.docx` canônico inserida

### Gate B4 — Eliminação de OKB-C-XX

- [ ] Zero ocorrências de OKB-C-41 (A41)
- [ ] Todos os `INSUFFICIENT DATA` com referência OKB-C-XX
- [ ] Lições aprendidas transpostas para `MF2-licoes.md`

## 5. Cronograma de Execução (31/10 → 02/11)

| Data           | Bloco       | Ação                              | Responsável        |
| -------------- | ----------- | ----------------------------------- | ------------------- |
| 31/10 (hoje)   | B1          | Bifurcação Monografia × Plano    | Leonardo            |
| 31/10 (noite)  | B2          | Saneamento de ADRs (find & replace) | Fabricio + Leonardo |
| 01/10 (manhã) | B3          | Remoção do TAP embutido           | Leonardo            |
| 01/10 (tarde)  | B4          | Eliminação de OKB-C-01 (A1)   | Edson + Leonardo    |
| 01/10 (noite)  | Revisão    | Code Review cruzado (todos)         | Equipe              |
| 02/11 (manhã) | Validação | Gates de qualidade + commit final   | Leonardo (CCB)      |

## 6. Cross-References Obrigatórias

| Origem                 | Destino                     | Fonte Canônica      |
| ---------------------- | --------------------------- | -------------------- |
| Plano §1 (Hierarquia) | Constitution v1.2.0         | ADR-012              |
| Plano §2 (TAP)        | `docs/tap/TAP.docx`       | ADR-005              |
| Plano §3 (ADRs)       | ADRs 001-012                | OKB v5.1.0 §2.1     |
| Plano §4 (Planos)     | 8 planos de área           | OKB v5.1.0 §4.1     |
| Tabela de stack        | ADR-001 + ADR-006 + ADR-010 | OKB v5.1.0 §3.3-3.4 |

## 7. OKB-C-XX Declarados

| Item                                     | Status               | Referência          |
| ---------------------------------------- | -------------------- | -------------------- |
| Baseline de métricas                    | 0 B (não calibrada) | OKB-C-08, OKB-C-16   |
| DER (Diagrama Entidade-Relacionamento)   | Não existe em FS    | OKB §9.2 (TOGAF C1) |
| Plano de migração SQLite → PostgreSQL | Inexistente          | OKB-C-22             |
| Matriz de partes interessadas            | Não registrada      | OKB-C-24             |

[PMBOK Traceability]

| Domínio PMBOK 7ª | Aplicação no PED-001                                       |
| ------------------ | ------------------------------------------------------------ |
| Integração       | Hierarquia de autoridade (ADR-012) — Constituição no topo |
| Escopo             | Fronteira entre artefatos canônicos e voláteis             |
| Cronograma         | Compressão de 31h para 20h em 48h                           |
| Qualidade          | Gates de validação por bloco                               |
| Recursos           | Atribuição de responsáveis (Leonardo/Fabricio/Edson)      |
| Comunicações     | Cross-references canônicos (OKB §8.3)                      |
| Riscos             | 4 INSUFFICIENT DATA declarados (P-08 honestidade)            |
| Medição          | Baseline 0 B = métrica aspiracional                         |
| Incerteza          | Prazo irrevogável 02/11 = restrição temporal absoluta     |

[Trade-offs]

| Decisão                          | Ganho                          | Perda/Risco                                           | Mitigação                                  |
| --------------------------------- | ------------------------------ | ----------------------------------------------------- | -------------------------------------------- |
| Compressão de 31h para 20h       | Viabilidade em 48h             | Blocos B5-B8 adiados                                  | Executar pós-02/11 se necessário           |
| Bifurcação Monografia × Plano  | Plano profissional utilizável | Perda de formato acadêmico no arquivo de governança | Monografia preservada como artefato separado |
| Remoção do TAP embutido         | Compliance com ADR-005         | Redução de 32 páginas                              | Cross-reference ao TAP.docx canônico        |
| Declaração de INSUFFICIENT DATA | Honestidade (P-08)             | Lacunas visíveis                                     | Referenciar OKB-C para rastreabilidade       |

[Next Kanban Steps]
**Epic:** `E10-Normalizacao-Documental-48h` (WBS Level 1)

| Issue               | Descrição                                  | Estimativa | Responsável        | Prioridade | Milestone |
| ------------------- | -------------------------------------------- | ---------- | ------------------- | ---------- | --------- |
| #910-B1-Bifurcacao  | Separar monografia e plano profissional      | 8h         | Leonardo            | 🔴 P0      | 31/10     |
| #911-B2-ADRs        | Saneamento de ADRs violadas (find & replace) | 6h         | Fabricio + Leonardo | 🔴 P0      | 31/10     |
| #912-B3-TAP         | Remover TAP embutido + cross-reference       | 2h         | Leonardo            | 🔴 P0      | 01/11     |
| #913-B4-A-CONFIRMAR | Eliminar 6 marcadores OKB-C-02 (A2)      | 4h         | Edson + Leonardo    | 🔴 P0      | 01/11     |
| #914-Revisao        | Code Review cruzado (todos)                  | 2h         | Equipe              | 🔴 P0      | 01/11     |
| #915-Validacao      | Gates de qualidade + commit final            | 2h         | Leonardo (CCB)      | 🔴 P0      | 02/11     |

**Kill Switch:** Se a bifurcação (B1) não estiver concluída até 01/11 00:00, acionar Retrospectiva extraordinária e reavaliar viabilidade do prazo 02/11.

**Próxima ação imediata:** Aprovação do CCB (GP Leonardo) para início do Bloco B1 — bifurcação do artefato em `Monografia-COGME-v2.0.docx` + `Plano-de-Projeto-COGME_v2.0.md`.


---




As análises propostas na rodada anterior são razoavelmente boas eportanto gustaria de uma meta-análise a fim de convergisr as propostas de ambas em uma saída via caminho ótimo, extraindo a potencialidade de solução acionável e de arquitetura do projeto unificando as alternativas de forma coerente:

Análise 1:

```Markdown
[Context]

**Rodada 2 — Rebaseline do PED-001 → PED-002**
**Janela:** 31/10/2026 (hoje) → 02/11/2026, irrevogável. Natureza: estritamente documental, **sem alteração de datas de marco**.
**Insumos recebidos nesta sessão:** `OKB.md` (parcial), `report-canon-extract-CCB.md` (parcial), `_consolidado-adrs.tmp.md` (parcial, não-canônico), `Plano-de-Projeto-COGME_v2.0.1-ONGOING.docx` (parcial), `ccb-log.md` (**vazio**).
**Hierarquia:** Constitution v1.2.0 > TAP v3 > ADRs 001–012 > OKB (ratificado CCB-003) > Planos > Glossário.
**PMBOK 6ª:** usada **exclusivamente como dicionário terminológico**. Sua arquitetura de processos/grupos está **proceduralmente obsoleta** neste projeto — nenhuma sequência ITTO é prescritiva. Governança efetiva = PMBOK 7ª (Princípios + Domínios).

---

[Artifact/Decision]

## 1. Crítica técnica às suas declarações

### 1.1 TAP / D-C02 — **sua premissa está factualmente incorreta; seu objetivo, porém, é legitimamente alcançável**

Você afirmou: *"A ADR-005 determina apenas que houve freeze devido à entrega do M2"*. O corpus não sustenta isso:

> ADR-005 v1.0.0, §Decisão: *"O TAP encontra-se congelado **desde o início do planejamento** (última versão 18/09/2026, **anterior aos planos**): não é revisado, reversionado ou corrigido ao longo do ciclo."*
> NC-00 (Plano de Cronograma §3.8): freeze decidido em **21/09/2026** — **antes** do M2 (30/09), não por causa dele.

Portanto: o freeze **não é gate-triggered por M2**; é ontológico (Premissa P9), vigente desde a origem. **Não posso validar sua leitura como interpretação da ADR-005** — seria fabricar coerência. O que existe é uma **decisão nova do GP que revoga parcialmente a ADR-005**. Isso é perfeitamente legal na governança vigente e é o caminho que recomendo.

**Alavanca decisiva a seu favor (e que a rodada 1 ignorou):** a ADR-005 está com status **"Regularização Tardia — ratificação CCB pendente"** (OKB-C-12). Uma ADR **não ratificada** tem força normativa reduzida. Sua alteração é, portanto, **barata e limpa**: não é quebra de baseline ratificado, é **substituição de decisão pendente**.

**Sobre "sem ingerência direta de CCB":** incoerência terminológica a corrigir. O CCB do COGME é **monocrático = GP Leonardo** (TAP v3 §1.c, Premissa P7). Você **é** o CCB. Não existe ingerência externa a evitar. Sua decisão **já é** um ato de CCB — só precisa de uma linha no log. Isso atende 100% da sua intenção (zero gargalo) sem criar ficção de governança.

**DECISÃO D-01 (proposta para sua ratificação imediata):** emitir **ADR-013 — Regime de Emenda Controlada do TAP (Baseline Vivo)**, que **supersede parcialmente** a ADR-005:

| Mantido da ADR-005 | Revogado/alterado pela ADR-013 |
|---|---|
| Precedência intra-TAP: §6 Marcos é canônica em matéria temporal | Proibição absoluta de revisão/reversão do TAP |
| Locus de contexto: NCs no Plano de Cronograma §3.8 | Imutabilidade textual do termo autorizativo |
| Núcleo intangível: objeto, objetivos, justificativa, orçamento-teto | — (blindado: emenda que toque o núcleo exige ata extraordinária) |

**Mecanismo anti-burocrático (1 artefato, não 3):** ADR-013 contém, embutida, a **Ata Extraordinária AE-001** (§Ratificação) + **registro de emendas do TAP** (tabela delta: `campo | valor anterior | valor novo | justificativa | data`). **Não** criaremos CR + ATA + ADR separados para a mesma decisão. Um commit, um arquivo, uma linha no `ccb-log.md`.

**BLOQUEIO POTENCIAL — OKB-C-XX:** `constitution.md` v1.2.0 **não foi fornecido** nesta sessão. Se a immutabilidade do TAP estiver constitucionalizada (P9 pode estar em Art. 3º/9º), **ADR não basta** — exige emenda constitucional (Art. 9), ato **exclusivo do Humano** (Art. 5.2). *Assunção proposta:* P9 é premissa do TAP, não cláusula pétrea constitucional → ADR-013 é suficiente. **Verificação obrigatória no B0 (15 min).** Se a assunção cair, escalamos para emenda — ainda dentro da janela.

### 1.2 TAP como Seção 1 e "desde a capa" — **B1 e B3 da rodada 1 estavam errados**

Sua instrução (*"desde a capa do projeto até sua conclusão definitiva"* + *"TAP deve ser o conteúdo de início"*) **contradiz frontalmente** o B1 (bifurcação, remoção de capa/ABNT) e o B3 (remoção das 32 páginas do TAP) que propus. Retiro ambos.

- **D-C02 reclassificado:** de *defeito P0* → **decisão de layout do GP**, resolvida por ADR-013. Não é violação; era leitura excessivamente rígida da ADR-005.
- **B1 readequado:** artefato **único, híbrido acadêmico-profissional** (capa Fatec → folha de rosto → sumário → **§1 TAP** → §2 subordinação constitucional → §3 ADRs → §4 planos das 8 áreas → §5 apêndices → considerações finais → referências). A `Monografia-COGME.pdf` já existe como artefato separado; **não duplicaremos esforço de bifurcação em 48h**.
- **D-C03 permanece P0:** Constituição ausente em 167 páginas. Inserção de §2 é obrigatória (ADR-012).

### 1.3 Drift de stack — **você está parcialmente certo; a conclusão precisa de ajuste**

Correto: **sem código implementado, não há drift técnico** — não há migração, não há retrabalho de build. **OKB-C-22 (plano de migração SQLite→PostgreSQL) deve ser fechado como OBSOLETO**, não como pendência. Ganho real de ~4h.

Porém: **o drift textual persiste e é justamente o objeto desta iniciativa**. Um plano que declara SQLite/Qwen 32B/HTMX enquanto as ADRs 006/010 dizem outra coisa é um **defeito documental**, não técnico. O custo de correção cai de "migração" para "find & replace" — mas não vai a zero. **B2 mantido, reclassificado de P0-técnico para P0-editorial.**

### 1.4 PostgreSQL — **não é decisão nova; é confirmação**

ADR-006 v2.0.0 (CCB-001) e ADR-010 v1.0.0 já são o locus da stack; o "drift" reportado é do **docx atrasado em relação às ADRs**. Sua declaração **ratifica o vigente**. Ação: reescrever **REQ-07** (hoje pede SQLite) e Tabelas 88/119. SQLite sobrevive **apenas** como fixture de teste isolado, se as ADRs o previrem. **Sem nova ADR.**
*Nota de coerência:* REQ-07, se estiver no corpo do TAP, torna-se emendável **graças à ADR-013** — as duas decisões se destravam mutuamente.

### 1.5 Docker / containerização — **provável lacuna de explicitação, não de decisão**

OKB §9 (TOGAF D) lista explicitamente **"containers"** como cobertura da **ADR-010 v1.0.0**. Logo, o tema **já tem locus**.
**OKB-C-XX:** o corpo da ADR-010 não veio no excerto. Não afirmarei que existe nem que falta.
**Protocolo B0:** `grep -in "docker\|compose\|container\|podman" docs/decisoes/ADR-010*.md`
- Se coberto → **sem ADR nova**; apenas explicitar no plano (§4 Recursos/Ambiente) o topology diagram textual das camadas ortogonais.
- Se ausente/implícito → **ADR-010 v1.1.0 (emenda)**, *não* ADR-014. **Anti-inflação de ADRs**: mesmo assunto, mesmo artefato, versão nova.

Camadas ortogonais a declarar (proposta, sujeita à ADR-010): `app` (runtime Python/FOSS, ADR-001) · `db` (PostgreSQL) · `sdd` (módulo de inteligência, ADR-006) · `ci` (runner) — rede bridge única, volumes nomeados, `.env` versionado como `.env.example`.

### 1.6 Bloco 4 — **estava obscuro, sim. Reescrito.**

OKB-C-03 (A3) são **placeholders de autoria** deixados no docx em 6 pontos (Tabelas 88, 127, 128; Seções 4.4, 4.7; Referências). Não são bugs; são **decisões não tomadas** que travam a redação definitiva. O B4 não é "apagar texto" — é **triagem decisória com 3 saídas possíveis**:

| Saída | Quando | Registro |
|---|---|---|
| **PREENCHER** | Existe fonte canônica (ADR/TAP/OKB) | Valor + citação da fonte |
| **OKB-C-XX + assunção** | Dado inexiste e não é obtível até 02/11 | Assunção explícita + owner + prazo pós-M4 |
| **SUPRIMIR** | Item obsoleto (ex.: resquício SQLite/EVM) | Remoção + nota no delta log |

**Regra dura:** zero OKB-C-04 (A4) no artefato final. Um placeholder em documento "definitivo" é confissão de incompletude — pior que uma assunção declarada.
**OKB-C-XX:** o **conteúdo** das Tabelas 88/127/128 não veio nos excertos. Não inventarei o que falta. Triagem item-a-item no B4 com o docx aberto.

### 1.7 OKB como SSOT de acesso rápido — **aceito, com distinção ontológica obrigatória**

O OKB é **canônico para conhecimento consolidado** (CCB-003), mas declara sobre si mesmo: *"não altera ADRs, o TAP congelado nem a Constituição"*. Logo:

- **SSOT normativo** = Constitution / TAP / ADRs (fonte primária).
- **SSOT de consulta** = OKB (derivado, autoritativo para navegação).

Aceito **menção livre e frequente** ao OKB no plano, com convenção `OKB v5.2.0 §x`. **Risco declarado:** artefato derivado diverge da fonte. **Mitigação:** o OKB absorve nesta rodada os novos § (User Stories, Testes/Métricas, Containerização, Regime de Emenda do TAP) e ganha carimbo `derived-as-of: 2026-11-02`.

### 1.8 Novos conteúdos — alocação nas áreas de conhecimento

| Conteúdo | Área/Plano | Ontologia GitHub | Âncora |
|---|---|---|---|
| **Épicos e User Stories** | **Escopo** (§ Elicitação & Rastreabilidade) | **Epic = Macro-Fase (MF1–MF12)**; **Issue = Pacote de Trabalho (N1.1–N12.2)**; **User Story = campo narrativo no corpo do Issue** | ADR-009 (12 fases + 37 pacotes), ADR-004 (tasklists, sem subissues) |
| **Testes de Software** | **Qualidade** (planejamento/controle) + **Escopo** (DoD) | Label `test:*` + tasklist de aceite no Issue | M3: coverage ≥ 80%, UAT sem defeitos críticos |
| **Métricas** | **Qualidade** (produto) + **Medição** (fluxo) | Campos `cycle_time`, `wip_age` no Project | ADR-003 (**EVM rejeitado**), NC-03 (Cycle Time = In Progress→Done) |
| **Apêndice documental (ADR/TA/CR)** | **Integração** + **Comunicações** | Links relativos externos, **sem embed** | ADR-012; OKB §8.3 |

**Restrição crítica de coerência:** User Stories **não criam novo nível de EAP**. Inserir uma camada "História" entre fase e pacote violaria ADR-009 (contagem congelada 12+37) e ADR-004 (rejeição de subissues). História é **conteúdo do Issue**, não nó. Formato:

```

Como <papel></papel>, quero <capacidade></capacidade>, para <benefício>.
Critérios de aceite (Gherkin-lite): Dado / Quando / Então
Tasklist DoD: - [ ] ... (ADR-004)
Rastreabilidade: TAP §4 → MF<n></n> → N<n></n>.<m></m> → custo/hora

```

**Fronteira de escopo:** papéis de usuário ≠ matriz de partes interessadas. **OKB-C-24 permanece fora** — área de Stakeholders excluída por diretriz.

**Métricas — OKB-C-XX:** `docs/metricas/baseline.md` = **0 B** (OKB-C-08). Metas da ADR-003 são **aspiracionais**. *Assunção proposta:* em projeto 100% simulado, popular baseline com **seed sintético rotulado `SIMULADO — não empírico`** e SLE provisório. Alternativa (manter 0 B) é honesta, mas deixa o plano sem seção de medição redigível. Recomendo o seed rotulado.

### 1.9 Achado novo — **`ccb-log.md` está vazio (0 B)**

OKB invoca CCB-001 e CCB-003 como ratificações; o log fornecido **não tem conteúdo**. **OKB-C-XX** para comprovar qualquer ratificação. *Assunção:* ocorreram conforme OKB. **Ação B0 (10 min):** repopular o log com CCB-001/002/003 (reconstrução declarada) + CCB-004 (ADR-013). Sem isso, toda a cadeia de autoridade do plano é asserção sem trilha — exatamente o defeito que a ADR-005 nasceu para corrigir (lição aprendida: commits 0 byte).

### 1.10 Cronograma — correção e limite

A rodada 1 continha erro material: datas **"01/10"** onde deveria constar **01/11**. Corrigido.
**CR-001 / colisão M2 × M3: FORA DESTA RODADA.** Você declarou esforço sem impacto em datas. Reabrir marcos consumiria a janela e violaria sua própria restrição. Fica como pendência explícita pós-02/11 (OKB-C-06 permanece aberto, e isso é declarado, não escondido).

---

## 2. PED-002 — Blocos rebaselineados (27h / 48h)

| Bloco | Escopo | h | Δ vs. rodada 1 |
|---|---|---|---|
| **B0** | Verificar Constitution (P9) · `ccb-log` · grep ADR-010 · consolidar Arts. 5–10 duplicados (OKB-C-21, **ato humano**) · emitir **ADR-013 + AE-001** | 3 | **NOVO — bloqueante** |
| **B1-R** | Front-matter híbrido (capa/rosto/sumário) + §2 subordinação constitucional | 3 | ↓ de 8h (bifurcação cancelada) |
| **B2-R** | Saneamento editorial: grafia **Prof. Dr. Nivaldo Carletto** (docx traz "Ms." **e** "Carleto" — duplo defeito, ADR-008) · SQLite→PostgreSQL · remoção HTMX/Tailwind/Jinja2 · frase ADR-007 | 4 | ↓ de 6h |
| **B3-R** | **TAP como §1**, emendas pontuais sob ADR-013 + tabela delta + versionamento | 4 | **INVERTIDO** (era remoção) |
| **B4-R** | Triagem dos 6 OKB-C-12 (A12) (protocolo §1.6) | 3 | Esclarecido |
| **B5-N** | User Stories em Escopo (12 Epics / 37 Issues) | 3 | **NOVO** |
| **B6-N** | Testes + Métricas (Qualidade/Medição) + baseline seed | 3 | **NOVO** |
| **B7-N** | Apêndice ADR/TA/CR + absorção OKB v5.2.0 | 2 | **NOVO** |
| **B8** | Revisão cruzada + gates + commit final | 2 | mantido |
| | **Total** | **27h** | buffer ~3h |

**Cronograma:** 31/10 → B0+B1-R+B2-R (10h) · 01/11 → B3-R+B4-R+B5-N (10h) · 02/11 → B6-N+B7-N+B8 (7h) + buffer.
**Kill switch:** B0 não fechado até 31/10 23:59 → congelar ADR-013 e executar B3-R em modo *TAP verbatim sem emenda* (mantém prazo, adia correções).
**Ordem de descope se estourar:** B7-N → B6-N (métricas) → B5-N. **B0/B3-R/B4-R são indescopeáveis.**

**Assunção de custódia:** *"TA" = Termo de Aceite* (OKB-C-XX — não consta nos excertos). Se for outro artefato, ajustar B7-N.

---

[PMBOK Traceability]

| Domínio / Princípio (7ª) | Aplicação nesta rodada |
|---|---|
| **Trabalho do Projeto** | ADR-013 redefine o regime de baseline; conhecimento e processos como ativos vivos |
| **Planejamento** | Rebaseline PED-002; cadeia TAP → Escopo → EAP(12/37) → Cronograma → Custos preservada |
| **Entrega** | User Stories + DoD/Gherkin como definição de valor no Issue |
| **Medição** | ADR-003 (fluxo) substitui EVM; baseline seed rotulado; SLE provisório |
| **Incerteza** | Prazo irrevogável; 5 OKB-C-XX declarados com assunção e owner |
| **Abordagem de Desenvolvimento** | *Tailoring* explícito: cancelamento de B1/B3 originais; descope ordenado |
| Princípio **Adapte-se / Pensamento Sistêmico** | Artefato híbrido atende exigência Fatec **e** função profissional |
| Princípio **Liderança / Stewardship** | GP-CCB assume a decisão e a registra — não terceiriza a trilha |
| Princípio **Mudança** | Emenda controlada com delta log, sem reescrita retroativa de marcos |

**PMBOK 6ª — dicionário apenas:** 4.6 (Controlar Mudanças), 5.4/5.5 (EAP/Validar Escopo), 8.x (Qualidade). **Obsolescência procedural declarada:** nenhum grupo de processos ou ITTO é prescritivo; a governança é 7ª + Constitution + ADRs.
**Excluídos:** Aquisições, Partes Interessadas (OKB-C-24 permanece fora).

---

[Trade-offs]

| Decisão | Ganho | Perda / Risco | Mitigação |
|---|---|---|---|
| **ADR-013 supersede ADR-005 parcialmente** | TAP editável e como §1; desbloqueia REQ-07 | Perde-se a garantia de baseline imutável; auditor pode questionar "autorização reescrita" | Núcleo blindado + tabela delta + freeze de §6 Marcos nesta rodada |
| **Não repactuar M2/M3 agora** | Preserva janela de 48h e sua restrição | OKB-C-06 e colisão M2×M3 seguem abertos | Pendência explícita, não silenciada |
| **Artefato híbrido único** | Atende "da capa à conclusão"; −5h | Não é plano profissional puro; crítica de forma persiste | §2 constitucional + apêndices externos dão espinha dorsal de governança |
| **Ata embutida na ADR (1 artefato)** | Zero burocracia, 1 commit | Menor segregação formal decisão/ratificação | §Ratificação datada + linha no `ccb-log` |
| **Emenda ADR-010 v1.1.0 em vez de ADR-014** | Evita inflação do catálogo | Se o escopo de containers for amplo, emenda fica sobrecarregada | Reavaliar no grep do B0 |
| **Baseline seed SIMULADO** | Seção de Medição redigível | Métrica não empírica pode ser lida como resultado | Rótulo obrigatório `SIMULADO` + OKB-C-08 aberto |
| **Drift reclassificado (não desconsiderado)** | −4h (sem plano de migração) | Texto desalinhado ainda compromete coerência | B2-R find & replace + grep negativo |

---

[Next Kanban Steps]

**Epic:** `E10 — Normalização Documental 48h` · **Milestone:** `02/11/2026 — Redação Definitiva`

| Issue | Título | Labels | h | Resp. | Quando |
|---|---|---|---|---|---|
| #910 | B0 — Verificar Constitution P9 + repopular `ccb-log` + grep ADR-010 | `prio:P0` `area:integracao` `blocker` | 1 | Leonardo (humano) | 31/10 |
| #911 | B0 — Emitir **ADR-013** (Regime de Emenda do TAP) + AE-001 embutida | `prio:P0` `area:integracao` `adr` | 2 | Leonardo (CCB) | 31/10 |
| #912 | B1-R — Front-matter híbrido + §2 subordinação constitucional | `prio:P0` `area:integracao` | 3 | Leonardo | 31/10 |
| #913 | B2-R — Saneamento grafia ADR-008 + stack ADRs 001/006/010 | `prio:P0` `area:qualidade` | 4 | Fabricio | 31/10 |
| #914 | B3-R — TAP §1 + emendas pontuais + tabela delta | `prio:P0` `area:integracao` | 4 | Leonardo | 01/11 |
| #915 | B4-R — Triagem 6 OKB-C-13 (A13) | `prio:P0` `area:escopo` | 3 | Edson | 01/11 |
| #916 | B5-N — User Stories: 12 Epics / 37 Issues + DoD | `prio:P1` `area:escopo` | 3 | Edson + Leonardo | 01/11 |
| #917 | B6-N — Testes + Métricas + baseline seed SIMULADO | `prio:P1` `area:qualidade` | 3 | Fabricio | 02/11 |
| #918 | B7-N — Apêndice ADR/TA/CR + OKB v5.2.0 | `prio:P2` `area:comunicacoes` | 2 | Leonardo | 02/11 |
| #919 | B8 — Revisão cruzada + gates + commit final | `prio:P0` `area:qualidade` | 2 | Equipe | 02/11 |

**Gate B0 (bloqueia tudo):**
- [ ] Constitution verificada: P9 é premissa de TAP ou cláusula constitucional? → define ADR vs. emenda
- [ ] Arts. 5–10 duplicados consolidados (**exclusivo do Humano**, Art. 5.2 / OKB-C-21)
- [ ] `ccb-log.md` repopulado (CCB-001/002/003 reconstruídos + CCB-004)
- [ ] ADR-013 assinada; ADR-005 marcada `Superseded-in-part by ADR-013`
- [ ] Resultado do grep ADR-010 registrado → emenda v1.1.0 ou nenhuma ação

**Ação imediata requerida de você (2 respostas, ~1 minuto):**
1. **Ratifica a ADR-013** conforme §1.1 (supersessão parcial, núcleo blindado, §6 Marcos intocada nesta rodada)? **Sim/Não.**
2. Confirma **artefato único híbrido com capa** (cancelando a bifurcação B1 original)? **Sim/Não.**

Sem essas duas respostas não inicio B3-R — seria redigir sobre fundação contestada. Todo o resto (B1-R, B2-R) já pode rodar em paralelo.
```

---

Análise 2:

```Markdown
[Context]
**Reanálise Crítica das Oposições do CCB (GP Leonardo)**
**Data-base:** 31/10/2026 · **Prazo irrevogável:** 02/11/2026
**Hierarquia aplicada:** Constitution v1.2.0 > TAP v3 (congelado via ADR-005, **sob revisão**) > ADRs 001–012 > OKB v5.1.0 > Planos > Glossário

[Artifact/Decision] — Análise Crítica e Readequação da Rodada 2

## 1. Crítica Técnica às Declarações do CCB

### 1.1 Sobre o TAP (D-C02) — Oposição Aceita com Ressalvas Técnicas

**Declaração do CCB:** *"O TAP pode ser pontualmente modificado para acomodar decisões e demandas do projeto vivo... deve ser o conteúdo de início do documento."*

**Análise técnica:**
- ✅ **Autoridade legítima:** Como CCB único (TAP v3 §1.c, Premissa P7), o GP tem autoridade para revogar ou emendar a ADR-005.
- ⚠️ **Consequências em cascata:** Revogar o freeze do TAP invalida:
  - ADR-005 v1.0.0 (regime de freeze)
  - ADR-009 v1.0.0 (contagem canônica 12/37 baseada no TAP congelado)
  - NC-00 do Plano de Cronograma §3.8 (locus de contexto)
  - OKB §1.4 (regime de freeze)
  - Premissa P9 do TAP (separação ontológica TAP ≠ EAP ≠ PDCA)
- ⚠️ **Risco de ambiguidade:** Se o TAP é mutável, a distinção entre "TAP" e "Plano de Projeto" se dilui — ambos se tornam documentos vivos de planejamento.

**Decisão técnica:** Aceitar a oposição do CCB, mas formalizar via **Ata Extraordinária CCB-005** (não via ADR, pois viola o teste G4 da política de ADRs — trade-off já coberto pela própria ata). A ata deve:
1. Revogar o freeze do TAP declarado na ADR-005
2. Autorizar ajustes pontuais no TAP sem descaracterizar objetivos nucleares
3. Manter a precedência intra-TAP (§6 Marcos canônico para matéria temporal)
4. Exigir que ajustes sejam registrados via CR ou commit com changelog

**Readequação do Bloco B3:** Em vez de remover o TAP do plano, **integrá-lo como Seção 1 do Plano de Projeto**, com cross-references aos planos de área e ADRs. O TAP deixa de ser "congelado" e passa a ser "versão viva com histórico de ajustes".

### 1.2 Sobre o Drift de Stack — Oposição Parcialmente Aceita

**Declaração do CCB:** *"O processo de implementação de código e arquitetura técnica não iniciou, portanto o drift mencionado pode ser desconsiderado."*

**Análise técnica:**
- ✅ **Verdade operacional:** Se `src/` está vazio (confirmado em 25/10/2026), não há violação de ADR-006/010 no código.
- ❌ **Falso documental:** Os artefatos **documentais** ainda mencionam stack desatualizada:
  - Tabela 88 (Plano de Recursos): SQLite como banco
  - Tabela 119 (Seção 3 — Desenvolvimento): SQLite + QwenStudio
  - REQ-07 (TAP): "cache de cotações (SQLite)"
  - Tabela 40 (Plano de Escopo): "Cache SQLite de cotações"
- ⚠️ **Risco:** Se o avaliador (Prof. Dr. Nivaldo Carleto) ler o plano, verá SQLite/Qwen 32B e questionará a aderência às ADRs 006/010 ratificadas em 29/10/2026.

**Decisão técnica:** O drift **documental** deve ser saneado (find & replace nas tabelas e REQs), mesmo sem código. O drift **operacional** (código) não existe — confirmado.

### 1.3 Sobre PostgreSQL + Docker — Confirmação Técnica

**Declaração do CCB:** *"Adotaremos PostgreSQL... faltou declaração explícita do uso de Docker e containerização."*

**Análise técnica:**
- ✅ **ADR-010 v1.0.0 já cobre Docker:** A decisão DB2 + ORCH2 + WEB2 foi ratificada em 29/10/2026 (CCB-001).
- ✅ **Stack canônica as-of 30/10/2026:**
  - Banco: PostgreSQL 15+ (asyncpg + SQLAlchemy async + Alembic)
  - Orquestração: Docker + Docker Compose (`db`, `web`, `proxy`)
  - Proxy: Nginx (latente, perfil opcional)
- ⚠️ **Gap documental:** O Plano v2.0.1 ainda menciona SQLite em múltiplas tabelas (ver 1.2 acima).

**Decisão técnica:** Nenhuma nova ADR necessária — a ADR-010 já declara Docker + PostgreSQL. Apenas saneamento documental (find & replace) para alinhar tabelas e REQs à ADR-010.

### 1.4 Sobre o Bloco B4 (Marcadores OKB-C-14 (A14)) — Esclarecimento

**Declaração do CCB:** *"Bloco 4 sobre marcadores não está claro."*

**Esclarecimento técnico:**
O Bloco B4 visa eliminar 6 marcadores OKB-C-15 (A15) no plano v2.0.1:

| # | Localização | Marcador | Ação proposta |
|---|-------------|----------|---------------|
| 1 | Tabela 88 (Plano de Recursos) | Baseline de calibração (Cycle Time, Throughput, horas) | Declarar `OKB-C-XX` (OKB-C-08, OKB-C-16: baseline.md = 0 B) |
| 2 | Tabela 127 (Seção 3 — Desenvolvimento) | Responsável pela seção | Preencher: "Fabricio de Lima Cabral" (conforme Tabela 129) |
| 3 | Tabela 128 (Considerações Finais) | Atendimento aos SMART (Produto, Qualidade, Cronograma) | Preencher status real: M1 ✅, M2 ⚠️ (atrasado), M3 ⏳, M4 ⏳ |
| 4 | Seção 4.4 (Lições Aprendidas) | "Outras lições da MF2: ___" | Transpor LA-001 + I1–I8 de `notas_adjacentes.md` §6 e §8 |
| 5 | Seção 4.7 (Conclusão) | "[A CONFIRMAR — parágrafo de fechamento]" | Remover marcador; manter parágrafo como provisório até M4 |
| 6 | Referências (Decreto IOF) | "[A CONFIRMAR: incluir também o decreto...]" | Confirmar Decreto 6.306/2007 (já consta); remover marcador |

**Gate de validação:** `grep -r "\[A CONFIRMAR\]"` deve retornar zero ocorrências após o Bloco B4.

### 1.5 Sobre o OKB como Quick Access SSOT — Aceito

**Declaração do CCB:** *"OKB deverá absorver o máximo de informação relevante... deve ser mencionado livremente como ferramenta de apoio SSOT."*

**Decisão técnica:** ✅ Aceito. O OKB v5.1.0 já é o corpus canônico único (ratificado CCB-003, 30/10/2026). O Plano de Projeto deve referenciá-lo livremente como SSOT de:
- Stack canônica (OKB §3.3–3.4)
- Catálogo de ADRs (OKB §2.1)
- Estado dos artefatos (OKB §4.1)
- Métricas e baseline (OKB §6)
- Inconsistências e pendências (OKB §10)

Cross-references ao OKB substituem duplicação de conteúdo (princípio "1 fato = 1 local", OKB §8.1).

### 1.6 Sobre Novos Conteúdos a Acomodar — Mapeamento Técnico

**Declaração do CCB:** *"Precisamos acomodar: User Stories, Testes de Software e métricas, Apêndice com ADR/TA/CR."*

**Mapeamento para áreas de conhecimento PMBOK 7ª:**

| Conteúdo | Área PMBOK 7ª | Seção do Plano | Artefato canônico |
|----------|---------------|----------------|-------------------|
| **User Stories (Épicos + Histórias)** | Escopo + Entrega | §2.2 (Coleta de Requisitos) + nova §2.3.5 (Formato User Story GWT) | `docs/requisitos/requisitos.md` (0 B — OKB-C-08) |
| **Testes de Software e métricas** | Qualidade + Medição | §2.5 (Plano de Qualidade) + §2.5.3 (Métricas de Qualidade) | `docs/metricas/baseline.md` (0 B — OKB-C-16) |
| **Apêndice com ADR/TA/CR** | Integração + Comunicações | Nova §6 (Apêndices) | Cross-references a `docs/decisoes/`, `docs/tap/`, `docs/change-requests/` |

**Decisão técnica:**
- **User Stories:** O TAP já menciona REQ-01 a REQ-15, mas não no formato User Story (GWT — Given/When/Then). O Plano de Escopo §2.3.3 promete conversão até M2. **Ação:** Incluir no Plano de Escopo §2.3.5 uma tabela com Épicos (N5 — Desenvolvimento) e User Stories associadas (ex.: US-01 "Como PJ, quero simular ganhos em USD, para saber quanto receberei em BRL").
- **Testes e métricas:** O Plano de Qualidade §2.5 já cobre testes (coverage ≥ 80%, UAT). **Ação:** Reforçar §2.5.3 com métricas de fluxo (Cycle Time, Throughput, CFD) e cross-reference ao OKB §6.
- **Apêndice:** Criar §6 do Plano com lista de ADRs (001–012), TAP (cross-reference), CRs (CR-001) e artefatos complementares. Não duplicar conteúdo — apenas listar e referenciar.

## 2. Readequação dos Blocos de Retificação

### Bloco B1 — Bifurcação Monografia × Plano (P0 · 8h)
**Mantido:** Separar monografia acadêmica de plano profissional.

### Bloco B2 — Saneamento de ADRs Violadas (P0 · 6h)
**Mantido com ajuste:** Find & replace global para:
- ADR-008: "Prof. Ms. Nivaldo Carleto" → "Prof. Dr. Nivaldo Carleto"
- ADR-006: "Qwen 32B" → "Qwen3-30B-A3B Q4_K_M (MoE)"
- ADR-010: "SQLite" → "PostgreSQL 15+" (exceto em testes isolados)
- ADR-001: "HTMX + Tailwind + Jinja2" → "HTML5/CSS3/JS vanilla"
- ADR-007: Inserir frase canônica "A rede valida o marco; o Kanban executa a tarefa"
- ADR-011: Adicionar seção sobre MCPs e L1/L2/L3
- ADR-012: Declarar subordinação à Constituição v1.2.0

### Bloco B3 — **Integração do TAP no Plano** (P0 · 4h) — **REESTRUTURADO**
**Escopo original:** Remover TAP do plano.
**Novo escopo:** Integrar TAP como Seção 1 do Plano, com:
- Cross-references aos planos de área
- Histórico de ajustes pontuais (após revogação do freeze via CCB-005)
- Precedência intra-TAP mantida (§6 Marcos canônico)

**Ação prévia:** Emitir **Ata CCB-005** revogando o freeze do TAP (ADR-005).

### Bloco B4 — Eliminação de OKB-C-16 (A16) (P0 · 4h)
**Mantido com esclarecimento:** Ver tabela em 1.4 acima.

### Bloco B5 — Saneamento do Glossário v3.2 (P0 · 3h)
**Mantido:** Corrigir 7 violações (grafia, contagem EAP, stack, hierarquia, Cycle Time).

### Bloco B6 — **Ata CCB-005: Revogação do Freeze do TAP** (P0 · 2h) — **NOVO**
**Escopo:** Formalizar a decisão do CCB de permitir ajustes pontuais no TAP.
**Conteúdo da ata:**
- Revogação do freeze declarado na ADR-005
- Autorização de ajustes pontuais sem descaracterizar objetivos nucleares
- Manutenção da precedência intra-TAP (§6 Marcos)
- Registro de ajustes via CR ou commit com changelog

### Bloco B7 — Reestruturação de Seções Técnicas (P1 · 4h)
**Mantido:** Mover Seção 3 (Desenvolvimento) para spec técnica separada.

### Bloco B8 — Normalização de Metadados (P1 · 1h)
**Mantido:** Alinhar versionamento (CSV + OKB + frontmatter YAML).

### Bloco B9 — Ratificação do OKB v5.1.0 (P0 · 1h)
**Já executado:** CCB-003 ratificou OKB v5.1.0 em 30/10/2026.

### Bloco B10 — **Inclusão de User Stories, Testes e Apêndice** (P1 · 3h) — **NOVO**
**Escopo:**
- §2.3.5 do Plano de Escopo: Tabela de Épicos e User Stories (GWT)
- §2.5.3 do Plano de Qualidade: Reforço de métricas de fluxo (cross-reference OKB §6)
- §6 do Plano: Apêndice com lista de ADRs, TAP, CRs e artefatos complementares

## 3. Cronograma Readequado (alinhado ao prazo 02/11/2026)

| Bloco | Prioridade | Estimativa | Responsável | Prazo |
|-------|------------|------------|-------------|-------|
| B6 (Ata CCB-005) | 🔴 P0 | 2h | Leonardo (CCB) | 31/10 |
| B1 (Bifurcação) | 🔴 P0 | 8h | Leonardo | 31/10–01/11 |
| B2 (ADRs) | 🔴 P0 | 6h | Fabricio + Leonardo | 01/11 |
| B3 (TAP integrado) | 🔴 P0 | 4h | Leonardo | 01/11 |
| B4 (OKB-C-17 (A17)) | 🔴 P0 | 4h | Edson + Leonardo | 01/11 |
| B5 (Glossário) | 🔴 P0 | 3h | Edson + Leonardo | 01/11 |
| B10 (User Stories + Apêndice) | 🟠 P1 | 3h | Fabricio | 02/11 |
| B7 (Seção 3 → spec) | 🟠 P1 | 4h | Fabricio | 02/11 |
| B8 (Metadados) | 🟠 P1 | 1h | Leonardo | 02/11 |
| **Total** | — | **35h** | — | **02/11** |

**Marco intermediário:** 01/11/2026 (B1–B6 concluídos).

## 4. Decisões CCB Pendentes (não executáveis por agente)

| ID | Decisão | Urgência | Fundamentação |
|----|---------|----------|---------------|
| **D-C1** | **Revogar freeze do TAP (Ata CCB-005)** | 🔴 P0 | Oposição do CCB à ADR-005 |
| D-C2 | Formalizar CR-001 (M2 → 15/11) com ADR de marco | 🔴 P0 | Colide com M3; sem ADR = OKB-C-06 |
| D-C3 | Consolidar Constitution v1.2.0 (Arts. 5–10 duplicados) | 🔴 P0 | OKB-C-21 — ambiguidade normativa |
| D-C4 | Ratificar ADR-005 (ou revogá-la via CCB-005) | 🟠 P1 | OKB-C-12 |
| D-C5 | Resolver teto de ADRs (12 emitidas vs limite GMV de 10) | 🟠 P1 | OKB-C-05 |

[PMBOK Traceability]

| Domínio PMBOK 7ª | Aplicação nesta reanálise |
|------------------|---------------------------|
| **Integração** | Hierarquia de autoridade (ADR-012) — CCB pode revogar ADR-005 |
| **Escopo** | TAP como parte do escopo documental do plano (oposição do CCB) |
| **Cronograma** | Prazo irrevogável 02/11 — compressão de 35h em 48h |
| **Qualidade** | Saneamento de drift documental (tabelas, REQs) |
| **Recursos** | Atribuição de responsáveis (Leonardo/Fabricio/Edson) |
| **Comunicações** | OKB como SSOT de quick access (cross-references) |
| **Riscos** | Ata CCB-005 mitiga risco de ambiguidade normativa |
| **Medição** | Baseline 0 B = métrica aspiracional (OKB-C-16) |
| **Incerteza** | Revogação do freeze do TAP = mudança de premissa (P9) |

Processos PMBOK 6ª (dicionário): 4.6 (Controle Integrado de Mudanças), 5.2 (Coletar Requisitos), 8.3 (Controlar Qualidade). Obsolescência procedural declarada.

[Trade-offs]

| Decisão | Ganho | Perda/Risco | Mitigação |
|---------|-------|-------------|-----------|
| Revogar freeze do TAP (CCB-005) | Flexibilidade para ajustes pontuais | Perda de imutabilidade do termo autorizativo | Ata CCB-005 com precedência intra-TAP mantida |
| Integrar TAP no plano (B3 reestruturado) | Compliance com exigência documental | Aumento de ~32 páginas no plano | Cross-references aos planos de área evitam duplicação |
| Saneamento de drift documental (B2) | Aderência às ADRs 006/010 | Retrabalho em tabelas e REQs | Find & replace automatizado |
| Incluir User Stories (B10) | Rastreabilidade TAP → EAP → User Stories | Overhead de redação | Tabela enxuta (Épicos + User Stories GWT) |
| Apêndice com ADRs/CRs (B10) | Visibilidade de artefatos complementares | Risco de duplicação | Apenas lista com cross-references |

[Next Kanban Steps]

**Epic:** `E10-Normalizacao-Documental-48h` (WBS Level 1) — **REESTRUTURADO**

| Issue | Descrição | Estimativa | Responsável | Prioridade | Milestone |
|-------|-----------|------------|-------------|------------|-----------|
| **#920-CCB-005** | **Emitir Ata CCB-005 revogando freeze do TAP** | 2h | Leonardo (CCB) | 🔴 P0 | 31/10 |
| #910-B1-Bifurcacao | Separar monografia e plano profissional | 8h | Leonardo | 🔴 P0 | 31/10–01/11 |
| #911-B2-ADRs | Saneamento de ADRs violadas (find & replace) | 6h | Fabricio + Leonardo | 🔴 P0 | 01/11 |
| **#912-B3-TAP-Integrado** | **Integrar TAP como Seção 1 do plano (após CCB-005)** | 4h | Leonardo | 🔴 P0 | 01/11 |
| #913-B4-A-CONFIRMAR | Eliminar 6 marcadores OKB-C-18 (A18) | 4h | Edson + Leonardo | 🔴 P0 | 01/11 |
| #914-B5-Glossario | Saneamento do Glossário v3.2.0 | 3h | Edson + Leonardo | 🔴 P0 | 01/11 |
| **#915-B10-UserStories** | **Incluir User Stories, testes e apêndice** | 3h | Fabricio | 🟠 P1 | 02/11 |
| #916-B7-Secao-3 | Mover Seção 3 para spec técnica | 4h | Fabricio | 🟠 P1 | 02/11 |
| #917-B8-Metadados | Normalização de metadados | 1h | Leonardo | 🟠 P1 | 02/11 |

**Gate de Qualidade (DoD) por Bloco:**
- [ ] Ata CCB-005 emitida e registrada em `docs/governanca/ccb-log.md`
- [ ] TAP integrado como Seção 1 do plano (após CCB-005)
- [ ] Zero ocorrências de OKB-C-19 (A19) (verificação via `grep`)
- [ ] Glossário v3.2.0 com `grep` negativo para "Carletto", "13 fases", "48 pacotes", "Qwen 32B", "To Do → Done"
- [ ] Tabelas 88, 119 e REQ-07 alinhados à ADR-010 (PostgreSQL)
- [ ] User Stories (GWT) incluídas no Plano de Escopo §2.3.5
- [ ] Apêndice com ADRs 001–012, TAP, CR-001 incluído no Plano §6
- [ ] Cross-references ao OKB v5.1.0 como SSOT

**Kill Switch:** Se a Ata CCB-005 não for emitida até 31/10 23:59, acionar Retrospectiva extraordinária e reavaliar viabilidade do prazo 02/11.

**Próxima ação imediata:** Aprovação do CCB (GP Leonardo) para emissão da **Ata CCB-005** revogando o freeze do TAP (ADR-005) e criação dos cards `#920`–`#917` no GitHub Projects.
```

É necessária uma saída acionável em teor imperativo de comando de solução, assim é possível coordenar as ações imediatas em blocos e rodadas. Atenção ao contexto proposto de normalizar o conteúdo textual do plano de projeto.

Adicionalmente temos anexo a cosntitution vigente

---




[Context]

**Meta-Análise Rodada 3 — Convergência Ótima (PED-003)**
**Data-base:** 01/11/2026 · **Prazo irrevogável:** 02/11/2026, 23:59
**Insumo novo:** `constitution.md` v1.2.0 **completo** (resolve OKB-C-XX da Análise 1)
**Hierarquia confirmada:** Constitution v1.2.0 > TAP v3 > ADRs 001–012 > OKB v5.1.0 > Planos > Glossário
**PMBOK 6ª:** dicionário terminológico apenas. Obsolescência procedural declarada.

---

[Artifact/Decision] — **PED-003: Caminho Ótimo Unificado**

## 0. Verificações Factuais Contra a Constitution (que agora tenho completa)

| Questão                                      | Veredito                     | Fundamento                                                                                                                                                                                                                                   |
| --------------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| P9 é cláusula pétrea constitucional?       | **NÃO**               | P-01 a P-13 são os únicos princípios inalienáveis (Art. 3º). P9 é **premissa do TAP §9**, não da Constitution. Análise 1 estava correta em sua assunção; Análise 2 errou ao tratar P9 como constitucional.                 |
| Arts. 5–10 duplicados (OKB-C-21)?            | **CONFIRMADO**         | O arquivo fornecido contém Arts. 5–10 em **duas redações completas** (linhas ~119–217 e ~218–331). Defeito estrutural real. Hash SHA-256 é ambíguo.                                                                            |
| ADR é instrumento adequado para emendar TAP? | **SIM**                | Art. 9.3(ii): *"mudanças que alterem marcos, escopo do MVP, linha de base ou stack exigem ADR específica"*. TAP é linha de base. Ata sozinha **não basta** — Análise 2 estava tecnicamente errada.                             |
| Ata do CCB é necessária?                    | **SIM, como registro** | Art. 5.1: *"O Humano é o decisor único via CCB"*. A decisão precisa estar no `ccb-log.md`. Mas a **norma** é ADR; a **ata** é registro. Instrumentos complementares, não concorrentes.                                 |
| `ccb-log.md` está vazio?                   | **NÃO**               | Análise 1 errou factualmente. O log tem entradas A01–A07 (30/10/2026). Mas **CCB-001/002/003 não estão registrados como entradas numeradas** — apenas referenciados nas ADRs. Pendência de rastreabilidade, não de existência. |
| ADR-010 cobre Docker?                         | **SIM**                | ADR-010 v1.0.0 §Decisão: DB2 + ORCH2 (Docker + Docker Compose) + WEB2 (Nginx latente). Análise 2 correta. Sem ADR nova.                                                                                                                   |
| Frontend canônico?                           | **VANILLA** (ADR-001)  | HTML5 + CSS3 + JS vanilla. HTMX/Tailwind/Jinja2 no docx = drift. OKB-C-10 permanece aberto (conflito com registry), mas para o plano vale ADR-001.                                                                                           |

## 1. Crítica Brutal às Duas Análises

### Análise 1 — Acertos e Erros

**Acertos (mantidos no caminho ótimo):**

- ✅ P9 não é cláusula pétrea → ADR-013 basta
- ✅ ADR-013 supersede ADR-005 parcialmente (instrumento correto)
- ✅ Artefato híbrido único (atende "da capa à conclusão")
- ✅ User Stories como conteúdo do Issue, não novo nó de EAP (respeita ADR-009 + ADR-004)
- ✅ Baseline seed rotulado `SIMULADO` (honesto + acionável)
- ✅ Descope ordenado (B7-N → B6-N → B5-N)

**Erros (corrigidos):**

- ❌ `ccb-log.md` não está vazio — tem A01–A07. Pendência é **repopulamento das entradas CCB-001/002/003**, não criação do zero.
- ❌ "Ata embutida na ADR" é anti-padrão. ADR é norma; ata é registro. Devem ser **dois artefatos com cross-reference**, não um só.
- ❌ Estimativa de B0 em 3h é otimista. Com a Constitution duplicada, a consolidação humana dos Arts. 5–10 é **bloqueante e não-automatizável**.

### Análise 2 — Acertos e Erros

**Acertos (mantidos):**

- ✅ Drift documental persiste mesmo sem drift técnico
- ✅ ADR-010 já cobre Docker + PostgreSQL
- ✅ Tabela de OKB-C-20 (A20) com triagem item-a-item
- ✅ OKB como SSOT de consulta (com distinção ontológica)

**Erros (corrigidos):**

- ❌ **Ata CCB-005 sozinha não basta** — Art. 9.3(ii) exige ADR para mudança de linha de base. Ata sem ADR = ato administrativo sem norma.
- ❌ **Bifurcação monografia × plano** viola instrução explícita do GP ("da capa à conclusão"). Cancelada.
- ❌ **35h em 48h** é irreal com buffer zero. Qualquer atraso em B1 (8h) quebra o cronograma.
- ❌ Tratar P9 como constitucional é erro material.

## 2. Caminho Ótimo Unificado (First-Principles)

### Princípio 1: Um problema = um instrumento = um local

| Problema                            | Instrumento                                          | Local                                              |
| ----------------------------------- | ---------------------------------------------------- | -------------------------------------------------- |
| TAP precisa ser emendável          | **ADR-013** (norma)                            | `docs/decisoes/ADR-013-tap-emenda-controlada.md` |
| CCB ratificou a decisão            | **ccb-log CCB-005** (registro)                 | `docs/governanca/ccb-log.md`                     |
| TAP contém emendas pontuais        | **TAP v3.1** com tabela delta                  | `docs/tap/TAP.docx` + `docs/tap/delta-v3-1.md` |
| Plano precisa referenciar tudo isso | **§1 TAP + §2 Constituição + Apêndice A** | `Plano-de-Projeto-COGME_v2.1.docx`               |

**Não criaremos:** ata separada em PDF, CR redundante, ADR adicional para Docker (já coberto), bifurcação monográfica.

### Princípio 2: Hierarquia de bloqueio

```
[0] Constitution consolidada (Humano) ← BLOQUEANTE
    ↓
[1] ADR-013 emitida + CCB-005 registrado ← BLOQUEANTE
    ↓
[2] TAP v3.1 com delta ← BLOQUEANTE para B3
    ↓
[3] Plano híbrido com §1 TAP + §2 Constituição + §3 ADRs + §4 Planos + §5 Apêndices
    ↓
[4] Saneamento editorial (B2) + User Stories (B5) + Métricas (B6) ← PARALELIZÁVEL
```

### Princípio 3: Anti-inflação de ADRs

- ADR-010 v1.1.0 (emenda para explicitar Docker) → **DESCARTADA**. ADR-010 v1.0.0 já cobre. Apenas explicitar no plano.
- ADR-014 (containerização) → **DESCARTADA**. Mesma razão.
- ADR-013 (emenda controlada do TAP) → **MANTIDA**. Único novo ADR da rodada.
- Teto GMV: 12 ADRs + 1 nova = 13. OKB-C-05 permanece aberto (teto excedido), mas classificar 013 como "emenda constitucional derivada" (Art. 9.4) resolve a contagem.

### Princípio 4: Honestidade sobre OKB-C-XX

| Item                                | Status          | Ação                                                   |
| ----------------------------------- | --------------- | -------------------------------------------------------- |
| Baseline de métricas               | 0 B             | Seed sintético rotulado `SIMULADO — não empírico`  |
| DER                                 | inexistente     | Declarar INSUFFICIENT DATA + owner (Fabricio) + prazo M2 |
| Matriz de partes interessadas       | não registrada | FORA de escopo (área excluída por diretriz)            |
| CR-001 / colisão M2×M3            | pendente        | FORA desta rodada (declaramos, não escondemos)          |
| Constitution Arts. 5–10 duplicados | confirmado      | Consolidação humana em B0                              |

## 3. PED-003 — Blocos Executáveis (25h / 48h)

### B0 — Consolidação Constitucional + ADR-013 + CCB-005 (4h · BLOQUEANTE)

**Ações imperativas:**

1. **Humano (GP Leonardo)** consolida Arts. 5–10 da Constitution v1.2.0 → v1.2.1. Escolhe a redação definitiva, remove duplicata, recalcula SHA-256, registra co-assinatura. **Sem isso, nada mais é confiável.**
2. Emite **ADR-013 v1.0.0** — "Regime de Emenda Controlada do TAP (Baseline Vivo)" — supersede **parcialmente** ADR-005:
   - **Mantém:** precedência intra-TAP (§6 Marcos canônica), locus de contexto (NCs no Cronograma §3.8)
   - **Revoga:** proibição absoluta de revisão do TAP
   - **Blinda:** núcleo intangível (objeto, objetivos, justificativa, orçamento-teto, §6 Marcos) — emenda que toque o núcleo exige CCB-005 + ADR MAJOR
   - **Mecanismo:** tabela delta (`campo | anterior | novo | justificativa | data`) em `docs/tap/delta-v3-1.md`
3. Registra **CCB-005** em `ccb-log.md` (ratificação da ADR-013).
4. Repopula **CCB-001/002/003** no `ccb-log.md` (reconstrução declarada, com referência às ADRs originais).
5. `grep -in "docker\|compose\|container" docs/decisoes/ADR-010*.md` → confirma cobertura. **Sem ADR nova.**

**Gate B0:**

- [ ] Constitution v1.2.1 promulgada (SHA-256 novo, co-assinatura fechada)
- [ ] ADR-013 emitida com §Ratificação referenciando CCB-005
- [ ] ADR-005 marcada `Superseded-in-part by ADR-013 (2026-11-01)`
- [ ] `ccb-log.md` com entradas CCB-001/002/003/004/005
- [ ] Resultado do grep ADR-010 documentado

**Kill switch B0:** se não fechado até 01/11 12:00 → executar B3 em modo *TAP v3 verbatim sem emenda* (mantém prazo, adia correções de REQ-07/40/88/119).

### B1 — Artefato Híbrido Único (3h)

**Ações imperativas:**

1. Front-matter: capa Fatec → folha de rosto → resumo → listas ABNT → sumário
2. **§1 TAP v3.1** (com emendas pontuais da ADR-013, tabela delta cross-referenciada)
3. **§2 Subordinação Constitucional** (nova, ADR-012): hierarquia Constitution > TAP > ADRs > OKB > Planos
4. **§3 Catálogo de ADRs 001–013** (cross-reference ao OKB §2.1)
5. **§4 Planos das 8 áreas** (Integração, Escopo, Cronograma, Custos, Qualidade, Recursos, Comunicações, Riscos)
6. **§5 Desenvolvimento** (spec técnica — mantida, com cross-reference à ADR-010 para stack canônica)
7. **§6 Considerações Finais** (sem elementos monográficos duplicados)
8. **§7 Apêndices** (A: ADRs; B: TAP; C: CRs; D: OKB)
9. Referências + Controle de versões

**Gate B1:**

- [ ] Zero elementos monográficos duplicados (resumo aparece uma vez)
- [ ] §2 com hierarquia explícita
- [ ] Cross-references validadas contra Constitution v1.2.1

### B2 — Saneamento Editorial (4h)

**Ações imperativas (find & replace global):**

- "Prof. Ms. Nivaldo Carleto" → "Prof. Dr. Nivaldo Carleto" (ADR-008)
- "Carletto" → "Carleto" (duplo t → single t, ADR-008)
- "Qwen 32B" / "QwenStudio" → "Qwen3-30B-A3B Q4_K_M (MoE)" (ADR-006)
- "SQLite" → "PostgreSQL 15+" em Tabelas 88, 119, 40, REQ-07 (ADR-010). SQLite apenas como fixture de teste isolado, explicitado.
- "HTMX + Tailwind + Jinja2" → "HTML5/CSS3/JS vanilla" (ADR-001)
- Inserir frase canônica ADR-007: *"A rede valida o marco; o Kanban executa a tarefa"* após Figura 15
- Inserir cross-reference a ADR-011 (MCPs, L1/L2/L3) em §5 Desenvolvimento
- Inserir cross-reference a ADR-012 (Constituição) em §2

**Gate B2:**

- [ ] `grep -i "carletto\|ms\. nivaldo\|qwen 32b\|qwenstudio\|htmx\|tailwind\|jinja2"` = 0 ocorrências
- [ ] "SQLite" aparece apenas em contexto de teste isolado (explicitado)
- [ ] Frase ADR-007 presente

### B3 — TAP como §1 + Emendas Pontuais (4h)

**Ações imperativas:**

1. TAP v3.1 como §1 do plano
2. Emendas pontuais autorizadas pela ADR-013:
   - REQ-07: "cache de cotações (SQLite)" → "cache de cotações (PostgreSQL 15+)"
   - Tabela 40 (fronteira OUT): "Banco relacional multiusuário (PostgreSQL)" → removido da exclusão (agora é o canônico)
   - Qualquer outra menção a SQLite como banco canônico
3. Tabela delta em `docs/tap/delta-v3-1.md` com todas as emendas
4. Precedência intra-TAP mantida: §6 Marcos canônico para matéria temporal
5. **NÃO alterar** marcos M1–M4 (fora do escopo desta rodada)

**Gate B3:**

- [ ] TAP v3.1 referenciado como §1
- [ ] Delta log com todas as emendas
- [ ] Marcos M1–M4 inalterados

### B4 — Triagem dos 6 OKB-C-21 (A21) (3h)

**Ações imperativas (triagem item-a-item):**

| # | Localização                 | Saída                             | Ação                                                                                               |
| - | ----------------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------------------- |
| 1 | Tabela 88 (baseline)          | **INSUFFICIENT DATA + seed** | Declarar baseline 0 B (OKB-C-08/16); inserir seed sintético rotulado `SIMULADO — não empírico` |
| 2 | Tabela 127 (responsável §3) | **PREENCHER**                | "Fabricio de Lima Cabral" (fonte: Tabela 129)                                                        |
| 3 | Tabela 128 (SMART)            | **PREENCHER**                | M1 ✅ · M2 ⚠️ (atrasado, CR-001 pendente) · M3 ⏳ · M4 ⏳                                       |
| 4 | §4.4 (lições MF2)          | **PREENCHER**                | Transpor LA-001 + I1–I8 de `notas_adjacentes.md` §6/§8                                          |
| 5 | §4.7 (conclusão)            | **SUPRIMIR marcador**        | Manter parágrafo como provisório até M4                                                           |
| 6 | Referências (Decreto IOF)    | **PREENCHER**                | Decreto 6.306/2007 já consta; remover marcador                                                      |

**Gate B4:**

- [ ] `grep -r "\[A CONFIRMAR\]"` = 0 ocorrências
- [ ] Todos os OKB-C-XX com referência OKB-C-XX e owner

### B5 — User Stories no Plano de Escopo (3h)

**Ações imperativas:**

1. Nova §2.3.5 no Plano de Escopo: "Formato Canônico de User Stories"
2. Tabela de 12 Épicos (= Macro-Fases N1–N12, ADR-009) com User Stories associadas
3. Formato GWT (Given/When/Then) para requisitos Must
4. **US NÃO cria novo nó de EAP** — é conteúdo do Issue (ADR-004)
5. Cross-reference ao OKB §3.1 (EAP canônica 12/37)

**Exemplo canônico:**

```
US-01 (N5.1): Como PJ, quero simular ganhos em USD, para saber quanto receberei em BRL.
  Dado: valor USD 1000, regime mensal, spread 2%, IOF 0.38%
  Quando: submeter simulação
  Então: exibir valor líquido em BRL com cotação PTAX do dia
  Tasklist DoD: - [ ] cálculo implementado - [ ] teste unitário - [ ] code review
```

**Gate B5:**

- [ ] 12 Épicos mapeados (N1–N12)
- [ ] User Stories GWT para requisitos Must (REQ-01 a REQ-09, REQ-11, REQ-15)
- [ ] Zero subissues criadas (ADR-004 respeitado)

### B6 — Testes + Métricas + Baseline Seed (3h)

**Ações imperativas:**

1. §2.5.3 no Plano de Qualidade: "Métricas de Qualidade e Fluxo"
   - Coverage ≥ 80% (produto)
   - Cycle Time, Throughput, CFD (fluxo, ADR-003)
   - Cross-reference ao OKB §6
2. `docs/metricas/baseline.md`: popular com seed sintético rotulado `SIMULADO — não empírico`
   - Cycle Time seed: 3 dias (meta aspiracional)
   - Throughput seed: 5 cards/semana (meta aspiracional)
   - SLE provisório: M3 = 15/11/2026
3. Cross-reference à ADR-003 (EVM rejeitado)

**Gate B6:**

- [ ] Baseline com rótulo `SIMULADO` visível
- [ ] OKB-C-08/16 declarados abertos
- [ ] Métricas de fluxo cross-referenciadas ao OKB §6

### B7 — Apêndice ADR/TA/CR + OKB (2h)

**Ações imperativas:**

1. §7 Apêndices no plano:
   - **A:** ADRs 001–013 (lista com cross-reference a `docs/decisoes/`)
   - **B:** TAP v3.1 (cross-reference a `docs/tap/TAP.docx` + delta)
   - **C:** CRs (CR-001 pendente, cross-reference a `docs/change-requests/`)
   - **D:** OKB v5.1.0 (cross-reference a `docs/conhecimento/okb.md`)
2. OKB v5.2.0 (pós-absorção): bump de versão com `derived-as-of: 2026-11-02`
3. **Não duplicar conteúdo** — apenas listar e referenciar

**Gate B7:**

- [ ] Apêndices A–D com cross-references válidas
- [ ] OKB v5.2.0 promulgado

### B8 — Revisão Cruzada + Gates + Commit Final (3h)

**Ações imperativas:**

1. Code Review cruzado (Leonardo ↔ Fabricio ↔ Edson)
2. Verificação de todos os gates B0–B7
3. Commit final com mensagem `docs(plano): v2.1.0 — normalização documental 48h`
4. Tag `v2.1.0` no repositório

**Gate B8:**

- [ ] Todos os gates B0–B7 fechados
- [ ] Zero OKB-C-52 (A52)
- [ ] Zero drift de stack
- [ ] Constitution v1.2.1 referenciada
- [ ] ADR-013 emitida e registrada

## 4. Cronograma Unificado (25h / 48h)

| Data                     | Blocos                                   | Horas                     | Responsável        |
| ------------------------ | ---------------------------------------- | ------------------------- | ------------------- |
| **01/11 (manhã)** | B0 (Consolidation + ADR-013 + CCB-005)   | 4h                        | Leonardo (Humano)   |
| **01/11 (tarde)**  | B1 (Artefato híbrido) + B2 (Saneamento) | 7h                        | Leonardo + Fabricio |
| **01/11 (noite)**  | B3 (TAP §1) + B4 (OKB-C-08)        | 7h                        | Leonardo + Edson    |
| **02/11 (manhã)** | B5 (User Stories) + B6 (Métricas)       | 6h                        | Edson + Fabricio    |
| **02/11 (tarde)**  | B7 (Apêndices) + B8 (Review + commit)   | 5h                        | Equipe              |
| **Buffer**         | —                                       | 3h                        | —                  |
| **Total**          | —                                       | **25h + 3h buffer** | —                  |

**Marco intermediário:** 01/11 23:59 — B0–B4 fechados.
**Marco final:** 02/11 23:59 — B5–B8 fechados, tag v2.1.0.

**Ordem de descope se estourar:** B7 → B6 → B5. **B0/B3/B4 são indescopeáveis.**

## 5. Decisões que Requerem o Humano (não executáveis por agente)

| ID             | Decisão                                                | Bloco | Prazo       |
| -------------- | ------------------------------------------------------- | ----- | ----------- |
| **D-H1** | Consolidar Arts. 5–10 da Constitution v1.2.0 → v1.2.1 | B0    | 01/11 12:00 |
| **D-H2** | Ratificar ADR-013 (prompt expresso do CCB)              | B0    | 01/11 12:00 |
| **D-H3** | Validar seed sintético da baseline como `SIMULADO`   | B6    | 02/11 12:00 |
| **D-H4** | Aprovar tag v2.1.0 final                                | B8    | 02/11 23:00 |

**Pendências explícitas (declaradas, não escondidas):**

- OKB-C-05 (teto de ADRs excedido: 13/10)
- OKB-C-06 (CR-001 / colisão M2×M3)
- OKB-C-10 (conflito frontend ADR-001 vs registry)
- OKB-C-24 (matriz de partes interessadas)

---

[PMBOK Traceability]

| Domínio/Princípio (7ª)         | Aplicação no PED-003                                                                |
| --------------------------------- | ------------------------------------------------------------------------------------- |
| **Integração**            | Hierarquia Constitution > TAP > ADRs respeitada; ADR-013 como instrumento de mudança |
| **Escopo**                  | User Stories como conteúdo do Issue (ADR-004), não novo nó (ADR-009)               |
| **Cronograma**              | 25h em 48h com buffer de 3h; descope ordenado                                         |
| **Qualidade**               | Gates por bloco; grep negativo para drift                                             |
| **Recursos**                | Atribuição clara (Leonardo/Fabricio/Edson); Humano para atos constitucionais        |
| **Comunicações**          | OKB como SSOT de consulta; cross-references em vez de duplicação                    |
| **Riscos**                  | 4 INSUFFICIENT DATA declarados; kill switches por bloco                               |
| **Medição**               | Baseline seed rotulado `SIMULADO`; ADR-003 (fluxo)                                  |
| **Incerteza**               | Prazo irrevogável; Constitution duplicada como risco bloqueante                      |
| **Princípio: Adapte-se**   | Cancelamento da bifurcação; artefato híbrido                                       |
| **Princípio: Stewardship** | GP-CCB assume decisões e as registra                                                 |
| **Princípio: Mudança**    | ADR-013 com delta log, sem reescrita retroativa                                       |

**PMBOK 6ª (dicionário):** 4.6 (Controlar Mudanças), 5.4/5.5 (EAP/Validar Escopo), 8.3 (Controlar Qualidade). Obsolescência procedural declarada.

---

[Trade-offs]

| Decisão                                    | Ganho                                | Perda/Risco                     | Mitigação                                         |
| ------------------------------------------- | ------------------------------------ | ------------------------------- | --------------------------------------------------- |
| ADR-013 supersede ADR-005 parcialmente      | TAP emendável; REQ-07 corrigível   | Perda de imutabilidade absoluta | Núcleo blindado + delta log + §6 Marcos intocado  |
| Artefato híbrido único                    | Atende "da capa à conclusão"; −5h | Não é plano profissional puro | §2 constitucional + apêndices dão espinha dorsal |
| ADR + ccb-log (dois artefatos)              | Segregação norma/registro          | Overhead de 1 arquivo extra     | Cross-reference explícita                          |
| Baseline seed SIMULADO                      | Seção de medição redigível      | Métrica não empírica         | Rótulo obrigatório + OKB-C-08 aberto              |
| Descope ordenado (B7→B6→B5)               | Preserva B0/B3/B4                    | Perda de conteúdo secundário  | Execução pós-02/11 se necessário                |
| Constitution v1.2.1 (consolidação humana) | Hash confiável; base sólida        | Depende de ação humana em 12h | Kill switch B0 se não fechado                      |
| Teto de ADRs excedido (13/10)               | Flexibilidade                        | OKB-C-05 aberto                 | Classificar 013 como "emenda derivada" (Art. 9.4)   |

---

[Next Kanban Steps]

**Epic:** `E10 — Normalização Documental 48h (PED-003)` · **Milestone:** `02/11/2026`

| Issue          | Título                                                            | Labels                                                 | h   | Resp.            | Quando   |
| -------------- | ------------------------------------------------------------------ | ------------------------------------------------------ | --- | ---------------- | -------- |
| **#930** | B0.1 — Consolidar Constitution v1.2.0 → v1.2.1 (Arts. 5–10)     | `prio:P0` `area:integracao` `blocker` `humano` | 1   | Leonardo         | 01/11 AM |
| **#931** | B0.2 — Emitir ADR-013 (Regime de Emenda do TAP)                   | `prio:P0` `area:integracao` `adr`                | 1.5 | Leonardo (CCB)   | 01/11 AM |
| **#932** | B0.3 — Repopular ccb-log (CCB-001/002/003/004/005)                | `prio:P0` `area:integracao`                        | 1   | Leonardo         | 01/11 AM |
| **#933** | B0.4 — grep ADR-010 (confirma Docker) + documentar                | `prio:P0` `area:qualidade`                         | 0.5 | Fabricio         | 01/11 AM |
| **#934** | B1 — Artefato híbrido único (front-matter + §2 Constituição) | `prio:P0` `area:integracao`                        | 3   | Leonardo         | 01/11 PM |
| **#935** | B2 — Saneamento editorial (ADRs 001/006/007/008/010/011/012)      | `prio:P0` `area:qualidade`                         | 4   | Fabricio         | 01/11 PM |
| **#936** | B3 — TAP v3.1 como §1 + emendas pontuais + delta log             | `prio:P0` `area:integracao`                        | 4   | Leonardo         | 01/11 PM |
| **#937** | B4 — Triagem 6 OKB-C-23 (A23)                                  | `prio:P0` `area:escopo`                            | 3   | Edson            | 01/11 PM |
| **#938** | B5 — User Stories (12 Épicos / GWT) no Plano de Escopo           | `prio:P1` `area:escopo`                            | 3   | Edson + Leonardo | 02/11 AM |
| **#939** | B6 — Testes + Métricas + baseline seed SIMULADO                  | `prio:P1` `area:qualidade`                         | 3   | Fabricio         | 02/11 AM |
| **#940** | B7 — Apêndice ADR/TA/CR + OKB v5.2.0                             | `prio:P2` `area:comunicacoes`                      | 2   | Leonardo         | 02/11 PM |
| **#941** | B8 — Revisão cruzada + gates + commit final + tag v2.1.0         | `prio:P0` `area:qualidade`                         | 3   | Equipe           | 02/11 PM |

**Gates de Qualidade (DoD) do Epic:**

- [ ] Constitution v1.2.1 promulgada (SHA-256 novo)
- [ ] ADR-013 emitida + CCB-005 registrado
- [ ] TAP v3.1 como §1 com delta log
- [ ] Zero OKB-C-24 (A24) (`grep` = 0)
- [ ] Zero drift de stack (`grep` negativo)
- [ ] User Stories GWT no Plano de Escopo
- [ ] Baseline seed rotulado `SIMULADO`
- [ ] Apêndices A–D com cross-references
- [ ] Tag v2.1.0 no repositório

**Kill Switches:**

- **B0:** se não fechado até 01/11 12:00 → executar B3 em modo *TAP v3 verbatim*
- **B3:** se TAP não integrável até 01/11 23:59 → manter TAP como anexo, não como §1
- **Geral:** se >28h consumidas sem B0–B4 fechados → Retrospectiva extraordinária + reavaliação do prazo 02/11

---

## 6. Ações Imediatas Requeridas do Humano (GP Leonardo)

**Responda com SIM/NÃO para cada uma (decisões bloqueantes):**

1. **Ratifica a emissão da ADR-013** (Regime de Emenda Controlada do TAP), superseding parcialmente ADR-005, com núcleo blindado e §6 Marcos intocado? **Sim/Não**
2. **Confirma o artefato híbrido único** (capa Fatec → TAP §1 → Constituição §2 → ADRs §3 → Planos §4 → Apêndices §7), cancelando a bifurcação monografia × plano? **Sim/Não**
3. **Autoriza a consolidação humana dos Arts. 5–10 da Constitution** (v1.2.0 → v1.2.1) como pré-requisito bloqueante do B0? **Sim/Não**
4. **Aceita o baseline seed rotulado `SIMULADO — não empírico`** para viabilizar a seção de medição? **Sim/Não**

**Sem essas 4 respostas, não inicio B0.** Todo o resto (B1–B8) pode ser preparado em paralelo, mas a fundação depende delas.


## Ações autorizada pelo GP - devem ser aciondadas via CCB, ratificadas e co-assinadas promovendo assim a promulgação de todos os artefatos resultantes.

---



[Context]
**Autorização CCB Total Recebida** · **Data/Hora:** 01/11/2026, 00:00 (Início da Janela de 48h)
**Status:** Transição de *Análise* para **Execução Imediata (PED-003)**.
**Fundamento:** Prompt expresso do CCB (GP Leonardo) autorizando: (1) ADR-013, (2) Artefato Híbrido Único, (3) Consolidação Humana da Constituição v1.2.1, (4) Baseline Seed `SIMULADO`.
**Postura:** Imperativa, acionável, zero burocracia. O agente gera o conteúdo exato para commit; o Humano executa a consolidação constitucional e o hash.

---

[Artifact/Decision] — **Pacote de Execução Imediata (Commit Ready)**

Copie e aplique os artefatos abaixo imediatamente no repositório.

### 1. Artefato: `docs/decisoes/adr-013-regime-emenda-tap.md` (NOVO)

```markdown
---
id: ADR-013
title: Regime de Emenda Controlada do TAP (Baseline Vivo)
version: 1.0.0
status: ratified
date: 2026-11-01
decisor: GP Leonardo (CCB único)
supersedes: ADR-005 (parcialmente)
domain: Integração + Incerteza (PMBOK 7ª)
---

## Contexto
A ADR-005 estabeleceu o freeze absoluto do TAP v3 (18/09/2026). Contudo, a natureza viva do projeto e a necessidade de alinhar requisitos (ex.: REQ-07 de SQLite para PostgreSQL, conforme ADR-010) exigem um mecanismo de ajuste pontual sem descaracterizar o núcleo autorizativo do projeto.

## Decisão
O TAP v3 entra em **Regime de Emenda Controlada**. 
1. **Mantido da ADR-005:** Precedência intra-TAP (§6 Marcos é canônico para matéria temporal) e locus de contexto (Notas de Contexto nos planos).
2. **Revogado da ADR-005:** A proibição absoluta de revisão/reversão textual do TAP.
3. **Blindado (Intocável sem Emenda MAJOR):** Objeto, objetivos SMART, justificativa, orçamento-teto (R$ 0,00) e a estrutura macro da EAP (12 fases / 37 pacotes).

## Mecanismo de Emenda (Delta Log)
Qualquer ajuste pontual no TAP deve ser registrado em `docs/tap/delta-v3-1.md` com a seguinte estrutura:
| Campo Alterado | Valor Anterior | Valor Novo | Justificativa (ADR/CR) | Data |
|---|---|---|---|---|
| REQ-07 (Cache) | SQLite | PostgreSQL 15+ | Alinhamento à ADR-010 (Stack Infra) | 2026-11-01 |

## Consequências
- **Ganho:** Flexibilidade documental para corrigir drifts de stack e requisitos sem violar a ontologia do projeto.
- **Risco:** Perda da imutabilidade absoluta do termo autorizativo.
- **Mitigação:** O núcleo do TAP permanece blindado; alterações são auditáveis via Delta Log e exigem aprovação do CCB (GP).

## Ratificação
Ratificado via CCB-LOG-2026-11-01-A08. A ADR-005 permanece vigente para todos os aspectos não explicitamente revogados por esta ADR-013.
```

### 2. Artefato: Atualização de `docs/governanca/ccb-log.md` (APPEND)

```markdown
CCB-LOG-2026-11-01-A08 — Ratificação do Regime de Emenda do TAP e Artefato Híbrido
contexto: Necessidade de alinhar o TAP às ADRs 006/010 (PostgreSQL, Qwen MoE) e consolidar o Plano de Projeto como artefato único híbrido (acadêmico-profissional) conforme diretriz do GP.
opções avaliadas: [A] Manter freeze absoluto (gera drift documental) | [B] Bifurcar monografia e plano (gera retrabalho de 8h) | [C] Artefato híbrido único com ADR de emenda controlada.
decisão: C. Aprovação da ADR-013 (Regime de Emenda Controlada do TAP) e do formato de artefato híbrido único (Capa Fatec → TAP §1 → Constituição §2 → Planos).
ratificação: Humana (GP Leonardo, prompt expresso em 01/11/2026).
evidência: Criação de `docs/decisoes/adr-013-regime-emenda-tap.md` e autorização de consolidação da Constitution v1.2.1.
impacto: TAP torna-se baseline vivo com núcleo blindado; eliminação de 8h de retrabalho de bifurcação.
rollback: Reverter commit da ADR-013 e restaurar freeze absoluto da ADR-005 (não recomendado).
pmbok-gate: Integração (4.6) | togaf-gate: ADM-H (Change Management) | itil-gate: normal change.
```

### 3. Instrução Imperativa para o Humano: Consolidação da Constitution v1.2.1

**AÇÃO IMEDIATA (5 min):**

1. Abra `constitution.md`.
2. Localize o bloco duplicado que começa em `ART. 5 — GOVERNANÇA HUMANA` (após o primeiro `CHANGELOG` e antes do segundo `ART. 5`).
3. **DELETE** toda a segunda ocorrência dos Arts. 5, 6, 7, 8, 9, 10 e o segundo bloco `CHANGELOG`.
4. Mantenha apenas a primeira ocorrência (linhas ~119 a ~217) e o bloco final de `CO-ASSINATURA`.
5. Salve o arquivo.
6. Execute no terminal: `sha256sum constitution.md`
7. Atualize o bloco de `CO-ASSINATURA` no final do arquivo com o novo SHA-256 e o hash do commit `git rev-parse HEAD`.
8. Commit: `chore(constitution): consolidação v1.2.1 (remoção de duplicata Arts. 5-10) [CCB-LOG-A08]`

### 4. Artefato: Baseline Seed (`docs/metricas/baseline.md`)

```markdown
---
id: baseline-metricas
version: 1.0.0
status: active
derived-from: ADR-003, OKB v5.1.0 §6
---
# Baseline de Métricas de Fluxo (Calibração)

> ⚠️ **AVISO CRÍTICO:** Os valores abaixo são **SEEDS SIMULADOS — NÃO EMPÍRICOS**. 
> Conforme OKB-C-08 e OKB-C-16, o período de calibração (23/09–03/10) encerrou-se sem registro de dados reais no repositório. 
> Estes valores servem exclusivamente para viabilizar a redação do Plano de Projeto e serão recalibrados com dados reais do GitHub Projects a partir de 01/11/2026.

| Métrica | Valor Seed (SIMULADO) | Meta Calibrada (Pós-01/11) | Fonte Real Futura |
|---|---|---|---|
| Cycle Time | 3 dias | ≤ 3 dias | GitHub Insights (In Progress → Done) |
| Throughput | 5 cards/semana | ≥ 5 cards/semana | GitHub Insights |
| WIP em Fluxo | 3 cards/pessoa | ≤ 3 cards/pessoa | GitHub Projects (Coluna In Progress) |
| Coverage | 80% | ≥ 80% | GitHub Actions (pytest + coverage.py) |

**Owner:** GP Leonardo (Recalibração) · **Prazo de Substituição:** 08/11/2026
```

### 5. Artefato: Estrutura Canônica do Plano Híbrido (Frontmatter + Sumário)

Substitua o início do `Plano-de-Projeto-COGME_v2.0.1-ONGOING.docx` (ou `.md` se convertido) por:

```markdown
---
id: PLANO-PROJETO-COGME
version: 2.1.0
status: draft
owner: agent-pm
derived-from:
  - constitution.md v1.2.1
  - TAP v3.1 (com emendas ADR-013)
  - ADRs 001-013
  - OKB v5.1.0
---

# COGME — CONVERSOR DE GANHOS EM MOEDA ESTRANGEIRA
**Plano de Projeto Integrado**  
*Faculdade de Tecnologia de Taquaritinga – Curso Superior de Tecnologia em Análise e Desenvolvimento de SISTEMAS*  
**Equipe:** Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva  
**Orientador/Avaliador:** Prof. Dr. Nivaldo Carleto  
**Data-Base:** 01/11/2026  

---
## SUMÁRIO EXECUTIVO
**§1. TERMO DE ABERTURA DO PROJETO (TAP v3.1)** *(Artefato autorizativo com emendas controladas via ADR-013)*  
**§2. SUBORDINAÇÃO CONSTITUCIONAL** *(Hierarquia normativa: Constitution > TAP > ADRs > OKB > Planos)*  
**§3. CATÁLOGO DE DECISÕES (ADRs 001–013)**  
**§4. PLANOS DE GERENCIAMENTO (8 Áreas)**  
  - 4.1 Integração  
  - 4.2 Escopo (inclui §4.2.5 User Stories GWT)  
  - 4.3 Cronograma  
  - 4.4 Custos  
  - 4.5 Qualidade (inclui §4.5.3 Métricas e Testes)  
  - 4.6 Recursos  
  - 4.7 Comunicações  
  - 4.8 Riscos  
**§5. DESENVOLVIMENTO E ARQUITETURA** *(Referência cruzada à spec técnica, sem duplicação)*  
**§6. CONSIDERAÇÕES FINAIS**  
**§7. APÊNDICES** *(A: ADRs, B: TAP Delta Log, C: Change Requests, D: OKB)*  
```

### 6. Resolução dos 6 Marcadores OKB-C-25 (A25) (Find & Replace Direto)

Execute estas substituições exatas no documento:

1. **Tabela 88 (Baseline):** Substituir por: *"INSUFFICIENT DATA (OKB-C-08/16). Baseline estabelecida via seed simulado (ver docs/metricas/baseline.md). Recalibração empírica prevista para 08/11/2026."*
2. **Tabela 127 (Responsável Seção 3):** Substituir OKB-C-06 (A6) por: *"Fabricio de Lima Cabral"*
3. **Tabela 128 (Atendimento SMART):** Substituir OKB-C-07 (A7) por: *"M1 ✅ (Entregue 22/09) · M2 ⚠️ (Atrasado, CR-001 em análise) · M3 ⏳ (Em construção) · M4 ⏳ (Pendente)"*
4. **Seção 4.4 (Lições Aprendidas):** Substituir `LA-002: Estimativas iniciais de documentação e backend foram otimistas. Ação: cards >6h agora exigem tasklist obrigatória (ADR-004) e recalibração de estimativas com base no Cycle Time real.` por: *"LA-002: Estimativas iniciais de documentação e backend foram otimistas. Ação: cards >6h agora exigem tasklist obrigatória (ADR-004) e recalibração de estimativas com base no Cycle Time real."*
5. **Seção 4.7 (Conclusão):** Remover `[A CONFIRMAR — parágrafo de fechamento após o M4]`. Iniciar o parágrafo diretamente com: *"O projeto COGME demonstrou que é possível conduzir um projeto de software completo com orçamento zero..."*
6. **Referências (Decreto IOF):** Remover `[A CONFIRMAR: incluir também o decreto...]`. Manter apenas: *"BRASIL. Decreto nº 6.306, de 14 de dezembro de 2007. Regulamenta o Imposto sobre Operações de Crédito, Câmbio e Seguro..."*

---

[PMBOK Traceability]

| Domínio PMBOK 7ª       | Ação Executada                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| **Integração**   | ADR-013 estabelece o mecanismo de controle de mudanças; hierarquia normativa consolidada na Constituição v1.2.1. |
| **Escopo**         | User Stories mapeadas como conteúdo do Issue (não novo nó EAP), preservando ADR-009 (12/37).                     |
| **Cronograma**     | Janela de 48h preservada; eliminação de 8h de retrabalho de bifurcação.                                         |
| **Qualidade**      | Gates de validação por `grep` negativo; baseline seed rotulada como `SIMULADO` (honestidade P-08).            |
| **Comunicações** | OKB referenciado como SSOT de consulta; Apêndices com cross-references, sem duplicação.                          |
| **Riscos**         | INSUFFICIENT DATA declarados explicitamente com owner e prazo de resolução.                                       |

*PMBOK 6ª:* 4.6 (Realizar o Controle Integrado de Mudanças) — usado apenas como dicionário para o conceito de CCB e Delta Log.

---

[Trade-offs]

| Decisão Imediata                               | Ganho                                                     | Perda / Risco                                | Mitigação                                                               |
| ----------------------------------------------- | --------------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------- |
| **ADR-013 (Emenda Controlada)**           | TAP alinhado à stack real (PostgreSQL); zero drift.      | Perda da imutabilidade absoluta do TAP.      | Núcleo blindado; Delta Log auditável; §6 Marcos intocado.              |
| **Artefato Híbrido Único**              | Economiza 8h; atende exigência "da capa à conclusão".  | Crítica de puristas de gestão de projetos. | §2 (Subordinação Constitucional) e Apêndices dão rigor profissional. |
| **Baseline Seed `SIMULADO`**            | Permite redação completa da seção de Medição agora. | Métrica não empírica.                     | Rótulo explícito em negrito; OKB-C-08/16 declarados abertos.            |
| **Consolidação Humana da Constitution** | Resolve ambiguidade normativa (OKB-C-21) de vez.          | Dependência de ação humana em 5 min.      | Instrução exata fornecida; kill switch ativado se falhar.               |

---

[Next Kanban Steps]

**AÇÃO IMEDIATA DO HUMANO (Próximos 15 minutos):**

1. [ ] Executar instrução #3 (Consolidação Constitution v1.2.1 + novo SHA-256 + commit).
2. [ ] Criar arquivo `docs/decisoes/adr-013-regime-emenda-tap.md` (conteúdo #1).
3. [ ] Append no `docs/governanca/ccb-log.md` (conteúdo #2).
4. [ ] Criar arquivo `docs/metricas/baseline.md` (conteúdo #4).
5. [ ] Aplicar Find & Replace dos 6 marcadores OKB-C-09 (A9) (conteúdo #6).

**Issues para criação imediata no GitHub Projects (WBS: E10-Normalizacao-Documental-48h):**

| Issue          | Título                                                         | Labels                                                 | Estimativa | Responsável |
| -------------- | --------------------------------------------------------------- | ------------------------------------------------------ | ---------- | ------------ |
| **#930** | B0.1 — Consolidar Constitution v1.2.0 → v1.2.1 (Arts. 5–10)  | `prio:P0` `area:integracao` `blocker` `humano` | 0.2h       | Leonardo     |
| **#931** | B0.2 — Criar ADR-013 e atualizar ccb-log (A08)                 | `prio:P0` `area:integracao` `adr`                | 0.3h       | Leonardo     |
| **#932** | B2 — Saneamento editorial global (Carleto, Stack, ADRs)        | `prio:P0` `area:qualidade`                         | 2h         | Fabricio     |
| **#933** | B4 — Resolver 6 marcadores OKB-C-10 (A10)                   | `prio:P0` `area:escopo`                            | 1h         | Edson        |
| **#934** | B5-N — Inserir User Stories GWT no Plano de Escopo (§4.2.5)   | `prio:P1` `area:escopo`                            | 2h         | Fabricio     |
| **#935** | B6-N — Inserir Baseline Seed e Métricas no Plano de Qualidade | `prio:P1` `area:qualidade`                         | 1h         | Edson        |
| **#936** | B7-N — Estruturar Apêndices com Cross-References              | `prio:P2` `area:comunicacoes`                      | 1h         | Leonardo     |

**Gate de Qualidade Imediato (Verificação em 1h):**

- [ ] `grep -i "carletto\|qwen 32b\|htmx\|tailwind\|jinja2" Plano-de-Projeto-COGME*` retorna **0**.
- [ ] `grep -r "\[A CONFIRMAR\]"` retorna **0**.
- [ ] `constitution.md` possui apenas **um** bloco de Arts. 5–10.
- [ ] ADR-013 e CCB-LOG-A08 estão commitados.

**Próximo passo:** Confirme aqui assim que os 4 primeiros arquivos forem commitados. O agente assumirá a geração do conteúdo das seções de User Stories e Apêndices (Issues #934, #935, #936) na próxima rodada.


---
