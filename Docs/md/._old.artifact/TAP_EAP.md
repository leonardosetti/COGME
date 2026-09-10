# SEÇÃO 5 — ESTRUTURA ANALÍTICA DO PROJETO (EAP/WBS)
**Versão:** v0.9 (r3 — alinhada ao OKB_COGME_v3.0 §6)
**Referência normativa:** OKB_COGME_v3.0 §4.6 (Macro-Fases) + §6 (EAP 13+4)
**Governança:** PMBOK 7ª (primária) + PMBOK 6ª (dicionário — processo 5.4 "Criar EAP")
**Método de execução:** Kanban via GitHub Projects (ADR-001)

---

## 5.1. NÍVEL 0 — RAIZ

| ID | Nó | Descrição | Macro-Fase |
|---|---|---|---|
| `N0` | 📁 | **Projeto COGME — Conversor de Ganhos em Moeda Estrangeira** | — |

---

## 5.2. NÍVEIS 1 E 2 — FASES OBRIGATÓRIAS (MVP Acadêmico)

### 5.2.1. Tabela Estrutural (formato tabular)

| ID Nível 1 | Fase (Nível 1) | ID Nível 2 | Pacote de Trabalho (Nível 2) | Macro-Fase |
|---|---|---|---|---|
| `N1` | **1. Iniciação e Planejamento** | `N1.1` | 1.1. Termo de Abertura do Projeto (TAP) | MF1 |
| | | `N1.2` | 1.2. Identificação de Stakeholders | MF1 |
| | | `N1.3` | 1.3. Planos de Gerenciamento (Escopo, Cronograma, Custo, Riscos) | MF1 |
| | | `N1.4` | 1.4. Plano da Qualidade | MF1 |
| | | `N1.5` | 1.5. Política de Licenciamento FOSS | MF1 |
| | | `N1.6` | 1.6. Definição do Backlog e Kanban (GitHub Projects) | MF1 |
| `N2` | **2. Levantamento e Análise de Requisitos** | `N2.1` | 2.1. Requisitos Funcionais | MF1 |
| | | `N2.2` | 2.2. Requisitos Não Funcionais | MF1 |
| | | `N2.3` | 2.3. Casos de Uso e Histórias de Usuário | MF1 |
| `N3` | **3. Modelagem e Prototipação** | `N3.1` | 3.1. Arquitetura da Solução | MF1 |
| | | `N3.2` | 3.2. Protótipo UX/UI | MF1 |
| | | `N3.3` | 3.3. Modelagem de Dados (DER) | MF1 |
| `N4` | **4. Configuração de Ambiente** | `N4.1` | 4.1. Seleção e Validação da Stack FOSS | MF1 |
| | | `N4.2` | 4.2. Repositório Git + CI/CD | MF1 |
| | | `N4.3` | 4.3. Setup Local e Homologação | MF1 |
| | | `N4.4` | 4.4. Auditoria de Licenças | MF1 |
| `N5` | **5. Desenvolvimento do Sistema** | `N5.1` | 5.1. Backend — Lógica de Negócio (Câmbio, Spread, IOF) | MF2 |
| | | `N5.2` | 5.2. Backend — API de Câmbio + Cache Redis | MF2 |
| | | `N5.3` | 5.3. Frontend — Interface e Simulações | MF2 |
| | | `N5.4` | 5.4. Módulo PDF (WeasyPrint) | MF2 |
| | | `N5.5` | 5.5. SDD com IA (Prompts + Revisão) | MF2 |
| | | `N5.6` | 5.6. Execução Kanban (Rituais no GitHub Projects) | MF2 |
| `N6` | **6. Garantia da Qualidade e Testes** | `N6.1` | 6.1. Testes Unitários/Integração (≥ 80% coverage) | MF2 |
| | | `N6.2` | 6.2. Testes de Aceitação (UAT) | MF2 |
| | | `N6.3` | 6.3. Testes de Performance e Carga | MF2 |
| `N7` | **7. DevOps e CI/CD** | `N7.1` | 7.1. Pipeline CI (lint + testes) | MF2 |
| | | `N7.2` | 7.2. Pipeline CD (build + deploy) | MF2 |
| `N8` | **8. Implantação (Deploy)** | `N8.1` | 8.1. Publicação em Produção | MF2 |
| | | `N8.2` | 8.2. Documentação de Deploy + Rollback | MF2 |
| `N9` | **9. Comunicação** ⭐ | `N9.1` | 9.1. Matriz de Comunicação (RACI) | MF1 |
| | | `N9.2` | 9.2. Canais Oficiais (GitHub, e-mail, reuniões) | MF1 |
| | | `N9.3` | 9.3. Relatórios de Status Quinzenais | MF1 |
| | | `N9.4` | 9.4. Cerimônias com Stakeholder (Prof. Nivaldo) | MF1 |
| `N10` | **10. Base de Conhecimento** ⭐ | `N10.1` | 10.1. ADRs (decisões arquiteturais) | MF1 |
| | | `N10.2` | 10.2. Lições Aprendidas Contínuas (Retrospectivas) | MF1 |
| | | `N10.3` | 10.3. Catálogo de Prompts SDD | MF1 |
| | | `N10.4` | 10.4. Runbooks Operacionais | MF1 |
| `N11` | **11. Gestão de Mudanças** ⭐ | `N11.1` | 11.1. CCB (Change Control Board) — Prof. Nivaldo | MF2 |
| | | `N11.2` | 11.2. Registro de Solicitações de Mudança | MF2 |
| | | `N11.3` | 11.3. Análise de Impacto (escopo/custo/prazo) | MF2 |
| | | `N11.4` | 11.4. Aprovação e Versionamento | MF2 |
| `N12` | **12. Documentação do Projeto** | `N12.1` | 12.1. Documentação Técnica (Arquitetura, APIs) | MF3 |
| | | `N12.2` | 12.2. Manual do Usuário | MF3 |
| | | `N12.3` | 12.3. Relatórios de Desempenho (EVM/Burndown) | MF3 |
| | | `N12.4` | 12.4. Consolidação da Documentação Parcial (Entrega 08/09/2026) | MF3 |
| `N13` | **13. Encerramento** | `N13.1` | 13.1. Lições Aprendidas Finais | MF3 |
| | | `N13.2` | 13.2. Verificação SMART | MF3 |
| | | `N13.3` | 13.3. Apresentação Final + Aceite | MF3 |
| | | `N13.4` | 13.4. Auditoria FOSS Final | MF3 |

