# Relatório Analítico: Persistência e Recuperação de Invoices

**Data:** 2026-11-14  
**Autor:** Análise Arquitetural  
**Referência:** ADR-016 D4 (RAT-2026-11-05-A16-D4) = PERSISTIR com rota de erase  
**Status:** Para decisão CCB/PO

---

## 1. Estado Atual (AS-IS)

### 1.1 Decisões Ratificadas
| Decisão | Instrumento | Status |
|---------|-------------|--------|
| **D1 (Persistência invoice)** | ADR-016 emenda D4, RAT-2026-11-05-A16-D4 | **RATIFICADA = PERSISTIR com rota de erase** |
| **SPEC-007 (modelo de dados)** | HF-0608, status: `ratificada` | Contrato canônico emitido, 25+ campos |
| **SPEC-015 (LGPD produto)** | HF-0616, D1 ratificada, D2-D7 pendentes | D1 = PERSISTIR; D2-D7 aguardam CCB/PO |

### 1.2 Implementação Atual (Código)
- **Endpoint único:** `POST /v1/invoice` → gera PDF *on-the-fly*, **não persiste**
- **Contrato vigente (spec-004:126):** "invoice nunca é persistida" — **superado por ADR-016 D4**
- **Banco:** Apenas migração `0001_create_fx_quotes.py` existe; **tabela `invoices` não criada**
- **Frontend:** Formulário de geração (`invoice_form.html`) → download direto do PDF
- **LGPD:** Logs sem PII/valores (spec-004:126, critério herdado como D5 em spec-015)

### 1.3 Gaps Identificados
| Gap | Descritor | Impacto |
|-----|-----------|---------|
| **GAP-01** | Nenhuma rota de listagem/recuperação de invoices | Usuário não acessa histórico |
| **GAP-02** | Tabela `invoices` não existe no banco | Persistência declarada mas não implementada |
| **GAP-03** | Rota de **erase (DELETE)** obrigatória (LGPD art. 18) não existe | Bloqueador legal se persistir |
| **GAP-04** | Políticas de retenção (D6) e base legal (D2, D3) não ratificadas | Insegurança jurídica |
| **GAP-05** | CR-006 (ciclo rascunho/finalizada) e CR-007 (bilíngue) pendentes | Funcionalidades condicionais não decididas |

---

## 2. Análise das Opções Arquiteturais

### Opção A: **Persistência Mínima (Snapshot Completo)**
Armazena **todos os campos** da invoice (conforme SPEC-007 §3.1) na tabela `invoices`. O PDF é **re-renderizado** a partir dos dados persistidos na recuperação.

| Aspecto | Detalhamento |
|---------|-------------|
| **Armazenamento** | 25+ colunas: identidade, partes, regime, valores calculados, cotação (rate, source, quoted_at, bulletin), datas, descrição, dados bancários (opcionais) |
| **Recuperação** | `GET /v1/invoices/{id}` → renderiza PDF via template Jinja2 (mesmo `invoice.html`) |
| **Listagem** | `GET /v1/invoices` paginado, ordenado por `created_at DESC`, filtro por status/cliente/período |
| **Vantagens** | Reprodutibilidade total; auditoria fiel; LGPD: erase apaga 1 linha; atende US-016/017 (status draft/finalized) |
| **Riscos** | Volume de dados maior; duplicação de valores calculados (mitigado: identity check `gross_brl - spread_brl - iof_brl == net_brl`); migração complexa |

### Opção B: **Persistência de Entrada + Reprocessamento (Source of Truth = Request)**
Armazena **apenas o payload de entrada** (`InvoiceRequest` serializado) + metadados (cotação usada, `created_at`). Na recuperação, **recalcula no servidor** (conforme spec-004 §6) e renderiza.

| Aspecto | Detalhamento |
|---------|-------------|
| **Armazenamento** | JSONB `request_payload` + colunas de controle (`id`, `invoice_number`, `created_at`, `quote_rate`, `quote_source`, `quoted_at`, `bulletin`, `stale`) |
| **Recuperação** | Desserializa → roda `simulate()` com cotação **original** (guardada) → renderiza PDF |
| **Listagem** | Igual à Opção A, mas valores exibidos vêm de view computada ou recálculo *on-demand* |
| **Vantagens** | Menos colunas; valores sempre consistentes com regra de negócio vigente; minimização natural (não guarda dados bancários se não enviados) |
| **Riscos** | **Quebra reprodutibilidade** se regra de cálculo mudar (ex.: arredondamento, IOF); cotação "original" deve ser persistida fielmente; LGPD: erase apaga payload inteiro |

