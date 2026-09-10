# CONFIRMAÇÃO DE INSERÇÃO DA EAP v2.0 NO TAP v1.1

**Emissor:** GP Sênior PMBOK 7ª / PMO (Co-Autor Crítico)  
**Data:** 11/09/2026  
**Status:** ✅ EAP 2.0 consolidada e pronta para inserção

---

## 1. CORREÇÃO DE ENTENDIMENTO — AUTORIA DOS COMENTÁRIOS

✅ **Reconhecido e registrado**: Os comentários inseridos no documento TAP são **decisões estratégicas dos alunos** (Leonardo David Silva Setti e Fabricio de Lima Cabral), não orientações do Prof. Dr. Nivaldo Carletto.

**Fundamentação**: Conforme OKB_COGME_v3.0 §3.1 (Hierarquia de Resolução de Conflitos), os alunos possuem autonomia para tomar decisões durante o desenvolvimento do projeto, desde que alinhadas aos princípios constitutivos (P1-P9) e ao guardrail operacional.

**Ciclo de avaliação do Prof. Dr. Nivaldo Carletto**:
- **Entrega Parcial**: 22/09/2026 (documentação das áreas 1-5 do PMBOK 6ª)
- **Entrega Final**: Novembro/Dezembro 2026 (MVP funcional + documentação consolidada)

**Impacto no processo**: A submissão formal ao Prof. Nivaldo ocorrerá apenas em 22/09/2026, conforme planejamento. Até lá, os alunos mantêm autonomia para refinar o TAP conforme decisões estratégicas internas.

---

## 2. CONFIRMAÇÃO DA EAP v2.0 — PRONTA PARA INSERÇÃO

✅ **EAP v2.0 consolidada** conforme análise arquitetural v2.0 e decisões estratégicas dos alunos.

**Mudanças aplicadas**:
- ✅ Remoção de N1.1 (TAP) — separação ontológica TAP ≠ EAP
- ✅ Remoção de N5.6 (Execução Kanban) — fundido com N1.6
- ✅ Remoção de N6.3 (Testes de Performance) — YAGNI
- ✅ Remoção de N7.2 (Deploy Manual Documentado) — YAGNI (sem N8)
- ✅ **Remoção completa da Fase N8 (Implantação/Deploy)** — MVP acadêmico não exige produção
- ✅ Remoção de N9.4 (Cerimônias com Prof. Nivaldo) — Kanban assíncrono
- ✅ Remoção de N11.1 (CCB formal) — label `change-request` no GitHub basta
- ✅ Remoção de N12.2 (Manual do Usuário) — README + docs técnicas bastam
- ✅ **Adição de N6.3 (Aplicação de Ferramentas da Qualidade: 12 PDCAs + Ishikawa 6M)** — atendimento à demanda acadêmica
- ✅ Substituição de "Cache Redis" por "Cache" (genérico) — stack canônica usa SQLite

**Resultado líquido**:
- Fases Nível 1: 13 → **12** (-1)
- Pacotes Nível 2: 48 → **37** (-11)
- Redução de escopo: **23%** (alinhamento YAGNI + MVP acadêmico)

---

## 3. EAP v2.0 — ESTRUTURA ORGANIZADA CONFORME PMO

### 3.1. NÍVEL 0 — RAIZ

| ID | Nó | Descrição | Macro-Fase |
|---|---|---|---|
| N0 | — | COGME — Conversor de Ganhos em Moeda Estrangeira | — |

### 3.2. NÍVEIS 1 E 2 — FASES OBRIGATÓRIAS (MVP Acadêmico)