⭐ = Fases adicionadas em relação ao TAP v1.0 (alinham domínios PMBOK 7ª: Stakeholders, Equipe, Planejamento)

---

### 5.2.2. Lista Hierárquica Aninhada (formato para parse XML → draw.io)

```
N0: Projeto COGME — Conversor de Ganhos em Moeda Estrangeira
├── N1: 1. Iniciação e Planejamento [MF1]
│   ├── N1.1: 1.1. Termo de Abertura do Projeto (TAP)
│   ├── N1.2: 1.2. Identificação de Stakeholders
│   ├── N1.3: 1.3. Planos de Gerenciamento (Escopo, Cronograma, Custo, Riscos)
│   ├── N1.4: 1.4. Plano da Qualidade
│   ├── N1.5: 1.5. Política de Licenciamento FOSS
│   └── N1.6: 1.6. Definição do Backlog e Kanban (GitHub Projects)
├── N2: 2. Levantamento e Análise de Requisitos [MF1]
│   ├── N2.1: 2.1. Requisitos Funcionais
│   ├── N2.2: 2.2. Requisitos Não Funcionais
│   └── N2.3: 2.3. Casos de Uso e Histórias de Usuário
├── N3: 3. Modelagem e Prototipação [MF1]
│   ├── N3.1: 3.1. Arquitetura da Solução
│   ├── N3.2: 3.2. Protótipo UX/UI
│   └── N3.3: 3.3. Modelagem de Dados (DER)
├── N4: 4. Configuração de Ambiente [MF1]
│   ├── N4.1: 4.1. Seleção e Validação da Stack FOSS
│   ├── N4.2: 4.2. Repositório Git + CI/CD
│   ├── N4.3: 4.3. Setup Local e Homologação
│   └── N4.4: 4.4. Auditoria de Licenças
├── N5: 5. Desenvolvimento do Sistema [MF2]
│   ├── N5.1: 5.1. Backend — Lógica de Negócio (Câmbio, Spread, IOF)
│   ├── N5.2: 5.2. Backend — API de Câmbio + Cache Redis
│   ├── N5.3: 5.3. Frontend — Interface e Simulações
│   ├── N5.4: 5.4. Módulo PDF (WeasyPrint)
│   ├── N5.5: 5.5. SDD com IA (Prompts + Revisão)
│   └── N5.6: 5.6. Execução Kanban (Rituais no GitHub Projects)
├── N6: 6. Garantia da Qualidade e Testes [MF2]
│   ├── N6.1: 6.1. Testes Unitários/Integração (≥ 80% coverage)
│   ├── N6.2: 6.2. Testes de Aceitação (UAT)
│   └── N6.3: 6.3. Testes de Performance e Carga
├── N7: 7. DevOps e CI/CD [MF2]
│   ├── N7.1: 7.1. Pipeline CI (lint + testes)
│   └── N7.2: 7.2. Pipeline CD (build + deploy)
├── N8: 8. Implantação (Deploy) [MF2]
│   ├── N8.1: 8.1. Publicação em Produção
│   └── N8.2: 8.2. Documentação de Deploy + Rollback
├── N9: 9. Comunicação [MF1] ⭐
│   ├── N9.1: 9.1. Matriz de Comunicação (RACI)
│   ├── N9.2: 9.2. Canais Oficiais (GitHub, e-mail, reuniões)
│   ├── N9.3: 9.3. Relatórios de Status Quinzenais
│   └── N9.4: 9.4. Cerimônias com Stakeholder (Prof. Nivaldo)
├── N10: 10. Base de Conhecimento [MF1] ⭐
│   ├── N10.1: 10.1. ADRs (decisões arquiteturais)
│   ├── N10.2: 10.2. Lições Aprendidas Contínuas (Retrospectivas)
│   ├── N10.3: 10.3. Catálogo de Prompts SDD
│   └── N10.4: 10.4. Runbooks Operacionais
├── N11: 11. Gestão de Mudanças [MF2] ⭐
│   ├── N11.1: 11.1. CCB (Change Control Board) — Prof. Nivaldo
│   ├── N11.2: 11.2. Registro de Solicitações de Mudança
│   ├── N11.3: 11.3. Análise de Impacto (escopo/custo/prazo)
│   └── N11.4: 11.4. Aprovação e Versionamento
├── N12: 12. Documentação do Projeto [MF3]
│   ├── N12.1: 12.1. Documentação Técnica (Arquitetura, APIs)
│   ├── N12.2: 12.2. Manual do Usuário
│   ├── N12.3: 12.3. Relatórios de Desempenho (EVM/Burndown)
│   └── N12.4: 12.4. Consolidação da Documentação Parcial (Entrega 08/09/2026)
└── N13: 13. Encerramento [MF3]
    ├── N13.1: 13.1. Lições Aprendidas Finais
    ├── N13.2: 13.2. Verificação SMART
    ├── N13.3: 13.3. Apresentação Final + Aceite
    └── N13.4: 13.4. Auditoria FOSS Final
```

