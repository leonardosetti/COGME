## 5 QUALIDADE

**Plano de Gerenciamento da Qualidade**

**Projeto:** COGME — Conversor de Ganhos em Moeda Estrangeira
**Versão:** 1.1
**Data:** 21/09/2026
**Autores:** Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

Este plano deriva diretamente das Premissas P1 (governança híbrida), P3 (SDD com IA auditável), P4 (código como deliverable), P5 (disponibilidade de 20h/semana) e P9 (separação ontológica TAP ≠ EAP ≠ PDCA), e das Restrições de Qualidade e Cronograma do TAP (§8.5 e §8.2), respeitando os Domínios de Medição, Entrega e Melhoria do PMBOK® 7ª edição. Aplica-se o regime de freeze do TAP e as Notas de Contexto registradas na seção 5.9 (NC-Q1 a NC-Q4).

## 5.1 IDENTIFICAÇÃO E PROPÓSITO

Este Plano de Gerenciamento da Qualidade estabelece os mecanismos para garantir que o COGME atenda aos critérios de aceite técnicos: cobertura de testes ≥ 80%, UAT sem defeitos críticos/bloqueantes, e aplicação sistemática de ferramentas da qualidade (12 ciclos PDCA + 3 diagramas de Ishikawa 6M).

**Função ontológica:** O plano não duplica gates de qualidade do Escopo §2.6 (DoR/DoD) — operacionaliza critérios técnicos de qualidade específicos para código, testes e documentação, garantindo conformidade com REQ-08, REQ-09 e REQ-10.

**Domínios PMBOK 7ª:** Medição (métricas de qualidade), Entrega (critérios de aceite) e Melhoria (ciclos PDCA).

**Processos PMBOK 6ª (dicionário, obsolescência declarada conforme Integração §1.2.4):** 8.1 Planejar o Gerenciamento da Qualidade, 8.2 Gerenciar a Qualidade, 8.3 Controlar a Qualidade.

**Trade-off declarado:** Abre-se mão de burocracia documental em favor de automação (pipeline CI) e melhoria contínua (PDCA por fase), alinhado ao Princípio "Foco em Valor" (PMBOK 7ª) e ao Valor Ágil "Software funcionando sobre documentação abrangente".

## 5.2 ABORDAGEM DE GERENCIAMENTO DA QUALIDADE

A qualidade do COGME opera em três dimensões complementares:

| Dimensão            | Objeto                             | Mecanismo de Controle                             | Fonte Canônica        |
| -------------------- | ---------------------------------- | ------------------------------------------------- | ---------------------- |
| **Preventiva** | Qualidade do código e arquitetura | Code Review + SDD com IA auditável + Clean Code  | Escopo §2.6 + ADR-004 |
| **Detectiva**  | Cobertura de testes e defeitos     | Pipeline CI + pytest + coverage.py ≥ 80%         | REQ-08 + N6.1          |
| **Corretiva**  | Melhoria contínua de processo     | 12 ciclos PDCA (um por fase da EAP) + Ishikawa 6M | REQ-10 + N6.3          |

**Regra de ouro:** Nenhum card migra para `Done` sem: (i) pipeline CI verde, (ii) coverage ≥ 80% no módulo afetado, (iii) code review aprovado, (iv) tasklist 100% concluída (se aplicável, ADR-004).

**Hierarquia de resolução de conflitos (aplicada à qualidade):**

1. Critérios de aceite do TAP §3.2 (coverage ≥ 80%, UAT sem defeitos críticos)
2. Clean Code e ACID (Premissa P5)
3. Conveniência técnica (preferência do desenvolvedor)

**[FIG-1 — Fluxo de Garantia da Qualidade]**
*SVG gerado — Fluxograma vertical com gates de qualidade sequenciais*

![FIG-1 — Fluxo de Garantia da Qualidade](../../../diagrams/fig-01-fluxo-qualidade.png)

*Conteúdo:* Fluxograma vertical com gates de qualidade sequenciais, destacando revisão humana para código SDD-IA e critérios binários de aprovação.
*Necessidade real:* Materializa visualmente o DoD técnico, demonstrando ao avaliador que qualidade não é inspeção final, mas processo contínuo com gates automáticos (CI) e manuais (review).

## 5.3 MÉTRICAS DE QUALIDADE