### Opção C: **Híbrida (Snapshot de Valores + Payload de Entrada)**
Persiste **tabela canônica (Opção A)** + **JSONB `request_snapshot`** opcional para auditoria/debug. Recuperação usa snapshot de valores (garante reprodutibilidade), payload serve só para inspeção.

| Aspecto | Detalhamento |
|---------|-------------|
| **Armazenamento** | Tabela `invoices` completa (SPEC-007) + coluna `request_snapshot JSONB NULL` |
| **Recuperação** | Prioriza colunas tipadas; `request_snapshot` só leitura admin/auditoria |
| **Vantagens** | Melhor dos dois mundos: reprodutibilidade + rastreabilidade de entrada |
| **Riscos** | Duplicação controlada; mais storage; complexidade de sincronia |

---

## 3. Avaliação Comparativa

| Critério | Opção A (Snapshot Completo) | Opção B (Reprocessamento) | Opção C (Híbrida) |
|----------|----------------------------|---------------------------|-------------------|
| **Reprodutibilidade (spec-007 §3.4)** | ✅ Garantida por colunas tipadas | ⚠️ Dependente de regra estável | ✅ Garantida |
| **LGPD Minimização (P-04, art. 6º III)** | ⚠️ Guarda tudo (incl. bancários opcionais) | ✅ Guarda só o enviado | ⚠️ Guarda tudo + snapshot opcional |
| **Rota Erase (LGPD art. 18)** | ✅ `DELETE 1 linha` | ✅ `DELETE 1 linha` | ✅ `DELETE 1 linha` |
| **Retenção/Backup (D6)** | ✅ Linha única, clara | ✅ Linha única, clara | ⚠️ Duas fontes |
| **Implementação (DDL Alembic)** | Média (25+ colunas, CHECKs, UNIQUE) | Baixa (JSONB + poucas colunas) | Alta (ambas) |
| **Performance Listagem** | ✅ Índices em colunas tipadas | ⚠️ JSONB precisa GIN/extração | ✅ Índices tipados |
| **US-016/017 (draft/finalized, clone)** | ✅ Nativo (coluna `status`) | ⚠️ Precisa coluna extra no JSONB | ✅ Nativo |
| **CR-007 (bilíngue: locale, country_code)** | ✅ Colunas dedicadas | ⚠️ No JSONB | ✅ Colunas dedicadas |
| **Auditoria/Compliance** | ✅ Valores explícitos, queryáveis | ⚠️ Precisa parse JSONB | ✅ Ambos disponíveis |

---

## 4. Recomendação: **Opção A (Snapshot Completo) com Adaptações LGPD**

### Justificativa
1. **Conformidade com SPEC-007 ratificada** — o contrato de dados canônico **é** a tabela `invoices` com 25+ colunas tipadas (§3.1). Opção B desvia do modelo ratificado.
2. **Reprodutibilidade obrigatória** — spec-007 §3.4 exige que "colunas de valores casam com o reprocesso". Snapshot tipado garante isso sem depender de código.
3. **US-016/017 e CR-006/007** — ciclos de estado, clonagem, bilíngue exigem colunas estruturadas (`status`, `locale`, `client_country_code`, `finalized_at`, `supersedes_invoice_id`).
4. **Performance de listagem** — índices B-tree em `created_at`, `invoice_number`, `issuer_tax_id_digits`, `status` superam JSONB.
5. **Auditoria/Compliance** — valores em colunas tipadas são queryáveis por SQL padrão (relatórios, fiscalização).

### Adaptações LGPD Obrigatórias (condicionantes D2-D6)
| Condicionante | Ação Requerida |
|---------------|----------------|
| **D2** (art. 4º I) | Definir se tratamento é "exclusivamente particular" → afeta base legal |
| **D3** (art. 7º V) | Ratificar base legal para dados de terceiros (cliente) |
| **D4** (inventário mínimo) | **Confirmar quais campos são obrigatórios vs NULLable** (endereço, bancários) |
| **D5** (logs sem PII) | Já implementado (spec-004:126) — manter |
| **D6** (retenção + erase) | **Definir política de retenção** (ex.: 5 anos fiscal + 6 meses pós-contrato) + implementar `DELETE /v1/invoices/{id}` |
| **D7** (drift LISTA) | Corrigir LISTA-SPECS-PENDENTES.md antes de novas referências |

