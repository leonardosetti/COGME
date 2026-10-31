# Notas Adjacentes — Projeto COGME

**Natureza:** Documento de apoio não canônico · Registro operacional · Ações ad-hoc
**Classificação:** `chore` — não integra a estrutura formal do projeto
**Hierarquia:** TAP > OKB > Glossário > ADRs > **Notas Adjacentes (este documento)**
**Data de referência:** 19–22/09/2026 (MF1 — Fundação)
**GP:** Leonardo David Silva Setti
**Stakeholder-Avaliador:** Prof. Dr. Nivaldo Carleto

> **Nota de uso:** Este documento registra raciocínio operacional, decisões ad-hoc e produção visual do ciclo 19–22/09/2026. Menções ao OKB, Glossário e ADRs são exclusivamente para orientação interna de navegação — as fontes canônicas residem nos respectivos artefatos em `/docs/`. Em caso de conflito, o artefato canônico prevalece.

---

## 0. Metadados e Linha do Tempo

| Campo | Valor |
|-------|-------|
| Projeto | COGME — Conversor de Ganhos em Moeda Estrangeira |
| Instituição | Fatec Taquaritinga — ADS |
| Equipe | Leonardo, Fabricio, Edson |
| Marco ativo | M1 — Entrega Parcial Documental (22/09/2026) |
| Artefatos gráficos | 14 SVGs (13 únicos + 1 refação por overlap) |
| Configuração SSOT | 27 labels, 5 milestones, 21 cards M1 |

### Linha do tempo sintética

~~~
19/09/2026
  ├── OKB v2.2 vigente
  ├── Backlog M1 original (10 cards)
  ├── Inconsistência de fronteira M1 detectada (5 vs 8 planos)
  └── Correção: Entrega Faseada (5 planos M1 + 3 planos M2)

20/09/2026
  ├── Flag de Estado: Revisão Diferida (PDCA futuro)
  ├── OKB v3.0 emitido (substitui v2.2)
  ├── ADR-004 emitida (Tasklists Markdown)
  ├── Política de ADRs e Integração Documental (Aditivo)
  ├── Configuração GitHub formalizada (27 labels, 5 milestones)
  ├── Padrões de Redação de Cards (A/B) + P0–P3
  ├── Backlog M1 consolidado (21 cards)
  └── Rodada 1: EAP fracionada (4 SVGs)

21/09/2026
  ├── Rodada 2: Governança + Mudanças (2 SVGs)
  ├── Rodada 3: CFD + Sequenciamento (2 SVGs)
  ├── Correção 3.5: Fix de overlap (1 SVG refeito)
  ├── Notas ABNT retroativas (7 figuras)
  ├── Rodada 4: Fluxo Kanban (1 SVG)
  ├── Rodada 5: Custos (2 SVGs)
  ├── Rodada 6: Escopo (2 SVGs)
  └── Proposta de Reestruturação do Repositório

22/09/2026
  └── LA-001: Incidente de reestruturação paralela
~~~

---

## 1. Flag de Estado: Revisão Diferida (PDCA Futuro)

**Natureza:** Metadado de sessão não canônico. Não integra documentação formal.

**Veredito:** A produção das seções do Plano de Gerenciamento prossegue sem interrupção; a revisão integral será alocada como item de entrada para um ciclo PDCA futuro, sem contaminar a saída formal atual.

**Riscos identificados:**
- Técnico: deriva de escopo se a revisão futura não possuir critérios de aceitação definidos
- Humano: stakeholders consumirem a versão atual como definitiva

**Gatilho de reavaliação:** Comando explícito: "Iniciar revisão integral do Plano de Gerenciamento (PDCA)".

**Premissas:** Esta nota é estado transitório de projeto. O ciclo PDCA deve iniciar com critérios objetivos, evitando "revisão por revisão" sem ganho de valor.

---

## 2. Notas de Orientação Técnica (Literatura de Apoio)

> **Orientação interna:** O conteúdo canônico destas questões reside no OKB §8 (Literatura de Apoio — Questões Adjacentes). As notas abaixo registram o raciocínio que originou aquelas decisões.

### 2.1 Rede de Projeto e Caminho Crítico

**Questão:** Qual área de conhecimento deve conter a rede de projeto para cálculo de precedências e caminhos críticos?

**Resolução aplicada:**
- PMBOK 6ª (dicionário): Gerenciamento do Cronograma — Processos 6.4 e 6.6
- PMBOK 7ª (governança): Domínio de Planejamento + Domínio de Medição
- No COGME: CPM/Gantt declarados LEGADO (ADR-003). Caminho crítico identificado empiricamente via CFD, Cycle Time, cards P0 e label `blocked`
- Trade-off: formalidade preditiva → métricas de fluxo nativas Kanban

### 2.2 Estruturação do CFD para Demonstração Formal

**Resolução aplicada:**
- CFD aparece em três artefatos: Integração §1.6.1 (definição), Cronograma §2.3 (monitoramento), Comunicações §3.2 (relatório)
- Regra GMV: não criar artefato separado — CFD é nativo do GitHub Insights
- Para M1: apenas definição formal; primeiro CFD real após calibração (06/10/2026)
- Blindagem acadêmica: três pilares (Domínio Medição PMBOK 7ª, orçamento zero, fluxo contínuo)

### 2.3 Fronteira M1 — Inconsistência Sanada

**Questão:** TAP §6 declara 5 planos; OKB v2.2 lista 8.

**Resolução:** Elaboração Progressiva (PMBOK 6ª) + Tailoring (PMBOK 7ª). M1 = 5 planos (Áreas 1–5). M2 = 3 planos (Áreas 6–8). TAP §6 correto como linha de base faseada. OKB correto como inventário total.

---

## 3. Produção Visual — Rodadas de Diagramas

**Diretrizes de padronização:**
- Fundo: `#FFFFFF` · Tipografia: `Arial, Helvetica, sans-serif`
- N0 (Raiz): `#111111` · MF1: `#1F3A5F` · MF2: `#2E7D32` · MF3: `#6A1B9A`
- Pacotes Nível 2: `#F8F9FA` com bordas `#555555`
- Sem overlaps · Sem legendas internas (ABNT externo) · Margens seguras

### 3.1 Rodada 1 — EAP Fracionada (4 SVGs) — 20/09/2026

**Justificativa do fracionamento:** Diagrama único com 12 fases e 37 pacotes exigiria `viewBox` excessivamente largo (~3000×1000), resultando em fontes < 10px. Fracionamento em 4 camadas preserva legibilidade ABNT.

#### FIG-EAP-01: `fig-eap-nivel-0-macro.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" font-family="Arial, Helvetica, sans-serif">
   <rect x="0" y="0" width="1200" height="500" fill="#FFFFFF"/>
   <text x="600" y="42" text-anchor="middle" font-size="23" font-weight="bold" fill="#111111">Estrutura Analítica do Projeto (EAP) — Visão Macro</text>
   <!-- N0 -->
   <rect x="450" y="80" width="300" height="60" rx="6" fill="#111111" stroke="#111111" stroke-width="2"/>
   <text x="600" y="116" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">N0: COGME</text>
   <!-- Linhas para MFs -->
   <line x1="600" y1="140" x2="600" y2="180" stroke="#777777" stroke-width="2"/>
   <line x1="200" y1="180" x2="1000" y2="180" stroke="#777777" stroke-width="2"/>
   <line x1="200" y1="180" x2="200" y2="220" stroke="#777777" stroke-width="2"/>
   <line x1="600" y1="180" x2="600" y2="220" stroke="#777777" stroke-width="2"/>
   <line x1="1000" y1="180" x2="1000" y2="220" stroke="#777777" stroke-width="2"/>
   <!-- MF1 -->
   <rect x="50" y="220" width="300" height="240" rx="6" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="3"/>
   <rect x="50" y="220" width="300" height="40" rx="6" fill="#1F3A5F"/>
   <text x="200" y="246" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">MF1: Fundação</text>
   <text x="200" y="280" text-anchor="middle" font-size="14" fill="#111111">N1. Iniciação e Planejamento</text>
   <text x="200" y="305" text-anchor="middle" font-size="14" fill="#111111">N2. Levantamento de Requisitos</text>
   <text x="200" y="330" text-anchor="middle" font-size="14" fill="#111111">N3. Modelagem e Prototipação</text>
   <text x="200" y="355" text-anchor="middle" font-size="14" fill="#111111">N4. Configuração de Ambiente</text>
   <text x="200" y="380" text-anchor="middle" font-size="14" fill="#111111">N8. Comunicação</text>
   <text x="200" y="405" text-anchor="middle" font-size="14" fill="#111111">N9. Base de Conhecimento</text>
   <!-- MF2 -->
   <rect x="450" y="220" width="300" height="240" rx="6" fill="#FFFFFF" stroke="#2E7D32" stroke-width="3"/>
   <rect x="450" y="220" width="300" height="40" rx="6" fill="#2E7D32"/>
   <text x="600" y="246" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">MF2: Construção</text>
   <text x="600" y="280" text-anchor="middle" font-size="14" fill="#111111">N5. Desenvolvimento do Sistema</text>
   <text x="600" y="305" text-anchor="middle" font-size="14" fill="#111111">N6. Garantia da Qualidade</text>
   <text x="600" y="330" text-anchor="middle" font-size="14" fill="#111111">N7. DevOps e CI/CD</text>
   <text x="600" y="355" text-anchor="middle" font-size="14" fill="#111111">N10. Gestão de Mudanças</text>
   <!-- MF3 -->
   <rect x="850" y="220" width="300" height="240" rx="6" fill="#FFFFFF" stroke="#6A1B9A" stroke-width="3"/>
   <rect x="850" y="220" width="300" height="40" rx="6" fill="#6A1B9A"/>
   <text x="1000" y="246" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">MF3: Consolidação</text>
   <text x="1000" y="280" text-anchor="middle" font-size="14" fill="#111111">N11. Documentação do Projeto</text>
   <text x="1000" y="305" text-anchor="middle" font-size="14" fill="#111111">N12. Encerramento</text>
 </svg>
~~~