Dada a inaplicabilidade de EVM (ADR-003, Integração §1.6.2), o controle de qualidade opera por métricas técnicas automatizadas:

| Métrica                                | Fórmula/Definição                                                 | Meta   | Frequência        | Responsável     |
| --------------------------------------- | -------------------------------------------------------------------- | ------ | ------------------ | ---------------- |
| **Coverage**                      | (Linhas testadas / Total de linhas) × 100                           | ≥ 80% | Por push (CI)      | Pipeline + GP    |
| **Defeitos Críticos**            | Número de bugs bloqueantes/críticos em UAT                         | 0      | Por marco (M3, M4) | GP + UAT         |
| **Taxa de Aprovação em Review** | (PRs aprovados / Total de PRs) × 100                                | ≥ 90% | Semanal            | GP               |
| **Technical Debt Ratio**          | (Dívida técnica / Custo total) — estimado via SonarQube Free Tier | < 5%   | Por marco          | GP               |
| **Tempo de Resposta**             | Latência p95 das requisições da API                               | ≤ 3s  | M3 (homologação) | Pipeline + Edson |

**Nota (I5):** SonarQube Free Tier é utilizado para análise estática de dívida técnica, em conformidade com TAP §11 (proibição de ferramentas pagas). O Free Tier fornece análise básica sem custos.

**Gatilhos de ação corretiva:**

- Se `Coverage` < 80% por 2 commits consecutivos → bloqueio de merge até correção
- Se `Defeitos Críticos` > 0 em UAT → retrabalho imediato + congelamento de novas features
- Se `Taxa de Aprovação em Review` < 90% por 2 semanas → retrospectiva extraordinária + revisão de padrões de código

**[FIG-2 — Dashboard de Métricas de Qualidade]**
*Exclusão justificada por GMV*

**Decisão:** Dashboard separado não será produzido.
**Justificativa GMV:** GitHub Insights + coverage.py + pytest já fornecem visibilidade nativa sem overhead documental. Produzir artefato duplicado violaria o princípio de Governança Mínima Viável (OKB §3.2).
**Alternativa:** Evidências serão capturadas diretamente do GitHub Actions e relatórios de coverage quando solicitadas pelo Prof. Dr. Nivaldo Carleto em avaliação.

## 5.4 CRITÉRIOS DE ACEITE TÉCNICOS

### 5.4.1 Código-Fonte

| Critério                       | Descrição                                                               | Verificação                                                                                        |
| ------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **Clean Code**            | Nomes significativos, funções ≤ 20 linhas, sem duplicação > 3 linhas | Code Review + pylint/flake8                                                                          |
| **Type Safety**           | Type hints em 100% das funções públicas (Python 3.11+)                 | mypy --strict (ferramenta complementar de análise estática, não parte da stack principal ADR-001) |
| **Documentação Inline** | Docstrings em todas as classes e funções públicas (padrão Google)     | pydocstyle                                                                                           |
| **SDD Auditável**        | Commits de código gerado por IA declaram co-autoria e link para prompt   | Git log + .ai/handoffs/                                                                              |

**Nota (I6):** mypy é ferramenta complementar de análise estática de tipos, não listada na ADR-001 (stack principal). Sua utilização é opcional e recomendada para garantir type safety, sem impacto no orçamento (FOSS, MIT License).

### 5.4.2 Testes Automatizados

| Critério                     | Descrição                                                  | Verificação              |
| ----------------------------- | ------------------------------------------------------------ | -------------------------- |
| **Cobertura Mínima**   | ≥ 80% de linhas testadas (unitários + integração)        | coverage.py report         |
| **Testes Críticos**    | 100% dos fluxos REQ-01 a REQ-07 cobertos                     | coverage branch + UAT      |
| **Tempo de Execução** | Suite completa em ≤ 5 minutos                               | GitHub Actions CI (REQ-11) |
| **Isolamento**          | Testes não dependem de ordem de execução ou estado global | pytest --random-order      |

### 5.4.3 Documentação

| Critério                 | Descrição                                                           | Verificação             |
| ------------------------- | --------------------------------------------------------------------- | ------------------------- |
| **Rastreabilidade** | 100% dos requisitos (REQ-01 a REQ-15) mapeados a cards e testes       | Matriz de rastreabilidade |
| **Atualização**   | Documentação atualizada antes do merge (código + docs no mesmo PR) | Code Review               |
| **Consistência**   | Glossário e OKB atualizados quando novos termos/decisões surgirem   | Refinement semanal        |

