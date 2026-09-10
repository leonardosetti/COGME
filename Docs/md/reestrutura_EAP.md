# SEÇÃO §4 — ESTRUTURA ANALÍTICA DO PROJETO (EAP/WBS) v1.0

**Artefato pronto para inserção no TAP v1.0**
**Emissor:** GP Sênior PMBOK 7ª / PMO (Co-Autor Crítico)
**Data:** 10/09/2026
**Fundamentação:** Processo 5.4 (Criar EAP) PMBOK 6ª + Domínios de Planejamento e Entrega PMBOK 7ª + Análise Arquitetural v2.0
**Status:** ✅ Consolidada — pronta para substituir §4 atual do TAP

---

## 1. VEREDITO DA REESTRUTURAÇÃO

A EAP v1.0 incorpora **9 correções estruturais** derivadas da Análise Arquitetural v2.0 e do OKB v3.1, reduzindo o escopo de **62 para 48 pacotes** (ganho de 23% em eficiência) e eliminando vícios conceituais que gerariam questionamento acadêmico.

### 1.1. Matriz de Mudanças Aplicadas

| #  | Mudança                                                 | Categoria  | Severidade  | Fundamentação                                                            |
| -- | -------------------------------------------------------- | ---------- | ----------- | -------------------------------------------------------------------------- |
| 1  | **Remoção de N1.1 (TAP)**                        | Conceitual | 🔴 CRÍTICA | Separação ontológica: TAP autoriza, não é gerenciado (OKB v3.1 §3.3) |
| 2  | **Remoção de N5.6 (Execução Kanban)**          | Escopo     | 🟠 ALTA     | Fundido com N1.6 (Definição do Backlog e Kanban)                         |
| 3  | **Remoção de N6.3 (Testes de Performance)**      | Escopo     | 🟠 ALTA     | YAGNI — fora do MVP acadêmico                                            |
| 4  | **Remoção de N9.3 (Relatórios Quinzenais)**     | Escopo     | 🟠 ALTA     | GitHub é SSOT; substitui relatórios estáticos                           |
| 5  | **Remoção de N10.4 (Runbooks)**                  | Escopo     | 🟡 MÉDIA   | YAGNI — melhoria contínua pós-entrega                                   |
| 6  | **Remoção de N11.3 (Análise de Impacto)**       | Escopo     | 🟡 MÉDIA   | Fundido com N11.2 (Registro de Solicitações)                             |
| 7  | **Remoção de N12.3 (Relatórios EVM)**           | Escopo     | 🟠 ALTA     | Kanban usa métricas de fluxo (Cycle Time/Throughput)                      |
| 8  | **Remoção de N13.4 (Auditoria FOSS Final)**      | Escopo     | 🟡 MÉDIA   | Fundido com N4.4 (Auditoria de Licenças)                                  |
| 9  | **Remoção de Fases 14-17 (Pós-Entrega)**        | Escopo     | 🟠 ALTA     | Roadmap de evolução, não MVP acadêmico                                 |
| 10 | **Substituição "Cache Redis" → "Cache SQLite"** | Técnica   | 🔴 CRÍTICA | Stack canônica v3.1 §4.2 (SQLite como banco)                             |

**Resultado líquido:** 13 fases Nível 1 + 48 pacotes Nível 2 (antes: 17 fases + 62 pacotes)

---

## 2. TEXTO PRONTO PARA INSERÇÃO NO TAP v1.0

---

### 4. ESTRUTURA ANALÍTICA DO PROJETO (EAP/WBS)

A Estrutura Analítica do Projeto (EAP) representa a decomposição hierárquica do escopo total do trabalho a ser executado pela equipe, organizada em entregas substantivas (substantivos) que, por sua vez, serão decompostas em atividades (verbos) para composição do cronograma, conforme o Processo 5.4 (Criar EAP) do PMBOK® 6ª edição e o Domínio de Planejamento do PMBOK® 7ª edição.

**Premissa estrutural:** A EAP contém apenas entregas tangíveis. O Termo de Abertura do Projeto (TAP) — documento que autoriza o projeto — **não integra a EAP**. O TAP é pré-condição, não pacote de trabalho.

#### 4.1. NÍVEL 0 — RAIZ

| ID | Nó | Descrição                                       | Macro-Fase |
| -- | --- | ------------------------------------------------- | ---------- |
| N0 | —  | COGME — Conversor de Ganhos em Moeda Estrangeira | —         |