#### FIG-EAP-02: `fig-eap-mf1-fundacao.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 900" font-family="Arial, Helvetica, sans-serif">
   <rect x="0" y="0" width="1600" height="900" fill="#FFFFFF"/>
   <text x="800" y="42" text-anchor="middle" font-size="23" font-weight="bold" fill="#111111">EAP — Macro-Fase 1: Fundação (MF1)</text>
   <!-- N1 -->
   <g transform="translate(60, 100)">
     <rect x="0" y="0" width="220" height="50" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
     <text x="110" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N1. Iniciação e Planejamento</text>
     <line x1="110" y1="50" x2="110" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="105" text-anchor="middle" font-size="12" fill="#222222">N1.1 Identificação de Stakeholders</text>
     <rect x="10" y="130" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="155" text-anchor="middle" font-size="12" fill="#222222">N1.2 Planos de Gerenciamento</text>
     <rect x="10" y="180" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="205" text-anchor="middle" font-size="12" fill="#222222">N1.3 Plano da Qualidade</text>
     <rect x="10" y="230" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="255" text-anchor="middle" font-size="12" fill="#222222">N1.4 Política de Licenciamento FOSS</text>
     <rect x="10" y="280" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="305" text-anchor="middle" font-size="12" fill="#222222">N1.5 Definição do Backlog e Kanban</text>
   </g>
   <!-- N2 -->
   <g transform="translate(320, 100)">
     <rect x="0" y="0" width="220" height="50" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
     <text x="110" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N2. Levantamento de Requisitos</text>
     <line x1="110" y1="50" x2="110" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="105" text-anchor="middle" font-size="12" fill="#222222">N2.1 Requisitos Funcionais</text>
     <rect x="10" y="130" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="155" text-anchor="middle" font-size="12" fill="#222222">N2.2 Requisitos Não Funcionais</text>
     <rect x="10" y="180" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="205" text-anchor="middle" font-size="12" fill="#222222">N2.3 Casos de Uso e Histórias</text>
   </g>
   <!-- N3 -->
   <g transform="translate(580, 100)">
     <rect x="0" y="0" width="220" height="50" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
     <text x="110" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N3. Modelagem e Prototipação</text>
     <line x1="110" y1="50" x2="110" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="105" text-anchor="middle" font-size="12" fill="#222222">N3.1 Arquitetura da Solução</text>
     <rect x="10" y="130" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="155" text-anchor="middle" font-size="12" fill="#222222">N3.2 Protótipo UX/UI</text>
     <rect x="10" y="180" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="205" text-anchor="middle" font-size="12" fill="#222222">N3.3 Modelagem de Dados (DER)</text>
   </g>
   <!-- N4 -->
   <g transform="translate(840, 100)">
     <rect x="0" y="0" width="220" height="50" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
     <text x="110" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N4. Configuração de Ambiente</text>
     <line x1="110" y1="50" x2="110" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="105" text-anchor="middle" font-size="12" fill="#222222">N4.1 Seleção e Validação da Stack</text>
     <rect x="10" y="130" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="155" text-anchor="middle" font-size="12" fill="#222222">N4.2 Repositório Git + CI/CD</text>
     <rect x="10" y="180" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="205" text-anchor="middle" font-size="12" fill="#222222">N4.3 Setup Local e Homologação</text>
     <rect x="10" y="230" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="255" text-anchor="middle" font-size="12" fill="#222222">N4.4 Auditoria de Licenças</text>
   </g>
   <!-- N8 -->
   <g transform="translate(1100, 100)">
     <rect x="0" y="0" width="220" height="50" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
     <text x="110" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N8. Comunicação</text>
     <line x1="110" y1="50" x2="110" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="105" text-anchor="middle" font-size="12" fill="#222222">N8.1 Matriz de Comunicação (RACI)</text>
     <rect x="10" y="130" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="155" text-anchor="middle" font-size="12" fill="#222222">N8.2 Canais Oficiais</text>
   </g>
   <!-- N9 -->
   <g transform="translate(1360, 100)">
     <rect x="0" y="0" width="220" height="50" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
     <text x="110" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N9. Base de Conhecimento</text>
     <line x1="110" y1="50" x2="110" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="105" text-anchor="middle" font-size="12" fill="#222222">N9.1 ADRs (decisões arquiteturais)</text>
     <rect x="10" y="130" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="155" text-anchor="middle" font-size="12" fill="#222222">N9.2 Lições Aprendidas Contínuas</text>
     <rect x="10" y="180" width="200" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="110" y="205" text-anchor="middle" font-size="12" fill="#222222">N9.3 Catálogo de Prompts SDD</text>
   </g>
 </svg>
~~~

#### FIG-EAP-03: `fig-eap-mf2-construcao.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 700" font-family="Arial, Helvetica, sans-serif">
   <rect x="0" y="0" width="1200" height="700" fill="#FFFFFF"/>
   <text x="600" y="42" text-anchor="middle" font-size="23" font-weight="bold" fill="#111111">EAP — Macro-Fase 2: Construção (MF2)</text>
   <!-- N5 -->
   <g transform="translate(60, 100)">
     <rect x="0" y="0" width="240" height="50" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
     <text x="120" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N5. Desenvolvimento do Sistema</text>
     <line x1="120" y1="50" x2="120" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="105" text-anchor="middle" font-size="12" fill="#222222">N5.1 Backend — Lógica de Negócio</text>
     <rect x="10" y="130" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="155" text-anchor="middle" font-size="12" fill="#222222">N5.2 Backend — API de Câmbio + Cache</text>
     <rect x="10" y="180" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="205" text-anchor="middle" font-size="12" fill="#222222">N5.3 Frontend — Interface e Simulações</text>
     <rect x="10" y="230" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="255" text-anchor="middle" font-size="12" fill="#222222">N5.4 Módulo PDF (WeasyPrint)</text>
     <rect x="10" y="280" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="305" text-anchor="middle" font-size="12" fill="#222222">N5.5 SDD com IA (Prompts + Revisão)</text>
   </g>
   <!-- N6 -->
   <g transform="translate(340, 100)">
     <rect x="0" y="0" width="240" height="50" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
     <text x="120" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N6. Garantia da Qualidade</text>
     <line x1="120" y1="50" x2="120" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="105" text-anchor="middle" font-size="12" fill="#222222">N6.1 Testes Unitários/Integração (≥ 80%)</text>
     <rect x="10" y="130" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="155" text-anchor="middle" font-size="12" fill="#222222">N6.2 Testes de Aceitação (UAT)</text>
     <rect x="10" y="180" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="205" text-anchor="middle" font-size="12" fill="#222222">N6.3 Ferramentas da Qualidade (12 PDCAs)</text>
   </g>
   <!-- N7 -->
   <g transform="translate(620, 100)">
     <rect x="0" y="0" width="240" height="50" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
     <text x="120" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N7. DevOps e CI/CD</text>
     <line x1="120" y1="50" x2="120" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="105" text-anchor="middle" font-size="12" fill="#222222">N7.1 Pipeline CI (lint + testes)</text>
   </g>
   <!-- N10 -->
   <g transform="translate(900, 100)">
     <rect x="0" y="0" width="240" height="50" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
     <text x="120" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N10. Gestão de Mudanças</text>
     <line x1="120" y1="50" x2="120" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="105" text-anchor="middle" font-size="12" fill="#222222">N10.1 Registro de Solicitações</text>
     <rect x="10" y="130" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="155" text-anchor="middle" font-size="12" fill="#222222">N10.2 Label change-request no GitHub</text>
     <rect x="10" y="180" width="220" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="120" y="205" text-anchor="middle" font-size="12" fill="#222222">N10.3 Aprovação e Versionamento</text>
   </g>
 </svg>
~~~

#### FIG-EAP-04: `fig-eap-mf3-consolidacao.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" font-family="Arial, Helvetica, sans-serif">
   <rect x="0" y="0" width="800" height="500" fill="#FFFFFF"/>
   <text x="400" y="42" text-anchor="middle" font-size="23" font-weight="bold" fill="#111111">EAP — Macro-Fase 3: Consolidação (MF3)</text>
   <!-- N11 -->
   <g transform="translate(100, 100)">
     <rect x="0" y="0" width="260" height="50" rx="4" fill="#FFFFFF" stroke="#6A1B9A" stroke-width="2"/>
     <text x="130" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N11. Documentação do Projeto</text>
     <line x1="130" y1="50" x2="130" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="240" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="130" y="105" text-anchor="middle" font-size="12" fill="#222222">N11.1 Documentação Técnica (Arquitetura)</text>
     <rect x="10" y="130" width="240" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="130" y="155" text-anchor="middle" font-size="12" fill="#222222">N11.2 Consolidação da Documentação Parcial</text>
   </g>
   <!-- N12 -->
   <g transform="translate(440, 100)">
     <rect x="0" y="0" width="260" height="50" rx="4" fill="#FFFFFF" stroke="#6A1B9A" stroke-width="2"/>
     <text x="130" y="30" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">N12. Encerramento</text>
     <line x1="130" y1="50" x2="130" y2="80" stroke="#777777" stroke-width="1.5"/>
     <rect x="10" y="80" width="240" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="130" y="105" text-anchor="middle" font-size="12" fill="#222222">N12.1 Lições Aprendidas Finais</text>
     <rect x="10" y="130" width="240" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="130" y="155" text-anchor="middle" font-size="12" fill="#222222">N12.2 Verificação SMART</text>
     <rect x="10" y="180" width="240" height="40" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1.5"/>
     <text x="130" y="205" text-anchor="middle" font-size="12" fill="#222222">N12.3 Apresentação Final + Aceite</text>
   </g>
 </svg>
~~~

### 3.2 Rodada 2 — Governança e Mudanças (2 SVGs) — 21/09/2026

#### FIG-GOV-01: `fig-1-governanca-hibrida.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" font-family="Arial, Helvetica, sans-serif">
   <defs>
     <marker id="ar" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
       <path d="M0,0 L9,3 L0,6 Z" fill="#1F3A5F"/>
     </marker>
     <marker id="ar-green" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
       <path d="M0,0 L9,3 L0,6 Z" fill="#2E7D32"/>
     </marker>
   </defs>
   <rect x="0" y="0" width="800" height="600" fill="#FFFFFF"/>
   <text x="400" y="40" text-anchor="middle" font-size="20" font-weight="bold" fill="#111111">Modelo de Governança Híbrida Trifásico</text>
   <rect x="150" y="80" width="500" height="100" rx="6" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
   <text x="400" y="115" text-anchor="middle" font-size="18" font-weight="bold" fill="#FFFFFF">PMBOK® 7ª Edição</text>
   <text x="400" y="140" text-anchor="middle" font-size="14" fill="#E0E7EF">12 Princípios + 8 Domínios de Desempenho</text>
   <text x="400" y="160" text-anchor="middle" font-size="13" fill="#E0E7EF">(Governança Primária: Por que e Para quê)</text>
   <line x1="400" y1="180" x2="400" y2="210" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar)"/>
   <text x="415" y="200" font-size="11" fill="#555555">Autoridade Normativa</text>
   <rect x="150" y="220" width="500" height="100" rx="6" fill="#F8F9FA" stroke="#546E7A" stroke-width="2" stroke-dasharray="6,4"/>
   <text x="400" y="255" text-anchor="middle" font-size="18" font-weight="bold" fill="#37474F">PMBOK® 6ª Edição</text>
   <text x="400" y="280" text-anchor="middle" font-size="14" fill="#555555">Processos como Dicionário Complementar</text>
   <text x="400" y="300" text-anchor="middle" font-size="13" fill="#C0392B" font-weight="bold">Obsolescência Assumida para Métricas Preditivas (EVM)</text>
   <line x1="400" y1="320" x2="400" y2="350" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar)"/>
   <text x="415" y="340" font-size="11" fill="#555555">Vocabulário Estrutural</text>
   <rect x="150" y="360" width="500" height="100" rx="6" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
   <text x="400" y="395" text-anchor="middle" font-size="18" font-weight="bold" fill="#FFFFFF">Manifesto Ágil + Kanban (GitHub Projects)</text>
   <text x="400" y="420" text-anchor="middle" font-size="14" fill="#E8F5E9">Fluxo Contínuo, WIP Limits e Métricas de Fluxo</text>
   <text x="400" y="440" text-anchor="middle" font-size="13" fill="#E8F5E9">(Método de Execução: Como o trabalho flui)</text>
   <path d="M 650 410 Q 720 410 720 270 Q 720 130 650 130" fill="none" stroke="#2E7D32" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#ar-green)"/>
   <text x="735" y="275" font-size="12" font-weight="bold" fill="#2E7D32" text-anchor="start">Lições Aprendidas</text>
   <text x="735" y="290" font-size="12" font-weight="bold" fill="#2E7D32" text-anchor="start">e Realimentação</text>
 </svg>