## 5.5 FERRAMENTAS DA QUALIDADE

### 5.5.1 Pipeline de Integração Contínua (CI)

Conforme N7.1 da EAP e REQ-11, o pipeline CI executa automaticamente a cada push:

~~~yaml
# .github/workflows/ci.yml (resumo)
name: CI Pipeline
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Lint
        run: flake8 . && mypy --strict cogme/
      - name: Test with pytest
        run: pytest --cov=cogme --cov-report=xml --cov-fail-under=80
      - name: Upload coverage
        uses: codecov/codecov-action@v3
~~~

**Critérios de qualidade do pipeline:**

- Execução completa em ≤ 5 minutos (REQ-11)
- Falha imediata se coverage < 80%
- Bloqueio de merge se pipeline vermelho

### 5.5.2 Ciclos PDCA por Fase da EAP

**Fundamentação:** Cada uma das 12 fases da EAP (N1-N12, conforme baseline TAP §4) possui um ciclo PDCA específico, garantindo melhoria contínua sem burocracia excessiva. O TAP não integra ciclos PDCA (Premissa P9).

**Formato GMV:** Cada PDCA é documentado em máximo 6 linhas: Problema → Ação → Responsável → Métrica → Verificação → Lição.

## 5.6 CICLOS PDCA CONSOLIDADOS (12 FASES EAP)

### PDCA-N1: Iniciação e Planejamento

| Etapa                   | Descrição                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| **Problema**      | Risco de escopo mal definido ou premissas inválidas no início do projeto               |
| **Ação**        | Revisão em pares do TAP e EAP antes da submissão no M1; validação de premissas P1-P9 |
| **Responsável**  | Leonardo (GP) + Fabricio (par)                                                           |
| **Métrica**      | Zero inconsistências críticas identificadas pelo Prof. Dr. Nivaldo Carleto no M1       |
| **Verificação** | Validação acadêmica no M1 (22/09/2026)                                                |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1.md                          |

### PDCA-N2: Levantamento de Requisitos

| Etapa                   | Descrição                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| **Problema**      | Requisitos ambíguos ou não rastreáveis a objetivos SMART                              |
| **Ação**        | Conversão de REQ-01 a REQ-15 para formato User Story GWT (Padrão B, OKB §9.3) até M2 |
| **Responsável**  | Edson + Leonardo (revisão)                                                              |
| **Métrica**      | 100% dos requisitos Must (REQ-01 a REQ-09, REQ-11, REQ-15) com critérios GWT            |
| **Verificação** | Refinement semanal (23/09, 30/09)                                                        |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1.md                          |

### PDCA-N3: Modelagem e Prototipação

| Etapa                   | Descrição                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| **Problema**      | Arquitetura ou DER não validados antes da implementação                               |
| **Ação**        | Protótipo "Hello World" da stack (N4.1) + revisão de DER antes de N5 (Desenvolvimento) |
| **Responsável**  | Fabricio (DER) + Edson (protótipo)                                                      |
| **Métrica**      | Zero retrabalho de arquitetura após início de N5                                       |
| **Verificação** | Marco M2 (30/09/2026) — pipeline CI verde + DER versionado                              |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1.md                          |

### PDCA-N4: Configuração de Ambiente

| Etapa                   | Descrição                                                                   |
| ----------------------- | ----------------------------------------------------------------------------- |
| **Problema**      | Incompatibilidade de ferramentas FOSS ou ambiente local instável             |
| **Ação**        | Validação de stack via protótipo funcional + auditoria de licenças (N4.4) |
| **Responsável**  | Leonardo (stack) + Edson (auditoria)                                          |
| **Métrica**      | 100% das dependências com licença OSI-approved (Custos §4.5)               |
| **Verificação** | M2 (30/09/2026) — /docs/dependencias/registro.md atualizado                  |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1.md               |

### PDCA-N5: Desenvolvimento do Sistema