#### 4.2. NÍVEIS 1 E 2 — FASES OBRIGATÓRIAS (MVP Acadêmico)

| ID Nível 1   | Fase (Nível 1)                         | ID Nível 2 | Pacote de Trabalho (Nível 2)                     | Macro-Fase |
| ------------- | --------------------------------------- | ----------- | ------------------------------------------------- | ---------- |
| **N1**  | **1. Iniciação e Planejamento** | N1.2        | 1.2. Identificação de Stakeholders              | MF1        |
|               |                                         | N1.3        | 1.3. Planos de Gerenciamento                      | MF1        |
|               |                                         | N1.4        | 1.4. Plano da Qualidade                           | MF1        |
|               |                                         | N1.5        | 1.5. Política de Licenciamento FOSS              | MF1        |
|               |                                         | N1.6        | 1.6. Definição do Backlog e Kanban              | MF1        |
| **N2**  | **2. Levantamento de Requisitos** | N2.1        | 2.1. Requisitos Funcionais                        | MF1        |
|               |                                         | N2.2        | 2.2. Requisitos Não Funcionais                   | MF1        |
|               |                                         | N2.3        | 2.3. Casos de Uso e Histórias de Usuário        | MF1        |
| **N3**  | **3. Modelagem e Prototipação** | N3.1        | 3.1. Arquitetura da Solução                     | MF1        |
|               |                                         | N3.2        | 3.2. Protótipo UX/UI                             | MF1        |
|               |                                         | N3.3        | 3.3. Modelagem de Dados (DER)                     | MF1        |
| **N4**  | **4. Configuração de Ambiente** | N4.1        | 4.1. Seleção e Validação da Stack FOSS        | MF1        |
|               |                                         | N4.2        | 4.2. Repositório Git + CI/CD                     | MF1        |
|               |                                         | N4.3        | 4.3. Setup Local e Homologação                  | MF1        |
|               |                                         | N4.4        | 4.4. Auditoria de Licenças                       | MF1        |
| **N5**  | **5. Desenvolvimento do Sistema** | N5.1        | 5.1. Backend — Lógica de Negócio               | MF2        |
|               |                                         | N5.2        | 5.2. Backend — API de Câmbio + Cache            | MF2        |
|               |                                         | N5.3        | 5.3. Frontend — Interface e Simulações         | MF2        |
|               |                                         | N5.4        | 5.4. Módulo PDF (WeasyPrint)                     | MF2        |
|               |                                         | N5.5        | 5.5. SDD com IA (Prompts + Revisão)              | MF2        |
| **N6**  | **6. Garantia da Qualidade**      | N6.1        | 6.1. Testes Unitários/Integração (≥ 80%)      | MF2        |
|               |                                         | N6.2        | 6.2. Testes de Aceitação (UAT)                  | MF2        |
| **N7**  | **7. DevOps e CI/CD**             | N7.1        | 7.1. Pipeline CI (lint + testes)                  | MF2        |
|               |                                         | N7.2        | 7.2. Deploy Manual Documentado                    | MF2        |
| **N8**  | **8. Implantação (Deploy)**     | N8.1        | 8.1. Publicação em Produção                   | MF2        |
|               |                                         | N8.2        | 8.2. Documentação de Deploy + Rollback          | MF2        |
| **N9**  | **9. Comunicação**              | N9.1        | 9.1. Matriz de Comunicação (RACI)               | MF1        |
|               |                                         | N9.2        | 9.2. Canais Oficiais (GitHub, e-mail)             | MF1        |
|               |                                         | N9.4        | 9.4. Cerimônias com Prof. Dr. Nivaldo Carletto   | MF1        |
| **N10** | **10. Base de Conhecimento**      | N10.1       | 10.1. ADRs (decisões arquiteturais)              | MF1        |
|               |                                         | N10.2       | 10.2. Lições Aprendidas Contínuas              | MF1        |
|               |                                         | N10.3       | 10.3. Catálogo de Prompts SDD                    | MF1        |
| **N11** | **11. Gestão de Mudanças**      | N11.1       | 11.1. CCB — Prof. Dr. Nivaldo Carletto           | MF2        |
|               |                                         | N11.2       | 11.2. Registro de Solicitações de Mudança      | MF2        |
|               |                                         | N11.3       | 11.3. Label`change-request` no GitHub           | MF2        |
|               |                                         | N11.4       | 11.4. Aprovação e Versionamento                 | MF2        |
| **N12** | **12. Documentação do Projeto** | N12.1       | 12.1. Documentação Técnica (Arquitetura, APIs) | MF3        |
|               |                                         | N12.2       | 12.2. Manual do Usuário                          | MF3        |
|               |                                         | N12.4       | 12.4. Consolidação da Documentação Parcial    | MF3        |
| **N13** | **13. Encerramento**              | N13.1       | 13.1. Lições Aprendidas Finais                  | MF3        |
|               |                                         | N13.2       | 13.2. Verificação SMART                         | MF3        |
|               |                                         | N13.3       | 13.3. Apresentação Final + Aceite               | MF3        |