~~~

#### FIG-MUD-01: `fig-4-controle-mudancas.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 650" font-family="Arial, Helvetica, sans-serif">
   <defs>
     <marker id="ar-flow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
       <path d="M0,0 L9,3 L0,6 Z" fill="#1F3A5F"/>
     </marker>
     <marker id="ar-reject" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
       <path d="M0,0 L9,3 L0,6 Z" fill="#C0392B"/>
     </marker>
     <marker id="ar-approve" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
       <path d="M0,0 L9,3 L0,6 Z" fill="#2E7D32"/>
     </marker>
   </defs>
   <rect x="0" y="0" width="800" height="650" fill="#FFFFFF"/>
   <text x="400" y="40" text-anchor="middle" font-size="20" font-weight="bold" fill="#111111">Fluxo de Controle Integrado de Mudanças</text>
   <rect x="200" y="70" width="400" height="60" rx="4" fill="#F8F9FA" stroke="#1F3A5F" stroke-width="2"/>
   <text x="400" y="95" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">1. Abertura de Issue com label</text>
   <text x="400" y="115" text-anchor="middle" font-size="13" fill="#333333">change-request (Qualquer membro | Prazo: Imediato)</text>
   <line x1="400" y1="130" x2="400" y2="160" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <text x="415" y="150" font-size="11" fill="#555555">Imediato</text>
   <rect x="200" y="160" width="400" height="60" rx="4" fill="#F8F9FA" stroke="#1F3A5F" stroke-width="2"/>
   <text x="400" y="185" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">2. Análise de impacto (escopo, prazo, qualidade)</text>
   <text x="400" y="205" text-anchor="middle" font-size="13" fill="#333333">Responsável: GP (CCB membro único) | Prazo: ≤ 48h</text>
   <line x1="400" y1="220" x2="400" y2="250" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <text x="415" y="240" font-size="11" fill="#555555">≤ 48h</text>
   <polygon points="400,260 540,300 400,340 260,300" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
   <text x="400" y="295" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">3. Aprovação</text>
   <text x="400" y="315" text-anchor="middle" font-size="12" fill="#333333">pelo CCB (GP)</text>
   <text x="400" y="330" text-anchor="middle" font-size="11" fill="#555555">Prazo: ≤ 24h</text>
   <line x1="540" y1="300" x2="620" y2="300" stroke="#C0392B" stroke-width="2" marker-end="url(#ar-reject)"/>
   <rect x="620" y="270" width="150" height="60" rx="4" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
   <text x="695" y="295" text-anchor="middle" font-size="13" font-weight="bold" fill="#C0392B">Rejeitada</text>
   <text x="695" y="315" text-anchor="middle" font-size="11" fill="#333333">Encerramento com</text>
   <text x="695" y="330" text-anchor="middle" font-size="11" fill="#333333">registro na Issue</text>
   <line x1="400" y1="340" x2="400" y2="380" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-approve)"/>
   <text x="415" y="365" font-size="11" fill="#2E7D32" font-weight="bold">Aprovada</text>
   <rect x="200" y="380" width="400" height="70" rx="4" fill="#F8F9FA" stroke="#1F3A5F" stroke-width="2"/>
   <text x="400" y="410" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">4. Execução da Mudança</text>
   <text x="400" y="435" text-anchor="middle" font-size="13" fill="#333333">Responsável: Equipe | Prazo: ≤ 24h após aprovação</text>
   <path d="M 200 415 L 120 415 L 120 480" fill="none" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <rect x="20" y="480" width="200" height="60" rx="4" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
   <text x="120" y="505" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">Mudança Simples</text>
   <text x="120" y="525" text-anchor="middle" font-size="12" fill="#333333">Atualização de backlog</text>
   <text x="120" y="540" text-anchor="middle" font-size="12" fill="#333333">+ commit na Issue</text>
   <path d="M 600 415 L 680 415 L 680 480" fill="none" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <rect x="580" y="480" width="200" height="60" rx="4" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
   <text x="680" y="505" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">Mudança de Marco / Escopo MVP</text>
   <text x="680" y="525" text-anchor="middle" font-size="12" fill="#333333">Registro formal via ADR +</text>
   <text x="680" y="540" text-anchor="middle" font-size="12" fill="#333333">Comunicação no marco subsequente</text>
 </svg>
~~~

### 3.3 Rodada 3 — CFD e Sequenciamento (2 SVGs) — 21/09/2026

#### FIG-CFD-01: `fig-3-cfd-saudavel-vs-gargalo.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 700" font-family="Arial, Helvetica, sans-serif">
   <rect x="0" y="0" width="1400" height="700" fill="#FFFFFF"/>
   <text x="700" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Cumulative Flow Diagram (CFD) — Padrão Saudável vs. Gargalo</text>
   <!-- Painel A: CFD Saudável -->
   <g transform="translate(50, 80)">
     <text x="300" y="0" text-anchor="middle" font-size="18" font-weight="bold" fill="#1F3A5F">(a) CFD Saudável — Fluxo Estável</text>
     <line x1="50" y1="40" x2="50" y2="480" stroke="#333333" stroke-width="2"/>
     <line x1="50" y1="480" x2="600" y2="480" stroke="#333333" stroke-width="2"/>
     <text x="20" y="260" text-anchor="middle" font-size="12" fill="#555555" transform="rotate(-90, 20, 260)">Cards Acumulados</text>
     <text x="325" y="510" text-anchor="middle" font-size="12" fill="#555555">Tempo (semanas)</text>
     <path d="M 50 480 L 600 480 L 600 420 L 50 420 Z" fill="#2E7D32" opacity="0.8"/>
     <text x="580" y="455" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Done</text>
     <path d="M 50 420 L 600 420 L 600 370 L 50 370 Z" fill="#4A90E2" opacity="0.8"/>
     <text x="580" y="400" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Code Review</text>
     <path d="M 50 370 L 600 370 L 600 310 L 50 310 Z" fill="#1F3A5F" opacity="0.8"/>
     <text x="580" y="345" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">In Progress</text>
     <path d="M 50 310 L 600 310 L 600 260 L 50 260 Z" fill="#E67E22" opacity="0.8"/>
     <text x="580" y="290" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Ready</text>
     <path d="M 50 260 L 600 260 L 600 200 L 50 200 Z" fill="#7F8C8D" opacity="0.8"/>
     <text x="580" y="235" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Backlog</text>
     <text x="325" y="540" text-anchor="middle" font-size="12" fill="#2E7D32" font-weight="bold">Bandas paralelas e de largura constante</text>
     <text x="325" y="555" text-anchor="middle" font-size="11" fill="#555555">Fluxo estável — WIP sob controle</text>
   </g>
   <!-- Painel B: CFD com Gargalo -->
   <g transform="translate(750, 80)">
     <text x="300" y="0" text-anchor="middle" font-size="18" font-weight="bold" fill="#C0392B">(b) CFD com Gargalo — Code Review</text>
     <line x1="50" y1="40" x2="50" y2="480" stroke="#333333" stroke-width="2"/>
     <line x1="50" y1="480" x2="600" y2="480" stroke="#333333" stroke-width="2"/>
     <text x="20" y="260" text-anchor="middle" font-size="12" fill="#555555" transform="rotate(-90, 20, 260)">Cards Acumulados</text>
     <text x="325" y="510" text-anchor="middle" font-size="12" fill="#555555">Tempo (semanas)</text>
     <path d="M 50 480 L 600 480 L 600 450 L 50 450 Z" fill="#2E7D32" opacity="0.8"/>
     <text x="580" y="470" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Done</text>
     <path d="M 50 450 L 200 450 L 350 420 L 500 380 L 600 350 L 600 250 L 500 280 L 350 320 L 200 350 L 50 350 Z" fill="#4A90E2" opacity="0.8"/>
     <text x="580" y="310" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Code Review</text>
     <path d="M 400 340 L 450 320" stroke="#C0392B" stroke-width="2" marker-end="url(#arrow-red)"/>
     <text x="460" y="315" font-size="10" fill="#C0392B" font-weight="bold">Gargalo</text>
     <path d="M 50 350 L 200 350 L 350 320 L 500 280 L 600 250 L 600 200 L 500 230 L 350 270 L 200 300 L 50 300 Z" fill="#1F3A5F" opacity="0.8"/>
     <text x="580" y="230" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">In Progress</text>
     <path d="M 50 300 L 200 300 L 350 270 L 500 230 L 600 200 L 600 160 L 500 190 L 350 230 L 200 260 L 50 260 Z" fill="#E67E22" opacity="0.8"/>
     <text x="580" y="190" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Ready</text>
     <path d="M 50 260 L 200 260 L 350 230 L 500 190 L 600 160 L 600 120 L 500 150 L 350 190 L 200 220 L 50 220 Z" fill="#7F8C8D" opacity="0.8"/>
     <text x="580" y="150" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Backlog</text>
     <text x="325" y="540" text-anchor="middle" font-size="12" fill="#C0392B" font-weight="bold">Banda Code Review alargando progressivamente</text>
     <text x="325" y="555" text-anchor="middle" font-size="11" fill="#555555">Gargalo detectado — ação corretiva necessária</text>
   </g>
   <rect x="200" y="620" width="1000" height="60" rx="6" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
   <text x="700" y="645" text-anchor="middle" font-size="14" font-weight="bold" fill="#E65100">Regra de Ação Corretiva (Integração §1.6.1)</text>
   <text x="700" y="665" text-anchor="middle" font-size="12" fill="#333333">Se uma banda ultrapassar 2× a largura média das demais por 2 semanas consecutivas → Retrospectiva extraordinária (ADR-002)</text>
   <defs>
     <marker id="arrow-red" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
       <path d="M0,0 L9,3 L0,6 Z" fill="#C0392B"/>
     </marker>
   </defs>
 </svg>