| Etapa                   | Descrição                                                                     |
| ----------------------- | ------------------------------------------------------------------------------- |
| **Problema**      | Código sem testes, coverage insuficiente ou SDD-IA sem revisão                |
| **Ação**        | TDD quando aplicável + code review obrigatório + tasklists Markdown (ADR-004) |
| **Responsável**  | Todos (desenvolvedores) + GP (supervisão)                                      |
| **Métrica**      | Coverage ≥ 80% por módulo; 100% dos commits SDD-IA com co-autoria declarada   |
| **Verificação** | Pipeline CI verde a cada push; Code Review antes de merge                       |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2.md                 |

### PDCA-N6: Garantia da Qualidade

| Etapa                   | Descrição                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------- |
| **Problema**      | Defeitos críticos em UAT ou coverage abaixo da meta                                        |
| **Ação**        | UAT estruturado com roteiro de testes + Ishikawa 6M para defeitos recorrentes (seção 5.7) |
| **Responsável**  | Edson (UAT) + GP (Ishikawa)                                                                 |
| **Métrica**      | Zero defeitos críticos/bloqueantes; coverage ≥ 80% consolidado                            |
| **Verificação** | M3 (15/11/2026) — relatório UAT + coverage.xml                                            |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2.md                             |

### PDCA-N7: DevOps e CI/CD

| Etapa                   | Descrição                                                     |
| ----------------------- | --------------------------------------------------------------- |
| **Problema**      | Pipeline lento (> 5min, conforme REQ-11) ou instável           |
| **Ação**        | Otimização de testes paralelos + cache de dependências       |
| **Responsável**  | Leonardo (CI) + Fabricio (otimização)                         |
| **Métrica**      | Tempo de CI ≤ 5 minutos (REQ-11); taxa de sucesso ≥ 95%       |
| **Verificação** | GitHub Actions Insights (semanal)                               |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2.md |

### PDCA-N8: Comunicação

| Etapa                   | Descrição                                                                |
| ----------------------- | -------------------------------------------------------------------------- |
| **Problema**      | Falhas de comunicação entre equipe ou com stakeholder                    |
| **Ação**        | Daily assíncrona padronizada + refinement semanal com pauta fixa          |
| **Responsável**  | GP (facilitação) + equipe (participação)                               |
| **Métrica**      | 100% das dailies realizadas; zero cards bloqueados > 48h sem comunicação |
| **Verificação** | GitHub Issues (daily) + GitHub Projects (refinement)                       |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2.md            |

### PDCA-N9: Base de Conhecimento

| Etapa                   | Descrição                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------- |
| **Problema**      | ADRs tardias ou prompts SDD não catalogados                                          |
| **Ação**        | Catálogo de prompts em .ai/handoffs/ + ADRs emitidas antes de M2 (quando aplicável) |
| **Responsável**  | Leonardo (ADRs) + todos (prompts)                                                     |
| **Métrica**      | 100% dos prompts versionados; ≤ 30% de ADRs tardias                                  |
| **Verificação** | /docs/decisoes/ + .ai/handoffs/ (semanal)                                             |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF3.md                       |

### PDCA-N10: Gestão de Mudanças

| Etapa                   | Descrição                                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------- |
| **Problema**      | Mudanças não registradas ou scope creep > 15% (Escopo §2.7, Integração §1.9)        |
| **Ação**        | Label`change-request` obrigatória + análise de impacto em ≤ 48h (Integração §1.7) |
| **Responsável**  | GP (CCB) + equipe (solicitações)                                                        |
| **Métrica**      | 100% das mudanças registradas; scope creep < 15% (Escopo §2.7)                          |
| **Verificação** | GitHub Issues com label`change-request`                                                 |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2.md                           |

### PDCA-N11: Documentação do Projeto

| Etapa                   | Descrição                                                               |
| ----------------------- | ------------------------------------------------------------------------- |
| **Problema**      | Documentação desatualizada ou inconsistente com código                 |
| **Ação**        | Código + docs no mesmo PR + revisão de consistência antes de M4        |
| **Responsável**  | Todos (documentação) + GP (consolidação)                              |
| **Métrica**      | 100% dos requisitos mapeados a docs; zero inconsistências TAP → código |
| **Verificação** | M4 (15/12/2026) — documentação consolidada                             |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF3.md           |

### PDCA-N12: Encerramento