---

## 5.3. NÍVEIS 1 E 2 — FASES DESEJÁVEIS (Melhoria Contínua Pós-Entrega)

**Nota de governança:** As fases 14 a 17 **não compõem o MVP acadêmico obrigatório**. São tratadas como roadmap de evolução pós-entrega (Dez/2026 em diante), conforme OKB_COGME_v3.0 §6 e princípio P1 (valor sobre documentação). Não integram a linha de base de escopo do TAP.

### 5.3.1. Tabela Estrutural

| ID Nível 1 | Fase (Nível 1) | ID Nível 2 | Pacote de Trabalho (Nível 2) | Status |
|---|---|---|---|---|
| `N14` | **14. Segurança e Privacidade** ⚠️ | `N14.1` | 14.1. Análise OWASP Top 10 | Pós-entrega |
| | | `N14.2` | 14.2. Conformidade LGPD | Pós-entrega |
| | | `N14.3` | 14.3. Pentest básico | Pós-entrega |
| | | `N14.4` | 14.4. Política de Senhas e JWT | Pós-entrega |
| `N15` | **15. Acessibilidade** ⚠️ | `N15.1` | 15.1. Auditoria WCAG 2.1 AA | Pós-entrega |
| | | `N15.2` | 15.2. Testes com leitores de tela | Pós-entrega |
| | | `N15.3` | 15.3. Contraste e navegação por teclado | Pós-entrega |
| `N16` | **16. Observabilidade** ⚠️ | `N16.1` | 16.1. Logging Estruturado (JSON) | Pós-entrega |
| | | `N16.2` | 16.2. Health Checks (/health, /warmup) | Pós-entrega |
| | | `N16.3` | 16.3. Métricas de Negócio | Pós-entrega |
| | | `N16.4` | 16.4. Alertas de Falha | Pós-entrega |
| `N17` | **17. Internacionalização (i18n)** ⚠️ | `N17.1` | 17.1. Múltiplas moedas (USD, EUR, GBP, BRL) | Pós-entrega |
| | | `N17.2` | 17.2. Formatação por locale | Pós-entrega |
| | | `N17.3` | 17.3. Preparação para tradução de UI | Pós-entrega |