~~~

#### FIG-SEQ-01: `fig-1-sequenciamento-macro-caminho-critico.svg` (v1 — SUPERSEDED pela v2 na Correção 3.5)

### 3.4 Correção 3.5 — Fix de Overlap (1 SVG refeito) — 21/09/2026

**Problema na v1:** Múltiplas setas convergiam para ponto cartesiano único (`500, 200`), empilhando pontas de flechas. `viewBox` subdimensionado comprimia elementos.

**Correções:** Canvas expandido (1200×700), ancoragem distribuída, tipografia com `<tspan>` e `dy` controlado, feedback orgânico com seta curva tracejada.

#### FIG-SEQ-01 v2 (CANÔNICA): `fig-1-sequenciamento-macro-caminho-critico.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 700" font-family="Arial, Helvetica, sans-serif">
   <defs>
     <marker id="ar-flow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
       <path d="M0,0 L9,3 L0,6 Z" fill="#1F3A5F"/>
     </marker>
     <marker id="ar-green" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
       <path d="M0,0 L9,3 L0,6 Z" fill="#2E7D32"/>
     </marker>
     <marker id="ar-feedback" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
       <path d="M0,0 L9,3 L0,6 Z" fill="#E67E22"/>
     </marker>
   </defs>
   <rect x="0" y="0" width="1200" height="700" fill="#FFFFFF"/>
   <text x="600" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Sequenciamento Macro e Caminho Crítico Empírico</text>
   <text x="600" y="75" text-anchor="middle" font-size="16" font-weight="bold" fill="#1F3A5F">Camada Macro — Macro-Fases e Gates de Controle</text>
   <rect x="60" y="95" width="200" height="70" rx="6" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
   <text x="160" y="120" text-anchor="middle" font-size="14" font-weight="bold" fill="#FFFFFF"><tspan x="160" dy="0">MF1: Fundação</tspan><tspan x="160" dy="20" font-size="11" font-weight="normal" fill="#E0E7EF">01/09 – 30/09/2026</tspan><tspan x="160" dy="15" font-size="11" font-weight="normal" fill="#E0E7EF">5 planos (Áreas 1–5)</tspan></text>
   <line x1="260" y1="130" x2="280" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <polygon points="300,110 320,130 300,150 280,130" fill="#E67E22" stroke="#E67E22" stroke-width="2"/>
   <text x="300" y="170" text-anchor="middle" font-size="11" font-weight="bold" fill="#E67E22">M2</text>
   <text x="300" y="185" text-anchor="middle" font-size="10" fill="#555555">30/09</text>
   <line x1="320" y1="130" x2="340" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <rect x="340" y="105" width="140" height="50" rx="6" fill="#FFF3E0" stroke="#E67E22" stroke-width="2" stroke-dasharray="4,2"/>
   <text x="410" y="125" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100"><tspan x="410" dy="0">Calibração</tspan><tspan x="410" dy="18" font-size="11" font-weight="normal" fill="#555555">03/10 (auxiliar)</tspan></text>
   <line x1="480" y1="130" x2="500" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <rect x="500" y="95" width="200" height="70" rx="6" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
   <text x="600" y="120" text-anchor="middle" font-size="14" font-weight="bold" fill="#FFFFFF"><tspan x="600" dy="0">MF2: Construção</tspan><tspan x="600" dy="20" font-size="11" font-weight="normal" fill="#E8F5E9">01/10 – 15/11/2026</tspan><tspan x="600" dy="15" font-size="11" font-weight="normal" fill="#E8F5E9">MVP funcional + coverage ≥80%</tspan></text>
   <line x1="700" y1="130" x2="720" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <polygon points="740,110 760,130 740,150 720,130" fill="#E67E22" stroke="#E67E22" stroke-width="2"/>
   <text x="740" y="170" text-anchor="middle" font-size="11" font-weight="bold" fill="#E67E22">M3</text>
   <text x="740" y="185" text-anchor="middle" font-size="10" fill="#555555">15/11</text>
   <line x1="760" y1="130" x2="780" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <rect x="780" y="95" width="200" height="70" rx="6" fill="#6A1B9A" stroke="#6A1B9A" stroke-width="2"/>
   <text x="880" y="120" text-anchor="middle" font-size="14" font-weight="bold" fill="#FFFFFF"><tspan x="880" dy="0">MF3: Consolidação</tspan><tspan x="880" dy="20" font-size="11" font-weight="normal" fill="#F3E5F5">16/11 – 15/12/2026</tspan><tspan x="880" dy="15" font-size="11" font-weight="normal" fill="#F3E5F5">Documentação + Aceite M4</tspan></text>
   <line x1="980" y1="130" x2="1000" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <polygon points="1020,110 1040,130 1020,150 1000,130" fill="#E67E22" stroke="#E67E22" stroke-width="2"/>
   <text x="1020" y="170" text-anchor="middle" font-size="11" font-weight="bold" fill="#E67E22">M4</text>
   <text x="1020" y="185" text-anchor="middle" font-size="10" fill="#555555">15/12</text>
   <text x="600" y="240" text-anchor="middle" font-size="16" font-weight="bold" fill="#2E7D32">Camada Operacional — Detectores do Caminho Crítico Empírico</text>
   <rect x="80" y="270" width="220" height="90" rx="6" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
   <text x="190" y="295" text-anchor="middle" font-size="13" font-weight="bold" fill="#C0392B"><tspan x="190" dy="0">Cards P0</tspan><tspan x="190" dy="20" font-size="11" font-weight="normal" fill="#333333">Prioridade temporal</tspan><tspan x="190" dy="15" font-size="11" font-weight="normal" fill="#333333">crítica do marco</tspan><tspan x="190" dy="15" font-size="10" font-weight="normal" fill="#555555">(OKB §9.4)</tspan></text>
   <rect x="330" y="270" width="220" height="90" rx="6" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
   <text x="440" y="295" text-anchor="middle" font-size="13" font-weight="bold" fill="#C0392B"><tspan x="440" dy="0">Label blocked</tspan><tspan x="440" dy="20" font-size="11" font-weight="normal" fill="#333333">Dependência registrada</tspan><tspan x="440" dy="15" font-size="11" font-weight="normal" fill="#333333">no corpo da Issue</tspan><tspan x="440" dy="15" font-size="10" font-weight="normal" fill="#555555">(OKB §9.1)</tspan></text>
   <rect x="580" y="270" width="220" height="90" rx="6" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
   <text x="690" y="295" text-anchor="middle" font-size="13" font-weight="bold" fill="#E65100"><tspan x="690" dy="0">Bandas do CFD</tspan><tspan x="690" dy="20" font-size="11" font-weight="normal" fill="#333333">Alargamento > 2×</tspan><tspan x="690" dy="15" font-size="11" font-weight="normal" fill="#333333">largura média</tspan><tspan x="690" dy="15" font-size="10" font-weight="normal" fill="#555555">(Integração §1.6.1)</tspan></text>
   <rect x="830" y="270" width="220" height="90" rx="6" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
   <text x="940" y="295" text-anchor="middle" font-size="13" font-weight="bold" fill="#E65100"><tspan x="940" dy="0">Desvio Cycle Time</tspan><tspan x="940" dy="20" font-size="11" font-weight="normal" fill="#333333">Meta ≤ 3 dias</tspan><tspan x="940" dy="15" font-size="11" font-weight="normal" fill="#333333">violada persistentemente</tspan><tspan x="940" dy="15" font-size="10" font-weight="normal" fill="#555555">(ADR-003)</tspan></text>
   <line x1="190" y1="360" x2="380" y2="410" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
   <line x1="440" y1="360" x2="520" y2="410" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
   <line x1="690" y1="360" x2="620" y2="410" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
   <line x1="940" y1="360" x2="720" y2="410" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
   <rect x="330" y="410" width="540" height="80" rx="6" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
   <text x="600" y="440" text-anchor="middle" font-size="15" font-weight="bold" fill="#FFFFFF"><tspan x="600" dy="0">Refinement Semanal + Retrospectiva Quinzenal</tspan><tspan x="600" dy="22" font-size="12" font-weight="normal" fill="#E8F5E9">Decisão de replanejamento e ajuste de prioridades</tspan><tspan x="600" dy="16" font-size="11" font-weight="normal" fill="#E8F5E9">(sem violar os gates de controle das Macro-Fases)</tspan></text>
   <path d="M 870 450 Q 1100 450 1100 130 L 1040 130" fill="none" stroke="#E67E22" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#ar-feedback)"/>
   <text x="1110" y="290" font-size="11" font-weight="bold" fill="#E67E22" text-anchor="start">Feedback de</text>
   <text x="1110" y="305" font-size="11" font-weight="bold" fill="#E67E22" text-anchor="start">Replanejamento</text>
   <rect x="100" y="540" width="1000" height="60" rx="6" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="1.5"/>
   <text x="600" y="565" text-anchor="middle" font-size="12" font-weight="bold" fill="#111111">Nota Técnica:</text>
   <text x="600" y="585" text-anchor="middle" font-size="12" fill="#333333">Caminho crítico identificado empiricamente — sem rede CPM preditiva. Substitui o Gantt/EVM por</text>
   <text x="600" y="600" text-anchor="middle" font-size="12" fill="#333333">métricas de fluxo Kanban, conforme ADR-003 e OKB §8.1.</text>
 </svg>
~~~

### 3.5 Rodada 4 — Fluxo Kanban (1 SVG) — 21/09/2026