| Etapa                   | Descrição                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------- |
| **Problema**      | Lições aprendidas não consolidadas ou critérios SMART não verificados          |
| **Ação**        | Checklist de encerramento + lições finais + tag de release                        |
| **Responsável**  | GP (consolidação) + equipe (lições)                                             |
| **Métrica**      | 100% dos critérios SMART verificados; lições consolidadas em /docs/conhecimento/ |
| **Verificação** | M4 (15/12/2026) — validação acadêmica + tag de release                          |
| **Lição**       | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF3.md                     |

## 5.7 DIAGRAMA DE ISHIKAWA 6M (3 ANÁLISES)

**Fundamentação:** Conforme REQ-10 e N6.3 da EAP, três diagramas de Ishikawa 6M são aplicados para análise de causa-raiz de problemas críticos de qualidade. Cada diagrama foca em um efeito indesejado específico.

**Nota sobre qualidade de processo vs. produto (I3):** Os dois primeiros diagramas (Coverage < 80% e Defeitos Críticos em UAT) analisam qualidade de produto. O terceiro diagrama (Cycle Time > 3 dias) analisa qualidade de processo — especificamente, eficiência do fluxo de trabalho. Ambos os tipos são ferramentas da qualidade conforme REQ-10, e a delimitação entre eles é explicitada na seção 5.8.2.

### Ishikawa-1: Coverage < 80%

**[FIG-3 — Ishikawa: Coverage Insuficiente]**
*SVG gerado — Diagrama espinha-de-peixe tradicional 6M*

![FIG-3 — Ishikawa: Coverage Insuficiente](../../../diagrams/fig-05-ishikawa-coverage.png)

*Conteúdo:* Diagrama 6M (Método, Mão de Obra, Máquina, Material, Medida, Meio Ambiente) com causas-raiz específicas do COGME.
*Necessidade real:* Permite ao GP e equipe identificar ações corretivas priorizadas (ex: tornar coverage gate obrigatório no CI) em vez de tratar sintomas.

**Ações corretivas derivadas:**

1. **Método:** Implementar TDD obrigatório para REQ-01 a REQ-07 (críticos)
2. **Medida:** Configurar `--cov-fail-under=80` no pipeline CI (gate bloqueante)
3. **Mão de Obra:** Pair programming para módulos complexos (N5.1, N5.2)

### Ishikawa-2: Defeitos Críticos em UAT

**[FIG-4 — Ishikawa: Defeitos Críticos em UAT]**
*SVG gerado — Diagrama espinha-de-peixe tradicional 6M*

![FIG-4 — Ishikawa: Defeitos Críticos em UAT](../../../diagrams/fig-06-ishikawa-uat.png)

*Conteúdo:* Diagrama 6M focado em defeitos de UAT, destacando causas relacionadas a SDD-IA e validação acadêmica.
*Necessidade real:* Evidencia para o Prof. Dr. Nivaldo Carleto que a equipe compreende as limitações do ambiente acadêmico (usuários-piloto limitados) e propõe mitigações (UAT estruturado).

**Ações corretivas derivadas:**

1. **Método:** Roteiro de UAT com cenários Given/When/Then para REQ-01 a REQ-07
2. **Mão de Obra:** Code review cruzado (Fabricio revisa Edson, Edson revisa Leonardo)
3. **Medida:** Label `bug-critical` no GitHub com template de reporte padronizado

### Ishikawa-3: Desvio de Cycle Time > 3 dias

**[FIG-5 — Ishikawa: Cycle Time Excedido]**
*SVG gerado — Diagrama espinha-de-peixe tradicional 6M*

![FIG-5 — Ishikawa: Cycle Time Excedido](../../../diagrams/fig-05-ishikawa-coverage.png)

*Conteúdo:* Diagrama 6M focado em gargalos de fluxo, conectando causas a ADR-002 (Kanban) e ADR-004 (tasklists).
*Necessidade real:* Demonstra ao avaliador que a equipe entende que "Cycle Time > 3 dias" não é falha individual, mas sistêmica, exigindo ações em múltiplas dimensões.

**Ações corretivas derivadas:**

1. **Método:** DoR gate rigoroso (Escopo §2.6) — card sem DoR não entra em `Ready`
2. **Mão de Obra:** Cross-training para reduzir dependência de membro único
3. **Medida:** Publicação semanal de CFD (Integração §1.6.1) + ação corretiva se banda > 2× média