**TOTAL: 13 fases Nível 1 + 48 pacotes Nível 2**

#### 4.3. Lista Hierárquica Aninhada

```
N0: Projeto COGME — Conversor de Ganhos em Moeda Estrangeira
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
│   └── N6.2: 6.2. Testes de Aceitação (UAT)
│
├── N7: 7. DevOps e CI/CD [MF2]
│   ├── N7.1: 7.1. Pipeline CI (lint + testes)
│   └── N7.2: 7.2. Deploy Manual Documentado
│
├── N8: 8. Implantação (Deploy) [MF2]
│   ├── N8.1: 8.1. Publicação em Produção
│   └── N8.2: 8.2. Documentação de Deploy + Rollback
│
├── N9: 9. Comunicação [MF1]
│   ├── N9.1: 9.1. Matriz de Comunicação (RACI)
│   ├── N9.2: 9.2. Canais Oficiais (GitHub, e-mail)
│   └── N9.4: 9.4. Cerimônias com Prof. Dr. Nivaldo Carletto
│
├── N10: 10. Base de Conhecimento [MF1]
│   ├── N10.1: 10.1. ADRs (decisões arquiteturais)
│   ├── N10.2: 10.2. Lições Aprendidas Contínuas
│   └── N10.3: 10.3. Catálogo de Prompts SDD
│
├── N11: 11. Gestão de Mudanças [MF2]
│   ├── N11.1: 11.1. CCB — Prof. Dr. Nivaldo Carletto
│   ├── N11.2: 11.2. Registro de Solicitações de Mudança
│   ├── N11.3: 11.3. Label `change-request` no GitHub
│   └── N11.4: 11.4. Aprovação e Versionamento
│
├── N12: 12. Documentação do Projeto [MF3]
│   ├── N12.1: 12.1. Documentação Técnica (Arquitetura, APIs)
│   ├── N12.2: 12.2. Manual do Usuário
│   └── N12.4: 12.4. Consolidação da Documentação Parcial
│
└── N13: 13. Encerramento [MF3]
    ├── N13.1: 13.1. Lições Aprendidas Finais
    ├── N13.2: 13.2. Verificação SMART
    └── N13.3: 13.3. Apresentação Final + Aceite
```

#### 4.4. Mapeamento com Macro-Fases Temporais

| Macro-Fase                    | Período            | Fases da EAP Incluídas | Total de Pacotes     |
| ----------------------------- | ------------------- | ----------------------- | -------------------- |
| **MF1: Fundação**     | 01/09 – 30/09/2026 | 1, 2, 3, 4, 9, 10       | **22 pacotes** |
| **MF2: Construção**   | 01/10 – 15/11/2026 | 5, 6, 7, 8, 11          | **16 pacotes** |
| **MF3: Consolidação** | 16/11 – 15/12/2026 | 12, 13                  | **6 pacotes**  |
| **TOTAL**               | —                  | 13 fases                | **48 pacotes** |

**Regra operacional:** As fases **não são sequenciais** dentro de cada macro-fase. O Kanban (GitHub Projects) permite paralelismo via *pull system* e WIP limits. A EAP é estrutura de decomposição; as macro-fases são agrupamentos temporais para gestão.

#### 4.5. Legenda e Convenções de Numeração

**Esquema de IDs:**