#### FIG-KAN-01: `fig-2-fluxo-kanban-oficial.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 500" font-family="Arial, Helvetica, sans-serif">
   <defs>
     <marker id="ar-flow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
       <path d="M0,0 L9,3 L0,6 Z" fill="#1F3A5F"/>
     </marker>
   </defs>
   <rect x="0" y="0" width="1400" height="500" fill="#FFFFFF"/>
   <text x="700" y="35" text-anchor="middle" font-size="20" font-weight="bold" fill="#111111">Fluxo Kanban Oficial — Gates de Qualidade e WIP Limits</text>
   <rect x="40" y="80" width="200" height="320" rx="8" fill="#F4F6F8" stroke="#555555" stroke-width="2"/>
   <text x="140" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#111111">Backlog</text>
   <text x="140" y="135" text-anchor="middle" font-size="11" fill="#555555">Product Backlog</text>
   <text x="140" y="150" text-anchor="middle" font-size="11" fill="#555555">não refinado</text>
   <rect x="280" y="80" width="200" height="320" rx="8" fill="#E0E7EF" stroke="#1F3A5F" stroke-width="2"/>
   <text x="380" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#111111">Ready (DoR)</text>
   <text x="380" y="135" text-anchor="middle" font-size="11" fill="#333333">Card pronto para</text>
   <text x="380" y="150" text-anchor="middle" font-size="11" fill="#333333">execução</text>
   <rect x="520" y="80" width="200" height="320" rx="8" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
   <text x="620" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">In Progress</text>
   <text x="620" y="135" text-anchor="middle" font-size="11" fill="#E0E7EF">Card em execução</text>
   <text x="620" y="150" text-anchor="middle" font-size="11" fill="#E0E7EF">pelo responsável</text>
   <rect x="540" y="60" width="160" height="30" rx="4" fill="#C0392B" stroke="#C0392B" stroke-width="2"/>
   <text x="620" y="80" text-anchor="middle" font-size="12" font-weight="bold" fill="#FFFFFF">WIP LIMIT: 3 cards/pessoa</text>
   <rect x="760" y="80" width="200" height="320" rx="8" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
   <text x="860" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#111111">Code Review</text>
   <text x="860" y="135" text-anchor="middle" font-size="11" fill="#333333">Revisão em pares</text>
   <text x="860" y="150" text-anchor="middle" font-size="11" fill="#333333">obrigatória</text>
   <rect x="1000" y="80" width="200" height="320" rx="8" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
   <text x="1100" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">Done (DoD)</text>
   <text x="1100" y="135" text-anchor="middle" font-size="11" fill="#E8F5E9">Card concluído</text>
   <text x="1100" y="150" text-anchor="middle" font-size="11" fill="#E8F5E9">e validado</text>
   <polygon points="250,220 270,240 250,260 230,240" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
   <text x="250" y="285" text-anchor="middle" font-size="10" font-weight="bold" fill="#1F3A5F">Gate DoR</text>
   <text x="250" y="300" text-anchor="middle" font-size="9" fill="#555555">Critérios de</text>
   <text x="250" y="312" text-anchor="middle" font-size="9" fill="#555555">prontidão</text>
   <polygon points="490,220 510,240 490,260 470,240" fill="#C0392B" stroke="#C0392B" stroke-width="2"/>
   <text x="490" y="285" text-anchor="middle" font-size="10" font-weight="bold" fill="#C0392B">Gate WIP</text>
   <text x="490" y="300" text-anchor="middle" font-size="9" fill="#555555">Capacidade</text>
   <text x="490" y="312" text-anchor="middle" font-size="9" fill="#555555">disponível</text>
   <polygon points="730,220 750,240 730,260 710,240" fill="#E65100" stroke="#E65100" stroke-width="2"/>
   <text x="730" y="285" text-anchor="middle" font-size="10" font-weight="bold" fill="#E65100">Gate Tasklist</text>
   <text x="730" y="300" text-anchor="middle" font-size="9" fill="#555555">100% itens</text>
   <text x="730" y="312" text-anchor="middle" font-size="9" fill="#555555">concluídos</text>
   <polygon points="970,220 990,240 970,260 950,240" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
   <text x="970" y="285" text-anchor="middle" font-size="10" font-weight="bold" fill="#2E7D32">Gate DoD</text>
   <text x="970" y="300" text-anchor="middle" font-size="9" fill="#555555">Critérios de</text>
   <text x="970" y="312" text-anchor="middle" font-size="9" fill="#555555">conclusão</text>
   <line x1="240" y1="240" x2="270" y2="240" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <line x1="480" y1="240" x2="510" y2="240" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <line x1="720" y1="240" x2="750" y2="240" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <line x1="960" y1="240" x2="990" y2="240" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <rect x="100" y="420" width="1200" height="60" rx="6" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="1.5"/>
   <text x="700" y="445" text-anchor="middle" font-size="12" font-weight="bold" fill="#111111">Regra de Ação Corretiva (ADR-002 + ADR-004):</text>
   <text x="700" y="465" text-anchor="middle" font-size="11" fill="#333333">Se WIP limit for violado ou tasklist não estiver 100% concluída, o card não migra para a coluna seguinte.</text>
   <text x="700" y="478" text-anchor="middle" font-size="11" fill="#333333">Gargalos persistentes acionam Retrospectiva extraordinária (Integração §1.6.1).</text>
 </svg>
~~~

### 3.6 Rodada 5 — Custos (2 SVGs) — 21/09/2026

#### FIG-CUST-01: `fig-5-fluxo-prevencao-custos.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 900" font-family="Arial, Helvetica, sans-serif">
   <defs>
     <marker id="ar-flow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3 L0,6 Z" fill="#1F3A5F"/></marker>
     <marker id="ar-reject" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3 L0,6 Z" fill="#C0392B"/></marker>
     <marker id="ar-approve" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3 L0,6 Z" fill="#2E7D32"/></marker>
   </defs>
   <rect x="0" y="0" width="800" height="900" fill="#FFFFFF"/>
   <text x="400" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Fluxo de Prevenção de Custos — Conformidade FOSS</text>
   <rect x="250" y="80" width="300" height="60" rx="6" fill="#F8F9FA" stroke="#1F3A5F" stroke-width="2"/>
   <text x="400" y="105" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">Nova dependência identificada</text>
   <text x="400" y="125" text-anchor="middle" font-size="12" fill="#555555">(biblioteca, API, ferramenta, serviço)</text>
   <line x1="400" y1="140" x2="400" y2="180" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <polygon points="400,180 520,220 400,260 280,220" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
   <text x="400" y="215" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">Gate 1:</text>
   <text x="400" y="235" text-anchor="middle" font-size="12" fill="#333333">Licença OSI-approved?</text>
   <line x1="520" y1="220" x2="620" y2="220" stroke="#C0392B" stroke-width="2" marker-end="url(#ar-reject)"/>
   <text x="570" y="210" text-anchor="middle" font-size="11" font-weight="bold" fill="#C0392B">NÃO</text>
   <rect x="620" y="190" width="150" height="60" rx="4" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
   <text x="695" y="215" text-anchor="middle" font-size="12" font-weight="bold" fill="#C0392B">Rejeição imediata</text>
   <text x="695" y="235" text-anchor="middle" font-size="10" fill="#333333">Buscar alternativa FOSS</text>
   <line x1="400" y1="260" x2="400" y2="300" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-approve)"/>
   <text x="415" y="285" font-size="11" font-weight="bold" fill="#2E7D32">SIM</text>
   <polygon points="400,300 520,340 400,380 280,340" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
   <text x="400" y="335" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">Gate 2:</text>
   <text x="400" y="355" text-anchor="middle" font-size="12" fill="#333333">Plano gratuito suficiente</text>
   <text x="400" y="370" text-anchor="middle" font-size="12" fill="#333333">para MVP acadêmico?</text>
   <line x1="520" y1="340" x2="620" y2="340" stroke="#E65100" stroke-width="2" marker-end="url(#ar-flow)"/>
   <text x="570" y="330" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">NÃO</text>
   <rect x="620" y="310" width="150" height="60" rx="4" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
   <text x="695" y="335" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">Buscar alternativa FOSS</text>
   <text x="695" y="355" text-anchor="middle" font-size="10" fill="#333333">com plano gratuito</text>
   <path d="M 695 370 L 695 390 L 400 390 L 400 380" fill="none" stroke="#E65100" stroke-width="1.5" stroke-dasharray="4,2"/>
   <line x1="400" y1="380" x2="400" y2="420" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-approve)"/>
   <text x="415" y="405" font-size="11" font-weight="bold" fill="#2E7D32">SIM</text>
   <polygon points="400,420 520,460 400,500 280,460" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
   <text x="400" y="455" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">Gate 3:</text>
   <text x="400" y="475" text-anchor="middle" font-size="12" fill="#333333">Registrado em ADR-001</text>
   <text x="400" y="490" text-anchor="middle" font-size="12" fill="#333333">ou nova ADR?</text>
   <line x1="520" y1="460" x2="620" y2="460" stroke="#E65100" stroke-width="2" marker-end="url(#ar-flow)"/>
   <text x="570" y="450" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">NÃO</text>
   <rect x="620" y="430" width="150" height="60" rx="4" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
   <text x="695" y="455" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">Registrar antes de usar</text>
   <text x="695" y="475" text-anchor="middle" font-size="10" fill="#333333">ADR específica ou</text>
   <text x="695" y="488" text-anchor="middle" font-size="10" fill="#333333">atualização ADR-001</text>
   <path d="M 695 490 L 695 510 L 400 510 L 400 500" fill="none" stroke="#E65100" stroke-width="1.5" stroke-dasharray="4,2"/>
   <line x1="400" y1="500" x2="400" y2="540" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-approve)"/>
   <text x="415" y="525" font-size="11" font-weight="bold" fill="#2E7D32">SIM</text>
   <rect x="250" y="540" width="300" height="60" rx="6" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
   <text x="400" y="565" text-anchor="middle" font-size="14" font-weight="bold" fill="#FFFFFF">Incorporação autorizada</text>
   <text x="400" y="585" text-anchor="middle" font-size="12" fill="#E8F5E9">Dependência FOSS conformante</text>
   <rect x="150" y="650" width="500" height="80" rx="6" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
   <text x="400" y="675" text-anchor="middle" font-size="13" font-weight="bold" fill="#C0392B">Desvio de qualquer gate aciona:</text>
   <text x="400" y="695" text-anchor="middle" font-size="12" fill="#333333">Issue com label change-request (Integração §1.7)</text>
   <text x="400" y="712" text-anchor="middle" font-size="11" fill="#555555">Análise de impacto pelo GP (CCB) em ≤ 48h</text>
   <text x="400" y="725" text-anchor="middle" font-size="11" fill="#555555">Registro em ADR se alteração de marco ou escopo MVP</text>
   <rect x="150" y="780" width="500" height="50" rx="4" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="1.5"/>
   <text x="400" y="805" text-anchor="middle" font-size="12" font-weight="bold" fill="#111111">Linha de Base de Custos: R$ 0,00 (imutável sem CCB)</text>
   <text x="400" y="820" text-anchor="middle" font-size="11" fill="#555555">TAP §11 + Premissa P2 (FOSS absoluto)</text>
 </svg>
~~~

