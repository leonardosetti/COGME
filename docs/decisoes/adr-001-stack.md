---
id: docs-decisoes-adr-001-stack
title: ADR-001 — Stack Tecnológica FOSS
type: adr
version: 1.0.0
status: ativo
owner: agent-project-analyst
derived-from:
- docs/decisoes/adr-001-stack.md (adequado à norma em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- decisoes
- docs
- adequado-a-norma
---
---
id: decisoes-adr-001-stack
title: ADR-001 — Stack Tecnológica FOSS
version: 1.2.0
class: decisao-adr
status: ratificado
owner: agent-project-analyst
derived-from:
- docs/decisoes/adr-001-stack.md (normalizado em 2026-11-05)
last-revised: '2026-11-05'
lgpd-class: n/a
tags:
- decisoes
- docs
- normalizado
- self-updated
data-decisao: '19/09/2026'
data-formalizacao: '28/10/2026'
decisor: GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7)
gatilhos: G1, G2, G4
rastreabilidade: TAP §3 (Inovação) + §8 (Restrições FOSS/§8.4 orçamento zero) + §11; EAP N1.4, N4.1, N5.1–N5.4 (fila N9.1); REQ-12 (ADRs); ADRs correlatas: ADR-005 (freeze), ADR-006 (LLM local), ADR-010 (supersedida por esta versão — veja ADR-LOG-001)
dominio-pmbok: Trabalho do Projeto + Abordagem de Desenvolvimento
processo-pmbok-6: 4.6
kill-switch: screened
---
# ADR-001 — Stack Tecnológica FOSS

| Campo | Valor |
|---|---|
| Versão | 1.2.0 |
| Status | Ratificado (CCB único) |
| Data da decisão | 19/09/2026 |
| Data de formalização do documento | 28/10/2026 (v1.0.0); 31/10/2026 (v1.1.0 — emenda ADR-LOG-001); 05/11/2026 (v1.2.0 — emenda frontend ADR-LOG-002) |
| Decisor | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| Gatilhos G1–G4 | G1 (impacto transversal — todas as fases N4–N12), G2 (irreversibilidade prática — troca de stack reescreve backend), G4 (trade-off FOSS × conveniência proprietária) |
| Rastreabilidade | TAP §3 (Inovação) + §8 (Restrições FOSS/§8.4 orçamento zero) + §11; EAP N1.4, N4.1, N5.1–N5.4 (fila N9.1); REQ-12 (ADRs); ADRs correlatas: [ADR-005 v1.1.0](docs/decisoes/adr-005-regime-tap.md) (freeze), [ADR-006 v2.1.0](docs/decisoes/adr-006-ecossistema-sddai.md) (LLM local), [ADR-010 v1.0.0](docs/decisoes/adr-010-stack-infraestrutura.md) (supersedida por esta versão — veja ADR-LOG-001) |
| Domínio PMBOK 7ª | Trabalho do Projeto + Abordagem de Desenvolvimento |

## Contexto

O projeto exige stack 100% FOSS (restrição TAP §8.4, orçamento zero — TAP §11), com capacidade de: backend assíncrono para simulação cambial (REQ-01, latência ≤ 2s); geração de PDF (REQ-04, ≤ 3s); cache local (REQ-07); testes automatizados (REQ-08, coverage ≥ 80%). A seleção é executada na fase EAP N4.1 (Seleção e Validação da Stack FOSS), com validação por protótipo (TAP §10, R2; Plano de Cronograma NC-04).

**Emenda ADR-LOG-001 (31/10/2026):** Substituição de SQLite por PostgreSQL 15+ como banco canônico; adição de Docker Compose + Nginx latente como orquestração e proxy; definição de hierarquia de APIs de câmbio (Frankfurter primária, PTAX/BCB fallback). Esta emenda incorpora o conteúdo deliberado na ADR-010 (emitida 29/10/2026), que agora fica consolidada nesta ADR-001 v1.1.0. A ADR-010 permanece como artefato histórico de rastreamento.

Fonte autorizativa do corpo: resumo aprovado em `git dd3b087` (21/09/2026) + OKB §4 (ADR-001). O commit dd3b087 persistiu emissões 001–005 com 0 byte; a formalização em corpo íntegra ocorre em 28/10/2026 (ver ADR-005 para a política de regularização). A emenda v1.1.0 foi autorizada pelo CCB em 31/10/2026 (RAT-2026-10-31-A13).

## Decisão

Adoção da seguinte stack (todas as licenças OSI-approved):