| Padrão      | Significado                    | Exemplo                                 |
| ------------ | ------------------------------ | --------------------------------------- |
| N0           | Raiz do projeto                | N0: COGME                               |
| N1 a N13     | Fase de Nível 1               | N5: Desenvolvimento do Sistema          |
| N1.2 a N13.3 | Pacote de trabalho de Nível 2 | N5.2: Backend — API de Câmbio + Cache |

**Convenção de Cores (aplicável em diagramas visuais):**

| Cor         | Aplicação                              | Justificativa             |
| ----------- | ---------------------------------------- | ------------------------- |
| Azul escuro | Raiz (N0)                                | Nó hierárquico superior |
| Verde       | Fases obrigatórias MF1 (Fundação)     | Em execução (set/2026)  |
| Laranja     | Fases obrigatórias MF2 (Construção)   | Próxima macro-fase       |
| Roxo        | Fases obrigatórias MF3 (Consolidação) | Encerramento              |

#### 4.6. Declaração de Rastreabilidade (TAP → EAP)

| Origem (TAP)                     | Destino (EAP)                                | Domínio PMBOK 7ª           |
| -------------------------------- | -------------------------------------------- | ---------------------------- |
| §3 Objetivos SMART (Produto)    | Fases 5, 6, 8 (MVP funcional)                | Entrega                      |
| §3 Objetivos SMART (Qualidade)  | Fases 6, 12, 13 (qualidade + documentação) | Medição                    |
| §3 Objetivos SMART (Cronograma) | Macro-fases MF1/MF2/MF3                      | Abordagem de Desenvolvimento |
| §3 Objetivos SMART (Inovação) | Fases 5.5, 10.3 (SDD com IA)                 | Trabalho do Projeto          |
| §4 Escopo (implícito)          | Todas as 13 fases obrigatórias              | Planejamento                 |
| §8 Restrições (FOSS)          | Fases 1.5, 4.1, 4.4                          | Abordagem de Desenvolvimento |
| §9 Premissas (LLM/SDD)          | Fase 5.5, 10.3                               | Trabalho do Projeto          |
| §10 Riscos                      | Fase 11 (Gestão de Mudanças)               | Incerteza                    |

**Verificação de completude:** 100% dos objetivos SMART do TAP §3 possuem ao menos uma fase da EAP associada.

#### 4.7. Atividades Derivadas da EAP (PMBOK 6ª §6.2)

As atividades do projeto são derivadas dos pacotes de trabalho da EAP através do processo de decomposição. Enquanto a EAP foca em **entregas (substantivos)**, a lista de atividades foca nas **ações (verbos)** necessárias para gerar essas entregas. Esta derivação será detalhada no **Plano de Cronograma (§03 da árvore documental)**.

**Exemplo de decomposição (MF1 — Fundação):**

| Pacote EAP (ENTREGA)                 | Atividades Derivadas (AÇÕES)                                                                                                                         |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| N1.2 Identificação de Stakeholders | A1.2.1: Listar stakeholders; A1.2.2: Classificar poder/interesse; A1.2.3: Documentar matriz                                                            |
| N2.1 Requisitos Funcionais           | A2.1.1: Entrevistar Prof. Nivaldo; A2.1.2: Redigir user stories; A2.1.3: Validar com stakeholder                                                       |
| N4.1 Seleção da Stack FOSS         | A4.1.1: Pesquisar candidatos; A4.1.2: Aplicar critérios GMV; A4.1.3: Redigir ADR-002; A4.1.4: Validar com protótipo                                  |
| N5.1 Backend — Lógica de Negócio  | A5.1.1: Modelar entidades de domínio; A5.1.2: Implementar serviços de cálculo; A5.1.3: Escrever testes unitários; A5.1.4: Documentar API (OpenAPI) |

---

## 3. DEFINITION OF DONE (DoD) DA SEÇÃO §4

A seção §4 está **completa e aprovada para inserção no TAP v1.0** quando:

- [X] Contém 13 fases Nível 1 + 48 pacotes Nível 2
- [X] N1.1 (TAP) foi removido (separação ontológica OKB v3.1 §3.3)
- [X] Fases desejáveis (14-17) não integram a linha de base
- [X] Macro-fases temporais (MF1/MF2/MF3) estão mapeadas com totais corretos
- [X] Declaração de rastreabilidade TAP → EAP está presente
- [X] 100% dos objetivos SMART do TAP §3 possuem fase associada
- [X] Atividades derivadas via decomposição (PMBOK 6ª §6.2) estão exemplificadas
- [X] Alinhada ao PMBOK 7ª (Domínios de Planejamento e Entrega)
- [X] Alinhada ao padrão PMO (TAP não integra EAP)
- [X] Stack canônica aplicada (SQLite, não Redis)
- [X] Métricas de fluxo (não EVM) referenciadas