#### FIG-CUST-02: `fig-6-matriz-rastreabilidade-dependencias.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" font-family="Arial, Helvetica, sans-serif">
   <rect x="0" y="0" width="1200" height="500" fill="#FFFFFF"/>
   <text x="600" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Matriz de Rastreabilidade de Dependências — Stack FOSS Canônica</text>
   <rect x="50" y="80" width="1100" height="50" rx="4" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
   <text x="150" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">Dependência</text>
   <text x="320" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">Versão</text>
   <text x="470" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">Licença</text>
   <text x="620" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">Conformidade</text>
   <text x="770" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">EAP N1.4/N4.4</text>
   <text x="920" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">ADR-001</text>
   <text x="1070" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">Categoria</text>
   <rect x="50" y="130" width="1100" height="50" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1"/>
   <text x="150" y="160" text-anchor="middle" font-size="12" fill="#111111">FastAPI</text>
   <text x="320" y="160" text-anchor="middle" font-size="12" fill="#333333">≥0.100</text>
   <text x="470" y="160" text-anchor="middle" font-size="12" fill="#333333">MIT</text>
   <text x="620" y="160" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
   <text x="770" y="160" text-anchor="middle" font-size="12" fill="#333333">N4.4</text>
   <text x="920" y="160" text-anchor="middle" font-size="12" fill="#333333">✅</text>
   <text x="1070" y="160" text-anchor="middle" font-size="11" fill="#555555">Backend</text>
   <rect x="50" y="180" width="1100" height="50" rx="4" fill="#FFFFFF" stroke="#555555" stroke-width="1"/>
   <text x="150" y="210" text-anchor="middle" font-size="12" fill="#111111">SQLite</text>
   <text x="320" y="210" text-anchor="middle" font-size="12" fill="#333333">3.x</text>
   <text x="470" y="210" text-anchor="middle" font-size="12" fill="#333333">Public Domain</text>
   <text x="620" y="210" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
   <text x="770" y="210" text-anchor="middle" font-size="12" fill="#333333">N4.4</text>
   <text x="920" y="210" text-anchor="middle" font-size="12" fill="#333333">✅</text>
   <text x="1070" y="210" text-anchor="middle" font-size="11" fill="#555555">Banco de Dados</text>
   <rect x="50" y="230" width="1100" height="50" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1"/>
   <text x="150" y="260" text-anchor="middle" font-size="12" fill="#111111">WeasyPrint</text>
   <text x="320" y="260" text-anchor="middle" font-size="12" fill="#333333">≥59.0</text>
   <text x="470" y="260" text-anchor="middle" font-size="12" fill="#333333">BSD-3-Clause</text>
   <text x="620" y="260" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
   <text x="770" y="260" text-anchor="middle" font-size="12" fill="#333333">N4.4</text>
   <text x="920" y="260" text-anchor="middle" font-size="12" fill="#333333">✅</text>
   <text x="1070" y="260" text-anchor="middle" font-size="11" fill="#555555">Geração PDF</text>
   <rect x="50" y="280" width="1100" height="50" rx="4" fill="#FFFFFF" stroke="#555555" stroke-width="1"/>
   <text x="150" y="310" text-anchor="middle" font-size="12" fill="#111111">pytest</text>
   <text x="320" y="310" text-anchor="middle" font-size="12" fill="#333333">≥7.0</text>
   <text x="470" y="310" text-anchor="middle" font-size="12" fill="#333333">MIT</text>
   <text x="620" y="310" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
   <text x="770" y="310" text-anchor="middle" font-size="12" fill="#333333">N4.4</text>
   <text x="920" y="310" text-anchor="middle" font-size="12" fill="#333333">✅</text>
   <text x="1070" y="310" text-anchor="middle" font-size="11" fill="#555555">Testes</text>
   <rect x="50" y="330" width="1100" height="50" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1"/>
   <text x="150" y="360" text-anchor="middle" font-size="12" fill="#111111">GitHub Actions</text>
   <text x="320" y="360" text-anchor="middle" font-size="12" fill="#333333">Free Tier</text>
   <text x="470" y="360" text-anchor="middle" font-size="12" fill="#333333">Proprietário gratuito</text>
   <text x="620" y="360" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
   <text x="770" y="360" text-anchor="middle" font-size="12" fill="#333333">N1.4</text>
   <text x="920" y="360" text-anchor="middle" font-size="12" fill="#333333">✅</text>
   <text x="1070" y="360" text-anchor="middle" font-size="11" fill="#555555">CI/CD</text>
   <rect x="50" y="380" width="1100" height="50" rx="4" fill="#FFFFFF" stroke="#555555" stroke-width="1"/>
   <text x="150" y="410" text-anchor="middle" font-size="12" fill="#111111">llama.cpp</text>
   <text x="320" y="410" text-anchor="middle" font-size="12" fill="#333333">0.4.0-dev</text>
   <text x="470" y="410" text-anchor="middle" font-size="12" fill="#333333">MIT</text>
   <text x="620" y="410" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
   <text x="770" y="410" text-anchor="middle" font-size="12" fill="#333333">N4.4</text>
   <text x="920" y="410" text-anchor="middle" font-size="12" fill="#333333">✅</text>
   <text x="1070" y="410" text-anchor="middle" font-size="11" fill="#555555">SDD Local (IA)</text>
   <rect x="50" y="450" width="1100" height="40" rx="4" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
   <text x="600" y="475" text-anchor="middle" font-size="13" font-weight="bold" fill="#2E7D32">100% das dependências auditadas e conformantes — Linha de base R$ 0,00 preservada</text>
 </svg>
~~~

### 3.7 Rodada 6 — Escopo (2 SVGs) — 21/09/2026

#### FIG-ESC-01: `fig-eap-visao-executiva.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" font-family="Arial, Helvetica, sans-serif">
   <defs><marker id="ar-flow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3 L0,6 Z" fill="#1F3A5F"/></marker></defs>
   <rect x="0" y="0" width="1200" height="850" fill="#FFFFFF"/>
   <text x="600" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Estrutura Analítica do Projeto (EAP) — Visão Executiva</text>
   <rect x="450" y="70" width="300" height="60" rx="6" fill="#111111" stroke="#111111" stroke-width="2"/>
   <text x="600" y="105" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">N0: COGME</text>
   <line x1="600" y1="130" x2="600" y2="170" stroke="#777777" stroke-width="2"/>
   <rect x="50" y="170" width="1100" height="200" rx="8" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
   <text x="600" y="195" text-anchor="middle" font-size="16" font-weight="bold" fill="#1F3A5F">MF1: Fundação (01/09 – 30/09/2026)</text>
   <rect x="70" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
   <text x="150" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N1</text>
   <text x="150" y="255" text-anchor="middle" font-size="11" fill="#333333">Iniciação e</text>
   <text x="150" y="270" text-anchor="middle" font-size="11" fill="#333333">Planejamento</text>
   <text x="150" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(5 pacotes)</text>
   <rect x="245" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
   <text x="325" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N2</text>
   <text x="325" y="255" text-anchor="middle" font-size="11" fill="#333333">Levantamento de</text>
   <text x="325" y="270" text-anchor="middle" font-size="11" fill="#333333">Requisitos</text>
   <text x="325" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(3 pacotes)</text>
   <rect x="420" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
   <text x="500" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N3</text>
   <text x="500" y="255" text-anchor="middle" font-size="11" fill="#333333">Modelagem e</text>
   <text x="500" y="270" text-anchor="middle" font-size="11" fill="#333333">Prototipação</text>
   <text x="500" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(3 pacotes)</text>
   <rect x="595" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
   <text x="675" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N4</text>
   <text x="675" y="255" text-anchor="middle" font-size="11" fill="#333333">Configuração de</text>
   <text x="675" y="270" text-anchor="middle" font-size="11" fill="#333333">Ambiente</text>
   <text x="675" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(4 pacotes)</text>
   <rect x="770" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
   <text x="850" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N8</text>
   <text x="850" y="255" text-anchor="middle" font-size="11" fill="#333333">Comunicação</text>
   <text x="850" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(2 pacotes)</text>
   <rect x="945" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
   <text x="1025" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N9</text>
   <text x="1025" y="255" text-anchor="middle" font-size="11" fill="#333333">Base de</text>
   <text x="1025" y="270" text-anchor="middle" font-size="11" fill="#333333">Conhecimento</text>
   <text x="1025" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(3 pacotes)</text>
   <rect x="50" y="390" width="1100" height="200" rx="8" fill="#F4F6F8" stroke="#2E7D32" stroke-width="2"/>
   <text x="600" y="415" text-anchor="middle" font-size="16" font-weight="bold" fill="#2E7D32">MF2: Construção (01/10 – 15/11/2026)</text>
   <rect x="120" y="430" width="200" height="140" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
   <text x="220" y="455" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N5</text>
   <text x="220" y="475" text-anchor="middle" font-size="11" fill="#333333">Desenvolvimento</text>
   <text x="220" y="490" text-anchor="middle" font-size="11" fill="#333333">do Sistema</text>
   <text x="220" y="515" text-anchor="middle" font-size="12" font-weight="bold" fill="#2E7D32">(5 pacotes)</text>
   <rect x="340" y="430" width="200" height="140" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
   <text x="440" y="455" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N6</text>
   <text x="440" y="475" text-anchor="middle" font-size="11" fill="#333333">Garantia da</text>
   <text x="440" y="490" text-anchor="middle" font-size="11" fill="#333333">Qualidade</text>
   <text x="440" y="515" text-anchor="middle" font-size="12" font-weight="bold" fill="#2E7D32">(3 pacotes)</text>
   <rect x="560" y="430" width="200" height="140" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
   <text x="660" y="455" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N7</text>
   <text x="660" y="475" text-anchor="middle" font-size="11" fill="#333333">DevOps e CI/CD</text>
   <text x="660" y="515" text-anchor="middle" font-size="12" font-weight="bold" fill="#2E7D32">(1 pacote)</text>
   <rect x="780" y="430" width="200" height="140" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
   <text x="880" y="455" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N10</text>
   <text x="880" y="475" text-anchor="middle" font-size="11" fill="#333333">Gestão de</text>
   <text x="880" y="490" text-anchor="middle" font-size="11" fill="#333333">Mudanças</text>
   <text x="880" y="515" text-anchor="middle" font-size="12" font-weight="bold" fill="#2E7D32">(3 pacotes)</text>
   <rect x="50" y="610" width="1100" height="200" rx="8" fill="#F4F6F8" stroke="#6A1B9A" stroke-width="2"/>
   <text x="600" y="635" text-anchor="middle" font-size="16" font-weight="bold" fill="#6A1B9A">MF3: Consolidação (16/11 – 15/12/2026)</text>
   <rect x="250" y="650" width="250" height="140" rx="4" fill="#FFFFFF" stroke="#6A1B9A" stroke-width="2"/>
   <text x="375" y="675" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N11</text>
   <text x="375" y="695" text-anchor="middle" font-size="11" fill="#333333">Documentação</text>
   <text x="375" y="710" text-anchor="middle" font-size="11" fill="#333333">do Projeto</text>
   <text x="375" y="735" text-anchor="middle" font-size="12" font-weight="bold" fill="#6A1B9A">(2 pacotes)</text>
   <rect x="550" y="650" width="250" height="140" rx="4" fill="#FFFFFF" stroke="#6A1B9A" stroke-width="2"/>
   <text x="675" y="675" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N12</text>
   <text x="675" y="695" text-anchor="middle" font-size="11" fill="#333333">Encerramento</text>
   <text x="675" y="735" text-anchor="middle" font-size="12" font-weight="bold" fill="#6A1B9A">(3 pacotes)</text>
   <rect x="200" y="820" width="800" height="25" rx="4" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
   <text x="600" y="837" text-anchor="middle" font-size="11" fill="#333333">Total: 12 fases de Nível 1 + 37 pacotes de Nível 2 (baseline canônica do TAP §4)</text>
 </svg>