| ID Nível 1 | Fase (Nível 1) | ID Nível 2 | Pacote de Trabalho (Nível 2) | Macro-Fase |
|---|---|---|---|---|
| **N1** | **1. Iniciação e Planejamento** | N1.2 | 1.2. Identificação de Stakeholders | MF1 |
| | | N1.3 | 1.3. Planos de Gerenciamento | MF1 |
| | | N1.4 | 1.4. Plano da Qualidade | MF1 |
| | | N1.5 | 1.5. Política de Licenciamento FOSS | MF1 |
| | | N1.6 | 1.6. Definição do Backlog e Kanban | MF1 |
| **N2** | **2. Levantamento de Requisitos** | N2.1 | 2.1. Requisitos Funcionais | MF1 |
| | | N2.2 | 2.2. Requisitos Não Funcionais | MF1 |
| | | N2.3 | 2.3. Casos de Uso e Histórias de Usuário | MF1 |
| **N3** | **3. Modelagem e Prototipação** | N3.1 | 3.1. Arquitetura da Solução | MF1 |
| | | N3.2 | 3.2. Protótipo UX/UI | MF1 |
| | | N3.3 | 3.3. Modelagem de Dados (DER) | MF1 |
| **N4** | **4. Configuração de Ambiente** | N4.1 | 4.1. Seleção e Validação da Stack FOSS | MF1 |
| | | N4.2 | 4.2. Repositório Git + CI/CD | MF1 |
| | | N4.3 | 4.3. Setup Local e Homologação | MF1 |
| | | N4.4 | 4.4. Auditoria de Licenças | MF1 |
| **N5** | **5. Desenvolvimento do Sistema** | N5.1 | 5.1. Backend — Lógica de Negócio | MF2 |
| | | N5.2 | 5.2. Backend — API de Câmbio + Cache | MF2 |
| | | N5.3 | 5.3. Frontend — Interface e Simulações | MF2 |
| | | N5.4 | 5.4. Módulo PDF (WeasyPrint) | MF2 |
| | | N5.5 | 5.5. SDD com IA (Prompts + Revisão) | MF2 |
| **N6** | **6. Garantia da Qualidade** | N6.1 | 6.1. Testes Unitários/Integração (≥ 80%) | MF2 |
| | | N6.2 | 6.2. Testes de Aceitação (UAT) | MF2 |
| | | **N6.3** | **6.3. Aplicação de Ferramentas da Qualidade (12 PDCAs + Ishikawa 6M)** | MF2 |
| **N7** | **7. DevOps e CI/CD** | N7.1 | 7.1. Pipeline CI (lint + testes) | MF2 |
| **N9** | **9. Comunicação** | N9.1 | 9.1. Matriz de Comunicação (RACI) | MF1 |
| | | N9.2 | 9.2. Canais Oficiais (GitHub, e-mail) | MF1 |
| **N10** | **10. Base de Conhecimento** | N10.1 | 10.1. ADRs (decisões arquiteturais) | MF1 |
| | | N10.2 | 10.2. Lições Aprendidas Contínuas | MF1 |
| | | N10.3 | 10.3. Catálogo de Prompts SDD | MF1 |
| **N11** | **11. Gestão de Mudanças** | N11.2 | 11.2. Registro de Solicitações de Mudança | MF2 |
| | | N11.3 | 11.3. Label `change-request` no GitHub | MF2 |
| | | N11.4 | 11.4. Aprovação e Versionamento | MF2 |
| **N12** | **12. Documentação do Projeto** | N12.1 | 12.1. Documentação Técnica (Arquitetura, APIs) | MF3 |
| | | N12.4 | 12.4. Consolidação da Documentação Parcial | MF3 |
| **N13** | **13. Encerramento** | N13.1 | 13.1. Lições Aprendidas Finais | MF3 |
| | | N13.2 | 13.2. Verificação SMART | MF3 |
| | | N13.3 | 13.3. Apresentação Final + Aceite | MF3 |

**TOTAL: 12 fases Nível 1 + 37 pacotes Nível 2**

### 3.3. Lista Hierárquica Aninhada