---

## 5. Especificação da Solução (Para Complementar SPEC-007)

### 5.1 Rotas de API a Adicionar (spec-004 §9)
| Rota | Método | Descrição | Spec Ref |
|------|--------|-----------|----------|
| `/v1/invoices` | GET | Listagem paginada (filtros: status, cliente, período) | Nova |
| `/v1/invoices/{id}` | GET | Recupera invoice → renderiza PDF (Content-Disposition: attachment) | Nova |
| `/v1/invoices/{id}` | DELETE | Rota de erase (LGPD art. 18) — **obrigatória se D1=PERSISTIR** | Spec-007 §3.6, Spec-015 CP-3 |
| `/v1/invoices/{id}/clone` | POST | Clona finalizada → novo rascunho (US-017, CR-006) | Condicional CR6-D01 |
| `/v1/invoices/{id}/finalize` | POST | Transição draft → finalized (imutável, `finalized_at`) | Condicional CR6-D01 |

### 5.2 Modelo de Dados (Estende SPEC-007 §3.1)
```sql
-- Adições para ciclo de vida (CR-006) e bilíngue (CR-007)
ALTER TABLE invoices ADD COLUMN IF NOT EXISTS
    owner_user_id        BIGINT NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
    client_id            BIGINT REFERENCES clients(id) ON DELETE RESTRICT,
    simulation_id        BIGINT REFERENCES simulations(id) ON DELETE RESTRICT,
    status               VARCHAR(16) NOT NULL DEFAULT 'finalized'
        CHECK (status IN ('draft','finalized')),
    locale               VARCHAR(8) NOT NULL DEFAULT 'pt-BR'
        CHECK (locale IN ('pt-BR','en')),
    client_country_code  CHAR(2),
    finalized_at         TIMESTAMPTZ,
    supersedes_invoice_id BIGINT REFERENCES invoices(id) ON DELETE SET NULL,
    -- Índices para listagem
    CREATE INDEX ix_invoices_owner_created ON invoices (owner_user_id, created_at DESC);
    CREATE INDEX ix_invoices_status ON invoices (status);
    CREATE INDEX ix_invoices_client ON invoices (client_id);
```

> **Nota:** `users`, `clients`, `simulations` são tabelas de CR-002/CR-005/CR-006 — dependência de ratificação CCB.

### 5.3 Frontend — Página de Lista de Invoices
| Componente | Descrição |
|------------|-----------|
| **Rota** | `/invoices` (protegida por sessão/owner) |
| **Tabela** | Colunas: Número, Data, Cliente, Regime, Valor Líquido, Status, Ações |
| **Filtros** | Status (rascunho/finalizada), Período, Cliente (autocomplete) |
| **Ações por linha** | Visualizar PDF, Clonar (se finalizada), Excluir (erase — confirmação LGPD) |
| **Estado vazio** | "Nenhuma invoice gerada. Crie sua primeira invoice." + botão CTA |
| **Paginação** | Server-side, 20 por página, ordenação `created_at DESC` |

### 5.4 Recuperação de Invoice (Fluxo)
```
GET /v1/invoices/{id}
  → Verifica owner_user_id = sessão atual (autorização)
  → Busca linha em invoices (JOIN clients se client_id)
  → Se status = draft: permite edição (PUT /v1/invoices/{id})
  → Renderiza template (invoice_pt_br.html ou invoice_en.html conforme locale)
  → Retorna PDF com Content-Disposition: attachment; filename="invoice-{number}.pdf"
  → Cache-Control: no-store
```

---

## 6. Decisões Bloqueadoras (Requerem CCB/PO Antes de Implementar)