| Camada | Tecnologia | Licença | Justificativa |
|---|---|---|---|
| Backend | Python 3.11 + FastAPI | PSF / MIT | Assíncrono nativo, ecossistema maduro |
| Banco | PostgreSQL 15+ | PostgreSQL License | Tipagem estrita, concorrência MVCC, ecossistema maduro, valor acadêmico. Substitui SQLite (ADR-001 v1.0.0) conforme ADR-LOG-001. |
| Banco (testes isolados) | SQLite | Public Domain | Apenas como fixture de teste isolado, explicitado |
| Geração PDF | WeasyPrint | BSD-3-Clause | HTML/CSS → PDF, FOSS |
| Testes | pytest + coverage.py | MIT | Padrão Python, integração CI |
| CI/CD | GitHub Actions (Free Tier) | Proprietário gratuito | Nativo ao SSOT |
| Frontend | Jinja2 + HTMX + Tailwind CSS | BSD-3-Clause / MIT | Templates server-side (Jinja) + interatividade leve (HTMX) + estilização utility-first (Tailwind); alinha roster/infra e encerra OKB-C-10 |
| LLM (SDD) | Qwen3-30B-A3B Q4_K_M (MoE) | Licença autorizada | TAP §3 (Inovação); inferência local via llama.cpp/Qwen no hardware 8700G/60GB — ver ADR-006 |
| Orquestração | Docker + Docker Compose | FOSS (Apache-2.0 / MIT) | Paridade dev/test/prod, isolamento de camadas (ADR-010) |
| Proxy | Nginx (latente, perfil opcional) | FOSS (BSD-2-Clause) | Reverse proxy latente para perfil opcional (ADR-010) |
| Hierarquia de APIs de câmbio | Frankfurter (primária) + PTAX/BCB (fallback obrigatório) | MIT / Governo Brasileiro | Cotação oficial PTAX como âncora de soberania (ADR-010) |

## Alternativas Consideradas

- Flask (MIT) — fallback registrado, acionável se a curva de aprendizado do FastAPI for excessiva.
- SQLite — mantido apenas como fixture de teste isolado (não como banco canônico de persistência). Substituído por PostgreSQL 15+ como banco canônico (ADR-LOG-001).
- Ferramentas proprietárias de PDF/CI — descartadas: violam a restrição FOSS absoluta (P2) e orçamento zero.
- Ferramentas proprietárias de PDF/CI — descartadas: violam a restrição FOSS absoluta (P2) e orçamento zero.

## Consequências e Trade-offs

- ✅ Positivas: zero custo, auditabilidade total, comunidade ativa, compatibilidade com hardware local (P6 revisada), tipagem estrita e concorrência MVCC (PostgreSQL), paridade ambiental (Docker), resiliência cambial multi-fonte com âncora brasileira (PTAX).
- ⚠️ Riscos: SQLite limita concorrência (aceitável apenas como fixture de teste isolado); WeasyPrint exige dependências nativas (glibc, Pango); overhead inicial de setup Docker.
- 🔄 Fallback: FastAPI com curva excessiva → Flask (MIT); PostgreSQL → SQLite apenas como fixture de teste isolado (não como banco canônico).
- Trade-offs aceitos: Simplicidade (KISS) > Performance extrema; FOSS absoluto > conveniência proprietária; PostgreSQL > SQLite como banco canônico (ADR-LOG-001).
- Stack sob regime de emenda controlada (ADR-013): mudança de componente exige ADR específica, nunca bypass (contratos: Plano de Custos §4.5/§4.6, gates de registro em ADR-001 ou ADR específica).

## Governança

- Custódia: agent-architect (R-01 stack-drift watch, CVE half co-ownership com digital-security).
- Emenda: somente via change-request + CCB humano (GP Leonardo) + ADR específica (Integração §1.7; Plano de Custos §4.6).
- kill_switch: screened (sem vigilância por design; sem kernel proprietário sem Pilares de Bypass).

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo | Domínio PMBOK 7ª | Data |
|---|---|---|---|---|
| ADR-010 | Parcial | Substituição de SQLite por PostgreSQL 15+; adição de Docker Compose + Nginx latente; definição de hierarquia de APIs de câmbio (Frankfurter primária, PTAX/BCB fallback) | Abordagem de Desenvolvimento | 29/10/2026 |
| ADR-001 v1.1.0 | Parcial | Substituição do frontend HTML5/CSS3/JS vanilla por Jinja2 + HTMX + Tailwind CSS (alinha roster/infra; encerra OKB-C-10) | Abordagem de Desenvolvimento | 05/11/2026 |

## Histórico

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 28/10/2026 | agent-architect | Formalização do corpo (decisão CCB de 19/09/2026; emissão original comprometida em commit de 0 byte — 21/09/2026; stubs contraditórios detectados 26/10) |
| 1.1.0 | 31/10/2026 | GP Leonardo (CCB) | Emenda ADR-LOG-001: substituição de SQLite por PostgreSQL 15+ como banco canônico; adição de Docker Compose + Nginx latente; definição de hierarquia de APIs de câmbio (Frankfurter primária, PTAX/BCB fallback). Incorpora conteúdo da ADR-010 (emitida 29/10/2026), que passa a ser referência histórica. |
| 1.2.0 | 05/11/2026 | GP Leonardo (CCB) | Emenda ADR-LOG-002: substituição do frontend HTML5/CSS3/JS vanilla por Jinja2 + HTMX + Tailwind CSS (alinha roster/infra; encerra OKB-C-10). Sobrepõe parcialmente a ADR-001 v1.1.0 (camada Frontend). |