```
N0: COGME — Conversor de Ganhos em Moeda Estrangeira
│
├── N1: 1. Iniciação e Planejamento [MF1]
│   ├── N1.2: 1.2. Identificação de Stakeholders
│   ├── N1.3: 1.3. Planos de Gerenciamento
│   ├── N1.4: 1.4. Plano da Qualidade
│   ├── N1.5: 1.5. Política de Licenciamento FOSS
│   └── N1.6: 1.6. Definição do Backlog e Kanban
│
├── N2: 2. Levantamento de Requisitos [MF1]
│   ├── N2.1: 2.1. Requisitos Funcionais
│   ├── N2.2: 2.2. Requisitos Não Funcionais
│   └── N2.3: 2.3. Casos de Uso e Histórias de Usuário
│
├── N3: 3. Modelagem e Prototipação [MF1]
│   ├── N3.1: 3.1. Arquitetura da Solução
│   ├── N3.2: 3.2. Protótipo UX/UI
│   └── N3.3: 3.3. Modelagem de Dados (DER)
│
├── N4: 4. Configuração de Ambiente [MF1]
│   ├── N4.1: 4.1. Seleção e Validação da Stack FOSS
│   ├── N4.2: 4.2. Repositório Git + CI/CD
│   ├── N4.3: 4.3. Setup Local e Homologação
│   └── N4.4: 4.4. Auditoria de Licenças
│
├── N5: 5. Desenvolvimento do Sistema [MF2]
│   ├── N5.1: 5.1. Backend — Lógica de Negócio
│   ├── N5.2: 5.2. Backend — API de Câmbio + Cache
│   ├── N5.3: 5.3. Frontend — Interface e Simulações
│   ├── N5.4: 5.4. Módulo PDF (WeasyPrint)
│   └── N5.5: 5.5. SDD com IA (Prompts + Revisão)
│
├── N6: 6. Garantia da Qualidade [MF2]
│   ├── N6.1: 6.1. Testes Unitários/Integração (≥ 80%)
│   ├── N6.2: 6.2. Testes de Aceitação (UAT)
│   └── N6.3: 6.3. Aplicação de Ferramentas da Qualidade (12 PDCAs + Ishikawa 6M) [NOVO]
│
├── N7: 7. DevOps e CI/CD [MF2]
│   └── N7.1: 7.1. Pipeline CI (lint + testes)
│
├── N9: 9. Comunicação [MF1]
│   ├── N9.1: 9.1. Matriz de Comunicação (RACI)
│   └── N9.2: 9.2. Canais Oficiais (GitHub, e-mail)
│
├── N10: 10. Base de Conhecimento [MF1]
│   ├── N10.1: 10.1. ADRs (decisões arquiteturais)
│   ├── N10.2: 10.2. Lições Aprendidas Contínuas
│   └── N10.3: 10.3. Catálogo de Prompts SDD
│
├── N11: 11. Gestão de Mudanças [MF2]
│   ├── N11.2: 11.2. Registro de Solicitações de Mudança
│   ├── N11.3: 11.3. Label `change-request` no GitHub
│   └── N11.4: 11.4. Aprovação e Versionamento
│
├── N12: 12. Documentação do Projeto [MF3]
│   ├── N12.1: 12.1. Documentação Técnica (Arquitetura, APIs)
│   └── N12.4: 12.4. Consolidação da Documentação Parcial
│
└── N13: 13. Encerramento [MF3]
    ├── N13.1: 13.1. Lições Aprendidas Finais
    ├── N13.2: 13.2. Verificação SMART
    └── N13.3: 13.3. Apresentação Final + Aceite
```

### 3.4. Mapeamento com Macro-Fases Temporais

| Macro-Fase | Período | Fases da EAP Incluídas | Total de Pacotes |
|---|---|---|---|
| **MF1: Fundação** | 01/09 – 30/09/2026 | 1, 2, 3, 4, 9, 10 | **20 pacotes** |
| **MF2: Construção** | 01/10 – 15/11/2026 | 5, 6, 7, 11 | **12 pacotes** |
| **MF3: Consolidação** | 16/11 – 15/12/2026 | 12, 13 | **5 pacotes** |
| **TOTAL** | — | 12 fases | **37 pacotes** |

**Regra operacional**: As fases **não são sequenciais** dentro de cada macro-fase. O Kanban (GitHub Projects) permite paralelismo via *pull system* e WIP limits. A EAP é estrutura de decomposição; as macro-fases são agrupamentos temporais para gestão.

### 3.5. Declaração de Rastreabilidade (TAP → EAP v2.0)

| Origem (TAP) | Destino (EAP v2.0) | Domínio PMBOK 7ª |
|---|---|---|
| §3 Objetivos SMART (Produto) | Fases 5, 6, 7 (MVP funcional + qualidade + CI) | Entrega |
| §3 Objetivos SMART (Qualidade) | Fases 6 (testes + ferramentas qualidade), 12, 13 | Medição |
| §3 Objetivos SMART (Cronograma) | Macro-fases MF1/MF2/MF3 | Abordagem de Desenvolvimento |
| §3 Objetivos SMART (Inovação) | Fases 5.5, 10.3 (SDD com IA) | Trabalho do Projeto |
| §4 Escopo (implícito) | Todas as 12 fases obrigatórias | Planejamento |
| §8 Restrições (FOSS) | Fases 1.5, 4.1, 4.4 | Abordagem de Desenvolvimento |
| §9 Premissas (LLM/SDD) | Fases 5.5, 10.3 | Trabalho do Projeto |
| §10 Riscos | Fase 11 (Gestão de Mudanças) | Incerteza |

**Verificação de completude**: 100% dos objetivos SMART do TAP §3 possuem ao menos uma fase da EAP v2.0 associada.