⚠️ = Fora da linha de base do MVP acadêmico; roadmap de evolução pós-Dez/2026

### 5.3.2. Lista Hierárquica Aninhada (formato para parse XML → draw.io)

```
N14: 14. Segurança e Privacidade [PÓS-ENTREGA] ⚠️
├── N14.1: 14.1. Análise OWASP Top 10
├── N14.2: 14.2. Conformidade LGPD
├── N14.3: 14.3. Pentest básico
└── N14.4: 14.4. Política de Senhas e JWT
N15: 15. Acessibilidade [PÓS-ENTREGA] ⚠️
├── N15.1: 15.1. Auditoria WCAG 2.1 AA
├── N15.2: 15.2. Testes com leitores de tela
└── N15.3: 15.3. Contraste e navegação por teclado
N16: 16. Observabilidade [PÓS-ENTREGA] ⚠️
├── N16.1: 16.1. Logging Estruturado (JSON)
├── N16.2: 16.2. Health Checks (/health, /warmup)
├── N16.3: 16.3. Métricas de Negócio
└── N16.4: 16.4. Alertas de Falha
N17: 17. Internacionalização (i18n) [PÓS-ENTREGA] ⚠️
├── N17.1: 17.1. Múltiplas moedas (USD, EUR, GBP, BRL)
├── N17.2: 17.2. Formatação por locale
└── N17.3: 17.3. Preparação para tradução de UI
```

---

## 5.4. MAPEAMENTO COM MACRO-FASES TEMPORAIS (OKB v3.0 §4.6)

| Macro-Fase | Período | Fases da EAP Incluídas | Total de Pacotes (Nível 2) |
|---|---|---|---|
| **MF1: Fundação** | 01/09 – 30/09/2026 | 1, 2, 3, 4, 9, 10 | 24 |
| **MF2: Construção** | 01/10 – 15/11/2026 | 5, 6, 7, 8, 11 | 17 |
| **MF3: Consolidação** | 16/11 – 15/12/2026 | 12, 13 | 8 |
| **Pós-Entrega** | Dez/2026 em diante | 14, 15, 16, 17 | 13 |
| **TOTAL GERAL** | — | 17 fases | **62 pacotes de trabalho** |

**Regra operacional:** As fases **não são sequenciais** dentro de cada macro-fase. O Kanban (GitHub Projects) permite paralelismo via pull system e WIP limits. A EAP é estrutura de decomposição; as macro-fases são agrupamentos temporais para gestão.

---

## 5.5. LEGENDA E CONVENÇÕES DE NUMERAÇÃO (para draw.io)

### 5.5.1. Esquema de IDs

| Padrão | Significado | Exemplo |
|---|---|---|
| `N0` | Raiz do projeto | N0: COGME |
| `N1` a `N17` | Fase de Nível 1 | N5: Desenvolvimento do Sistema |
| `N1.1` a `N17.3` | Pacote de trabalho de Nível 2 | N5.2: Backend — API de Câmbio + Cache Redis |

