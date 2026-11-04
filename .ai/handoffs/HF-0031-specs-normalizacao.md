---
id: HF-0031
agent: agent-sdd-specialist
status: ready
created: 2026-11-02
---
# Handoff: Normalização integral do corpus de specs — slug, versionamento, corpo canônico, realocação e pendentes (TA-0031)

## Contexto

Decisão ratificada pelo GP/Humano (2026-11-02, constitution.md Art. 5.1 — autoridade de
outorga/ratificação/promulgação outorgada e registrada em ledger no entry TA-0030): normalizar
TODO o corpus de `./.ai/specs/` — padronizar o corpo das specs com todas as camadas
fundamentais, normatizar nomenclatura para o slug `spec_id-specname.spec.md`, versionar todas
as specs, realocar o que não for spec para a estrutura correspondente e listar as specs
pendentes de criação.

Estado verificado (2026-11-02): 11 arquivos em `.ai/specs/` — 3 com sufixo `.spec.md`
(`000-SDD_CONF-memory.spec.md`, `backend-mvp-v1.spec.md`, `container-layers-v1.spec.md`
Status 0.2.0 pós-TA-0030); 2 com frontmatter `spec_id:` mas sem sufixo
(`constitution-round-1-proposta.md`, `requisitos-review-round-1.md`); 3 VAZIOS 0 B
(`requisitos.md`, `tap.md`, `eap.md`); 1 taxonomy (`kb-taxonomy.md`); 1 input canônico
(`input-canonico-v4.1.1.md`); 1 changelog AFA (`afa-changelog.md`).

## Tarefa

1. **Inventário e classificação** de cada arquivo de `.ai/specs/`: `spec` | `non-spec` |
   `pinned`, com evidência de referência (grep de entradas) e destino/justificativa.
2. **Template canônico de corpo** (camadas fundamentais obrigatórias), derivado do estilo de
   `backend-mvp-v1.spec.md` + `container-layers-v1.spec.md` e do ciclo Art. 6:
   (a) cabeçalho — `spec_id`, versão, status, custódia, datas, handoff de origem;
   (b) Contexto/origem; (c) Resolução de conflitos (quando aplicável);
   (d) corpo de decisões/requisitos/contratos do domínio; (e) Critérios de aceite/testes;
   (f) Rastreabilidade (REQ/ADR/Art./US); (g) Fora de escopo (YAGNI); (h) Changelog.
3. **Renomear TODAS as specs** para slug `spec_id-specname.spec.md` (kebab-case; `spec_id`
   sequencial proposto por você com justificativa de precedente — o frontmatter atual usa
   `spec_id: <nome>-1`; o repo usa padrões HF-/TA-/ADR-/VIO-NNN). **Versionar todas**
   (versão explícita no cabeçalho; bump inicial nas que não têm; preservar 0.2.0 do
   container-layers). Não regressar a amenda TA-0030 (proxy aceito e mantido).
4. **Aplicar o template** a cada spec: preservar TODO conteúdo existente (decisões não se
   reescrevem); lacunas de conteúdo = seção declarada `UNKNOWN - verify`, nunca inventada.
5. **Realocar não-specs** para a estrutura correspondente (`docs/planos/`, `docs/analise/`,
   `docs/decisoes/`, `docs/conhecimento/` — escolha justificada por conteúdo), ATUALIZANDO
   todas as referências vivas. Arquivo ambíguo (papel incerto no ciclo SDD): NÃO mover —
   classifique `pinned/ambiguous` e justifique.
6. **Lista de specs PENDENTES de criação**: derive de REQ-01..15, `docs/planos/plano-granular/plano-producao-agentes.md`
   (ondas), TAP/EAP, ADRs, gaps conhecidos (G-01..G-08, GAP-01..07 das reviews) e domínios
   sem spec; cada item COM citação de origem (sem invenção). Inclua os placeholders vazios
   `requisitos.md`/`tap.md`/`eap.md` como "existentes, conteúdo pendente". Entregue em
   `docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md` + resumo compacto na parcela.
