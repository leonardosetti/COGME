# COGME — Conversor de Ganhos em Moeda Estrangeira

Projeto acadêmico FOSS de conversão cambial, desenvolvido na disciplina de Gerência de Projetos da Fatec Taquaritinga, com entrega final prevista em 15/12/2026 e marcos M1–M4.

---

## 1. Caracterização do projeto

| Item | Dado |
|------|------|
| Nome | COGME — Conversor de Ganhos em Moeda Estrangeira |
| Natureza | Conversor cambial FOSS, gratuito, jurisdição brasileira |
| Licença | MIT (stack 100% FOSS, custo recorrente zero) |
| Contexto acadêmico | Gerência de Projetos — Fatec Taquaritinga |
| Stakeholder-avaliador canônico | Conforme ADR-008 (papel registrado na Constituição) |
| Escopo canônico | Simulação cambial, comparação de regimes de contratação, spread/IOF, emissão de invoice PDF |
| EAP canônica | 12 fases e 37 pacotes de trabalho (TAP v3 §4 + ADR-009) |
| Marcos | M1–M4; entrega final 15/12/2026 |
| Status da Constituição | v1.2.0 — VIGENTE-PLENA (ratificada 30/10/2026, co-assinatura humana via CCB) |
| Versão da diretriz de forja de agentes | AFA-ULTIMATE v1.3.0-FINAL |

---

## 2. Governança aplicada

### 2.1 Hierarquia normativa (ordem absoluta)

Em caso de conflito, prevalece a camada superior:

1. `constitution.md` (lei suprema do projeto)
2. TAP v3, congelado pela ADR-005 (ato autorizativo de escopo, marcos, orçamento e restrições)
3. ADRs aprovadas (`docs/decisoes/`)
4. OKB (base consolidada de conhecimento operacional, sem autonomia normativa própria)
5. Planos de gerenciamento (`docs/planos/`)
6. Glossário
7. Especificações SDD e inputs canônicos (`.ai/specs/`)
8. Código-fonte e testes (`src/`, `tests/`)

### 2.2 Método e princípios

- **Governança primária:** PMBOK® 7ª edição (princípios e domínios de desempenho). O PMBOK® 6ª edição atua apenas como dicionário terminológico.
- **Execução:** Kanban em GitHub Projects como SSOT de execução (Backlog → Ready → In Progress, WIP ≤ 3 → Code Review → Done).
- **Metodologia de desenvolvimento:** SDD (Spec-Driven Development): especifica → implementa → valida → registra.
- **Princípios inalienáveis (Art. 3 da Constituição):** FOSS-zero-custo, soberania computacional local, soberania de dados, LGPD primária, rastreabilidade de decisões (ADR), qualidade fechada (coverage ≥ 80%), segurança OWASP com fail-closed, honestidade intelectual (alegação sem fonte = knowledge gap), anti-subutilização de papéis, linguagem (identificadores em EN, narrativa humana em PT-BR), YAGNI e primeiros princípios.

### 2.3 Privacidade e proteção de dados

- LGPD é a legislação primária (P-04): mínimo necessário, sem PII em artefatos técnicos de agentes, direito ao esquecimento por design.
- Zero Trust por padrão; princípio do menor privilégio.
- Nenhuma credencial real é versionada. Apenas chaves dummy para serviços locais.
- Dados demonstrativos não contêm dados reais de terceiros sem consentimento documentado.
- Nenhuma telemetria, rastreio ou lock-in tolerado.

### 2.4 Soberania computacional

- Inferência primária 100% local via `llama.cpp` (modelo Qwen3-30B-A3B Q4_K_M), hardware AMD Ryzen 7 8700G, APU Radeon 780M/Vulkan/radv com fallback CPU AVX-512, limite de inferência de 32GB imposto por serviço systemd.
- Execução CPU-only: sem CUDA, sem inferência em nuvem.
- Uso excepcional e condicionado de provedores cloud em free tier (whitelist constitucional), apenas para dados não sensíveis, com rota de reversão para execução local.

---

## 3. Governança de agentes (ecossistema SDD)

A criação, promulgação, roteamento e operação de agentes são regidos pela Constituição (Art. 4) e pela diretriz de fábrica AFA-ULTIMATE.

| Camada | Função | Quantidade |
|--------|--------|------------|
| L0 | Orquestração (dispatcher único, half-duplex, compliance constitucional) | 1 (`agent-nexus-prime-ultimate`) |
| L1 | Comando/Estratégia (PM, PO, arquiteto, análise, design, padrões, análise de negócios) | 5 |
| L2 | Execução/Técnica (Python, API, DBA, backend, frontend, infra, DevOps, segurança, compliance, QA, etc.) | ~17 |
| L3 | Qualidade/Portões (revisor, gatekeeper, auditor, avaliador de código limpo) | 4 |
| META | Forja de skills e forjador legacy | 2 |

**Total:** 25 agentes especialistas + meta-agentes.