## 5.8 GESTÃO DE MELHORIA CONTÍNUA

### 5.8.1 Retrospectivas Quinzenais

Conforme ADR-002, retrospectivas ocorrem a cada 2 semanas com pauta fixa:

1. O que funcionou bem?
2. O que pode melhorar?
3. Ações para o próximo ciclo (máximo 3)

**Registro:** /docs/conhecimento/licoes-aprendidas/ (MF1, MF2, MF3)

### 5.8.2 Integração com Métricas de Fluxo

Conforme Cronograma §3.7 e Integração §1.6.1, o CFD e Cycle Time alimentam a melhoria de processo:

- CFD com banda > 2× média por 2 semanas → Retrospectiva extraordinária
- Throughput < 3 cards/semana por 2 semanas → Revisão de WIP limits (fallback ADR-002)

**Fronteira com Cronograma (I4):** Este plano usa métricas de fluxo como *input* para melhoria de qualidade de processo, não como métrica de qualidade de produto (que são coverage, defeitos, etc.). A definição formal, cadência e regra corretiva do CFD residem canonicamente em Integração §1.6.1; o monitoramento temporal detalhado reside em Cronograma §3.7.

## 5.9 NOTAS DE CONTEXTO E REGISTRO DE SANEAMENTO DOS ARTEFATOS VIVOS

**NC-Q1 — Regime de Freeze do TAP (Diretriz D3):**
O TAP é referência autorizativa congelada (última versão: 18/09/2026, anterior a todos os planos). Divergências textuais entre este plano e o TAP são leituras operacionais, não correções do termo autorizativo. Fontes: TAP Controle de Versões; Premissa P9; Glossário §11; PMBOK 6ª §4.1.

**NC-Q2 — Numeração de Processos no Glossário:**
O Glossário registra incorretamente "Processo 6.4 Estimar Custos" na seção de Cronograma. A numeração canônica é: Área 7 (Custos), Processo 7.2 (Estimar Custos). Esta inconsistência é registrada para saneamento na próxima revisão do Glossário (pós-M1). Similarmente, processos de qualidade (8.1-8.3) devem ser verificados no Glossário §3.

**NC-Q3 — Cycle Time e Definição Operacional:**
A definição operacional de Cycle Time aqui vigente é `In Progress` → `Done` (ADR-003), prevalecendo sobre redações divergentes em artefatos de origem (ex: Glossário que possa citar "To Do → Done"). O saneamento aplica-se apenas aos artefatos vivos (ADR-003, Glossário, baseline).

**NC-Q4 — EAP: 12 Fases, não 13:**
Este plano consolida 12 ciclos PDCA (N1-N12), conforme baseline do TAP §4 (12 fases + 37 pacotes). O Glossário v3.1 pode registrar "13 fases + 48 pacotes" — esta contagem é volátil e não canônica. O TAP e Planos de Integração/Escopo são as fontes canônicas. O TAP não integra ciclos PDCA (Premissa P9).

**NC-Q5 — Grafia do Stakeholder (E1):**
A seção 5 utiliza a grafia "Prof. Dr. Nivaldo Carleto" conforme TAP v3. O Glossário v3.1 registra "Carleto" (grafia incorreta). Esta inconsistência é registrada para saneamento na próxima revisão do Glossário (pós-M1).

**Registro de saneamento — artefatos vivos (não bloqueante):**

| Pendência                                          | Artefato vivo  | Momento previsto                |
| --------------------------------------------------- | -------------- | ------------------------------- |
| Numeração de processos 8.1-8.3                    | Glossário §3 | Próxima revisão do Glossário |
| Contagem EAP "13/48" → 12/37                       | Glossário §1 | Próxima revisão do Glossário |
| Cycle Time "To Do → Done" → "In Progress → Done" | Glossário     | Próxima revisão do Glossário |
| Grafia "Carleto" → "Carleto"                      | Glossário     | Próxima revisão do Glossário |

## 5.10 DECLARAÇÃO DE RASTREABILIDADE