| ID | Decisão | Responsável | Prazo Sugerido |
|----|---------|-------------|----------------|
| **DEC-01** | Ratificar D2 (art. 4º I — particular vs econômico) | CCB/PO + Jurídico | Imediato |
| **DEC-02** | Ratificar D3 (base legal art. 7º V para dados de cliente) | CCB/PO + Compliance | Imediato |
| **DEC-03** | Ratificar D4 (inventário mínimo: endereço obrigatório? bancários?) | CCB/PO + Business | Imediato |
| **DEC-04** | Definir política de retenção D6 (ex.: 5a fiscal + 6m pós-contrato) | CCB/PO + Compliance | Imediato |
| **DEC-05** | Ratificar US-016/017 (ciclo draft/finalized, clone) — CR6-D01 | CCB/PO | Antes de 16/11 |
| **DEC-06** | Solução de numeração (sem Sequence) — CR6-D02 | agent-dba + CCB | Antes de 16/11 |
| **DEC-07** | Ratificar bilíngue PT-BR/EN (CR7-D01) | CCB/PO | Antes de 16/11 |

---

## 7. Plano de Implementação Sugerido (Pós-Decisões)

| Fase | Entregável | Esforço Estimado | Dependências |
|------|------------|------------------|--------------|
| **F1** | Migration Alembic `invoices` (upgrade/downgrade + CHECKs, UNIQUE, FKs) | 2-3 dias | DEC-01..04, DEC-05 |
| **F2** | Repository Protocol + SqlAlchemyInvoiceRepository | 1-2 dias | F1 |
| **F3** | Rotas API: LIST, GET (PDF), DELETE (erase) | 2-3 dias | F2 |
| **F4** | Rotas condicionais: FINALIZE, CLONE (se DEC-05 ratificado) | 1-2 dias | F3, DEC-05 |
| **F5** | Frontend: Página `/invoices` (listagem, filtros, ações) | 2-3 dias | F3 |
| **F6** | Testes: Property test (persistência × reprocesso), LGPD erase test, integração | 2 dias | F3, F5 |
| **F7** | Documentação: Atualizar spec-004 §9, spec-007 §3.8, spec-015 CP-3 | 1 dia | F1-F6 |

**Total estimado:** 11-16 dias úteis após decisões CCB.

---

## 8. Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
|-------|---------------|---------|-----------|
| Decisões D2-D6 não ratificadas a tempo | Alta | Bloqueio total | Escalar para GP Leonardo (CCB membro único) já na 2026-11-14 |
| Migração Alembic falha em downgrade | Média | Rollback difícil | Testar upgrade/downgrade em CI PostgreSQL dedicado |
| Performance de listagem com muitos registros | Baixa (MVP single-user) | Degradação UX | Índices compostos `(owner_user_id, created_at DESC)` desde F1 |
| Vazamento de PII em logs na rota de persistência | Baixa (já controlado) | LGPD | Reutilizar critério D5 (spec-004:126) + teste automatizado CP-2 |
| Inconsistência entre snapshot e reprocesso | Baixa (identity check) | Auditoria | Property test obrigatório em F6 |

---

## 9. Conclusão e Próximos Passos

**A decisão D1 = PERSISTIR (ADR-016 D4) exige implementação concreta.** O estado atual (apenas geração de PDF *on-the-fly*) **não cumpre** a decisão ratificada.

**Recomendação imediata:**
1. **Submeter decisões DEC-01 a DEC-07 ao CCB/PO** (GP Leonardo) **hoje** — são bloqueadoras.
2. **Escolher Opção A (Snapshot Completo)** como base técnica — alinhada à SPEC-007 ratificada.
3. **Iniciar Migration Alembic (F1)** assim que D4 (inventário mínimo) for ratificado — é o caminho crítico.
4. **Paralelamente:** Preparar test plan para property test (reprocesso = persistência) e LGPD erase test.

**Artefatos a Atualizar Pós-Implementação:**
- `spec-004-backend-mvp-v1.spec.md` §9 (rotas de listagem/recuperação/erase)
- `spec-007-invoice-data-model-v1.spec.md` §3.8 (resolver UNKNOWNs 3 e 4: cotação persistida + status)
- `spec-015-lgpd-produto-proposta-v1.spec.md` CP-3 (teste de erase operante)
- `constitution.md` Art. 1.2 (admitir histórico de invoices e ciclo de vida)

---

**Fim do Relatório**  
*Este relatório não promove decisões; subsidia a deliberação do CCB/PO nos termos do Art. 5.1 da Constituição.*