---

## 4. INSTRUÇÕES DE INSERÇÃO NO TAP v1.1

### 4.1. Procedimento Operacional

1. **Abrir** o arquivo `Termo de Abertura do Projeto v1_opngoing.docx`
2. **Localizar** a seção §4 atual ("ESTRUTURA ANALÍTICA DO PROJETO (EAP/WBS)")
3. **Selecionar** todo o conteúdo da seção §4 (desde o título até o final da Declaração de Rastreabilidade)
4. **Substituir** pelo texto da Seção 3 deste artefato
5. **Salvar** como `Termo de Abertura do Projeto v1.1.docx` (incrementar versão)
6. **Atualizar** o Controle de Versões (§0) com:
   - Versão: 1.1
   - Data: 11/09/2026
   - Autores: Leonardo David Silva Setti, Fabricio de Lima Cabral
   - Notas: "EAP v2.0: remoção de N1.1 (TAP), remoção da Fase N8 (Deploy), adição de N6.3 (Ferramentas da Qualidade), redução de 48 para 37 pacotes (alinhamento YAGNI + MVP acadêmico)"

### 4.2. Verificação Pós-Inserção

- [ ] Tabela de Níveis 1 e 2 contém 37 linhas de pacotes (sem contar cabeçalhos)
- [ ] Lista hierárquica aninhada espelha a tabela (mesmos IDs e descrições)
- [ ] Total de pacotes por macro-fase: MF1=20, MF2=12, MF3=5, TOTAL=37
- [ ] Não há menção a "Redis" (substituído por "Cache")
- [ ] Não há Fase N8 (Implantação/Deploy)
- [ ] Não há N1.1 (TAP) na EAP
- [ ] N6.3 está presente com descrição "Aplicação de Ferramentas da Qualidade (12 PDCAs + Ishikawa 6M)"
- [ ] Não há N7.2, N9.4, N11.1, N12.2
- [ ] Fase N11 contém apenas N11.2, N11.3, N11.4 (sem N11.1)

---

## 5. PRÓXIMOS PASSOS (Sequência de Redação do TAP v1.1)

Após a inserção da seção §4 (EAP v2.0), prosseguir com as seções pendentes na ordem de prioridade:

| Prioridade | Seção | Ação | Prazo |
|---|---|---|---|
| 🔴 P0 | §5 | Redigir "Principais requisitos das entregas" | 11/09 |
| 🔴 P0 | §9 | Redigir "Premissas" (8 premissas fundamentais) | 11/09 |
| 🔴 P0 | §10 | Redigir "Riscos" (Top 5 riscos) | 11/09 |
| 🔴 P0 | §11 | Redigir "Orçamento do Projeto" (R$ 0,00 + justificativa) | 11/09 |
| 🟠 P1 | §6 | Preencher "Marcos" com datas concretas | 11/09 |
| 🟠 P1 | §7 | Corrigir nomes em "Partes interessadas" | 11/09 |
| 🟢 P3 | §1, §2, §3, §8 | Revisões textuais + reescrever item 1.c (hierarquia PMBOK 7ª → 6ª) | 11/09 |
| 🟢 P3 | Global | Remover comentários de revisão + padronização textual | 11/09 |

**Marco de submissão**: TAP v1.1 completo até 22/09/2026, 09:00 para submissão ao Prof. Dr. Nivaldo Carletto.

---

## 6. TRADE-OFFS SINALIZADOS

| Trade-off | Risco | Mitigação |
|---|---|---|
| Remoção de N8 (Deploy) | Percepção de "MVP incompleto" | Justificar via escopo acadêmico; UAT local é suficiente |
| Remoção de N9.4 (Cerimônias) | Percepção de "comunicação fraca" | Documentar no Plano de Comunicações que review é assíncrono via GitHub |
| Remoção de N11.1 (CCB formal) | Percepção de "gestão de mudanças fraca" | Label `change-request` + ADR garantem rastreabilidade |
| Remoção de N12.2 (Manual do Usuário) | Percepção de "documentação incompleta" | README + N12.1 (docs técnicas) cobrem necessidade |
| Adição de N6.3 (Ferramentas Qualidade) | Poluição da EAP com ferramentas | Pacote único consolidado minimiza impacto |

---

**EAP v2.0 confirmada e pronta para inserção no TAP v1.1.**

Aguardo confirmação da inserção para prosseguir com a seção §5 (Principais Requisitos das Entregas).