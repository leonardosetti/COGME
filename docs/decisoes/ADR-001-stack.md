# ADR-001 — Stack Tecnológica FOSS

| Campo | Valor |
|---|---|
| Versão | 1.0.0 |
| Status | Finalizado |
| Data da decisão | 19/09/2026 |
| Data de formalização do documento | 28/10/2026 |
| Decisor | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7) |
| Gatilhos G1–G4 | G1 (impacto transversal — todas as fases N4–N12), G2 (irreversibilidade prática — troca de stack reescreve backend), G4 (trade-off FOSS × conveniência proprietária) |
| Rastreabilidade | TAP §3 (Inovação) + §8 (Restrições FOSS/§8.4 orçamento zero) + §11; EAP N1.4, N4.1, N5.1–N5.4 (fila N9.1); REQ-12 (ADRs); ADRs correlatas: ADR-005 (freeze), ADR-006 (LLM local, Draft — Pending CCB Human Verification) |
| Domínio PMBOK 7ª | Trabalho do Projeto + Abordagem de Desenvolvimento |

## Contexto

O projeto exige stack 100% FOSS (restrição TAP §8.4, orçamento zero — TAP §11), com capacidade de: backend assíncrono para simulação cambial (REQ-01, latência ≤ 2s); geração de PDF (REQ-04, ≤ 3s); cache local (REQ-07); testes automatizados (REQ-08, coverage ≥ 80%). A seleção é executada na fase EAP N4.1 (Seleção e Validação da Stack FOSS), com validação por protótipo (TAP §10, R2; Plano de Cronograma NC-04).

Fonte autorizativa do corpo: resumo aprovado em `git dd3b087` (21/09/2026) + OKB §4 (ADR-001). O commit dd3b087 persistiu emissões 001–005 com 0 byte; a formalização em corpo íntegra ocorre em 28/10/2026 (ver ADR-005 para a política de regularização).

## Decisão

Adoção da seguinte stack (todas as licenças OSI-approved):

| Camada | Tecnologia | Licença | Justificativa |
|---|---|---|---|
| Backend | Python 3.11 + FastAPI | PSF / MIT | Assíncrono nativo, ecossistema maduro |
| Banco | SQLite | Public Domain | Zero-config, ACID, adequado ao MVP |
| Geração PDF | WeasyPrint | BSD-3-Clause | HTML/CSS → PDF, FOSS |
| Testes | pytest + coverage.py | MIT | Padrão Python, integração CI |
| CI/CD | GitHub Actions (Free Tier) | Proprietário gratuito | Nativo ao SSOT |
| Frontend | HTML5 + CSS3 + JS vanilla | — | KISS, sem framework pesado |
| LLM (SDD) | QwenStudio | Licença autorizada | TAP §3 (Inovação); inferência local via llama.cpp/Qwen 30B no hardware 8700G/60GB — ver ADR-006 (Draft — Pending CCB Human Verification) |

## Alternativas Consideradas

- Flask (MIT) — fallback registrado, acionável se a curva de aprendizado do FastAPI for excessiva.
- PostgreSQL — descartado: complexidade operacional desnecessária para MVP acadêmico.
- Ferramentas proprietárias de PDF/CI — descartadas: violam a restrição FOSS absoluta (P2) e orçamento zero.

## Consequências e Trade-offs

- ✅ Positivas: zero custo, auditabilidade total, comunidade ativa, compatibilidade com hardware local (P6 revisada).
- ⚠️ Riscos: SQLite limita concorrência (aceitável para o MVP acadêmico); WeasyPrint exige dependências nativas (glibc, Pango).
- 🔄 Fallback: FastAPI com curva excessiva → Flask (MIT).
- Trade-offs aceitos: Simplicidade (KISS) > Performance extrema; FOSS absoluto > conveniência proprietária; SQLite > PostgreSQL.
- Stack sob regime de freeze (ADR-005): mudança de componente exige ADR de emenda (KYB: MAJOR), nunca bypass (contratos: Plano de Custos §4.5/§4.6, gates de registro em ADR-001 ou ADR específica).

## Governança

- Custódia: agent-architect (R-01 stack-drift watch, CVE half co-ownership com digital-security).
- Emenda: somente via change-request + CCB humano (GP Leonardo) + ADR MAJOR (Integração §1.7; Plano de Custos §4.6).
- kill_switch: screened (sem vigilância por design; sem kernel proprietário sem Pilares de Bypass).

## Histórico

| Versão | Data | Autor | Mudança |
|---|---|---|---|
| 1.0.0 | 28/10/2026 | agent-architect | Formalização do corpo (decisão CCB de 19/09/2026; emissão original comprometida em commit de 0 byte — 21/09/2026; stubs contraditórios detectados 26/10) |
