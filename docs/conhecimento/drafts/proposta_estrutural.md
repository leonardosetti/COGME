# Proposta de Reestruturação do Projeto COGME — v1.0

**Fundamentação:** Alinhada ao **P3 (KISS como métrica de arquitetura)**, à **árvore de artefatos v2.1** (`OKB_COGME_v2.1.md §5`) e ao **Domínio de Abordagem de Desenvolvimento do PMBOK 7ª** (100% FOSS + Kanban + SDD auditável). A estrutura deve servir como **esqueleto executável**, não como depósito de arquivos.

---

## 1. Diagnóstico da Estrutura Atual

| Problema | Impacto | Referência OKB v2.1 |
|---|---|---|
| Organização por **formato** (`.docx`, `.md`, `.pdf`) em vez de **propósito** | Dificulta rastreabilidade TAP → EAP → Kanban | §5 (árvore de artefatos) |
| Ausência das pastas `00` a `11` da árvore v2.1 | Viola governança documental | §5 |
| Sem estrutura de código (backend/frontend/tests) | Bloqueia Fase 4 (Configuração de Ambiente) | §6 (Fase 4) |
| Sem estrutura Docker/volumes | Viola premissa de persistência local | Premissa do usuário |
| Sem CI/CD (`.github/workflows/`) | Bloqueia Fase 7 (DevOps) | §6 (Fase 7) |
| Imagens (drawio/png) sem referência aos artefatos | Perde rastreabilidade visual | §10 (checklist #1) |
| `xml/` com EAPs sem versão ou changelog | Risco de obsolescência silenciosa | §10 (checklist #2) |

---

## 2. Estrutura Proposta (Monorepo Full-Stack)

~~~
COGME/
│
├── 📄 README.md                          # Fonte de verdade do projeto
├── 📄 LICENSE                            # FOSS (P2)
├── 📄 .gitignore                         # v1.0 (já gerado)
├── 📄 .env.example                       # Template de variáveis (sem segredos)
├── 📄 docker-compose.yml                 # Orquestração (backend + frontend + redis + db)
├── 📄 Makefile                           # Comandos padronizados (make up, make test, make lint)
│
├── 📁 .github/
│   └── workflows/
│       ├── ci.yml                        # Lint + testes + coverage (Fase 7.1)
│       └── cd.yml                        # Build + deploy (Fase 7.2)
│
├── 📁 docker/
│   ├── backend/
│   │   └── Dockerfile
│   ├── frontend/
│   │   └── Dockerfile
│   ├── redis/
│   │   └── redis.conf
│   └── volumes/                          # ⚠️ GITIGNORED — persistência local
│       ├── postgres/
│       ├── redis/
│       └── invoices/                     # PDFs gerados (WeasyPrint)
│
├── 📁 00.TAP/
│   ├── TAP_v0.9.md                       # Termo de Abertura (viva)
│   ├── TAP_v0.9.pdf                      # Versão fechada (CCB)
│   └── changelog.md
│
├── 📁 01.PlanoIntegracao/
│   ├── plano_integracao.md
│   └── guardrails.md                     # OKB_COGME_v2.1.md (movido da raiz)
│
├── 📁 02.PlanoEscopo/
│   ├── plano_escopo.md
│   ├── eap/
│   │   ├── EAP.md                        # Versão textual (rastreável)
│   │   ├── EAP.drawio                    # Versão visual
│   │   ├── EAP.png                       # Export (gerado automaticamente)
│   │   └── dicionario_eap.md             # Descrição de cada pacote
│   └── requisitos/
│       ├── rf_rnf_consolidado.md         # Fusão de rf_rnf_qwen + deepseek
│       └── casos_uso.md
│
├── 📁 03.PlanoCronograma/
│   ├── plano_cronograma.md               # Roadmap estratégico (não Gantt)
│   ├── roadmap.md
│   └── kanban_setup.md                   # Configuração do GitHub Projects
│
├── 📁 04.PlanoCustos/
│   └── plano_custos.md
│
├── 📁 05.PlanoQualidade/
│   ├── plano_qualidade.md
│   ├── dod.md                            # Definition of Done
│   └── dor.md                            # Definition of Ready
│
├── 📁 06.PlanoRecursos/
│   ├── plano_recursos.md
│   └── raci.md
│
├── 📁 07.PlanoComunicacoes/
│   ├── plano_comunicacoes.md
│   └── matriz_comunicacao.md
│
├── 📁 08.PlanoRiscos/
│   ├── plano_riscos.md
│   ├── matriz_prob_impacto.md
│   └── risk_backlog.md
│
├── 📁 09.BaseConhecimento/
│   ├── 09.1.ADRs/
│   │   ├── ADR-001_github_projects_ssot.md
│   │   ├── ADR-002_stack_tecnologica.md  # Pendente
│   │   └── ADR-003_estrutura_diretorios.md  # Este documento
│   ├── 09.2.LicoesAprendidas/
│   │   └── retrospectivas.md
│   ├── 09.3.PromptsSDD/
│   │   ├── llm_base_persona.md           # Movido de Docs/md
│   │   └── catalogo_prompts.md
│   └── 09.4.Runbooks/
│       ├── setup_ambiente.md
│       └── troubleshooting.md
│
├── 📁 10.PlanoMudancas/
│   ├── plano_mudancas.md
│   └── registro_solicitacoes.md
│
├── 📁 11.src/                            # Código-fonte (MVP full-stack)
│   ├── backend/
│   │   ├── app/
│   │   │   ├── main.py                   # FastAPI/Flask entrypoint
│   │   │   ├── api/                      # Endpoints REST
│   │   │   ├── core/                     # Config, segurança, dependências
│   │   │   ├── services/                 # Lógica de negócio (câmbio, PDF)
│   │   │   ├── adapters/                 # Adapter pattern (APIs de câmbio)
│   │   │   ├── models/                   # SQLAlchemy/Pydantic
│   │   │   └── repositories/             # Acesso a dados
│   │   ├── tests/
│   │   │   ├── unit/
│   │   │   └── integration/
│   │   ├── alembic/                      # Migrações de BD
│   │   ├── requirements.txt
│   │   └── pyproject.toml
│   │
│   ├── frontend/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   ├── pages/
│   │   │   ├── services/                 # Chamadas à API
│   │   │   └── styles/
│   │   ├── public/
│   │   ├── tests/
│   │   ├── package.json
│   │   └── vite.config.js
│   │
│   ├── shared/                           # Tipos/contratos compartilhados
│   │   └── schemas/
│   │
│   └── scripts/                          # Utilitários (seed, migrate, etc)
│       ├── seed_db.py
│       └── generate_eap_png.sh
│
├── 📁 docs/                              # Documentação viva do projeto (não versionada como artefato)
│   ├── status/
│   │   └── status_COGME_YYYYMMDDHHMMSS.md  # Movido de _status_analitico
│   ├── analises/
│   │   ├── analise_stack_marcos.md       # Movido de Docs/md
│   │   ├── review_rf_rfn.md
│   │   └── log_resumo_projeto.md
│   └── glossario.md                      # Movido da raiz de Docs/md
│
├── 📁 assets/                            # Imagens e diagramas (referenciados por artefatos)
│   ├── drawio/
│   │   ├── EAP.drawio                    # Movido de img/drawio
│   │   └── arquitetura_sistema.drawio    # Novo
│   └── png/
│       ├── EAP_full.png                  # Movido de img/png_transparent
│       └── arquitetura_sistema.png
│
└── 📁 legacy/                            # ⚠️ GITIGNORED — material obsoleto
    ├── docx/
    │   └── Termo de Abertura do Projeto v1.doc
    └── xml/
        ├── EAP_monochrome.xml
        └── ...
~~~

---

## 3. Justificativa das Decisões

| Decisão | Fundamentação | Referência |
|---|---|---|
| **Numeração `00` a `11`** | Rastreabilidade direta com EAP (Nível 1) e com Kanban (Épicos) | OKB v2.1 §5 + §6 |
| **`docs/` separado de `09.BaseConhecimento/`** | `docs/` = trabalho em andamento (análises, status); `09.` = conhecimento consolidado (ADRs, prompts) | Domínio de Entrega PMBOK 7ª |
| **`docker/volumes/` gitignored** | Persistência local sem poluir repositório; alinhado à premissa do usuário | P3 KISS |
| **`11.src/` com backend + frontend + shared** | Monorepo simplifica CI/CD e compartilhamento de schemas (P3 KISS) | Fase 5 do OKB v2.1 |
| **`assets/` separado de artefatos** | Imagens são *referenciadas* por artefatos, não são artefatos em si | P3 KISS |
| **`legacy/` gitignored** | Preserva histórico pessoal sem poluir SSOT | P1 (Valor > documentação) |
| **`Makefile` na raiz** | Padroniza comandos (`make up`, `make test`) — reduz curva de aprendizado | P3 KISS + P5 Clean Code |
| **`shared/schemas/`** | Contratos entre backend e frontend (ex: Pydantic + TypeScript types) | Adapter Pattern (glossário §5) |

---

## 4. Mapeamento com Árvore de Artefatos v2.1

| Árvore v2.1 (§5) | Pasta Proposta | Status |
|---|---|---|
| `00. TAP` | `00.TAP/` | ✅ Mapeado |
| `01. Plano de Integração` | `01.PlanoIntegracao/` | ✅ Mapeado |
| `02. Plano de Escopo + EAP` | `02.PlanoEscopo/` | ✅ Mapeado (com subpastas `eap/` e `requisitos/`) |
| `03..08. Demais planos` | `03.PlanoCronograma/` a `08.PlanoRiscos/` | ✅ Mapeados |
| `09. Base de Conhecimento` | `09.BaseConhecimento/` | ✅ Mapeado (com 4 subpastas: ADRs, Lições, Prompts, Runbooks) |
| `10. Plano de Mudanças` | `10.PlanoMudancas/` | ✅ Mapeado |
| `11. Código-Fonte + DER + Diagramas` | `11.src/` + `assets/` | ✅ Mapeado |

---

## 5. Trade-offs Sinalizados

| Trade-off | Opção escolhida | Alternativa | Risco |
|---|---|---|---|
| **Monorepo vs. Polyrepo** | Monorepo (tudo em `COGME/`) | Repos separados para backend/frontend | Complexidade de CI aumenta com escala |
| **Numeração vs. Nomes semânticos** | Numeração (`00.TAP/`) | Nomes puros (`TAP/`) | Perde rastreabilidade com EAP |
| **`docs/` na raiz vs. dentro de `01.PlanoIntegracao/`** | Na raiz (acesso rápido) | Dentro do plano | Pode causar confusão com `09.BaseConhecimento/` |
| **`legacy/` gitignored vs. versionado** | Gitignored (não polui SSOT) | Versionado com tag `deprecated` | Perde histórico de evolução |
| **Docker Compose na raiz vs. em `docker/`** | Na raiz (convenção full-stack) | Em `docker/compose.yml` | Polui visualmente a raiz |

---

## 6. Plano de Ação para Migração

| Passo | Ação | Artefato | DoD |
|---|---|---|---|
| 1 | Criar nova estrutura de pastas vazias | Script `setup_structure.sh` | Todas as pastas `00` a `11` existem |
| 2 | Mover arquivos existentes para novas localizações | Script `migrate_files.sh` | Zero arquivos órfãos na raiz |
| 3 | Atualizar `.gitignore` para ignorar `docker/volumes/` e `legacy/` | `.gitignore v1.1` | Regras validadas |
| 4 | Criar `docker-compose.yml` base (backend + frontend + redis + postgres) | `docker-compose.yml` | `docker compose config` passa |
| 5 | Criar `Makefile` com comandos essenciais | `Makefile` | `make help` lista comandos |
| 6 | Redigir **ADR-003: Estrutura de Diretórios** | `09.1.ADRs/ADR-003.md` | ADR formatado e linkado |
| 7 | Atualizar `README.md` com nova estrutura | `README.md v1.1` | Seção "Estrutura do Projeto" atualizada |
| 8 | Commit + push + validação com Prof. Nivaldo | GitHub | Zero achados críticos no checklist §10 |

---

## 7. Próximos Passos Recomendados

1. **Validar esta estrutura** com você (GP/Redator) antes de executar a migração.
2. **Redigir ADR-003** formalizando esta decisão arquitetural.
3. **Prosseguir com ADR-002** (Definição da Stack Tecnológica) — pendente e bloqueia a Fase 4.
4. **Executar migração** via scripts automatizados (evitar erro humano).
5. **Atualizar TAP v0.9** referenciando a nova estrutura (seção de "Ambiente de Trabalho").

---

**Aguardo seu comando para:**
- (a) Gerar os scripts de migração (`setup_structure.sh` + `migrate_files.sh`)
- (b) Redigir o **ADR-003: Estrutura de Diretórios**
- (c) Criar o `docker-compose.yml` base
- (d) Prosseguir com o **TAP v0.9** ou **ADR-002**
