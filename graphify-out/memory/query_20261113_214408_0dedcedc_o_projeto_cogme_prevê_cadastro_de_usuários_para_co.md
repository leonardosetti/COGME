---
type: "query"
date: "2026-11-13T21:44:08.851484+00:00"
question: "O projeto COGME prevê cadastro de usuários para consistência de dados do trabalho e histórico de invoices correto?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["3.1 Entidade `invoices` (se e somente se D1 = persistir)", "post_invoice()", "spec-007-invoice-data-model-v1.spec.md"]
---

# Q: O projeto COGME prevê cadastro de usuários para consistência de dados do trabalho e histórico de invoices correto?

## Answer

Resposta: não, não no contrato atual. A spec-007 prevê persistir invoices e define apenas a tabela invoices, sem users, user_id ou work_id; o cálculo é recalculado no servidor, mas o vínculo de propriedade e o histórico por trabalho não existem. No código atual, a rota POST /v1/invoice apenas devolve PDF e declara que os dados não são persistidos; a única migração presente cria fx_quotes. US-016/US-017 (histórico de estados/clone) são legadas e condicionais, e histórico de simulações está fora de escopo. Expanded from original query via vocab: [user, cadastro, invoice, invoices, trabalho, historico, dados, responsabilidade, pagamento, job, jobs, inconsistencias, auth, identity, ownership, session].

## Outcome

- Signal: useful

## Source Nodes

- 3.1 Entidade `invoices` (se e somente se D1 = persistir)
- post_invoice()
- spec-007-invoice-data-model-v1.spec.md