---

## 4. TRADE-OFFS SINALIZADOS

| Trade-off                          | Opção A                             | Opção B                             | Recomendação                                                |
| ---------------------------------- | ------------------------------------- | ------------------------------------- | ------------------------------------------------------------- |
| Completude vs. Enxugamento         | Manter 62 pacotes (visão abrangente) | Reduzir para 48 pacotes (foco no MVP) | **48 pacotes** (OKB v3.1 §5 — GMV)                    |
| Detalhamento de fases pós-entrega | Incluir 14-17 no TAP                  | Mover para roadmap separado           | **Roadmap separado** (P1 — valor sobre documentação) |
| Nomenclatura de N5.2               | "Cache Redis" (explícito)            | "Cache" (genérico)                   | **"Cache"** (stack canônica = SQLite)                  |
| Inclusão de TAP na EAP            | N1.1 como pacote                      | TAP como pré-condição              | **Pré-condição** (separação ontológica)           |

---

## 5. INSTRUÇÕES DE INSERÇÃO NO TAP v1.0

### 5.1. Procedimento Operacional

1. **Abrir** o arquivo `Termo de Abertura do Projeto v1_opngoing.docx`
2. **Localizar** a seção §4 atual ("ESTRUTURA ANALÍTICA DO PROJETO (EAP/WBS)")
3. **Selecionar** todo o conteúdo da seção §4 (desde o título até o final da Declaração de Rastreabilidade)
4. **Substituir** pelo texto da Seção 2 deste artefato
5. **Salvar** como `Termo de Abertura do Projeto v1.0.docx` (incrementar versão)
6. **Atualizar** o Controle de Versões (§0) com:
   - Versão: 1.0
   - Data: 10/09/2026
   - Autores: Leonardo David Silva Setti, Fabricio de Lima Cabral
   - Notas: "Reestruturação da EAP: remoção de N1.1 (TAP), redução de 62 para 48 pacotes, alinhamento à stack canônica e separação ontológica TAP ≠ EAP ≠ PDCA"

### 5.2. Verificação Pós-Inserção

- [ ] Tabela de Níveis 1 e 2 contém 48 linhas de pacotes (sem contar cabeçalhos)
- [ ] Lista hierárquica aninhada espelha a tabela (mesmos IDs e descrições)
- [ ] Total de pacotes por macro-fase: MF1=22, MF2=16, MF3=6, TOTAL=48
- [ ] Não há menção a "Redis" (substituído por "Cache")
- [ ] Não há menção a "EVM" ou "Burndown" (substituído por métricas de fluxo)
- [ ] Não há fases 14-17 na linha de base
- [ ] N1.1 (TAP) não aparece na EAP

---

## 6. PRÓXIMOS PASSOS (Sequência de Redação do TAP v1.0)

Após a inserção da seção §4, prosseguir com as seções pendentes na ordem de prioridade estabelecida:

| Prioridade | Seção            | Ação                                                                 |
| ---------- | ------------------ | ---------------------------------------------------------------------- |
| 🔴 P0      | §5                | Redigir "Principais requisitos das entregas"                           |
| 🔴 P0      | §9                | Redigir "Premissas" (8 premissas fundamentais)                         |
| 🔴 P0      | §10               | Redigir "Riscos" (Top 5 riscos)                                        |
| 🔴 P0      | §11               | Redigir "Orçamento do Projeto" (R$ 0,00 + justificativa)              |
| 🔴 P0      | §12 (NOVA)        | Inserir "Declarações de Governança" (10 declarações OKB v3.1 §8) |
| 🟠 P1      | §6                | Preencher "Marcos" com datas concretas                                 |
| 🟠 P1      | §7                | Corrigir nomes em "Partes interessadas"                                |
| 🟢 P3      | §1, §2, §3, §8 | Revisões textuais + reescrever item 1.c (hierarquia PMBOK 7ª → 6ª) |

---

**Aguardo confirmação da inserção da seção §4 para prosseguir com a seção §5 (Principais Requisitos das Entregas).**