### 5.5.2. Convenção de Cores (sugestão para draw.io)

| Cor | Aplicação | Justificativa |
|---|---|---|
| 🔵 Azul escuro | Raiz (N0) | Nó hierárquico superior |
| 🟢 Verde | Fases obrigatórias MF1 (Fundação) | Em execução (set/2026) |
| 🟠 Laranja | Fases obrigatórias MF2 (Construção) | Próxima macro-fase |
| 🟣 Roxo | Fases obrigatórias MF3 (Consolidação) | Encerramento |
| ⚪ Cinza claro | Fases desejáveis pós-entrega (14-17) | Fora da linha de base |
| ⭐ Amarelo (borda) | Fases novas (9, 10, 11) | Acrescentadas no v0.9 |

### 5.5.3. Metadados por Nó (para XML draw.io)

Cada nó XML deve conter os seguintes atributos customizados:

```xml
<mxCell id="N5.2" value="5.2. Backend — API de Câmbio + Cache Redis"
        style="rounded=1;whiteSpace=wrap;fillColor=#fff2cc;strokeColor=#d6b656;"
        custom:id="N5.2"
        custom:macroFase="MF2"
        custom:fasePai="N5"
        custom:tipo="pacote_trabalho"
        custom:dominioPMBOK7="Entrega"
        custom:kanbanEpico="Epic-5.2"
        custom:status="pendente" />
```

---

## 5.6. DECLARAÇÃO DE RASTREABILIDADE

| Origem (TAP) | Destino (EAP) | Domínio PMBOK 7ª |
|---|---|---|
| §2 Objetivos SMART | Fases 5, 6, 8 (MVP funcional) | Entrega |
| §3 Critérios de Sucesso | Fases 6, 12, 13 (qualidade + documentação + encerramento) | Medição |
| §4 (implícito) Escopo | Todas as 13 fases obrigatórias | Planejamento |
| §7 Marcos | Macro-fases MF1/MF2/MF3 | Abordagem de Desenvolvimento |
| §8 Restrições (FOSS) | Fases 1.5, 4.1, 4.4, 13.4 | Abordagem de Desenvolvimento |
| §9 Premissas (LLM/SDD) | Fase 5.5, 10.3 | Trabalho do Projeto |
| §10 Riscos | Fase 11 (Gestão de Mudanças) | Incerteza |

**Verificação de completude:** 100% dos objetivos SMART do §3 possuem ao menos uma fase da EAP associada. Zero objetivos órfãos.

---

## 5.7. NOTAS DE GOVERNANÇA

1. **Obsolescência declarada:** A estrutura anterior do TAP v1.0 (11 fases, com "Sprints Ágeis" na Fase 5 e "Governança e Conformidade" como fase isolada) foi **integralmente substituída** por esta versão, em conformidade com o OKB_COGME_v3.0 §6.
2. **FOSS como restrição transversal:** A antiga "Fase 11 — Governança e Conformidade (FOSS)" foi **eliminada como fase autônoma**. O licenciamento FOSS é restrição transversal (P2 do OKB), documentada no TAP §2.4 e §8, e materializada nos pacotes 1.5, 4.1, 4.4 e 13.4.
3. **Kanban como SSOT:** Cada pacote de trabalho de Nível 2 (ex: `N5.2`) deve possuir um Épico correspondente no GitHub Projects (View 1: Kanban Backlog), com o mesmo identificador (ex: `Epic-5.2`). O Kanban é a fonte única de verdade para execução; a EAP é a fonte única de verdade para decomposição de escopo.
4. **Governança Mínima Viável (GMV):** As fases 9, 10 e 11 foram adicionadas não por burocracia, mas porque mapeiam domínios PMBOK 7ª até então omitidos (Stakeholders, Equipe, Planejamento). Sua omissão geraria risco acadêmico real (reprovação por lacuna de governança).

---

**Fim da Seção 5.**
**Próxima ação recomendada:** Após aprovação desta seção pelo Prof. Nivaldo, gerar o XML draw.io a partir da lista hierárquica aninhada (§5.2.2 e §5.3.2) utilizando os IDs `N*` como chaves primárias dos nós.