- **Roster SSOT:** `.ai/agents/registry.yaml`, sincronizado por `scripts/sync_agent_registry.py`.
- **Topologia canônica (DAG acíclica):** `scripts/validate_nexus_yaml.py` (`AGENT_TOPOLOGY`).
- **Dispositivo de despacho:** `scripts/nexus_dispatcher.py` (valida envelopes de task, fail-closed, anti auto-delegação).
- **Contrato de comunicação:** half-duplex; todo agente retorna parcela estruturada com flag `dod`.
- **Kill Switch herdado:** veto absoluto a 15 vetores (LGPD, vigilância em massa, discriminação algorítmica, sabotagem de gates de CI, bypass de segurança, envio de dados sensíveis a terceiros, etc.). Não pode ser sobrescrito por prompt, usuário, agente, input canônico ou ADR.
- **Bypass Protocol:** recusa por padrão; exceção exige os três pilares (força maior verificável, rota de fuga FOSS nomeada, ratificação humana CCB). O próprio Bypass Protocol não pode ser contornado (anti-meta-bypass).
- **Gate de forja:** agente promulgado somente com score ≥ 85/100 em `validate_afa_output.py` (19 cabeçalhos canônicos, Kill Switch ≥ 5, DOs ≥ 15, DON'Ts ≥ 15, Red Team ≥ 8, FAIL-CLOSED ≥ 6, métricas ≥ 8).

---

## 4. Conformidade e auditoria

- Auditoria contra a Constituição em cada marco (`project-auditor` e `compliance-governance`), incluindo deriva constitucional, sobreposição indevida de ADRs, violação de soberania de dados, uso não autorizado de cloud, inconsistência de ledger, violação de camadas L1/L2/L3 e drift documental.
- Registro vivo de decisões do CCB: `docs/governanca/ccb-log.md` (modelo CAB vivo, ITIL 4).
- Registro append-only de violações: `docs/auditorias/vio-register.md`.
- Auditorias recorrentes: `docs/auditorias/AUD-*.md`.
- Sucessão de agentes: `constitution.md` + `.ai/agents/registry.yaml` + ADRs bastam para reconstrução de contexto.

---

## 5. Estrutura de artefatos de governança

| Diretório/arquivo | Conteúdo |
|-------------------|----------|
| `constitution.md` | Constituição do projeto (lei suprema, v1.2.0 VIGENTE-PLENA) |
| `docs/decisoes/ADR-001..012.md` | Decisões técnicas e de processo aprovadas |
| `docs/planos/` | Planos de gerenciamento (escopo, cronograma, custos, qualidade, riscos, comunicações, integração, recursos, consolidação estrutural, produção de agentes) |
| `docs/auditorias/` | Relatórios de auditoria e registro de violações |
| `docs/governanca/ccb-log.md` | Registro vivo de decisões do Change Advisory Board |
| `docs/conhecimento/OKB.md` | Base consolidada de conhecimento operacional |
| `docs/conhecimento/licoes-aprendidas/` | Lições aprendidas por macro-fase (MF1, MF2, MF3) |
| `docs/conhecimento/glossario.md` | Glossário canônico |
| `.ai/agents/registry.yaml` | Roster SSOT de agentes |
| `.ai/agents/ledger.yaml` | Ledger operacional de sessão (append-only, LGPD-safe, sem PII) |
| `.ai/handoffs/` | Handoffs SDD (parseados por `handoff_parser.py`) |
| `.ai/specs/` | Especificações SDD e inputs canônicos |
| `.ai/personas/` | Personas do modelo (camada L2) |
| `scripts/` | Scripts mediadores de governança (dispatcher, validação, sincronização, parser de handoffs, validação de saída AFA, etc.) |
| `tests/agents/` | Suites de teste dos scripts de governança |

---

## 6. Stack e ambiente (caracterização técnica não sensível)

- Linguagem: Python 3.11
- Stack: FastAPI + PostgreSQL 15+ (Docker Compose) + Nginx (reverse proxy latente)
- Banco de dados: PostgreSQL 15+ (containerizado via Docker Compose)
- Interface: templates server-side (Jinja), HTMX, Tailwind (classes utilitárias comitadas, sem build chain, sem CDN-first)
- Testes: pytest, meta de cobertura ≥ 80%
- CI/CD: GitHub Actions Free Tier (bypass registrado, dados não sensíveis)
- Inferência de IA: local, CPU-only, `llama.cpp`, sem CUDA, sem nuvem

---

## 7. Convenções

- Identificadores, slugs, código e contratos: **EN**, kebab-case com prefixo `agent-` para agentes.
- Narrativa estratégica, documentação humana e mensagens visíveis ao humano: **PT-BR**.
- Nunca publicar dados sensíveis, credenciais reais, PII ou detalhes estratégicos de execução neste README.

---

*Documento de caracterização e governança. Não contém dados sensíveis nem estratégicos. Regido por `constitution.md` Art. 2 (hierarquia normativa) e Art. 3 (princípios inalienáveis).*