| Seção                      | Origem no TAP                             | Domínio PMBOK 7ª   | Processo PMBOK 6ª   |
| ---------------------------- | ----------------------------------------- | -------------------- | -------------------- |
| 5.1 (Propósito; freeze)     | §3.2 (Qualidade) + Premissa P9           | Medição + Entrega  | 8.1                  |
| 5.2 (Abordagem 3 dimensões) | §3 (Qualidade) + §8.5                   | Entrega + Melhoria   | 8.2                  |
| 5.3 (Métricas)              | §3 (Métricas) + ADR-003                 | Medição            | 8.3 (substituição) |
| 5.4 (Critérios técnicos)   | §3.2.b + §3.2.c                         | Entrega              | 8.3                  |
| 5.5 (Ferramentas: CI)        | §3 (Inovação) + N7.1                   | Trabalho do Projeto  | 8.2                  |
| 5.6 (12 PDCAs)               | §3.2.c + REQ-10 + N6.3                   | Melhoria             | 8.2                  |
| 5.7 (Ishikawa 6M)            | REQ-10 + N6.3                             | Melhoria + Incerteza | 8.3                  |
| 5.8 (Melhoria contínua)     | ADR-002 + Integração §1.6.1            | Melhoria             | 8.2                  |
| 5.9 (Notas de Contexto)      | Decisão do GP (21/09/2026) + Premissa P9 | Trabalho do Projeto  | 4.6 (dicionário)    |

**Verificação:** 100% das seções possuem rastreabilidade a ao menos um objetivo SMART, premissa, restrição do TAP ou REQ-08/09/10; referências cruzadas apontam exclusivamente para locais canônicos (Escopo §2.6 para DoR/DoD; Custos §4.5 para auditoria FOSS; Integração §1.6.1 para CFD).

## 5.11 PREMISSAS E RESTRIÇÕES APLICÁVEIS

**Premissas do TAP:**

- P1 (governança híbrida): fundamenta §5.2
- P3 (SDD com IA auditável): fundamenta §5.4.1 (código SDD)
- P4 (código como deliverable): fundamenta §5.4 (critérios técnicos)
- P5 (20h/semana): fundamenta §5.7 (Ishikawa-3: sobrecarga)
- P9 (separação ontológica TAP ≠ EAP ≠ PDCA): fundamenta §5.6 (12 PDCAs sem TAP) e §5.9 (freeze)

**Premissas específicas deste plano:**

- PA-Q1: GitHub Actions Free Tier permanece disponível e estável durante todo o ciclo (TAP §11)
- PA-Q2: pytest + coverage.py são suficientes para atingir ≥ 80% de cobertura sem ferramentas pagas
- PA-Q3: Usuários-piloto (3-5 pessoas) são representativos o suficiente para UAT acadêmico (TAP §8.5)
- PA-Q4: SonarQube Free Tier permanece disponível para análise de dívida técnica (TAP §11)

**Restrições:**

- TAP §8.5 (Qualidade): Tempo restrito para testes → priorização de fluxos críticos (REQ-01 a REQ-07)
- TAP §8.2 (Cronograma): Prazo letivo inegociável → PDCAs enxutos (6 linhas cada, GMV)
- TAP §11 (Orçamento zero): Proibição de ferramentas pagas de qualidade (ex: SonarCloud pago)

---

## CONTROLE DE VERSÕES

| Versão | Data       | Alteração                                                                                                                                                                                                                                                                                                                                                                                                                                               | Responsável         |
| ------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| 1.0     | 21/09/2026 | Emissão inicial: 12 PDCAs consolidados (N1-N12); 3 diagramas Ishikawa 6M; métricas de qualidade; FIG-1, FIG-3, FIG-4, FIG-5; exclusão de FIG-2 (GMV); NC-Q1 a NC-Q4 (freeze do TAP); delimitação de fronteiras com Custos §4.5 e Cronograma §3.7                                                                                                                                                                                                   | Leonardo D. S. Setti |
| 1.1     | 21/09/2026 | Refinamento pós-review: (I1) PDCA-N10 com referência a Escopo §2.7 e Integração §1.9; (I2) PDCA-N7 com referência a REQ-11; (I3) nota sobre qualidade de processo vs. produto na introdução §5.7; (I4) referência canônica em §5.8.2; (I5) especificação "SonarQube Free Tier" em §5.3; (I6) nota sobre mypy como ferramenta complementar em §5.4.1; (E1) NC-Q5 sobre grafia do stakeholder; 4 SVGs gerados (FIG-1, FIG-3, FIG-4, FIG-5) | Leonardo D. S. Setti |