7. **MANIFEST** em `.ai/specs/MANIFEST.md`: inventário (arquivo → classificação → nome novo
   → versão → refs atualizadas), mapa de redirecionamento old→new (resolve referências
   históricas), justificativa de cada `pinned` e de cada realocação.

## Regras de integridade de referência (fail-closed)

- **NUNCA editar** (imutáveis): `constitution.md`; `.ai/agents/registry.yaml` (inclusive
  comentários); `.opencode/agents/*` (forja AFA-ULTIMATE exclusiva, Art. 4.1);
  `.ai/handoffs/*` e `.ai/agents/ledger.yaml` (histórico append-only);
  `docs/decisoes/*` (ADRs — canon de decisão, Art. 2); `docs/auditorias/*` (evidência de
  auditoria). Referências antigas nesses arquivos ficam resolvidas pelo mapa do MANIFEST.
- **EDITAR permitido**: `.ai/specs/**`; referências vivas em `docs/planos/`, `docs/conhecimento/`,
  `docs/analise/`, `README.md`, `tests/`, `scripts/`, `.github/` — atualizar paths antigos.
- **PINADOS (não mover, não renomear)** — referenciados por prompts de agentes imutáveis:
  `afa-changelog.md` (canon AFA §15), `requisitos.md`, `tap.md`, `eap.md`, `kb-taxonomy.md`.
  Classifique-os no MANIFEST com a evidência do grep.
- Se uma referência viva não puder ser atualizada sem violar imutáveis: NÃO renomeie esse
  arquivo — registre `pending_rename` no MANIFEST e justifique (nunca quebre link canônico).

## Critérios de Aceite

- [ ] Template canônico definido no MANIFEST com todas as camadas fundamentais (a–h)
- [ ] TODAS as specs renomeadas para `spec_id-specname.spec.md` e com versão explícita no cabeçalho
- [ ] Cada spec contém as camadas fundamentais aplicáveis; conteúdo pré-exervado; lacunas `UNKNOWN - verify`
- [ ] Amenda TA-0030 preservada (proxy aceito e mantido, versão 0.2.0+)
- [ ] Não-specs realocados com referências vivas atualizadas; nenhum link quebrado
- [ ] Imutáveis intocados (git diff sem constitution/registry/.opencode/agents/handoffs/ledger/ADRs/auditorias)
- [ ] MANIFEST com inventário, mapa old→new e justificativas pinned/realocação
- [ ] `docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md` emitido, cada pendência com citação de origem
- [ ] `python3 -m pytest tests/agents/ -q` sem NOVAS falhas (baseline: 4 failed / 149 passed / 1 skipped pré-existentes)
- [ ] `python3 scripts/sync_agent_registry.py --check` permanece exit 0

## Restrições

- **Árvore de trabalho instável (realocação humana não-commitada, 2026-11-02 18:12 UTC):**
  21 deleções unstaged em `docs/planos/` com conteúdo movido para `docs/planos/legacy/` e
  `docs/planos/plano-granular/` (untracked). NÃO desfaça, NÃO stage, NÃO commit esses
  movimentos (Art. 5 — decisão do Humano). Resolva caminhos VIVOS via `ls`/`find`/`grep` —
  nunca confie em caminhos antigos de memória; referências vivas apontem para o caminho real.
- Escopo de edição: `.ai/specs/**` (inclui MANIFEST), destinos de realocação de não-specs,
  referências vivas listadas, `docs/analise/LISTA-SPECS-PENDENTES-2026-11-02.md`.
  Nenhum arquivo de código/compose/Dockerfile/workflow é alterado.
- Narrativa PT-BR; identificadores/caminhos EN; citação `arquivo:linha`; lacunas
  `UNKNOWN - verify`; sem invenção de status, datas ou métricas.
- Retorno: parcel half-duplex (schema 6), `dod` só com todos os critérios verificados;
  na `notes`, incluir o resumo da lista de pendentes (≤5 linhas). Resposta final ≤1200 tokens
  (conteúdo longo vai aos ARQUIVOS).
