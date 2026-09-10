# 4. **Estrutura Analítica do Projeto (EAP/WBS)**

### 4.1. NÍVEL 0 — RAIZ

| ID | Nó | Descrição                                       | Macro-Fase |
| -- | --- | ------------------------------------------------- | ---------- |
| N0 | —  | COGME — Conversor de Ganhos em Moeda Estrangeira | —         |

### 4.2. NÍVEIS 1 E 2 — FASES OBRIGATÓRIAS (MVP Acadêmico)

| ID Nível 1   | Fase (Nível 1)                         | ID Nível 2 | Pacote de Trabalho (Nível 2)                                         | Macro-Fase |
| ------------- | --------------------------------------- | ----------- | --------------------------------------------------------------------- | ---------- |
| **N1**  | **1. Iniciação e Planejamento** | N1.2        | 1.2. Identificação de Stakeholders                                  | MF1        |
|               |                                         | N1.3        | 1.3. Planos de Gerenciamento                                          | MF1        |
|               |                                         | N1.4        | 1.4. Plano da Qualidade                                               | MF1        |
|               |                                         | N1.5        | 1.5. Política de Licenciamento FOSS                                  | MF1        |
|               |                                         | N1.6        | 1.6. Definição do Backlog e Kanban                                  | MF1        |
| **N2**  | **2. Levantamento de Requisitos** | N2.1        | 2.1. Requisitos Funcionais                                            | MF1        |
|               |                                         | N2.2        | 2.2. Requisitos Não Funcionais                                       | MF1        |
|               |                                         | N2.3        | 2.3. Casos de Uso e Histórias de Usuário                            | MF1        |
| **N3**  | **3. Modelagem e Prototipação** | N3.1        | 3.1. Arquitetura da Solução                                         | MF1        |
|               |                                         | N3.2        | 3.2. Protótipo UX/UI                                                 | MF1        |
|               |                                         | N3.3        | 3.3. Modelagem de Dados (DER)                                         | MF1        |
| **N4**  | **4. Configuração de Ambiente** | N4.1        | 4.1. Seleção e Validação da Stack FOSS                            | MF1        |
|               |                                         | N4.2        | 4.2. Repositório Git + CI/CD                                         | MF1        |
|               |                                         | N4.3        | 4.3. Setup Local e Homologação                                      | MF1        |
|               |                                         | N4.4        | 4.4. Auditoria de Licenças                                           | MF1        |
| **N5**  | **5. Desenvolvimento do Sistema** | N5.1        | 5.1. Backend — Lógica de Negócio                                   | MF2        |
|               |                                         | N5.2        | 5.2. Backend — API de Câmbio + Cache                                | MF2        |
|               |                                         | N5.3        | 5.3. Frontend — Interface e Simulações                             | MF2        |
|               |                                         | N5.4        | 5.4. Módulo PDF (WeasyPrint)                                         | MF2        |
|               |                                         | N5.5        | 5.5. SDD com IA (Prompts + Revisão)                                  | MF2        |
| **N6**  | **6. Garantia da Qualidade**      | N6.1        | 6.1. Testes Unitários/Integração (≥ 80%)                          | MF2        |
|               |                                         | N6.2        | 6.2. Testes de Aceitação (UAT)                                      | MF2        |
|               |                                         | N6.3        | 6.3. Aplicação de Ferramentas da Qualidade (12 PDCAs + Ishikawa 6M) | MF2        |
| **N7**  | **7. DevOps e CI/CD**             | N7.1        | 7.1. Pipeline CI (lint + testes)                                      | MF2        |
| **N8**  | **8. Comunicação**              | N8.1        | 8.1. Matriz de Comunicação (RACI)                                   | MF1        |
|               |                                         | N8.2        | 8.2. Canais Oficiais (GitHub, e-mail)                                 | MF1        |
| **N10** | **10. Base de Conhecimento**      | N10.1       | 10.1. ADRs (decisões arquiteturais)                                  | MF1        |
|               |                                         | N10.2       | 10.2. Lições Aprendidas Contínuas                                  | MF1        |
|               |                                         | N10.3       | 10.3. Catálogo de Prompts SDD                                        | MF1        |
| **N11** | **11. Gestão de Mudanças**      | N11.2       | 11.2. Registro de Solicitações de Mudança                          | MF2        |
|               |                                         | N11.3       | 11.3. Label`change-request` no GitHub                               | MF2        |
|               |                                         | N11.4       | 11.4. Aprovação e Versionamento                                     | MF2        |
| **N12** | **12. Documentação do Projeto** | N12.1       | 12.1. Documentação Técnica (Arquitetura, APIs)                     | MF3        |
|               |                                         | N12.4       | 12.4. Consolidação da Documentação Parcial                        | MF3        |
| **N13** | **13. Encerramento**              | N13.1       | 13.1. Lições Aprendidas Finais                                      | MF3        |
|               |                                         | N13.2       | 13.2. Verificação SMART                                             | MF3        |
|               |                                         | N13.3       | 13.3. Apresentação Final + Aceite                                   | MF3        |

TOTAL: 12 fases Nível 1 + 37 pacotes Nível 2

### 4.3. Lista Hierárquica Aninhada

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
│   └── N6.3: 6.3. Aplicação de Ferramentas da Qualidade (12 PDCAs + Ishikawa 6M)
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

### 4.5. Declaração de Rastreabilidade (TAP → EAP v2.0)

| Origem (TAP)                     | Destino (EAP)                                    | Domínio PMBOK 7ª           |
| -------------------------------- | ------------------------------------------------ | ---------------------------- |
| §3 Objetivos SMART (Produto)    | Fases 5, 6, 7 (MVP funcional + qualidade + CI)   | Entrega                      |
| §3 Objetivos SMART (Qualidade)  | Fases 6 (testes + ferramentas qualidade), 12, 13 | Medição                    |
| §3 Objetivos SMART (Cronograma) | Macro-fases MF1/MF2/MF3                          | Abordagem de Desenvolvimento |
| §3 Objetivos SMART (Inovação) | Fases 5.5, 10.3 (SDD com IA)                     | Trabalho do Projeto          |
| §4 Escopo (implícito)          | Todas as 12 fases obrigatórias                  | Planejamento                 |
| §8 Restrições (FOSS)          | Fases 1.5, 4.1, 4.4                              | Abordagem de Desenvolvimento |
| §9 Premissas (LLM/SDD)          | Fases 5.5, 10.3                                  | Trabalho do Projeto          |
| §10 Riscos                      | Fase 11 (Gestão de Mudanças)                   | Incerteza                    |

**Verificação de completude**: 100% dos objetivos SMART do TAP §3 possuem ao menos uma fase da EAP v2.0 associada.

## 4.5. Diagramas - EAP (Macro-Fases e Pacotes de Trabalho)