~~~

#### FIG-ESC-02: `fig-2-cadeia-decomposicao-escopo.svg`

~~~svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 650" font-family="Arial, Helvetica, sans-serif">
   <defs><marker id="ar-flow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L9,3 L0,6 Z" fill="#1F3A5F"/></marker></defs>
   <rect x="0" y="0" width="1400" height="650" fill="#FFFFFF"/>
   <text x="700" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Cadeia de Decomposição do Escopo e Gates de Qualidade</text>
   <rect x="50" y="100" width="280" height="400" rx="6" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
   <text x="190" y="130" text-anchor="middle" font-size="14" font-weight="bold" fill="#1F3A5F">Nível 1: Pacote EAP (N2)</text>
   <text x="190" y="150" text-anchor="middle" font-size="11" fill="#555555">Entrega substantiva</text>
   <rect x="70" y="180" width="240" height="280" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
   <text x="190" y="210" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N5.1</text>
   <text x="190" y="235" text-anchor="middle" font-size="12" fill="#333333">Backend:</text>
   <text x="190" y="255" text-anchor="middle" font-size="12" fill="#333333">Lógica de Negócio</text>
   <text x="190" y="285" text-anchor="middle" font-size="11" fill="#555555">Fase: N5 (Desenvolvimento)</text>
   <text x="190" y="305" text-anchor="middle" font-size="11" fill="#555555">Macro-Fase: MF2</text>
   <text x="190" y="335" text-anchor="middle" font-size="11" fill="#555555">Requisitos:</text>
   <text x="190" y="355" text-anchor="middle" font-size="11" fill="#555555">REQ-01, REQ-02, REQ-03</text>
   <text x="190" y="385" text-anchor="middle" font-size="11" fill="#555555">Domínio PMBOK 7ª:</text>
   <text x="190" y="405" text-anchor="middle" font-size="11" fill="#555555">Entrega</text>
   <line x1="330" y1="320" x2="420" y2="320" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <polygon points="375,300 395,320 375,340 355,320" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
   <text x="375" y="365" text-anchor="middle" font-size="10" font-weight="bold" fill="#1F3A5F">Gate DoR</text>
   <rect x="420" y="100" width="280" height="400" rx="6" fill="#F4F6F8" stroke="#2E7D32" stroke-width="2"/>
   <text x="560" y="130" text-anchor="middle" font-size="14" font-weight="bold" fill="#2E7D32">Nível 2: Card Ubíquo Kanban</text>
   <text x="560" y="150" text-anchor="middle" font-size="11" fill="#555555">Unidade atômica (≤ 8h)</text>
   <rect x="440" y="180" width="240" height="280" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
   <text x="560" y="210" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N5.1 — Backend</text>
   <text x="560" y="235" text-anchor="middle" font-size="11" fill="#333333">Padrão A (Documental)</text>
   <text x="560" y="265" text-anchor="middle" font-size="11" fill="#555555">Contexto ubíquo:</text>
   <text x="560" y="285" text-anchor="middle" font-size="10" fill="#555555">Implementar lógica de</text>
   <text x="560" y="300" text-anchor="middle" font-size="10" fill="#555555">cálculo cambial</text>
   <text x="560" y="325" text-anchor="middle" font-size="11" fill="#555555">Critérios de aceite:</text>
   <text x="560" y="345" text-anchor="middle" font-size="10" fill="#555555">✓ 5 regimes operacionais</text>
   <text x="560" y="360" text-anchor="middle" font-size="10" fill="#555555">✓ Precisão 2 casas decimais</text>
   <text x="560" y="375" text-anchor="middle" font-size="10" fill="#555555">✓ Latência ≤ 2s</text>
   <text x="560" y="405" text-anchor="middle" font-size="11" fill="#555555">Estimativa: 6h</text>
   <text x="560" y="425" text-anchor="middle" font-size="11" fill="#555555">Responsável: Leonardo</text>
   <line x1="700" y1="320" x2="790" y2="320" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <polygon points="745,300 765,320 745,340 725,320" fill="#E65100" stroke="#E65100" stroke-width="2"/>
   <text x="745" y="365" text-anchor="middle" font-size="10" font-weight="bold" fill="#E65100">Gate Tasklist</text>
   <text x="745" y="380" text-anchor="middle" font-size="9" fill="#555555">+ Review</text>
   <rect x="790" y="100" width="280" height="400" rx="6" fill="#F4F6F8" stroke="#6A1B9A" stroke-width="2"/>
   <text x="930" y="130" text-anchor="middle" font-size="14" font-weight="bold" fill="#6A1B9A">Nível 3: Tasklist Markdown</text>
   <text x="930" y="150" text-anchor="middle" font-size="11" fill="#555555">Atividades derivadas (ADR-004)</text>
   <rect x="810" y="180" width="240" height="280" rx="4" fill="#FFFFFF" stroke="#6A1B9A" stroke-width="2"/>
   <text x="930" y="210" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">Tasklist (6 itens)</text>
   <text x="930" y="240" text-anchor="start" font-size="11" fill="#333333">- [x] Modelar entidades</text>
   <text x="930" y="260" text-anchor="start" font-size="11" fill="#333333">- [x] Implementar cálculo</text>
   <text x="930" y="280" text-anchor="start" font-size="11" fill="#333333">- [x] Escrever testes unitários</text>
   <text x="930" y="300" text-anchor="start" font-size="11" fill="#333333">- [x] Documentar API</text>
   <text x="930" y="320" text-anchor="start" font-size="11" fill="#333333">- [x] Revisão em pares</text>
   <text x="930" y="340" text-anchor="start" font-size="11" fill="#333333">- [x] Validação final</text>
   <text x="930" y="380" text-anchor="middle" font-size="11" fill="#555555">Formato: - [ ] / - [x]</text>
   <text x="930" y="400" text-anchor="middle" font-size="11" fill="#555555">Natureza binária</text>
   <text x="930" y="420" text-anchor="middle" font-size="11" fill="#555555">(feito/não feito)</text>
   <rect x="1100" y="150" width="280" height="120" rx="6" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
   <text x="1240" y="175" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">Regras de Métrica</text>
   <text x="1240" y="200" text-anchor="middle" font-size="11" fill="#333333">✓ Métricas de fluxo medem</text>
   <text x="1240" y="215" text-anchor="middle" font-size="11" fill="#333333">o card pai (ADR-003)</text>
   <text x="1240" y="240" text-anchor="middle" font-size="11" fill="#C0392B" font-weight="bold">✗ Subissues rejeitadas</text>
   <text x="1240" y="255" text-anchor="middle" font-size="11" fill="#C0392B" font-weight="bold">(ADR-004)</text>
   <line x1="1070" y1="320" x2="1100" y2="320" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
   <polygon points="1085,300 1105,320 1085,340 1065,320" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
   <text x="1085" y="365" text-anchor="middle" font-size="10" font-weight="bold" fill="#2E7D32">Gate DoD</text>
   <rect x="100" y="530" width="1200" height="100" rx="6" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="1.5"/>
   <text x="700" y="555" text-anchor="middle" font-size="12" font-weight="bold" fill="#111111">Fundamentação PMBOK 6ª (dicionário) + ADR-004:</text>
   <text x="700" y="580" text-anchor="middle" font-size="11" fill="#333333">Processo 6.2 (Definir Atividades): pacotes EAP decompõem-se em atividades derivadas (ações verbais).</text>
   <text x="700" y="600" text-anchor="middle" font-size="11" fill="#333333">No COGME, atividades são materializadas como tasklist Markdown (3 a 7 itens; último item "Validação final"),</text>
   <text x="700" y="615" text-anchor="middle" font-size="11" fill="#333333">rejeitando-se formalmente subissues para preservar a unidade atômica de métrica (card pai) e evitar fragmentação do backlog.</text>
 </svg>
~~~

---

## 4. Notas Técnicas ABNT (Legendas para Inserção Documental)

> **Regra:** Estas legendas são inseridas externamente aos arquivos SVG/PNG no documento `.docx` ou `.md`, conforme NBR 14724 / NBR 12225. O ativo gráfico permanece 100% focado na legibilidade visual.

**Figura 1** – Estrutura Analítica do Projeto (EAP) — Visão Macro e Macro-Fases.
Nota: Representação da linha de base estrutural do escopo, canônica conforme o TAP (§4). O diagrama fracionado em camadas substitui a EAP tradicional de página única.
Fonte: Elaborado pelos autores (2026).

**Figura 2** – Detalhamento da Macro-Fase 1 (MF1) — Fundação.
Nota: Esta camada sustenta os entregáveis do Marco M1 (22/09/2026), incluindo os 5 planos de gerenciamento iniciais e a configuração do SSOT.
Fonte: Elaborado pelos autores (2026).

**Figura 3** – Detalhamento da Macro-Fase 2 (MF2) — Construção.
Nota: Esta camada materializa o Domínio de Entrega e sustenta o Marco M3 (15/11/2026).
Fonte: Elaborado pelos autores (2026).

**Figura 4** – Detalhamento da Macro-Fase 3 (MF3) — Consolidação.
Nota: Esta camada garante a rastreabilidade dos critérios de aceite do Marco M4 (15/12/2026).
Fonte: Elaborado pelos autores (2026).

**Figura 5** – Modelo de Governança Híbrida Trifásico.
Nota: Ilustração da hierarquia normativa. A seta de realimentação representa o ciclo contínuo de lições aprendidas.
Fonte: Elaborado pelos autores (2026).

**Figura 6** – Fluxo de Controle Integrado de Mudanças.
Nota: Materialização do Processo 4.6 do PMBOK® 6ª (dicionário) adaptado ao fluxo contínuo Kanban.
Fonte: Elaborado pelos autores (2026).

**Figura 7** – Cumulative Flow Diagram (CFD) — Padrão Saudável vs. Padrão com Gargalo.
Nota: Ferramenta visual que substitui formalmente o Gantt e o EVM (ADR-003).
Fonte: Elaborado pelos autores (2026).

**Figura 8** – Fluxo Kanban Oficial com Gates de Qualidade e WIP Limits.
Nota: Materializa ADR-002 e ADR-004. Gates: DoR, WIP, Tasklist+Review, DoD.
Fonte: Elaborado pelos autores (2026).

**Figura 9** – Sequenciamento Macro e Caminho Crítico Empírico.
Nota: Substitui visualmente a rede CPM rejeitada pela ADR-003. Quatro detectores empíricos alimentam o Refinement.
Fonte: Elaborado pelos autores (2026).

**Figura 10** – Fluxo de Prevenção de Custos — Conformidade FOSS.
Nota: Demonstra que "custo zero" é governança rigorosa sobre conformidade de licenciamento.
Fonte: Elaborado pelos autores (2026).

**Figura 11** – Matriz de Rastreabilidade de Dependências — Stack FOSS Canônica.
Nota: 100% das dependências auditadas e conformantes.
Fonte: Elaborado pelos autores (2026).

**Figura 12** – EAP — Visão Executiva Consolidada.
Nota: 12 fases × 3 macro-fases. Sem abertura dos 37 pacotes para preservar legibilidade.
Fonte: Elaborado pelos autores (2026).

**Figura 13** – Cadeia de Decomposição do Escopo e Gates de Qualidade.
Nota: Pacote EAP → Card Ubíquo → Tasklist Markdown. Subissues rejeitadas (ADR-004).
Fonte: Elaborado pelos autores (2026).

---

## 5. Estrutura de Diretórios do Repositório

> **Orientação interna:** A estrutura canônica formal está definida no Aditivo do OKB §3.2. As notas abaixo registram a proposta operacional e o mapeamento da estrutura real.

### 5.1 Estrutura Canônica Proposta

~~~
COGME/
 ├── .ai/
 │   ├── personas/ (_base.md, pm.md, coder.md, reviewer.md, tester.md, active.md)
 │   ├── specs/ (tap.md, eap.md, requisitos.md)
 │   ├── handoffs/ (001-tap-foundation.md)
 │   └── workflows/ (sdd-cycle.sh)
 ├── docs/
 │   ├── planos/ (plano-integracao.md … plano-riscos.md)
 │   ├── decisoes/ (ADR-001 … ADR-005)
 │   ├── conhecimento/ (OKB.md, glossario.md, licoes-aprendidas/)
 │   ├── metricas/ (baseline.md)
 │   ├── requisitos/ (requisitos.md)
 │   ├── diagramas/ (integracao/, qualidade/, eap/, cronograma/, custos/, mermaid-config.json)
 │   ├── dependencias/ (registro.md)
 │   ├── tap/ (TAP.md, TAP.docx)
 │   └── archive/ (drafts/, docx/, eap-legacy/, tap-sections/, images-legacy/, diagramas-deprecated/)
 ├── src/ (backend/, frontend/, shared/)
 ├── tests/ (unit/, integration/)
 ├── .github/workflows/ (ci.yml)
 ├── README.md
 ├── LICENSE
 ├── pyproject.toml
 ├── requirements.txt
 └── .gitignore
~~~

### 5.2 Estrutura Atual Real (Mapeamento 22/09/2026)

~~~
.
 ├── docs/
 │   ├── archive/
 │   │   ├── diagramas-deprecated/ (10 arquivos [legacy])
 │   │   ├── docx/ (5 planos + _archive/ com 6 templates)
 │   │   ├── eap-legacy/ (correcao/ + inicial/)
 │   │   ├── images-legacy/diagramas/ (custos/, escopo/)
 │   │   └── tap-sections/ (14 arquivos)
 │   ├── conhecimento/
 │   │   ├── drafts/ (19 arquivos)
 │   │   ├── glossario.md
 │   │   ├── licoes-aprendidas/ (MF1, MF2, MF3)
 │   │   └── OKB.md
 │   ├── decisoes/ (ADR-001 … ADR-005)
 │   ├── dependencias/registro.md
 │   ├── diagramas/
 │   │   ├── cronograma/ (fig-01-sequenciamento)
 │   │   ├── custos/ (fig-01-fluxo-prevencao)
 │   │   ├── eap/ (fig-01-executiva + 4 mf + 2 nivel-0 + 6 [legacy])
 │   │   ├── fig-4-controle-mudancas.svg
 │   │   ├── integracao/ (fig-02-matriz + fig-1-governanca + fig-3-cfd)
 │   │   ├── mermaid-config.json
 │   │   └── qualidade/ (8 arquivos [legacy])
 │   ├── metricas/baseline.md
 │   ├── planos/ (8 planos)
 │   ├── requisitos/requisitos.md
 │   ├── tap/ (TAP.docx, TAP.md)
 │   └── xml/EAP_TAP/correcao/
 ├── LICENSE
 ├── pyproject.toml
 ├── README.md
 ├── requirements.txt
 ├── src/ (backend/, frontend/, shared/)
 └── tests/ (unit/, integration/)
 48 directories, 142 files
~~~

### 5.3 Anomalias Detectadas

| Anomalia | Descrição | Status |
|----------|-----------|--------|
| A1 | `docs/diagrams/1.svg` — nunca classificado | 🔴 Provavelmente perdido |
| A2 | `fig-02-fluxo-kanban.mmd.png` — deletado sem correspondente | 🔴 Perdido |
| A3 | `fig-4-controle-mudancas.svg` na raiz de diagramas (fora de subdiretório) | ⚠️ Mover para `integracao/` |
| A4 | `estrutura-de-diretorios.md` na raiz do repositório | ⚠️ Mover para `docs/conhecimento/drafts/` |

---

## 6. Registro de Incidente — LA-001

**Data:** 22/09/2026
**Macro-Fase:** MF1 (Fundação)
**Domínio PMBOK 7ª:** Trabalho do Projeto + Entrega
**Localização canônica:** `docs/conhecimento/licoes-aprendidas/MF1-licoes.md`

### O que aconteceu
Reestruturação formal do repositório executada em paralelo com produção ativa de diagramas e textos. Alguns artefatos recentes foram perdidos ou deslocados.

### Causa raiz
1. Ausência de branch dedicada para reestruturação (operação em `main` direta)
2. Uso de `mv` do sistema em vez de `git mv` (perda de rastreabilidade de rename)
3. Execução de `git add -A` sem verificação prévia da árvore de destino
4. Produção ativa de artefatos durante a janela de reestruturação

### Impacto
- Perda de 1-2 diagramas recentes (`1.svg`, `fig-02-fluxo-kanban.mmd.png`)
- Deslocamento temporário de diagramas canônicos para archive
- Necessidade de retrabalho estimado em 2-3h

### Ação corretiva (imediata)
- Commit corretivo `fix(diagramas)` para restaurar localização canônica
- Verificação via `git reflog` para recuperação de artefatos perdidos
- Retrabalho priorizado dos itens P0-P2

### Ação preventiva (futuro)
- Reestruturações SEMPRE em branch dedicada (`chore/restructure-*`)
- Usar `git mv` em vez de `mv` para qualquer movimentação versionada
- Congelar produção durante reestruturação (janela de manutenção)
- Verificar `tree` da estrutura de destino ANTES de `git add -A`
- Commit único de reestruturação com mensagem descritiva + tag de rollback

### Comandos de recuperação
~~~bash
git log --since="2026-09-20" --oneline --all
git reflog --since="2026-09-20"
git log --diff-filter=D --summary --since="2026-09-20" --name-only
~~~

---

## 7. Matriz Consolidada de Rastreabilidade de Diagramas

| ID | Arquivo | Descrição | Plano / Seção | Rodada | Status |
|---|---|---|---|---|---|
| FIG-EAP-01 | fig-eap-nivel-0-macro.svg | Visão Macro (N0 + MFs) | Escopo §2.5 | R1 | ✅ |
| FIG-EAP-02 | fig-eap-mf1-fundacao.svg | Detalhamento MF1 | Escopo §2.5 | R1 | ✅ |
| FIG-EAP-03 | fig-eap-mf2-construcao.svg | Detalhamento MF2 | Escopo §2.5 | R1 | ✅ |
| FIG-EAP-04 | fig-eap-mf3-consolidacao.svg | Detalhamento MF3 | Escopo §2.5 | R1 | ✅ |
| FIG-GOV-01 | fig-1-governanca-hibrida.svg | Governança Híbrida Trifásico | Integração §1.2 | R2 | ✅ |
| FIG-MUD-01 | fig-4-controle-mudancas.svg | Fluxo de Controle de Mudanças | Integração §1.7.2 | R2 | ✅ |
| FIG-CFD-01 | fig-3-cfd-saudavel-vs-gargalo.svg | CFD Saudável vs. Gargalo | Integração §1.6.1 | R3 | ✅ |
| FIG-SEQ-01 | fig-1-sequenciamento-macro-caminho-critico.svg | Sequenciamento + Caminho Crítico | Cronograma §3.4 | R3→R3.5 | ✅ (v2) |
| FIG-KAN-01 | fig-2-fluxo-kanban-oficial.svg | Fluxo Kanban com Gates e WIP | Integração §1.3.1 | R4 | ✅ |
| FIG-CUST-01 | fig-5-fluxo-prevencao-custos.svg | Fluxo de Prevenção de Custos | Custos §4.2 | R5 | ✅ |
| FIG-CUST-02 | fig-6-matriz-rastreabilidade-dependencias.svg | Matriz de Rastreabilidade | Custos §4.5.2 | R5 | ✅ |
| FIG-ESC-01 | fig-eap-visao-executiva.svg | EAP Visão Executiva | Escopo §2.5 | R6 | ✅ |
| FIG-ESC-02 | fig-2-cadeia-decomposicao-escopo.svg | Cadeia de Decomposição + Gates | Escopo §2.5 | R6 | ✅ |

**Total:** 13 diagramas canônicos (14 SVGs produzidos; 1 refação por overlap na R3.5).

---

## 8. Registro de Inconsistências Sanadas (Transversal)

| # | Inconsistência | Resolução |
|---|---|---|
| I1 | Matriz de rastreabilidade repetida 6 vezes nas rodadas | Consolidada em versão final única (Seção 7) |
| I2 | SVG v1 do sequenciamento com overlap | Marcado SUPERSEDED; v2 canônica |
| I3 | Notas ABNT das Figuras 1-4 apareciam soltas | Consolidadas na Seção 4 |
| I4 | Fronteira M1 ambígua (5 vs 8 planos) | Resolvida: Entrega Faseada (M1=5, M2=3) |
| I5 | Contagem EAP divergente (12/37 vs 13/48) | TAP §4 canônico (12/37); Glossário volátil |
| I6 | Cycle Time "To Do → Done" vs "In Progress → Done" | ADR-003 canônica: In Progress → Done |
| I7 | Grafia "Carleto" vs "Carleto" | TAP v3 canônico: "Carleto" |
| I8 | Estrutura de diretórios proposta vs atual divergente | Ambas documentadas; mapeamento fornecido |

---

## 9. Nota de Encerramento

**Status:** Documento reorganizado, desduplicado e sequenciado temporalmente. Conteúdo de contexto preservado. Snippets SVG integrais. Duplicidades técnicas com o OKB removidas (referências de orientação interna mantidas).

**Natureza confirmada:** `chore` — não integra a estrutura formal do projeto. Reside em `docs/conhecimento/drafts/notas_adjacentes.md` ou localização equivalente no archive.

**Próxima ação sugerida:** Confirmar integridade dos diagramas em `docs/diagramas/` e executar os comandos de recuperação da Seção 6 antes de prosseguir com novas produções.

---

*Fim do documento — Notas Adjacentes v2.0 | COGME | Fatec Taquaritinga | 19–22/09/2026*