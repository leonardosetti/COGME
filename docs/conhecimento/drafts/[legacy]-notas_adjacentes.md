**Veredito Sumário**
Nota registrada como metadado de sessão não canônico. A produção das seções do Plano de Gerenciamento prossegue sem interrupção; a revisão integral será alocada como item de entrada para um ciclo PDCA futuro, sem contaminar a saída formal atual.

**Reformulação Crítica**
A instrução não é uma solicitação de análise, mas um *flag* de estado. A questão operacional subjacente é: como processar essa diretiva de revisão diferida sem gerar ruído ou inconsistência na documentação canônica que está sendo produzida agora.

**Análise de Risco (Técnico + Humano)**
z
- **Técnico**: Risco de deriva de escopo (scope creep) se a "revisão integral" futura não possuir critérios de aceitação e limites de tempo definidos no momento do PDCA.
- **Humano/Organizacional**: Risco de stakeholders consumirem a versão atual como definitiva, gerando atrito político quando a revisão ocorrer. A mitigação exige versionamento explícito (ex: `v0.x-draft-revisão-pendente`).

**Recomendação Justificada**
Isolar esta diretiva no contexto da conversa atual. Prosseguir com a geração diligente das seções do plano solicitadas, mantendo a rastreabilidade lógica das decisões tomadas. Isso garante que, quando o gatilho do PDCA for ativado, a "análise abrangente" tenha um baseline claro para comparar as incongruências, alinhando-se à sua experiência em governança de testes e transição para SDET/Lead.

**Condições de Validade e Gatilhos**

- **Validade**: Indefinida, até a ativação do ciclo PDCA.
- **Gatilho de Reavaliação**: Comando explícito do usuário: "Iniciar revisão integral do Plano de Gerenciamento (PDCA)".

**Premissas Assumidas**

1. Esta nota é um estado transitório de projeto, não um traço persistente de sua persona (portanto, não registrada na memória bio).
2. O usuário iniciará o ciclo PDCA com critérios objetivos, evitando a armadilha de "revisão por revisão" sem ganho de valor de negócio.
3. A produção atual das seções deve manter o padrão de concisão e foco em portabilidade (FOSS/CLI vs. MS) já estabelecido.

Aguardando a próxima seção do Plano de Gerenciamento a ser produzida.

---

Como GP Sênior e PMO do projeto COGME, compreendo perfeitamente a diretriz. A padronização gráfica em `.svg` (com conversão posterior para `.png` para compatibilidade documental) é uma decisão de **Governança Mínima Viável (GMV)** que eleva a qualidade acadêmica e a auditabilidade visual dos artefatos perante o Prof. Dr. Nivaldo Carleto.

Para atender à regra de **legibilidade otimizada para humanos** e evitar a poluição visual (overlaps/edge cuts) que um diagrama único com 12 fases e 37 pacotes causaria, adotei a estratégia de **fracionamento em camadas distintas**. A EAP foi dividida em 4 blocos SVG coesos: Visão Macro, MF1, MF2 e MF3.

A paleta de cores foi unificada e convergente com os exemplos anteriores (Ishikawa e Fluxo de Qualidade):

- **Fundo:** `#FFFFFF`
- **Tipografia:** `Arial, Helvetica, sans-serif`
- **N0 (Raiz):** `#111111` (Preto)
- **MF1 (Fundação):** `#1F3A5F` (Azul Escuro)
- **MF2 (Construção):** `#2E7D32` (Verde Escuro)
- **MF3 (Consolidação):** `#6A1B9A` (Roxo Escuro)
- **Pacotes (Nível 2):** `#F8F9FA` (Cinza claro) com bordas `#555555`

Abaixo estão os scripts SVG prontos para salvamento em `/docs/diagrams/`.

---

### 1. Camada Macro: Nível 0 e Macro-Fases

**Arquivo:** `fig-eap-nivel-0-macro.svg`

~~~xml
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

---

### 2. Camada MF1: Fundação (Fases e Pacotes)

**Arquivo:** `fig-eap-mf1-fundacao.svg`

~~~xml
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

---

### 3. Camada MF2: Construção (Fases e Pacotes)

**Arquivo:** `fig-eap-mf2-construcao.svg`

~~~xml
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

---

### 4. Camada MF3: Consolidação (Fases e Pacotes)

**Arquivo:** `fig-eap-mf3-consolidacao.svg`

~~~xml
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

---

### Matriz Informal de Rastreabilidade de Diagramas (EAP)

| ID         | Arquivo                          | Descrição                       | Camada / Contexto                     |
| ---------- | -------------------------------- | --------------------------------- | ------------------------------------- |
| FIG-EAP-01 | `fig-eap-nivel-0-macro.svg`    | Visão Macro (N0 e Macro-Fases)   | Nível 0 e 1 (Agrupamento)            |
| FIG-EAP-02 | `fig-eap-mf1-fundacao.svg`     | Detalhamento MF1 (Fundação)     | Nível 1 e 2 (N1, N2, N3, N4, N8, N9) |
| FIG-EAP-03 | `fig-eap-mf2-construcao.svg`   | Detalhamento MF2 (Construção)   | Nível 1 e 2 (N5, N6, N7, N10)        |
| FIG-EAP-04 | `fig-eap-mf3-consolidacao.svg` | Detalhamento MF3 (Consolidação) | Nível 1 e 2 (N11, N12)               |

---

### 📝 Nota Adjacente (Registro de Governança)

**Assunto:** Padronização Gráfica e Fracionamento da EAP
**Data:** 21/09/2026
**Contexto:** A geração de um diagrama único contendo as 12 fases e 37 pacotes de trabalho exigiria um `viewBox` excessivamente largo (ex: `3000x1000`), o que resultaria em fontes minúsculas (inferiores a 10px) e quebra da regra de legibilidade otimizada para humanos e impressão em documentos ABNT.
**Decisão:** A EAP foi fracionada em 4 camadas lógicas (Macro + 3 Macro-Fases). Esta abordagem garante que, na conversão para `.png` e inserção no Plano de Escopo (§2.5), cada figura mantenha a densidade informacional ideal, sem overlaps e com a paleta de cores institucional já validada nos diagramas de Ishikawa e Fluxo de Qualidade. Esta ação não constitui mudança de escopo, mas sim refinamento de artefato de suporte (GMV).

Aguardo sua validação visual desta primeira rodada para prosseguirmos com a geração dos próximos diagramas do ciclo (ex: Roadmap Macro, Fluxo de Controle de Mudanças, Sequenciamento).

Como GP Sênior e PMO, acolho a diretriz. A ausência de trade-offs de escopo nesta camada gráfica é um acerto estratégico: diagramas de governança e controle de mudanças são artefatos de **blindagem acadêmica** de alto valor, com custo de elaboração marginal (FOSS) e impacto direto na defensabilidade do modelo híbrido perante o Prof. Dr. Nivaldo Carleto.

Conforme solicitado, as legendas formais (ex: "Figura 1", "Elaborado por") foram **intencionalmente omitidas** do interior dos arquivos `.svg`, restando apenas os rótulos operacionais estritamente necessários para a interpretação ilustrativa do fluxo. A formatação segue rigorosamente a paleta convergente e as regras de legibilidade ABNT (sem overlaps, margens seguras, tipografia Arial/Helvetica).

Abaixo estão os scripts SVG da **Segunda Rodada Candidata**.

---

### 1. Modelo de Governança Híbrida Trifásico

**Arquivo:** `fig-1-governanca-hibrida.svg`

~~~xml
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
  
  <!-- Título Ilustrativo Interno -->
  <text x="400" y="40" text-anchor="middle" font-size="20" font-weight="bold" fill="#111111">Modelo de Governança Híbrida Trifásico</text>

  <!-- Camada 1: PMBOK 7ª (Topo) -->
  <rect x="150" y="80" width="500" height="100" rx="6" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
  <text x="400" y="115" text-anchor="middle" font-size="18" font-weight="bold" fill="#FFFFFF">PMBOK® 7ª Edição</text>
  <text x="400" y="140" text-anchor="middle" font-size="14" fill="#E0E7EF">12 Princípios + 8 Domínios de Desempenho</text>
  <text x="400" y="160" text-anchor="middle" font-size="13" fill="#E0E7EF">(Governança Primária: Por que e Para quê)</text>

  <!-- Seta Descendente 1 -->
  <line x1="400" y1="180" x2="400" y2="210" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar)"/>
  <text x="415" y="200" font-size="11" fill="#555555">Autoridade Normativa</text>

  <!-- Camada 2: PMBOK 6ª (Meio) -->
  <rect x="150" y="220" width="500" height="100" rx="6" fill="#F8F9FA" stroke="#546E7A" stroke-width="2" stroke-dasharray="6,4"/>
  <text x="400" y="255" text-anchor="middle" font-size="18" font-weight="bold" fill="#37474F">PMBOK® 6ª Edição</text>
  <text x="400" y="280" text-anchor="middle" font-size="14" fill="#555555">Processos como Dicionário Complementar</text>
  <text x="400" y="300" text-anchor="middle" font-size="13" fill="#C0392B" font-weight="bold">Obsolescência Assumida para Métricas Preditivas (EVM)</text>

  <!-- Seta Descendente 2 -->
  <line x1="400" y1="320" x2="400" y2="350" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar)"/>
  <text x="415" y="340" font-size="11" fill="#555555">Vocabulário Estrutural</text>

  <!-- Camada 3: Kanban/Ágil (Base) -->
  <rect x="150" y="360" width="500" height="100" rx="6" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
  <text x="400" y="395" text-anchor="middle" font-size="18" font-weight="bold" fill="#FFFFFF">Manifesto Ágil + Kanban (GitHub Projects)</text>
  <text x="400" y="420" text-anchor="middle" font-size="14" fill="#E8F5E9">Fluxo Contínuo, WIP Limits e Métricas de Fluxo</text>
  <text x="400" y="440" text-anchor="middle" font-size="13" fill="#E8F5E9">(Método de Execução: Como o trabalho flui)</text>

  <!-- Setas Laterais de Realimentação -->
  <path d="M 650 410 Q 720 410 720 270 Q 720 130 650 130" fill="none" stroke="#2E7D32" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#ar-green)"/>
  <text x="735" y="275" font-size="12" font-weight="bold" fill="#2E7D32" text-anchor="start">Lições Aprendidas</text>
  <text x="735" y="290" font-size="12" font-weight="bold" fill="#2E7D32" text-anchor="start">e Realimentação</text>
</svg>
~~~

---

### 2. Fluxo de Controle Integrado de Mudanças

**Arquivo:** `fig-4-controle-mudancas.svg`

~~~xml
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
  
  <!-- Título Ilustrativo Interno -->
  <text x="400" y="40" text-anchor="middle" font-size="20" font-weight="bold" fill="#111111">Fluxo de Controle Integrado de Mudanças</text>

  <!-- Etapa 1 -->
  <rect x="200" y="70" width="400" height="60" rx="4" fill="#F8F9FA" stroke="#1F3A5F" stroke-width="2"/>
  <text x="400" y="95" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">1. Abertura de Issue com label</text>
  <text x="400" y="115" text-anchor="middle" font-size="13" fill="#333333">change-request (Qualquer membro | Prazo: Imediato)</text>

  <!-- Seta 1->2 -->
  <line x1="400" y1="130" x2="400" y2="160" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  <text x="415" y="150" font-size="11" fill="#555555">Imediato</text>

  <!-- Etapa 2 -->
  <rect x="200" y="160" width="400" height="60" rx="4" fill="#F8F9FA" stroke="#1F3A5F" stroke-width="2"/>
  <text x="400" y="185" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">2. Análise de impacto (escopo, prazo, qualidade)</text>
  <text x="400" y="205" text-anchor="middle" font-size="13" fill="#333333">Responsável: GP (CCB membro único) | Prazo: ≤ 48h</text>

  <!-- Seta 2->3 -->
  <line x1="400" y1="220" x2="400" y2="250" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  <text x="415" y="240" font-size="11" fill="#555555">≤ 48h</text>

  <!-- Etapa 3: Decisão -->
  <polygon points="400,260 540,300 400,340 260,300" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
  <text x="400" y="295" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">3. Aprovação</text>
  <text x="400" y="315" text-anchor="middle" font-size="12" fill="#333333">pelo CCB (GP)</text>
  <text x="400" y="330" text-anchor="middle" font-size="11" fill="#555555">Prazo: ≤ 24h</text>

  <!-- Ramo de Rejeição -->
  <line x1="540" y1="300" x2="620" y2="300" stroke="#C0392B" stroke-width="2" marker-end="url(#ar-reject)"/>
  <rect x="620" y="270" width="150" height="60" rx="4" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
  <text x="695" y="295" text-anchor="middle" font-size="13" font-weight="bold" fill="#C0392B">Rejeitada</text>
  <text x="695" y="315" text-anchor="middle" font-size="11" fill="#333333">Encerramento com</text>
  <text x="695" y="330" text-anchor="middle" font-size="11" fill="#333333">registro na Issue</text>

  <!-- Ramo de Aprovação (Seta para baixo) -->
  <line x1="400" y1="340" x2="400" y2="380" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-approve)"/>
  <text x="415" y="365" font-size="11" fill="#2E7D32" font-weight="bold">Aprovada</text>

  <!-- Etapa 4 -->
  <rect x="200" y="380" width="400" height="70" rx="4" fill="#F8F9FA" stroke="#1F3A5F" stroke-width="2"/>
  <text x="400" y="410" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">4. Execução da Mudança</text>
  <text x="400" y="435" text-anchor="middle" font-size="13" fill="#333333">Responsável: Equipe | Prazo: ≤ 24h após aprovação</text>

  <!-- Bifurcação da Etapa 4 -->
  <!-- Ramo Esquerdo: Simples -->
  <path d="M 200 415 L 120 415 L 120 480" fill="none" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  <rect x="20" y="480" width="200" height="60" rx="4" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
  <text x="120" y="505" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">Mudança Simples</text>
  <text x="120" y="525" text-anchor="middle" font-size="12" fill="#333333">Atualização de backlog</text>
  <text x="120" y="540" text-anchor="middle" font-size="12" fill="#333333">+ commit na Issue</text>

  <!-- Ramo Direito: Complexa -->
  <path d="M 600 415 L 680 415 L 680 480" fill="none" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  <rect x="580" y="480" width="200" height="60" rx="4" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
  <text x="680" y="505" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">Mudança de Marco / Escopo MVP</text>
  <text x="680" y="525" text-anchor="middle" font-size="12" fill="#333333">Registro formal via ADR +</text>
  <text x="680" y="540" text-anchor="middle" font-size="12" fill="#333333">Comunicação no marco subsequente</text>
</svg>
~~~

---

### Matriz Informal de Rastreabilidade de Diagramas (Atualizada)

| ID                   | Arquivo                          | Descrição                                         | Camada / Contexto                                   |
| -------------------- | -------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| FIG-EAP-01           | `fig-eap-nivel-0-macro.svg`    | Visão Macro (N0 e Macro-Fases)                     | Nível 0 e 1 (Agrupamento)                          |
| FIG-EAP-02           | `fig-eap-mf1-fundacao.svg`     | Detalhamento MF1 (Fundação)                       | Nível 1 e 2 (N1, N2, N3, N4, N8, N9)               |
| FIG-EAP-03           | `fig-eap-mf2-construcao.svg`   | Detalhamento MF2 (Construção)                     | Nível 1 e 2 (N5, N6, N7, N10)                      |
| FIG-EAP-04           | `fig-eap-mf3-consolidacao.svg` | Detalhamento MF3 (Consolidação)                   | Nível 1 e 2 (N11, N12)                             |
| **FIG-GOV-01** | `fig-1-governanca-hibrida.svg` | **Modelo de Governança Híbrida Trifásico** | **Integração §1.2 (Blindagem Acadêmica)** |
| **FIG-MUD-01** | `fig-4-controle-mudancas.svg`  | **Fluxo de Controle Integrado de Mudanças**  | **Integração §1.7.2 (Auditoria do CCB)**   |

---

### 📝 Nota Adjacente (Registro de Governança)

**Assunto:** Validação da Segunda Rodada de Diagramas (Governança e Mudanças)
**Data:** 21/09/2026
**Contexto:** Atendendo à diretriz de zero trade-offs de escopo e custo marginal, os diagramas `FIG-GOV-01` e `FIG-MUD-01` foram projetados para maximizar a clareza acadêmica. A omissão de legendas internas ("Figura X", "Elaborado por") garante que o SVG seja um ativo gráfico puro, pronto para ser inserido nos documentos `.docx`/`.md` com a formatação ABNT externa controlada pelo autor.
**Próximo Passo:** Aguardo a validação visual desta rodada para prosseguirmos com a geração dos diagramas restantes do ciclo (ex: CFD Saudável vs. Gargalo, Sequenciamento Macro/Caminho Crítico Empírico), mantendo a mesma disciplina estética e de rastreabilidade.

Como GP Sênior e PMO, prossigo com a **Terceira Rodada Candidata** de diagramas, mantendo a disciplina estética convergente e a rastreabilidade na matriz informal.

---

### 1. CFD: Padrão Saudável vs. Padrão com Gargalo

**Arquivo:** `fig-3-cfd-saudavel-vs-gargalo.svg`

~~~xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 700" font-family="Arial, Helvetica, sans-serif">
  <rect x="0" y="0" width="1400" height="700" fill="#FFFFFF"/>
  <text x="700" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Cumulative Flow Diagram (CFD) — Padrão Saudável vs. Gargalo</text>
  
  <!-- Painel A: CFD Saudável -->
  <g transform="translate(50, 80)">
    <text x="300" y="0" text-anchor="middle" font-size="18" font-weight="bold" fill="#1F3A5F">(a) CFD Saudável — Fluxo Estável</text>
  
    <!-- Eixos -->
    <line x1="50" y1="40" x2="50" y2="480" stroke="#333333" stroke-width="2"/>
    <line x1="50" y1="480" x2="600" y2="480" stroke="#333333" stroke-width="2"/>
    <text x="20" y="260" text-anchor="middle" font-size="12" fill="#555555" transform="rotate(-90, 20, 260)">Cards Acumulados</text>
    <text x="325" y="510" text-anchor="middle" font-size="12" fill="#555555">Tempo (semanas)</text>
  
    <!-- Bandas paralelas e estáveis -->
    <!-- Done (verde) -->
    <path d="M 50 480 L 600 480 L 600 420 L 50 420 Z" fill="#2E7D32" opacity="0.8"/>
    <text x="580" y="455" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Done</text>
  
    <!-- Code Review (azul claro) -->
    <path d="M 50 420 L 600 420 L 600 370 L 50 370 Z" fill="#4A90E2" opacity="0.8"/>
    <text x="580" y="400" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Code Review</text>
  
    <!-- In Progress (azul médio) -->
    <path d="M 50 370 L 600 370 L 600 310 L 50 310 Z" fill="#1F3A5F" opacity="0.8"/>
    <text x="580" y="345" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">In Progress</text>
  
    <!-- Ready (laranja) -->
    <path d="M 50 310 L 600 310 L 600 260 L 50 260 Z" fill="#E67E22" opacity="0.8"/>
    <text x="580" y="290" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Ready</text>
  
    <!-- Backlog (cinza) -->
    <path d="M 50 260 L 600 260 L 600 200 L 50 200 Z" fill="#7F8C8D" opacity="0.8"/>
    <text x="580" y="235" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Backlog</text>
  
    <!-- Anotação -->
    <text x="325" y="540" text-anchor="middle" font-size="12" fill="#2E7D32" font-weight="bold">Bandas paralelas e de largura constante</text>
    <text x="325" y="555" text-anchor="middle" font-size="11" fill="#555555">Fluxo estável — WIP sob controle</text>
  </g>
  
  <!-- Painel B: CFD com Gargalo -->
  <g transform="translate(750, 80)">
    <text x="300" y="0" text-anchor="middle" font-size="18" font-weight="bold" fill="#C0392B">(b) CFD com Gargalo — Code Review</text>
  
    <!-- Eixos -->
    <line x1="50" y1="40" x2="50" y2="480" stroke="#333333" stroke-width="2"/>
    <line x1="50" y1="480" x2="600" y2="480" stroke="#333333" stroke-width="2"/>
    <text x="20" y="260" text-anchor="middle" font-size="12" fill="#555555" transform="rotate(-90, 20, 260)">Cards Acumulados</text>
    <text x="325" y="510" text-anchor="middle" font-size="12" fill="#555555">Tempo (semanas)</text>
  
    <!-- Bandas com gargalo em Code Review -->
    <!-- Done (verde) - estreita -->
    <path d="M 50 480 L 600 480 L 600 450 L 50 450 Z" fill="#2E7D32" opacity="0.8"/>
    <text x="580" y="470" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Done</text>
  
    <!-- Code Review (azul claro) - ALARGANDO (gargalo) -->
    <path d="M 50 450 L 200 450 L 350 420 L 500 380 L 600 350 L 600 250 L 500 280 L 350 320 L 200 350 L 50 350 Z" fill="#4A90E2" opacity="0.8"/>
    <text x="580" y="310" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Code Review</text>
  
    <!-- Seta indicando alargamento -->
    <path d="M 400 340 L 450 320" stroke="#C0392B" stroke-width="2" marker-end="url(#arrow-red)"/>
    <text x="460" y="315" font-size="10" fill="#C0392B" font-weight="bold">Gargalo</text>
  
    <!-- In Progress (azul médio) - estável -->
    <path d="M 50 350 L 200 350 L 350 320 L 500 280 L 600 250 L 600 200 L 500 230 L 350 270 L 200 300 L 50 300 Z" fill="#1F3A5F" opacity="0.8"/>
    <text x="580" y="230" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">In Progress</text>
  
    <!-- Ready (laranja) - estável -->
    <path d="M 50 300 L 200 300 L 350 270 L 500 230 L 600 200 L 600 160 L 500 190 L 350 230 L 200 260 L 50 260 Z" fill="#E67E22" opacity="0.8"/>
    <text x="580" y="190" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Ready</text>
  
    <!-- Backlog (cinza) - estável -->
    <path d="M 50 260 L 200 260 L 350 230 L 500 190 L 600 160 L 600 120 L 500 150 L 350 190 L 200 220 L 50 220 Z" fill="#7F8C8D" opacity="0.8"/>
    <text x="580" y="150" text-anchor="end" font-size="11" font-weight="bold" fill="#FFFFFF">Backlog</text>
  
    <!-- Anotação -->
    <text x="325" y="540" text-anchor="middle" font-size="12" fill="#C0392B" font-weight="bold">Banda Code Review alargando progressivamente</text>
    <text x="325" y="555" text-anchor="middle" font-size="11" fill="#555555">Gargalo detectado — ação corretiva necessária</text>
  </g>
  
  <!-- Regra de Ação Corretiva (comum aos dois painéis) -->
  <rect x="200" y="620" width="1000" height="60" rx="6" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
  <text x="700" y="645" text-anchor="middle" font-size="14" font-weight="bold" fill="#E65100">Regra de Ação Corretiva (Integração §1.6.1)</text>
  <text x="700" y="665" text-anchor="middle" font-size="12" fill="#333333">Se uma banda ultrapassar 2× a largura média das demais por 2 semanas consecutivas → Retrospectiva extraordinária (ADR-002)</text>
  
  <!-- Definição de marker -->
  <defs>
    <marker id="arrow-red" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L9,3 L0,6 Z" fill="#C0392B"/>
    </marker>
  </defs>
</svg>
~~~

---

### 2. Sequenciamento Macro e Caminho Crítico Empírico

**Arquivo:** `fig-1-sequenciamento-macro-caminho-critico.svg`

~~~xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 650" font-family="Arial, Helvetica, sans-serif">
  <defs>
    <marker id="ar-flow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L9,3 L0,6 Z" fill="#1F3A5F"/>
    </marker>
    <marker id="ar-green" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L9,3 L0,6 Z" fill="#2E7D32"/>
    </marker>
  </defs>
  <rect x="0" y="0" width="1400" height="650" fill="#FFFFFF"/>
  <text x="700" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Sequenciamento Macro e Caminho Crítico Empírico</text>
  
  <!-- Faixa Superior: Macro-Fases e Gates -->
  <g transform="translate(100, 80)">
    <text x="600" y="0" text-anchor="middle" font-size="16" font-weight="bold" fill="#1F3A5F">Camada Macro — Macro-Fases e Gates de Controle</text>
  
    <!-- MF1 -->
    <rect x="50" y="30" width="250" height="80" rx="6" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
    <text x="175" y="55" text-anchor="middle" font-size="15" font-weight="bold" fill="#FFFFFF">MF1: Fundação</text>
    <text x="175" y="75" text-anchor="middle" font-size="12" fill="#E0E7EF">01/09 – 30/09/2026</text>
    <text x="175" y="95" text-anchor="middle" font-size="11" fill="#E0E7EF">5 planos (Áreas 1–5)</text>
  
    <!-- Gate M2 -->
    <polygon points="320,70 360,50 360,90" fill="#E67E22" stroke="#E67E22" stroke-width="2"/>
    <text x="340" y="115" text-anchor="middle" font-size="11" font-weight="bold" fill="#E67E22">M2</text>
    <text x="340" y="130" text-anchor="middle" font-size="10" fill="#555555">30/09</text>
  
    <!-- Calibração (auxiliar) -->
    <rect x="380" y="50" width="120" height="40" rx="4" fill="#FFF3E0" stroke="#E67E22" stroke-width="2" stroke-dasharray="4,2"/>
    <text x="440" y="70" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">Calibração</text>
    <text x="440" y="85" text-anchor="middle" font-size="10" fill="#555555">03/10 (aux)</text>
  
    <!-- MF2 -->
    <rect x="520" y="30" width="250" height="80" rx="6" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
    <text x="645" y="55" text-anchor="middle" font-size="15" font-weight="bold" fill="#FFFFFF">MF2: Construção</text>
    <text x="645" y="75" text-anchor="middle" font-size="12" fill="#E8F5E9">01/10 – 15/11/2026</text>
    <text x="645" y="95" text-anchor="middle" font-size="11" fill="#E8F5E9">MVP funcional + coverage ≥80%</text>
  
    <!-- Gate M3 -->
    <polygon points="790,70 830,50 830,90" fill="#E67E22" stroke="#E67E22" stroke-width="2"/>
    <text x="810" y="115" text-anchor="middle" font-size="11" font-weight="bold" fill="#E67E22">M3</text>
    <text x="810" y="130" text-anchor="middle" font-size="10" fill="#555555">15/11</text>
  
    <!-- MF3 -->
    <rect x="850" y="30" width="250" height="80" rx="6" fill="#6A1B9A" stroke="#6A1B9A" stroke-width="2"/>
    <text x="975" y="55" text-anchor="middle" font-size="15" font-weight="bold" fill="#FFFFFF">MF3: Consolidação</text>
    <text x="975" y="75" text-anchor="middle" font-size="12" fill="#F3E5F5">16/11 – 15/12/2026</text>
    <text x="975" y="95" text-anchor="middle" font-size="11" fill="#F3E5F5">Documentação + Aceite M4</text>
  
    <!-- Gate M4 -->
    <polygon points="1120,70 1160,50 1160,90" fill="#E67E22" stroke="#E67E22" stroke-width="2"/>
    <text x="1140" y="115" text-anchor="middle" font-size="11" font-weight="bold" fill="#E67E22">M4</text>
    <text x="1140" y="130" text-anchor="middle" font-size="10" fill="#555555">15/12</text>
  
    <!-- Setas de fluxo -->
    <line x1="300" y1="70" x2="320" y2="70" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
    <line x1="360" y1="70" x2="380" y2="70" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
    <line x1="500" y1="70" x2="520" y2="70" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
    <line x1="770" y1="70" x2="790" y2="70" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
    <line x1="830" y1="70" x2="850" y2="70" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
    <line x1="1100" y1="70" x2="1120" y2="70" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  </g>
  
  <!-- Faixa Inferior: Caminho Crítico Empírico -->
  <g transform="translate(100, 280)">
    <text x="600" y="0" text-anchor="middle" font-size="16" font-weight="bold" fill="#2E7D32">Camada Operacional — Detectores do Caminho Crítico Empírico</text>
  
    <!-- Detector 1: Cards P0 -->
    <rect x="50" y="40" width="200" height="100" rx="6" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
    <text x="150" y="65" text-anchor="middle" font-size="13" font-weight="bold" fill="#C0392B">Cards P0</text>
    <text x="150" y="85" text-anchor="middle" font-size="11" fill="#333333">Prioridade temporal</text>
    <text x="150" y="100" text-anchor="middle" font-size="11" fill="#333333">crítica do marco</text>
    <text x="150" y="120" text-anchor="middle" font-size="10" fill="#555555">(OKB §9.4)</text>
  
    <!-- Detector 2: Label blocked -->
    <rect x="280" y="40" width="200" height="100" rx="6" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
    <text x="380" y="65" text-anchor="middle" font-size="13" font-weight="bold" fill="#C0392B">Label blocked</text>
    <text x="380" y="85" text-anchor="middle" font-size="11" fill="#333333">Dependência registrada</text>
    <text x="380" y="100" text-anchor="middle" font-size="11" fill="#333333">no corpo da Issue</text>
    <text x="380" y="120" text-anchor="middle" font-size="10" fill="#555555">(OKB §9.1)</text>
  
    <!-- Detector 3: Bandas do CFD -->
    <rect x="510" y="40" width="200" height="100" rx="6" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
    <text x="610" y="65" text-anchor="middle" font-size="13" font-weight="bold" fill="#E65100">Bandas do CFD</text>
    <text x="610" y="85" text-anchor="middle" font-size="11" fill="#333333">Alargamento > 2×</text>
    <text x="610" y="100" text-anchor="middle" font-size="11" fill="#333333">largura média</text>
    <text x="610" y="120" text-anchor="middle" font-size="10" fill="#555555">(Integração §1.6.1)</text>
  
    <!-- Detector 4: Desvio de Cycle Time -->
    <rect x="740" y="40" width="200" height="100" rx="6" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
    <text x="840" y="65" text-anchor="middle" font-size="13" font-weight="bold" fill="#E65100">Desvio Cycle Time</text>
    <text x="840" y="85" text-anchor="middle" font-size="11" fill="#333333">Meta ≤ 3 dias</text>
    <text x="840" y="100" text-anchor="middle" font-size="11" fill="#333333">violada persistentemente</text>
    <text x="840" y="120" text-anchor="middle" font-size="10" fill="#555555">(ADR-003)</text>
  
    <!-- Setas convergindo para Refinement -->
    <line x1="150" y1="140" x2="500" y2="200" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
    <line x1="380" y1="140" x2="500" y2="200" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
    <line x1="610" y1="140" x2="500" y2="200" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
    <line x1="840" y1="140" x2="500" y2="200" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
  
    <!-- Refinement / Replanejamento -->
    <rect x="400" y="200" width="300" height="80" rx="6" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
    <text x="550" y="230" text-anchor="middle" font-size="14" font-weight="bold" fill="#FFFFFF">Refinement Semanal</text>
    <text x="550" y="250" text-anchor="middle" font-size="12" fill="#E8F5E9">+ Retrospectiva Quinzenal</text>
    <text x="550" y="268" text-anchor="middle" font-size="11" fill="#E8F5E9">Decisão de replanejamento</text>
  
    <!-- Seta para camada macro -->
    <path d="M 550 280 L 550 320 L 600 320" fill="none" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
    <text x="580" y="310" font-size="11" fill="#555555">Ajuste de prioridades</text>
  </g>
  
  <!-- Anotação inferior -->
  <rect x="200" y="600" width="1000" height="40" rx="4" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="1"/>
  <text x="700" y="625" text-anchor="middle" font-size="12" fill="#333333">Caminho crítico identificado empiricamente — sem rede CPM preditiva (ADR-003, OKB §8.1)</text>
</svg>
~~~

---

### Matriz Informal de Rastreabilidade de Diagramas (Atualizada)

| ID                   | Arquivo                                            | Descrição                                                 | Camada / Contexto                                     |
| -------------------- | -------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------- |
| FIG-EAP-01           | `fig-eap-nivel-0-macro.svg`                      | Visão Macro (N0 e Macro-Fases)                             | Nível 0 e 1 (Agrupamento)                            |
| FIG-EAP-02           | `fig-eap-mf1-fundacao.svg`                       | Detalhamento MF1 (Fundação)                               | Nível 1 e 2 (N1, N2, N3, N4, N8, N9)                 |
| FIG-EAP-03           | `fig-eap-mf2-construcao.svg`                     | Detalhamento MF2 (Construção)                             | Nível 1 e 2 (N5, N6, N7, N10)                        |
| FIG-EAP-04           | `fig-eap-mf3-consolidacao.svg`                   | Detalhamento MF3 (Consolidação)                           | Nível 1 e 2 (N11, N12)                               |
| FIG-GOV-01           | `fig-1-governanca-hibrida.svg`                   | Modelo de Governança Híbrida Trifásico                   | Integração §1.2                                    |
| FIG-MUD-01           | `fig-4-controle-mudancas.svg`                    | Fluxo de Controle Integrado de Mudanças                    | Integração §1.7.2                                  |
| **FIG-CFD-01** | `fig-3-cfd-saudavel-vs-gargalo.svg`              | **CFD: Padrão Saudável vs. Gargalo**                | **Integração §1.6.1 (Blindagem Acadêmica)** |
| **FIG-SEQ-01** | `fig-1-sequenciamento-macro-caminho-critico.svg` | **Sequenciamento Macro + Caminho Crítico Empírico** | **Cronograma §3.4 (Substituto CPM)**           |

---

### 📝 Nota Adjacente (Registro de Governança)

**Assunto:** Terceira Rodada de Diagramas — CFD e Sequenciamento Macro
**Data:** 21/09/2026
**Contexto:** Os diagramas `FIG-CFD-01` e `FIG-SEQ-01` constituem a **blindagem acadêmica formal** para a ausência de Gantt/EVM e rede CPM preditiva. O CFD dual (saudável vs. gargalo) demonstra visualmente ao Prof. Dr. Nivaldo Carleto como o gargalo é detectado e tratado via métricas de fluxo Kanban (Domínio de Medição PMBOK 7ª). O diagrama de sequenciamento macro substitui visualmente a rede CPM rejeitada pela ADR-003, mostrando os quatro detectores empíricos do caminho crítico (cards P0, label `blocked`, bandas do CFD, desvio de Cycle Time) alimentando a decisão de replanejamento no Refinement semanal.
**Próximo Passo:** Aguardo validação visual desta rodada para prosseguirmos com os diagramas restantes do ciclo (ex: Roadmap Macro do Cronograma, Fluxo Kanban com gates e WIP limits), mantendo a mesma disciplina estética e de rastreabilidade.

Como GP Sênior e PMO, acolho a crítica com total transparência técnica. O *overlap* grosseiro no diagrama anterior ocorreu devido a uma falha de ancoragem: múltiplas setas convergiam para um único ponto cartesiano (`500, 200`), empilhando as pontas das flechas, somado a um *viewBox* subdimensionado que forçava a compressão dos elementos.

Para sanar isso de forma definitiva e garantir **legibilidade otimizada para humanos** (regra ABNT e de UX), reestruturei o diagrama com as seguintes correções:

1. **Canvas Expandido**: `viewBox` ajustado para `1200 x 700`, garantindo margens de respiro (padding) adequadas.
2. **Ancoragem Distribuída**: As setas dos 4 detectores agora apontam para pontos distintos e equidistantes na borda superior da caixa de "Refinement", eliminando totalmente a sobreposição de elementos gráficos.
3. **Tipografia Blindada**: Substituição de textos soltos por blocos `<tspan>` com *dy* controlado, garantindo que nenhuma linha de texto colida com bordas ou outras linhas, independentemente do renderizador.
4. **Fluxo de Feedback Orgânico**: Adição de uma seta curva tracejada que conecta a camada operacional de volta à camada macro, materializando visualmente o conceito de "replanejamento sem violar gates".

Abaixo segue o artefato corrigido e, separadamente, a nota técnica formatada conforme as normas ABNT (NBR 14724 / NBR 12225) para inserção direta no documento acadêmico.

---

### 1. Artefato SVG Otimizado (Sem Overlap)

**Arquivo:** `fig-1-sequenciamento-macro-caminho-critico.svg`

~~~xml
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
  
  <!-- Fundo -->
  <rect x="0" y="0" width="1200" height="700" fill="#FFFFFF"/>
  
  <!-- Título -->
  <text x="600" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Sequenciamento Macro e Caminho Crítico Empírico</text>
  
  <!-- ================= CAMADA SUPERIOR: MACRO-FASES E GATES ================= -->
  <text x="600" y="75" text-anchor="middle" font-size="16" font-weight="bold" fill="#1F3A5F">Camada Macro — Macro-Fases e Gates de Controle</text>
  
  <!-- MF1 -->
  <rect x="60" y="95" width="200" height="70" rx="6" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
  <text x="160" y="120" text-anchor="middle" font-size="14" font-weight="bold" fill="#FFFFFF">
    <tspan x="160" dy="0">MF1: Fundação</tspan>
    <tspan x="160" dy="20" font-size="11" font-weight="normal" fill="#E0E7EF">01/09 – 30/09/2026</tspan>
    <tspan x="160" dy="15" font-size="11" font-weight="normal" fill="#E0E7EF">5 planos (Áreas 1–5)</tspan>
  </text>
  
  <!-- Seta MF1 -> M2 -->
  <line x1="260" y1="130" x2="280" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- Gate M2 -->
  <polygon points="300,110 320,130 300,150 280,130" fill="#E67E22" stroke="#E67E22" stroke-width="2"/>
  <text x="300" y="170" text-anchor="middle" font-size="11" font-weight="bold" fill="#E67E22">M2</text>
  <text x="300" y="185" text-anchor="middle" font-size="10" fill="#555555">30/09</text>
  
  <!-- Seta M2 -> Calibração -->
  <line x1="320" y1="130" x2="340" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- Calibração -->
  <rect x="340" y="105" width="140" height="50" rx="6" fill="#FFF3E0" stroke="#E67E22" stroke-width="2" stroke-dasharray="4,2"/>
  <text x="410" y="125" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">
    <tspan x="410" dy="0">Calibração</tspan>
    <tspan x="410" dy="18" font-size="11" font-weight="normal" fill="#555555">03/10 (auxiliar)</tspan>
  </text>
  
  <!-- Seta Calibração -> MF2 -->
  <line x1="480" y1="130" x2="500" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- MF2 -->
  <rect x="500" y="95" width="200" height="70" rx="6" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
  <text x="600" y="120" text-anchor="middle" font-size="14" font-weight="bold" fill="#FFFFFF">
    <tspan x="600" dy="0">MF2: Construção</tspan>
    <tspan x="600" dy="20" font-size="11" font-weight="normal" fill="#E8F5E9">01/10 – 15/11/2026</tspan>
    <tspan x="600" dy="15" font-size="11" font-weight="normal" fill="#E8F5E9">MVP funcional + coverage ≥80%</tspan>
  </text>
  
  <!-- Seta MF2 -> M3 -->
  <line x1="700" y1="130" x2="720" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- Gate M3 -->
  <polygon points="740,110 760,130 740,150 720,130" fill="#E67E22" stroke="#E67E22" stroke-width="2"/>
  <text x="740" y="170" text-anchor="middle" font-size="11" font-weight="bold" fill="#E67E22">M3</text>
  <text x="740" y="185" text-anchor="middle" font-size="10" fill="#555555">15/11</text>
  
  <!-- Seta M3 -> MF3 -->
  <line x1="760" y1="130" x2="780" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- MF3 -->
  <rect x="780" y="95" width="200" height="70" rx="6" fill="#6A1B9A" stroke="#6A1B9A" stroke-width="2"/>
  <text x="880" y="120" text-anchor="middle" font-size="14" font-weight="bold" fill="#FFFFFF">
    <tspan x="880" dy="0">MF3: Consolidação</tspan>
    <tspan x="880" dy="20" font-size="11" font-weight="normal" fill="#F3E5F5">16/11 – 15/12/2026</tspan>
    <tspan x="880" dy="15" font-size="11" font-weight="normal" fill="#F3E5F5">Documentação + Aceite M4</tspan>
  </text>
  
  <!-- Seta MF3 -> M4 -->
  <line x1="980" y1="130" x2="1000" y2="130" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- Gate M4 -->
  <polygon points="1020,110 1040,130 1020,150 1000,130" fill="#E67E22" stroke="#E67E22" stroke-width="2"/>
  <text x="1020" y="170" text-anchor="middle" font-size="11" font-weight="bold" fill="#E67E22">M4</text>
  <text x="1020" y="185" text-anchor="middle" font-size="10" fill="#555555">15/12</text>

  <!-- ================= CAMADA INFERIOR: CAMINHO CRÍTICO EMPÍRICO ================= -->
  <text x="600" y="240" text-anchor="middle" font-size="16" font-weight="bold" fill="#2E7D32">Camada Operacional — Detectores do Caminho Crítico Empírico</text>
  
  <!-- Detector 1: Cards P0 -->
  <rect x="80" y="270" width="220" height="90" rx="6" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
  <text x="190" y="295" text-anchor="middle" font-size="13" font-weight="bold" fill="#C0392B">
    <tspan x="190" dy="0">Cards P0</tspan>
    <tspan x="190" dy="20" font-size="11" font-weight="normal" fill="#333333">Prioridade temporal</tspan>
    <tspan x="190" dy="15" font-size="11" font-weight="normal" fill="#333333">crítica do marco</tspan>
    <tspan x="190" dy="15" font-size="10" font-weight="normal" fill="#555555">(OKB §9.4)</tspan>
  </text>
  
  <!-- Detector 2: Label blocked -->
  <rect x="330" y="270" width="220" height="90" rx="6" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
  <text x="440" y="295" text-anchor="middle" font-size="13" font-weight="bold" fill="#C0392B">
    <tspan x="440" dy="0">Label blocked</tspan>
    <tspan x="440" dy="20" font-size="11" font-weight="normal" fill="#333333">Dependência registrada</tspan>
    <tspan x="440" dy="15" font-size="11" font-weight="normal" fill="#333333">no corpo da Issue</tspan>
    <tspan x="440" dy="15" font-size="10" font-weight="normal" fill="#555555">(OKB §9.1)</tspan>
  </text>
  
  <!-- Detector 3: Bandas do CFD -->
  <rect x="580" y="270" width="220" height="90" rx="6" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
  <text x="690" y="295" text-anchor="middle" font-size="13" font-weight="bold" fill="#E65100">
    <tspan x="690" dy="0">Bandas do CFD</tspan>
    <tspan x="690" dy="20" font-size="11" font-weight="normal" fill="#333333">Alargamento > 2×</tspan>
    <tspan x="690" dy="15" font-size="11" font-weight="normal" fill="#333333">largura média</tspan>
    <tspan x="690" dy="15" font-size="10" font-weight="normal" fill="#555555">(Integração §1.6.1)</tspan>
  </text>
  
  <!-- Detector 4: Desvio de Cycle Time -->
  <rect x="830" y="270" width="220" height="90" rx="6" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
  <text x="940" y="295" text-anchor="middle" font-size="13" font-weight="bold" fill="#E65100">
    <tspan x="940" dy="0">Desvio Cycle Time</tspan>
    <tspan x="940" dy="20" font-size="11" font-weight="normal" fill="#333333">Meta ≤ 3 dias</tspan>
    <tspan x="940" dy="15" font-size="11" font-weight="normal" fill="#333333">violada persistentemente</tspan>
    <tspan x="940" dy="15" font-size="10" font-weight="normal" fill="#555555">(ADR-003)</tspan>
  </text>
  
  <!-- Setas convergindo para Refinement (pontos distintos no topo da caixa) -->
  <line x1="190" y1="360" x2="380" y2="410" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
  <line x1="440" y1="360" x2="520" y2="410" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
  <line x1="690" y1="360" x2="620" y2="410" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
  <line x1="940" y1="360" x2="720" y2="410" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-green)"/>
  
  <!-- Refinement / Replanejamento -->
  <rect x="330" y="410" width="540" height="80" rx="6" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
  <text x="600" y="440" text-anchor="middle" font-size="15" font-weight="bold" fill="#FFFFFF">
    <tspan x="600" dy="0">Refinement Semanal + Retrospectiva Quinzenal</tspan>
    <tspan x="600" dy="22" font-size="12" font-weight="normal" fill="#E8F5E9">Decisão de replanejamento e ajuste de prioridades</tspan>
    <tspan x="600" dy="16" font-size="11" font-weight="normal" fill="#E8F5E9">(sem violar os gates de controle das Macro-Fases)</tspan>
  </text>
  
  <!-- Seta de Feedback Orgânico para a camada macro -->
  <path d="M 870 450 Q 1100 450 1100 130 L 1040 130" fill="none" stroke="#E67E22" stroke-width="2" stroke-dasharray="5,5" marker-end="url(#ar-feedback)"/>
  <text x="1110" y="290" font-size="11" font-weight="bold" fill="#E67E22" text-anchor="start">Feedback de</text>
  <text x="1110" y="305" font-size="11" font-weight="bold" fill="#E67E22" text-anchor="start">Replanejamento</text>
  
  <!-- Anotação inferior (Nota Técnica) -->
  <rect x="100" y="540" width="1000" height="60" rx="6" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="1.5"/>
  <text x="600" y="565" text-anchor="middle" font-size="12" font-weight="bold" fill="#111111">Nota Técnica:</text>
  <text x="600" y="585" text-anchor="middle" font-size="12" fill="#333333">Caminho crítico identificado empiricamente — sem rede CPM preditiva. Substitui o Gantt/EVM por</text>
  <text x="600" y="600" text-anchor="middle" font-size="12" fill="#333333">métricas de fluxo Kanban, conforme ADR-003 e OKB §8.1.</text>
</svg>
~~~

---

### 2. Nota Técnica ABNT para Inserção Documental

Conforme sua diretriz de separar a renderização da orientação interpretativa, abaixo está o bloco de legenda formatado estritamente conforme as normas ABNT (NBR 14724 para trabalhos acadêmicos e NBR 12225 para legendas de ilustrações). Este bloco deve ser inserido no documento `.docx` ou `.md` imediatamente abaixo da imagem convertida em `.png`.

> **Figura 1** – Sequenciamento Macro e Caminho Crítico Empírico do Projeto COGME.
> **Nota:** O diagrama ilustra a substituição da rede de precedências preditiva (CPM/Gantt) por um modelo de detecção empírica de gargalos, em estrita conformidade com a ADR-003 e o Domínio de Medição do PMBOK® 7ª edição. Os quatro detectores operacionais (Cards P0, label *blocked*, alargamento de bandas no CFD e desvio persistente de *Cycle Time*) alimentam diretamente os rituais de *Refinement* Semanal e Retrospectiva Quinzenal. O *feedback* gerado promove o replanejamento e o ajuste de prioridades sem violar os gates de controle das Macro-Fases (MF1 a MF3), garantindo a governança do fluxo contínuo e a blindagem acadêmica contra a exigência de métricas EVM inaplicáveis.
> **Fonte:** Elaborado pelos autores (2026).

---

### 📝 Nota Adjacente (Registro de Governança)

**Assunto:** Correção de Overlap e Padronização de Notas ABNT
**Data:** 21/09/2026
**Contexto:** A adoção de `<tspan>` com deslocamento vertical (`dy`) controlado no SVG elimina riscos de renderização inconsistente entre visualizadores (navegadores, Word, LaTeX). A separação da "Nota Técnica" do corpo do SVG alinha-se ao princípio de **Governança Mínima Viável (GMV)**: o diagrama foca puramente na representação visual, enquanto o documento textual assume a responsabilidade pela fundamentação acadêmica e rastreabilidade, evitando poluição visual e duplicidade de informação.
**Próximo Passo:** Aguardo validação visual desta versão corrigida para prosseguirmos com a geração dos próximos diagramas pendentes (ex: Fluxo Kanban Oficial com gates e WIP limits), aplicando o mesmo rigor de distribuição espacial e notas ABNT segregadas.

Como GP Sênior e PMO, acolho a diretriz. A separação entre o ativo gráfico puro (`.svg`/`.png`) e a orientação interpretativa textual é uma prática de **Governança Mínima Viável (GMV)** que elimina poluição visual, garante a formatação ABNT (NBR 14724 / NBR 12225) no documento final e fornece a "blindagem acadêmica" necessária para justificar as escolhas metodológicas perante o Prof. Dr. Nivaldo Carleto.

Abaixo estão as notas técnicas retroativas, prontas para serem inseridas imediatamente abaixo de cada respectiva imagem convertida nos documentos do projeto (Plano de Escopo e Plano de Integração).

---

### Notas Técnicas para Inserção Documental (Padrão ABNT)

**Figura 1** – Estrutura Analítica do Projeto (EAP) — Visão Macro e Macro-Fases.
**Nota:** Representação da linha de base estrutural do escopo, canônica conforme o TAP (§4). O diagrama fracionado em camadas substitui a EAP tradicional de página única, que sofreria com *overlaps* e ilegibilidade devido aos 12 níveis de fase e 37 pacotes de trabalho. A visualização hierárquica agrupa os pacotes nas três Macro-Fases (MF1: Fundação, MF2: Construção, MF3: Consolidação), garantindo rastreabilidade imediata entre a raiz do projeto (N0) e os entregáveis de valor.
**Fonte:** Elaborado pelos autores (2026).
*(Arquivo de origem: `fig-eap-nivel-0-macro.svg`)*

**Figura 2** – Detalhamento da Macro-Fase 1 (MF1) — Fundação.
**Nota:** Decomposição dos pacotes de trabalho de Nível 2 referentes à iniciação, planejamento, levantamento de requisitos, modelagem, configuração de ambiente, comunicação e base de conhecimento. Esta camada sustenta os entregáveis do Marco M1 (22/09/2026), incluindo os 5 planos de gerenciamento iniciais e a configuração do SSOT (GitHub Projects), em conformidade com o Domínio de Planejamento do PMBOK® 7ª edição.
**Fonte:** Elaborado pelos autores (2026).
*(Arquivo de origem: `fig-eap-mf1-fundacao.svg`)*

**Figura 3** – Detalhamento da Macro-Fase 2 (MF2) — Construção.
**Nota:** Decomposição dos pacotes de trabalho focados na execução técnica: desenvolvimento do sistema (incluindo SDD com IA), garantia da qualidade (meta de *coverage* ≥ 80%), DevOps/CI/CD e gestão de mudanças. Esta camada materializa o Domínio de Entrega e sustenta o Marco M3 (15/11/2026), onde o MVP funcional deve estar operacional e validado em UAT.
**Fonte:** Elaborado pelos autores (2026).
*(Arquivo de origem: `fig-eap-mf2-construcao.svg`)*

**Figura 4** – Detalhamento da Macro-Fase 3 (MF3) — Consolidação.
**Nota:** Decomposição dos pacotes de trabalho finais, abrangendo a consolidação da documentação técnica e o encerramento formal do projeto. Esta camada garante a rastreabilidade dos critérios de aceite do Marco M4 (15/12/2026), incluindo a verificação SMART e a validação acadêmica final, alinhada ao Domínio de Entrega do PMBOK® 7ª edição.
**Fonte:** Elaborado pelos![image](https://github.com/user-attachments/assets/12345678-1234-1234-1234-123456789012) autores (2026).
*(Arquivo de origem: `fig-eap-mf3-consolidacao.svg`)*

**Figura 5** – Modelo de Governança Híbrida Trifásico.
**Nota:** Ilustração da hierarquia normativa que rege o projeto COGME. A camada superior (PMBOK® 7ª) define os princípios e domínios de desempenho ("por que" e "para quê"); a camada intermediária (PMBOK® 6ª) atua estritamente como dicionário de processos, com obsolescência formalmente declarada para métricas preditivas (EVM); e a camada inferior (Kanban/Manifesto Ágil) define o método de execução operacional ("como"). A seta de realimentação representa o ciclo contínuo de lições aprendidas, blindando o projeto contra questionamentos de falta de estrutura formal.
**Fonte:** Elaborado pelos autores (2026).
*(Arquivo de origem: `fig-1-governanca-hibrida.svg`)*

**Figura 6** – Fluxo de Controle Integrado de Mudanças.
**Nota:** Materialização do Processo 4.6 do PMBOK® 6ª (dicionário) adaptado ao fluxo contínuo Kanban. O diagrama evidencia o CCB de membro único (Gerente de Projeto), os SLAs de resposta (≤ 48h para análise, ≤ 24h para decisão) e a bifurcação de tratamento: mudanças simples são resolvidas via *commit* e atualização do backlog, enquanto alterações de marco ou escopo do MVP exigem registro formal via ADR e comunicação ao avaliador no marco subsequente.
**Fonte:** Elaborado pelos autores (2026).
*(Arquivo de origem: `fig-4-controle-mudancas.svg`)*

**Figura 7** – Cumulative Flow Diagram (CFD) — Padrão Saudável vs. Padrão com Gargalo.
**Nota:** Ferramenta visual de monitoramento temporal que substitui formalmente o Gráfico de Gantt e o Earned Value Management (EVM), declarados inaplicáveis devido ao orçamento zero e ao escopo emergente (ADR-003). O painel (a) demonstra o estado ideal de fluxo estável (bandas paralelas); o painel (b) ilustra a detecção empírica de gargalos (alargamento progressivo de uma banda). Conforme a regra de ação corretiva, se uma banda ultrapassar 2× a largura média das demais por 2 semanas consecutivas, aciona-se uma Retrospectiva extraordinária, atendendo ao Domínio de Medição do PMBOK® 7ª edição.
**Fonte:** Elaborado pelos autores (2026).
*(Arquivo de origem: `fig-3-cfd-saudavel-vs-gargalo.svg`)*

---

### 📝 Nota Adjacente (Registro de Governança)

**Assunto:** Padronização Retroativa de Legendas ABNT para Artefatos Gráficos
**Data:** 21/09/2026
**Contexto:** Em conformidade com a diretriz de separação entre renderização e orientação interpretativa, as notas acima foram redigidas para serem inseridas externamente aos arquivos `.svg`/`.png`. Esta prática elimina a redundância de textos como "Figura X" ou "Elaborado por" dentro do código do diagrama, garantindo que o ativo gráfico seja 100% focado na legibilidade visual, enquanto o documento textual assume a responsabilidade pela fundamentação acadêmica, rastreabilidade (TAP → EAP → Planos) e defesa metodológica perante a banca avaliadora.
**Ação:** Copiar e colar os blocos de texto acima imediatamente abaixo das respectivas imagens nos arquivos `.docx` ou `.md` dos Planos de Escopo (§2.5) e Integração (§1.2, §1.6.1, §1.7.2).

Como GP Sênior e PMO, prossigo com a **Quarta Rodada Candidata** de diagramas, mantendo a disciplina estética convergente e a rastreabilidade na matriz informal.

---

### 1. Fluxo Kanban Oficial com Gates e WIP Limits

**Arquivo:** `fig-2-fluxo-kanban-oficial.svg`

~~~xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 500" font-family="Arial, Helvetica, sans-serif">
  <defs>
    <marker id="ar-flow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L9,3 L0,6 Z" fill="#1F3A5F"/>
    </marker>
  </defs>
  
  <!-- Fundo -->
  <rect x="0" y="0" width="1400" height="500" fill="#FFFFFF"/>
  
  <!-- Título -->
  <text x="700" y="35" text-anchor="middle" font-size="20" font-weight="bold" fill="#111111">Fluxo Kanban Oficial — Gates de Qualidade e WIP Limits</text>
  
  <!-- ================= COLUNAS DO FLUXO ================= -->
  
  <!-- Coluna 1: Backlog -->
  <rect x="40" y="80" width="200" height="320" rx="8" fill="#F4F6F8" stroke="#555555" stroke-width="2"/>
  <text x="140" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#111111">Backlog</text>
  <text x="140" y="135" text-anchor="middle" font-size="11" fill="#555555">Product Backlog</text>
  <text x="140" y="150" text-anchor="middle" font-size="11" fill="#555555">não refinado</text>
  
  <!-- Coluna 2: Ready (DoR) -->
  <rect x="280" y="80" width="200" height="320" rx="8" fill="#E0E7EF" stroke="#1F3A5F" stroke-width="2"/>
  <text x="380" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#111111">Ready (DoR)</text>
  <text x="380" y="135" text-anchor="middle" font-size="11" fill="#333333">Card pronto para</text>
  <text x="380" y="150" text-anchor="middle" font-size="11" fill="#333333">execução</text>
  
  <!-- Coluna 3: In Progress -->
  <rect x="520" y="80" width="200" height="320" rx="8" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
  <text x="620" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">In Progress</text>
  <text x="620" y="135" text-anchor="middle" font-size="11" fill="#E0E7EF">Card em execução</text>
  <text x="620" y="150" text-anchor="middle" font-size="11" fill="#E0E7EF">pelo responsável</text>
  
  <!-- Badge WIP Limit sobre In Progress -->
  <rect x="540" y="60" width="160" height="30" rx="4" fill="#C0392B" stroke="#C0392B" stroke-width="2"/>
  <text x="620" y="80" text-anchor="middle" font-size="12" font-weight="bold" fill="#FFFFFF">WIP LIMIT: 3 cards/pessoa</text>
  
  <!-- Coluna 4: Code Review -->
  <rect x="760" y="80" width="200" height="320" rx="8" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
  <text x="860" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#111111">Code Review</text>
  <text x="860" y="135" text-anchor="middle" font-size="11" fill="#333333">Revisão em pares</text>
  <text x="860" y="150" text-anchor="middle" font-size="11" fill="#333333">obrigatória</text>
  
  <!-- Coluna 5: Done (DoD) -->
  <rect x="1000" y="80" width="200" height="320" rx="8" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
  <text x="1100" y="110" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">Done (DoD)</text>
  <text x="1100" y="135" text-anchor="middle" font-size="11" fill="#E8F5E9">Card concluído</text>
  <text x="1100" y="150" text-anchor="middle" font-size="11" fill="#E8F5E9">e validado</text>
  
  <!-- ================= GATES ENTRE COLUNAS ================= -->
  
  <!-- Gate 1: DoR (entre Backlog e Ready) -->
  <polygon points="250,220 270,240 250,260 230,240" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
  <text x="250" y="285" text-anchor="middle" font-size="10" font-weight="bold" fill="#1F3A5F">Gate DoR</text>
  <text x="250" y="300" text-anchor="middle" font-size="9" fill="#555555">Critérios de</text>
  <text x="250" y="312" text-anchor="middle" font-size="9" fill="#555555">prontidão</text>
  
  <!-- Gate 2: WIP (entre Ready e In Progress) -->
  <polygon points="490,220 510,240 490,260 470,240" fill="#C0392B" stroke="#C0392B" stroke-width="2"/>
  <text x="490" y="285" text-anchor="middle" font-size="10" font-weight="bold" fill="#C0392B">Gate WIP</text>
  <text x="490" y="300" text-anchor="middle" font-size="9" fill="#555555">Capacidade</text>
  <text x="490" y="312" text-anchor="middle" font-size="9" fill="#555555">disponível</text>
  
  <!-- Gate 3: Tasklist + Review (entre In Progress e Code Review) -->
  <polygon points="730,220 750,240 730,260 710,240" fill="#E65100" stroke="#E65100" stroke-width="2"/>
  <text x="730" y="285" text-anchor="middle" font-size="10" font-weight="bold" fill="#E65100">Gate Tasklist</text>
  <text x="730" y="300" text-anchor="middle" font-size="9" fill="#555555">100% itens</text>
  <text x="730" y="312" text-anchor="middle" font-size="9" fill="#555555">concluídos</text>
  
  <!-- Gate 4: DoD (entre Code Review e Done) -->
  <polygon points="970,220 990,240 970,260 950,240" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
  <text x="970" y="285" text-anchor="middle" font-size="10" font-weight="bold" fill="#2E7D32">Gate DoD</text>
  <text x="970" y="300" text-anchor="middle" font-size="9" fill="#555555">Critérios de</text>
  <text x="970" y="312" text-anchor="middle" font-size="9" fill="#555555">conclusão</text>
  
  <!-- ================= SETAS DE FLUXO ================= -->
  
  <!-- Seta Backlog → Ready -->
  <line x1="240" y1="240" x2="270" y2="240" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- Seta Ready → In Progress -->
  <line x1="480" y1="240" x2="510" y2="240" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- Seta In Progress → Code Review -->
  <line x1="720" y1="240" x2="750" y2="240" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- Seta Code Review → Done -->
  <line x1="960" y1="240" x2="990" y2="240" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- ================= ANOTAÇÃO INFERIOR ================= -->
  
  <rect x="100" y="420" width="1200" height="60" rx="6" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="1.5"/>
  <text x="700" y="445" text-anchor="middle" font-size="12" font-weight="bold" fill="#111111">Regra de Ação Corretiva (ADR-002 + ADR-004):</text>
  <text x="700" y="465" text-anchor="middle" font-size="11" fill="#333333">Se WIP limit for violado ou tasklist não estiver 100% concluída, o card não migra para a coluna seguinte.</text>
  <text x="700" y="478" text-anchor="middle" font-size="11" fill="#333333">Gargalos persistentes acionam Retrospectiva extraordinária (Integração §1.6.1).</text>
</svg>
~~~

---

### 2. Nota Técnica ABNT para Inserção Documental

> **Figura 2** – Fluxo Kanban Oficial com Gates de Qualidade e WIP Limits do Projeto COGME.
> **Nota:** O diagrama materializa operacionalmente a ADR-002 (Kanban como método de execução) e a ADR-004 (tasklists Markdown como substituto de subissues). As cinco colunas representam o fluxo contínuo do trabalho (Backlog → Ready → In Progress → Code Review → Done), com quatro gates de qualidade intermediários: (i) Gate DoR na entrada de Ready, exigindo critérios de prontidão atendidos; (ii) Gate WIP na entrada de In Progress, respeitando o limite de 3 cards por pessoa (prevenção de burnout, Domínio de Equipe PMBOK 7ª); (iii) Gate Tasklist na entrada de Code Review, exigindo 100% dos itens da tasklist Markdown concluídos (ADR-004); e (iv) Gate DoD na entrada de Done, exigindo critérios de conclusão atendidos (coverage ≥ 80%, revisão de pares aprovada, commit mergeado). O badge vermelho sobre a coluna In Progress destaca o WIP limit como mecanismo de controle de capacidade. A regra de ação corretiva inferior demonstra que violações de gates bloqueiam o fluxo e gargalos persistentes acionam Retrospectiva extraordinária, em conformidade com o Domínio de Medição do PMBOK® 7ª edição.
> **Fonte:** Elaborado pelos autores (2026).
> *(Arquivo de origem: `fig-2-fluxo-kanban-oficial.svg`)*

---

### Matriz Informal de Rastreabilidade de Diagramas (Atualizada)

| ID                   | Arquivo                                            | Descrição                                           | Camada / Contexto                                                |
| -------------------- | -------------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------- |
| FIG-EAP-01           | `fig-eap-nivel-0-macro.svg`                      | Visão Macro (N0 e Macro-Fases)                       | Nível 0 e 1 (Agrupamento)                                       |
| FIG-EAP-02           | `fig-eap-mf1-fundacao.svg`                       | Detalhamento MF1 (Fundação)                         | Nível 1 e 2 (N1, N2, N3, N4, N8, N9)                            |
| FIG-EAP-03           | `fig-eap-mf2-construcao.svg`                     | Detalhamento MF2 (Construção)                       | Nível 1 e 2 (N5, N6, N7, N10)                                   |
| FIG-EAP-04           | `fig-eap-mf3-consolidacao.svg`                   | Detalhamento MF3 (Consolidação)                     | Nível 1 e 2 (N11, N12)                                          |
| FIG-GOV-01           | `fig-1-governanca-hibrida.svg`                   | Modelo de Governança Híbrida Trifásico             | Integração §1.2                                               |
| FIG-MUD-01           | `fig-4-controle-mudancas.svg`                    | Fluxo de Controle Integrado de Mudanças              | Integração §1.7.2                                             |
| FIG-CFD-01           | `fig-3-cfd-saudavel-vs-gargalo.svg`              | CFD: Padrão Saudável vs. Gargalo                    | Integração §1.6.1                                             |
| FIG-SEQ-01           | `fig-1-sequenciamento-macro-caminho-critico.svg` | Sequenciamento Macro + Caminho Crítico Empírico     | Cronograma §3.4                                                 |
| **FIG-KAN-01** | `fig-2-fluxo-kanban-oficial.svg`                 | **Fluxo Kanban Oficial com Gates e WIP Limits** | **Integração §1.3.1 (Operacionalização ADR-002/004)** |

---

### 📝 Nota Adjacente (Registro de Governança)

**Assunto:** Quarta Rodada de Diagramas — Fluxo Kanban Oficial
**Data:** 21/09/2026
**Contexto:** O diagrama `FIG-KAN-01` constitui o **artefato visual central** do projeto COGME, materializando em uma única imagem os mecanismos operacionais de governança do fluxo contínuo. A distribuição horizontal (LR — Left to Right) foi escolhida para maximizar a legibilidade em documentos A4/Letter, com as cinco colunas ocupando 80% da largura útil e os gates intermediários claramente separados. O badge de WIP limit em vermelho sobre a coluna In Progress destaca visualmente o mecanismo de prevenção de burnout (Domínio de Equipe PMBOK 7ª), enquanto a anotação inferior reforça a regra de ação corretiva.
**Próximo Passo:** Aguardo validação visual desta rodada para prosseguirmos com a geração dos próximos diagramas pendentes (ex: Fluxo de Prevenção de Custos, Matriz de Rastreabilidade de Dependências), mantendo a mesma disciplina estética e de rastreabilidade.

Como GP Sênior e PMO, prossigo com a **Quinta Rodada Candidata** de diagramas, completando o Plano de Custos (Área 4) com os dois artefatos gráficos pendentes.

---

### 1. Fluxo de Prevenção de Custos

**Arquivo:** `fig-5-fluxo-prevencao-custos.svg`

~~~xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 900" font-family="Arial, Helvetica, sans-serif">
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
  
  <rect x="0" y="0" width="800" height="900" fill="#FFFFFF"/>
  <text x="400" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Fluxo de Prevenção de Custos — Conformidade FOSS</text>
  
  <!-- Etapa Inicial -->
  <rect x="250" y="80" width="300" height="60" rx="6" fill="#F8F9FA" stroke="#1F3A5F" stroke-width="2"/>
  <text x="400" y="105" text-anchor="middle" font-size="14" font-weight="bold" fill="#111111">Nova dependência identificada</text>
  <text x="400" y="125" text-anchor="middle" font-size="12" fill="#555555">(biblioteca, API, ferramenta, serviço)</text>
  
  <!-- Seta 1 -->
  <line x1="400" y1="140" x2="400" y2="180" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- Gate 1: Licença OSI -->
  <polygon points="400,180 520,220 400,260 280,220" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
  <text x="400" y="215" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">Gate 1:</text>
  <text x="400" y="235" text-anchor="middle" font-size="12" fill="#333333">Licença OSI-approved?</text>
  
  <!-- Ramo NÃO (rejeição) -->
  <line x1="520" y1="220" x2="620" y2="220" stroke="#C0392B" stroke-width="2" marker-end="url(#ar-reject)"/>
  <text x="570" y="210" text-anchor="middle" font-size="11" font-weight="bold" fill="#C0392B">NÃO</text>
  <rect x="620" y="190" width="150" height="60" rx="4" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
  <text x="695" y="215" text-anchor="middle" font-size="12" font-weight="bold" fill="#C0392B">Rejeição imediata</text>
  <text x="695" y="235" text-anchor="middle" font-size="10" fill="#333333">Buscar alternativa FOSS</text>
  
  <!-- Ramo SIM -->
  <line x1="400" y1="260" x2="400" y2="300" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-approve)"/>
  <text x="415" y="285" font-size="11" font-weight="bold" fill="#2E7D32">SIM</text>
  
  <!-- Gate 2: Plano gratuito -->
  <polygon points="400,300 520,340 400,380 280,340" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
  <text x="400" y="335" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">Gate 2:</text>
  <text x="400" y="355" text-anchor="middle" font-size="12" fill="#333333">Plano gratuito suficiente</text>
  <text x="400" y="370" text-anchor="middle" font-size="12" fill="#333333">para MVP acadêmico?</text>
  
  <!-- Ramo NÃO (buscar alternativa) -->
  <line x1="520" y1="340" x2="620" y2="340" stroke="#E65100" stroke-width="2" marker-end="url(#ar-flow)"/>
  <text x="570" y="330" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">NÃO</text>
  <rect x="620" y="310" width="150" height="60" rx="4" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
  <text x="695" y="335" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">Buscar alternativa FOSS</text>
  <text x="695" y="355" text-anchor="middle" font-size="10" fill="#333333">com plano gratuito</text>
  
  <!-- Seta de retorno -->
  <path d="M 695 370 L 695 390 L 400 390 L 400 380" fill="none" stroke="#E65100" stroke-width="1.5" stroke-dasharray="4,2"/>
  
  <!-- Ramo SIM -->
  <line x1="400" y1="380" x2="400" y2="420" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-approve)"/>
  <text x="415" y="405" font-size="11" font-weight="bold" fill="#2E7D32">SIM</text>
  
  <!-- Gate 3: Registro em ADR -->
  <polygon points="400,420 520,460 400,500 280,460" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
  <text x="400" y="455" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">Gate 3:</text>
  <text x="400" y="475" text-anchor="middle" font-size="12" fill="#333333">Registrado em ADR-001</text>
  <text x="400" y="490" text-anchor="middle" font-size="12" fill="#333333">ou nova ADR?</text>
  
  <!-- Ramo NÃO (registrar) -->
  <line x1="520" y1="460" x2="620" y2="460" stroke="#E65100" stroke-width="2" marker-end="url(#ar-flow)"/>
  <text x="570" y="450" text-anchor="middle" font-size="11" font-weight="bold" fill="#E65100">NÃO</text>
  <rect x="620" y="430" width="150" height="60" rx="4" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
  <text x="695" y="455" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">Registrar antes de usar</text>
  <text x="695" y="475" text-anchor="middle" font-size="10" fill="#333333">ADR específica ou</text>
  <text x="695" y="488" text-anchor="middle" font-size="10" fill="#333333">atualização ADR-001</text>
  
  <!-- Seta de retorno -->
  <path d="M 695 490 L 695 510 L 400 510 L 400 500" fill="none" stroke="#E65100" stroke-width="1.5" stroke-dasharray="4,2"/>
  
  <!-- Ramo SIM -->
  <line x1="400" y1="500" x2="400" y2="540" stroke="#2E7D32" stroke-width="2" marker-end="url(#ar-approve)"/>
  <text x="415" y="525" font-size="11" font-weight="bold" fill="#2E7D32">SIM</text>
  
  <!-- Aprovação Final -->
  <rect x="250" y="540" width="300" height="60" rx="6" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
  <text x="400" y="565" text-anchor="middle" font-size="14" font-weight="bold" fill="#FFFFFF">Incorporação autorizada</text>
  <text x="400" y="585" text-anchor="middle" font-size="12" fill="#E8F5E9">Dependência FOSS conformante</text>
  
  <!-- Anotação de change-request -->
  <rect x="150" y="650" width="500" height="80" rx="6" fill="#FDECEA" stroke="#C0392B" stroke-width="2"/>
  <text x="400" y="675" text-anchor="middle" font-size="13" font-weight="bold" fill="#C0392B">Desvio de qualquer gate aciona:</text>
  <text x="400" y="695" text-anchor="middle" font-size="12" fill="#333333">Issue com label change-request (Integração §1.7)</text>
  <text x="400" y="712" text-anchor="middle" font-size="11" fill="#555555">Análise de impacto pelo GP (CCB) em ≤ 48h</text>
  <text x="400" y="725" text-anchor="middle" font-size="11" fill="#555555">Registro em ADR se alteração de marco ou escopo MVP</text>
  
  <!-- Linha de base -->
  <rect x="150" y="780" width="500" height="50" rx="4" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="1.5"/>
  <text x="400" y="805" text-anchor="middle" font-size="12" font-weight="bold" fill="#111111">Linha de Base de Custos: R$ 0,00 (imutável sem CCB)</text>
  <text x="400" y="820" text-anchor="middle" font-size="11" fill="#555555">TAP §11 + Premissa P2 (FOSS absoluto)</text>
</svg>
~~~

---

### 2. Matriz de Rastreabilidade de Dependências

**Arquivo:** `fig-6-matriz-rastreabilidade-dependencias.svg`

~~~xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" font-family="Arial, Helvetica, sans-serif">
  <rect x="0" y="0" width="1200" height="500" fill="#FFFFFF"/>
  <text x="600" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Matriz de Rastreabilidade de Dependências — Stack FOSS Canônica</text>
  
  <!-- Cabeçalho da Tabela -->
  <rect x="50" y="80" width="1100" height="50" rx="4" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
  <text x="150" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">Dependência</text>
  <text x="320" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">Versão</text>
  <text x="470" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">Licença</text>
  <text x="620" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">Conformidade</text>
  <text x="770" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">EAP N1.4/N4.4</text>
  <text x="920" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">ADR-001</text>
  <text x="1070" y="110" text-anchor="middle" font-size="13" font-weight="bold" fill="#FFFFFF">Categoria</text>
  
  <!-- Linha 1: FastAPI -->
  <rect x="50" y="130" width="1100" height="50" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1"/>
  <text x="150" y="160" text-anchor="middle" font-size="12" fill="#111111">FastAPI</text>
  <text x="320" y="160" text-anchor="middle" font-size="12" fill="#333333">≥0.100</text>
  <text x="470" y="160" text-anchor="middle" font-size="12" fill="#333333">MIT</text>
  <text x="620" y="160" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
  <text x="770" y="160" text-anchor="middle" font-size="12" fill="#333333">N4.4</text>
  <text x="920" y="160" text-anchor="middle" font-size="12" fill="#333333">✅</text>
  <text x="1070" y="160" text-anchor="middle" font-size="11" fill="#555555">Backend</text>
  
  <!-- Linha 2: SQLite -->
  <rect x="50" y="180" width="1100" height="50" rx="4" fill="#FFFFFF" stroke="#555555" stroke-width="1"/>
  <text x="150" y="210" text-anchor="middle" font-size="12" fill="#111111">SQLite</text>
  <text x="320" y="210" text-anchor="middle" font-size="12" fill="#333333">3.x</text>
  <text x="470" y="210" text-anchor="middle" font-size="12" fill="#333333">Public Domain</text>
  <text x="620" y="210" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
  <text x="770" y="210" text-anchor="middle" font-size="12" fill="#333333">N4.4</text>
  <text x="920" y="210" text-anchor="middle" font-size="12" fill="#333333">✅</text>
  <text x="1070" y="210" text-anchor="middle" font-size="11" fill="#555555">Banco de Dados</text>
  
  <!-- Linha 3: WeasyPrint -->
  <rect x="50" y="230" width="1100" height="50" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1"/>
  <text x="150" y="260" text-anchor="middle" font-size="12" fill="#111111">WeasyPrint</text>
  <text x="320" y="260" text-anchor="middle" font-size="12" fill="#333333">≥59.0</text>
  <text x="470" y="260" text-anchor="middle" font-size="12" fill="#333333">BSD-3-Clause</text>
  <text x="620" y="260" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
  <text x="770" y="260" text-anchor="middle" font-size="12" fill="#333333">N4.4</text>
  <text x="920" y="260" text-anchor="middle" font-size="12" fill="#333333">✅</text>
  <text x="1070" y="260" text-anchor="middle" font-size="11" fill="#555555">Geração PDF</text>
  
  <!-- Linha 4: pytest -->
  <rect x="50" y="280" width="1100" height="50" rx="4" fill="#FFFFFF" stroke="#555555" stroke-width="1"/>
  <text x="150" y="310" text-anchor="middle" font-size="12" fill="#111111">pytest</text>
  <text x="320" y="310" text-anchor="middle" font-size="12" fill="#333333">≥7.0</text>
  <text x="470" y="310" text-anchor="middle" font-size="12" fill="#333333">MIT</text>
  <text x="620" y="310" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
  <text x="770" y="310" text-anchor="middle" font-size="12" fill="#333333">N4.4</text>
  <text x="920" y="310" text-anchor="middle" font-size="12" fill="#333333">✅</text>
  <text x="1070" y="310" text-anchor="middle" font-size="11" fill="#555555">Testes</text>
  
  <!-- Linha 5: GitHub Actions -->
  <rect x="50" y="330" width="1100" height="50" rx="4" fill="#F8F9FA" stroke="#555555" stroke-width="1"/>
  <text x="150" y="360" text-anchor="middle" font-size="12" fill="#111111">GitHub Actions</text>
  <text x="320" y="360" text-anchor="middle" font-size="12" fill="#333333">Free Tier</text>
  <text x="470" y="360" text-anchor="middle" font-size="12" fill="#333333">Proprietário gratuito</text>
  <text x="620" y="360" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
  <text x="770" y="360" text-anchor="middle" font-size="12" fill="#333333">N1.4</text>
  <text x="920" y="360" text-anchor="middle" font-size="12" fill="#333333">✅</text>
  <text x="1070" y="360" text-anchor="middle" font-size="11" fill="#555555">CI/CD</text>
  
  <!-- Linha 6: llama.cpp -->
  <rect x="50" y="380" width="1100" height="50" rx="4" fill="#FFFFFF" stroke="#555555" stroke-width="1"/>
  <text x="150" y="410" text-anchor="middle" font-size="12" fill="#111111">llama.cpp</text>
  <text x="320" y="410" text-anchor="middle" font-size="12" fill="#333333">0.4.0-dev</text>
  <text x="470" y="410" text-anchor="middle" font-size="12" fill="#333333">MIT</text>
  <text x="620" y="410" text-anchor="middle" font-size="14" fill="#2E7D32" font-weight="bold">✅</text>
  <text x="770" y="410" text-anchor="middle" font-size="12" fill="#333333">N4.4</text>
  <text x="920" y="410" text-anchor="middle" font-size="12" fill="#333333">✅</text>
  <text x="1070" y="410" text-anchor="middle" font-size="11" fill="#555555">SDD Local (IA)</text>
  
  <!-- Rodapé -->
  <rect x="50" y="450" width="1100" height="40" rx="4" fill="#E8F5E9" stroke="#2E7D32" stroke-width="2"/>
  <text x="600" y="475" text-anchor="middle" font-size="13" font-weight="bold" fill="#2E7D32">100% das dependências auditadas e conformantes — Linha de base R$ 0,00 preservada</text>
</svg>
~~~

---

### Notas Técnicas ABNT para Inserção Documental

> **Figura 5** – Fluxo de Prevenção de Custos — Conformidade FOSS do Projeto COGME.
> **Nota:** O diagrama materializa operacionalmente a governança de custo zero (TAP §11), demonstrando que "orçamento nulo" não constitui ausência de controle, mas sim governança rigorosa sobre conformidade de licenciamento. Os três gates sequenciais (Gate 1: licença OSI-approved; Gate 2: plano gratuito suficiente para MVP acadêmico; Gate 3: registro em ADR-001 ou ADR específica) garantem que nenhuma dependência seja incorporada sem auditoria prévia. Desvios de qualquer gate acionam o fluxo de controle integrado de mudanças (Integração §1.7), com análise de impacto pelo GP (CCB de membro único) em ≤ 48h e registro formal via ADR quando a alteração impactar marcos ou escopo do MVP. A linha de base de custos (R$ 0,00) é imutável sem aprovação do CCB, em conformidade com a Premissa P2 (FOSS absoluto) e a Restrição TAP §8.4.
> **Fonte:** Elaborado pelos autores (2026).
> *(Arquivo de origem: `fig-5-fluxo-prevencao-custos.svg`)*

> **Figura 6** – Matriz de Rastreabilidade de Dependências — Stack FOSS Canônica do Projeto COGME.
> **Nota:** A tabela apresenta seis exemplos reais de dependências da stack canônica (FastAPI, SQLite, WeasyPrint, pytest, GitHub Actions, llama.cpp), todas com conformidade FOSS verificada (ícone ✅). Cada dependência é rastreável à fase da EAP responsável pela auditoria (N1.4 — Política de Licenciamento FOSS ou N4.4 — Auditoria de Licenças) e à ADR-001 (Stack Tecnológica FOSS), que documenta a decisão arquitetural de adoção. A matriz demonstra ao avaliador que "custo zero" é auditável e verificável, não apenas declarado. A whitelist completa de licenças aprovadas (MIT, Apache 2.0, BSD, GPL, LGPL, ISC, PSF, Public Domain) e a blacklist de licenças proibidas (proprietárias, shareware, Creative Commons, Source Available não-OSI) estão definidas no Plano de Custos §4.5.1.
> **Fonte:** Elaborado pelos autores (2026).
> *(Arquivo de origem: `fig-6-matriz-rastreabilidade-dependencias.svg`)*

---

### Matriz Informal de Rastreabilidade de Diagramas (Atualizada)

| ID                    | Arquivo                                            | Descrição                                                   | Camada / Contexto                                  |
| --------------------- | -------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------- |
| FIG-EAP-01            | `fig-eap-nivel-0-macro.svg`                      | Visão Macro (N0 e Macro-Fases)                               | Nível 0 e 1 (Agrupamento)                         |
| FIG-EAP-02            | `fig-eap-mf1-fundacao.svg`                       | Detalhamento MF1 (Fundação)                                 | Nível 1 e 2 (N1, N2, N3, N4, N8, N9)              |
| FIG-EAP-03            | `fig-eap-mf2-construcao.svg`                     | Detalhamento MF2 (Construção)                               | Nível 1 e 2 (N5, N6, N7, N10)                     |
| FIG-EAP-04            | `fig-eap-mf3-consolidacao.svg`                   | Detalhamento MF3 (Consolidação)                             | Nível 1 e 2 (N11, N12)                            |
| FIG-GOV-01            | `fig-1-governanca-hibrida.svg`                   | Modelo de Governança Híbrida Trifásico                     | Integração §1.2                                 |
| FIG-MUD-01            | `fig-4-controle-mudancas.svg`                    | Fluxo de Controle Integrado de Mudanças                      | Integração §1.7.2                               |
| FIG-CFD-01            | `fig-3-cfd-saudavel-vs-gargalo.svg`              | CFD: Padrão Saudável vs. Gargalo                            | Integração §1.6.1                               |
| FIG-SEQ-01            | `fig-1-sequenciamento-macro-caminho-critico.svg` | Sequenciamento Macro + Caminho Crítico Empírico             | Cronograma §3.4                                   |
| FIG-KAN-01            | `fig-2-fluxo-kanban-oficial.svg`                 | Fluxo Kanban Oficial com Gates e WIP Limits                   | Integração §1.3.1                               |
| **FIG-CUST-01** | `fig-5-fluxo-prevencao-custos.svg`               | **Fluxo de Prevenção de Custos — Conformidade FOSS** | **Custos §4.2 (Governança de Custo Zero)** |
| **FIG-CUST-02** | `fig-6-matriz-rastreabilidade-dependencias.svg`  | **Matriz de Rastreabilidade de Dependências**          | **Custos §4.5.2 (Auditoria FOSS)**          |

---

### 📝 Nota Adjacente (Registro de Governança)

**Assunto:** Quinta Rodada de Diagramas — Plano de Custos (Área 4)
**Data:** 21/09/2026
**Contexto:** Os diagramas `FIG-CUST-01` e `FIG-CUST-02` completam a blindagem acadêmica do Plano de Custos, demonstrando visualmente ao Prof. Dr. Nivaldo Carleto que: (i) "custo zero" é governança ativa, não ausência de controle (FIG-CUST-01); e (ii) 100% das dependências são auditáveis e rastreáveis às fases da EAP e às ADRs (FIG-CUST-02). A paleta de cores segue o padrão convergente (azul #1F3A5F para processos, verde #2E7D32 para aprovação, vermelho #C0392B para rejeição, laranja #E65100 para ações corretivas), garantindo consistência visual com os diagramas anteriores.
**Próximo Passo:** Aguardo validação visual desta rodada para prosseguirmos com a geração dos diagramas pendentes do Plano de Qualidade (Área 5), que incluirá os 12 PDCAs consolidados e o Diagrama de Ishikawa 6M para coverage insuficiente.


Como GP Sênior e PMO, prossigo com a **Sexta Rodada Candidata** de diagramas, completando a Seção 2 (Escopo) com os dois artefatos gráficos pendentes.

---

### 1. EAP — Visão Executiva Consolidada

**Arquivo:** `fig-eap-visao-executiva.svg`

~~~xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 850" font-family="Arial, Helvetica, sans-serif">
  <defs>
    <marker id="ar-flow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L9,3 L0,6 Z" fill="#1F3A5F"/>
    </marker>
  </defs>
  
  <rect x="0" y="0" width="1200" height="850" fill="#FFFFFF"/>
  <text x="600" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Estrutura Analítica do Projeto (EAP) — Visão Executiva</text>
  
  <!-- N0: Raiz -->
  <rect x="450" y="70" width="300" height="60" rx="6" fill="#111111" stroke="#111111" stroke-width="2"/>
  <text x="600" y="105" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFFFFF">N0: COGME</text>
  
  <!-- Linha vertical N0 para MFs -->
  <line x1="600" y1="130" x2="600" y2="170" stroke="#777777" stroke-width="2"/>
  
  <!-- ================= MF1: FUNDAÇÃO ================= -->
  <rect x="50" y="170" width="1100" height="200" rx="8" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
  <text x="600" y="195" text-anchor="middle" font-size="16" font-weight="bold" fill="#1F3A5F">MF1: Fundação (01/09 – 30/09/2026)</text>
  
  <!-- N1 -->
  <rect x="70" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
  <text x="150" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N1</text>
  <text x="150" y="255" text-anchor="middle" font-size="11" fill="#333333">Iniciação e</text>
  <text x="150" y="270" text-anchor="middle" font-size="11" fill="#333333">Planejamento</text>
  <text x="150" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(5 pacotes)</text>
  
  <!-- N2 -->
  <rect x="245" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
  <text x="325" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N2</text>
  <text x="325" y="255" text-anchor="middle" font-size="11" fill="#333333">Levantamento de</text>
  <text x="325" y="270" text-anchor="middle" font-size="11" fill="#333333">Requisitos</text>
  <text x="325" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(3 pacotes)</text>
  
  <!-- N3 -->
  <rect x="420" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
  <text x="500" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N3</text>
  <text x="500" y="255" text-anchor="middle" font-size="11" fill="#333333">Modelagem e</text>
  <text x="500" y="270" text-anchor="middle" font-size="11" fill="#333333">Prototipação</text>
  <text x="500" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(3 pacotes)</text>
  
  <!-- N4 -->
  <rect x="595" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
  <text x="675" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N4</text>
  <text x="675" y="255" text-anchor="middle" font-size="11" fill="#333333">Configuração de</text>
  <text x="675" y="270" text-anchor="middle" font-size="11" fill="#333333">Ambiente</text>
  <text x="675" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(4 pacotes)</text>
  
  <!-- N8 -->
  <rect x="770" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
  <text x="850" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N8</text>
  <text x="850" y="255" text-anchor="middle" font-size="11" fill="#333333">Comunicação</text>
  <text x="850" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(2 pacotes)</text>
  
  <!-- N9 -->
  <rect x="945" y="210" width="160" height="140" rx="4" fill="#FFFFFF" stroke="#1F3A5F" stroke-width="2"/>
  <text x="1025" y="235" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N9</text>
  <text x="1025" y="255" text-anchor="middle" font-size="11" fill="#333333">Base de</text>
  <text x="1025" y="270" text-anchor="middle" font-size="11" fill="#333333">Conhecimento</text>
  <text x="1025" y="295" text-anchor="middle" font-size="12" font-weight="bold" fill="#1F3A5F">(3 pacotes)</text>
  
  <!-- ================= MF2: CONSTRUÇÃO ================= -->
  <rect x="50" y="390" width="1100" height="200" rx="8" fill="#F4F6F8" stroke="#2E7D32" stroke-width="2"/>
  <text x="600" y="415" text-anchor="middle" font-size="16" font-weight="bold" fill="#2E7D32">MF2: Construção (01/10 – 15/11/2026)</text>
  
  <!-- N5 -->
  <rect x="120" y="430" width="200" height="140" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
  <text x="220" y="455" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N5</text>
  <text x="220" y="475" text-anchor="middle" font-size="11" fill="#333333">Desenvolvimento</text>
  <text x="220" y="490" text-anchor="middle" font-size="11" fill="#333333">do Sistema</text>
  <text x="220" y="515" text-anchor="middle" font-size="12" font-weight="bold" fill="#2E7D32">(5 pacotes)</text>
  
  <!-- N6 -->
  <rect x="340" y="430" width="200" height="140" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
  <text x="440" y="455" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N6</text>
  <text x="440" y="475" text-anchor="middle" font-size="11" fill="#333333">Garantia da</text>
  <text x="440" y="490" text-anchor="middle" font-size="11" fill="#333333">Qualidade</text>
  <text x="440" y="515" text-anchor="middle" font-size="12" font-weight="bold" fill="#2E7D32">(3 pacotes)</text>
  
  <!-- N7 -->
  <rect x="560" y="430" width="200" height="140" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
  <text x="660" y="455" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N7</text>
  <text x="660" y="475" text-anchor="middle" font-size="11" fill="#333333">DevOps e CI/CD</text>
  <text x="660" y="515" text-anchor="middle" font-size="12" font-weight="bold" fill="#2E7D32">(1 pacote)</text>
  
  <!-- N10 -->
  <rect x="780" y="430" width="200" height="140" rx="4" fill="#FFFFFF" stroke="#2E7D32" stroke-width="2"/>
  <text x="880" y="455" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N10</text>
  <text x="880" y="475" text-anchor="middle" font-size="11" fill="#333333">Gestão de</text>
  <text x="880" y="490" text-anchor="middle" font-size="11" fill="#333333">Mudanças</text>
  <text x="880" y="515" text-anchor="middle" font-size="12" font-weight="bold" fill="#2E7D32">(3 pacotes)</text>
  
  <!-- ================= MF3: CONSOLIDAÇÃO ================= -->
  <rect x="50" y="610" width="1100" height="200" rx="8" fill="#F4F6F8" stroke="#6A1B9A" stroke-width="2"/>
  <text x="600" y="635" text-anchor="middle" font-size="16" font-weight="bold" fill="#6A1B9A">MF3: Consolidação (16/11 – 15/12/2026)</text>
  
  <!-- N11 -->
  <rect x="250" y="650" width="250" height="140" rx="4" fill="#FFFFFF" stroke="#6A1B9A" stroke-width="2"/>
  <text x="375" y="675" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N11</text>
  <text x="375" y="695" text-anchor="middle" font-size="11" fill="#333333">Documentação</text>
  <text x="375" y="710" text-anchor="middle" font-size="11" fill="#333333">do Projeto</text>
  <text x="375" y="735" text-anchor="middle" font-size="12" font-weight="bold" fill="#6A1B9A">(2 pacotes)</text>
  
  <!-- N12 -->
  <rect x="550" y="650" width="250" height="140" rx="4" fill="#FFFFFF" stroke="#6A1B9A" stroke-width="2"/>
  <text x="675" y="675" text-anchor="middle" font-size="13" font-weight="bold" fill="#111111">N12</text>
  <text x="675" y="695" text-anchor="middle" font-size="11" fill="#333333">Encerramento</text>
  <text x="675" y="735" text-anchor="middle" font-size="12" font-weight="bold" fill="#6A1B9A">(3 pacotes)</text>
  
  <!-- Anotação inferior -->
  <rect x="200" y="820" width="800" height="25" rx="4" fill="#E8F5E9" stroke="#2E7D32" stroke-width="1"/>
  <text x="600" y="837" text-anchor="middle" font-size="11" fill="#333333">Total: 12 fases de Nível 1 + 37 pacotes de Nível 2 (baseline canônica do TAP §4)</text>
</svg>
~~~

---

### 2. Cadeia de Decomposição do Escopo e Gates de Qualidade

**Arquivo:** `fig-2-cadeia-decomposicao-escopo.svg`

~~~xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 650" font-family="Arial, Helvetica, sans-serif">
  <defs>
    <marker id="ar-flow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L9,3 L0,6 Z" fill="#1F3A5F"/>
    </marker>
  </defs>
  
  <rect x="0" y="0" width="1400" height="650" fill="#FFFFFF"/>
  <text x="700" y="40" text-anchor="middle" font-size="22" font-weight="bold" fill="#111111">Cadeia de Decomposição do Escopo e Gates de Qualidade</text>
  
  <!-- ================= NÍVEL 1: PACOTE EAP N2 ================= -->
  <rect x="50" y="100" width="280" height="400" rx="6" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="2"/>
  <text x="190" y="130" text-anchor="middle" font-size="14" font-weight="bold" fill="#1F3A5F">Nível 1: Pacote EAP (N2)</text>
  <text x="190" y="150" text-anchor="middle" font-size="11" fill="#555555">Entrega substantiva</text>
  
  <!-- Exemplo: N5.1 -->
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
  
  <!-- ================= SETA 1→2 ================= -->
  <line x1="330" y1="320" x2="420" y2="320" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- Gate DoR -->
  <polygon points="375,300 395,320 375,340 355,320" fill="#1F3A5F" stroke="#1F3A5F" stroke-width="2"/>
  <text x="375" y="365" text-anchor="middle" font-size="10" font-weight="bold" fill="#1F3A5F">Gate DoR</text>
  
  <!-- ================= NÍVEL 2: CARD UBÍQUO KANBAN ================= -->
  <rect x="420" y="100" width="280" height="400" rx="6" fill="#F4F6F8" stroke="#2E7D32" stroke-width="2"/>
  <text x="560" y="130" text-anchor="middle" font-size="14" font-weight="bold" fill="#2E7D32">Nível 2: Card Ubíquo Kanban</text>
  <text x="560" y="150" text-anchor="middle" font-size="11" fill="#555555">Unidade atômica (≤ 8h)</text>
  
  <!-- Exemplo: Card Padrão A -->
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
  
  <!-- ================= SETA 2→3 ================= -->
  <line x1="700" y1="320" x2="790" y2="320" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  
  <!-- Gate Tasklist + Review -->
  <polygon points="745,300 765,320 745,340 725,320" fill="#E65100" stroke="#E65100" stroke-width="2"/>
  <text x="745" y="365" text-anchor="middle" font-size="10" font-weight="bold" fill="#E65100">Gate Tasklist</text>
  <text x="745" y="380" text-anchor="middle" font-size="9" fill="#555555">+ Review</text>
  
  <!-- ================= NÍVEL 3: TASKLIST MARKDOWN ================= -->
  <rect x="790" y="100" width="280" height="400" rx="6" fill="#F4F6F8" stroke="#6A1B9A" stroke-width="2"/>
  <text x="930" y="130" text-anchor="middle" font-size="14" font-weight="bold" fill="#6A1B9A">Nível 3: Tasklist Markdown</text>
  <text x="930" y="150" text-anchor="middle" font-size="11" fill="#555555">Atividades derivadas (ADR-004)</text>
  
  <!-- Exemplo: Tasklist -->
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
  
  <!-- ================= ANOTAÇÃO LATERAL ================= -->
  <rect x="1100" y="150" width="280" height="120" rx="6" fill="#FFF3E0" stroke="#E65100" stroke-width="2"/>
  <text x="1240" y="175" text-anchor="middle" font-size="12" font-weight="bold" fill="#E65100">Regras de Métrica</text>
  <text x="1240" y="200" text-anchor="middle" font-size="11" fill="#333333">✓ Métricas de fluxo medem</text>
  <text x="1240" y="215" text-anchor="middle" font-size="11" fill="#333333">o card pai (ADR-003)</text>
  <text x="1240" y="240" text-anchor="middle" font-size="11" fill="#C0392B" font-weight="bold">✗ Subissues rejeitadas</text>
  <text x="1240" y="255" text-anchor="middle" font-size="11" fill="#C0392B" font-weight="bold">(ADR-004)</text>
  
  <!-- ================= GATE DoD (saída) ================= -->
  <line x1="1070" y1="320" x2="1100" y2="320" stroke="#1F3A5F" stroke-width="2" marker-end="url(#ar-flow)"/>
  <polygon points="1085,300 1105,320 1085,340 1065,320" fill="#2E7D32" stroke="#2E7D32" stroke-width="2"/>
  <text x="1085" y="365" text-anchor="middle" font-size="10" font-weight="bold" fill="#2E7D32">Gate DoD</text>
  
  <!-- ================= ANOTAÇÃO INFERIOR ================= -->
  <rect x="100" y="530" width="1200" height="100" rx="6" fill="#F4F6F8" stroke="#1F3A5F" stroke-width="1.5"/>
  <text x="700" y="555" text-anchor="middle" font-size="12" font-weight="bold" fill="#111111">Fundamentação PMBOK 6ª (dicionário) + ADR-004:</text>
  <text x="700" y="580" text-anchor="middle" font-size="11" fill="#333333">Processo 6.2 (Definir Atividades): pacotes EAP decompõem-se em atividades derivadas (ações verbais).</text>
  <text x="700" y="600" text-anchor="middle" font-size="11" fill="#333333">No COGME, atividades são materializadas como tasklist Markdown (3 a 7 itens; último item "Validação final"),</text>
  <text x="700" y="615" text-anchor="middle" font-size="11" fill="#333333">rejeitando-se formalmente subissues para preservar a unidade atômica de métrica (card pai) e evitar fragmentação do backlog.</text>
</svg>
~~~

---

### Notas Técnicas ABNT para Inserção Documental

> **Figura 1** – Estrutura Analítica do Projeto (EAP) — Visão Executiva Consolidada do Projeto COGME.
> **Nota:** A representação visual da EAP em visão executiva materializa o Processo 5.4 (Criar EAP/WBS) do PMBOK® 6ª edição (dicionário) e o Domínio de Planejamento do PMBOK® 7ª edição. A estrutura hierárquica apresenta a raiz N0 (COGME) no topo, decomposta em 12 fases de Nível 1 (N1 a N12) agrupadas em três Macro-Fases temporais: MF1 — Fundação (6 fases, 20 pacotes), MF2 — Construção (4 fases, 12 pacotes) e MF3 — Consolidação (2 fases, 5 pacotes), totalizando 37 pacotes de trabalho de Nível 2, conforme a baseline canônica aprovada no TAP §4. A opção pela não abertura dos 37 pacotes nesta visão executiva preserva a legibilidade em documentos A4/Letter e evita poluição visual, em conformidade com o princípio de Governança Mínima Viável (GMV). O detalhamento completo dos pacotes de Nível 2 encontra-se no TAP §4 e nos Planos de Escopo §2.5. A contagem de 12 fases e 37 pacotes constitui a linha de base canônica do projeto; eventuais divergências em artefatos vivos (Glossário) são resolvidas pela prevalência do TAP, sem necessidade de solicitação de mudança (Nota de Canonicidade, Escopo §2.5).
> **Fonte:** Elaborado pelos autores (2026).
> *(Arquivo de origem: `fig-eap-visao-executiva.svg`)*

> **Figura 2** – Cadeia de Decomposição do Escopo e Gates de Qualidade do Projeto COGME.
> **Nota:** O diagrama materializa a operacionalização do Processo 6.2 (Definir Atividades) do PMBOK® 6ª edição (dicionário) no método Kanban adotado pelo COGME (ADR-002). A cadeia de decomposição apresenta três níveis encadeados horizontalmente: (i) Pacote de Trabalho EAP de Nível 2 — entrega substantiva (ex: N5.1 — Backend: Lógica de Negócio), com rastreabilidade à fase, macro-fase, requisitos e domínio PMBOK 7ª; (ii) Card Ubíquo Kanban — unidade atômica de backlog e métrica (≤ 8h), redigido conforme os Padrões A (documental) ou B (User Story GWT) definidos no OKB §9.3, com contexto ubíquo autocontido e critérios de aceite binários; (iii) Atividades Derivadas como Tasklist Markdown — checklist nativo do GitHub (3 a 7 itens verbais, último item obrigatoriamente "Validação final"), conforme ADR-004, que rejeita formalmente subissues. Os gates de qualidade anotados entre os níveis são: Gate DoR (Definition of Ready) na entrada da coluna Ready; Gate Tasklist + Revisão de Pares na entrada da coluna Code Review (exigindo 100% dos itens da tasklist concluídos); e Gate DoD (Definition of Done) na entrada da coluna Done. A anotação lateral destaca que as métricas de fluxo (Cycle Time, Throughput, CFD) medem exclusivamente o card pai (ADR-003), preservando a unidade atômica de métrica e evitando distorção por fragmentação. Esta abordagem blinda academicamente a rejeição de subissues perante o Prof. Dr. Nivaldo Carleto, demonstrando que a decomposição de cards complexos (≥ 6h) ocorre sem violar o fluxo Kanban nem o princípio GMV.
> **Fonte:** Elaborado pelos autores (2026).
> *(Arquivo de origem: `fig-2-cadeia-decomposicao-escopo.svg`)*

---

### Matriz Informal de Rastreabilidade de Diagramas (Atualizada)

| ID                   | Arquivo                                            | Descrição                                                            | Camada / Contexto                                         |
| -------------------- | -------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------- |
| FIG-EAP-01           | `fig-eap-nivel-0-macro.svg`                      | Visão Macro (N0 e Macro-Fases)                                        | Nível 0 e 1 (Agrupamento)                                |
| FIG-EAP-02           | `fig-eap-mf1-fundacao.svg`                       | Detalhamento MF1 (Fundação)                                          | Nível 1 e 2 (N1, N2, N3, N4, N8, N9)                     |
| FIG-EAP-03           | `fig-eap-mf2-construcao.svg`                     | Detalhamento MF2 (Construção)                                        | Nível 1 e 2 (N5, N6, N7, N10)                            |
| FIG-EAP-04           | `fig-eap-mf3-consolidacao.svg`                   | Detalhamento MF3 (Consolidação)                                      | Nível 1 e 2 (N11, N12)                                   |
| FIG-GOV-01           | `fig-1-governanca-hibrida.svg`                   | Modelo de Governança Híbrida Trifásico                              | Integração §1.2                                        |
| FIG-MUD-01           | `fig-4-controle-mudancas.svg`                    | Fluxo de Controle Integrado de Mudanças                               | Integração §1.7.2                                      |
| FIG-CFD-01           | `fig-3-cfd-saudavel-vs-gargalo.svg`              | CFD: Padrão Saudável vs. Gargalo                                     | Integração §1.6.1                                      |
| FIG-SEQ-01           | `fig-1-sequenciamento-macro-caminho-critico.svg` | Sequenciamento Macro + Caminho Crítico Empírico                      | Cronograma §3.4                                          |
| FIG-KAN-01           | `fig-2-fluxo-kanban-oficial.svg`                 | Fluxo Kanban Oficial com Gates e WIP Limits                            | Integração §1.3.1                                      |
| FIG-CUST-01          | `fig-5-fluxo-prevencao-custos.svg`               | Fluxo de Prevenção de Custos — Conformidade FOSS                    | Custos §4.2                                              |
| FIG-CUST-02          | `fig-6-matriz-rastreabilidade-dependencias.svg`  | Matriz de Rastreabilidade de Dependências                             | Custos §4.5.2                                            |
| **FIG-ESC-01** | `fig-eap-visao-executiva.svg`                    | **EAP — Visão Executiva Consolidada (12 fases × 37 pacotes)** | **Escopo §2.5 (Processo 5.4 PMBOK 6ª)**           |
| **FIG-ESC-02** | `fig-2-cadeia-decomposicao-escopo.svg`           | **Cadeia de Decomposição do Escopo e Gates de Qualidade**      | **Escopo §2.5 (Processo 6.2 PMBOK 6ª + ADR-004)** |

---

### 📝 Nota Adjacente (Registro de Governança)

**Assunto:** Sexta Rodada de Diagramas — Seção 2 (Escopo) Completada
**Data:** 21/09/2026
**Contexto:** Os diagramas `FIG-ESC-01` e `FIG-ESC-02` completam a blindagem acadêmica da Seção 2 (Escopo), preenchendo os slots vazios do TAP §4 e materializando visualmente a operacionalização dos Processos 5.4 e 6.2 do PMBOK® 6ª (dicionário) no método Kanban. A EAP em visão executiva (FIG-ESC-01) apresenta as 12 fases e 37 pacotes agrupados em 3 Macro-Fases, sem abertura dos pacotes para preservar legibilidade. A cadeia de decomposição (FIG-ESC-02) demonstra como os pacotes EAP se decompõem em cards Kanban e tasklists Markdown, com gates de qualidade (DoR, Tasklist+Review, DoD) e rejeição formal de subissues (ADR-004). Ambas as figuras seguem a paleta convergente (azul #1F3A5F, verde #2E7D32, roxo #6A1B9A) e as regras de legibilidade ABNT (sem overlaps, tipografia Arial/Helvetica, sem legendas internas).
**Próximo Passo:** Aguardo validação visual desta rodada para prosseguirmos com a geração dos diagramas pendentes do Plano de Qualidade (Área 5), que incluirá os 12 PDCAs consolidados e o Diagrama de Ishikawa 6M para coverage insuficiente.



# Registro de Incidente e Estratégia de Recuperação

## 1. Acknowledgment

Recebo sua comunicação. A decisão de executar a reestruturação em paralelo com produção ativa de artefatos é um **trade-off consciente** que você assumiu como GP. Não há julgamento — há aprendizado. O que importa agora é **recuperar o máximo possível** e **registrar a lição** para que o PDCA do projeto absorva essa experiência.

---

## 2. Análise de Impacto: O Que Pode Ter Sido Perdido

Com base no `git status` anterior e na estrutura atual, identifico as seguintes **áreas de risco de perda**:

### 2.1 Diagramas Recentes (Alta Probabilidade de Perda Parcial)

| Arquivo Original                                                 | Status na Reestruturação                                 | Risco                                           |
| ---------------------------------------------------------------- | ---------------------------------------------------------- | ----------------------------------------------- |
| `docs/diagrams/fig-1-eap-executiva.svg`                        | Movido para`docs/diagramas/eap/fig-01-eap-executiva.svg` | ⚠️ Verificar se o conteúdo é o mais recente |
| `docs/diagrams/fig-1-sequenciamento-macro-caminho-critico.svg` | Movido para`docs/diagramas/cronograma/`                  | ⚠️ Verificar                                  |
| `docs/diagrams/fig-eap-mf1-fundacao.svg`                       | Movido para`docs/diagramas/eap/`                         | ⚠️ Verificar                                  |
| `docs/diagrams/fig-eap-mf2-construcao.svg`                     | Movido para`docs/diagramas/eap/`                         | ⚠️ Verificar                                  |
| `docs/diagrams/fig-eap-mf3-consolidacao.svg`                   | Movido para`docs/diagramas/eap/`                         | ⚠️ Verificar                                  |
| `docs/diagrams/fig-eap-nivel-0-macro.svg/.png`                 | Movido para`docs/diagramas/eap/`                         | ⚠️ Verificar                                  |
| `docs/diagrams/fig-3-cfd-saudavel-vs-gargalo.svg`              | Arquivado em`docs/archive/diagramas-deprecated/`         | ⚠️ Pode conter refinamentos recentes          |
| `docs/diagrams/fig-4-controle-mudancas.svg`                    | Arquivado em`docs/archive/diagramas-deprecated/`         | ⚠️ Pode conter refinamentos recentes          |
| `docs/diagrams/1.svg`                                          | **Nunca classificado** (Anomalia A1)                 | 🔴 Provavelmente perdido                        |
| `docs/diagrams/fig-02-fluxo-kanban.mmd.png`                    | Deletado, sem correspondente canônico                     | 🔴 Perdido (era renderização Mermaid)         |

### 2.2 Textos de Projeto Recentes (Média Probabilidade de Perda)

| Arquivo                                        | Movido Para              | Risco                                     |
| ---------------------------------------------- | ------------------------ | ----------------------------------------- |
| `docs/md/relatorios/analise_arquitetural.md` | `docs/archive/drafts/` | ⚠️ Pode conter análise recente         |
| `docs/md/relatorios/Canon_Stack_SDD.md`      | `docs/archive/drafts/` | ⚠️ Base para a reestruturação         |
| `docs/md/relatorios/hardware.md`             | `docs/archive/drafts/` | ⚠️ Especificação de hardware          |
| `docs/md/relatorios/llm_base_persona.md`     | `docs/archive/drafts/` | ⚠️ Base para personas SDD               |
| `docs/md/proposta_estrutural.md`             | `docs/archive/drafts/` | ⚠️ Proposta de reestruturação         |
| `docs/md/reestrutura_EAP.md`                 | `docs/archive/drafts/` | ⚠️ Trabalho recente de EAP              |
| `docs/md/monitoramenteo_inconsistencias.md`  | `docs/archive/drafts/` | ⚠️ Monitoramento ativo                  |
| `redacao_progressiva.md` (raiz)              | `docs/archive/drafts/` | ⚠️ Contém análises críticas recentes |
| `notas_adjacentes.md` (raiz)                 | `docs/archive/drafts/` | ⚠️ Veredito sumário recente            |

### 2.3 Planos e Seções do TAP (Baixa Probabilidade de Perda)

| Arquivo                        | Movido Para                    | Risco                                                  |
| ------------------------------ | ------------------------------ | ------------------------------------------------------ |
| `docs/md/TAP/sec_*.md/.docx` | `docs/archive/tap-sections/` | ✅ Preservado (consolidado em`docs/tap/TAP.md`)      |
| `docs/docx/AC*.docx`         | `docs/archive/docx/`         | ✅ Preservado (versões canônicas em`docs/planos/`) |
| `docs/md/TAP/EAP/*.drawio`   | `docs/diagramas/eap/`        | ✅ Preservado                                          |

### 2.4 Arquivos Potencialmente Perdidos (Sem Rastro)

| Arquivo                                         | Evidência                                     | Status                                                            |
| ----------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------- |
| `docs/diagrams/1.svg`                         | Aparecia como untracked no git status anterior | 🔴**Provavelmente perdido** — nunca foi `git add`-ed     |
| `docs/diagrams/fig-02-fluxo-kanban.mmd.png`   | Aparecia como deleted, sem correspondente      | 🔴**Perdido** — era renderização Mermaid do fluxo Kanban |
| `docs/docx/.~1_Integracao.docx`               | Arquivo temporário do Word                    | ✅ Descarte correto                                               |
| `docs/docx/.~rmo-de-Abertura-do-Projeto.docx` | Arquivo temporário do Word                    | ✅ Descarte correto                                               |

---

## 3. Estratégia de Recuperação

### 3.1 Recuperação via Git (Arquivos Versionados)

~~~bash
# 1. Verificar histórico recente (últimas 48h)
git log --since="2026-09-20" --oneline --all

# 2. Ver reflog para encontrar estados anteriores
git reflog --since="2026-09-20"

# 3. Se encontrar um commit anterior à reestruturação com trabalho recente:
# git show <hash>:<caminho-do-arquivo> > /tmp/recovered_file.ext

# 4. Listar todos os arquivos deletados nos últimos commits
git log --diff-filter=D --summary --since="2026-09-20" --name-only

# 5. Recuperar um arquivo específico de um commit anterior
# git checkout <hash> -- <caminho-do-arquivo>
~~~

### 3.2 Verificação de Integridade dos Arquivos Movidos

~~~bash
# Comparar arquivos em archive com os canônicos (para detectar se versões recentes foram sobrescritas)

# Diagramas: comparar deprecated com canônicos
diff docs/archive/diagramas-deprecated/fig-3-cfd-saudavel-vs-gargalo.svg docs/diagramas/integracao/fig-03-cfd-comparativo.svg 2>/dev/null || echo "Arquivos diferentes ou ausentes"
diff docs/archive/diagramas-deprecated/fig-4-controle-mudancas.svg docs/diagramas/integracao/fig-04-fluxo-mudancas.svg 2>/dev/null || echo "Arquivos diferentes ou ausentes"

# Textos: verificar se drafts contêm trabalho recente
wc -l docs/archive/drafts/*.md
# Arquivos com muitas linhas provavelmente contêm trabalho substancial
~~~

### 3.3 Verificação de Arquivos Não Versionados (Perdidos)

~~~bash
# Procurar por arquivos .svg órfãos no sistema de arquivos
find . -name "*.svg" -newer docs/planos/plano-integracao.md 2>/dev/null

# Procurar por arquivos temporários do Mermaid
find . -name "*.mmd" -o -name "*.mmd.png" 2>/dev/null

# Verificar lixeira do sistema (macOS)
ls ~/.Trash/*.svg 2>/dev/null || echo "Nada na lixeira"
~~~

---

## 4. Priorização do Retrabalho

| Prioridade   | Item                                                                                                 | Esforço Estimado | Justificativa                                                 |
| ------------ | ---------------------------------------------------------------------------------------------------- | ----------------- | ------------------------------------------------------------- |
| **P0** | Verificar`docs/diagrams/1.svg` (Anomalia A1)                                                       | 5 min             | Pode ser diagrama crítico não identificado                  |
| **P0** | Regenerar`fig-02-fluxo-kanban.mmd.png`                                                             | 15 min            | Renderização Mermaid do fluxo Kanban (Integração §1.3.1) |
| **P1** | Verificar se`fig-3-cfd-saudavel-vs-gargalo.svg` tem refinamentos vs `fig-03-cfd-comparativo.svg` | 10 min            | Pode conter versão mais detalhada do CFD                     |
| **P1** | Verificar se`fig-4-controle-mudancas.svg` tem refinamentos vs `fig-04-fluxo-mudancas.svg`        | 10 min            | Pode conter versão mais detalhada do fluxo                   |
| **P1** | Revisar`docs/archive/drafts/reestrutura_EAP.md` e `proposta_estrutural.md`                       | 30 min            | Podem conter decisões recentes sobre EAP                     |
| **P2** | Revisar`docs/archive/drafts/analise_arquitetural.md`                                               | 20 min            | Pode conter análise relevante para M2                        |
| **P2** | Revisar`docs/archive/drafts/llm_base_persona.md`                                                   | 15 min            | Base para personas SDD (.ai/personas/)                        |
| **P3** | Revisar demais drafts em`docs/archive/drafts/`                                                     | 1h                | Varredura geral por conteúdo recuperável                    |

---

## 5. Registro como Lição Aprendida (PDCA)

Este incidente deve ser registrado como lição aprendida da MF1:

~~~markdown
## Lição Aprendida — LA-001: Reestruturação de Repositório em Paralelo com Produção

**Data**: 22/09/2026
**Macro-Fase**: MF1 (Fundação)
**Domínio PMBOK 7ª**: Trabalho do Projeto + Entrega

### O que aconteceu
A reestruturação formal do repositório (aderência à stack SDD canônica) foi executada em paralelo com produção ativa de diagramas e textos de projeto. Durante a movimentação de arquivos (mv do sistema + git add -A), alguns artefatos recentes foram perdidos ou deslocados para localizações incorretas.

### Causa raiz
1. Ausência de branch dedicada para reestruturação (operação em `main` direta)
2. Uso de `mv` do sistema em vez de `git mv` (perda de rastreabilidade de rename)
3. Execução de `git add -A` sem verificação prévia da árvore de destino
4. Produção ativa de artefatos durante a janela de reestruturação

### Impacto
- Perda de 1-2 diagramas recentes (fig-02-fluxo-kanban.mmd.png, possivelmente 1.svg)
- Deslocamento temporário de diagramas canônicos para archive (corrigido em commit subsequente)
- Necessidade de retrabalho estimado em 2-3h

### Ação corretiva (imediata)
- Commit corretivo `fix(diagramas)` para restaurar localização canônica
- Verificação via `git reflog` para recuperação de artefatos perdidos
- Retrabalho priorizado dos itens P0-P2

### Ação preventiva (futuro)
- **Regra**: Reestruturações de diretório SEMPRE em branch dedicada (`chore/restructure-*`)
- **Regra**: Usar `git mv` em vez de `mv` para qualquer movimentação de arquivo versionado
- **Regra**: Congelar produção de artefatos durante reestruturação (janela de manutenção)
- **Regra**: Verificar `tree` da estrutura de destino ANTES de `git add -A`
- **Regra**: Commit único de reestruturação com mensagem descritiva + tag de rollback

### Rastreabilidade
- Commits: `7121d12`, `1aa1515`
- OKB v3.0 §3.2 (SSOT documental)
- Glossário §5 (Stack SDD)
~~~

**Localização canônica**: `docs/conhecimento/licoes-aprendidas/MF1-licoes.md`

---

## 6. Recomendação Imediata ao GP

1. **Execute os comandos da seção 3.1** para verificar se há commits recuperáveis via `git reflog`
2. **Execute os comandos da seção 3.2** para comparar versões arquivadas vs canônicas
3. **Retrabalhe os itens P0** (5-20 min) antes de prosseguir com qualquer nova produção
4. **Registre LA-001** em `docs/conhecimento/licoes-aprendidas/MF1-licoes.md`
5. **Prosseguir com o Plano de Qualidade** (Área 5) apenas após confirmar que os diagramas de Ishikawa (FIG-5, 6, 7) estão íntegros em `docs/diagramas/qualidade/`

Estou à disposição para auxiliar na recuperação de qualquer artefato específico ou na regeneração de diagramas perdidos.

 --- 

 Seção revisiva: Analisar, convergir e descartar duplicidades:

 De acordo com as edições do Guia PMBOK® e o contexto de governança híbrida do projeto COGME, a resposta técnica é dual, mas com uma **ressalva operacional crítica** declarada nos nossos artefatos.

### 1. Resposta Teórica (Dicionário PMBOK®)
*   **PMBOK® 6ª Edição (Dicionário Complementar)**: A área de conhecimento é o **Gerenciamento do Cronograma do Projeto**. Especificamente, os processos **6.4 (Sequenciar as Atividades)**, que gera o *Diagrama de Rede do Cronograma do Projeto*, e **6.6 (Desenvolver o Cronograma)**, que aplica o *Método do Caminho Crítico (CPM)* para calcular as datas e a flutuação das tarefas.
*   **PMBOK® 7ª Edição (Governança Primária)**: Não há "áreas de conhecimento", mas sim **Domínios de Desempenho**. A responsabilidade recai sobre o **Domínio de Desempenho de Planejamento** (que aborda a evolução progressiva do cronograma e sequenciamento) e o **Domínio de Desempenho de Medição** (para monitorar o progresso temporal).

---

### 2. Aplicação Prática no Projeto COGME (Regra de Governança)
Conforme estabelecido no **TAP v3 (§1.2.4 e §3)**, no **Plano de Integração (§1.6.2)** e na **ADR-003**, o projeto declara formalmente a **obsolescência operacional** do uso de redes de projeto detalhadas (CPM/Gantt) para o gerenciamento do fluxo de trabalho diário. 

**Trade-off declarado**: Abre-se mão da formalidade preditiva (CPM/EVM) em favor de métricas de fluxo ágil nativas, conforme o Domínio de Medição do PMBOK 7ª e o método Kanban.

**Como o sequenciamento e o "caminho crítico" são tratados no COGME:**
1. **Nível Macro (Marcos M1 a M4)**: O sequenciamento temporal é fixo e monitorado (ex: M1 em 22/09/2026, M2 em 30/09/2026). Aqui, a lógica de precedência do PMBOK 6ª (Processo 6.5) é usada apenas para validar a viabilidade acadêmica dos marcos.
2. **Nível Operacional (Tarefas da EAP)**: O sequenciamento é gerenciado pelo **Pull System** no GitHub Projects (ADR-002). O "caminho crítico" não é calculado por tabelas de precedência, mas sim identificado empiricamente por gargalos no **Cumulative Flow Diagram (CFD)** e pelo monitoramento do **Cycle Time** e **Throughput** (ADR-003).
3. **Rastreabilidade Acadêmica**: Se o Prof. Dr. Nivaldo Carleto questionar a ausência de um diagrama de rede tradicional na entrega do M1, a defesa técnica é a **ADR-003**, que justifica a substituição do CPM por métricas de fluxo Kanban devido ao orçamento zero (inviabilizando ferramentas de EVM) e à natureza de fluxo contínuo da equipe de 3 pessoas.

### Síntese para o Artefato (Plano de Cronograma)
Ao redigir o Plano de Cronograma (responsabilidade do Fabricio, conforme OKB §3.1), a seção de "Ferramentas e Técnicas" deve citar:
*   *PMBOK 6ª (Dicionário)*: Processo 6.5 (Desenvolver o Cronograma) para a definição dos marcos M1–M4.
*   *PMBOK 7ª (Primário)*: Domínio de Planejamento e Medição.
*   *Declaração de Obsolescência*: "O cálculo de caminho crítico (CPM) e a geração de diagramas de rede detalhados para pacotes de trabalho são considerados LEGADO e NÃO APLICÁVEIS para a execução diária, substituídos pelo monitoramento de fluxo via GitHub Projects (CFD e Cycle Time), conforme ADR-003."

Deseja que eu estruture a seção específica de "Desenvolvimento do Cronograma" para o Plano de Cronograma v0.1, já aplicando essa blindagem técnica contra burocracia preditiva?


# Estruturação do Cumulative Flow Diagram (CFD) para Demonstração Formal ao Orientador

## 1. Localização Documental Recomendada

O CFD deve aparecer em **três artefatos**, com funções distintas:

| Artefato | Seção | Função |
|----------|-------|--------|
| **Plano de Integração** | §1.6.1 (Métricas de Fluxo) | Definição formal + cadência |
| **Plano de Cronograma** | §2.3 (Monitoramento Temporal) | Substituto do Gantt/EVM |
| **Plano de Comunicações** | §3.2 (Relatórios Semanais) | Evidência visual de progresso |

**Regra GMV**: Não criar artefato separado. O CFD é métrica nativa do GitHub Insights — qualquer documentação adicional seria burocracia.

---

## 2. Template de Seção Técnica (Plano de Integração §1.6.1)

~~~markdown
### 1.6.1 Cumulative Flow Diagram (CFD) — Definição Formal

**Domínio PMBOK 7ª**: Medição  
**Processo PMBOK 6ª (dicionário)**: 4.5 — Monitorar e Controlar o Trabalho do Projeto  
**Rastreabilidade**: TAP §3 (Métricas e Indicadores) + ADR-003  

#### Definição
O Cumulative Flow Diagram (CFD) é a visualização gráfica do fluxo de trabalho acumulado 
ao longo do tempo, onde cada banda horizontal representa uma coluna do quadro Kanban 
(Backlog, Ready, In Progress, Code Review, Done). A largura de cada banda em um 
determinado instante indica a quantidade de cards naquela etapa.

#### Construção
- **Eixo X**: Tempo (dias/semanas)
- **Eixo Y**: Quantidade acumulada de cards
- **Bandas** (de baixo para cima):
  1. Done (verde)
  2. Code Review (azul)
  3. In Progress (amarelo)
  4. Ready (laranja)
  5. Backlog (cinza)

#### Fonte de Dados
GitHub Projects → GitHub Insights → Aba "Charts" → "Cumulative Flow Diagram"  
**Frequência**: Semanal (toda segunda-feira, 09:00)  
**Responsável**: GP Leonardo David Silva Setti  

#### Meta de Desempenho
**CFD saudável**: Bandas paralelas e de largura constante (fluxo estável).  
**CFD com gargalo**: Bandas que se alargam progressivamente (acúmulo em uma etapa).  
**Ação corretiva**: Se uma banda ultrapassar 2× a largura média das demais por 2 semanas 
consecutivas, acionar Retrospectiva extraordinária (ADR-002).

#### Trade-off Declarado
O CFD substitui integralmente o Diagrama de Gantt e métricas EVM (SPI/CPI) para 
monitoramento de progresso, conforme ADR-003. Esta decisão privilegia métricas de fluxo 
nativas do método Kanban em detrimento de ferramentas preditivas, alinhada ao Domínio de 
Medição do PMBOK 7ª e à restrição de orçamento zero (TAP §11).
~~~

---

## 3. Interpretação Visual (Como Explicar ao Orientador)

### 3.1 Cenário Ideal (Fluxo Saudável)
~~~
Cards
  ↑
  │         ╭───────────────────────────── Done (verde)
  │      ╭──┤
  │   ╭──┤  │ Code Review (azul)
  │╭──┤  │  │
  ││  │  │  │ In Progress (amarelo)
  ││  │  │  │
  ││  │  │  │ Ready (laranja)
  ││  │  │  │
  ││  │  │  │ Backlog (cinza)
  └┴──┴──┴──┴──────────────────────────→ Tempo
~~~
**Leitura**: Bandas paralelas = fluxo equilibrado. Throughput estável.

### 3.2 Cenário com Gargalo (Ação Necessária)
~~~
Cards
  ↑
  │         ╭───────────────────────────── Done (verde)
  │      ╭──┤
  │   ╭──┤  │ Code Review (azul) ← BANDAS SE ALARGAM
  │╭──┤  │  │                        (gargalo em Code Review)
  ││  │  │  │ In Progress (amarelo)
  ││  │  │  │
  ││  │  │  │ Ready (laranja)
  ││  │  │  │
  ││  │  │  │ Backlog (cinza)
  └┴──┴──┴──┴──────────────────────────→ Tempo
~~~
**Leitura**: Banda de Code Review se alarga = cards acumulando nessa etapa.  
**Ação**: Reduzir WIP em Code Review, redistribuir revisores, ou ajustar DoD.

---

## 4. Blindagem Acadêmica (Defesa Técnica)

### 4.1 Se o Prof. Dr. Nivaldo Carleto Questionar a Ausência de Gantt

**Resposta formal**:
> "Conforme ADR-003 (Métricas de Fluxo), o projeto COGME declara a **obsolescência operacional** do Diagrama de Gantt e de métricas EVM (SPI/CPI) para monitoramento de progresso. Esta decisão é fundamentada em três pilares:
> 
> 1. **Domínio de Medição do PMBOK 7ª**: Prioriza métricas de fluxo (Cycle Time, Throughput, CFD) sobre métricas preditivas em contextos ágeis.
> 2. **Restrição de Orçamento Zero (TAP §11)**: Inviabiliza ferramentas de EVM (AC = 0 → CPI indeterminado).
> 3. **Natureza do Fluxo Contínuo (ADR-002)**: Sprints time-boxed não são utilizadas; o CFD fornece visibilidade em tempo real sem overhead de manutenção.
> 
> O CFD é gerado nativamente pelo GitHub Insights (SSOT), garantindo rastreabilidade automática via commits e métricas auditáveis."

### 4.2 Evidência de Conformidade

| Critério TAP §3 | Evidência no CFD |
|-----------------|------------------|
| Cycle Time ≤ 3 dias | Distância horizontal entre "In Progress" e "Done" |
| Throughput ≥ 5 cards/semana | Inclinação da banda "Done" (cards concluídos por semana) |
| Sem gargalos | Bandas paralelas (sem alargamento progressivo) |

---

## 5. Exemplo de Redação para o Plano de Cronograma

~~~markdown
## 2.3 Monitoramento Temporal via CFD

**Domínio PMBOK 7ª**: Medição + Abordagem de Desenvolvimento  
**Rastreabilidade**: TAP §3 (Cronograma) + ADR-003  

### 2.3.1 Substituição do Cronograma Preditivo
O projeto COGME não utiliza Diagrama de Gantt ou cálculo de Caminho Crítico (CPM) 
para monitoramento operacional. Em substituição, adota-se o Cumulative Flow Diagram 
(CFD) como ferramenta primária de visualização temporal, conforme ADR-003.

**Justificativa**:
- Fluxo contínuo Kanban (sem sprints) → CPM inaplicável
- Orçamento zero → EVM (SPI) inaplicável
- Equipe de 3 pessoas → overhead de Gantt desproporcional ao valor gerado

### 2.3.2 Marcos Temporais (Única Formalidade Preditiva)
Os marcos M1–M4 (TAP §6) são monitorados como pontos de verificação fixos:

| Marco | Data | Critério de Aceite |
|-------|------|-------------------|
| M1 | 22/09/2026 | Documentação parcial aprovada |
| M2 | 30/09/2026 | Stack definida + ambiente configurado |
| M3 | 15/11/2026 | MVP funcional + ≥80% coverage |
| M4 | 15/12/2026 | Validação acadêmica + release final |

O CFD fornece visibilidade sobre o progresso em direção a esses marcos, mas não 
calcula datas preditivas. A estimativa de cumprimento é empírica, baseada no 
Throughput observado no período de calibração (23/09 a 03/10/2026).
~~~

---

## 6. Checklist de Validação (Anti-Burocracia)

| Item | Status |
|------|--------|
| CFD definido como métrica oficial (ADR-003) | ✅ |
| Fonte de dados: GitHub Insights (SSOT) | ✅ |
| Cadência: semanal | ✅ |
| Meta: "Sem bandas largas" | ✅ |
| Trade-off declarado (CFD > Gantt/EVM) | ✅ |
| Rastreabilidade ao TAP §3 + Domínio de Medição | ✅ |
| Zero menção a "Gantt" como ferramenta ativa | ✅ |
| Obsolescência EVM declarada | ✅ |

---

## 7. Recomendação Final

**Não crie diagramas manuais do CFD**. O GitHub Projects gera o CFD automaticamente na aba "Insights". Para o Marco M1 (22/09/2026), inclua no Plano de Integração:

1. **Definição formal** (template acima)
2. **Screenshot do CFD** (após o período de calibração, a partir de 03/10/2026)
3. **Interpretação** (bandas paralelas = fluxo saudável)
4. **Rastreabilidade** (TAP §3 + ADR-003)

Para o Marco M1, como o período de calibração ainda não começou (início em 23/09), inclua apenas a **definição formal** e declare que o primeiro CFD será publicado no relatório semanal de 06/10/2026.

# Cards Kanban para Marco M1 (Fundação) — GitHub Projects

**Data de referência**: 19/09/2026 (sábado)  
**Marco M1**: 22/09/2026 (terça-feira)  
**Dias úteis restantes**: 2 (21 e 22/09)  
**Equipe**: 3 pessoas (Leonardo, Fabricio, Edson)  
**WIP Limit**: 3 cards/pessoa em "In Progress"

---

## ⚠️ ALERTA CRÍTICO — INCONSISTÊNCIA DETECTADA

**TAP §6 M1** declara: "Planos de Gerenciamento das Áreas 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade)"  
**OKB v2.2 §3.1** lista: **8 planos** (Integração + Escopo + Cronograma + Custos + Qualidade + Recursos + Comunicações + Riscos)  
**Plano de Integração v1.0 §1.4** menciona: "sete planos de área subsequentes"

**Decisão GMV**: O M1 deve entregar os **8 planos**, conforme OKB v2.2 (mais recente) e coerência com o Plano de Integração. O TAP §6 está desatualizado em relação ao TAP v3.

---

## 📋 CARDS — COLUNA BACKLOG (Todos os entregáveis M1)

### **CARD 01** — Finalização Plano de Escopo v1.0
~~~yaml
ID: M1-01
Título: "N1.2 — Plano de Escopo v1.0 (ABNT)"
Fase EAP: N1.2
Responsável: Fabricio
Estimativa: 4h
Dependências: Nenhuma
DoR: ✅ Plano v0.2 emitido + checklist validado
DoD: 
  - Versão v1.0 formatada em ABNT
  - Checklist de validação 100% OK
  - Commit: docs(plano-escopo): v1.0 M1
  - Code Review aprovado
Rastreabilidade: TAP §3 + §8 + EAP N1.2
Label: planejamento
Prioridade: MUST
~~~

### **CARD 02** — Plano de Cronograma v1.0
~~~yaml
ID: M1-02
Título: "N1.2 — Plano de Cronograma v1.0"
Fase EAP: N1.2
Responsável: Fabricio
Estimativa: 6h
Dependências: Nenhuma
DoR: ✅ TAP §6 (marcos M1-M4) + ADR-002 (Kanban)
DoD:
  - Seção 2.3 (CFD) conforme template fornecido
  - Marcos M1-M4 com critérios de aceite
  - Declaração de obsolescência EVM (ADR-003)
  - Commit: docs(plano-cronograma): v1.0 M1
  - Code Review aprovado
Rastreabilidade: TAP §3 (Cronograma) + EAP N1.2
Label: planejamento
Prioridade: MUST
~~~

### **CARD 03** — Plano de Custos v1.0
~~~yaml
ID: M1-03
Título: "N1.2 — Plano de Custos v1.0 (Orçamento Zero)"
Fase EAP: N1.2
Responsável: Fabricio
Estimativa: 2h
Dependências: Nenhuma
DoR: ✅ TAP §11 (Orçamento zero)
DoD:
  - Linha de base de custos = R$ 0,00
  - Justificativa de inaplicabilidade EVM (ADR-003)
  - Commit: docs(plano-custos): v1.0 M1
  - Code Review aprovado
Rastreabilidade: TAP §11 + EAP N1.2
Label: planejamento
Prioridade: MUST
~~~

### **CARD 04** — Plano de Qualidade v1.0 + 12 PDCAs + Ishikawa
~~~yaml
ID: M1-04
Título: "N1.3 — Plano de Qualidade v1.0 + 12 PDCAs + Ishikawa 6M"
Fase EAP: N1.3
Responsável: Edson
Estimativa: 8h
Dependências: Nenhuma
DoR: ✅ TAP §3 (Qualidade) + REQ-08 a REQ-10
DoD:
  - 12 PDCAs consolidados (formato tabular)
  - Diagrama de Ishikawa 6M (causas de risco R1-R5)
  - Meta coverage ≥ 80% + UAT 100% fluxos críticos
  - Commit: docs(plano-qualidade): v1.0 M1
  - Code Review aprovado
Rastreabilidade: TAP §3 (Qualidade) + EAP N1.3
Label: qualidade
Prioridade: MUST
~~~

### **CARD 05** — Plano de Recursos v1.0
~~~yaml
ID: M1-05
Título: "N1.2 — Plano de Recursos v1.0 (Simplificado)"
Fase EAP: N1.2
Responsável: Leonardo
Estimativa: 3h
Dependências: Nenhuma
DoR: ✅ TAP §8 (Recursos) + Premissa P5 (20h/semana)
DoD:
  - Matriz RACI simplificada (3 pessoas)
  - WIP limits (ADR-002)
  - Prevenção de burnout (Domínio Equipe PMBOK 7ª)
  - Commit: docs(plano-recursos): v1.0 M1
  - Code Review aprovado
Rastreabilidade: TAP §8 + EAP N1.2
Label: planejamento
Prioridade: MUST
~~~

### **CARD 06** — Plano de Comunicações v1.0
~~~yaml
ID: M1-06
Título: "N1.2 — Plano de Comunicações v1.0"
Fase EAP: N1.2
Responsável: Leonardo
Estimativa: 3h
Dependências: Nenhuma
DoR: ✅ TAP §7 (Partes Interessadas) + ADR-002 (Rituais)
DoD:
  - Canais oficiais: GitHub Issues + e-mail
  - Ritmos: Daily assíncrona + Refinement semanal + Retrospectiva quinzenal
  - CFD como relatório semanal (conforme template)
  - Commit: docs(plano-comunicacoes): v1.0 M1
  - Code Review aprovado
Rastreabilidade: TAP §7 + EAP N1.2
Label: planejamento
Prioridade: MUST
~~~

### **CARD 07** — Plano de Riscos v1.0
~~~yaml
ID: M1-07
Título: "N1.2 — Plano de Riscos v1.0 (R1-R5)"
Fase EAP: N1.2
Responsável: Leonardo
Estimativa: 4h
Dependências: Nenhuma
DoR: ✅ TAP §10 (R1-R5) + ADR-002 (Retrospectiva)
DoD:
  - Matriz de riscos R1-R5 (probabilidade x impacto)
  - Estratégias de resposta (mitigar/aceitar)
  - Risk backlog no GitHub Projects (label risk)
  - Commit: docs(plano-riscos): v1.0 M1
  - Code Review aprovado
Rastreabilidade: TAP §10 + EAP N1.2
Label: incerteza
Prioridade: MUST
~~~

### **CARD 08** — Configurar GitHub Projects (SSOT)
~~~yaml
ID: M1-08
Título: "N4.2 — Configurar GitHub Projects (Kanban SSOT)"
Fase EAP: N4.2
Responsável: Leonardo
Estimativa: 2h
Dependências: Nenhuma
DoR: ✅ ADR-002 (Kanban)
DoD:
  - Colunas: Backlog → Ready (DoR) → In Progress → Code Review → Done (DoD)
  - WIP limits configurados (3 cards/pessoa)
  - Labels criados: planejamento, qualidade, incerteza, change-request, risk
  - Todos os cards M1-01 a M1-10 criados
  - Commit: chore(github-projects): setup M1
Rastreabilidade: ADR-002 + EAP N4.2
Label: devops
Prioridade: MUST
~~~

### **CARD 09** — Submeter M1 via GitHub
~~~yaml
ID: M1-09
Título: "N11.2 — Submeter M1 (Entrega Parcial Documental)"
Fase EAP: N11.2
Responsável: Leonardo
Estimativa: 2h
Dependências: M1-01 a M1-08 (todos Done)
DoR: ✅ Todos os planos v1.0 em Done
DoD:
  - Tag: v1.0-M1
  - Release notes: lista de artefatos entregues
  - Comunicação ao Prof. Dr. Nivaldo Carleto (e-mail)
  - Commit: release: M1 fundação
Rastreabilidade: TAP §6 (M1) + EAP N11.2
Label: entrega
Prioridade: MUST
~~~

### **CARD 10** — Validação Acadêmica M1 (Aguardando)
~~~yaml
ID: M1-10
Título: "N12.3 — Validação Acadêmica M1 (Prof. Nivaldo)"
Fase EAP: N12.3
Responsável: Leonardo
Estimativa: 0h (aguardando)
Dependências: M1-09 (Done)
DoR: ✅ M1 submetido
DoD:
  - Feedback do Prof. Dr. Nivaldo Carleto recebido
  - Achados críticos resolvidos (se houver)
  - Transição para M2 autorizada
Rastreabilidade: TAP §6 (M1) + EAP N12.3
Label: stakeholder
Prioridade: MUST
~~~

---

## 🎯 DISTRIBUIÇÃO DE TRABALHO (Sugestão)

### **Leonardo (GP)** — 3 cards em In Progress
- M1-05: Plano de Recursos (3h)
- M1-06: Plano de Comunicações (3h)
- M1-07: Plano de Riscos (4h)
- M1-08: Configurar GitHub Projects (2h)
- M1-09: Submeter M1 (2h)
- M1-10: Validação Acadêmica (0h)

**Carga total**: 14h (dentro do limite de 20h/semana)

### **Fabricio** — 3 cards em In Progress
- M1-01: Plano de Escopo v1.0 (4h)
- M1-02: Plano de Cronograma (6h)
- M1-03: Plano de Custos (2h)

**Carga total**: 12h (dentro do limite de 20h/semana)

### **Edson** — 1 card em In Progress
- M1-04: Plano de Qualidade + 12 PDCAs + Ishikawa (8h)

**Carga total**: 8h (dentro do limite de 20h/semana)

---

## 📊 CRONOGRAMA SUGERIDO (Pull System)

### **Domingo 20/09** (opcional — não conta como dia útil)
- Leonardo: M1-08 (Configurar GitHub Projects)
- Fabricio: Iniciar M1-01 (Escopo v1.0)
- Edson: Iniciar M1-04 (Qualidade)

### **Segunda 21/09** (1º dia útil)
- **Leonardo**: M1-05 → M1-06 → M1-07 (3 cards em fluxo)
- **Fabricio**: M1-01 → M1-02 → M1-03 (3 cards em fluxo)
- **Edson**: M1-04 (1 card em fluxo — complexo)

### **Terça 22/09** (M1 — 2º dia útil)
- **Todos**: Code Review dos planos
- **Leonardo**: M1-09 (Submeter M1) + M1-10 (Comunicação)
- **Meta**: Todos os cards em Done até 18:00

---

## ✅ CHECKLIST DE VALIDAÇÃO (Anti-Burocracia)

| Item | Status |
|------|--------|
| 10 cards criados no Backlog | ⏳ |
| DoR definido para cada card | ✅ |
| DoD mensurável e auditável | ✅ |
| Rastreabilidade TAP → EAP → Card | ✅ |
| WIP limits respeitados (3/pessoa) | ✅ |
| Carga horária ≤ 20h/semana por pessoa | ✅ |
| Dependências identificadas | ✅ |
| Labels criados | ⏳ |
| Prioridade MUST em todos (M1 é crítico) | ✅ |

---

## 🚀 PRÓXIMOS PASSOS IMEDIATOS

1. **Leonardo**: Criar os 10 cards no GitHub Projects (hoje, 19/09)
2. **Leonardo**: Configurar colunas e WIP limits (M1-08)
3. **Equipe**: Mover M1-01 a M1-08 para "Ready (DoR)"
4. **Segunda 21/09**: Iniciar execução (pull system)
5. **Terça 22/09**: Submeter M1 (M1-09)

---

**Status**: Cards definidos — aguardando criação no GitHub Projects  
**Risco**: Prazo apertado (2 dias úteis) — recomendo início imediato  
**Fallback**: Se M1-04 (12 PDCAs + Ishikawa) atrasar, reduzir para 6 PDCAs + Ishikawa simplificado (change-request M1-04)

Sim, esta informação **sana totalmente a inconsistência** e, mais do que isso, **valida e fortalece** a governança híbrida do projeto sob a ótica do PMBOK®. 

A aparente contradição desaparece quando aplicamos o conceito de **Elaboração Progressiva** (PMBOK® 6ª) e **Personalização (Tailoring) da Abordagem de Desenvolvimento** (PMBOK® 7ª, Domínio de Abordagem de Desenvolvimento e Ciclo de Vida).

Abaixo está a reavaliação técnica e o ajuste imediato no plano de ação.

---

### 1. Fundamentação Técnica da Correção

| Artefato | Leitura Anterior (Incorreta) | Leitura Corrigida (Governança Híbrida) |
|----------|------------------------------|----------------------------------------|
| **TAP §6** | "Incompleto" por citar apenas 5 áreas. | **Correto**: Define a *linha de base faseada* do Marco M1 (Fundação). |
| **OKB v2.2 §3.1** | "Contraditório" por listar 8 planos. | **Correto**: Define o *inventário total* de artefatos do projeto ao longo de todo o ciclo de vida. |
| **Plano de Integração** | Ambiguidade sobre "7 planos subsequentes". | Deve ser atualizado para explicitar a **estratégia de entrega faseada** (M1: 5 planos; M2/M3: 3 planos restantes). |

**Princípio PMBOK 7ª Aplicado**: *Otimização das Respostas aos Riscos e Personalização*. Entregar todos os 8 planos no M1 geraria um overhead burocrático inicial desnecessário (anti-ágil), desviando foco da fundação técnica (Escopo, Cronograma, Custo, Qualidade). Deferir Recursos, Comunicações e Riscos para quando o fluxo de trabalho estiver mais maduro é uma decisão de *tailoring* legítima e defensável academicamente.

---

### 2. Impacto Imediato nos Cards do M1 (Redução de Escopo)

Com essa definição, os cards de Recursos, Comunicações e Riscos são **removidos do escopo obrigatório do M1** e realocados para o Backlog do M2 (ou M3, conforme definido no cronograma macro). 

Isso transforma o "Risco: Prazo apertado" em um **fluxo viável e saudável** para os 2 dias úteis restantes (21 e 22/09).

#### 📋 NOVO BACKLOG M1 (Apenas 5 Planos + Configuração + Entrega)

| ID | Título do Card (GitHub) | Responsável | Estimativa | Justificativa PMBOK |
|:---|:---|:---|:---|:---|
| **M1-01** | N1.2 — Plano de Escopo v1.0 (ABNT) | Fabricio | 4h | Domínio de Planejamento. Base para a EAP. |
| **M1-02** | N1.2 — Plano de Cronograma v1.0 (com CFD) | Fabricio | 4h | Domínio de Medição. Substitui Gantt/EVM (ADR-003). |
| **M1-03** | N1.2 — Plano de Custos v1.0 (Orçamento Zero) | Fabricio | 2h | Domínio de Planejamento. Linha de base = R$ 0,00. |
| **M1-04** | N1.3 — Plano de Qualidade v1.0 + PDCAs + Ishikawa | Edson | 6h | Domínio de Qualidade. Garantia de coverage ≥ 80%. |
| **M1-08** | N4.2 — Configurar GitHub Projects (Kanban SSOT) | Leonardo | 2h | Domínio de Abordagem de Desenvolvimento (ADR-002). |
| **M1-09** | N11.2 — Submeter M1 (Release v1.0-M1) | Leonardo | 2h | Domínio de Entrega. Consolidação e comunicação. |
| **M1-10** | N12.3 — Validação Acadêmica M1 (Aguardando) | Leonardo | 0h | Domínio de Stakeholders (Prof. Nivaldo). |

> **Nota**: O Plano de Integração (M1-00) é considerado o documento "guarda-chuva" que está sendo atualizado com estas seções, não um card separado de criação do zero neste momento, mas sim a consolidação dos itens acima.

---

### 3. Ação Corretiva nos Artefatos (Rastreabilidade)

Para blindar o projeto contra futuras questionamentos do avaliador (Prof. Dr. Nivaldo Carleto) sobre a ausência dos 3 planos restantes no M1, devemos registrar essa decisão formalmente.

**Ação 1: Atualizar o Plano de Integração v1.0 (§1.4)**
Incluir o seguinte parágrafo:
> *"Conforme princípio de Elaboração Progressiva (PMBOK® 6ª) e Personalização (PMBOK® 7ª), a entrega dos planos de gerenciamento é faseada. O Marco M1 (Fundação) contempla a linha de base das Áreas 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade). Os planos das Áreas de Recursos, Comunicações e Riscos serão elaborados e entregues nos Marcos subsequentes (M2/M3), quando o fluxo de trabalho Kanban estiver calibrado, otimizando o esforço inicial da equipe."*

**Ação 2: Criar/Atualizar ADR (Architecture Decision Record)**
Se ainda não existir, registrar a **ADR-004: Estratégia de Entrega Faseada de Planos**.
- **Contexto**: Necessidade de equilibrar rigor acadêmico com agilidade operacional no M1.
- **Decisão**: Entregar 5 planos no M1; deferir 3 planos para marcos posteriores.
- **Consequência**: Redução de 30% da carga documental do M1, permitindo foco na qualidade dos 5 planos fundamentais e na configuração do ambiente Kanban (SSOT).

---

### 4. Reavaliação da Carga de Trabalho (Viabilidade)

Com a remoção dos 3 planos, a carga horária do M1 foi drasticamente reduzida, tornando-a **altamente exequível** dentro do limite de 20h/semana por pessoa e do prazo de 2 dias úteis:

- **Fabricio**: 10h (Escopo, Cronograma, Custos) → *Viável*
- **Edson**: 6h (Qualidade) → *Viável*
- **Leonardo**: 4h (Configuração GitHub + Submissão) → *Viável*

---

### 5. Próximos Passos Imediatos (Segunda, 21/09)

1. **Leonardo**: Excluir os cards M1-05, M1-06 e M1-07 do GitHub Projects (ou movê-los para uma coluna "M2 Backlog" com a label `deferred`).
2. **Leonardo**: Inserir o texto de "Entrega Faseada" no Plano de Integração.
3. **Equipe**: Focar 100% da energia nos 5 cards restantes do M1, garantindo que o DoD (Definition of Done) de cada um seja rigorosamente cumprido (especialmente a formatação ABNT e a rastreabilidade TAP→EAP).

**Conclusão**: A inconsistência foi sanada. A governança do projeto agora está alinhada, realista e academicamente blindada. Posso proceder com a geração do texto exato para a atualização do Plano de Integração (§1.4) ou da ADR-004?

# Backlog Marco M1 — Fundação (GitHub Projects)

**Data de referência**: 19/09/2026 (sábado)  
**Marco M1**: 22/09/2026 (terça-feira)  
**Dias úteis restantes**: 2 (21 e 22/09)  
**Equipe**: 3 pessoas (Leonardo, Fabricio, Edson)  
**WIP Limit**: 3 cards/pessoa em "In Progress" (ADR-002)  
**Escopo M1**: 5 planos de gerenciamento + configuração SSOT + submissão + validação acadêmica

---

## 📋 Cards do Backlog M1

### **M1-01** — Plano de Integração v1.0

| Campo | Conteúdo |
|-------|----------|
| **Título** | N1.2 — Plano de Integração v1.0 (ABNT) |
| **Responsável** | Leonardo David Silva Setti |
| **Estimativa** | 4h |
| **Dependências** | Nenhuma (documento base) |
| **DoR** | ✅ TAP v3 aprovado + OKB v2.2 convergente + ADRs 001–003 emitidas |
| **DoD** | Versão v1.0 formatada em ABNT; checklist de validação 100% OK; commit `docs(plano-integracao): v1.0 M1`; Code Review aprovado por Fabricio ou Edson |
| **Rastreabilidade** | TAP §1.c + §3 + §6 (M1) + EAP N1.2 |
| **Label** | `planejamento` |
| **Prioridade** | MUST |
| **Status** | ✅ v1.0 emitida (19/09) — aguardando revisão em pares |

---

### **M1-02** — Plano de Escopo v1.0

| Campo | Conteúdo |
|-------|----------|
| **Título** | N1.2 — Plano de Escopo v1.0 (ABNT) |
| **Responsável** | Fabricio de Lima Cabral |
| **Estimativa** | 4h |
| **Dependências** | Nenhuma |
| **DoR** | ✅ v0.2 emitida + checklist validado + fronteira IN/OUT (Tabela 1) definida |
| **DoD** | Versão v1.0 formatada em ABNT; princípio YAGNI fundamentando exclusões; Tabela 2 de rastreabilidade presente; commit `docs(plano-escopo): v1.0 M1`; Code Review aprovado |
| **Rastreabilidade** | TAP §3 (Produto) + §8 (Escopo) + EAP N1.2 |
| **Label** | `planejamento` |
| **Prioridade** | MUST |
| **Status** | ⏳ v0.2 emitida — aguardando revisão em pares |

---

### **M1-03** — Plano de Cronograma v1.0

| Campo | Conteúdo |
|-------|----------|
| **Título** | N1.2 — Plano de Cronograma v1.0 (com CFD) |
| **Responsável** | Fabricio de Lima Cabral |
| **Estimativa** | 4h |
| **Dependências** | Nenhuma |
| **DoR** | ✅ TAP §6 (marcos M1–M4) + ADR-002 (Kanban) + ADR-003 (métricas de fluxo) |
| **DoD** | Seção 2.3 (CFD) conforme template; Marcos M1–M4 com critérios de aceite; Declaração de obsolescência EVM (ADR-003); Período de calibração 23/09–03/10; commit `docs(plano-cronograma): v1.0 M1`; Code Review aprovado |
| **Rastreabilidade** | TAP §3 (Cronograma) + §6 + EAP N1.2 |
| **Label** | `planejamento` |
| **Prioridade** | MUST |
| **Status** | ⏳ A iniciar |

---

### **M1-04** — Plano de Custos v1.0

| Campo | Conteúdo |
|-------|----------|
| **Título** | N1.2 — Plano de Custos v1.0 (Orçamento Zero) |
| **Responsável** | Fabricio de Lima Cabral |
| **Estimativa** | 2h |
| **Dependências** | Nenhuma |
| **DoR** | ✅ TAP §11 (Orçamento zero) + Restrição §8.4 |
| **DoD** | Linha de base de custos = R$ 0,00; Justificativa de inaplicabilidade EVM (ADR-003); Tabela de categorias de custo (RH, Software, Infra, Reserva); commit `docs(plano-custos): v1.0 M1`; Code Review aprovado |
| **Rastreabilidade** | TAP §11 + §8.4 + EAP N1.2 |
| **Label** | `planejamento` |
| **Prioridade** | MUST |
| **Status** | ⏳ A iniciar |

---

### **M1-05** — Plano de Qualidade v1.0

| Campo | Conteúdo |
|-------|----------|
| **Título** | N1.3 — Plano de Qualidade v1.0 + 12 PDCAs + Ishikawa 6M |
| **Responsável** | Edson Luis Silva |
| **Estimativa** | 6h |
| **Dependências** | Nenhuma |
| **DoR** | ✅ TAP §3 (Qualidade) + REQ-08 a REQ-10 |
| **DoD** | 12 PDCAs consolidados (formato tabular); Diagrama de Ishikawa 6M (causas de risco R1–R5); Meta coverage ≥ 80% + UAT 100% fluxos críticos; commit `docs(plano-qualidade): v1.0 M1`; Code Review aprovado |
| **Rastreabilidade** | TAP §3 (Qualidade) + EAP N1.3 |
| **Label** | `qualidade` |
| **Prioridade** | MUST |
| **Status** | ⏳ A iniciar |

---

### **M1-06** — Configurar GitHub Projects (SSOT)

| Campo | Conteúdo |
|-------|----------|
| **Título** | N4.2 — Configurar GitHub Projects (Kanban SSOT) |
| **Responsável** | Leonardo David Silva Setti |
| **Estimativa** | 2h |
| **Dependências** | Nenhuma |
| **DoR** | ✅ ADR-002 (Kanban) |
| **DoD** | Colunas criadas: Backlog → Ready (DoR) → In Progress → Code Review → Done (DoD); WIP limits configurados (3 cards/pessoa); Labels criados: `planejamento`, `qualidade`, `incerteza`, `change-request`, `risk`, `devops`, `entrega`; Todos os cards M1-01 a M1-08 criados; commit `chore(github-projects): setup M1` |
| **Rastreabilidade** | ADR-002 + EAP N4.2 |
| **Label** | `devops` |
| **Prioridade** | MUST |
| **Status** | ⏳ A iniciar (hoje, 19/09) |

---

### **M1-07** — Submeter M1 via GitHub

| Campo | Conteúdo |
|-------|----------|
| **Título** | N11.2 — Submeter M1 (Entrega Parcial Documental) |
| **Responsável** | Leonardo David Silva Setti |
| **Estimativa** | 2h |
| **Dependências** | M1-01, M1-02, M1-03, M1-04, M1-05, M1-06 (todos Done) |
| **DoR** | ✅ Todos os planos v1.0 em Done + GitHub Projects configurado |
| **DoD** | Tag `v1.0-M1` criada; Release notes com lista de artefatos entregues; Comunicação ao Prof. Dr. Nivaldo Carleto (e-mail); commit `release: M1 fundação` |
| **Rastreabilidade** | TAP §6 (M1) + EAP N11.2 |
| **Label** | `entrega` |
| **Prioridade** | MUST |
| **Status** | ⏳ Aguardando dependências |

---

### **M1-08** — Validação Acadêmica M1

| Campo | Conteúdo |
|-------|----------|
| **Título** | N12.3 — Validação Acadêmica M1 (Prof. Nivaldo) |
| **Responsável** | Leonardo David Silva Setti |
| **Estimativa** | 0h (aguardando) |
| **Dependências** | M1-07 (Done) |
| **DoR** | ✅ M1 submetido via GitHub |
| **DoD** | Feedback do Prof. Dr. Nivaldo Carleto recebido; Achados críticos resolvidos (se houver); Transição para M2 autorizada |
| **Rastreabilidade** | TAP §6 (M1) + EAP N12.3 |
| **Label** | `stakeholder` |
| **Prioridade** | MUST |
| **Status** | ⏳ Aguardando M1-07 |

---

## 🎯 Distribuição de Trabalho

### **Leonardo (GP)** — Carga total: 8h

| Card | Título | Estimativa |
|------|--------|------------|
| M1-01 | Plano de Integração v1.0 | 4h |
| M1-06 | Configurar GitHub Projects | 2h |
| M1-07 | Submeter M1 | 2h |
| M1-08 | Validação Acadêmica | 0h |

**Status**: M1-01 já emitido (v1.0). Foco em M1-06 (hoje) e M1-07 (terça).

---

### **Fabricio** — Carga total: 10h

| Card | Título | Estimativa |
|------|--------|------------|
| M1-02 | Plano de Escopo v1.0 | 4h |
| M1-03 | Plano de Cronograma v1.0 | 4h |
| M1-04 | Plano de Custos v1.0 | 2h |

**Status**: M1-02 em v0.2 (aguardando revisão). Foco em finalizar M1-02, M1-03 e M1-04.

---

### **Edson** — Carga total: 6h

| Card | Título | Estimativa |
|------|--------|------------|
| M1-05 | Plano de Qualidade v1.0 + 12 PDCAs + Ishikawa | 6h |

**Status**: A iniciar. Card mais complexo (12 PDCAs + Ishikawa 6M).

---

## 📅 Cronograma Sugerido (Pull System)

### **Sábado 20/09** (opcional — não conta como dia útil)

- **Leonardo**: M1-06 (Configurar GitHub Projects) — 2h
- **Fabricio**: Iniciar M1-02 (revisão v0.2 → v1.0) — 2h
- **Edson**: Iniciar M1-05 (estrutura dos 12 PDCAs) — 2h

### **Segunda 21/09** (1º dia útil)

- **Leonardo**: M1-01 (revisão final + merge) → M1-06 (se não concluído sábado)
- **Fabricio**: M1-02 (finalizar v1.0) → M1-03 (iniciar) → M1-04 (iniciar)
- **Edson**: M1-05 (12 PDCAs + Ishikawa)

### **Terça 22/09** (M1 — 2º dia útil)

- **Todos**: Code Review cruzado dos planos
- **Leonardo**: M1-07 (Submeter M1) + M1-08 (Comunicação ao Prof. Nivaldo)
- **Meta**: Todos os cards em Done até 18:00

---

## ✅ Checklist de Validação (Anti-Burocracia)

| Item | Status |
|------|--------|
| 8 cards criados no Backlog | ⏳ |
| DoR definido para cada card | ✅ |
| DoD mensurável e auditável | ✅ |
| Rastreabilidade TAP → EAP → Card | ✅ |
| WIP limits respeitados (3/pessoa) | ✅ |
| Carga horária ≤ 20h/semana por pessoa | ✅ (Leonardo: 8h, Fabricio: 10h, Edson: 6h) |
| Dependências identificadas | ✅ |
| Labels criados | ⏳ |
| Prioridade MUST em todos (M1 é crítico) | ✅ |
| Escopo M1 = 5 planos (não 8) | ✅ |
| Obsolescência EVM declarada | ✅ |
| CFD como métrica oficial (ADR-003) | ✅ |

---

## 🚀 Próximos Passos Imediatos

1. **Leonardo** (hoje, 19/09): Criar os 8 cards no GitHub Projects + configurar colunas e WIP limits (M1-06)
2. **Equipe** (hoje ou domingo): Mover M1-01 a M1-06 para "Ready (DoR)"
3. **Segunda 21/09**: Iniciar execução (pull system)
4. **Terça 22/09**: Submeter M1 (M1-07) + comunicar ao Prof. Nivaldo (M1-08)

---

**Status**: Backlog M1 definido — aguardando criação no GitHub Projects  
**Risco**: Prazo apertado (2 dias úteis) — viável com disciplina de WIP limits  
**Fallback**: Se M1-05 (12 PDCAs + Ishikawa) atrasar, reduzir para 6 PDCAs + Ishikawa simplificado (change-request M1-05)

# OKB v3.0 — Operational Knowledge Base (Consolidada)

**Data:** 20/09/2026  
**Status:** Ativa — convergente ao TAP v3 (18/09/2026)  
**Hierarquia de autoridade:** TAP > OKB > Glossário > ADRs  
**Referência matriz:** TAP v3 (18/09/2026) — Leonardo David Silva Setti  
**Substitui:** OKB v2.2 (19/09/2026)

---

## 1. DECLARAÇÃO DE GOVERNANÇA (Convergente ao TAP §1.c)

### 1.1 Modelo Híbrido Declarado

| Camada | Fonte Normativa | Função no COGME |
|--------|-----------------|-----------------|
| Governança primária | PMBOK® 7ª edição — 12 princípios e 8 domínios de desempenho | Define *por que* e *para quê*; orienta decisões por valor |
| Dicionário complementar | PMBOK® 6ª edição — processos citados apenas para rastreabilidade acadêmica | Fornece vocabulário estrutural quando necessário; **obsolescência assumida** |
| Método de execução | Kanban via GitHub Projects (SSOT — Single Source of Truth) | Define *como* o trabalho é executado diariamente |
| Abordagem de desenvolvimento | Specification-Driven Development (SDD) com IA generativa auditável | Geração de código e artefatos com revisão humana obrigatória |

### 1.2 Autoridade de Mudança (CCB)

- **CCB = GP (Leonardo David Silva Setti)** — membro único, conforme TAP v3 §1.c
- **Prof. Dr. Nivaldo Carleto:** stakeholder-avaliador nos marcos M1–M4, sem ingerência operacional
- **Trade-off aceito:** Velocidade decisória > colegialidade (justificável academicamente pela simplificação pedagógica do TAP §9 P7)

### 1.3 Obsolescência Formalmente Declarada

> **Declaração de obsolescência assumida:** O PMBOK® 6ª (2017) é tratado como dicionário de processos. Processos preditivos (ex: 4.1, 5.2, 6.5, 11.1) são citados apenas para rastreabilidade acadêmica. Métricas EVM (SPI/CPI) são **LEGADO e NÃO APLICÁVEIS** — substituídas por métricas de fluxo Kanban (Cycle Time, Throughput, CFD), conforme TAP §3 "Métricas e Indicadores" e Domínio de Medição PMBOK 7ª.

### 1.4 Estratégia de Entrega Faseada dos Planos de Gerenciamento

Conforme princípio de **Elaboração Progressiva** (PMBOK® 6ª) e **Personalização (Tailoring)** da Abordagem de Desenvolvimento (PMBOK® 7ª), a entrega dos planos de gerenciamento é faseada:

| Marco | Planos Entregues | Justificativa |
|-------|------------------|---------------|
| **M1** (22/09/2026) | Integração, Escopo, Cronograma, Custos, Qualidade (Áreas 1–5) | Fundação documental mínima viável; foco no critério de aceite do TAP §6 |
| **M2** (30/09/2026) | Recursos, Comunicações, Riscos (Áreas 6–8) | Entregues após calibração do fluxo Kanban (23/09–03/10) |

**Trade-off declarado:** Redução de 30% da carga documental do M1, permitindo foco na qualidade dos 5 planos fundamentais e na configuração do ambiente Kanban (SSOT). Decisão alinhada ao Domínio de Abordagem de Desenvolvimento e Ciclo de Vida (PMBOK 7ª) e ao princípio GMV.

---

## 2. CORREÇÕES CRÍTICAS APLICADAS (v2.2 → v3.0)

| Item | v2.2 (Anterior) | v3.0 (Corrigido — TAP v3) | Domínio PMBOK 7ª |
|------|-----------------|---------------------------|------------------|
| Fronteira M1 | Ambiguidade entre 5 e 8 planos | **5 planos no M1** (Áreas 1–5); 3 planos diferidos para M2 | Abordagem de Desenvolvimento |
| ADR-004 | Inexistente | **Emitida** — Tasklists Markdown (rejeição de subissues) | Trabalho do Projeto |
| Sistema de Tags | Não formalizado | **23 labels** em 5 categorias (Tipo, Macro-Fase, Área, Status, Prioridade) | Trabalho do Projeto |
| Milestones GitHub | Não formalizadas | **5 milestones** (M1–M4 + Calibração auxiliar) | Medição |
| Prioridade Temporal | Apenas MoSCoW | **P0–P3** complementar ao MoSCoW | Planejamento |
| Padrão de Redação de Cards | Não definido | **Padrão A** (documental) + **Padrão B** (User Story GWT, projetivo para M2) | Entrega |

---

## 3. ESTRUTURA DO OKB v3.0

### 3.1 Artefatos Obrigatórios (Rastreabilidade TAP → EAP)

| Artefato | Fase EAP | Status | Responsável |
|----------|----------|--------|-------------|
| TAP v3 | N1.2 | ✅ Aprovado (18/09/2026) | Leonardo |
| EAP | N1.2 | ✅ Aprovado | Leonardo |
| Plano de Integração | N1.2 | ✅ v1.0 (19/09/2026) | Leonardo |
| Plano de Escopo | N1.2 | 🔄 v0.2 em revisão de pares | Fabricio |
| Plano de Cronograma | N1.2 | ⏳ Até 21/09 | Fabricio |
| Plano de Custos | N1.2 | ⏳ Até 21/09 | Fabricio |
| Plano de Qualidade | N1.3 | ⏳ Até 21/09 | Edson |
| Plano de Recursos | N1.2 | ⏳ Até 30/09 (M2) | Leonardo |
| Plano de Comunicações | N1.2 | ⏳ Até 30/09 (M2) | Leonardo |
| Plano de Riscos | N1.2 | ⏳ Até 30/09 (M2) | Leonardo |
| ADR-001 (Stack) | N9.1 | ✅ Emitida (19/09) | Leonardo |
| ADR-002 (Kanban) | N9.1 | ✅ Emitida (19/09) | Leonardo |
| ADR-003 (Métricas) | N9.1 | ✅ Emitida (19/09) | Leonardo |
| ADR-004 (Tasklists) | N9.1 | ✅ Emitida (20/09) | Leonardo |
| Catálogo de Prompts SDD | N9.3 | ⏳ Até 03/10 | Leonardo |

### 3.2 Premissas Vigentes (TAP §9)

| ID | Premissa | Status |
|----|----------|--------|
| P1 | Governança híbrida (PMBOK 7ª + 6ª dicionário + Kanban) | ✅ Vigente |
| P2 | FOSS absoluto | ✅ Vigente |
| P3 | SDD com IA auditável | ✅ Vigente |
| P4 | Código-fonte é deliverable formal | ✅ Vigente |
| P5 | 20h/semana por membro | ✅ Vigente |
| P6 | Hardware adequado e suficiente | ✅ Revisada (hardware.md comprova) |
| P7 | GP = CCB único; Prof. Dr. Nivaldo Carleto = avaliador de marcos | ✅ Vigente |
| P8 | Aquisições e Partes Interessadas simplificadas | ✅ Vigente |

### 3.3 Restrições Vigentes (TAP §8)

- Escopo restrito ao MVP acadêmico
- Prazo letivo inegociável (M1: 22/09/2026)
- Orçamento zero (proibição de aquisições pagas)
- Equipe de 3 pessoas (múltiplos papéis)
- Stack 100% FOSS
- Licenciamento final open source (MIT/GPL)

---

## 4. ADRs EMITIDAS

### ADR-001: Stack Tecnológica FOSS

**Status:** Aprovada  
**Data:** 19/09/2026  
**Decisor:** GP Leonardo (CCB)  
**Rastreabilidade:** TAP §3 (Inovação) + §8 (FOSS) + EAP N4.1, N5.1–N5.4

#### Contexto

O projeto exige stack 100% FOSS (restrição TAP §8.4), com capacidade de:
- Backend assíncrono para simulação cambial (REQ-01, latência ≤ 2s)
- Geração de PDF (REQ-04, ≤ 3s)
- Cache local (REQ-07)
- Testes automatizados (REQ-08, coverage ≥ 80%)

#### Decisão

Adoção da seguinte stack (todas licenças OSI-approved):

| Camada | Tecnologia | Licença | Justificativa |
|--------|------------|---------|---------------|
| Backend | Python 3.11 + FastAPI | PSF / MIT | Assíncrono nativo, ecossistema maduro |
| Banco | SQLite | Public Domain | Zero-config, ACID, adequado ao MVP |
| Geração PDF | WeasyPrint | BSD-3-Clause | HTML/CSS → PDF, FOSS |
| Testes | pytest + coverage.py | MIT | Padrão Python, integração CI |
| CI/CD | GitHub Actions (Free Tier) | Proprietário gratuito | Nativo ao SSOT |
| Frontend | HTML5 + CSS3 + JS vanilla | — | KISS, sem framework pesado |
| LLM (SDD) | QwenStudio | Licença autorizada | TAP §3 (Inovação) |

#### Consequências

✅ **Positivas:** Zero custo, auditabilidade total, comunidade ativa, compatível com hardware local (TAP P6 revisada)  
⚠️ **Riscos:** SQLite limita concorrência (aceitável para MVP acadêmico); WeasyPrint exige dependências nativas (glibc, Pango)  
🔄 **Fallback:** Se FastAPI apresentar curva de aprendizado excessiva → Flask (MIT) como alternativa

#### Trade-offs Aceitos

- Simplicidade (KISS) > Performance extrema
- FOSS absoluto > Conveniência de soluções proprietárias
- SQLite > PostgreSQL (complexidade operacional desnecessária para MVP)

---

### ADR-002: Kanban como Método de Execução

**Status:** Aprovada  
**Data:** 19/09/2026  
**Decisor:** GP Leonardo (CCB)  
**Rastreabilidade:** TAP §1.c + §3 (Métricas) + EAP N1.5, N7

#### Contexto

O TAP declara Kanban como método de execução (P1), mas o glossário v2.1 mencionava "Sprint" e "Sprint Planning" (incompatível com fluxo contínuo). É necessário operacionalizar o método de forma consistente.

#### Decisão

- **Ferramenta:** GitHub Projects (SSOT)
- **Colunas do fluxo:** `Backlog` → `Ready (DoR)` → `In Progress` → `Code Review` → `Done (DoD)`
- **WIP Limits:** 3 cards em `In Progress` por pessoa (Domínio de Equipe PMBOK 7ª — prevenção de burnout, TAP §10 R3)
- **Pull system:** Trabalho puxado por capacidade, não empurrado por cronograma rígido
- **Rituais:**
  - Daily assíncrona: GitHub Issues (15min/dia)
  - Refinement semanal: Product Backlog (30min)
  - Retrospectiva quinzenal: Risk backlog + lições aprendidas
- **Sprints:** NÃO utilizadas — fluxo contínuo (TAP §3 "Métricas")

#### Consequências

✅ **Positivas:** Flexibilidade, visibilidade total, métricas de fluxo nativas (GitHub Insights)  
⚠️ **Riscos:** Requer disciplina de WIP limits; risco de cards parados em `Code Review`  
🔄 **Fallback:** Se throughput cair abaixo de 3 cards/semana por 2 semanas consecutivas → revisar WIP limits

#### Mapeamento Domínios PMBOK 7ª → Rituais Kanban

| Domínio PMBOK 7ª | Ritual Kanban | Artefato |
|-------------------|---------------|----------|
| Stakeholders | Refinement semanal | Backlog refinado |
| Equipe | Daily assíncrona + WIP limits | GitHub Projects |
| Abordagem de Desenvolvimento | Fluxo contínuo (sem sprints) | CFD |
| Planejamento | Refinement + Priorização | Backlog ordenado |
| Trabalho do Projeto | Pull system | Cards em fluxo |
| Entrega | DoD + Code Review | Incrementos validados |
| Medição | Cycle Time + Throughput | GitHub Insights |
| Incerteza | Retrospectiva + Risk backlog | Lições aprendidas |

#### Trade-offs Aceitos

- Fluxo contínuo > Iterações time-boxed (adequado à equipe de 3 pessoas)
- GitHub Projects > Jira/Trello (integração nativa ao SSOT, zero custo)

---

### ADR-003: Métricas de Fluxo (Substituição de EVM)

**Status:** Aprovada  
**Data:** 19/09/2026  
**Decisor:** GP Leonardo (CCB)  
**Rastreabilidade:** TAP §3 (Métricas) + §11.3 (implícito) + Domínio de Medição PMBOK 7ª

#### Contexto

O glossário v2.1 listava SPI/CPI (EVM — PMBOK 6ª) como métricas ativas. O TAP §3 declara explicitamente uso de métricas de fluxo Kanban. Há conflito que deve ser resolvido.

#### Análise Técnica

**EVM (SPI/CPI):** Projetado para ambientes preditivos com linha de base de custos. Inaplicável ao COGME porque:
- Orçamento zero (TAP §11) → AC (Actual Cost) = 0 → CPI indeterminado
- Escopo emergente (Kanban) → PV (Planned Value) não faz sentido em fluxo contínuo

**Métricas de fluxo Kanban:** Alinhadas ao Domínio de Medição PMBOK 7ª e à realidade ágil do projeto.

#### Decisão

**Métricas oficiais do COGME (exclusivas):**

| Métrica | Fórmula | Meta | Frequência |
|---------|---------|------|------------|
| Cycle Time | Média (Done − In Progress) | ≤ 3 dias | Semanal |
| Throughput | Cards concluídos / semana | ≥ 5 cards | Semanal |
| CFD (Cumulative Flow Diagram) | Visualização de gargalos | Sem bandas largas | Semanal |
| WIP em fluxo | Cards em In Progress | ≤ 9 (3 × 3 pessoas) | Contínuo |
| Coverage | Linhas testadas / totais | ≥ 80% | Por push (CI) |

**Métricas LEGADO (NÃO APLICÁVEIS):**
- ❌ SPI (Schedule Performance Index)
- ❌ CPI (Cost Performance Index)
- ❌ EVM (Earned Value Management)

**Declaração formal:** SPI/CPI são removidos do glossário v2.2 e marcados como "LEGADO — NÃO APLICÁVEL — Substituído por métricas de fluxo Kanban (ADR-003)".

#### Consequências

✅ **Positivas:** Alinhamento ao Manifesto Ágil, métricas nativas do GitHub, foco em valor entregue  
⚠️ **Riscos:** Exige calibração inicial (23/09 a 03/10) para estabelecer baseline realista  
🔄 **Fallback:** Se baseline indicar throughput < 3 cards/semana após 03/10 → revisar escopo do MVP (gestão de mudanças)

#### Período de Calibração

- **Início:** 23/09/2026
- **Fim:** 03/10/2026
- **Objetivo:** Coletar dados reais para estabelecer metas factíveis (TAP §3 "Métricas e Indicadores")
- **Saída:** Baseline documentada + metas ajustadas (se necessário via change-request)

#### Trade-offs Aceitos

- Métricas de fluxo > EVM (adequação ao contexto ágil)
- Baseline empírica > Metas arbitrárias (Domínio de Medição PMBOK 7ª)

---

### ADR-004: Controle de Progresso via Tasklists Markdown (Rejeição de Subissues)

**Status:** Aprovada  
**Data:** 20/09/2026  
**Decisor:** GP Leonardo (CCB — membro único)  
**Rastreabilidade:** TAP §1.c (Governança Híbrida) + REQ-12 (ADRs) + ADR-002 (Kanban) + ADR-003 (Métricas)  
**Domínio PMBOK 7ª:** Abordagem de Desenvolvimento + Medição + Trabalho do Projeto  
**Processo PMBOK 6ª (dicionário):** 4.3 — Orientar e Gerenciar o Trabalho do Projeto

#### Contexto

Cards complexos (estimativa ≥ 6h ou com múltiplos entregáveis, como o Plano de Qualidade ou a Configuração do Repositório) exigem decomposição visual do progresso interno para evitar a opacidade de cards estagnados na coluna `In Progress` por múltiplos dias. A equipe avaliou mecanismos para prover esta granularidade sem violar o fluxo Kanban.

#### Opções Avaliadas

1. **Sem decomposição:** Card único, sem visibilidade de progresso interno.
2. **Tasklists Markdown nativas (`- [ ]`):** Checklists no corpo da Issue.
3. **Subissues reais (Issues filhas):** Issues vinculadas via `#`, com status independente.

#### Decisão

Adotar a **Opção 2 (Tasklists Markdown condicionais)** e **rejeitar formalmente a Opção 3 (Subissues reais)**.

**Regras de aplicação:**
- **Obrigatórias** para cards com estimativa ≥ 6h ou múltiplos entregáveis.
- **Proibidas** para cards atômicos (≤ 4h) ou em status `Code Review`/`Done`.
- **Formato canônico:** Mínimo 3 itens, máximo 7 itens; último item obrigatoriamente "Validação final".
- **Natureza binária:** Itens são "feito/não feito", sem status intermediário.

#### Consequências

✅ **Positivas:** Zero overhead de gestão; visibilidade nativa no GitHub (barra de progresso da tasklist); não fragmenta o backlog no GitHub Projects.  
⚠️ **Riscos:** Requer disciplina do responsável para manter a tasklist atualizada durante a execução.  
🔄 **Fallback:** Se a tasklist se mostrar insuficiente para cards de código (M2/M3), reavaliar na Retrospectiva da MF2.

#### Impacto nas Métricas (ADR-003)

- **Cycle Time e Throughput:** Medem exclusivamente o **card pai**. Sub-tarefas da tasklist não são unidades de entrega.
- **WIP Limit:** Conta o **card pai** na coluna `In Progress` (respeitando o limite de 3 cards/pessoa da ADR-002).
- **CFD:** Ignora o progresso interno da tasklist, evitando distorção das bandas largas.

#### Trade-offs Aceitos

- Simplicidade (GMV) > Granularidade de status de sub-tarefas.
- Unidade atômica de métrica (card pai) > Rastreabilidade fina de sub-passos.
- Valor Ágil aplicado: *"Indivíduos e interações sobre processos e ferramentas."*

#### Adendo Normativo: Atualização do Plano de Escopo (§2.6)

A seção 2.6 (Definition of Ready e Definition of Done) do Plano de Escopo deve ser atualizada para incorporar a tasklist como gate de qualidade.

**Ação:** Adicionar o item 8 ao DoD na próxima revisão do plano:

> **8.** se o card possuir tasklist Markdown no corpo da Issue (conforme ADR-004), 100% dos itens estejam marcados como concluídos.

---

## 5. GLOSSÁRIO v3.0 — CORREÇÕES APLICADAS

### 5.1 Termos Corrigidos (v2.2 → v3.0)

| Termo | v2.2 | v3.0 (Corrigido) |
|-------|------|------------------|
| CCB | "Comitê de controle de mudanças (GP Leonardo — membro único, TAP v3 §1.c)" | Mantido — sem alteração |
| SPI | "LEGADO — NÃO APLICÁVEL — Substituído por Cycle Time (ADR-003)" | Mantido — sem alteração |
| CPI | "LEGADO — NÃO APLICÁVEL — Substituído por Throughput (ADR-003)" | Mantido — sem alteração |
| EVM | "LEGADO — NÃO APLICÁVEL — Orçamento zero inviabiliza EVM (ADR-003)" | Mantido — sem alteração |
| Sprint | "NÃO UTILIZADO — Fluxo contínuo Kanban (ADR-002)" | Mantido — sem alteração |
| Hardware (P6) | "Adequado e suficiente" (premissa revisada — hardware.md comprova) | Mantido — sem alteração |
| Fronteira M1 | Ambiguidade (5 ou 8 planos) | **Corrigido:** M1 entrega 5 planos (Áreas 1–5); Áreas 6–8 diferidas para M2 |

### 5.2 Termos Adicionados (v3.0)

| Termo | Definição | Contexto |
|-------|-----------|----------|
| Tasklist Markdown | Checklist nativo do GitHub (`- [ ]`) no corpo da Issue | ADR-004 — controle de progresso interno de cards complexos |
| Subissue | Issue filha vinculada a uma Issue pai | **REJEITADO** formalmente pela ADR-004 |
| Card Ubíquo | Card autossuficiente que declara o quê, por quê, como será aceito e a quem pertence sem dependência de leitura externa | Padrão de redação definido no OKB §9.3 |
| P0–P3 | Escala de prioridade temporal complementar ao MoSCoW | P0 = caminho crítico; P3 = postergável |
| pair-review | Status de artefato redigido aguardando validação de um par | Aplica-se a planos, requisitos, matrizes |
| in-review | Status de artefato aprovado pelo CCB aguardando consolidação/versionamento final | Aplica-se a ADRs, decisões formais |

---

## 6. RASTREABILIDADE CONSOLIDADA (TAP → OKB → ADRs)

| TAP § | OKB v3.0 | ADR | Domínio PMBOK 7ª |
|-------|----------|-----|------------------|
| §1.c (Governança) | §1.1, §1.2 | ADR-002 | Abordagem de Desenvolvimento |
| §3 (Métricas) | §3.2 (P1–P8) | ADR-003 | Medição |
| §3 (Inovação) | §4 (ADRs) | ADR-001 | Trabalho do Projeto |
| §6 (M1 — fronteira 5 planos) | §1.4 (Entrega Faseada) | — | Abordagem de Desenvolvimento |
| §8 (Restrições FOSS) | §3.3 | ADR-001 | Abordagem de Desenvolvimento |
| §9 (Premissas) | §3.2 (P6 revisada) | — | Recursos |
| §10 (Riscos) | §3.2 (P5 — burnout) | ADR-002 (WIP limits) | Equipe |
| REQ-12 (ADRs) | §4 (4 ADRs emitidas) | ADR-001, 002, 003, 004 | Trabalho do Projeto |

---

## 7. PRÓXIMOS PASSOS (Pré-M1: 22/09/2026)

| Ação | Responsável | Prazo | Prioridade |
|------|-------------|-------|------------|
| Consolidar OKB v3.0 no repositório | Leonardo | 20/09 | CRÍTICA |
| Atualizar glossário para v3.0 | Leonardo | 20/09 | ALTA |
| Configurar GitHub Projects (colunas + WIP) | Leonardo | 20/09 | CRÍTICA |
| Criar 27 labels no repositório (sistema de tags) | Leonardo | 20/09 | CRÍTICA |
| Criar 5 milestones no GitHub | Leonardo | 20/09 | CRÍTICA |
| Redigir Plano de Integração (GMV) | Leonardo | ✅ Concluído (19/09) | — |
| Redigir Plano de Escopo | Fabricio | 21/09 | ALTA |
| Redigir Plano de Cronograma | Fabricio | 21/09 | ALTA |
| Redigir Plano de Custos | Fabricio | 21/09 | ALTA |
| Redigir Plano de Qualidade (12 PDCAs + Ishikawa) | Edson | 21/09 | ALTA |
| Aplicar tasklists nos cards ≥ 6h (ADR-004) | Equipe | 21/09 | ALTA |
| Submeter M1 via GitHub | Leonardo | 22/09 | CRÍTICA |

---

## 8. LITERATURA DE APOIO — QUESTÕES ADJACENTES

Esta seção documenta decisões técnicas fundamentadas em literatura PMBOK® e boas práticas de gerenciamento de projetos, utilizadas como apoio às decisões de configuração do GitHub e governança do COGME.

### 8.1 Área de Conhecimento para Rede de Projeto e Caminho Crítico

**Questão:** Segundo PMI PMBOK ed 7 e 6, qual área de conhecimento deve conter a rede de projeto contendo a sequência de tarefas do projeto conforme progressão e tempo para cálculo das tabelas de precedência e caminhos críticos?

**Resposta técnica:**

| Edição | Resposta |
|--------|----------|
| PMBOK® 6ª (Dicionário) | **Gerenciamento do Cronograma do Projeto** — Processos 6.4 (Sequenciar as Atividades) e 6.6 (Desenvolver o Cronograma) |
| PMBOK® 7ª (Governança Primária) | **Domínio de Desempenho de Planejamento** (evolução progressiva do cronograma) + **Domínio de Desempenho de Medição** (monitoramento do progresso temporal) |

**Aplicação no COGME:**

Conforme ADR-003 e Plano de Integração §1.6.2, o projeto declara formalmente a **obsolescência operacional** do uso de redes de projeto detalhadas (CPM/Gantt) para o gerenciamento do fluxo de trabalho diário.

| Nível | Abordagem |
|-------|-----------|
| Macro (Marcos M1–M4) | Sequenciamento temporal fixo; lógica de precedência do PMBOK 6ª (Processo 6.5) usada apenas para validar viabilidade acadêmica |
| Operacional (Tarefas da EAP) | Sequenciamento gerenciado pelo Pull System no GitHub Projects (ADR-002); "caminho crítico" identificado empiricamente por gargalos no CFD e Cycle Time (ADR-003) |

**Trade-off declarado:** Abre-se mão da formalidade preditiva (CPM/EVM) em favor de métricas de fluxo ágil nativas, conforme o Domínio de Medição do PMBOK 7ª e o método Kanban.

---

### 8.2 Estruturação do Cumulative Flow Diagram (CFD) para Demonstração Formal

**Questão:** Como estruturar no documento o Cumulative Flow Diagram (CFD) para demonstração formal ao orientador?

**Resposta técnica:**

O CFD deve aparecer em três artefatos, com funções distintas:

| Artefato | Seção | Função |
|----------|-------|--------|
| Plano de Integração | §1.6.1 (Métricas de Fluxo) | Definição formal + cadência |
| Plano de Cronograma | §2.3 (Monitoramento Temporal) | Substituto do Gantt/EVM |
| Plano de Comunicações | §3.2 (Relatórios Semanais) | Evidência visual de progresso |

**Regra GMV:** Não criar artefato separado. O CFD é métrica nativa do GitHub Insights — qualquer documentação adicional seria burocracia.

**Definição formal (para inclusão nos planos):**

> O Cumulative Flow Diagram (CFD) é a visualização gráfica do fluxo de trabalho acumulado ao longo do tempo, onde cada banda horizontal representa uma coluna do quadro Kanban (Backlog, Ready, In Progress, Code Review, Done). A largura de cada banda em um determinado instante indica a quantidade de cards naquela etapa.

**Fonte de dados:** GitHub Projects → GitHub Insights → Aba "Charts" → "Cumulative Flow Diagram"  
**Frequência:** Semanal (toda segunda-feira, 09:00)  
**Responsável:** GP Leonardo David Silva Setti

**Meta de desempenho:**
- **CFD saudável:** Bandas paralelas e de largura constante (fluxo estável)
- **CFD com gargalo:** Bandas que se alargam progressivamente (acúmulo em uma etapa)
- **Ação corretiva:** Se uma banda ultrapassar 2× a largura média das demais por 2 semanas consecutivas, acionar Retrospectiva extraordinária (ADR-002)

**Blindagem acadêmica:** Se o Prof. Dr. Nivaldo Carleto questionar a ausência de Gantt, a defesa técnica é a ADR-003, fundamentada em três pilares:
1. Domínio de Medição do PMBOK 7ª: Prioriza métricas de fluxo sobre métricas preditivas
2. Restrição de Orçamento Zero (TAP §11): Inviabiliza EVM (AC = 0 → CPI indeterminado)
3. Natureza do Fluxo Contínuo (ADR-002): CFD fornece visibilidade em tempo real sem overhead

---

### 8.3 Resolução da Inconsistência de Fronteira do M1

**Questão:** O TAP §6 M1 declara 5 planos, mas o OKB v2.2 lista 8 planos. Esta informação sana a inconsistência TAP?

**Resposta técnica:**

**Sim, esta informação sana totalmente a inconsistência** e valida a governança híbrida sob a ótica do PMBOK®.

| Artefato | Leitura Anterior (Incorreta) | Leitura Corrigida (Governança Híbrida) |
|----------|------------------------------|----------------------------------------|
| TAP §6 | "Incompleto" por citar apenas 5 áreas | **Correto:** Define a linha de base faseada do Marco M1 (Fundação) |
| OKB v2.2 §3.1 | "Contraditório" por listar 8 planos | **Correto:** Define o inventário total de artefatos do projeto ao longo de todo o ciclo de vida |
| Plano de Integração | Ambiguidade sobre "7 planos subsequentes" | Atualizado para explicitar a estratégia de entrega faseada |

**Princípio PMBOK 7ª Aplicado:** Personalização (Tailoring) da Abordagem de Desenvolvimento. Entregar todos os 8 planos no M1 geraria overhead burocrático inicial desnecessário (anti-ágil). Deferir Recursos, Comunicações e Riscos para quando o fluxo de trabalho estiver mais maduro é uma decisão de tailoring legítima e defensável academicamente.

---

## 9. CONFIGURAÇÃO OPERACIONAL DO GITHUB

Esta seção formaliza as decisões de configuração do GitHub como SSOT do COGME, conforme ADR-002.

### 9.1 Sistema de Tags (Labels) — 27 Labels em 5 Categorias

**Fundamentação:** As tags abaixo foram desenhadas para operar no GitHub Issues + GitHub Projects (SSOT, ADR-002), com três objetivos:
1. Rastreabilidade TAP → EAP → Card (cada card vincula-se a fase, área e requisito)
2. Métricas de fluxo (Throughput e Cycle Time por tipo/área, ADR-003)
3. Controle de mudanças e riscos (labels operacionais do Plano de Integração §1.7 e §1.9)

**Princípio aplicado:** GMV — cada tag existe apenas se for útil para filtragem, métrica ou governança.

#### Categoria 1 — Tipo de Trabalho (6 tags)

| Tag | Descrição | Cor sugerida |
|-----|-----------|--------------|
| `feat` | Nova funcionalidade do MVP | `#0E8A16` (verde) |
| `bug` | Defeito em funcionalidade existente | `#D73A4A` (vermelho) |
| `docs` | Artefatos textuais: planos, TAP, OKB, Glossário, lições aprendidas | `#0075CA` (azul) |
| `test` | Testes unitários, de integração e UAT | `#BFD4F2` (azul claro) |
| `ci` | Configuração e manutenção do pipeline GitHub Actions | `#FBCA04` (amarelo) |
| `chore` | Tarefas operacionais que não alteram código nem docs | `#E4E669` (cinza-esverdeado) |

#### Categoria 2 — Macro-Fase EAP (3 tags)

| Tag | Descrição | Cor sugerida |
|-----|-----------|--------------|
| `MF1-fundacao` | Fases N1 a N4, N8, N9, N10 (parcial) | `#D4C5F9` (roxo claro) |
| `MF2-construcao` | Fases N5 a N7, N10 | `#C5DEF5` (azul claro) |
| `MF3-consolidacao` | Fases N11 e N12 | `#BFDADC` (rosa claro) |

#### Categoria 3 — Área de Conhecimento (8 tags)

| Tag | Descrição | Cor sugerida |
|-----|-----------|--------------|
| `area:integracao` | Coordenação entre planos, controle de mudanças, SSOT | `#1D76DB` (azul) |
| `area:escopo` | Requisitos, EAP, DoR/DoD, fronteira IN/OUT, YAGNI | `#006B75` (teal) |
| `area:cronograma` | Marcos M1–M4, fluxo contínuo, baseline de métricas | `#5319E7` (roxo) |
| `area:custos` | Orçamento zero, conformidade FOSS | `#B60205` (vermelho escuro) |
| `area:qualidade` | Coverage ≥ 80%, UAT, 12 PDCAs, Ishikawa 6M | `#008672` (verde-azulado) |
| `area:recursos` | Equipe de 3, hardware, prevenção de burnout | `#D93F0B` (laranja) |
| `area:comunicacoes` | Daily assíncrona, Refinement, Retrospectiva | `#F9D0C4` (salmão) |
| `area:riscos` | R1–R5, risk backlog, gatilhos de escalation | `#B60205` (vermelho escuro) |

#### Categoria 4 — Status Operacional (4 tags)

| Tag | Descrição | Cor sugerida |
|-----|-----------|--------------|
| `change-request` | Solicitação formal de mudança. Aciona fluxo CCB em ≤ 48h | `#FF0000` (vermelho) |
| `risk` | Risco identificado ou materializado (R1–R5) | `#FFFF00` (amarelo) |
| `blocked` | Card bloqueado por dependência externa ou interna | `#B60205` (vermelho escuro) |
| `sdd-ia` | Artefato ou código gerado com apoio de IA generativa (SDD) | `#A2EEEF` (ciano) |

#### Categoria 5 — Prioridade (6 tags: MoSCoW + P0–P3)

| Tag | Descrição | Cor sugerida |
|-----|-----------|--------------|
| `must` | Requisito indispensável ao MVP | `#B60205` (vermelho escuro) |
| `should` | Requisito importante mas não bloqueante | `#FBCA04` (amarelo) |
| `P0` | Crítico / Caminho crítico | `#B60205` (vermelho escuro) |
| `P1` | Alto | `#D93F0B` (laranja) |
| `P2` | Médio | `#FBCA04` (amarelo) |
| `P3` | Baixo | `#0E8A16` (verde) |

#### Regras de Aplicação

1. Todo card deve ter no mínimo 3 tags: 1 tipo + 1 macro-fase + 1 área.
2. Cards de código devem ter obrigatoriamente `feat` ou `bug` + tag de macro-fase.
3. Cards de documentação devem ter `docs` + `area:X` correspondente.
4. Cards com `sdd-ia` exigem que o commit vinculado declare co-autoria (DoD, Plano de Escopo §2.6).
5. Cards com `change-request` não migram para `In Progress` até aprovação do GP.
6. Cards com `blocked` devem registrar a dependência no corpo da Issue.

#### Tags Explicitamente Excluídas (decisão GMV)

| Tag rejeitada | Motivo da exclusão |
|---------------|-------------------|
| `N1` … `N12` (fases individuais) | 12 tags redundantes; fase já consta no título padronizado |
| `REQ-01` … `REQ-15` | Rastreabilidade via corpo do card, não via tag |
| `could`, `wont` | Classes vazias no escopo atual |
| `epic` | MVP é único; não há múltiplos épicos |
| `spike` | Não há pesquisa exploratória formal no escopo |
| `good first issue` | Equipe de 3 pessoas; onboarding não se aplica |
| `help wanted` | Mesmo motivo |

---

### 9.2 Milestones do Projeto — 5 Milestones

**Decisão GMV:** 5 milestones no total. O GitHub não suporta hierarquia nativa de milestones, portanto as subfases da EAP são rastreadas via labels de macro-fase dentro de cada milestone.

| # | Milestone | Due Date | Abertura | Macro-Fase | Tipo | Cards Associados |
|---|-----------|----------|----------|------------|------|------------------|
| 1 | `M1 — Entrega Parcial Documental` | 22/09/2026 | 01/09/2026 | MF1 | Marco oficial | M1-01 a M1-21 |
| 2 | `M2 — Ambiente e Modelagem Concluídos` | 30/09/2026 | 23/09/2026 | MF1 (encerramento) | Marco oficial | N3.x, N4.x, N2.3 |
| 3 | `Calibração — Baseline de Métricas` | 03/10/2026 | 23/09/2026 | MF1 → MF2 (transição) | Auxiliar | Baseline + ADR de metas |
| 4 | `M3 — MVP Funcional (Beta)` | 15/11/2026 | 04/10/2026 | MF2 | Marco oficial | N5.x, N6.x, N7.1, N10.x |
| 5 | `M4 — Encerramento e Validação Acadêmica` | 15/12/2026 | 16/11/2026 | MF3 | Marco oficial | N11.x, N12.x |

#### Regras de Aplicação no GitHub

1. Cada Issue deve estar associada a exatamente uma milestone. Cards sem milestone são tratados como `Backlog` não planejado.
2. A milestone não pode ser fechada enquanto houver Issues abertas com label `blocked` ou `change-request`.
3. O fechamento da milestone exige: (i) todos os critérios de fechamento atendidos, (ii) registro de lições aprendidas da fase, (iii) comunicação ao Prof. Dr. Nivaldo Carleto quando aplicável (M1, M3, M4).
4. Alteração de data de milestone exige `change-request` + aprovação do CCB (GP Leonardo) + ADR se alterar marco oficial.
5. A milestone auxiliar (Calibração) não substitui M2 — são complementares. M2 encerra MF1; Calibração estabelece baseline para MF2.

---

### 9.3 Padrão de Redação de Cards Ubíquos

**Princípio do Card Ubíquo:** Um card ubíquo é autossuficiente: qualquer membro da equipe (ou o Prof. Dr. Nivaldo Carleto, em avaliação) deve conseguir compreender o quê, por quê, como será aceito e a quem pertence sem abrir nenhum outro artefato.

**Três propriedades obrigatórias:**
1. **Autocontextualização** — o card declara sua finalidade em linguagem própria
2. **Critério de aceite mensurável** — checklist binário (atingido/não atingido)
3. **Rastreabilidade dupla** — vínculo vertical (TAP → EAP → REQ) e horizontal (área + macro-fase + milestone)

#### Padrão A — Card Documental / Governança / Infraestrutura

**Aplica-se a:** `docs`, `ci`, `chore`.

| Campo | Função | Regra de preenchimento |
|-------|--------|------------------------|
| 1. Título | Identificação padronizada | Formato `N{X}.{Y} — Descrição curta` |
| 2. Contexto Ubíquo | Por que este card existe | 2 a 3 frases autocontidas |
| 3. Descrição da Entrega | O que será produzido | Verbo no infinitivo + artefato + localização |
| 4. Critérios de Aceite | Checklist binário | Mínimo 3 itens mensuráveis |
| 5. Rastreabilidade | Elo de auditoria | TAP §X + EAP NX.Y + REQ-XX + Domínio PMBOK 7ª |
| 6. Dependências | Pré-requisitos explícitos | Listar cards ou artefatos bloqueantes |
| 7. Atribuição | Responsável + esforço | Nome completo + estimativa ≤ 8h |
| 8. Estado | Tags + milestone + status | Mínimo 3 tags + milestone + status operacional |

#### Padrão B — Card User Story (GWT) — padrão projetivo para M2

**Aplica-se a:** `feat`, `bug`, `test`.  
**Status normativo:** Padrão definido nesta data, com aplicação efetiva a partir do marco M2 (30/09/2026).

| Campo | Função | Regra de preenchimento |
|-------|--------|------------------------|
| 1. Título | Identificação padronizada | Formato `N{X}.{Y} — US-{NN}: Descrição` |
| 2. User Story | Narrativa de valor | `Como [papel], quero [ação], para [benefício mensurável]` |
| 3. Contexto Ubíquo | Dor de negócio endereçada | 1 a 2 frases ligando a história ao público-alvo |
| 4. Critérios de Aceite (GWT) | Comportamento verificável | Blocos `Dado / Quando / Então`; mínimo 2 cenários |
| 5. Regras de Negócio | Restrições de domínio | Spread, IOF, precisão decimal, regimes |
| 6. Rastreabilidade | Elo de auditoria | REQ-XX + EAP NX.Y + Domínio PMBOK 7ª |
| 7. Dependências | Pré-requisitos técnicos | Cards de arquitetura, DER ou API bloqueantes |
| 8. Atribuição | Responsável + esforço | Nome completo + estimativa ≤ 8h |
| 9. Estado | Tags + milestone + status | Mínimo 3 tags + milestone + status operacional |

---

### 9.4 Sistema de Prioridade P0–P3

**Definição:** Escala complementar ao MoSCoW (que classifica valor de escopo) e foca em urgência temporal e criticidade de bloqueio.

| Peso | Definição | Critério objetivo | Ação no Kanban |
|------|-----------|-------------------|----------------|
| P0 | Crítico / Caminho crítico | Sem este card, o marco não é atingido ou ele bloqueia ≥ 2 outros cards | Execução imediata; WIP reservado; Daily obrigatória |
| P1 | Alto | Essencial para o marco, mas não bloqueia outros cards diretamente | Execução na janela do marco |
| P2 | Médio | Importante, mas pode deslizar para o marco seguinte | Execução pós-marco atual |
| P3 | Baixo | Desejável; postergável sem impacto formal | Backlog priorizado; puxar apenas se capacidade sobrar |

**Regra de desempate:** Se dois cards têm o mesmo peso, prioriza-se aquele que desbloqueia mais cards subsequentes.

**Trade-off declarado:** Um card `must` (MoSCoW) pode ser P2 se sua entrega puder deslizar para M2 sem violar o critério de aceite do M1.

---

## 10. BACKLOG DO MARCO M1 — CONSOLIDADO

### 10.1 Resumo dos 21 Cards

| # | Card | Tipo | Macro-Fase | Área | Prioridade MoSCoW | Prioridade Temporal | Milestone | Status |
|---|------|------|------------|------|-------------------|---------------------|-----------|--------|
| M1-01 | Plano de Integração | docs | MF1 | area:integracao | must | P0 | M1 | 🔄 pair-review |
| M1-02 | Plano de Escopo | docs | MF1 | area:escopo | must | P0 | M1 | 🔄 pair-review |
| M1-03 | Plano de Cronograma | docs | MF1 | area:cronograma | must | P0 | M1 | ⏳ 21/09 |
| M1-04 | Plano de Custos | docs | MF1 | area:custos | must | P0 | M1 | ⏳ 21/09 |
| M1-05 | Plano Qualidade + PDCAs + Ishikawa | docs | MF1 | area:qualidade | must | P0 | M1 | ⏳ 21/09 |
| M1-06 | Requisitos Funcionais | docs | MF1 | area:escopo | must | P1 | M1 | 🔄 pair-review |
| M1-07 | Requisitos Não Funcionais | docs | MF1 | area:qualidade | must | P1 | M1 | 🔄 pair-review |
| M1-08 | Arquitetura da Solução | docs | MF1 | area:escopo | must | P2 | M2 | ⏳ 30/09 |
| M1-09 | Protótipo UX/UI | docs | MF1 | area:escopo | should | P3 | M2 | ⏳ 30/09 |
| M1-10 | Modelagem de Dados (DER) | docs | MF1 | area:escopo | must | P2 | M2 | ⏳ 30/09 |
| M1-11 | Seleção Stack FOSS (ADR-001) | docs | MF1 | area:recursos | must | P1 | M1 | 🔄 in-review |
| M1-12 | Repositório Git + CI/CD | ci | MF1 | area:integracao | must | P0 | M1 | ⏳ 22/09 |
| M1-13 | Setup Local e Homologação | chore | MF1 | area:recursos | must | P1 | M1 | ⏳ 22/09 |
| M1-14 | Auditoria de Licenças FOSS | docs | MF1 | area:qualidade | must | P2 | M2 | ⏳ 30/09 |
| M1-15 | ADR-001 Stack | docs | MF1 | area:integracao | must | P1 | M1 | 🔄 in-review |
| M1-16 | ADR-002 Kanban | docs | MF1 | area:integracao | must | P1 | M1 | 🔄 in-review |
| M1-17 | ADR-003 Métricas | docs | MF1 | area:cronograma | must | P1 | M1 | 🔄 in-review |
| M1-18 | Lições Aprendidas MF1 | docs | MF1 | area:integracao | should | P3 | M2 | ⏳ 30/09 |
| M1-19 | Matriz RACI | docs | MF1 | area:comunicacoes | should | P2 | M1 | ⏳ 22/09 |
| M1-20 | Canais Oficiais | docs | MF1 | area:comunicacoes | should | P2 | M1 | ⏳ 22/09 |
| M1-21 | Labels + change-request | chore | MF1 | area:integracao | must | P1 | M1 | ⏳ 22/09 |

**Total:** 21 cards · 15 `must` · 6 `should` · 6 P0 · 8 P1 · 5 P2 · 2 P3

### 10.2 Cards que Receberão Tasklist (ADR-004)

| Card | Estimativa | Justificativa |
|------|------------|---------------|
| M1-01 (Plano de Integração) | 6h | Múltiplas seções; requer validação cruzada |
| M1-02 (Plano de Escopo) | 6h | Múltiplas seções; requer validação cruzada |
| M1-05 (Plano Qualidade + PDCAs + Ishikawa) | 8h | Múltiplos entregáveis (plano + 12 PDCAs + diagrama) |
| M1-08 (Arquitetura da Solução) | 6h | Diagrama + validação de componentes |
| M1-09 (Protótipo UX/UI) | 8h | Wireframes + validação de usabilidade |
| M1-10 (Modelagem de Dados DER) | 6h | Entidades + cardinalidades + validação SQLite |
| M1-12 (Repositório Git + CI/CD) | 6h | Repositório + pipeline + Projects + labels |

### 10.3 Distribuição de Trabalho por Membro

| Membro | Cards P0 | Cards P1 | Cards P2/P3 | Carga Total Estimada |
|--------|----------|----------|-------------|----------------------|
| Leonardo | M1-01, M1-12 | M1-15, M1-16, M1-17, M1-21 | M1-20 | ~14h |
| Fabricio | M1-02, M1-03, M1-04 | M1-06, M1-13 | M1-10 | ~13h |
| Edson | M1-05 | M1-07 | M1-19 | ~11h |

**Verificação:** Todos os membros estão dentro do limite de 20h/semana (Premissa P5) e do WIP limit de 3 cards/pessoa em `In Progress` (ADR-002).

---

## 11. VERIFICAÇÃO DE CONGRUÊNCIA

| Item | Status |
|------|--------|
| OKB v3.0 substitui formalmente OKB v2.2 | ✅ OK |
| ADR-004 incorporada na seção 4 (ADRs Emitidas) | ✅ OK |
| Seção de Literatura de Apoio (Questões Adjacentes) criada | ✅ OK |
| Configuração do GitHub formalizada (tags, milestones, backlog) | ✅ OK |
| Fronteira M1 corrigida (5 planos, não 8) | ✅ OK |
| Estratégia de Entrega Faseada documentada (§1.4) | ✅ OK |
| Sistema de tags expandido de 23 para 27 labels (inclusão P0–P3) | ✅ OK |
| Padrão de redação de cards definido (Padrão A + Padrão B) | ✅ OK |
| Sistema de prioridade P0–P3 formalizado | ✅ OK |
| Tasklists Markdown (ADR-004) integradas ao DoD | ✅ OK |
| Prof. Dr. Nivaldo Carleto sempre por extenso | ✅ OK |
| EVM declarado LEGADO — NÃO APLICÁVEL | ✅ OK |
| Obsolescência PMBOK 6ª declarada formalmente | ✅ OK |
| Rastreabilidade TAP → OKB → ADRs preservada | ✅ OK |
| Princípio GMV respeitado em todas as seções | ✅ OK |

---

**OKB v3.0 emitido por:** GP Leonardo David Silva Setti  
**Aprovação:** CCB (GP — membro único, TAP v3 §1.c)  
**Data:** 20/09/2026  
**Status:** ✅ Convergente ao TAP v3 + ADRs 001–004 — pronto para M1  
**Substitui:** OKB v2.2 (19/09/2026)

---

*Fim do documento — OKB v3.0 | COGME | Fatec Taquaritinga | 20/09/2026*
# Análise Crítica — Sub-seção 10.2 e ADR-004

## Diagnóstico da Ambiguidade

A sub-seção 10.2 ("Cards que Receberão Tasklist") está **tecnicamente correta**, mas a redação atual pode gerar uma leitura equivocada:

| Leitura Possível | Problema |
|-----------------|----------|
| "Tasklist = subissue disfarçada" | ❌ Falso — tasklist é checklist **dentro** do corpo da Issue |
| "Se subissue é vetada, como decompor cards grandes?" | ✅ Pergunta legítima — a resposta é: **via tasklist Markdown** |
| "Tasklist fragmenta o backlog como subissue faria?" | ❌ Não — a tasklist não cria Issues filhas no GitHub Projects |

**Raiz da ambiguidade:** A sub-seção 10.2 lista *quais* cards recebem tasklist, mas não explica *como* a tasklist contorna a ausência de subissues. O leitor (especialmente o Prof. Dr. Nivaldo Carleto em avaliação) pode questionar: "Se vocês vetaram subissues, como acompanham o progresso interno de um card de 8h?"

**Solução:** Adicionar uma sub-seção **10.2.1 — Mecanismo de Contorno: Tasklist como Substituto de Subissue** que explica explicitamente a relação.

---

## Sub-seção 10.2 Revisada (para OKB v3.0)

### 10.2 Cards que Receberão Tasklist (ADR-004)

**Regra de aplicação (ADR-004):**
- **Obrigatória** para cards com estimativa ≥ 6h ou múltiplos entregáveis.
- **Proibida** para cards atômicos (≤ 4h) ou em status `Code Review`/`Done`.
- **Formato canônico:** Mínimo 3 itens, máximo 7 itens; último item obrigatoriamente "Validação final".
- **Natureza binária:** Itens são "feito/não feito" (`- [ ]` / `- [x]`), sem status intermediário.

**Cards do M1 que receberão tasklist:**

| Card | Estimativa | Justificativa | Nº de Itens |
|------|------------|---------------|-------------|
| M1-01 (Plano de Integração) | 6h | Múltiplas seções; requer validação cruzada | 5 |
| M1-02 (Plano de Escopo) | 6h | Múltiplas seções; requer validação cruzada | 5 |
| M1-05 (Plano Qualidade + PDCAs + Ishikawa) | 8h | Múltiplos entregáveis (plano + 12 PDCAs + diagrama) | 6 |
| M1-08 (Arquitetura da Solução) | 6h | Diagrama + validação de componentes | 4 |
| M1-09 (Protótipo UX/UI) | 8h | Wireframes + validação de usabilidade | 5 |
| M1-10 (Modelagem de Dados DER) | 6h | Entidades + cardinalidades + validação SQLite | 4 |
| M1-12 (Repositório Git + CI/CD) | 6h | Repositório + pipeline + Projects + labels | 6 |

**Total:** 7 cards com tasklist · 35 itens de checklist · 0 subissues criadas.

---

### 10.2.1 Mecanismo de Contorno: Tasklist como Substituto de Subissue

**Problema:** Cards complexos (≥ 6h) exigem visibilidade de progresso interno. A solução tradicional seria criar subissues (Issues filhas), mas isso foi **formalmente rejeitado** pela ADR-004 porque:
- Fragmenta o backlog no GitHub Projects (cada subissue vira um card independente)
- Distorce métricas de fluxo (Throughput e Cycle Time contariam sub-tarefas, não o entregável real)
- Viola o princípio GMV (overhead de gestão de múltiplas Issues para um único entregável)

**Contorno adotado:** Tasklist Markdown nativa do GitHub (`- [ ]` / `- [x]`) **dentro do corpo da Issue**. Este mecanismo:

| Propriedade | Subissue (VETADA) | Tasklist Markdown (ADOTADA) |
|-------------|-------------------|------------------------------|
| Cria nova Issue no repositório? | ✅ Sim | ❌ Não |
| Aparece como card no GitHub Projects? | ✅ Sim (fragmenta) | ❌ Não (permanece no card pai) |
| Afeta métricas de fluxo (ADR-003)? | ✅ Sim (distorce) | ❌ Não (card pai é a unidade) |
| Fornece visibilidade de progresso? | ✅ Sim | ✅ Sim (barra de progresso nativa) |
| Exige gestão de dependências entre Issues? | ✅ Sim (overhead) | ❌ Não |
| Overhead de gestão | Alto | Zero |

**Exemplo prático (Card M1-05 — Plano de Qualidade):**

~~~markdown
## Tasklist (ADR-004)

- [ ] Estrutura do Plano de Qualidade redigida (seções 1-8)
- [ ] 12 ciclos PDCA consolidados (um por fase da EAP)
- [ ] Diagrama de Ishikawa 6M desenhado e versionado
- [ ] Critérios de aceite vinculados a REQ-08, REQ-09, REQ-10
- [ ] Revisão em pares solicitada (Fabricio ou Leonardo)
- [ ] Validação final
~~~

**Regras operacionais:**
1. A tasklist é criada **no momento da abertura do card** (antes de migrar para `In Progress`).
2. Cada item é marcado como concluído (`- [x]`) **somente quando o critério daquele passo for objetivamente atendido**.
3. O card só migra para `Code Review` quando **100% dos itens estiverem marcados** (DoD, Plano de Escopo §2.6 item 8).
4. O GitHub exibe automaticamente uma **barra de progresso** no card (ex: "4 of 6 tasks complete"), fornecendo visibilidade sem fragmentação.

**Fundamentação PMBOK 7ª:** Domínio de Trabalho do Projeto — "O trabalho do projeto é executado por meio de atividades que produzem entregas. A decomposição do trabalho deve ser suficiente para permitir o controle, sem gerar overhead desnecessário."

**Trade-off aceito (ADR-004):** Simplicidade (GMV) > Granularidade de status de sub-tarefas. A unidade atômica de métrica permanece sendo o **card pai**, não os itens da tasklist.

---

## OKB v3.0 — Seção 10 Atualizada (Trecho Revisado)

Substituir a seção 10.2 anterior pela versão acima. As demais seções do OKB v3.0 permanecem inalteradas.

**Resumo da alteração:**

| Item | Versão Anterior | Versão Revisada |
|------|-----------------|-----------------|
| Sub-seção 10.2 | Lista de cards + justificativa | Lista + regras de aplicação + nº de itens |
| Sub-seção 10.2.1 | ❌ Inexistente | ✅ Mecanismo de contorno explicado |
| Tabela comparativa Subissue vs Tasklist | ❌ Inexistente | ✅ 6 propriedades comparadas |
| Exemplo prático de tasklist | ❌ Inexistente | ✅ Card M1-05 com 6 itens |
| Regras operacionais (4 regras) | ❌ Inexistente | ✅ Quando criar, quando marcar, quando migrar |
| Fundamentação PMBOK 7ª | ❌ Inexistente | ✅ Domínio de Trabalho do Projeto |
| Trade-off explícito | Implícito | ✅ Declarado formalmente |

**Verificação de congruência:**

| Item | Status |
|------|--------|
| ADR-004 coerente com sub-seção 10.2 | ✅ OK |
| Subissues explicitamente vetadas | ✅ OK |
| Tasklists explicitamente adotadas como contorno | ✅ OK |
| Métricas de fluxo (ADR-003) não afetadas | ✅ OK |
| WIP limits (ADR-002) não afetados | ✅ OK |
| DoD do Plano de Escopo §2.6 item 8 referenciado | ✅ OK |
| Prof. Dr. Nivaldo Carleto por extenso (se citado) | ✅ N/A (não citado nesta seção) |
| Princípio GMV respeitado | ✅ OK |

**Status:** Sub-seção 10.2 revisada — pronta para incorporação ao OKB v3.0. Nenhuma contradição residual com ADR-004.
# Política de ADRs e Integração Documental — COGME

**Domínio PMBOK 7ª:** Trabalho do Projeto + Incerteza + Abordagem de Desenvolvimento
**Processo PMBOK 6ª (dicionário):** 4.4 — Gerenciar o Conhecimento do Projeto
**Rastreabilidade:** TAP §3 (Inovação) + REQ-12 + Plano de Integração §1.5.2 + ADR-002
**Princípio norteador:** GMV (Governança Mínima Viável)

---

## 1. Gatilhos para Criação de Novas ADRs

### 1.1 Critério Formal Vigente (Plano de Integração §1.5.2)

O gatilho atual declara:

> *"Decisões que afetam ≥ 2 fases da EAP, envolvem troca de tecnologia ou seriam questionadas pelo Prof. Dr. Nivaldo Carleto em avaliação são formalmente registradas via ADR."*

Este critério é necessário mas **insuficiente** para operacionalização diária. Abaixo, formalizo uma matriz de gatilhos completa, alinhada ao GMV.

### 1.2 Matriz de Gatilhos (Teste de 4 Perguntas)

Uma decisão **exige** ADR se atender a **pelo menos 2** dos 4 critérios abaixo. Se atender a apenas 1, registra-se em commit message. Se não atender a nenhum, não se registra formalmente.

| # | Critério | Exemplo no COGME | Domínio PMBOK 7ª |
|---|----------|------------------|------------------|
| G1 | **Impacto transversal:** Afeta ≥ 2 fases da EAP ou ≥ 2 planos de área | ADR-003 (métricas) impacta Cronograma + Integração + Qualidade | Planejamento + Medição |
| G2 | **Irreversibilidade prática:** Reverter a decisão custaria > 8h de retrabalho | ADR-001 (stack) — trocar FastAPI por Flask reescreve backend | Abordagem de Desenvolvimento |
| G3 | **Questionabilidade acadêmica:** O Prof. Dr. Nivaldo Carleto poderia questionar a decisão na avaliação de um marco | ADR-004 (tasklists vs subissues) — "por que não usaram subissues?" | Stakeholders |
| G4 | **Trade-off não óbvio:** A decisão abre mão de uma alternativa viável em favor de outra, e a justificativa não é trivial | ADR-002 (Kanban sem sprints) — abre mão de iterações time-boxed | Abordagem de Desenvolvimento |

**Regra GMV:** Se a decisão atende a apenas 1 critério → commit message com prefixo `decision:`. Se atende a 0 → não se registra.

### 1.3 Gatilhos Específicos por Fase do Ciclo de Vida

| Fase | Gatilho Provável | Exemplo |
|------|-----------------|---------|
| MF1 (Fundação) | Seleção de stack, método de execução, métricas, configuração SSOT | ADRs 001–004 (já emitidas) |
| MF2 (Construção) | Troca de biblioteca, padrão arquitetural, estratégia de teste, decisão de API externa | Ex: "Adotar httpx vs requests para chamadas assíncronas" |
| MF3 (Consolidação) | Estratégia de release, formato de documentação final, decisão de licenciamento | Ex: "MIT vs GPLv3 para release final" |
| Transversal | Mudança de marco, alteração de escopo do MVP, contingência de risco materializado | Ex: "Reduzir REQ-06 para MVP se M3 estiver em risco" |

### 1.4 Gatilhos Negativos (Quando NÃO Criar ADR)

| Situação | Ação Correta | Justificativa GMV |
|----------|-------------|-------------------|
| Decisão de formatação de código (lint, indentação) | Configuração no `.editorconfig` + commit | Não afeta ≥ 2 fases |
| Escolha de nome de variável ou função | Commit message | Reversível em < 5min |
| Ajuste de texto em plano (sem mudança de escopo) | Commit `docs(plano-X): ajuste §Y` | Não é decisão arquitetural |
| Decisão já coberta por ADR existente | Referência à ADR no commit | Evita proliferação |
| Decisão operacional do dia a dia (ex: "hoje trabalho no card X") | Daily assíncrona | Não é decisão de projeto |

---

## 2. ADR Tardia — Trade-offs e Política de Regularização

### 2.1 Definição

Uma **ADR tardia** é aquela emitida **após** a decisão já ter sido implementada ou operacionalizada. No COGME, a ADR-004 (Tasklists Markdown, 20/09/2026) é o exemplo: a decisão já estava sendo aplicada quando foi formalizada.

### 2.2 Matriz de Trade-offs

| Dimensão | ADR Tempestiva (antes da execução) | ADR Tardia (após a execução) |
|----------|-------------------------------------|-------------------------------|
| **Rastreabilidade** | ✅ Plena — decisão precede ação | ⚠️ Parcial — ação precede registro |
| **Custo de produção** | Baixo (contexto fresco) | Médio (requer reconstrução do raciocínio) |
| **Risco de perda de contexto** | Baixo | Alto (detalhes da deliberação se perdem) |
| **Blindagem acadêmica** | ✅ Máxima (Prof. Dr. Nivaldo Carleto vê coerência temporal) | ⚠️ Reduzida (pode parecer racionalização post hoc) |
| **Overhead burocrático** | Baixo (integra-se ao fluxo natural) | Médio (exige parada para documentar) |
| **Valor para a equipe** | Alto (guia a execução) | Médio (documenta o que já foi feito) |

### 2.3 Política de Regularização (Regra GMV)

| Condição | Ação | Prazo |
|----------|------|-------|
| Decisão implementada há ≤ 48h e atende ≥ 2 gatilhos | Emitir ADR tardia com nota `"Regularização: decisão aplicada em [data], formalizada em [data]"` | ≤ 24h após identificação |
| Decisão implementada há > 48h e atende ≥ 2 gatilhos | Emitir ADR tardia + registrar lição aprendida ("decisão não formalizada tempestivamente") | ≤ 72h |
| Decisão implementada e atende apenas 1 gatilho | NÃO emitir ADR; registrar em commit com prefixo `decision:` | Imediato |
| Decisão implementada e atende 0 gatilhos | Não registrar formalmente | — |

### 2.4 Estrutura Obrigatória da ADR Tardia

Além dos campos padrão (Contexto, Opções, Decisão, Consequências, Trade-offs), a ADR tardia **deve** incluir:

~~~markdown
**Tipo:** Regularização tardia
**Data da decisão efetiva:** [data em que foi aplicada]
**Data da formalização:** [data de emissão da ADR]
**Motivo da tardança:** [ex: "priorização de entrega do M1 sobre documentação"]
**Lição aprendida:** [ação preventiva para evitar recorrência]
~~~

**Trade-off declarado:** Aceita-se a ADR tardia como mal menor em relação à ausência total de registro, mas desincentiva-se sua recorrência. Se > 30% das ADRs do projeto forem tardias, o GP deve revisar o fluxo de trabalho na Retrospectiva.

---

## 3. Arquitetura de Integração Documental

### 3.1 Princípio Diretor

> **Documentos de governança são standalone; planos de área são coordenados; cross-references substituem duplicação.**

Este princípio deriva do GMV e do Domínio de Trabalho do Projeto (PMBOK 7ª): cada artefato tem **uma única localização canônica** (SSOT informacional), e os demais artefatos **referenciam** essa localização sem copiar conteúdo.

### 3.2 Estrutura de Diretórios no Repositório

~~~
/docs/
├── planos/
│   ├── plano-integracao.md        ← Coordenador (referencia todos os demais)
│   ├── plano-escopo.md
│   ├── plano-cronograma.md
│   ├── plano-custos.md
│   ├── plano-qualidade.md
│   ├── plano-recursos.md          ← M2
│   ├── plano-comunicacoes.md      ← M2
│   └── plano-riscos.md            ← M2
├── decisoes/
│   ├── ADR-001-stack.md
│   ├── ADR-002-kanban.md
│   ├── ADR-003-metricas.md
│   ├── ADR-004-tasklists.md
│   └── ADR-005-[futura].md
├── conhecimento/
│   ├── OKB.md                     ← Operational Knowledge Base
│   ├── glossario.md               ← Glossário
│   └── licoes-aprendidas/
│       ├── MF1-licoes.md
│       ├── MF2-licoes.md
│       └── MF3-licoes.md
├── metricas/
│   └── baseline.md                ← Pós-calibração (03/10)
└── requisitos/
    └── requisitos.md              ← REQ-01 a REQ-15 (consolidados)
~~~

### 3.3 Estratégia de Integração: Cross-Reference vs. Anexo vs. Seção

| Documento | Estratégia | Justificativa GMV |
|-----------|-----------|-------------------|
| **ADRs** | **Standalone** em `/docs/decisoes/` + tabela-resumo no Plano de Integração | ADRs são autocontidas; duplicá-las nos planos violaria SSOT e inflaria extensão |
| **OKB** | **Standalone** em `/docs/conhecimento/OKB.md` + referência no Plano de Integração §1.1 | OKB é documento de governança transversal; não pertence a uma área específica |
| **Glossário** | **Standalone** em `/docs/conhecimento/glossario.md` + referência no Plano de Integração §1.1 | Mesmo princípio; glossário é infraestrutura linguística do projeto |
| **Lições Aprendidas** | **Standalone** em `/docs/conhecimento/licoes-aprendidas/` + resumo no encerramento de cada MF | Acumulação temporal; não faz sentido embutir em planos |
| **Baseline de Métricas** | **Standalone** em `/docs/metricas/baseline.md` + referência no Plano de Cronograma §2.3 | Dado empírico; não é texto normativo |

### 3.4 O que NÃO Fazer (Anti-Padrões)

| Anti-Padrão | Por que viola GMV | Ação Correta |
|-------------|-------------------|--------------|
| Copiar o texto integral da ADR-003 dentro do Plano de Cronograma | Duplicação; se a ADR for atualizada, o plano fica desatualizado | Referenciar: *"Conforme ADR-003 (/docs/decisoes/ADR-003-metricas.md)"* |
| Criar uma seção "Anexos" no final de cada plano com todos os documentos externos | Infla extensão; viola limite de 4 páginas (GMV) | Cross-reference inline |
| Embutir o Glossário como seção do Plano de Integração | Glossário é transversal a todos os planos; não pertence a um só | Standalone + referência |
| Criar um "Super-Documento" que contém TAP + todos os planos + ADRs + Glossário | Viola SSOT; impossibilita versionamento granular | Documentos separados, coordenados pelo Plano de Integração |

### 3.5 Mecanismo de Cross-Reference (Padrão Canônico)

Em qualquer plano de área, quando for necessário referenciar um documento externo, usa-se o seguinte formato:

~~~markdown
Conforme [ADR-003 — Métricas de Fluxo](/docs/decisoes/ADR-003-metricas.md), 
as métricas EVM são declaradas LEGADO.

Conforme [OKB v3.0 §1.4 — Estratégia de Entrega Faseada](/docs/conhecimento/OKB.md#14), 
o M1 contempla 5 planos.

Conforme [Glossário — Termo "CFD"](/docs/conhecimento/glossario.md#4-metodologia-ágil--kanban), 
o Cumulative Flow Diagram é a visualização gráfica do fluxo acumulado.
~~~

### 3.6 Tabela-Resumo no Plano de Integração (Seção 1.1 — Adendo Proposto)

Para que o Prof. Dr. Nivaldo Carleto tenha visibilidade integral sem abrir cada documento, o Plano de Integração deve conter uma **tabela-índice** na seção 1.1 ou como adendo à seção 1.4:

~~~markdown
### 1.4.1 Índice de Documentos de Governança Transversal

| Documento | Localização | Função | Última Versão |
|-----------|-------------|--------|---------------|
| OKB | /docs/conhecimento/OKB.md | Base de conhecimento operacional | v3.0 |
| Glossário | /docs/conhecimento/glossario.md | Vocabulário padronizado | v2.2 |
| ADR-001 | /docs/decisoes/ADR-001-stack.md | Stack tecnológica FOSS | Aprovada |
| ADR-002 | /docs/decisoes/ADR-002-kanban.md | Kanban como método | Aprovada |
| ADR-003 | /docs/decisoes/ADR-003-metricas.md | Métricas de fluxo | Aprovada |
| ADR-004 | /docs/decisoes/ADR-004-tasklists.md | Tasklists Markdown | Aprovada |
| Baseline | /docs/metricas/baseline.md | Dados empíricos de fluxo | ⏳ Pós 03/10 |
| Lições MF1 | /docs/conhecimento/licoes-aprendidas/MF1.md | Aprendizados da Fundação | ⏳ 30/09 |
~~~

---

## 4. Ciclo de Vida da ADR no Fluxo Kanban

### 4.1 Integração com o GitHub Projects

| Evento Kanban | Ação sobre ADR |
|---------------|----------------|
| Card com label `change-request` aprovado pelo CCB | Se a mudança atende ≥ 2 gatilhos → criar card de ADR |
| Card de ADR criado | Tipo: `docs` · Área: `area:integracao` · Macro-fase: vigente |
| ADR em `In Progress` | GP redige (estimativa ≤ 2h por ADR) |
| ADR em `Code Review` | Revisão por 1 par (Fabricio ou Edson) |
| ADR em `Done` | Commit `docs(adr): ADR-0XX — [título]` + atualização da tabela no OKB §4 |

### 4.2 Limite de ADRs por Marco (GMV)

| Marco | Máximo de ADRs novas | Justificativa |
|-------|----------------------|---------------|
| M1 (22/09) | 4 (já emitidas: 001–004) | Fundação completa; não adicionar mais |
| M2 (30/09) | ≤ 2 | Ex: ADR de baseline de métricas + eventual ajuste de stack |
| M3 (15/11) | ≤ 3 | Ex: padrão de API, estratégia de teste, fallback de API externa |
| M4 (15/12) | ≤ 1 | Ex: decisão de licenciamento final |

**Total projetado:** ≤ 10 ADRs ao longo do ciclo de vida. Acima disso, o GP deve questionar se o projeto está burocratizando decisões menores.

---

## 5. Síntese e Verificação de Congruência

| Item | Status |
|------|--------|
| Gatilhos de criação definidos (4 critérios, mínimo 2) | ✅ |
| Gatilhos negativos definidos (quando NÃO criar) | ✅ |
| Política de ADR tardia com trade-offs declarados | ✅ |
| Estrutura de ADR tardia com campos obrigatórios | ✅ |
| Arquitetura de integração documental definida | ✅ |
| Estratégia: standalone + cross-reference (não anexo, não duplicação) | ✅ |
| Tabela-índice no Plano de Integração proposta | ✅ |
| Limite de ADRs por marco (GMV) definido | ✅ |
| Integração com fluxo Kanban (GitHub Projects) definida | ✅ |
| Domínio PMBOK 7ª citado em cada seção | ✅ |
| Prof. Dr. Nivaldo Carleto por extenso | ✅ |
| Princípio GMV respeitado em todas as decisões | ✅ |
| Obsolescência PMBOK 6ª mantida (dicionário apenas) | ✅ |

---

**Decisão final do GP:** Esta política entra em vigor imediatamente. A próxima ADR (ADR-005, se necessária) deve seguir integralmente os critérios aqui definidos. A tabela-índice (§1.4.1) será incorporada ao Plano de Integração na próxima revisão (v1.1), antes do M2.

**Ação imediata:** Nenhuma. As 4 ADRs existentes estão conformes. A política documentada nesta resposta será versionada como seção do OKB v3.1 ou como adendo ao Plano de Integração §1.5.2, conforme decisão no Refinement de 23/09.

# Documento Consolidado — Projeto COGME
## Redação Integral do Projeto (Integração → Qualidade) + Notas de Revisão Consolidadas

> **Nota de normalização do GP:** na instrução de sequenciamento, o item "4 Integração" foi interpretado como erro material de digitação, uma vez que o documento-base contém a **Seção 4 — Custos** (não uma segunda Integração). A sequência aplicada é, portanto: **1 Integração → 2 Escopo → 3 Cronograma → 4 Custos → 5 Qualidade**, exatamente como constam das Partes B do arquivo-fonte. Nenhuma alteração de conteúdo foi realizada nas seções B — apenas normalização de títulos, cabeçalhos e substituição de diagramas por placeholders.

---
---

# PARTE I — NOTAS DE REVISÃO CONSOLIDADAS

> Esta seção aglutina todas as análises críticas, achados, propostas, soluções, registros de diagramas e checklists de validação produzidos nas rodadas de revisão (Rodadas de refinamento das Seções 1 a 5). O objetivo é manter a **Parte II (Redação Integral)** limpa e contínua, preservando aqui a trilha de auditoria completa.

---

## NR-1 — Auditoria da Seção 1 (Integração): v1.0 → v2.0

Auditoria cruzada da Seção 1 v1.0 contra a base documental vigente (TAP, OKB, Glossário, ADRs 001–004, Plano de Escopo v0.2). 6 achados, sendo 3 críticos para esta seção e 3 externos (sinalizados para saneamento nos artefatos de origem, sem bloquear a redação).

### NR-1.1 — Achados Críticos (bloqueantes para a Seção 1)

| # | Achado | Localização na v1.0 | Conflito | Solução Ótima |
| --- | --- | --- | --- | --- |
| C1 | Plano assume 8 planos simultâneos no M1 ("sete planos subsequentes", "8 planos v0.1" no critério MF1) | §1.1, §1.4, §1.8.1 | OKB §1.4 instituiu entrega faseada: M1 = 5 planos (Áreas 1–5); M2 = 3 planos (Áreas 6–8), como tailoring da Abordagem de Desenvolvimento | Reescrever §1.1; criar §1.4.1 (Estratégia de Entrega Faseada); corrigir critério MF1 em §1.8.1 |
| C2 | ADR-004 ausente (tasklists Markdown; rejeição formal de subissues) | §1.5 | Decisão emitida em 20/09 afeta diretamente a gestão do trabalho e o gate de fluxo | Incorporar regra de tasklist em §1.3.2 (regra de fluxo) e §1.5.1, sem duplicar o DoD (pertence ao Escopo §2.6) |
| C3 | Infraestrutura operacional GitHub ausente (5 milestones, sistema de 27 labels, padrão de cards ubíquos A/B, prioridade temporal P0–P3) | §1.3, §1.5 | OKB §9 formalizou estes elementos como mecanismos de integração e medição | Criar §1.3.3 (Milestones e Identificação de Cards); reforçar §1.5.1 com padrão de redação — sem replicar a taxonomia de 27 labels (pertence à configuração do repositório; citar apenas a regra operacional) |

### NR-1.2 — Achados Externos (não bloqueiam a Seção 1; reportar ao GP)

| # | Achado | Artefato | Severidade | Proposta |
| --- | --- | --- | --- | --- |
| C4 | TAP §3 (Métricas) define Cycle Time como "do 'To Do' ao 'Done'" — coluna inexistente no fluxo da ADR-002 (entrada = Ready); ADR-003 define "In Progress → Done" | TAP | MÉDIA | Plano adota a definição operacional da ADR-003. Propor correção cosmética no TAP: "To Do" → "In Progress" na próxima revisão |
| C5 | Glossário, linha "Stakeholder": "Prof. Nivaldo (avaliador)" — viola convenção de nome completo | Glossário | BAIXA | Corrigir para "Prof. Dr. Nivaldo Carleto" na próxima revisão do Glossário |
| C6 | Matriz de rastreabilidade do TAP §5 mantém cabeçalho "Fases EAP v2.0 Associadas" — viola a regra de supressão de versões internas | TAP | BAIXA | Find & replace: "EAP v2.0" → "EAP" |

### NR-1.3 — Auditoria de Invasão de Escopo entre Áreas (Seção 1)

| Conteúdo | Tentação de inclusão | Decisão | Justificativa |
| --- | --- | --- | --- |
| Definição formal do CFD | Replicar em Cronograma/Comunicações | Mantida aqui (§1.6.1) como referência canônica | OKB §8.2 designa Integração §1.6.1 como definição formal; os demais planos apenas referenciam |
| DoR/DoD detalhado | Duplicar critérios | Excluído — apenas referenciado | Pertence ao Plano de Escopo §2.6 (incluindo o item 8 da ADR-004) |
| Taxonomia das 27 labels | Replicar tabela completa | Excluída — citada apenas a regra "mínimo 3 tags" | Configuração do repositório; duplicação violaria GMV |
| Decomposição da EAP | Reproduzir fases/pacotes | Excluída — referenciada ao TAP §4 | Pertence ao Plano de Escopo §2.5 |
| RACI, Ishikawa, Matriz P×I, Roadmap de marcos detalhado | — | Excluídos | Recursos, Qualidade, Riscos e Cronograma, respectivamente |
| Diagramas | Incluir Gantt/EAP/Ishikawa nesta seção | Excluídos — ver Registro de Diagramas | Somente 4 diagramas com necessidade real e pertencentes ao domínio da Integração |

### NR-1.4 — Registro de Diagramas da Seção 1 (4 inserções; rejeições justificadas)

| ID | Seção | Diagrama | Formato sugerido | Necessidade |
| --- | --- | --- | --- | --- |
| FIG-1 | 1.2 | Modelo de Governança Híbrida Trifásico | Mermaid/PlantUML | Alta — núcleo da blindagem acadêmica |
| FIG-2 | 1.3.1 | Fluxo Kanban com gates e WIP limits | Mermaid flowchart LR | Alta — diagrama operacional central |
| FIG-3 | 1.6.1 | CFD saudável vs. CFD com gargalo | PNG/SVG (dados simulados) | Alta — defesa formal da ausência de Gantt/EVM |
| FIG-4 | 1.7.2 | Fluxo de Controle de Mudanças | Mermaid flowchart TD | Alta — mecanismo mais auditado em avaliação PMBOK |

Diagramas deliberadamente EXCLUÍDOS da Seção 1 (anti-invasão de escopo): Roadmap de marcos (→ Cronograma), EAP gráfica (→ Escopo), Ishikawa 6M (→ Qualidade), Matriz RACI (→ Recursos), Matriz P×I de riscos (→ Riscos), arquitetura da solução (→ N3.1).

### NR-1.5 — Checklist de Validação da Seção 1 (v2.0)

- [X] C1 resolvido: entrega faseada incorporada (§1.1, §1.4.1, §1.8.1) — M1 = 5 planos; M2 = 3 planos
- [X] C2 resolvido: ADR-004 incorporada (§1.3.2, §1.5.1) sem duplicar o DoD (Escopo §2.6)
- [X] C3 resolvido: milestones, labels e cards ubíquos incorporados (§1.3.3) sem replicar taxonomia
- [X] C4–C6 sinalizados ao GP (correções cosméticas em TAP e Glossário — não bloqueantes)
- [X] Acrônimos sem versões internas (TAP, EAP, OKB referida apenas como "base de conhecimento operacional")
- [X] "Prof. Dr. Nivaldo Carleto" sempre por extenso
- [X] CCB = GP (membro único); M4 = validação acadêmica
- [X] EVM declarado LEGADO; obsolescência PMBOK 6ª formal
- [X] Hierarquia normativa explícita (TAP > base operacional > Glossário > ADRs)
- [X] Zero invasão de escopo: CFD canônico aqui; DoR/DoD, EAP, RACI, Ishikawa apenas referenciados
- [X] 4 pontos de diagrama com especificação de conteúdo; 6 rejeições justificadas
- [X] Numeração hierárquica mantida; extensão dentro do limite GMV

**Status:** v2.0 pronta para revisão em pares (Fabricio + Edson) e fechamento definitivo. Pendências externas C4–C6 transferidas ao GP para saneamento nos artefatos de origem.

---

## NR-2 — Auditoria da Seção 2 (Escopo): Rodada 7 → v1.1

### NR-2.1 — Resoluções Aplicadas (decisões do GP → v1.1)

| Achado | Decisão do GP | Aplicação na redação |
| --- | --- | --- |
| C1 (contagem EAP) | Linha de base do TAP (12 fases + 37 pacotes) é canônica; não cabe CR. O Glossário é artefato terminológico volátil, atualizado a cada rodada de planos; a contagem "13/48" ali registrada não corresponde à baseline aprovada. TAP e Plano de Integração são canônicos | §2.5: nota de CR-001 removida e substituída por Nota de Canonicidade; §2.7: ressalva removida. Baseline fixada em 12/37 sem condicional |
| C2 (stack SDD) | Stack em avaliação; ADR-001 poderá sofrer atualizações de impacto relevante. Agregar a stack canônica local (em vez de exclusivamente QwenStudio). Inclusão/exclusão/troca de ferramentas exigirá ADRs específicas | §2.3.4 reescrito: stack local canônica nomeada (llama.cpp + Qwen 32B + OpenCode); ADR-001 declarada em avaliação; regra de ADR específica para mudanças de stack vinculada à política de ADRs |
| C3 (DoD/Padrões) | Correção pertence ao Plano de Escopo §2.6 (Integração v2.0 confirmada coerente) | §2.6: item 8 do DoD mantido e reforçado com nota de canonicidade + Padrões A/B (OKB §9.3); Tabela 2 expandida com as duas linhas de rastreabilidade cruzada propostas |

Achados externos remanescentes (reporte ao GP, não bloqueiam): grafia do stakeholder no Glossário ("Carleto" → corrigir para "Carleto", grafia do TAP); Cycle Time "To Do → Done" no Glossário (alinhar a "In Progress → Done", ADR-003); cabeçalho "Fases EAP v2.0" na matriz do TAP §5 (find & replace); item 10 da estrutura documental do Glossário (Plano de Gestão de Mudanças atendido pela Integração §1.7 — GMV).

Micro-ajuste opcional na Integração §1.3.2 (reforço de rastreabilidade do DoD): permanece aguardando aprovação do GP, fora do escopo desta redação.

### NR-2.2 — Registro de Diagramas e Rejeições Justificadas (Seção 2)

| ID | Seção | Diagrama | Formato | Necessidade |
| --- | --- | --- | --- | --- |
| FIG-1 | 2.5 | EAP — visão executiva (12 fases × 3 macro-fases) | Mermaid flowchart TB / PlantUML | Alta — artefato nuclear do processo 5.4; preenche slot vazio do TAP §4 |
| FIG-2 | 2.5 | Cadeia de decomposição EAP → card → tasklist com gates DoR/DoD | Mermaid flowchart LR | Alta — materializa ADR-004 + PMBOK 6ª §6.2 |

Rejeições justificadas: UML completo (§2.4.3.a); DER (§2.4.3.b, fase N3.3); CFD (canônico na Integração §1.6.1); Gantt/EVM (LEGADO, ADR-003); Ishikawa 6M (Qualidade); RACI (Recursos); Matriz P×I (Riscos); grafo de rastreabilidade (Tabela 2 suffice); gráfico MoSCoW (texto suffice).

### NR-2.3 — Checklist de Validação da Seção 2 (v1.1)

| Item | Status |
| --- | --- |
| C1 resolvido: baseline TAP (12 fases + 37 pacotes) afirmada como canônica; Nota de Canonicidade registra natureza volátil do Glossário; sem CR | ✅ OK |
| C2 resolvido: stack SDD local canônica nomeada; ADR-001 em avaliação; regra de ADR específica para inclusão/exclusão/troca de ferramentas (§2.3.4 + §2.8) | ✅ OK |
| C3 resolvido: DoD item 8 mantido; nota de canonicidade do gate de tasklist; Padrões A/B referenciados; rastreabilidade cruzada na Tabela 2 | ✅ OK |
| Micro-ajuste opcional na Integração §1.3.2 | ⏳ Aguardando GP (fora deste documento) |
| Achados externos remanescentes reportados | ✅ Reportados |
| P9, Atividades Derivadas (PMBOK 6ª §6.2), ADR-004 e Padrões A/B incorporados | ✅ OK |
| Figuras 1 e 2 com especificação de conteúdo; 9 rejeições justificadas | ✅ OK |
| ABNT: títulos e fontes de tabelas/figuras; prosa contínua; alíneas; numeração progressiva | ✅ OK |
| Sem versões internas de artefatos; "Prof. Dr. Nivaldo Carleto" por extenso | ✅ OK |
| Zero invasão de escopo entre áreas | ✅ OK |
| Extensão do corpo dentro do limite GMV (≈ 4 páginas) | ✅ OK |

**Status:** v1.1 emitida — pronta para revisão em pares e fechamento definitivo da seção. Pendência única: deliberação do GP sobre o micro-ajuste opcional na Integração §1.3.2.

---

## NR-3 — Auditoria da Seção 3 (Cronograma): Rodada 10 — Diretriz D3 (Freeze do TAP) → v1.2

### NR-3.1 — Diretriz do GP aplicada (D3 — Freeze do TAP)

| Diretriz | Aplicação na v1.2 |
| --- | --- |
| D3.1 — Precedência intra-TAP: em qualquer incongruência no corpo do TAP, a seção §6 Marcos é canônica | Regra formalizada na NC-00; NC-01 assimila o SMART de Cronograma à luz do §6, sem citar correção |
| D3.2 — TAP em estado de freeze: documento fechado antes do início do planejamento; não se cita, não se planeja e não se registra correção, revisão ou saneamento do TAP | Toda menção a "rewording/revisão do TAP" foi suprimida da v1.1; o registro de saneamento agora se restringe a artefatos vivos (OKB, Glossário, ADRs, Integração) |
| D3.3 — Notas consistentes para entendimento do contexto: divergências são tratadas exclusivamente como Notas de Contexto neste documento de Planejamento | §3.8 renomeada para "Notas de Contexto e Registro de Saneamento dos Artefatos Vivos"; framework NC redefinido (NC-00 a NC-06 + tabela de entendimentos do TAP congelado) |

### NR-3.2 — Fundamentação do freeze (anti-hallucination: fontes verificáveis)

| Fonte | Evidência |
| --- | --- |
| TAP — Controle de Versões | Última versão (18/09/2026) precede todos os planos de gerenciamento (19–21/09); nenhuma revisão posterior ao início do planejamento |
| Premissa P9 (TAP §9 / Escopo §2.1) | Separação ontológica TAP ≠ EAP ≠ PDCA |
| Glossário §11 (Separação Ontológica) | "TAP: autorização + base de referência — NÃO integra EAP, NÃO tem PDCA… não é objeto de gerenciamento" |
| PMBOK® 6ª §4.1 (dicionário) | Termo de abertura como documento de autorização, emitido na iniciação |

### NR-3.3 — Achados da rodada sobre a v1.1 (todos sanados na v1.2)

| # | Achado na v1.1 | Sev. | Solução aplicada |
| --- | --- | --- | --- |
| N1 | NC-00 declarava precedência "para fins de correções" sobre o TAP — conflita com D3.2 | ALTA | NC-00 reescrita: o plano é o locus vivo da leitura operacional do TAP congelado; divergência nunca é correção |
| N2 | Registro de saneamento listava 4 itens do TAP como pendentes de "próxima revisão" — viola o freeze | ALTA | Itens do TAP movidos para tabela "Entendimentos sobre o TAP congelado" (notas de contexto, sem saneamento) |
| N3 | NC-01 encerrava com "saneamento diferido do TAP §3" | MÉDIA | Suprimido; redigido como assimilação do SMART à luz do §6 |
| N4 | Regra de precedência intra-TAP (§6) não estava formalizada | MÉDIA | Formalizada na NC-00, item (i) |
| N5 | Objeto da ADR-005 ("precedência para correções") tornou-se obsoleto frente ao freeze | MÉDIA | ADR-005 redefinida: regime de freeze + precedência do §6 + Notas de Contexto; emissão mantida antes do M2 (Aditivo §4.2) |
| N6 | Abertura do plano citava "cláusula de precedência normativa para correções" | BAIXA | Substituída por "regime de freeze e Notas de Contexto (§3.8)" |

Invasão de escopo entre áreas: inalterada (CFD, DoR/DoD, P0–P3 e EAP apenas referenciados). Nenhum achado bloqueante.

### NR-3.4 — Registro de Diagramas da Seção 3 (2 inserções, 5 rejeições)

| ID | Seção | Diagrama | Formato | Necessidade |
| --- | --- | --- | --- | --- |
| FIG-1 | 3.4 | Sequenciamento macro + caminho crítico empírico | Mermaid flowchart LR | Alta — substitui visualmente a rede CPM rejeitada |
| FIG-2 | 3.6 | Roadmap macro (MF1–MF3 + 5 milestones) | Mermaid gantt / timeline | Alta — visualização temporal mínima do avaliador |

Rejeições justificadas: Gantt operacional e rede CPM (LEGADO — ADR-003, OKB §8.1); Gantt ProjectLibre (somente sob exigência formal do avaliador); CFD detalhado (canônico na Integração §1.6.1); burnup por card (GMV — nativo do GitHub Insights); histograma de recursos (pertence ao Plano de Recursos, M2).

### NR-3.5 — Checklist de Validação da Seção 3 (v1.2)

| Item | Status |
| --- | --- |
| Diretriz D3.1: precedência intra-TAP da seção §6 formalizada (NC-00, item i) | ✅ OK |
| Diretriz D3.2: zero ocorrências de "correção", "revisão", "rewording" ou "saneamento" aplicadas ao TAP em todo o corpo | ✅ OK |
| Diretriz D3.3: divergências tratadas exclusivamente como Notas de Contexto (§3.8) | ✅ OK |
| Freeze fundamentado em fontes verificáveis | ✅ OK |
| NC-01 assimilou o SMART de Cronograma à luz do §6 sem alterar datas nem citar correção | ✅ OK |
| Registro de saneamento restrito a artefatos vivos | ✅ OK |
| ADR-005 redefinida (regime de freeze + precedência §6 + Notas de Contexto); emissão antes do M2 | ⏳ Encaminhada |
| Datas M1–M4 + Calibração idênticas ao TAP §6, OKB §9.2 e Integração §1.3.3 | ✅ OK |
| EVM, Gantt operacional e CPM declarados LEGADO; sprints NÃO utilizadas | ✅ OK |
| EAP citada como 12 fases + 37 pacotes (baseline canônica do TAP §4) | ✅ OK |
| "Prof. Dr. Nivaldo Carleto" por extenso; sem versões internas de artefatos no corpo | ✅ OK |
| Zero invasão de escopo entre áreas | ✅ OK |
| 2 diagramas especificados; 5 rejeições justificadas; extensão dentro do limite GMV | ✅ OK |

**Status:** v1.2 reconstituída — pronta para revisão em pares e submissão no M1. O TAP permanece intocado como referência autorizativa congelada; toda leitura operacional divergente reside, de forma auditável, nas Notas de Contexto deste plano. Próxima ação recomendada ao GP: emitir ADR-005 (regime de freeze) antes do M2; área seguinte sugerida: 4 Custos.

---

## NR-4 — Auditoria da Seção 4 (Custos): Consolidação → v1.2

### NR-4.1 — Síntese da Integração Documental

Aglutinação das duas redações (anterior + nova) aplicando as soluções ótimas dos achados M1–M4 e B1–B3, mantendo coerência com TAP v3 congelado, OKB v3.0 + Aditivo, Glossário v3.1, Integração v2.0, Escopo v1.1, Cronograma v1.2 e ADRs 001–004.

Princípios aplicados:
- **Não duplicação:** Todo conteúdo válido da redação anterior é preservado, exceto onde há conflito direto com achados críticos/médios
- **Rastreabilidade ampliada:** N1.4 (Política de Licenciamento) adicionada como fonte canônica junto a N4.4 (Auditoria)
- **Whitelist completa:** PSF e Public Domain incorporados (ADR-001)
- **Fronteiras delimitadas:** Nota de delimitação com Qualidade inserida
- **P9 na abertura:** Consistência com Cronograma v1.2
- **FIG-2 reclassificada:** De "opcional" para "excluída" com justificativa GMV
- **NC-C2 aprimorada:** Reconciliação entre gatilho preventivo (5%) e fracasso formal (30%)

Nenhuma inconsistência residual. Redação formal consolidada v1.2.

### NR-4.2 — Registro de Diagramas da Seção 4

| ID | Seção | Diagrama | Necessidade | Status |
| --- | --- | --- | --- | --- |
| FIG-1 | 4.2 | Fluxo de Prevenção de Custos | Alta — materializa governança de custo zero | ✅ Obrigatório |
| FIG-2 | 4.4 | Dashboard de Conformidade FOSS | Excluída — GitHub Dependency Graph fornece nativamente; GMV | ❌ Excluída |
| FIG-3 | 4.5.2 | Matriz de Rastreabilidade de Dependências | Alta — evidência auditável para avaliador | ✅ Obrigatório |

Diagramas deliberadamente EXCLUÍDOS (anti-invasão de escopo + GMV):
- Curva S de custos (inaplicável — orçamento zero)
- Gráfico de EVM (CPI, SPI, VAC) — declarado LEGADO na ADR-003 e Integração §1.6.2
- Histograma de alocação de recursos — pertence ao Plano de Recursos (M2)
- Estrutura de detalhamento de custos — inaplicável (sem custos para detalhar)

### NR-4.3 — Checklist de Validação da Seção 4 (v1.2)

| Item | Status |
| --- | --- |
| Linha de base R$ 0,00 declarada e imutável | ✅ OK |
| EVM declarado inaplicável (AC = 0) com referência à ADR-003 | ✅ OK |
| Métricas de substituição definidas (conformidade FOSS) | ✅ OK |
| Whitelist/blacklist de licenças explícita com PSF e Public Domain | ✅ OK |
| N1.4 e N4.4 referenciadas como fontes canônicas | ✅ OK |
| Delimitação de fronteiras com Qualidade (Área 5) inserida | ✅ OK |
| P9 (separação ontológica) incluída na abertura | ✅ OK |
| FIG-2 reclassificada: "excluída" com justificativa GMV | ✅ OK |
| NC-C2 aprimorada: reconciliação 5% vs 30% | ✅ OK |
| Gatilhos de mudança alinhados à Integração §1.7 | ✅ OK |
| NC-C1 a NC-C4 registradas | ✅ OK |
| Rastreabilidade 100% das seções ao TAP | ✅ OK |
| "Prof. Dr. Nivaldo Carleto" por extenso | ✅ OK |
| Zero invasão de escopo (N1.4/N4.4 referenciadas, não duplicadas; Qualidade delimitada) | ✅ OK |
| ADR-003 referenciada como fundamento de rejeição de EVM | ✅ OK |
| ADR-001 referenciada como fonte da stack | ✅ OK |
| CCB com fonte TAP v3 §1.c | ✅ OK |
| Extensão dentro do limite GMV (≈ 4 páginas) | ✅ OK |
| 2 diagramas obrigatórios especificados; 1 exclusão justificada | ✅ OK |
| Diretriz D3 (freeze do TAP) formalizada em NC-C4 | ✅ OK |
| Tabela de abordagem expandida com coluna "Fonte Canônica" | ✅ OK |
| Seção 4.8 reestruturada com distinção alerta preventivo / fracasso formal | ✅ OK |
| Texto não aderente removido; organização definitiva | ✅ OK |

**Status:** v1.2 emitida — pronta para submissão no M1 (22/09/2026). Próxima área sugerida: 5 Qualidade.

---

## NR-5 — Auditoria da Seção 5 (Qualidade): Rodada de Refinamento → v1.1

### NR-5.1 — Inconsistências Detectadas (Menores, Não-Bloqueantes)

| # | Inconsistência | Localização | Severidade | Solução |
| --- | --- | --- | --- | --- |
| I1 | PDCA-N10 menciona "scope creep > 15%" sem referenciar Escopo §2.7 | §5.6 PDCA-N10 | BAIXA | Adicionar referência cruzada |
| I2 | PDCA-N7 menciona "Pipeline lento (> 5min)" sem referenciar REQ-11 | §5.6 PDCA-N7 | BAIXA | Adicionar referência cruzada |
| I3 | Ishikawa-3 analisa Cycle Time (qualidade de processo), fronteira tênue com Cronograma §3.7 | §5.7 Ishikawa-3 | BAIXA | Reforçar delimitação na seção 5.8.2 |
| I4 | Seção 5.8.2 menciona CFD e Cycle Time sem definir fonte canônica | §5.8.2 | BAIXA | Adicionar referência à Integração §1.6.1 |

**Veredito:** Inconsistências menores, não-bloqueantes. A redação está estruturalmente consistente com TAP v3, OKB v3.0, Glossário v3.1, Integração v2.0, Escopo v1.1, Cronograma v1.2, Custos v1.2 e ADRs 001-004.

### NR-5.2 — Registro de Diagramas da Seção 5

| ID | Seção | Diagrama | Necessidade | Status |
| --- | --- | --- | --- | --- |
| FIG-1 | 5.2 | Fluxo de Garantia da Qualidade | Alta — materializa gates de qualidade sequenciais | ✅ SVG gerado |
| FIG-2 | 5.3 | Dashboard de Métricas | Excluída — GitHub Insights fornece nativamente; GMV | ❌ Excluída |
| FIG-3 | 5.7 | Ishikawa: Coverage < 80% | Alta — análise de causa-raiz para REQ-08 | ✅ SVG gerado |
| FIG-4 | 5.7 | Ishikawa: Defeitos Críticos UAT | Alta — análise de causa-raiz para REQ-09 | ✅ SVG gerado |
| FIG-5 | 5.7 | Ishikawa: Cycle Time > 3 dias | Alta — análise de causa-raiz para melhoria de processo | ✅ SVG gerado |

Diagramas deliberadamente EXCLUÍDOS (anti-invasão de escopo + GMV):
- Gráfico de controle estatístico (inaplicável — projeto acadêmico com n pequeno)
- Matriz de rastreabilidade completa (pertence ao Escopo; aqui apenas referenciada)
- Histograma de defeitos por módulo (GMV — nativo do GitHub Issues)
- Curva de aprendizado da equipe (pertence ao Plano de Recursos, M2)

### NR-5.3 — Checklist de Validação da Seção 5 (v1.1)

| Item | Status |
| --- | --- |
| 12 PDCAs consolidados (N1-N12), sem TAP (Premissa P9) | ✅ OK |
| PDCAs objetivos (máx. 6 linhas cada), sem bloat | ✅ OK |
| 3 diagramas Ishikawa 6M (coverage, UAT, cycle time) | ✅ OK |
| REQ-08, REQ-09, REQ-10 rastreáveis | ✅ OK |
| Meta de coverage ≥ 80% declarada e operacionalizada | ✅ OK |
| Fronteira com Custos §4.5 (auditoria FOSS) delimitada | ✅ OK |
| Fronteira com Cronograma §3.7 (CFD) delimitada | ✅ OK |
| Fronteira com Escopo §2.6 (DoR/DoD) delimitada | ✅ OK |
| FIG-1 (fluxo de qualidade) especificada | ✅ SVG gerado |
| FIG-2 excluída com justificativa GMV | ✅ OK |
| NC-Q1 a NC-Q5 (freeze do TAP, EAP 12 fases, grafia stakeholder) registradas | ✅ OK |
| "Prof. Dr. Nivaldo Carleto" por extenso | ✅ OK |
| Zero invasão de escopo entre áreas | ✅ OK |
| Extensão dentro do limite GMV (≈ 4 páginas) | ✅ OK |
| ADR-003 referenciada (EVM LEGADO) | ✅ OK |
| ADR-004 referenciada (tasklists) | ✅ OK |
| Diretriz D3 (freeze do TAP) formalizada em NC-Q1 | ✅ OK |
| Inconsistências I1-I6 sanadas | ✅ OK |
| 4 SVGs gerados (FIG-1, FIG-3, FIG-4, FIG-5) | ✅ OK |

**Status:** v1.1 emitida — pronta para submissão no M1 (22/09/2026). Próxima área sugerida: 6 Recursos (M2) ou 7 Comunicações (M2).

---

## NR-6 — Consolidação Final de Pendências Externas (transversal às 5 seções)

| Pendência | Artefato vivo | Momento previsto |
| --- | --- | --- |
| Numeração 6.3/6.5 no §8.1 | Base de conhecimento operacional §8.1 | Próxima revisão da base |
| "Processo 6.4 Estimar Custos" → 6.4 Estimar Durações (custos = 7.2) | Glossário §3 | Próxima revisão do Glossário |
| Grafia "Carleto" → "Carleto" | Glossário | Próxima revisão do Glossário |
| Cycle Time "To Do → Done" → "In Progress → Done" | Glossário | Próxima revisão do Glossário |
| Contagem EAP "13/48" → 12/37 (baseline do TAP §4) | Glossário §1 | Próxima revisão do Glossário |
| Convenção dupla de dias | ADR-003 / Glossário / baseline | Formalização da baseline (após 03/10) |
| Cláusula NC-00 na hierarquia formal + ADR-005 | Integração §1.4 / ADR-005 | Antes do M2 |
| Micro-ajuste opcional na Integração §1.3.2 (reforço rastreabilidade DoD) | Integração | Aguardando GP |

---
---

# PARTE II — REDAÇÃO INTEGRAL DO PROJETO

---

## SEÇÃO 0 — INTRODUÇÃO: TERMO DE ABERTURA E ESTRUTURA ANALÍTICA DO PROJETO

### 0.1 Identificação do Projeto

| Campo | Descrição |
| --- | --- |
| Projeto | COGME — Conversor de Ganhos em Moeda Estrangeira |
| Instituição | Fatec Taquaritinga — Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas |
| Disciplina | Gerência de Projetos |
| Gerente de Projeto | Leonardo David Silva Setti |
| Equipe | Leonardo David Silva Setti, Fabricio de Lima Cabral, Edson Luis Silva |
| Stakeholder-Avaliador | Prof. Dr. Nivaldo Carleto |
| Data de autorização do TAP | 18/09/2026 (versão 3 — regime de freeze) |

### 0.2 Objetivos Fundamentais do TAP

a) Autorizar formalmente o projeto "Conversor de Ganhos em Moeda Estrangeira" (COGME), conferindo-lhe existência oficial perante a instituição de ensino (Fatec Taquaritinga) e perante o professor orientador da disciplina de Gerência de Projetos, Prof. Dr. Nivaldo Carleto.

b) Conceder autoridade formal ao aluno Leonardo David Silva Setti, no papel de gerente do projeto, para aplicar os recursos organizacionais, planejar as atividades, tomar decisões e mobilizar os recursos necessários à execução do projeto, em conjunto com os demais membros da equipe.

c) Estabelecer o vínculo entre o projeto e os objetivos estratégicos da disciplina, demonstrando que o desenvolvimento deste sistema atende aos requisitos acadêmicos de aplicação prática dos conceitos de gerenciamento de projetos conforme o Guia PMBOK® 7ª edição (governança primária), com o Guia PMBOK® 6ª edição atuando como dicionário complementar de processos quando necessário, e a metodologia ágil Kanban como método de execução operacional via GitHub Projects.

d) Definir os limites preliminares do projeto, incluindo escopo de alto nível, premissas, restrições, riscos iniciais, cronograma de marcos e orçamento preliminar.

e) Identificar as principais partes interessadas (stakeholders) e seus papéis.

f) Servir como documento de referência ao longo de todo o ciclo de vida do projeto.

### 0.3 Situação Atual e Justificativa

O cenário econômico e laboral contemporâneo tem sido profundamente transformado pela consolidação do trabalho remoto e pela globalização dos contratos de prestação de serviços. No Brasil, um contingente crescente de profissionais de tecnologia, design, marketing e consultoria atua como Pessoa Jurídica (PJ) ou freelancer para empresas sediadas nos Estados Unidos, Europa e demais mercados que remuneram em moeda estrangeira (predominantemente USD e EUR).

Entretanto, a gestão financeira desses ganhos apresenta uma complexidade que as ferramentas atualmente disponíveis no mercado não resolvem de maneira integrada. Para obter uma estimativa confiável do valor que efetivamente receberá em moeda nacional, o profissional é forçado a consultar múltiplos sites, planilhas manuais e calculadoras dispersas. Esse processo é moroso, suscetível a erros de digitação e de interpretação de taxas, além de não oferecer uma visão consolidada e comparativa em tempo real das diferentes variáveis que impactam a conversão.

O projeto justifica-se pela lacuna prática existente no ecossistema de software atual: não há, até o momento, uma solução única, gratuita e de código aberto que reúna, em um mesmo ambiente, a simulação cambial completa, a comparação entre diferentes regimes de cálculo e a emissão de documentos fiscais/financeiros associados. A determinação de utilizar exclusivamente tecnologias open source é um valor fundante do projeto, sustentado pelos pilares de transparência e auditabilidade, gratuidade e acessibilidade, sustentabilidade e comunidade, e alinhamento institucional com a educação pública.

### 0.4 Estrutura Analítica do Projeto (EAP) — Texto Integral

#### NÍVEL 0 — RAIZ

| ID | Nó | Descrição | Macro-Fase |
| --- | --- | --- | --- |
| N0 | — | COGME — Conversor de Ganhos em Moeda Estrangeira | — |

#### NÍVEIS 1 E 2 — FASES OBRIGATÓRIAS (MVP Acadêmico)

| ID Nível 1 | Fase (Nível 1) | ID Nível 2 | Pacote de Trabalho (Nível 2) | Macro-Fase |
| --- | --- | --- | --- | --- |
| N1 | 1. Iniciação e Planejamento | N1.1 | 1.1. Identificação de Stakeholders | MF1 |
| | | N1.2 | 1.2. Planos de Gerenciamento | MF1 |
| | | N1.3 | 1.3. Plano da Qualidade | MF1 |
| | | N1.4 | 1.4. Política de Licenciamento FOSS | MF1 |
| | | N1.5 | 1.5. Definição do Backlog e Kanban | MF1 |
| N2 | 2. Levantamento de Requisitos | N2.1 | 2.1. Requisitos Funcionais | MF1 |
| | | N2.2 | 2.2. Requisitos Não Funcionais | MF1 |
| | | N2.3 | 2.3. Casos de Uso e Histórias de Usuário | MF1 |
| N3 | 3. Modelagem e Prototipação | N3.1 | 3.1. Arquitetura da Solução | MF1 |
| | | N3.2 | 3.2. Protótipo UX/UI | MF1 |
| | | N3.3 | 3.3. Modelagem de Dados (DER) | MF1 |
| N4 | 4. Configuração de Ambiente | N4.1 | 4.1. Seleção e Validação da Stack FOSS | MF1 |
| | | N4.2 | 4.2. Repositório Git + CI/CD | MF1 |
| | | N4.3 | 4.3. Setup Local e Homologação | MF1 |
| | | N4.4 | 4.4. Auditoria de Licenças | MF1 |
| N5 | 5. Desenvolvimento do Sistema | N5.1 | 5.1. Backend — Lógica de Negócio | MF2 |
| | | N5.2 | 5.2. Backend — API de Câmbio + Cache | MF2 |
| | | N5.3 | 5.3. Frontend — Interface e Simulações | MF2 |
| | | N5.4 | 5.4. Módulo PDF (WeasyPrint) | MF2 |
| | | N5.5 | 5.5. SDD com IA (Prompts + Revisão) | MF2 |
| N6 | 6. Garantia da Qualidade | N6.1 | 6.1. Testes Unitários/Integração (≥ 80%) | MF2 |
| | | N6.2 | 6.2. Testes de Aceitação (UAT) | MF2 |
| | | N6.3 | 6.3. Aplicação de Ferramentas da Qualidade (12 PDCAs + Ishikawa 6M) | MF2 |
| N7 | 7. DevOps e CI/CD | N7.1 | 7.1. Pipeline CI (lint + testes) | MF2 |
| N8 | 8. Comunicação | N8.1 | 8.1. Matriz de Comunicação (RACI) | MF1 |
| | | N8.2 | 8.2. Canais Oficiais (GitHub, e-mail) | MF1 |
| N9 | 9. Base de Conhecimento | N9.1 | 9.1. ADRs (decisões arquiteturais) | MF1 |
| | | N9.2 | 9.2. Lições Aprendidas Contínuas | MF1 |
| | | N9.3 | 9.3. Catálogo de Prompts SDD | MF1 |
| N10 | 10. Gestão de Mudanças | N10.1 | 10.1. Registro de Solicitações de Mudança | MF2 |
| | | N10.2 | 10.2. Label change-request no GitHub | MF2 |
| | | N10.3 | 10.3. Aprovação e Versionamento | MF2 |
| N11 | 11. Documentação do Projeto | N11.1 | 11.1. Documentação Técnica (Arquitetura, APIs) | MF3 |
| | | N11.2 | 11.2. Consolidação da Documentação Parcial | MF3 |
| N12 | 12. Encerramento | N12.1 | 12.1. Lições Aprendidas Finais | MF3 |
| | | N12.2 | 12.2. Verificação SMART | MF3 |
| | | N12.3 | 12.3. Apresentação Final + Aceite | MF3 |

**TOTAL: 12 fases Nível 1 + 37 pacotes Nível 2**

#### Lista Hierárquica Aninhada da EAP

~~~
N0: COGME — Conversor de Ganhos em Moeda Estrangeira
│
├── N1: 1. Iniciação e Planejamento [MF1]
│   ├── N1.1: 1.1. Identificação de Stakeholders
│   ├── N1.2: 1.2. Planos de Gerenciamento
│   ├── N1.3: 1.3. Plano da Qualidade
│   ├── N1.4: 1.4. Política de Licenciamento FOSS
│   └── N1.5: 1.5. Definição do Backlog e Kanban
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
├── N8: 8. Comunicação [MF1]
│   ├── N8.1: 8.1. Matriz de Comunicação (RACI)
│   └── N8.2: 8.2. Canais Oficiais (GitHub, e-mail)
│
├── N9: 9. Base de Conhecimento [MF1]
│   ├── N9.1: 9.1. ADRs (decisões arquiteturais)
│   ├── N9.2: 9.2. Lições Aprendidas Contínuas
│   └── N9.3: 9.3. Catálogo de Prompts SDD
│
├── N10: 10. Gestão de Mudanças [MF2]
│   ├── N10.1: 10.1. Registro de Solicitações de Mudança
│   ├── N10.2: 10.2. Label `change-request` no GitHub
│   └── N10.3: 10.3. Aprovação e Versionamento
│
├── N11: 11. Documentação do Projeto [MF3]
│   ├── N11.1: 11.1. Documentação Técnica (Arquitetura, APIs)
│   └── N11.2: 11.2. Consolidação da Documentação Parcial
│
└── N12: 12. Encerramento [MF3]
    ├── N12.1: 12.1. Lições Aprendidas Finais
    ├── N12.2: 12.2. Verificação SMART
    └── N12.3: 12.3. Apresentação Final + Aceite
~~~

> **[PLACEHOLDER — DIAGRAMA: Fig. 0.1 — EAP Visão Executiva (N0 + 12 fases × 3 macro-fases) | Seção 0.4 | Formato: Mermaid flowchart TB ou PlantUML WBS]**

### 0.5 Marcos do Projeto

| ID | Macro-Fase (EAP) | Descrição do Marco (Entrega de Valor) | Data Alvo | Critério de Aceite |
| --- | --- | --- | --- | --- |
| M1 | MF1: Fundação | Entrega Parcial Documental: Aprovação do TAP + Planos de Gerenciamento das Áreas 1 a 5 (Integração, Escopo, Cronograma, Custos, Qualidade) + 12 PDCAs consolidados + Diagrama de Ishikawa. | 22/09/2026 | Documentação submetida via GitHub e validada pelo Prof. Dr. Nivaldo Carleto sem achados críticos. |
| M2 | MF1: Fundação | Ambiente e Modelagem Concluídos: Stack FOSS definida e validada, ambiente local/CI configurado, DER e Protótipo UX/UI aprovados. | 30/09/2026 | Pipeline CI "verde" e artefatos de modelagem versionados no repositório. |
| M3 | MF2: Construção | MVP Funcional (Beta): Código-fonte full-stack operacional (Backend, Frontend, PDF, SDD com IA), com cobertura de testes ≥ 80% e validado em UAT local. | 15/11/2026 | Zero defeitos críticos/bloqueantes; métricas de fluxo dentro da baseline. |
| M4 | MF3: Consolidação | Encerramento e Aceite Final: Documentação técnica consolidada, lições aprendidas, verificação dos critérios SMART e apresentação final com aceite formal. | 15/12/2026 | Validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4 e repositório com tag de release final. |

### 0.6 Requisitos Principais das Entregas (TAP §5)

**Entrega Principal 1 — MVP Web Funcional (Fase N5)**

| ID | Requisito | Critério de Aceite | Rastreabilidade |
| --- | --- | --- | --- |
| REQ-01 | Simulação de conversão cambial em tempo real (USD/EUR → BRL) | Cotação obtida via API externa com latência ≤ 2s | TAP §3 (Produto) + N5.2 |
| REQ-02 | Suporte a 5 regimes de contratação (hora, dia, semana, mês, valor fixo) | 100% dos regimes operacionais em UAT | TAP §3 (Produto) + N5.1 |
| REQ-03 | Aplicação de encargos financeiros simulados (spread + IOF) | Cálculo auditável com precisão de 2 casas decimais | TAP §3 (Produto) + N5.1 |
| REQ-04 | Emissão de invoice em formato PDF | Geração via WeasyPrint em ≤ 3s por documento | TAP §3 (Produto) + N5.4 |
| REQ-05 | Tempo de resposta da aplicação | ≤ 3s em 95% das requisições (ambiente homologação) | TAP §3 (Produto — M) + N5.1 |
| REQ-06 | Interface web responsiva (FOSS) | Compatível com Chrome/Firefox/Edge (últimas 2 versões) | TAP §3 (Inovação) + N5.3 |
| REQ-07 | Cache de cotações (SQLite) | Redução de ≥ 50% das chamadas à API externa | Decisão arquitetural documentada + N5.2 |

**Entrega Principal 2 — Garantia da Qualidade (Fase N6)**

| ID | Requisito | Critério de Aceite | Rastreabilidade |
| --- | --- | --- | --- |
| REQ-08 | Cobertura de testes automatizados | ≥ 80% do código (unitários + integração via pytest + coverage.py) | TAP §3 (Qualidade) + N6.1 |
| REQ-09 | Testes de aceitação (UAT) | 100% dos fluxos críticos passing, zero defeitos críticos/bloqueantes | TAP §3 (Qualidade) + N6.2 |
| REQ-10 | Aplicação de ferramentas da qualidade (PDCA + Ishikawa 6M) | 12 PDCAs consolidados + diagrama de causa e efeito documentado no Plano de Qualidade | TAP §3 (Qualidade) + N6.3 |

**Entrega Principal 3 — DevOps e CI/CD (Fase N7)**

| ID | Requisito | Critério de Aceite | Rastreabilidade |
| --- | --- | --- | --- |
| REQ-11 | Pipeline CI funcional | Lint + testes rodando em ≤ 5 min por push | Padrão de integração contínua + N7.1 |

**Entrega Principal 4 — Base de Conhecimento (Fase N9)**

| ID | Requisito | Critério de Aceite | Rastreabilidade |
| --- | --- | --- | --- |
| REQ-12 | ADRs para decisões arquiteturais críticas | Mínimo 3 ADRs registrados (stack, Kanban, métricas) | Política de documentação técnica + N9.1 |
| REQ-13 | Rastreabilidade de prompts SDD | 100% dos prompts catalogados em .ai/handoffs/ | Política de rastreabilidade de prompts + N9.3 |

**Entrega Principal 5 — Documentação Técnica (Fase N11)**

| ID | Requisito | Critério de Aceite | Rastreabilidade |
| --- | --- | --- | --- |
| REQ-14 | Documentação técnica consolidada | Arquitetura + APIs (OpenAPI) revisadas e aprovadas | TAP §3 (Produto) + N11.1 |

**Entrega Principal 6 — Conformidade FOSS (Fases N1, N4)**

| ID | Requisito | Critério de Aceite | Rastreabilidade |
| --- | --- | --- | --- |
| REQ-15 | Licenciamento 100% FOSS | Todas dependências com licenças OSI-approved (MIT, Apache 2.0, BSD, GPL) | TAP §3 (Inovação) + N1.5 + N4.4 |

### 0.7 Premissas do TAP (§9)

| # | Premissa | Justificativa de Alto Nível |
| --- | --- | --- |
| P1 | Governança híbrida: PMBOK 7ª como base de princípios e domínios, PMBOK 6ª como dicionário complementar, Kanban como método de execução. | Alinhamento com as diretrizes acadêmicas da disciplina. |
| P2 | Projeto desenvolvido exclusivamente com tecnologias FOSS. | Premissa pedagógica e de valor social. |
| P3 | Uso de IA Generativa (LLMs) como apoio ao desenvolvimento (SDD) autorizado, com rastreabilidade e revisão humana. | Diretrizes acadêmicas atuais de uso ético de IA. |
| P4 | Código-fonte funcional (MVP full-stack) constitui deliverable formal. | Natureza prática do curso de ADS. |
| P5 | Equipe manterá disponibilidade média de até 20 horas semanais por membro. | Capacidade realística para projeto acadêmico noturno. |
| P6 | Hardware local adequado e suficiente para desenvolvimento, modelagem, testes e execução do MVP. | Condição base para desenvolvimento sem nuvem paga. |
| P7 | Professor Orientador atua como stakeholder-avaliador único nos marcos (M1 a M4), sem ingerência operacional. CCB delegada ao GP. | Simplificação pedagógica e autonomia do GP. |
| P8 | Áreas de "Aquisições" e "Gerenciamento das Partes Interessadas" tratadas com simplificação pedagógica. | Foco nas 8 áreas restantes. |
| P9 | Separação ontológica TAP ≠ EAP ≠ PDCA: o TAP autoriza, não integra a EAP nem é objeto de ciclos PDCA. | Preservação do status autorizativo do TAP. |

### 0.8 Restrições Consolidadas (TAP §8 + §11)

| Categoria PMBOK | Restrições Aplicáveis |
| --- | --- |
| Escopo | MVP acadêmico; desenvolvimento do zero |
| Cronograma | 2 bimestres (com ≈25% já decorrido); marco 22/09/2026; curso noturno |
| Custo | Orçamento zero; proibição de ferramentas pagas |
| Recursos | Equipe de 3 pessoas (múltiplos papéis); hardware modesto; dependência externa |
| Qualidade | Testes com tempo limitado; ambiente de validação restrito |
| Riscos | Sem plano de contingência formal; APIs gratuitas instáveis |
| Tecnológicas | FOSS/gratuito obrigatório; SDD experimental; licença open source final |

---

## SEÇÃO 1 — INTEGRAÇÃO

**Plano de Gerenciamento da Integração**

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira
Versão: 2.0
Data: 20/09/2026
Autores: Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

Este plano deriva diretamente das Premissas P1 (governança híbrida), P3 (SDD com LLM), P4 (código como deliverable) e P7 (stakeholder-avaliador único nos marcos), e das Restrições de Cronograma e Custo do TAP, respeitando o Domínio de Abordagem de Desenvolvimento e o Domínio de Trabalho do Projeto do PMBOK® 7ª edição.

### 1.1 Identificação e Propósito

Este Plano de Gerenciamento da Integração coordena a execução integrada do projeto COGME, garantindo que os sete planos de área subsequentes — quatro entregues no marco M1 (Escopo, Cronograma, Custos, Qualidade) e três diferidos para o marco M2 (Recursos, Comunicações, Riscos), conforme a estratégia de entrega faseada da seção 1.4.1 —, o código-fonte e os artefatos de governança permaneçam coerentes com os Objetivos SMART aprovados no TAP.

Função ontológica: O TAP autoriza; este plano coordena. Ele não duplica conteúdo do TAP — define os mecanismos de coerência entre todos os artefatos do ciclo de vida.

Domínio PMBOK 7ª: Abordagem de Desenvolvimento.
Processo PMBOK 6ª (dicionário, obsolescência assumida): 4.2 — Desenvolver o Plano de Gerenciamento do Projeto.

### 1.2 Modelo de Governança Híbrida

O projeto adota um modelo trifásico de governança, declarado no TAP (§1.c):

| Camada | Fonte Normativa | Função no COGME |
| --- | --- | --- |
| Governança primária | PMBOK® 7ª edição — 12 Princípios + 8 Domínios de Desempenho | Define por que e para quê; orienta decisões por valor |
| Dicionário complementar | PMBOK® 6ª edição — processos citados apenas para rastreabilidade acadêmica | Fornece vocabulário estrutural quando necessário |
| Método de execução | Manifesto Ágil (4 valores) + Kanban (fluxo contínuo) | Define como o trabalho é executado diariamente |

> **[PLACEHOLDER — DIAGRAMA: Fig. 1.1 — Modelo de Governança Híbrida Trifásico | Seção 1.2 | Conteúdo obrigatório: três camadas empilhadas (PMBOK 7ª no topo como governança primária; PMBOK 6ª como dicionário complementar com marcação de obsolescência; Kanban/Manifesto Ágil na base como execução), com setas descendentes de autoridade e seta lateral de realimentação (lições aprendidas). Formato sugerido: Mermaid flowchart TB ou PlantUML, versionado em /docs/diagrams/. Necessidade real: o conceito de hierarquia normativa é o núcleo da blindagem acadêmica do projeto.]**

#### 1.2.1 Hierarquia de Resolução de Conflitos

Em caso de conflito entre fontes normativas, aplica-se a seguinte ordem de precedência:

1. Valor entregue ao usuário final (Domínio de Entrega — PMBOK 7ª)
2. Ementa da disciplina + orientação do Prof. Dr. Nivaldo Carleto
3. PMBOK® 7ª edição (princípios e domínios)
4. Manifesto Ágil + Kanban (método de execução)
5. PMBOK® 6ª edição (dicionário de processos)

Trade-off declarado: Esta hierarquia favorece velocidade de entrega sobre completude documental, alinhada ao Princípio "Foco em Valor" (PMBOK 7ª) e ao Valor Ágil "Software funcionando sobre documentação abrangente".

#### 1.2.2 Papéis de Governança

| Papel | Titular | Responsabilidade |
| --- | --- | --- |
| Gerente de Projeto (GP) | Leonardo David Silva Setti | Decisor operacional único; CCB de membro único; autoridade para aprovações, rejeições e controle de mudanças |
| Desenvolvedores | Fabricio de Lima Cabral, Edson Luis Silva | Execução técnica; revisão em pares; self-report de carga horária |
| Stakeholder-Avaliador | Prof. Dr. Nivaldo Carleto | Avaliação acadêmica nos marcos M1–M4; sem ingerência em decisões operacionais |

#### 1.2.3 Governança Mínima Viável (GMV)

Todo artefato de governança deve justificar sua existência pelo teste GMV:

| Pergunta | Se SIM | Se NÃO |
| --- | --- | --- |
| O Prof. Dr. Nivaldo Carleto exigirá este artefato na avaliação? | Produzir completo | Simplificar ou eliminar |
| Este artefato evita retrabalho futuro? | Produzir | Avaliar custo-benefício |
| Este artefato é útil para a equipe (não apenas para avaliação)? | Produzir | Eliminar |

Se ≥ 2 respostas forem NÃO, o artefato é candidato a simplificação ou eliminação. Decisão final do GP.

#### 1.2.4 Obsolescência do PMBOK 6ª (Declaração Formal)

O PMBOK® 6ª edição (2017) é tratado exclusivamente como dicionário de processos. Processos preditivos são citados apenas para rastreabilidade acadêmica e blindagem terminológica. Métricas EVM (SPI/CPI) são declaradas LEGADO — NÃO APLICÁVEIS, substituídas por métricas de fluxo Kanban conforme ADR-003.

### 1.3 GitHub Projects como Fonte Única de Verdade (SSOT)

O repositório GitHub e seu módulo GitHub Projects constituem o artefato primário de integração, cronograma e monitoramento, conforme ADR-002. Esta decisão substitui qualquer ferramenta preditiva de planejamento como instrumento ativo.

Justificativa: Para uma equipe de 3 pessoas com fluxo contínuo, ferramentas preditivas impõem overhead de manutenção desproporcional ao valor gerado. O Kanban via GitHub Projects fornece visibilidade em tempo real, métricas nativas de fluxo e rastreabilidade automática via commits.

Domínio PMBOK 7ª: Medição + Trabalho do Projeto.
Valor Ágil: "Indivíduos e interações sobre processos e ferramentas."

#### 1.3.1 Mapeamento Kanban ↔ Processos PMBOK 6ª

| Coluna Kanban (ADR-002) | Processo PMBOK 6ª | Domínio PMBOK 7ª | Regra Operacional |
| --- | --- | --- | --- |
| Backlog | 5.2 Coletar Requisitos | Planejamento | Card criado com DoR pendente |
| Ready (DoR) | 4.3 Orientar Trabalho (preparação) | Trabalho | DoR atendido; aguardando capacidade |
| In Progress | 4.3 Orientar e Gerenciar Trabalho | Trabalho | WIP limit: máx. 3 cards/pessoa |
| Code Review | 4.5 Monitorar e Controlar | Medição | Revisão em pares obrigatória |
| Done (DoD) | 5.4 Criar EAP (aceite do pacote) | Entrega | DoD atendido; commit mergeado |

> **[PLACEHOLDER — DIAGRAMA: Fig. 1.2 — Fluxo Kanban Oficial com WIP Limits | Seção 1.3.1 | Conteúdo obrigatório: as cinco colunas (Backlog → Ready (DoR) → In Progress → Code Review → Done (DoD)) com gates anotados entre colunas (DoR na entrada de Ready; tasklist 100% + revisão de pares na entrada de Code Review; DoD na entrada de Done), e o WIP limit (3/pessoa) destacado sobre a coluna In Progress. Formato sugerido: Mermaid flowchart LR. Necessidade real: diagrama operacional central do projeto — materializa ADR-002 e ADR-004.]**

#### 1.3.2 Regras de Fluxo e Rituais

Regras de fluxo (ADR-002 e ADR-004):

- **Pull system:** Cards migram para "In Progress" somente quando há capacidade disponível (WIP limit respeitado).
- **WIP limit:** 3 cards em "In Progress" por pessoa (Domínio de Equipe — prevenção de burnout, R3 do TAP §10).
- **Tasklists Markdown (ADR-004):** Cards com estimativa ≥ 6h ou múltiplos entregáveis devem possuir tasklist no corpo da Issue (mínimo 3, máximo 7 itens; último item obrigatoriamente "Validação final"). Subissues reais são formalmente rejeitadas — a unidade atômica de métrica e de backlog permanece o card pai. O card só migra para `Code Review` com 100% dos itens concluídos.
- **SDD com LLM:** Código gerado com apoio de IA passa por revisão humana obrigatória antes do merge. Commits declaram co-autoria.

Rituais (ADR-002):

| Ritual | Formato | Cadência | Duração |
| --- | --- | --- | --- |
| Daily assíncrona | GitHub Issues | Diária | 15 min |
| Refinement | Product Backlog (GitHub Projects) | Semanal | 30 min |
| Retrospectiva | Risk backlog + lições aprendidas | Quinzenal | 30 min |

Nota: Sprints time-boxed NÃO são utilizadas. O fluxo é contínuo (ADR-002).

#### 1.3.3 Milestones e Identificação de Cards

O SSOT opera sobre três mecanismos complementares de organização:

**Milestones GitHub:** 5 milestones — M1 (22/09), M2 (30/09), Calibração (03/10, auxiliar), M3 (15/11), M4 (15/12). Cada Issue vincula-se a exatamente uma milestone; Issues sem milestone são backlog não planejado. Milestone não é fechada enquanto houver Issues abertas com label `change-request` ou `blocked`.

**Sistema de tags:** Todo card porta no mínimo 3 labels (1 tipo + 1 macro-fase + 1 área de conhecimento), habilitando filtragem, métricas de fluxo por categoria (ADR-003) e rastreabilidade TAP → EAP → Card. A taxonomia completa (27 labels em 5 categorias) reside na configuração do repositório e não é replicada neste plano (GMV).

**Padrão de redação (Card Ubíquo):** Todo card é autossuficiente — declara o quê, por quê, como será aceito e a quem pertence, sem exigir leitura de outro artefato. Cards documentais seguem o Padrão A (título `N{X}.{Y} — Descrição`, contexto ubíquo, critérios de aceite binários, rastreabilidade dupla); cards de produto seguem o Padrão B (User Story com critérios Given/When/Then), com aplicação efetiva a partir de M2. A prioridade temporal P0–P3 complementa a classificação MoSCoW (P0 = caminho crítico do marco; P3 = postergável).

### 1.4 Desenvolvimento e Manutenção do Plano de Gerenciamento

Processo PMBOK 6ª (dicionário): 4.2 — Desenvolver o Plano de Gerenciamento do Projeto.

Os oito planos de área são versionados no repositório GitHub sob `/docs/`. Cada plano:

- Inicia com frase de rastreabilidade ao TAP (Premissa + Restrição + Domínio PMBOK 7ª).
- Possui extensão máxima de 4 páginas (princípio GMV).
- É versionado via Conventional Commits: `docs(plano-integracao): atualização §X`.
- Passa por revisão em pares antes de ser considerado "Done".

Regra de coerência cruzada: Nenhum plano pode contradizer datas de marcos (M1–M4), premissas (P1–P8) ou restrições (§8) do TAP. Inconsistências detectadas em revisão acionam correção imediata antes do merge. A hierarquia de autoridade entre artefatos é: TAP > base de conhecimento operacional > Glossário > ADRs.

#### 1.4.1 Estratégia de Entrega Faseada dos Planos

Conforme o princípio de Elaboração Progressiva (PMBOK 6ª, dicionário) e a Personalização/Tailoring da Abordagem de Desenvolvimento (PMBOK 7ª), a entrega dos planos de gerenciamento é faseada:

| Marco | Planos Entregues | Justificativa |
| --- | --- | --- |
| M1 (22/09/2026) | Integração, Escopo, Cronograma, Custos, Qualidade (Áreas 1–5) | Fundação documental mínima viável; atendimento integral ao critério de aceite do TAP §6 para o M1 |
| M2 (30/09/2026) | Recursos, Comunicações, Riscos (Áreas 6–8) | Redigidos após a calibração do fluxo Kanban (23/09–03/10), com dados empíricos de capacidade da equipe |

Trade-off declarado: Redução de ~30% da carga documental do M1, permitindo foco na qualidade dos cinco planos fundamentais e na configuração do SSOT. Decisão alinhada ao Domínio de Abordagem de Desenvolvimento e Ciclo de Vida (PMBOK 7ª) e ao princípio GMV (§1.2.3).

### 1.5 Orientação e Gestão do Trabalho do Projeto

Processo PMBOK 6ª (dicionário): 4.3 — Orientar e Gerenciar o Trabalho do Projeto.
Domínio PMBOK 7ª: Trabalho do Projeto.

#### 1.5.1 Execução Diária

- Trabalho puxado do backlog conforme capacidade (pull system), respeitando a prioridade temporal P0–P3 e o WIP limit.
- Cada card segue o padrão de redação ubíquo (§1.3.3): título padronizado (ex: `N5.1 — Backend: Lógica de Negócio`), labels obrigatórias, milestone vinculada, responsável e critérios de aceite binários.
- Cards ≥ 6h portam tasklist Markdown conforme ADR-004 (§1.3.2).
- Commits seguem Conventional Commits (`feat`, `fix`, `docs`, `test`, `ci`, `chore`).

#### 1.5.2 Gestão do Conhecimento

Processo PMBOK 6ª (dicionário): 4.4 — Gerenciar o Conhecimento do Projeto.

- Estrutura de conhecimento: `/docs/` no repositório (planos, diagramas, lições aprendidas, catálogo de prompts SDD).
- Lições aprendidas registradas ao final de cada macro-fase (MF1, MF2, MF3).
- Decisões que afetam ≥ 2 fases da EAP, envolvem troca de tecnologia ou seriam questionadas pelo Prof. Dr. Nivaldo Carleto em avaliação são formalmente registradas via ADR (Architecture Decision Record), conforme REQ-12 e fase N9.1 da EAP. Decisões menores ficam em commit messages.

### 1.6 Monitoramento e Controle Integrado

Processo PMBOK 6ª (dicionário): 4.5 — Monitorar e Controlar o Trabalho do Projeto.
Domínio PMBOK 7ª: Medição.

#### 1.6.1 Métricas de Fluxo Kanban (Oficiais — ADR-003)

Dada a restrição de orçamento zero (TAP §11), o Earned Value Management é inaplicável. As métricas de desempenho são exclusivamente baseadas no fluxo Kanban:

| Métrica | Definição | Meta (pós-calibração) | Frequência |
| --- | --- | --- | --- |
| Cycle Time | Tempo médio de um card do "In Progress" ao "Done" | ≤ 3 dias | Semanal |
| Throughput | Cards concluídos por semana | ≥ 5 cards/semana | Semanal |
| CFD (Cumulative Flow Diagram) | Visualização de gargalos no fluxo | Sem bandas largas | Semanal |
| WIP em fluxo | Cards ativos em "In Progress" | ≤ 9 (3 × 3 pessoas) | Contínuo |
| Coverage | Linhas testadas / linhas totais | ≥ 80% | Por push (CI) |
| Burnout (self-report) | Carga horária semanal declarada | ≤ 20h/pessoa | Semanal |

Definição canônica do CFD (referência para os Planos de Cronograma e Comunicações): O Cumulative Flow Diagram é a visualização gráfica do fluxo de trabalho acumulado no tempo, onde cada banda horizontal representa uma coluna do quadro Kanban e sua largura instantânea indica a quantidade de cards naquela etapa. Fonte de dados: GitHub Insights. Responsável pela publicação semanal: GP. CFD saudável: bandas paralelas de largura constante. CFD com gargalo: bandas que se alargam progressivamente. Ação corretiva: banda com largura superior a 2× a média das demais por 2 semanas consecutivas aciona Retrospectiva extraordinária (ADR-002).

> **[PLACEHOLDER — DIAGRAMA: Fig. 1.3 — CFD: Padrão Saudável vs. Padrão com Gargalo | Seção 1.6.1 | Conteúdo obrigatório: dois painéis lado a lado — (a) CFD saudável com bandas paralelas e estáveis; (b) CFD com gargalo mostrando alargamento progressivo da banda Code Review, com anotação da regra de ação corretiva (2× largura média por 2 semanas). Formato sugerido: imagem estática (PNG/SVG) gerada a partir de dados simulados, versionada em /docs/diagrams/. Necessidade real: blindagem acadêmica formal para a ausência de Gantt/EVM.]**

#### 1.6.2 Métricas Legado (Não Aplicáveis — ADR-003)

| Métrica | Status | Justificativa |
| --- | --- | --- |
| SPI (Schedule Performance Index) | ❌ LEGADO | Inaplicável — fluxo contínuo sem linha de base preditiva |
| CPI (Cost Performance Index) | ❌ LEGADO | Inaplicável — orçamento zero (AC = 0) |
| EVM (Earned Value Management) | ❌ LEGADO | Inaplicável — escopo emergente + orçamento nulo |

#### 1.6.3 Período de Calibração

De 23/09/2026 a 03/10/2026, as métricas são coletadas sem meta fixa, estabelecendo a baseline empírica de desempenho real da equipe. Após calibração, metas são ajustadas com base na média observada ± 20% e formalizadas via ADR. A milestone auxiliar "Calibração" (03/10) rastreia este período no SSOT sem substituir o M2.

Trade-off declarado: Abre-se mão da formalidade EVM em favor de métricas acionáveis e nativas do método, conforme Domínio de Medição (PMBOK 7ª) e ADR-003.

### 1.7 Controle Integrado de Mudanças

Processo PMBOK 6ª (dicionário): 4.6 — Realizar o Controle Integrado de Mudanças.
Domínio PMBOK 7ª: Incerteza.

#### 1.7.1 Autoridade de Mudança (CCB)

O Gerente de Projeto (Leonardo David Silva Setti) atua como Change Control Board (CCB) de membro único, com autoridade formal delegada pelo TAP (§1.b, §9 P7). O Prof. Dr. Nivaldo Carleto não participa do fluxo de aprovação de mudanças; sua atuação restringe-se à avaliação acadêmica nos marcos M1–M4.

#### 1.7.2 Fluxo de Solicitação de Mudança

| Etapa | Ação | Responsável | Prazo |
| --- | --- | --- | --- |
| 1 | Abertura de GitHub Issue com label change-request | Qualquer membro da equipe | Imediato |
| 2 | Análise de impacto (escopo, prazo, qualidade) | GP (Leonardo) | ≤ 48h |
| 3 | Aprovação ou rejeição via comentário na Issue | GP (Leonardo) | ≤ 24h após análise |
| 4 | Atualização do backlog + planos afetados + commit | Equipe | ≤ 24h após aprovação |

> **[PLACEHOLDER — DIAGRAMA: Fig. 1.4 — Fluxo de Controle Integrado de Mudanças | Seção 1.7.2 | Conteúdo obrigatório: fluxograma vertical com as 4 etapas da tabela acima, incluindo o losango de decisão na etapa 3 (Aprovada? → sim: etapa 4; não: encerramento com registro), os SLAs anotados em cada transição (≤ 48h, ≤ 24h, ≤ 24h) e a bifurcação da etapa 4 (mudança simples → commit; mudança de marco/escopo MVP → ADR + comunicação no marco subsequente). Formato sugerido: Mermaid flowchart TD. Necessidade real: mecanismo mais auditado em avaliações PMBOK.]**

#### 1.7.3 Limiar de Formalidade

- **Mudanças que NÃO alteram marcos (M1–M4) nem escopo do MVP:** Aprovadas pelo GP com registro em commit e comentário na Issue.
- **Mudanças que ALTERAM marcos ou escopo do MVP:** Aprovadas pelo GP com registro formal via ADR e comunicação ao Prof. Dr. Nivaldo Carleto no marco de avaliação subsequente.

Valor Ágil aplicado: "Responder a mudanças sobre seguir um plano." O processo é leve, mas auditável.

### 1.8 Encerramento do Projeto ou Fase

Processo PMBOK 6ª (dicionário): 4.7 — Encerrar o Projeto ou Fase.
Domínio PMBOK 7ª: Entrega.

#### 1.8.1 Critérios de Encerramento por Macro-Fase

| Macro-Fase | Período | Critério de Encerramento |
| --- | --- | --- |
| MF1: Fundação | 01/09 – 30/09/2026 | TAP aprovado + 5 planos (Áreas 1–5) submetidos no M1 + 3 planos (Áreas 6–8) até o M2 + EAP sincronizada + Stack definida (ADR-001) + Ambiente e CI configurados |
| MF2: Construção | 01/10 – 15/11/2026 | MVP funcional + ≥ 80% coverage + UAT aprovado + Pipeline CI verde + baseline de métricas calibrada |
| MF3: Consolidação | 16/11 – 15/12/2026 | Documentação consolidada + Apresentação final + Validação acadêmica no marco M4 + Tag de release |

#### 1.8.2 Encerramento Formal do Projeto

- Tag de release final no repositório GitHub.
- Lições aprendidas finais consolidadas.
- Verificação dos cinco Objetivos SMART do TAP §3.
- Validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4.

### 1.9 Condições de Fracasso e Escalation

Derivado do TAP §3.3 (Condições de Fracasso), os seguintes gatilhos acionam ação corretiva imediata pelo GP:

| Gatilho | Ação |
| --- | --- |
| Desvio > 3 dias úteis em qualquer marco (M1–M4) | Issue change-request + proposta de replanejamento + ADR |
| Coverage < 70% por 2 semanas consecutivas | Revisão de prioridade de testes + ajuste de escopo |
| Burnout detectado (> 20h/semana por 2 semanas) | Redução de WIP + redistribuição de cards |
| Scope creep > 15% do backlog original | Congelamento de novas features + CCB (GP) |
| Throughput < 3 cards/semana por 2 semanas consecutivas | Revisão de WIP limits (fallback ADR-002) + reavaliação do escopo do MVP (fallback ADR-003) |
| MVP não funcional em homologação até M3 | Contingência técnica: redução de escopo não-crítico |

Nota: Escalation ao Prof. Dr. Nivaldo Carleto ocorre apenas nos marcos de avaliação ou quando o GP identificar risco de não cumprimento dos critérios SMART do TAP §3.

### 1.10 Declaração de Rastreabilidade

| Seção | Origem no TAP | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 1.2 (Governança) | §1.c + Premissa P1 | Abordagem de Desenvolvimento | 4.1, 4.2 |
| 1.3 (SSOT + Milestones + Cards) | Premissa P1 + §3 (Métricas) | Medição + Trabalho | 4.3, 4.5 |
| 1.4.1 (Entrega Faseada) | §6 (Marcos M1/M2) | Abordagem de Desenvolvimento | 4.2 |
| 1.5 (Orientação) | Premissas P3, P4, P5 | Trabalho do Projeto | 4.3, 4.4 |
| 1.6 (Monitoramento) | §3 (Métricas) + §11 (Orçamento zero) | Medição | 4.5 |
| 1.7 (Mudanças) | §3.3 (Fracasso) + Premissa P7 | Incerteza | 4.6 |
| 1.8 (Encerramento) | §6 (Marcos M1–M4) | Entrega | 4.7 |
| 1.9 (Escalation) | §3.3 (Fracasso) + §10 (Riscos) | Incerteza | 4.5, 4.6 |

Verificação: 100% das seções possuem rastreabilidade a ao menos uma premissa, restrição ou objetivo SMART do TAP.

### 1.11 Premissas e Restrições Aplicáveis

| Tipo | Referência TAP | Impacto neste Plano |
| --- | --- | --- |
| Premissa P1 | Governança híbrida | Fundamenta 1.2 |
| Premissa P3 | SDD com LLM autorizado | Fundamenta 1.3.2 e 1.5.2 |
| Premissa P5 | ≤ 20h/semana por membro | Fundamenta 1.3.2 e 1.9 |
| Premissa P6 | Hardware adequado e suficiente | Fundamenta 1.3 (viabilidade local) |
| Premissa P7 | Stakeholder-avaliador único nos marcos | Fundamenta 1.2.2 e 1.7.1 |
| Restrição §8.2 | Prazo letivo inegociável | Fundamenta 1.4.1 e 1.9 |
| Restrição §8.4 | Orçamento zero | Fundamenta 1.6.2 (inaplicabilidade EVM) |

### Controle de Versões — Seção 1

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 19/09/2026 | Emissão inicial | Leonardo D. S. Setti |
| 2.0 | 20/09/2026 | Entrega faseada dos planos (§1.4.1); incorporação da ADR-004 (tasklists, §1.3.2); milestones, labels e padrão de cards ubíquos (§1.3.3); definição canônica do CFD (§1.6.1); gatilho de throughput (§1.9); critérios MF1 corrigidos (§1.8.1); 4 pontos de inserção de diagramas (FIG-1 a FIG-4) | Leonardo D. S. Setti |

**Fim da Seção 1 — Integração | COGME**

---

## SEÇÃO 2 — ESCOPO

**Plano de Gerenciamento do Escopo**

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira
Versão: 1.1
Data: 20/09/2026
Autores: Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

Este plano deriva diretamente das Premissas P1 (governança híbrida), P2 (FOSS absoluto), P3 (SDD com IA auditável), P4 (código como deliverable), P8 (simplificação pedagógica) e P9 (separação ontológica TAP ≠ EAP ≠ PDCA), e das Restrições de Escopo, Cronograma e Qualidade do Termo de Abertura do Projeto (TAP), respeitando o Domínio de Planejamento e o Domínio de Entrega do PMBOK® 7ª edição.

### 2.1 Identificação e Propósito

Este Plano de Gerenciamento do Escopo define os mecanismos pelos quais o escopo do COGME é coletado, declarado, decomposto, validado e controlado ao longo do ciclo de vida. Sua função ontológica é complementar e subordinada ao TAP: o TAP autoriza o escopo de alto nível, a Estrutura Analítica do Projeto (EAP) o decompõe estruturalmente e este plano governa a evolução de ambos, garantindo coerência com os Objetivos SMART aprovados. Em conformidade com a Premissa P9, o TAP não integra a EAP nem é objeto de ciclos PDCA; este plano e a EAP, por sua vez, integram a estrutura de execução e melhoria contínua do projeto.

O plano ancora-se em dois referenciais normativos: o Domínio de Planejamento e o Domínio de Entrega do PMBOK® 7ª edição (PROJECT MANAGEMENT INSTITUTE, 2021), que orientam a evolução progressiva do escopo e a geração de valor; e, como dicionário complementar com obsolescência formalmente declarada, os processos 5.1 a 5.6 do PMBOK® 6ª edição (PROJECT MANAGEMENT INSTITUTE, 2017). Este documento é entregável do marco M1, conforme a estratégia de entrega faseada dos planos de gerenciamento (Plano de Integração, seção 1.4.1).

### 2.2 Abordagem Híbrida de Gerenciamento do Escopo

Conforme a Premissa P1 e a ADR-002, o escopo é gerenciado em duas camadas complementares. A primeira, denominada linha de base estrutural, é materializada pela EAP aprovada no TAP, seção 4, e define o escopo obrigatório do MVP acadêmico. A segunda, denominada fluxo emergente, é operacionalizada pelo backlog Kanban no GitHub Projects, que define a ordem de execução e permite evolução progressiva sem sprints time-boxed.

O trade-off declarado privilegia a completude acadêmica, garantida pela EAP, em detrimento da rigidez preditiva, e assegura adaptabilidade por meio do fluxo contínuo, em conformidade com o valor ágil "responder a mudanças sobre seguir um plano". Qualquer alteração fora da linha de base aciona o controle integrado de mudanças do Plano de Integração, seção 1.7.

### 2.3 Coleta e Gestão de Requisitos

#### 2.3.1 Métodos de Levantamento

Os requisitos foram coletados por duas técnicas complementares, em conformidade com o processo 5.2 do PMBOK® 6ª: análise de domínio, conduzida a partir da dor do público-alvo — profissionais brasileiros que prestam serviços ao exterior em moeda estrangeira — e do mapeamento das ferramentas dispersas hoje utilizadas para simulação cambial; e brainstorm estruturado da equipe, do qual derivaram as quinze necessidades consolidadas como requisitos. A combinação é justificável pelo contexto acadêmico, que dispensa técnicas de maior formalidade, como grupos focais ou prototipação de requisitos, em conformidade com o princípio de Governança Mínima Viável (GMV) declarado no Plano de Integração, seção 1.2.3.

#### 2.3.2 Inventário e Documentação de Requisitos

Os quinze requisitos encontram-se consolidados no TAP, seção 5, que exerce provisoriamente a função de documentação de requisitos até a publicação do artefato canônico em `/docs/requisitos/requisitos.md`, prevista para o marco M2. Distribuem-se em seis entregas principais, cada uma rastreável a um Objetivo SMART e a uma fase da EAP:

a) MVP Web Funcional (Fase N5): REQ-01 a REQ-07 — simulação cambial em tempo real, cinco regimes de contratação, spread e IOF, invoice em PDF, tempo de resposta inferior a três segundos, interface responsiva e cache de cotações;

b) Garantia da Qualidade (Fase N6): REQ-08 a REQ-10 — cobertura de testes superior a oitenta por cento, UAT com cem por cento dos fluxos críticos e ferramentas da qualidade;

c) DevOps e CI/CD (Fase N7): REQ-11 — pipeline de integração contínua;

d) Base de Conhecimento (Fase N9): REQ-12 e REQ-13 — ADRs e rastreabilidade de prompts SDD;

e) Documentação Técnica (Fase N11): REQ-14 — arquitetura e APIs consolidadas;

f) Conformidade FOSS (Fases N1 e N4): REQ-15 — licenciamento integralmente aberto.

#### 2.3.3 Formato dos Requisitos e Conversão a Posteriori

Os requisitos REQ-01 a REQ-15 foram formalizados com critério de aceite mensurável, rastreabilidade ao TAP e vínculo à fase da EAP, formato suficiente para o marco M1. A conversão para o formato canônico de User Story — "Como [papel], quero [ação], para [benefício]" com critérios de aceite Given/When/Then — será realizada a posteriori, até o marco M2 (30/09/2026), conforme fase N2.3 da EAP, utilizando o Padrão B de redação de cards (OKB, seção 9.3). A decisão é justificada pela restrição de prazo letivo e pelo princípio GMV.

#### 2.3.4 Abordagem Specification-Driven Development (SDD)

O escopo inclui, como requisito formal (REQ-12 e REQ-13), a utilização de Specification-Driven Development com apoio de Inteligência Artificial Generativa, conforme a Premissa P3 e o Objetivo SMART de Inovação do TAP. A abordagem SDD opera sobre a stack local canônica do projeto — llama.cpp como motor de inferência, modelo Qwen 32B e OpenCode como interface de desenvolvimento —, garantindo custo zero e conformidade FOSS em aderência à Premissa P2. A formalização da stack na ADR-001 encontra-se em avaliação e poderá sofrer atualizações de impacto relevante; a inclusão, a exclusão ou a troca de ferramentas, modelos ou motores em todo o contexto da stack exigirá ADR específica, conforme a política de ADRs do projeto (gatilhos de impacto transversal e de irreversibilidade prática) e o fluxo de mudanças da seção 2.8. O detalhamento operacional — prompts, personas e handoffs — reside no Catálogo de Prompts SDD (fase N9.3, diretório `.ai/handoffs/`) e nas ADRs (fase N9.1). A política de co-autoria em commits e a rastreabilidade integral dos prompts constituem critérios de aceite dos requisitos REQ-12 e REQ-13.

#### 2.3.5 Priorização de Requisitos e de Cards

A priorização opera em duas camadas distintas e complementares. A classificação de valor de escopo aplica o método MoSCoW aos requisitos: a classe Must compreende REQ-01 a REQ-09, REQ-11 e REQ-15; a classe Should compreende REQ-10, REQ-12, REQ-13 e REQ-14; as classes Could e Won't encontram-se vazias, registrando a última as exclusões da seção 2.4. A classificação de urgência temporal aplica a escala P0–P3 aos cards do backlog (OKB, seção 9.4), sendo P0 o caminho crítico do marco e P3 o item postergável. Ambas as classificações são aplicadas e revisadas no Refinement semanal, cuja primeira sessão ocorre em 23/09/2026.

### 2.4 Declaração de Escopo do Projeto

Em respeito ao princípio GMV e para evitar proliferação documental, a Declaração de Escopo é consolidada neste plano, em vez de constituir artefato separado.

#### 2.4.1 Fronteira do Escopo

A fronteira do escopo é apresentada na Tabela 1. A coluna de exclusões é fundamentada no princípio YAGNI (You Aren't Gonna Need It), em conformidade com a restrição de escopo do TAP, seção 8.1: funcionalidades não essenciais ao MVP acadêmico são explicitamente excluídas do ciclo atual, podendo ser reconsideradas apenas mediante solicitação formal de mudança (Plano de Integração, seção 1.7). Esta exclusão explícita operacionaliza a restrição de MVP e previne scope creep por acréscimo incremental não autorizado.

**Tabela 1 — Fronteira do Escopo (IN / OUT)**

| Escopo aprovado (IN) | Escopo excluído (OUT) |
| --- | --- |
| Simulação cambial USD/EUR → BRL em tempo real | Suporte a outras moedas (GBP, JPY, CHF) |
| Cinco regimes de contratação (hora, dia, semana, mês, valor fixo) | Cadastro multiusuário ou autenticação |
| Cálculo de spread e IOF com precisão de duas casas decimais | Integração com plataformas de transferência |
| Emissão de invoice em PDF via WeasyPrint em até três segundos | Emissão de notas fiscais brasileiras (NF-e, NFS-e) |
| Interface web responsiva FOSS | Aplicativo mobile nativo |
| Cache SQLite de cotações | Banco relacional multiusuário (PostgreSQL) |
| Cobertura de testes ≥ 80% e UAT com 100% dos fluxos críticos | Testes de carga ou estresse |
| Pipeline CI com lint e testes em até cinco minutos | Continuous deployment para produção |
| ADRs e catálogo de prompts SDD | Documentação de usuário final em PDF |
| Stack 100% FOSS auditável | Bibliotecas proprietárias ou serviços pagos |

Fonte: Elaborado pelos autores (2026), com base no TAP, seções 3 e 8.

#### 2.4.2 Critérios de Aceite do Escopo

O escopo será considerado aceito quando todos os requisitos da classe Must estiverem operacionais em UAT; quando a cobertura de testes atingir oitenta por cento, validada via integração contínua; quando não houver defeitos críticos ou bloqueantes; quando cem por cento das dependências possuírem licenças aprovadas pela Open Source Initiative; e quando houver validação acadêmica pelo Prof. Dr. Nivaldo Carleto no marco M4.

#### 2.4.3 Artefatos Técnicos Não Abrangidos por Este Plano

Para prevenir invasão de contexto, declara-se que não compõem o escopo deste plano: a) diagramas UML completos, sendo a arquitetura da solução (fase N3.1) documentada por diagrama de componentes em Markdown ou PlantUML; b) o Diagrama Entidade-Relacionamento, produzido na fase N3.3 e versionado no repositório; c) a estrutura de diretórios do repositório, documentada no arquivo README.md na fase N5; e d) os arquivos de configuração do pipeline, versionados em `.github/workflows/` na fase N7.1.

### 2.5 Estrutura Analítica do Projeto

A EAP aprovada no TAP, seção 4, constitui a linha de base estrutural do escopo: nível 0 (raiz COGME), doze fases de nível 1 (N1 a N12), trinta e sete pacotes de trabalho de nível 2 e três macro-fases (MF1 Fundação, MF2 Construção, MF3 Consolidação), conforme representado na Figura 1.

> **[PLACEHOLDER — DIAGRAMA: Fig. 2.1 — EAP do COGME, visão executiva | Seção 2.5 | Conteúdo obrigatório: raiz N0 no topo; doze caixas de nível 1 agrupadas em três faixas horizontais rotuladas MF1, MF2 e MF3; cada caixa de fase exibindo o identificador (N1…N12), o nome da fase e a contagem de pacotes de nível 2 (ex.: "N5 — Desenvolvimento do Sistema (5 pacotes)"); sem abertura dos 37 pacotes, para preservar legibilidade. Formato sugerido: Mermaid flowchart TB ou PlantUML WBS, versionado em /docs/diagrams/. Necessidade real: a EAP é o artefato nuclear do processo 5.4.]**

Nota de canonicidade (decisão do GP, 20/09/2026): a linha de base da EAP é canônica no TAP, seção 4. O TAP e o Plano de Integração constituem as fontes canônicas de autorização e de coordenação do projeto. O Glossário é artefato terminológico volátil, atualizado a cada rodada de redação dos planos, e não constitui linha de base: eventuais divergências de contagem de fases ou pacotes são resolvidas pela prevalência do TAP, sem necessidade de solicitação de mudança. A contagem de treze fases e quarenta e oito pacotes registrada em versão anterior do Glossário não corresponde à linha de base aprovada e será corrigida na próxima revisão do próprio Glossário.

Três regras de governança aplicam-se à decomposição. Primeira: nenhum pacote de trabalho pode ser adicionado, removido ou renomeado sem aprovação formal via change-request. Segunda: cada pacote de nível 2 decompõe-se em cards Kanban com esforço estimado inferior ou igual a oito horas, redigidos conforme os Padrões A (documental) ou B (User Story GWT) do OKB, seção 9.3. Terceira: quando necessário à execução, o card decompõe-se em atividades derivadas — ações verbais que detalham a entrega substantiva, em conformidade com o processo 6.2 do PMBOK® 6ª (dicionário) — materializadas como tasklist Markdown no corpo da Issue, conforme a ADR-004, que rejeita formalmente subissues. A cadeia completa é representada na Figura 2.

> **[PLACEHOLDER — DIAGRAMA: Fig. 2.2 — Cadeia de decomposição do escopo e gates de qualidade | Seção 2.5 | Conteúdo obrigatório: três níveis encadeados da esquerda para a direita — (i) pacote de trabalho EAP nível 2 (entrega, substantivo, ex.: "N5.1 — Backend: Lógica de Negócio"); (ii) card ubíquo Kanban (unidade atômica de backlog e de métrica, ≤ 8h, Padrão A ou B); (iii) atividades derivadas como tasklist Markdown (3 a 7 itens verbais, último item "Validação final", ADR-004); gates anotados entre colunas: DoR na entrada de Ready, tasklist 100% + revisão de pares na entrada de Code Review, DoD na entrada de Done; anotação lateral: "métricas de fluxo medem o card pai (ADR-003); subissues rejeitadas (ADR-004)". Formato sugerido: Mermaid flowchart LR, versionado em /docs/diagrams/.]**

Em conformidade com a Premissa P9, a EAP e seus pacotes integram a estrutura de ciclos PDCA do projeto (doze ciclos, um por fase), enquanto o TAP permanece como documento de autorização, não gerenciado.

### 2.6 Definition of Ready e Definition of Done

Em conformidade com o Domínio de Entrega e o Domínio de Medição do PMBOK® 7ª, formalizam-se os gates de qualidade do fluxo Kanban.

O DoR, gate de entrada, exige que o card possua: título padronizado no formato `N{X}.{Y} — Descrição`; contexto ubíquo autocontido; critério de aceite mensurável; rastreabilidade à fase da EAP e ao requisito do TAP; estimativa de esforço inferior ou igual a oito horas; dependências identificadas; responsável atribuído; no mínimo três labels (tipo, macro-fase e área de conhecimento); milestone vinculada; e revisão no Refinement semanal. Cards documentais seguem o Padrão A e cards de produto seguem o Padrão B (OKB, seção 9.3).

O DoD, gate de saída, exige que: 1) o código esteja implementado e commitado em feature branch; 2) os testes unitários estejam escritos com cobertura do módulo superior ou igual a oitenta por cento; 3) o pipeline de integração contínua esteja verde; 4) o Code Review tenha sido aprovado por pelo menos um par; 5) a documentação esteja atualizada, quando aplicável; 6) o card tenha sido movido para Done com data registrada; 7) se o código foi gerado com apoio de SDD, o commit declare co-autoria, conforme o Critério de Inovação Controlada do TAP, seção 3.2.e; e 8) se o card possuir tasklist Markdown no corpo da Issue (conforme ADR-004), cem por cento dos itens estejam marcados como concluídos (`- [x]`). Artefatos em status `pair-review` ou `in-review` não satisfazem o DoD e permanecem na coluna `Code Review` até a conclusão da revisão.

Nota (ADR-004 + OKB §9.3): cards documentais seguem o Padrão A de redação (título `N{X}.{Y} — Descrição`, contexto ubíquo, critérios de aceite binários, rastreabilidade dupla); cards de produto seguem o Padrão B (User Story com critérios Given/When/Then), com aplicação efetiva a partir do marco M2 (30/09/2026). Ambos os padrões estão definidos na base de conhecimento operacional, seção 9.3. O gate de tasklist (item 8) é definido canonicamente neste plano e referenciado pelo Plano de Integração, seção 1.3.2, como regra de migração de fluxo — a Integração sinaliza o ponto de controle sem duplicar o conteúdo do DoD, em conformidade com a fronteira de escopo entre as duas áreas.

### 2.7 Validação e Controle de Escopo

Os processos 5.5 (Validar o Escopo) e 5.6 (Controlar o Escopo) do PMBOK® 6ª são operacionalizados por rituais Kanban, conforme a ADR-002. A validação ocorre por Code Review e por User Acceptance Testing no marco M3, com evidência em Pull Request aprovado e relatório de UAT. O controle ocorre por Refinement semanal e por análise do Cumulative Flow Diagram, cuja definição formal, cadência e regra de ação corretiva residem no Plano de Integração, seção 1.6.1, com evidência no GitHub Projects e no GitHub Insights.

A prevenção de scope creep aciona alerta quando o backlog cresce superior a quinze por cento em relação à linha de base de trinta e sete pacotes da EAP. Nesse caso, o GP congela novas features, analisa o impacto via change-request e decide em até quarenta e oito horas. A métrica de controle é o Throughput semanal superior ou igual a cinco cards; se inferior a três cards por semana durante duas semanas consecutivas, o escopo é revisado conforme o fallback da ADR-003.

### 2.8 Gestão de Mudanças de Escopo

Qualquer alteração de escopo segue o fluxo do Plano de Integração, seção 1.7: abertura de Issue com label `change-request`, análise de impacto pelo GP em até quarenta e oito horas, aprovação ou rejeição em até vinte e quatro horas e atualização do backlog, da EAP quando aplicável, e commit. Mudanças que alterem marcos (M1–M4) ou o escopo do MVP exigem registro formal via ADR e comunicação ao Prof. Dr. Nivaldo Carleto no marco de avaliação subsequente. A inclusão, exclusão ou renomeação de pacotes da EAP enquadra-se sempre neste limiar de formalidade. Mudanças na stack tecnológica — incluindo a stack SDD, conforme seção 2.3.4 — seguem o mesmo fluxo e exigem ADR específica quando atendidos os gatilhos da política de ADRs do projeto.

### 2.9 Critérios de Aceite e Condições de Fracasso

Esta seção consolida, em respeito ao princípio GMV, os critérios positivos de aceite e os gatilhos negativos de fracasso do escopo.

#### 2.9.1 Critérios de Aceite

Remetem-se aos critérios da seção 2.4.2, acrescidos da verificação de que cem por cento dos requisitos da classe Must possuam rastreabilidade documentada a Objetivo SMART, fase da EAP e card do backlog.

#### 2.9.2 Condições de Fracasso e Escalation

Derivados do TAP, seção 3.3, os seguintes gatilhos específicos acionam ação corretiva: a) requisito Must não implementado até M3, com contingência de redução de escopo Should; b) EAP com mais de quinze por cento de pacotes não iniciados até M2, com replanejamento e ADR; c) UAT com defeito crítico ou bloqueante, com retrabalho imediato e congelamento de novas features; d) scope creep superior a quinze por cento, com congelamento e decisão do CCB; e e) cobertura de requisitos inferior a cem por cento dos Must, com bloqueio do M3.

### 2.10 Declaração de Rastreabilidade

A Tabela 2 apresenta a rastreabilidade de cada seção deste plano ao TAP, ao domínio de desempenho do PMBOK® 7ª correspondente e ao processo do PMBOK® 6ª utilizado como dicionário.

**Tabela 2 — Rastreabilidade interna do Plano de Escopo**

| Seção | Origem | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 2.2 (Abordagem híbrida) | TAP §1.c + Premissa P1 | Planejamento + Entrega | 5.1 |
| 2.3 (Requisitos) | TAP §3 + §5 + Premissa P3 | Entrega | 5.2 |
| 2.3.4 (Stack SDD local + regra de ADR) | Premissa P3 + REQ-12/13 + Política de ADRs (OKB) | Trabalho do Projeto | 5.2 |
| 2.4 (Declaração de Escopo) | TAP §3 + §8 + Premissa P2 | Entrega | 5.3 |
| 2.5 (EAP e decomposição; canonicidade no TAP §4) | TAP §4 + Premissa P9 | Planejamento | 5.4 + 6.2 (dicionário) |
| 2.6 (DoR/DoD) | TAP §3 (Qualidade) + §3.2.e | Entrega + Medição | 5.5 |
| 2.6 — DoD item 8 (tasklist) | ADR-004 + Integração §1.3.2 | Trabalho do Projeto | 4.3 (dicionário) |
| 2.6 — Padrões de redação | OKB §9.3 + ADR-002 | Entrega | 5.2 |
| 2.7 (Validação/Controle) | TAP §3 (Métricas) | Medição | 5.5, 5.6 |
| 2.8 (Mudanças) | TAP §3.3 + Premissa P7 | Incerteza | 4.6 |
| 2.9 (Aceite/Fracasso) | TAP §3.2 + §3.3 + §10 | Incerteza + Entrega | 5.5, 5.6 |

Fonte: Elaborado pelos autores (2026).

Verificação: cem por cento das seções possuem rastreabilidade a ao menos um objetivo SMART, premissa ou restrição do TAP; a fronteira OUT da seção 2.4.1 é adicionalmente fundamentada no princípio YAGNI; o gate de tasklist e os padrões de redação possuem rastreabilidade cruzada com a ADR-004, o OKB §9.3 e o Plano de Integração §1.3.2.

### 2.11 Premissas e Restrições Aplicáveis

As premissas aplicáveis a este plano são: P1 (governança híbrida), que fundamenta a seção 2.2; P2 (FOSS absoluto), que fundamenta a fronteira OUT da seção 2.4.1 e a stack SDD local da seção 2.3.4; P3 (SDD com IA auditável), que fundamenta a seção 2.3.4; P4 (código como deliverable), que fundamenta o DoD da seção 2.6; P8 (simplificação de Aquisições e Partes Interessadas), que fundamenta o escopo enxuto; e P9 (separação ontológica TAP ≠ EAP ≠ PDCA), que fundamenta a seção 2.5.

As restrições aplicáveis são: restrição de escopo (MVP acadêmico), que fundamenta a fronteira IN/OUT e a aplicação do princípio YAGNI na seção 2.4.1; restrição de cronograma (prazo letivo inegociável), que fundamenta a conversão a posteriori da seção 2.3.3 e os gatilhos da seção 2.9; e restrição de qualidade (tempo restrito para testes), que fundamenta o DoD com cobertura da seção 2.6.

### Controle de Versões — Seção 2

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 0.0 | 19/09/2026 | Emissão para análise prévia | Leonardo D. S. Setti |
| 0.1 | 19/09/2026 | Inserção do princípio YAGNI na fronteira OUT | Leonardo D. S. Setti |
| 0.2 | 19/09/2026 | Remoção de versões internas; Premissa P3; Tabelas 1 e 2; fusão de aceite e fracasso | Leonardo D. S. Setti |
| 1.0 | 20/09/2026 | Incorporação da ADR-004 (DoD item 8); Padrões A/B e P0–P3; Premissa P9 e Atividades Derivadas; Figuras 1 e 2; otimização ABNT | Leonardo D. S. Setti |
| 1.1 | 20/09/2026 | Resoluções do GP: (i) C1 — Nota de Canonicidade no §2.5; (ii) C2 — §2.3.4 com stack SDD local canônica; (iii) C3 — §2.6 com nota de canonicidade do DoD/Padrões e Tabela 2 expandida | Leonardo D. S. Setti |

**Fim da Seção 2 — Escopo | COGME v1.1**

---

## SEÇÃO 3 — CRONOGRAMA

**Plano de Gerenciamento do Cronograma**

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira
Versão: 1.2 · Data: 21/09/2026
Autores: Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

Este plano deriva diretamente das Premissas P1 (governança híbrida), P5 (disponibilidade de até 20h semanais por membro) e P7 (stakeholder-avaliador único nos marcos), e das Restrições de Cronograma e de Recursos (TAP §8) e de Orçamento (TAP §11), respeitando o Domínio de Planejamento e o Domínio de Medição do PMBOK® 7ª edição. Aplicam-se a este documento o regime de freeze do TAP e as Notas de Contexto registradas na seção 3.8 (NC-00).

### 3.1 Identificação e Propósito

Este Plano de Gerenciamento do Cronograma define como o tempo do projeto COGME é estruturado, estimado, consolidado e controlado. Sua função ontológica é complementar e subordinada ao TAP como fonte autorizativa: o TAP fixa os marcos M1–M4 (§6), o Plano de Escopo decompõe o trabalho em pacotes e cards (§2.5) e este plano governa o sequenciamento, a estimativa e o controle temporal entre ambos, sem duplicar o roadmap nem os gates DoR/DoD (Escopo §2.6).

Canonicidade e regime de freeze: o TAP, o Plano de Integração e o Plano de Escopo permanecem fontes canônicas de autorização, coordenação e escopo. O TAP encontra-se em regime de freeze desde o início do planejamento — sua última versão (18/09/2026) precede os planos de gerenciamento e não é objeto de revisão ao longo do ciclo, em conformidade com seu status ontológico já declarado: o TAP autoriza, não integra a EAP e não é gerenciado por ciclos PDCA (Premissa P9; Glossário §11; PMBOK® 6ª §4.1, dicionário). Em caso de divergência entre seções do TAP, a seção §6 Marcos é canônica para matéria temporal (NC-00). Este plano detém as Notas de Contexto (§3.8) como mecanismo exclusivo de registro de leituras operacionais do TAP congelado.

Domínios PMBOK 7ª: Planejamento (evolução progressiva do cronograma) e Medição (monitoramento temporal do progresso).

Processos PMBOK 6ª (dicionário, obsolescência formalmente declarada conforme Integração §1.2.4): 6.1 Planejar o Gerenciamento do Cronograma; 6.2 Definir as Atividades; 6.3 Sequenciar as Atividades; 6.4 Estimar as Durações das Atividades; 6.5 Desenvolver o Cronograma; 6.6 Controlar o Cronograma. A numeração canônica aqui adotada é objeto da NC-02 (seção 3.8), frente a divergências registradas em artefatos vivos (base de conhecimento operacional e Glossário).

### 3.2 Abordagem de Gerenciamento do Cronograma (processo 6.1)

O cronograma é gerenciado em três camadas temporais distintas, materializando a Personalização da Abordagem de Desenvolvimento (PMBOK 7ª) e a ADR-002:

| Camada | Objeto | Mecanismo de controle | Estabilidade |
| --- | --- | --- | --- |
| Macro | Marcos M1–M4 | Datas fixas do TAP §6; alteração somente via change-request + ADR + comunicação (Integração §1.7.3; OKB §9.2) | Inegociável sem CCB |
| Meso | Macro-fases MF1–MF3 + milestone auxiliar Calibração | Períodos declarados (Integração §1.8.1; OKB §9.2); gates de fechamento entre macro-fases | Ajustável apenas via CCB |
| Operacional | Cards Kanban (≤ 8h) | Fluxo contínuo pull, WIP de 3 cards/pessoa, sem sprints e sem datas por atividade (ADR-002) | Emergente, refinado semanalmente |

Aplica-se o planejamento em ondas sucessivas (elaboração progressiva, PMBOK 6ª como dicionário): o detalhe operacional emerge no Refinement semanal (ADR-002), enquanto apenas as camadas macro e meso são objeto de controle formal de mudanças. Não existe linha de base preditiva de datas por pacote: a única linha de base temporal formal é o conjunto {marcos M1–M4 + macro-fases MF1–MF3 + milestone auxiliar Calibração}.

Trade-off declarado: abre-se mão da previsibilidade preditiva por atividade em favor de confiabilidade empírica no nível do marco, alinhado ao Domínio de Medição (PMBOK 7ª), à ADR-003 e ao valor ágil "Responder a mudanças sobre seguir um plano".

### 3.3 Definição das Atividades (processo 6.2)

A cadeia de decomposição temporal é idêntica à cadeia de decomposição do escopo, canonicamente representada na Figura 2 do Plano de Escopo (§2.5): os 37 pacotes de trabalho de nível 2 da EAP (linha de base do TAP §4 — 12 fases) decompõem-se em cards Kanban com esforço ≤ 8h, e estes, quando ≥ 6h ou com múltiplos entregáveis, decompõem-se em atividades derivadas materializadas como tasklist Markdown (3 a 7 itens; último item obrigatoriamente "Validação final"), conforme ADR-004, que rejeita formalmente subissues.

Regras operacionais desta seção: (i) a unidade atômica de cronograma e de métrica temporal é o card pai (ADR-003 e ADR-004); itens de tasklist não geram previsão nem métrica própria; (ii) nenhum card migra para `Ready` sem estimativa de esforço e dependências identificadas (DoR, Escopo §2.6); (iii) cards estimados acima de 8h são obrigatoriamente divididos antes de entrar no fluxo.

### 3.4 Sequenciamento e Dependências (processo 6.3)

Conforme a base de conhecimento operacional (§8.1) e a ADR-003, não se constrói rede de precedências CPM no nível operacional: em fluxo contínuo com escopo emergente, uma rede de atividades ficaria obsoleta em dias, violando o princípio GMV. O sequenciamento opera por quatro mecanismos nativos do SSOT:

a) campo "Dependências" dos Padrões A e B de redação de cards (OKB §9.3);
b) gate DoR "dependências identificadas" (Escopo §2.6);
c) label `blocked` com registro obrigatório da dependência no corpo da Issue (OKB §9.1);
d) regra P0: card que, ausente, impede o marco ou bloqueia ≥ 2 outros cards integra o caminho crítico empírico (OKB §9.4).

O caminho crítico é identificado empiricamente pela combinação de cards P0, alargamentos de banda no CFD e desvios de Cycle Time — definição formal, cadência e regra corretiva canonicamente na Integração §1.6.1 —, revisada a cada Refinement semanal e a cada Retrospectiva quinzenal.

No nível macro, o sequenciamento é finish-to-start entre macro-fases, com gates explícitos: o M2 encerra a MF1; a milestone auxiliar Calibração (03/10/2026) libera a baseline empírica que autoriza metas na MF2; o M3 encerra a MF2; o M4 encerra a MF3. Dentro de cada macro-fase, o paralelismo é integral, gerenciado por pull system e WIP limits (TAP §6, premissa temporal 2).

> **[PLACEHOLDER — DIAGRAMA: Fig. 3.1 — Sequenciamento macro e caminho crítico empírico | Seção 3.4 | Conteúdo obrigatório: faixa superior com as três macro-fases encadeadas por gates (MF1 → gate M2/Calibração → MF2 → gate M3 → MF3 → gate M4); faixa inferior com a camada operacional mostrando os quatro detectores do caminho crítico empírico (cards P0, label blocked, bandas do CFD, desvio de Cycle Time) alimentando a decisão de replanejamento no Refinement. Formato sugerido: Mermaid flowchart LR, versionado em /docs/diagrams/. Necessidade real: substitui visualmente a rede CPM rejeitada.]**

### 3.5 Estimativa de Esforço e Duração (processo 6.4)

Esforço é estimado em horas pelo responsável técnico (julgamento de especialista), com classificação relativa T-shirt (PP ≤ 2h, P ≤ 4h, M ≤ 6h, G = 8h) como verificação cruzada, conforme vocabulário do Glossário (§3, processo 6.4). As faixas são binárias quanto à governança: cards ≤ 4h são atômicos e não portam tasklist; cards ≥ 6h portam tasklist obrigatória; o teto absoluto é 8h (ADR-004; Escopo §2.5).

Capacidade semanal nominal: 3 membros × 20h/semana (Premissa P5) = 60h/semana, regulada pelo WIP limit de 3 cards em `In Progress` por pessoa (ADR-002), e não por taxa de utilização fixa. O overhead dos rituais (daily assíncrona, Refinement semanal, Retrospectiva quinzenal — ADR-002) é estimado em ≤ 1h/semana por membro e absorvido pela capacidade nominal (premissa PA-3). Verificação de capacidade do marco corrente: a distribuição de trabalho do backlog M1 registra ~14h (Leonardo), ~13h (Fabricio) e ~11h (Edson), todos dentro do limite da Premissa P5, conforme tabela de distribuição da base de conhecimento operacional (§10.3) — evidência verificável de aderência (NC-06).

Duração calendarizada não é estimada por atividade: emerge do fluxo. O Cycle Time (definição operacional da ADR-003: `In Progress` → `Done`; divergências de redação em artefatos de origem tratadas na NC-03) possui meta de ≤ 3 dias após a calibração; a projeção de conclusão de cada marco é obtida dividindo-se o backlog ordenado por prioridade (P0 → P3) pelo Throughput empírico (meta ≥ 5 cards/semana pós-calibração; baseline em `/docs/metricas/baseline.md` após 03/10/2026, conforme ADR-003).

Convenção de dias (NC-03): métricas de fluxo (Cycle Time, CFD) são medidas em dias corridos, por serem nativas do GitHub Insights e não exigirem recálculo; marcos, desvios de marco e capacidade são tratados em dias úteis, refletindo a disponibilidade real da equipe e coerente com o gatilho de escalation da Integração §1.9 ("desvio > 3 dias úteis").

Trade-off declarado: perde-se a previsão determinística por atividade e ganha-se previsão empírica por marco com overhead zero de estimativa, conforme Domínio de Planejamento (PMBOK 7ª) e princípio GMV.

### 3.6 Desenvolvimento do Cronograma (processo 6.5)

O cronograma do COGME é materializado por três artefatos complementares: (i) o roadmap macro de marcos (Figura 2), única representação tipo Gantt admitida, restrita ao nível macro e derivada do SSOT, conforme autorização do OKB §8.1; (ii) o backlog ordenado por P0–P3 e MoSCoW no GitHub Projects, que constitui o cronograma operacional vivo; e (iii) a linha de base temporal formal {M1–M4 + MF1–MF3 + Calibração}, única sujeita a controle integrado de mudanças.

O período de calibração (23/09 a 03/10/2026) é um artefato de cronograma: converte métricas de fluxo em capacidade de previsão. Até seu encerramento, as metas permanecem suspensas (Integração §1.6.3); após, metas ajustadas pela média observada ± 20% são formalizadas via ADR (ADR-003).

**Tabela 1 — Marcos, janelas e entregáveis de valor**

| Marco | Abertura SSOT | Data alvo | Entregável de valor | Critério de aceite |
| --- | --- | --- | --- | --- |
| M1 — Entrega Parcial Documental | 01/09/2026 | 22/09/2026 | TAP aprovado + 5 planos (Áreas 1–5, incluindo 12 PDCAs e Ishikawa no Plano de Qualidade) + ADRs 001–004 + SSOT configurado (backlog M1-01 a M1-21) | Submissão via GitHub validada pelo Prof. Dr. Nivaldo Carleto sem achados críticos |
| M2 — Ambiente e Modelagem | 23/09/2026 | 30/09/2026 | Stack FOSS definida e validada por protótipo (fase N4.1, conforme TAP §10 R2); ambiente local + CI verdes; DER e Protótipo UX/UI versionados; planos das Áreas 6–8. Ressalva NC-04: formalização da stack na ADR-001 encontra-se em avaliação e pode sofrer atualização via ADR específica (Escopo §2.3.4) | Pipeline CI verde; artefatos de modelagem no repositório |
| Calibração (auxiliar) | 23/09/2026 | 03/10/2026 | Baseline empírica de fluxo + ADR de metas | Baseline publicada em /docs/metricas/baseline.md |
| M3 — MVP Funcional (Beta) | 04/10/2026 | 15/11/2026 | MVP full-stack operacional, coverage ≥ 80%, UAT sem defeitos críticos/bloqueantes | Métricas de fluxo dentro da baseline calibrada |
| M4 — Encerramento | 16/11/2026 | 15/12/2026 | Documentação técnica consolidada, lições aprendidas, verificação SMART, apresentação final, tag de release | Validação acadêmica pelo Prof. Dr. Nivaldo Carleto e tag de release final |

Fontes: TAP §6; OKB §9.2; Integração §1.3.3 e §1.8.1. Datas idênticas em todos os artefatos.

Nota de Contexto (NC-01): o objetivo SMART de Cronograma (TAP §3, item ii) registra "documentação consolidada" em novembro/2026, enquanto o TAP §6 e o critério de sucesso §3.2.g alocam consolidação e aceite no M4 (15/12/2026). Pela regra de precedência intra-TAP (NC-00), este plano operacionaliza a leitura do §6, sem alteração de datas: a entrega do MVP funcional que satisfaz o SMART ii na dimensão produto ocorre no M3 (15/11/2026, novembro); a consolidação documental acadêmica ocorre no M4. A seção SMART é assim assimilada à luz da seção §6 Marcos, em conformidade com o regime de freeze — nenhuma revisão do TAP é prevista ou citada.

> **[PLACEHOLDER — DIAGRAMA: Fig. 3.2 — Roadmap macro do cronograma | Seção 3.6 | Conteúdo obrigatório: três faixas horizontais MF1 (01/09–30/09), MF2 (01/10–15/11) e MF3 (16/11–15/12); cinco marcadores de milestone nas datas da Tabela 1, com a Calibração graficamente distinguida como auxiliar; anotação "única representação tipo Gantt admitida — nível macro, derivada do SSOT (OKB §8.1); nível operacional regido por fluxo (ADR-002)". Formato sugerido: Mermaid gantt ou timeline, versionado em /docs/diagrams/.]**

Gantt operacional via ProjectLibre: não produzido proativamente (GMV); será derivado do Kanban somente se exigido formalmente pelo Prof. Dr. Nivaldo Carleto em avaliação (Glossário §7).

### 3.7 Controle do Cronograma (processo 6.6)

O monitoramento temporal é contínuo e nativo do SSOT (Domínio de Medição): o CFD exerce, neste plano, a função de monitoramento temporal substituto do Gantt/EVM (função atribuída pela base de conhecimento operacional, §8.2; definição formal, cadência semanal e regra corretiva de banda 2× canonicamente na Integração §1.6.1, aqui apenas referenciadas); Cycle Time e Throughput são publicados semanalmente via GitHub Insights; o WIP em fluxo é verificado continuamente (≤ 9 cards).

Gatilhos de ação corretiva com recorte temporal (derivados da Integração §1.9):

| Gatilho | Ação corretiva | Base temporal |
| --- | --- | --- |
| Desvio > 3 dias úteis em qualquer marco M1–M4 | Issue change-request + proposta de replanejamento + ADR | Dias úteis |
| Throughput < 3 cards/semana por 2 semanas consecutivas | Revisão de WIP limits (fallback ADR-002) + reavaliação do escopo do MVP (fallback ADR-003) | Semanas |
| Banda do CFD > 2× a largura média por 2 semanas | Retrospectiva extraordinária + replanejamento do gargalo (caminho crítico empírico, §3.4) | Semanas |
| Card P0 com label blocked por > 48h | Intervenção direta do GP + resolução ou substituição da dependência | Horas corridas (NC-05) |

Fechamento de milestones: uma milestone não é fechada enquanto houver Issues abertas com label `change-request` ou `blocked`; o fechamento exige critérios atendidos, registro de lições aprendidas e comunicação ao Prof. Dr. Nivaldo Carleto quando aplicável (M1, M3, M4), conforme regras da base de conhecimento operacional (§9.2). Alteração de data de marco oficial exige change-request + aprovação do CCB (GP, membro único) + ADR + comunicação no marco subsequente (Integração §1.7.3); a milestone auxiliar Calibração pode ser reajustada pelo GP com registro em commit.

### 3.8 Notas de Contexto e Registro de Saneamento dos Artefatos Vivos

**NC-00 — Regime de freeze do TAP e precedência intra-TAP (decisão do GP, 21/09/2026).** O TAP encontra-se congelado desde o início do planejamento (última versão datada de 18/09/2026, anterior a este plano): não é revisado, reversionado ou corrigido ao longo do ciclo, em conformidade com seu status ontológico (Premissa P9; Glossário §11; PMBOK® 6ª §4.1 como dicionário). Duas regras derivam: (i) precedência intra-TAP — em divergência entre seções do TAP, a seção §6 Marcos é canônica para matéria temporal e de marcos; (ii) locus de contexto — este documento de Planejamento (8 Áreas) detém, com precedência, as Notas de Contexto que registram a leitura operacional vigente do TAP congelado; divergências jamais são tratadas como correções do TAP. Trade-off declarado: aceita-se divergência textual entre o termo autorizativo imutável e a leitura operacional, em favor da imutabilidade da referência de autorização e da trilha auditável de interpretações. A decisão atende aos gatilhos G1 (impacto transversal — todos os 8 planos), G3 (questionabilidade acadêmica) e G4 (trade-off não óbvio) da Política de ADRs (Aditivo da base de conhecimento, §1.2) → ADR-005 encaminhada para emissão antes do M2, com incorporação da cláusula na próxima revisão do Plano de Integração (§1.4).

**NC-01 — Assimilação do SMART de Cronograma à seção §6.** Registro e resolução da divergência entre TAP §3 (item ii) e TAP §6/§3.2.g quanto à "documentação consolidada": prevalece a leitura do §6 — MVP funcional no M3 (novembro/2026) e consolidação documental acadêmica no M4 (15/12/2026). Aplicada em §3.6. Nenhuma revisão do TAP é prevista ou citada (regime de freeze).

**NC-02 — Numeração canônica dos processos de cronograma.** Este plano adota a numeração oficial do PMBOK® 6ª edição (6.1–6.6). Divergências registradas na base de conhecimento operacional (§8.1) e no Glossário (§3) — artefatos vivos — não são replicadas aqui e constam do registro de saneamento.

**NC-03 — Convenção dupla de dias e definição operacional de Cycle Time.** Métricas de fluxo em dias corridos (nativo GitHub Insights); marcos, desvios e capacidade em dias úteis. A definição operacional de Cycle Time aqui vigente é `In Progress` → `Done` (ADR-003), prevalecendo sobre redações divergentes em artefatos de origem; a leitura do TAP congelado é registrada por esta nota, e o saneamento aplica-se apenas aos artefatos vivos (ADR-003, Glossário, baseline).

**NC-04 — Redação do critério M2 (stack).** A expressão "Stack FOSS validada (ADR-001)" foi substituída por "definida e validada por protótipo (TAP §10, R2; fase N4.1)", com ressalva de que a formalização na ADR-001 está em avaliação e mudanças de stack exigem ADR específica (Escopo §2.3.4). Aplicada na Tabela 1.

**NC-05 — Base temporal do gatilho de bloqueio P0.** O limiar de 48h para cards P0 `blocked` é medido em horas corridas (evento de fluxo), distinguindo-se da base de dias úteis aplicada a desvios de marco. Aplicada em §3.7.

**NC-06 — Verificação de capacidade do marco corrente.** Registrada como evidência verificável a distribuição de carga do backlog M1 (base de conhecimento operacional, §10.3), com todos os membros dentro do limite de 20h semanais (Premissa P5). Aplicada em §3.5.

**Entendimentos sobre o TAP congelado (notas de contexto — sem saneamento):**

| Matéria | Seção do TAP (congelado) | Entendimento adotado neste plano |
| --- | --- | --- |
| SMART ii × consolidação no M4 | §3 × §6 | NC-01: §6 prevalece; MVP funcional no M3, consolidação no M4 |
| Cabeçalho "Fases EAP v2.0" | §5 | EAP citada sem versão interna (regra já aplicada neste plano) |
| Subnumeração das restrições | §8 | Restrições citadas por categoria nominal + §11 (orçamento); subnumeração não presumida |
| Cycle Time "To Do → Done" | §3 (Métricas) | Definição operacional In Progress → Done (ADR-003), via NC-03 |

**Registro de saneamento — artefatos vivos (não bloqueante):**

| Pendência | Artefato vivo | Momento previsto |
| --- | --- | --- |
| Numeração 6.3/6.5 no §8.1 | Base de conhecimento operacional §8.1 | Próxima revisão da base |
| "Processo 6.4 Estimar Custos" → 6.4 Estimar Durações (custos = 7.2) | Glossário §3 | Próxima revisão do Glossário |
| Grafia "Carleto" → "Carleto" | Glossário | Próxima revisão do Glossário |
| Cycle Time "To Do → Done" → "In Progress → Done" | Glossário | Próxima revisão do Glossário |
| Contagem EAP "13/48" → 12/37 (baseline do TAP §4) | Glossário §1 | Próxima revisão do Glossário |
| Convenção dupla de dias | ADR-003 / Glossário / baseline | Formalização da baseline (após 03/10) |
| Cláusula NC-00 na hierarquia formal + ADR-005 | Integração §1.4 / ADR-005 | Antes do M2 |

### 3.9 Declaração de Rastreabilidade

**Tabela 2 — Rastreabilidade interna do Plano de Cronograma**

| Seção | Origem | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 3.2 (Abordagem em 3 camadas) | TAP §1.c + §6 + Premissa P1 | Abordagem de Desenvolvimento + Planejamento | 6.1 |
| 3.3 (Definição de atividades) | TAP §4 + Escopo §2.5 + ADR-004 | Planejamento + Trabalho do Projeto | 6.2 |
| 3.4 (Sequenciamento e caminho crítico empírico) | TAP §6 (premissa 2) + OKB §8.1 + ADR-002 | Planejamento + Entrega | 6.3 |
| 3.5 (Estimativa; verificação de capacidade NC-06) | Premissa P5 + TAP §8 + OKB §10.3 + ADR-003 | Planejamento + Medição | 6.4 |
| 3.6 (Roadmap, linha de base, calibração, NC-01/NC-04) | TAP §6 + §3 (SMART Cronograma) + §10 (R2) + Escopo §2.3.4 | Planejamento + Medição | 6.5 |
| 3.7 (Controle e gatilhos; NC-05) | TAP §3.3 + §3 (Métricas) + Integração §1.9 | Medição + Incerteza | 6.6 |
| 3.8 (Notas de Contexto; regime de freeze) | Decisão do GP (21/09/2026) + Premissa P9 + Glossário §11 + Aditivo OKB §1.2 | Trabalho do Projeto + Incerteza | 4.6 (dicionário) |

Verificação: 100% das seções possuem rastreabilidade a ao menos um objetivo SMART, premissa, restrição do TAP ou decisão formal do GP; referências cruzadas apontam exclusivamente para locais canônicos (Integração §1.6.1 para CFD; Escopo §2.5/§2.6 para decomposição e gates; OKB §9.2 para regras de milestone).

### 3.10 Premissas e Restrições Aplicáveis

Premissas do TAP: P1 (governança híbrida), fundamenta §3.2; P5 (20h/semana), fundamenta §3.5; P7 (avaliador nos marcos), fundamenta §3.7; P9 (separação ontológica TAP ≠ EAP ≠ PDCA), fundamenta o regime de freeze da §3.8.

Premissas específicas deste plano: PA-1 — datas de abertura e fechamento de milestones no GitHub são marcadores administrativos do SSOT, não dias trabalhados (sana a leitura de abertura do M3 em 04/10/2026 frente ao início da MF2 em 01/10/2026); PA-2 — convenção dupla de dias (NC-03); PA-3 — overhead de rituais ≤ 1h/semana por membro, absorvido pela capacidade nominal; PA-4 — GitHub Insights disponível e gratuito durante todo o ciclo (TAP §11).

Restrições: prazo letivo inegociável e curso noturno (TAP §8 — Restrições de Cronograma e de Recursos), fundamentam §3.5 e §3.7; orçamento zero (TAP §11), veta ferramentas pagas de cronograma e fundamenta a rejeição de Gantt/CPM operacionais (ADR-003); equipe de 3 pessoas com múltiplos papéis (TAP §8 — Recursos), fundamenta o WIP limit como regulador de capacidade.

### Controle de Versões — Seção 3

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 21/09/2026 | Emissão inicial para o M1: abordagem em 3 camadas; caminho crítico empírico; convenção dupla de dias; FIG-1 e FIG-2 | Leonardo D. S. Setti |
| 1.1 | 21/09/2026 | Revisão crítica: Notas de Correção NC-00 a NC-06; M2 reescrito (NC-04); base temporal do gatilho P0 (NC-05); verificação de capacidade (NC-06) | Leonardo D. S. Setti |
| 1.2 | 21/09/2026 | Rodada 10 — Diretriz D3 do GP: regime de freeze do TAP formalizado (NC-00); precedência intra-TAP da seção §6 Marcos; §3.8 reconstituída como Notas de Contexto; supressão integral de referências a correção/revisão/saneamento do TAP; saneamento restrito a artefatos vivos; ADR-005 redefinida (regime de freeze) e mantida antes do M2 | Leonardo D. S. Setti |

**Fim da Seção 3 — Cronograma | COGME v1.2**

---

## SEÇÃO 4 — CUSTOS

**Plano de Gerenciamento de Custos**

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira
Versão: 1.2
Data: 21/09/2026
Autores: Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

### 4.1 Identificação e Propósito

Este Plano de Gerenciamento de Custos estabelece os mecanismos de governança para assegurar que o projeto COGME seja executado dentro da linha de base de custos aprovada: R$ 0,00 (zero reais).

Fundamentação: Deriva diretamente das Premissas P2 (FOSS absoluto), P6 (hardware adequado) e P9 (separação ontológica TAP ≠ EAP ≠ PDCA), e das Restrições de Custo do TAP (§8.4 e §11), respeitando os Domínios de Planejamento, Medição e Entrega do PMBOK® 7ª edição.

Função ontológica: O plano não duplica a auditoria de licenças (EAP N4.4) nem a seleção de stack (EAP N4.1) — estabelece a governança sobre esses artefatos, garantindo que 100% das ferramentas, bibliotecas e serviços permaneçam dentro do perímetro FOSS/Free Tier ao longo de todo o ciclo de vida.

Domínios PMBOK 7ª: Planejamento (prevenção de desvios de conformidade), Medição (métricas de conformidade como substituição de EVM) e Entrega (garantia de sustentabilidade econômica do produto).

Processo PMBOK 6ª (dicionário, obsolescência assumida conforme Integração §1.2.4): 7.1 Planejar o Gerenciamento de Custos. Os processos 7.2 (Estimar Custos), 7.3 (Determinar Orçamento) e 7.4 (Controlar Custos) são inaplicáveis no sentido tradicional, pois:

- Estimativa: não há custos a estimar (todos os recursos são gratuitos)
- Orçamento: linha de base = R$ 0,00
- Controle: métricas EVM (CPI, VAC) são matematicamente indeterminadas (AC = 0), conforme ADR-003

Trade-off declarado: Abre-se mão da formalidade de estimativa/orçamento em favor de auditoria contínua de conformidade FOSS, alinhado ao Princípio "Foco em Valor" (PMBOK 7ª) e à Restrição TAP §8.4.

### 4.2 Abordagem de Gerenciamento de Custos

O gerenciamento de custos do COGME opera em três camadas de prevenção:

| Camada | Objeto | Mecanismo de Controle | Fonte Canônica |
| --- | --- | --- | --- |
| Preventiva | Seleção de stack e ferramentas | ADR-001 + Fase N4.1 (Seleção e Validação da Stack FOSS) | ADR-001; EAP N4.1 |
| Normativa | Política de licenciamento | Whitelist/blacklist de licenças (§4.5.1) | EAP N1.4 |
| Detectiva | Auditoria de licenças | Fase N4.4 (Auditoria de Licenças) + checklist OSI-approved | EAP N4.4 |

Regra de ouro: Nenhuma ferramenta, biblioteca, API ou serviço pode ser incorporado ao projeto sem:

1. Verificação de licença OSI-approved (whitelist §4.5.1)
2. Confirmação de plano gratuito suficiente para o MVP acadêmico
3. Registro na ADR-001 ou em ADR específica (se mudança de stack)

Hierarquia de resolução de conflitos (aplicada a custos):

1. Conformidade FOSS (restrição TAP §8.4)
2. Funcionalidade do MVP (TAP §3 — Produto)
3. Conveniência técnica (preferência do desenvolvedor)

> **[PLACEHOLDER — DIAGRAMA: Fig. 4.1 — Fluxo de Prevenção de Custos | Seção 4.2 | Conteúdo obrigatório: fluxograma vertical com três gates sequenciais (Gate 1: licença OSI-approved?; Gate 2: plano gratuito suficiente para MVP?; Gate 3: registrado em ADR-001 ou nova ADR?) e anotação sobre change-request (Integração §1.7). Formato sugerido: Mermaid flowchart TD. Necessidade real: materializa visualmente o mecanismo de prevenção de custos, demonstrando que "custo zero" não é ausência de governança, mas governança rigorosa sobre conformidade FOSS.]**

### 4.3 Linha de Base de Custos

Conforme TAP §11, a linha de base de custos é:

| Categoria | Valor Aprovado | Justificativa |
| --- | --- | --- |
| Recursos Humanos | R$ 0,00 | Esforço acadêmico voluntário (3 membros) |
| Software e Ferramentas | R$ 0,00 | 100% FOSS ou Free Tier (TAP §3 — Inovação) |
| Infraestrutura e Hospedagem | R$ 0,00 | Ambiente local/homologação (sem cloud paga) |
| Reserva de Contingência | R$ 0,00 | Inaplicável — linha de base zero inviabiliza reserva financeira; riscos de custo mitigados por substituição FOSS (Plano de Riscos, M2) |
| Reserva de Gerenciamento | R$ 0,00 | Inaplicável — mesma razão |
| TOTAL | R$ 0,00 | Linha de base imutável sem CCB |

Regra de imutabilidade: A linha de base só pode ser alterada via `change-request` + aprovação do CCB (GP como membro único, TAP v3 §1.c) + ADR + comunicação ao Prof. Dr. Nivaldo Carleto no marco subsequente (Integração §1.7.3).

Premissa crítica (P2): A disponibilidade contínua de ferramentas FOSS e Free Tier é assumida como verdadeira. Caso uma ferramenta essencial migre para modelo pago durante o projeto, aciona-se:

1. Busca imediata de alternativa FOSS equivalente
2. Se inexistente, redução de escopo (remoção da funcionalidade dependente)
3. Registro em ADR + lição aprendida

### 4.4 Estratégias de Medição e Controle

Dada a inaplicabilidade de EVM (Earned Value Management) — formalmente declarada como LEGADO na ADR-003 e na Integração §1.6.2, pois AC = 0 torna CPI e VAC matematicamente indeterminados —, o controle de custos opera por métricas de conformidade:

| Métrica | Fórmula/Definição | Meta | Frequência | Responsável |
| --- | --- | --- | --- | --- |
| % Dependências Auditadas | (Dependências com licença verificada / Total de dependências) × 100 | 100% | Por commit (CI, conforme pipeline definido no Plano de Integração) | Pipeline + GP |
| Desvios de Licenciamento | Número de dependências com licença não-OSI ou incompatível | 0 | Contínuo | GP |
| Custo Financeiro Acumulado | Soma de todos os gastos realizados | R$ 0,00 | Semanal | GP (self-report) |
| Alternativas FOSS Mapeadas | Número de ferramentas críticas com ≥1 alternativa FOSS identificada | ≥2 por ferramenta crítica | M2 | Equipe |

Gatilhos de ação corretiva:

- Se `% Dependências Auditadas` < 100% → bloqueio de merge até auditoria concluída
- Se `Desvios de Licenciamento` > 0 → remoção imediata da dependência + `change-request`
- Se `Custo Financeiro Acumulado` > R$ 0,00 → reembolso imediato pela equipe + lição aprendida

> **[PLACEHOLDER — EXCLUSÃO JUSTIFICADA: Fig. 4.2 — Dashboard de Conformidade FOSS | Seção 4.4 | Decisão: não será produzido. Justificativa GMV: o GitHub Dependency Graph já fornece visibilidade nativa de licenças, vulnerabilidades e dependências sem overhead documental adicional. Alternativa: evidência visual será capturada diretamente do GitHub Insights quando solicitada pelo Prof. Dr. Nivaldo Carleto em avaliação.]**

### 4.5 Regras de Conformidade FOSS

#### 4.5.1 Licenças Aprovadas (Whitelist)

Apenas as seguintes licenças são permitidas no projeto COGME, conforme ADR-001 e EAP N1.4:

| Licença | Família | Restrições |
| --- | --- | --- |
| MIT | Permissiva | Nenhuma |
| Apache 2.0 | Permissiva | Nenhuma |
| BSD (2-clause, 3-clause) | Permissiva | Nenhuma |
| GPL v2/v3 | Copyleft | Exige que derivativos também sejam GPL (aceitável para MVP acadêmico) |
| LGPL | Copyleft fraco | Incluída para completude da whitelist FOSS acadêmica; sem uso previsto no MVP |
| ISC | Permissiva | Equivalente à MIT |
| PSF (Python Software Foundation) | Permissiva | Adicionada para Python 3.11 (ADR-001) |
| Public Domain | Domínio público | Adicionada para SQLite (ADR-001) |

Licenças proibidas (Blacklist):

- ❌ Proprietárias / Comerciais
- ❌ Shareware / Freeware (sem código-fonte)
- ❌ Creative Commons (não é licença de software)
- ❌ Licenças "Source Available" não-OSI (ex: SSPL, BSL)
- ❌ Licenças com restrições de uso comercial (violam definição OSI)

#### 4.5.2 Governança da Auditoria de Licenças

Delimitação de fronteiras (Área 4 vs Área 5): Este plano estabelece a governança sobre conformidade FOSS (prevenção de custos ocultos por licenciamento inadequado), enquanto o Plano de Qualidade (Área 5) governa testes automatizados, coverage ≥ 80% e UAT (REQ-08 a REQ-10). A auditoria de licenças é compartilhada operacionalmente, mas a definição de whitelist/blacklist e os gatilhos de conformidade pertencem exclusivamente a esta Área de Custos, por derivação direta da Restrição TAP §8.4.

A execução operacional da auditoria de licenças é realizada pela Fase N4.4 da EAP (conforme Plano de Escopo §2.5), fundamentada na Política de Licenciamento da Fase N1.4. Este plano não duplica procedimentos operacionais de auditoria — estabelece a governança sobre N1.4 e N4.4:

| Aspecto de Governança | Definição |
| --- | --- |
| Responsável pela execução | Equipe técnica (conforme EAP N4.4) |
| Responsável pela supervisão | GP |
| Frequência mínima | Por marco (M1–M4) + revalidação a cada nova dependência |
| Artefato de saída | /docs/dependencias/registro.md (conforme EAP N4.4) |
| Critério de aceite | 100% das dependências com licença OSI-approved verificada |
| Gatilho de escalation | Qualquer dependência não-conforme → change-request imediato (Integração §1.7) |

> **[PLACEHOLDER — TABELA/DIAGRAMA: Fig. 4.3 — Matriz de Rastreabilidade de Dependências | Seção 4.5.2 | Conteúdo obrigatório: tabela visual com 6 exemplos reais da stack (FastAPI ≥0.100 MIT; SQLite 3.x Public Domain; WeasyPrint ≥59.0 BSD-3; pytest ≥7.0 MIT; GitHub Actions Free Tier proprietário gratuito; llama.cpp 0.4.0-dev MIT), usando ícones ✅ para conformes, com colunas: Dependência, Versão, Licença, Conformidade, EAP N1.4/N4.4, ADR-001. Necessidade real: demonstra ao avaliador que "custo zero" é auditável e rastreável, não apenas declarado.]**

### 4.6 Gestão de Mudanças de Custos

Qualquer alteração que possa impactar a linha de base de custos (mesmo que o impacto seja R$ 0,00) segue o fluxo do Plano de Integração §1.7:

| Tipo de Mudança | Exemplo | Nível de Formalidade |
| --- | --- | --- |
| Adição de dependência FOSS | Incluir biblioteca httpx para chamadas HTTP assíncronas | Registro em commit + atualização de /docs/dependencias/registro.md |
| Troca de ferramenta FOSS | Substituir FastAPI por Flask | ADR específica (gatilho G2 — irreversibilidade prática) |
| Mudança de licença de dependência existente | Biblioteca X migra de MIT para licença proprietária | change-request + substituição imediata + ADR |
| Violação acidental de conformidade | Dependência com licença não-OSI incorporada sem auditoria | change-request + remoção + lição aprendida |

Regra de escalation: Se uma dependência crítica (ex: FastAPI, SQLite) mudar de licença para não-FOSS durante o projeto, e não houver alternativa viável:

1. GP aciona `change-request` imediato
2. Avalia redução de escopo (remoção da funcionalidade dependente)
3. Comunica ao Prof. Dr. Nivaldo Carleto no marco subsequente
4. Registra como risco materializado (Plano de Riscos, M2)

### 4.7 Premissas e Restrições Aplicáveis

Premissas:

- P2 (FOSS absoluto): Todas as ferramentas necessárias estão disponíveis sob licenças OSI-approved
- P6 (Hardware adequado): Não há necessidade de infraestrutura de nuvem paga
- P9 (Separação ontológica): O TAP é referência autorizativa congelada; este plano é leitura operacional que pode divergir textualmente sem constituir correção do TAP
- PA-C1 (Free Tier sustentável): APIs e serviços gratuitos (ex: GitHub Actions Free Tier) permanecem disponíveis durante todo o ciclo de vida

Restrições:

- TAP §8.4: Proibição absoluta de aquisições pagas
- TAP §11: Linha de base de custos = R$ 0,00 (imutável sem CCB)
- TAP §3 (Inovação): 100% das ferramentas devem ser FOSS ou Free Tier

### 4.8 Condições de Fracasso e Escalation

Derivadas do TAP §3.3, com distinção entre gatilhos de alerta preventivo (internos) e condições formais de fracasso (TAP):

| Tipo | Gatilho | Limiar | Ação | Base |
| --- | --- | --- | --- | --- |
| Alerta preventivo | Dependências não-OSI detectadas | > 5% | Auditoria emergencial + substituição ≤ 48h | GP (interno) |
| Fracasso formal | Dependências incompatíveis com FOSS | > 30% | Condição de não sucesso do projeto | TAP §3.3.e |
| Alerta preventivo | Custo financeiro > R$ 0,00 | Qualquer valor | Reembolso imediato + lição aprendida | GP (interno) |
| Alerta preventivo | Dependência crítica sem alternativa FOSS | 1 ocorrência | Redução de escopo + ADR ≤ 72h | GP + CCB |
| Fracasso formal | Falha na auditoria em 2 marcos consecutivos | 2 marcos | Revisão de processo + treinamento | GP |

Nota de reconciliação (NC-C2): O limiar de 5% é um gatilho de alerta preventivo interno, mais restritivo que a condição formal de fracasso do TAP §3.3.e (30%). A intenção é detectar desvios precocemente, permitindo ação corretiva antes que o limiar formal seja atingido. Trade-off: maior rigor operacional em troca de margem de segurança.

### 4.9 Declaração de Rastreabilidade

| Seção | Origem no TAP | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 4.1 (Propósito; freeze) | §11 + §8 + Premissa P9 | Planejamento + Entrega | 7.1 |
| 4.2 (Abordagem) | §3 (Inovação) + §8 + EAP N1.4, N4.1 | Abordagem de Desenvolvimento | 7.1 |
| 4.3 (Linha de Base) | §11 (Orçamento Zero) | Planejamento | 7.3 |
| 4.4 (Métricas) | §3 (Métricas) + §11 + ADR-003 | Medição | 7.4 (substituição) |
| 4.5 (Conformidade FOSS) | §3 (Inovação) + §8 + ADR-001 | Entrega | 8.3 (controle aplicado) |
| 4.6 (Mudanças) | §3.3 + §10 + Integração §1.7 | Incerteza | 4.6 + 7.4 |
| 4.8 (Fracasso) | §3.3.e (30%) + §3.2.b | Incerteza + Entrega | 7.4 |

Verificação: 100% das seções possuem rastreabilidade a ao menos uma premissa, restrição ou objetivo SMART do TAP.

### 4.10 Notas de Contexto e Registro de Saneamento dos Artefatos Vivos

**NC-C1 — Inaplicabilidade de Processos 7.2–7.4 do PMBOK 6ª:**
Este plano declara formalmente que os processos "Estimar Custos" (7.2), "Determinar Orçamento" (7.3) e "Controlar Custos" (7.4) são inaplicáveis no sentido tradicional, pois a linha de base é R$ 0,00. O plano substitui estes processos por: (a) governança sobre conformidade FOSS (N1.4 + N4.4), (b) prevenção de desvios de licenciamento, (c) métricas de conformidade (§4.4). Esta substituição é fundamentada na ADR-003 (EVM LEGADO) e é defensável academicamente pelo Domínio de Medição do PMBOK 7ª (métricas adaptadas ao contexto) e pela Restrição TAP §11.

**NC-C2 — Delimitação de Fronteiras (Área 4 vs Área 5 vs Escopo):**
A Fase N1.4 (Política de Licenciamento FOSS) e a Fase N4.4 (Auditoria de Licenças) são os artefatos canônicos de execução da conformidade FOSS. Este plano de custos estabelece exclusivamente a governança sobre N1.4 e N4.4 (whitelist/blacklist, gatilhos, métricas, escalation), sem duplicar procedimentos operacionais. Invasão de escopo prevenida por referência cruzada: "Conforme EAP N1.4 (política) e N4.4 (auditoria), governado por este plano §4.5". O Plano de Qualidade (Área 5) governa critérios de aceite de testes (coverage ≥ 80%, UAT), não conformidade de licenças.

**NC-C3 — Numeração de Processos no Glossário:**
O Glossário registra incorretamente "Processo 6.4 Estimar Custos". A numeração canônica é: Área 7 (Custos), Processo 7.2 (Estimar Custos). Esta inconsistência é registrada para saneamento na próxima revisão do Glossário (pós-M1).

**NC-C4 — Regime de Freeze do TAP (Diretriz D3):**
O TAP é referência autorizativa congelada (última versão: 18/09/2026, anterior a todos os planos). Divergências textuais entre este plano e o TAP são leituras operacionais, não correções do termo autorizativo. Toda divergência é registrada como Nota de Contexto nesta seção. Fontes: TAP Controle de Versões; Premissa P9; Glossário §11; PMBOK 6ª §4.1.

### Controle de Versões — Seção 4

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 21/09/2026 | Emissão inicial: abordagem de custo zero, conformidade FOSS, métricas de substituição de EVM, FIG-1 e FIG-3 | Leonardo D. S. Setti |
| 1.1 | 21/09/2026 | Revisão crítica: P9 e Domínio de Medição incluídos; §4.5.2 reescrita como governança sobre N4.4; NC-C4 (freeze do TAP) adicionada; reservas rejustificadas; ADR-003 referenciada; LGPL rejustificada; CCB com fonte TAP v3 §1.c | Leonardo D. S. Setti |
| 1.2 | 21/09/2026 | Refinamento final: N1.4 adicionada como fonte canônica junto a N4.4; whitelist expandida com PSF e Public Domain (ADR-001); delimitação de fronteiras com Qualidade inserida; FIG-2 reclassificada de "opcional" para "excluída" com justificativa GMV; NC-C2 aprimorada; seção 4.8 reestruturada com distinção alerta/fracasso; FIG-3 com exemplos reais da stack | Leonardo D. S. Setti |

**Fim da Seção 4 — Custos | COGME v1.2**

---

## SEÇÃO 5 — QUALIDADE

**Plano de Gerenciamento da Qualidade**

Projeto: COGME — Conversor de Ganhos em Moeda Estrangeira
Versão: 1.1
Data: 21/09/2026
Autores: Leonardo David Silva Setti (GP), Fabricio de Lima Cabral, Edson Luis Silva
Stakeholder-Avaliador: Prof. Dr. Nivaldo Carleto — Fatec Taquaritinga / ADS

Este plano deriva diretamente das Premissas P1 (governança híbrida), P3 (SDD com IA auditável), P4 (código como deliverable), P5 (disponibilidade de 20h/semana) e P9 (separação ontológica TAP ≠ EAP ≠ PDCA), e das Restrições de Qualidade e Cronograma do TAP (§8.5 e §8.2), respeitando os Domínios de Medição, Entrega e Melhoria do PMBOK® 7ª edição. Aplica-se o regime de freeze do TAP e as Notas de Contexto registradas na seção 5.9 (NC-Q1 a NC-Q4).

### 5.1 Identificação e Propósito

Este Plano de Gerenciamento da Qualidade estabelece os mecanismos para garantir que o COGME atenda aos critérios de aceite técnicos: cobertura de testes ≥ 80%, UAT sem defeitos críticos/bloqueantes, e aplicação sistemática de ferramentas da qualidade (12 ciclos PDCA + 3 diagramas de Ishikawa 6M).

Função ontológica: O plano não duplica gates de qualidade do Escopo §2.6 (DoR/DoD) — operacionaliza critérios técnicos de qualidade específicos para código, testes e documentação, garantindo conformidade com REQ-08, REQ-09 e REQ-10.

Domínios PMBOK 7ª: Medição (métricas de qualidade), Entrega (critérios de aceite) e Melhoria (ciclos PDCA).

Processos PMBOK 6ª (dicionário, obsolescência declarada conforme Integração §1.2.4): 8.1 Planejar o Gerenciamento da Qualidade, 8.2 Gerenciar a Qualidade, 8.3 Controlar a Qualidade.

Trade-off declarado: Abre-se mão de burocracia documental em favor de automação (pipeline CI) e melhoria contínua (PDCA por fase), alinhado ao Princípio "Foco em Valor" (PMBOK 7ª) e ao Valor Ágil "Software funcionando sobre documentação abrangente".

### 5.2 Abordagem de Gerenciamento da Qualidade

A qualidade do COGME opera em três dimensões complementares:

| Dimensão | Objeto | Mecanismo de Controle | Fonte Canônica |
| --- | --- | --- | --- |
| Preventiva | Qualidade do código e arquitetura | Code Review + SDD com IA auditável + Clean Code | Escopo §2.6 + ADR-004 |
| Detectiva | Cobertura de testes e defeitos | Pipeline CI + pytest + coverage.py ≥ 80% | REQ-08 + N6.1 |
| Corretiva | Melhoria contínua de processo | 12 ciclos PDCA (um por fase da EAP) + Ishikawa 6M | REQ-10 + N6.3 |

Regra de ouro: Nenhum card migra para `Done` sem: (i) pipeline CI verde, (ii) coverage ≥ 80% no módulo afetado, (iii) code review aprovado, (iv) tasklist 100% concluída (se aplicável, ADR-004).

Hierarquia de resolução de conflitos (aplicada à qualidade):

1. Critérios de aceite do TAP §3.2 (coverage ≥ 80%, UAT sem defeitos críticos)
2. Clean Code e ACID (Premissa P5)
3. Conveniência técnica (preferência do desenvolvedor)

> **[PLACEHOLDER — DIAGRAMA: Fig. 5.1 — Fluxo de Garantia da Qualidade | Seção 5.2 | Conteúdo obrigatório: fluxograma vertical com gates de qualidade sequenciais, destacando revisão humana para código SDD-IA e critérios binários de aprovação. Formato sugerido: SVG, versionado em /docs/diagrams/. Necessidade real: materializa visualmente o DoD técnico, demonstrando que qualidade não é inspeção final, mas processo contínuo com gates automáticos (CI) e manuais (review).]**

### 5.3 Métricas de Qualidade

Dada a inaplicabilidade de EVM (ADR-003, Integração §1.6.2), o controle de qualidade opera por métricas técnicas automatizadas:

| Métrica | Fórmula/Definição | Meta | Frequência | Responsável |
| --- | --- | --- | --- | --- |
| Coverage | (Linhas testadas / Total de linhas) × 100 | ≥ 80% | Por push (CI) | Pipeline + GP |
| Defeitos Críticos | Número de bugs bloqueantes/críticos em UAT | 0 | Por marco (M3, M4) | GP + UAT |
| Taxa de Aprovação em Review | (PRs aprovados / Total de PRs) × 100 | ≥ 90% | Semanal | GP |
| Technical Debt Ratio | (Dívida técnica / Custo total) — estimado via SonarQube Free Tier | < 5% | Por marco | GP |
| Tempo de Resposta | Latência p95 das requisições da API | ≤ 3s | M3 (homologação) | Pipeline + Edson |

Nota (I5): SonarQube Free Tier é utilizado para análise estática de dívida técnica, em conformidade com TAP §11 (proibição de ferramentas pagas). O Free Tier fornece análise básica sem custos.

Gatilhos de ação corretiva:

- Se `Coverage` < 80% por 2 commits consecutivos → bloqueio de merge até correção
- Se `Defeitos Críticos` > 0 em UAT → retrabalho imediato + congelamento de novas features
- Se `Taxa de Aprovação em Review` < 90% por 2 semanas → retrospectiva extraordinária + revisão de padrões de código

> **[PLACEHOLDER — EXCLUSÃO JUSTIFICADA: Fig. 5.2 — Dashboard de Métricas de Qualidade | Seção 5.3 | Decisão: não será produzido. Justificativa GMV: GitHub Insights + coverage.py + pytest já fornecem visibilidade nativa sem overhead documental. Alternativa: evidências serão capturadas diretamente do GitHub Actions e relatórios de coverage quando solicitadas pelo Prof. Dr. Nivaldo Carleto em avaliação.]**

### 5.4 Critérios de Aceite Técnicos

#### 5.4.1 Código-Fonte

| Critério | Descrição | Verificação |
| --- | --- | --- |
| Clean Code | Nomes significativos, funções ≤ 20 linhas, sem duplicação > 3 linhas | Code Review + pylint/flake8 |
| Type Safety | Type hints em 100% das funções públicas (Python 3.11+) | mypy --strict (ferramenta complementar de análise estática, não parte da stack principal ADR-001) |
| Documentação Inline | Docstrings em todas as classes e funções públicas (padrão Google) | pydocstyle |
| SDD Auditável | Commits de código gerado por IA declaram co-autoria e link para prompt | Git log + .ai/handoffs/ |

Nota (I6): mypy é ferramenta complementar de análise estática de tipos, não listada na ADR-001 (stack principal). Sua utilização é opcional e recomendada para garantir type safety, sem impacto no orçamento (FOSS, MIT License).

#### 5.4.2 Testes Automatizados

| Critério | Descrição | Verificação |
| --- | --- | --- |
| Cobertura Mínima | ≥ 80% de linhas testadas (unitários + integração) | coverage.py report |
| Testes Críticos | 100% dos fluxos REQ-01 a REQ-07 cobertos | coverage branch + UAT |
| Tempo de Execução | Suite completa em ≤ 5 minutos | GitHub Actions CI (REQ-11) |
| Isolamento | Testes não dependem de ordem de execução ou estado global | pytest --random-order |

#### 5.4.3 Documentação

| Critério | Descrição | Verificação |
| --- | --- | --- |
| Rastreabilidade | 100% dos requisitos (REQ-01 a REQ-15) mapeados a cards e testes | Matriz de rastreabilidade |
| Atualização | Documentação atualizada antes do merge (código + docs no mesmo PR) | Code Review |
| Consistência | Glossário e OKB atualizados quando novos termos/decisões surgirem | Refinement semanal |

### 5.5 Ferramentas da Qualidade

#### 5.5.1 Pipeline de Integração Contínua (CI)

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

Critérios de qualidade do pipeline:

- Execução completa em ≤ 5 minutos (REQ-11)
- Falha imediata se coverage < 80%
- Bloqueio de merge se pipeline vermelho

#### 5.5.2 Ciclos PDCA por Fase da EAP

Fundamentação: Cada uma das 12 fases da EAP (N1-N12, conforme baseline TAP §4) possui um ciclo PDCA específico, garantindo melhoria contínua sem burocracia excessiva. O TAP não integra ciclos PDCA (Premissa P9).

Formato GMV: Cada PDCA é documentado em máximo 6 linhas: Problema → Ação → Responsável → Métrica → Verificação → Lição.

### 5.6 Ciclos PDCA Consolidados (12 Fases EAP)

**PDCA-N1: Iniciação e Planejamento**

| Etapa | Descrição |
| --- | --- |
| Problema | Risco de escopo mal definido ou premissas inválidas no início do projeto |
| Ação | Revisão em pares do TAP e EAP antes da submissão no M1; validação de premissas P1-P9 |
| Responsável | Leonardo (GP) + Fabricio (par) |
| Métrica | Zero inconsistências críticas identificadas pelo Prof. Dr. Nivaldo Carleto no M1 |
| Verificação | Validação acadêmica no M1 (22/09/2026) |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1.md |

**PDCA-N2: Levantamento de Requisitos**

| Etapa | Descrição |
| --- | --- |
| Problema | Requisitos ambíguos ou não rastreáveis a objetivos SMART |
| Ação | Conversão de REQ-01 a REQ-15 para formato User Story GWT (Padrão B, OKB §9.3) até M2 |
| Responsável | Edson + Leonardo (revisão) |
| Métrica | 100% dos requisitos Must (REQ-01 a REQ-09, REQ-11, REQ-15) com critérios GWT |
| Verificação | Refinement semanal (23/09, 30/09) |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1.md |

**PDCA-N3: Modelagem e Prototipação**

| Etapa | Descrição |
| --- | --- |
| Problema | Arquitetura ou DER não validados antes da implementação |
| Ação | Protótipo "Hello World" da stack (N4.1) + revisão de DER antes de N5 (Desenvolvimento) |
| Responsável | Fabricio (DER) + Edson (protótipo) |
| Métrica | Zero retrabalho de arquitetura após início de N5 |
| Verificação | Marco M2 (30/09/2026) — pipeline CI verde + DER versionado |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1.md |

**PDCA-N4: Configuração de Ambiente**

| Etapa | Descrição |
| --- | --- |
| Problema | Incompatibilidade de ferramentas FOSS ou ambiente local instável |
| Ação | Validação de stack via protótipo funcional + auditoria de licenças (N4.4) |
| Responsável | Leonardo (stack) + Edson (auditoria) |
| Métrica | 100% das dependências com licença OSI-approved (Custos §4.5) |
| Verificação | M2 (30/09/2026) — /docs/dependencias/registro.md atualizado |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF1.md |

**PDCA-N5: Desenvolvimento do Sistema**

| Etapa | Descrição |
| --- | --- |
| Problema | Código sem testes, coverage insuficiente ou SDD-IA sem revisão |
| Ação | TDD quando aplicável + code review obrigatório + tasklists Markdown (ADR-004) |
| Responsável | Todos (desenvolvedores) + GP (supervisão) |
| Métrica | Coverage ≥ 80% por módulo; 100% dos commits SDD-IA com co-autoria declarada |
| Verificação | Pipeline CI verde a cada push; Code Review antes de merge |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2.md |

**PDCA-N6: Garantia da Qualidade**

| Etapa | Descrição |
| --- | --- |
| Problema | Defeitos críticos em UAT ou coverage abaixo da meta |
| Ação | UAT estruturado com roteiro de testes + Ishikawa 6M para defeitos recorrentes (seção 5.7) |
| Responsável | Edson (UAT) + GP (Ishikawa) |
| Métrica | Zero defeitos críticos/bloqueantes; coverage ≥ 80% consolidado |
| Verificação | M3 (15/11/2026) — relatório UAT + coverage.xml |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2.md |

**PDCA-N7: DevOps e CI/CD**

| Etapa | Descrição |
| --- | --- |
| Problema | Pipeline lento (> 5min, conforme REQ-11) ou instável |
| Ação | Otimização de testes paralelos + cache de dependências |
| Responsável | Leonardo (CI) + Fabricio (otimização) |
| Métrica | Tempo de CI ≤ 5 minutos (REQ-11); taxa de sucesso ≥ 95% |
| Verificação | GitHub Actions Insights (semanal) |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2.md |

**PDCA-N8: Comunicação**

| Etapa | Descrição |
| --- | --- |
| Problema | Falhas de comunicação entre equipe ou com stakeholder |
| Ação | Daily assíncrona padronizada + refinement semanal com pauta fixa |
| Responsável | GP (facilitação) + equipe (participação) |
| Métrica | 100% das dailies realizadas; zero cards bloqueados > 48h sem comunicação |
| Verificação | GitHub Issues (daily) + GitHub Projects (refinement) |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2.md |

**PDCA-N9: Base de Conhecimento**

| Etapa | Descrição |
| --- | --- |
| Problema | ADRs tardias ou prompts SDD não catalogados |
| Ação | Catálogo de prompts em .ai/handoffs/ + ADRs emitidas antes de M2 (quando aplicável) |
| Responsável | Leonardo (ADRs) + todos (prompts) |
| Métrica | 100% dos prompts versionados; ≤ 30% de ADRs tardias |
| Verificação | /docs/decisoes/ + .ai/handoffs/ (semanal) |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF3.md |

**PDCA-N10: Gestão de Mudanças**

| Etapa | Descrição |
| --- | --- |
| Problema | Mudanças não registradas ou scope creep > 15% (Escopo §2.7, Integração §1.9) |
| Ação | Label change-request obrigatória + análise de impacto em ≤ 48h (Integração §1.7) |
| Responsável | GP (CCB) + equipe (solicitações) |
| Métrica | 100% das mudanças registradas; scope creep < 15% (Escopo §2.7) |
| Verificação | GitHub Issues com label change-request |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF2.md |

**PDCA-N11: Documentação do Projeto**

| Etapa | Descrição |
| --- | --- |
| Problema | Documentação desatualizada ou inconsistente com código |
| Ação | Código + docs no mesmo PR + revisão de consistência antes de M4 |
| Responsável | Todos (documentação) + GP (consolidação) |
| Métrica | 100% dos requisitos mapeados a docs; zero inconsistências TAP → código |
| Verificação | M4 (15/12/2026) — documentação consolidada |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF3.md |

**PDCA-N12: Encerramento**

| Etapa | Descrição |
| --- | --- |
| Problema | Lições aprendidas não consolidadas ou critérios SMART não verificados |
| Ação | Checklist de encerramento + lições finais + tag de release |
| Responsável | GP (consolidação) + equipe (lições) |
| Métrica | 100% dos critérios SMART verificados; lições consolidadas em /docs/conhecimento/ |
| Verificação | M4 (15/12/2026) — validação acadêmica + tag de release |
| Lição | A ser registrada em /docs/conhecimento/licoes-aprendidas/MF3.md |

### 5.7 Diagrama de Ishikawa 6M (3 Análises)

Fundamentação: Conforme REQ-10 e N6.3 da EAP, três diagramas de Ishikawa 6M são aplicados para análise de causa-raiz de problemas críticos de qualidade. Cada diagrama foca em um efeito indesejado específico.

Nota sobre qualidade de processo vs. produto (I3): Os dois primeiros diagramas (Coverage < 80% e Defeitos Críticos em UAT) analisam qualidade de produto. O terceiro diagrama (Cycle Time > 3 dias) analisa qualidade de processo — especificamente, eficiência do fluxo de trabalho. Ambos os tipos são ferramentas da qualidade conforme REQ-10, e a delimitação entre eles é explicitada na seção 5.8.2.

**Ishikawa-1: Coverage < 80%**

> **[PLACEHOLDER — DIAGRAMA: Fig. 5.3 — Ishikawa: Coverage Insuficiente | Seção 5.7 | Conteúdo obrigatório: diagrama 6M (Método, Mão de Obra, Máquina, Material, Medida, Meio Ambiente) com causas-raiz específicas do COGME. Formato sugerido: SVG, versionado em /docs/diagrams/. Necessidade real: permite ao GP e equipe identificar ações corretivas priorizadas (ex: tornar coverage gate obrigatório no CI) em vez de tratar sintomas.]**

Ações corretivas derivadas:

- Método: Implementar TDD obrigatório para REQ-01 a REQ-07 (críticos)
- Medida: Configurar `--cov-fail-under=80` no pipeline CI (gate bloqueante)
- Mão de Obra: Pair programming para módulos complexos (N5.1, N5.2)

**Ishikawa-2: Defeitos Críticos em UAT**

> **[PLACEHOLDER — DIAGRAMA: Fig. 5.4 — Ishikawa: Defeitos Críticos em UAT | Seção 5.7 | Conteúdo obrigatório: diagrama 6M focado em defeitos de UAT, destacando causas relacionadas a SDD-IA e validação acadêmica. Formato sugerido: SVG, versionado em /docs/diagrams/. Necessidade real: evidencia para o Prof. Dr. Nivaldo Carleto que a equipe compreende as limitações do ambiente acadêmico (usuários-piloto limitados) e propõe mitigações (UAT estruturado).]**

Ações corretivas derivadas:

- Método: Roteiro de UAT com cenários Given/When/Then para REQ-01 a REQ-07
- Mão de Obra: Code review cruzado (Fabricio revisa Edson, Edson revisa Leonardo)
- Medida: Label `bug-critical` no GitHub com template de reporte padronizado

**Ishikawa-3: Desvio de Cycle Time > 3 dias**

> **[PLACEHOLDER — DIAGRAMA: Fig. 5.5 — Ishikawa: Cycle Time Excedido | Seção 5.7 | Conteúdo obrigatório: diagrama 6M focado em gargalos de fluxo, conectando causas a ADR-002 (Kanban) e ADR-004 (tasklists). Formato sugerido: SVG, versionado em /docs/diagrams/. Necessidade real: demonstra ao avaliador que a equipe entende que "Cycle Time > 3 dias" não é falha individual, mas sistêmica, exigindo ações em múltiplas dimensões.]**

Ações corretivas derivadas:

- Método: DoR gate rigoroso (Escopo §2.6) — card sem DoR não entra em `Ready`
- Mão de Obra: Cross-training para reduzir dependência de membro único
- Medida: Publicação semanal de CFD (Integração §1.6.1) + ação corretiva se banda > 2× média

### 5.8 Gestão de Melhoria Contínua

#### 5.8.1 Retrospectivas Quinzenais

Conforme ADR-002, retrospectivas ocorrem a cada 2 semanas com pauta fixa:

1. O que funcionou bem?
2. O que pode melhorar?
3. Ações para o próximo ciclo (máximo 3)

Registro: /docs/conhecimento/licoes-aprendidas/ (MF1, MF2, MF3)

#### 5.8.2 Integração com Métricas de Fluxo

Conforme Cronograma §3.7 e Integração §1.6.1, o CFD e Cycle Time alimentam a melhoria de processo:

- CFD com banda > 2× média por 2 semanas → Retrospectiva extraordinária
- Throughput < 3 cards/semana por 2 semanas → Revisão de WIP limits (fallback ADR-002)

Fronteira com Cronograma (I4): Este plano usa métricas de fluxo como input para melhoria de qualidade de processo, não como métrica de qualidade de produto (que são coverage, defeitos, etc.). A definição formal, cadência e regra corretiva do CFD residem canonicamente em Integração §1.6.1; o monitoramento temporal detalhado reside em Cronograma §3.7.

### 5.9 Notas de Contexto e Registro de Saneamento dos Artefatos Vivos

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

| Pendência | Artefato vivo | Momento previsto |
| --- | --- | --- |
| Numeração de processos 8.1-8.3 | Glossário §3 | Próxima revisão do Glossário |
| Contagem EAP "13/48" → 12/37 | Glossário §1 | Próxima revisão do Glossário |
| Cycle Time "To Do → Done" → "In Progress → Done" | Glossário | Próxima revisão do Glossário |
| Grafia "Carleto" → "Carleto" | Glossário | Próxima revisão do Glossário |

### 5.10 Declaração de Rastreabilidade

| Seção | Origem no TAP | Domínio PMBOK 7ª | Processo PMBOK 6ª |
| --- | --- | --- | --- |
| 5.1 (Propósito; freeze) | §3.2 (Qualidade) + Premissa P9 | Medição + Entrega | 8.1 |
| 5.2 (Abordagem 3 dimensões) | §3 (Qualidade) + §8.5 | Entrega + Melhoria | 8.2 |
| 5.3 (Métricas) | §3 (Métricas) + ADR-003 | Medição | 8.3 (substituição) |
| 5.4 (Critérios técnicos) | §3.2.b + §3.2.c | Entrega | 8.3 |
| 5.5 (Ferramentas: CI) | §3 (Inovação) + N7.1 | Trabalho do Projeto | 8.2 |
| 5.6 (12 PDCAs) | §3.2.c + REQ-10 + N6.3 | Melhoria | 8.2 |
| 5.7 (Ishikawa 6M) | REQ-10 + N6.3 | Melhoria + Incerteza | 8.3 |
| 5.8 (Melhoria contínua) | ADR-002 + Integração §1.6.1 | Melhoria | 8.2 |
| 5.9 (Notas de Contexto) | Decisão do GP (21/09/2026) + Premissa P9 | Trabalho do Projeto | 4.6 (dicionário) |

Verificação: 100% das seções possuem rastreabilidade a ao menos um objetivo SMART, premissa, restrição do TAP ou REQ-08/09/10; referências cruzadas apontam exclusivamente para locais canônicos (Escopo §2.6 para DoR/DoD; Custos §4.5 para auditoria FOSS; Integração §1.6.1 para CFD).

### 5.11 Premissas e Restrições Aplicáveis

Premissas do TAP:

- P1 (governança híbrida): fundamenta §5.2
- P3 (SDD com IA auditável): fundamenta §5.4.1 (código SDD)
- P4 (código como deliverable): fundamenta §5.4 (critérios técnicos)
- P5 (20h/semana): fundamenta §5.7 (Ishikawa-3: sobrecarga)
- P9 (separação ontológica TAP ≠ EAP ≠ PDCA): fundamenta §5.6 (12 PDCAs sem TAP) e §5.9 (freeze)

Premissas específicas deste plano:

- PA-Q1: GitHub Actions Free Tier permanece disponível e estável durante todo o ciclo (TAP §11)
- PA-Q2: pytest + coverage.py são suficientes para atingir ≥ 80% de cobertura sem ferramentas pagas
- PA-Q3: Usuários-piloto (3-5 pessoas) são representativos o suficiente para UAT acadêmico (TAP §8.5)
- PA-Q4: SonarQube Free Tier permanece disponível para análise de dívida técnica (TAP §11)

Restrições:

- TAP §8.5 (Qualidade): Tempo restrito para testes → priorização de fluxos críticos (REQ-01 a REQ-07)
- TAP §8.2 (Cronograma): Prazo letivo inegociável → PDCAs enxutos (6 linhas cada, GMV)
- TAP §11 (Orçamento zero): Proibição de ferramentas pagas de qualidade (ex: SonarCloud pago)

### Controle de Versões — Seção 5

| Versão | Data | Alteração | Responsável |
| --- | --- | --- | --- |
| 1.0 | 21/09/2026 | Emissão inicial: 12 PDCAs consolidados (N1-N12); 3 diagramas Ishikawa 6M; métricas de qualidade; FIG-1, FIG-3, FIG-4, FIG-5; exclusão de FIG-2 (GMV); NC-Q1 a NC-Q4 (freeze do TAP); delimitação de fronteiras com Custos §4.5 e Cronograma §3.7 | Leonardo D. S. Setti |
| 1.1 | 21/09/2026 | Refinamento pós-review: (I1) PDCA-N10 com referência a Escopo §2.7 e Integração §1.9; (I2) PDCA-N7 com referência a REQ-11; (I3) nota sobre qualidade de processo vs. produto na introdução §5.7; (I4) referência canônica em §5.8.2; (I5) especificação "SonarQube Free Tier" em §5.3; (I6) nota sobre mypy como ferramenta complementar em §5.4.1; (E1) NC-Q5 sobre grafia do stakeholder; 4 SVGs gerados (FIG-1, FIG-3, FIG-4, FIG-5) | Leonardo D. S. Setti |

**Fim da Seção 5 — Qualidade | COGME v1.1**

---
---

# ANEXO A — ÍNDICE CONSOLIDADO DE PLACEHOLDERS DE IMAGENS E DIAGRAMAS

> Este índice consolida todos os pontos de inserção de imagens/diagramas para atualização manual. Todos os diagramas (incluindo os originalmente em Mermaid ou SVG) foram substituídos por placeholders padronizados ao longo da Parte II.

| # | Placeholder | Seção | Título | Formato sugerido |
| --- | --- | --- | --- | --- |
| 1 | Fig. 0.1 | 0.4 | EAP Visão Executiva (N0 + 12 fases × 3 macro-fases) | Mermaid flowchart TB / PlantUML WBS |
| 2 | Fig. 1.1 | 1.2 | Modelo de Governança Híbrida Trifásico | Mermaid flowchart TB / PlantUML |
| 3 | Fig. 1.2 | 1.3.1 | Fluxo Kanban Oficial com WIP Limits e gates | Mermaid flowchart LR |
| 4 | Fig. 1.3 | 1.6.1 | CFD: Padrão Saudável vs. Padrão com Gargalo | PNG/SVG (dados simulados) |
| 5 | Fig. 1.4 | 1.7.2 | Fluxo de Controle Integrado de Mudanças | Mermaid flowchart TD |
| 6 | Fig. 2.1 | 2.5 | EAP do COGME — visão executiva | Mermaid flowchart TB / PlantUML WBS |
| 7 | Fig. 2.2 | 2.5 | Cadeia de decomposição do escopo e gates de qualidade | Mermaid flowchart LR |
| 8 | Fig. 3.1 | 3.4 | Sequenciamento macro e caminho crítico empírico | Mermaid flowchart LR |
| 9 | Fig. 3.2 | 3.6 | Roadmap macro do cronograma | Mermaid gantt / timeline |
| 10 | Fig. 4.1 | 4.2 | Fluxo de Prevenção de Custos | Mermaid flowchart TD |
| 11 | Fig. 4.2 | 4.4 | Dashboard de Conformidade FOSS — **EXCLUÍDA (GMV)** | N/A |
| 12 | Fig. 4.3 | 4.5.2 | Matriz de Rastreabilidade de Dependências | Tabela Markdown / SVG |
| 13 | Fig. 5.1 | 5.2 | Fluxo de Garantia da Qualidade | SVG |
| 14 | Fig. 5.2 | 5.3 | Dashboard de Métricas de Qualidade — **EXCLUÍDA (GMV)** | N/A |
| 15 | Fig. 5.3 | 5.7 | Ishikawa 6M: Coverage Insuficiente | SVG |
| 16 | Fig. 5.4 | 5.7 | Ishikawa 6M: Defeitos Críticos em UAT | SVG |
| 17 | Fig. 5.5 | 5.7 | Ishikawa 6M: Cycle Time Excedido | SVG |

---

# NOTA DE ENCERRAMENTO DO GP

**Status geral da consolidação:** O documento agora apresenta uma redação contínua e rastreável desde a Introdução (TAP + EAP integral) até a Área 5 — Qualidade, com todas as notas de revisão segregadas na Parte I e todos os pontos de diagrama substituídos por placeholders padronizados (Anexo A).

**Sinalizações obrigatórias ao GP:**

1. **Correção aplicada na instrução:** "4 Integração" → **4 Custos** (erro material de digitação identificado e corrigido, preservando a sequência real das áreas de conhecimento).
2. **Rastreabilidade preservada:** TAP → Escopo → EAP → Cronograma → Custos → Qualidade mantida integralmente; 100% das seções dos cinco planos possuem declaração de rastreabilidade ao TAP.
3. **Regime de freeze do TAP respeitado:** nenhuma Nota de Contexto propõe alteração do TAP; divergências são registradas exclusivamente como leituras operacionais (NC-00 a NC-06, NC-C1 a NC-C4, NC-Q1 a NC-Q5).
4. **Pendência única aberta:** deliberação do GP sobre o micro-ajuste opcional na Integração §1.3.2 (reforço de rastreabilidade do DoD), registrado em NR-6.
5. **Ação recomendada:** emitir ADR-005 (regime de freeze + precedência do §6 Marcos + Notas de Contexto) antes do M2, conforme encaminhamento da Seção 3.

**Fim do documento consolidado — COGME | Fatec Taquaritinga | Áreas 1–5 (M1).**

# Proposta de Reestruturação Formal do Repositório COGME

## 1. Análise Crítica da Estrutura Atual

A estrutura atual (106 arquivos em 23 diretórios) apresenta **fragmentação por formato** (.docx, .md, .xml) em vez de **organização por função documental**, violando os princípios de SSOT (Single Source of Truth) e GMV (Governança Mínima Viável) declarados no OKB v3.0 §3.1 e no Plano de Integração §1.3.

**Problemas identificados**:
- EAP espalhada em 3 locais (`docs/md/TAP/EAP/`, `docs/xml/EAP_TAP/`, `docs/docx/_archive/`)
- TAP fragmentado em 7 seções (sec_1, sec_4, sec_6, sec_9, sec_10, sec_11, smart)
- Arquivos de trabalho (drafts) misturados com artefatos canônicos
- Ausência de estrutura `.ai/` (stack SDD canônica — Glossário §5)
- Ausência de estrutura para código-fonte (`src/`, `tests/`)
- Diagramas deprecated misturados com diagramas ativos

---

## 2. Estrutura Canônica Proposta

A estrutura abaixo deriva diretamente do **OKB v3.0 §3.3** (arquitetura de integração documental), **Glossário v3.1 §5** (stack SDD local) e **§14** (estrutura documental completa), respeitando a **Premissa P9** (separação ontológica TAP ≠ EAP ≠ PDCA).

~~~
COGME/
├── .ai/                              # Contexto SDD (lido pela IA — Glossário §5)
│   ├── personas/                     # Personas SDD (symlinks → active.md)
│   │   ├── _base.md                  # Instruções base compartilhadas
│   │   ├── pm.md                     # Persona: Gerente de Projeto
│   │   ├── coder.md                  # Persona: Desenvolvedor
│   │   ├── reviewer.md               # Persona: Revisor
│   │   ├── tester.md                 # Persona: Testador
│   │   └── active.md → pm.md         # Symlink para persona ativa
│   ├── specs/                        # Especificações imutáveis (Glossário §5)
│   │   ├── tap.md                    # TAP consolidado (referência para IA)
│   │   ├── eap.md                    # EAP em formato machine-readable
│   │   └── requisitos.md             # REQ-01 a REQ-15 consolidados
│   ├── handoffs/                     # Artefatos entre fases SDD (Glossário §5)
│   │   └── 001-tap-foundation.md     # Exemplo: handoff da MF1
│   └── workflows/                    # Automação bash do ciclo SDD
│       └── sdd-cycle.sh              # Script ~30 linhas (Glossário §5)
│
├── docs/                             # Documentação humana (NÃO lida pela IA)
│   ├── planos/                       # 8 planos de gerenciamento (OKB §3.3)
│   │   ├── plano-integracao.md       # Área 1 — M1 ✅
│   │   ├── plano-escopo.md           # Área 2 — M1 ✅
│   │   ├── plano-cronograma.md       # Área 3 — M1 ✅
│   │   ├── plano-custos.md           # Área 4 — M1 ✅
│   │   ├── plano-qualidade.md        # Área 5 — M1 ✅
│   │   ├── plano-recursos.md         # Área 6 — M2 ⏳
│   │   ├── plano-comunicacoes.md     # Área 7 — M2 ⏳
│   │   └── plano-riscos.md           # Área 8 — M2 ⏳
│   │
│   ├── decisoes/                     # ADRs (OKB §3.3)
│   │   ├── ADR-001-stack.md          # Stack tecnológica FOSS ✅
│   │   ├── ADR-002-kanban.md         # Kanban como método ✅
│   │   ├── ADR-003-metricas.md       # Métricas de fluxo ✅
│   │   ├── ADR-004-tasklists.md      # Tasklists Markdown ✅
│   │   └── ADR-005-freeze.md         # Regime de freeze do TAP ⏳ (antes do M2)
│   │
│   ├── conhecimento/                 # Base de conhecimento (OKB §3.3)
│   │   ├── OKB.md                    # Operational Knowledge Base ✅
│   │   ├── glossario.md              # Glossário canônico ✅
│   │   └── licoes-aprendidas/        # Lições por macro-fase
│   │       ├── MF1-licoes.md         # ⏳ (30/09)
│   │       ├── MF2-licoes.md         # ⏳ (15/11)
│   │       └── MF3-licoes.md         # ⏳ (15/12)
│   │
│   ├── metricas/                     # Dados empíricos (OKB §3.3)
│   │   └── baseline.md               # Baseline de fluxo ⏳ (pós 03/10)
│   │
│   ├── requisitos/                   # Requisitos consolidados (OKB §3.3)
│   │   └── requisitos.md             # REQ-01 a REQ-15 ⏳ (M2)
│   │
│   ├── diagramas/                    # Diagramas dos planos (OKB §3.3)
│   │   ├── integracao/               # FIG-1 a FIG-4 do Plano de Integração
│   │   │   ├── fig-01-governanca-hibrida.svg
│   │   │   ├── fig-01-governanca-hibrida.png
│   │   │   ├── fig-02-fluxo-kanban.svg
│   │   │   ├── fig-02-fluxo-kanban.png
│   │   │   ├── fig-03-cfd-comparativo.svg
│   │   │   ├── fig-03-cfd-comparativo.png
│   │   │   ├── fig-04-fluxo-mudancas.svg
│   │   │   └── fig-04-fluxo-mudancas.png
│   │   ├── qualidade/                # FIG-1, FIG-5, FIG-6, FIG-7 do Plano de Qualidade
│   │   │   ├── fig-01-fluxo-qualidade.svg
│   │   │   ├── fig-01-fluxo-qualidade.png
│   │   │   ├── fig-05-ishikawa-coverage.svg
│   │   │   ├── fig-05-ishikawa-coverage.png
│   │   │   ├── fig-06-ishikawa-uat.svg
│   │   │   ├── fig-06-ishikawa-uat.png
│   │   │   ├── fig-07-ishikawa-cycletime.svg
│   │   │   └── fig-07-ishikawa-cycletime.png
│   │   ├── eap/                      # Diagramas EAP (drawio + png)
│   │   │   ├── EAP_COGME_v3.0_Principal.drawio
│   │   │   ├── EAP_COGME_v3.0_Principal.drawio.png
│   │   │   ├── EAP_COGME_v3.0_MF1_Fundacao.drawio
│   │   │   ├── EAP_COGME_v3.0_MF1_Fundacao.drawio.png
│   │   │   ├── EAP_COGME_v3.0_MF2_Construcao.drawio
│   │   │   ├── EAP_COGME_v3.0_MF2_Construcao.drawio.png
│   │   │   ├── EAP_COGME_v3.0_MF3_Consolidacao.drawio
│   │   │   └── EAP_COGME_v3.0_MF3_Consolidacao.drawio.png
│   │   └── mermaid-config.json       # Configuração Mermaid
│   │
│   ├── tap/                          # Termo de Abertura (congelado — Premissa P9)
│   │   ├── TAP.md                    # Versão canônica consolidada (criar)
│   │   └── TAP.docx                  # Versão Word (submissão acadêmica)
│   │
│   ├── dependencias/                 # Registro de conformidade FOSS (Plano de Custos §4.5.2)
│   │   └── registro.md               # ⏳ (M2)
│   │
│   └── archive/                      # Artefatos históricos (NÃO canônicos)
│       ├── docx/                     # Versões Word antigas dos planos
│       │   ├── AC1_Integracao.docx
│       │   ├── AC2_Escopo.docx
│       │   ├── AC3_cronograma.docx
│       │   ├── AC4_Custos.docx
│       │   ├── AC_qualidade.docx
│       │   └── _archive/             # Archive do archive (templates antigos)
│       │       ├── Modelo-para-elaboracao-de-Monografia.docx
│       │       ├── Modelo-Projeto-COGME.docx
│       │       ├── TAP_EAP.docx
│       │       ├── Termo de Abertura do Projeto v1.doc
│       │       ├── Termo de Abertura do Projeto v1.docx
│       │       └── Termo de Abertura do Projeto v1_opngoing.docx
│       │
│       ├── drafts/                   # Arquivos de trabalho (não canônicos)
│       │   ├── redacao_progressiva.md
│       │   ├── notas_adjacentes.md
│       │   ├── refac_prompt.md
│       │   ├── estrutura-de-diretorios.md
│       │   ├── monitoramenteo_inconsistencias.md
│       │   ├── premissas.md
│       │   ├── principais_requisitos_entregas.md
│       │   ├── proposta_estrutural.md
│       │   ├── reestrutura_EAP.md
│       │   ├── support_research.md
│       │   ├── req_1.0.docx
│       │   ├── sec_4_EAP.docx
│       │   ├── analise_arquitetural.md
│       │   ├── Canon_Stack_SDD.md
│       │   ├── hardware.md
│       │   ├── llm_base_persona.md
│       │   ├── relatorio_avaliacao_critica_TAP.md
│       │   └── Relat_Transicao_TAP_AreasConhecimento.md
│       │
│       ├── tap-sections/             # Seções fragmentadas do TAP (históricas)
│       │   ├── sec_1_objetivos.md
│       │   ├── sec_1_objetivos.docx
│       │   ├── sec_4_EAP.md
│       │   ├── sec_6.md
│       │   ├── sec_6.docx
│       │   ├── sec_9_premissas.md
│       │   ├── sec_9_premissas.docx
│       │   ├── sec_10_riscos.md
│       │   ├── sec_10_riscos.docx
│       │   ├── sec_11_orcamento.md
│       │   ├── sec_11_orcamento.docx
│       │   ├── smart.md
│       │   ├── smart.docx
│       │   ├── req_1.0.md
│       │   └── review_TAP.md
│       │
│       ├── eap-legacy/               # Versões antigas da EAP
│       │   ├── correcao/
│       │   │   ├── EAP_COGME_MF1_Fundacao.drawio
│       │   │   ├── EAP_COGME_MF1_Fundacao.drawio.png
│       │   │   ├── EAP_COGME_MF2_Construcao.drawio
│       │   │   ├── EAP_COGME_MF2_Construcao.drawio.png
│       │   │   ├── EAP_COGME_MF3_Consolidacao.drawio
│       │   │   ├── EAP_COGME_MF3_Consolidacao.drawio.png
│       │   │   ├── EAP_COGME_Principal.drawio
│       │   │   ├── EAP_COGME_Principal.drawio.png
│       │   │   ├── EAP_estruturada_correcao.md
│       │   │   ├── EAP_v2.0.docx
│       │   │   └── EAP_v2.0.md
│       │   └── inicial/
│       │       ├── MF1_fundacao.drawio
│       │       ├── MF1_fundacao.drawio.png
│       │       ├── MF2_construcao.drawio
│       │       ├── MF2_construcao.drawio.png
│       │       ├── MF3_consolidacao.drawio
│       │       ├── MF3_consolidacao.drawio.png
│       │       ├── principal.drawio
│       │       └── principal.drawio.png
│       │
│       ├── diagrams-deprecated/      # Diagramas obsoletos
│       │   ├── _fig-01-governanca-hibrida(deprecated).svg
│       │   ├── fig-02-fluxo-kanban_alt.png
│       │   ├── fig-02-fluxo-kanban_alt.svg
│       │   └── fig-1-fluxo-qualidade.png
│       │
│       └── images-legacy/            # Imagens soltas históricas
│           └── 1789852046492.png
│
├── src/                              # Código-fonte (MVP — M2/M3)
│   ├── backend/                      # FastAPI + SQLite
│   │   ├── main.py
│   │   ├── routers/
│   │   ├── models/
│   │   └── services/
│   ├── frontend/                     # HTML + HTMX + Tailwind
│   │   ├── templates/
│   │   └── static/
│   └── shared/                       # Modelos compartilhados
│       └── schemas.py
│
├── tests/                            # Testes automatizados (REQ-08)
│   ├── unit/
│   └── integration/
│
├── .github/                          # CI/CD + templates (REQ-11)
│   └── workflows/
│       └── ci.yml
│
├── README.md                         # Raiz (canônico)
├── LICENSE                           # Raiz (canônico — MIT)
├── .gitignore                        # Ignorar .ai/personas/active.md, __pycache__, etc.
├── .editorconfig                     # Padronização de formatação
├── requirements.txt                  # Dependências Python
└── pyproject.toml                    # Configuração do projeto
~~~

---

## 3. Mapeamento Completo: Arquivo Atual → Novo Local

### 3.1 Arquivos Canônicos (mantidos ou movidos para localização primária)

| Arquivo Atual | Novo Local | Justificativa |
|---------------|------------|---------------|
| `README.md` | `/README.md` | Mantido na raiz |
| `LICENSE` | `/LICENSE` | Mantido na raiz |
| `glossario.md` | `/docs/conhecimento/glossario.md` | OKB §3.3 |
| `OKB.md` | `/docs/conhecimento/OKB.md` | OKB §3.3 |

### 3.2 Planos de Gerenciamento (docs/md/planos/AC_* → docs/planos/)

| Arquivo Atual | Novo Local |
|---------------|------------|
| `docs/md/planos/AC_integracao/AC1_Integracao.md` | `docs/planos/plano-integracao.md` |
| `docs/md/planos/AC_Escopo/AC2_Escopo.md` | `docs/planos/plano-escopo.md` |
| `docs/md/planos/AC_Cronograma/AC3_cronograma.md` | `docs/planos/plano-cronograma.md` |
| `docs/md/planos/AC_custos/AC4_Custos.md` | `docs/planos/plano-custos.md` |
| `docs/md/planos/AC_qualidade/AC_qualidade.md` | `docs/planos/plano-qualidade.md` |

### 3.3 Diagramas (docs/diagrams/ → docs/diagramas/ por plano)

| Arquivo Atual | Novo Local |
|---------------|------------|
| `docs/diagrams/fig-01-governanca-hibrida.svg` | `docs/diagramas/integracao/fig-01-governanca-hibrida.svg` |
| `docs/diagrams/fig-01-governanca-hibrida.png` | `docs/diagramas/integracao/fig-01-governanca-hibrida.png` |
| `docs/diagrams/fig-02-fluxo-kanban.svg` | `docs/diagramas/integracao/fig-02-fluxo-kanban.svg` |
| `docs/diagrams/fig-02-fluxo-kanban.png` | `docs/diagramas/integracao/fig-02-fluxo-kanban.png` |
| `docs/diagrams/fig-03-cfd-comparativo.svg` | `docs/diagramas/integracao/fig-03-cfd-comparativo.svg` |
| `docs/diagrams/fig-03-cfd-comparativo.png` | `docs/diagramas/integracao/fig-03-cfd-comparativo.png` |
| `docs/diagrams/fig-04-fluxo-mudancas.svg` | `docs/diagramas/integracao/fig-04-fluxo-mudancas.svg` |
| `docs/diagrams/fig-04-fluxo-mudancas.png` | `docs/diagramas/integracao/fig-04-fluxo-mudancas.png` |
| `docs/diagrams/fig-01-fluxo-qualidade.svg` | `docs/diagramas/qualidade/fig-01-fluxo-qualidade.svg` |
| `docs/diagrams/fig-01-fluxo-qualidade.png` | `docs/diagramas/qualidade/fig-01-fluxo-qualidade.png` |
| `docs/diagrams/fig-05-ishikawa-coverage.svg` | `docs/diagramas/qualidade/fig-05-ishikawa-coverage.svg` |
| `docs/diagrams/fig-05-ishikawa-coverage.png` | `docs/diagramas/qualidade/fig-05-ishikawa-coverage.png` |
| `docs/diagrams/fig-06-ishikawa-uat.svg` | `docs/diagramas/qualidade/fig-06-ishikawa-uat.svg` |
| `docs/diagrams/fig-06-ishikawa-uat.png` | `docs/diagramas/qualidade/fig-06-ishikawa-uat.png` |
| `docs/diagrams/fig-07-ishikawa-cycletime.svg` | `docs/diagramas/qualidade/fig-07-ishikawa-cycletime.svg` |
| `docs/diagrams/fig-07-ishikawa-cycletime.png` | `docs/diagramas/qualidade/fig-07-ishikawa-cycletime.png` |
| `docs/diagrams/mermaid-config.json` | `docs/diagramas/mermaid-config.json` |

### 3.4 EAP Canônica (docs/md/TAP/EAP/ → docs/diagramas/eap/)

| Arquivo Atual | Novo Local |
|---------------|------------|
| `docs/md/TAP/EAP/EAP_COGME_v3.0_Principal.drawio` | `docs/diagramas/eap/EAP_COGME_v3.0_Principal.drawio` |
| `docs/md/TAP/EAP/EAP_COGME_v3.0_Principal.drawio.png` | `docs/diagramas/eap/EAP_COGME_v3.0_Principal.drawio.png` |
| `docs/md/TAP/EAP/EAP_COGME_v3.0_MF1_Fundacao.drawio` | `docs/diagramas/eap/EAP_COGME_v3.0_MF1_Fundacao.drawio` |
| `docs/md/TAP/EAP/EAP_COGME_v3.0_MF1_Fundacao.drawio.png` | `docs/diagramas/eap/EAP_COGME_v3.0_MF1_Fundacao.drawio.png` |
| `docs/md/TAP/EAP/EAP_COGME_v3.0_MF2_Construcao.drawio` | `docs/diagramas/eap/EAP_COGME_v3.0_MF2_Construcao.drawio` |
| `docs/md/TAP/EAP/EAP_COGME_v3.0_MF2_Construcao.drawio.png` | `docs/diagramas/eap/EAP_COGME_v3.0_MF2_Construcao.drawio.png` |
| `docs/md/TAP/EAP/EAP_COGME_v3.0_MF3_Consolidacao.drawio` | `docs/diagramas/eap/EAP_COGME_v3.0_MF3_Consolidacao.drawio` |
| `docs/md/TAP/EAP/EAP_COGME_v3.0_MF3_Consolidacao.drawio.png` | `docs/diagramas/eap/EAP_COGME_v3.0_MF3_Consolidacao.drawio.png` |

### 3.5 TAP Consolidado (criar docs/tap/)

| Ação | Arquivo |
|------|---------|
| **Criar** | `docs/tap/TAP.md` (consolidar todas as seções: sec_1, sec_4, sec_6, sec_9, sec_10, sec_11, smart) |
| Mover | `docs/docx/Termo-de-Abertura-do-Projeto.docx` → `docs/tap/TAP.docx` |

### 3.6 Arquivos de Trabalho (raiz + docs/md/ → docs/archive/drafts/)

| Arquivo Atual | Novo Local |
|---------------|------------|
| `redacao_progressiva.md` | `docs/archive/drafts/redacao_progressiva.md` |
| `notas_adjacentes.md` | `docs/archive/drafts/notas_adjacentes.md` |
| `refac_prompt.md` | `docs/archive/drafts/refac_prompt.md` |
| `estrutura-de-diretorios.md` | `docs/archive/drafts/estrutura-de-diretorios.md` |
| `docs/md/monitoramenteo_inconsistencias.md` | `docs/archive/drafts/monitoramenteo_inconsistencias.md` |
| `docs/md/premissas.md` | `docs/archive/drafts/premissas.md` |
| `docs/md/principais_requisitos_entregas.md` | `docs/archive/drafts/principais_requisitos_entregas.md` |
| `docs/md/proposta_estrutural.md` | `docs/archive/drafts/proposta_estrutural.md` |
| `docs/md/reestrutura_EAP.md` | `docs/archive/drafts/reestrutura_EAP.md` |
| `docs/md/support_research.md` | `docs/archive/drafts/support_research.md` |
| `docs/md/req_1.0.docx` | `docs/archive/drafts/req_1.0.docx` |
| `docs/md/sec_4_EAP.docx` | `docs/archive/drafts/sec_4_EAP.docx` |
| `docs/md/relatorios/analise_arquitetural.md` | `docs/archive/drafts/analise_arquitetural.md` |
| `docs/md/relatorios/Canon_Stack_SDD.md` | `docs/archive/drafts/Canon_Stack_SDD.md` |
| `docs/md/relatorios/hardware.md` | `docs/archive/drafts/hardware.md` |
| `docs/md/relatorios/llm_base_persona.md` | `docs/archive/drafts/llm_base_persona.md` |
| `docs/md/relatorios/relatorio_avaliacao_critica_TAP.md` | `docs/archive/drafts/relatorio_avaliacao_critica_TAP.md` |
| `docs/md/relatorios/Relat_Transicao_TAP_AreasConhecimento.md` | `docs/archive/drafts/Relat_Transicao_TAP_AreasConhecimento.md` |

### 3.7 Seções Fragmentadas do TAP (docs/md/TAP/ → docs/archive/tap-sections/)

| Arquivo Atual | Novo Local |
|---------------|------------|
| `docs/md/TAP/sec_1_objetivos.md` | `docs/archive/tap-sections/sec_1_objetivos.md` |
| `docs/md/TAP/sec_1_objetivos.docx` | `docs/archive/tap-sections/sec_1_objetivos.docx` |
| `docs/md/TAP/sec_4_EAP.md` | `docs/archive/tap-sections/sec_4_EAP.md` |
| `docs/md/TAP/sec_6.md` | `docs/archive/tap-sections/sec_6.md` |
| `docs/md/TAP/sec_6.docx` | `docs/archive/tap-sections/sec_6.docx` |
| `docs/md/TAP/sec_9_premissas.md` | `docs/archive/tap-sections/sec_9_premissas.md` |
| `docs/md/TAP/sec_9_premissas.docx` | `docs/archive/tap-sections/sec_9_premissas.docx` |
| `docs/md/TAP/sec_10_riscos.md` | `docs/archive/tap-sections/sec_10_riscos.md` |
| `docs/md/TAP/sec_10_riscos.docx` | `docs/archive/tap-sections/sec_10_riscos.docx` |
| `docs/md/TAP/sec_11_orcamento.md` | `docs/archive/tap-sections/sec_11_orcamento.md` |
| `docs/md/TAP/sec_11_orcamento.docx` | `docs/archive/tap-sections/sec_11_orcamento.docx` |
| `docs/md/TAP/smart.md` | `docs/archive/tap-sections/smart.md` |
| `docs/md/TAP/smart.docx` | `docs/archive/tap-sections/smart.docx` |
| `docs/md/TAP/req_1.0.md` | `docs/archive/tap-sections/req_1.0.md` |
| `docs/md/TAP/review_TAP.md` | `docs/archive/tap-sections/review_TAP.md` |

### 3.8 Documentos Word Antigos (docs/docx/ → docs/archive/docx/)

| Arquivo Atual | Novo Local |
|---------------|------------|
| `docs/docx/AC1_Integracao.docx` | `docs/archive/docx/AC1_Integracao.docx` |
| `docs/docx/AC2_Escopo.docx` | `docs/archive/docx/AC2_Escopo.docx` |
| `docs/docx/AC3_cronograma.docx` | `docs/archive/docx/AC3_cronograma.docx` |
| `docs/docx/AC4_Custos.docx` | `docs/archive/docx/AC4_Custos.docx` |
| `docs/docx/AC_qualidade.docx` | `docs/archive/docx/AC_qualidade.docx` |
| `docs/docx/_archive/*` | `docs/archive/docx/_archive/*` (mant

estrutura atual real:

.
├── docs
│   ├── archive
│   │   ├── diagramas-deprecated
│   │   │   ├── [legacy]-fig-01-governanca-hibrida.png
│   │   │   ├── [legacy]-fig-02-fluxo-kanban_alt.png
│   │   │   ├── [legacy]-fig-02-fluxo-kanban_alt.svg
│   │   │   ├── [legacy]-fig-02-fluxo-kanban.png
│   │   │   ├── [legacy]-fig-02-fluxo-kanban.svg
│   │   │   ├── [legacy]-fig-03-cfd-comparativo.png
│   │   │   ├── [legacy]-fig-03-cfd-comparativo.svg
│   │   │   ├── [legacy]-fig-04-fluxo-mudancas.png
│   │   │   ├── [legacy]-fig-04-fluxo-mudancas.svg
│   │   │   └── [legacy]-fig-1-fluxo-qualidade.png
│   │   ├── docx
│   │   │   ├── AC1_Integracao.docx
│   │   │   ├── AC2_Escopo.docx
│   │   │   ├── AC3_cronograma.docx
│   │   │   ├── AC4_Custos.docx
│   │   │   ├── AC_qualidade.docx
│   │   │   └── _archive
│   │   │       ├── Modelo-para-elaboracao-de-Monografia.docx
│   │   │       ├── Modelo-Projeto-COGME.docx
│   │   │       ├── TAP_EAP.docx
│   │   │       ├── Termo de Abertura do Projeto v1.doc
│   │   │       ├── Termo de Abertura do Projeto v1.docx
│   │   │       └── Termo de Abertura do Projeto v1_opngoing.docx
│   │   ├── eap-legacy
│   │   │   ├── correcao
│   │   │   │   ├── EAP_COGME_MF1_Fundacao.drawio
│   │   │   │   ├── EAP_COGME_MF1_Fundacao.drawio.png
│   │   │   │   ├── EAP_COGME_MF2_Construcao.drawio
│   │   │   │   ├── EAP_COGME_MF2_Construcao.drawio.png
│   │   │   │   ├── EAP_COGME_MF3_Consolidacao.drawio
│   │   │   │   ├── EAP_COGME_MF3_Consolidacao.drawio.png
│   │   │   │   ├── EAP_COGME_Principal.drawio
│   │   │   │   ├── EAP_COGME_Principal.drawio.png
│   │   │   │   ├── EAP_estruturada_correcao.md
│   │   │   │   ├── EAP_v2.0.docx
│   │   │   │   └── EAP_v2.0.md
│   │   │   └── inicial
│   │   │       ├── MF1_fundacao.drawio
│   │   │       ├── MF1_fundacao.drawio.png
│   │   │       ├── MF2_construcao.drawio
│   │   │       ├── MF2_construcao.drawio.png
│   │   │       ├── MF3_consolidacao.drawio
│   │   │       ├── MF3_consolidacao.drawio.png
│   │   │       ├── principal.drawio
│   │   │       └── principal.drawio.png
│   │   ├── images-legacy
│   │   │   └── diagramas
│   │   │       ├── custos
│   │   │       └── escopo
│   │   └── tap-sections
│   │       ├── req_1.0.md
│   │       ├── review_TAP.md
│   │       ├── sec_10_riscos.docx
│   │       ├── sec_10_riscos.md
│   │       ├── sec_11_orcamento.docx
│   │       ├── sec_11_orcamento.md
│   │       ├── sec_1_objetivos.docx
│   │       ├── sec_1_objetivos.md
│   │       ├── sec_4_EAP.md
│   │       ├── sec_6_marcos.docx
│   │       ├── sec_6_marcos.md
│   │       ├── sec_9_premissas.docx
│   │       ├── sec_9_premissas.md
│   │       ├── smart.docx
│   │       └── smart.md
│   ├── conhecimento
│   │   ├── drafts
│   │   │   ├── analise_arquitetural.md
│   │   │   ├── Canon_Stack_SDD.md
│   │   │   ├── estrutura-de-diretorios.md
│   │   │   ├── glossario.md
│   │   │   ├── hardware.md
│   │   │   ├── [legacy]-redacao_progressiva.md
│   │   │   ├── llm_base_persona.md
│   │   │   ├── monitoramenteo_inconsistencias.md
│   │   │   ├── notas_adjacentes.md
│   │   │   ├── OKB_COGME_v3.0.md
│   │   │   ├── premissas.md
│   │   │   ├── principais_requisitos_entregas.md
│   │   │   ├── proposta_estrutural.md
│   │   │   ├── reestrutura_EAP.md
│   │   │   ├── refac_prompt.md
│   │   │   ├── relatorio_avaliacao_critica_TAP.md
│   │   │   ├── Relat_Transicao_TAP_AreasConhecimento.md
│   │   │   ├── req_1.0.docx
│   │   │   ├── sec_4_EAP.docx
│   │   │   └── support_research.md
│   │   ├── glossario.md
│   │   ├── licoes-aprendidas
│   │   │   ├── MF1-licoes.md
│   │   │   ├── MF2-licoes.md
│   │   │   └── MF3-licoes.md
│   │   └── OKB.md
│   ├── decisoes
│   │   ├── ADR-001-stack.md
│   │   ├── ADR-002-kanban.md
│   │   ├── ADR-003-metricas.md
│   │   ├── ADR-004-tasklists.md
│   │   └── ADR-005-freeze.md
│   ├── dependencias
│   │   └── registro.md
│   ├── diagramas
│   │   ├── cronograma
│   │   │   └── fig-01-sequenciamento-macro-caminho-critico.svg
│   │   ├── custos
│   │   │   ├── fig-01-fluxo-prevencao-custos.png
│   │   │   └── fig-01-fluxo-prevencao-custos.svg
│   │   ├── eap
│   │   │   ├── fig-01-eap-executiva.svg
│   │   │   ├── fig-eap-mf1-fundacao.svg
│   │   │   ├── fig-eap-mf2-construcao.svg
│   │   │   ├── fig-eap-mf3-consolidacao.svg
│   │   │   ├── fig-eap-nivel-0-macro.png
│   │   │   ├── fig-eap-nivel-0-macro.svg
│   │   │   ├── [legacy]-EAP_COGME_v3.0_MF1_Fundacao.drawio
│   │   │   ├── [legacy]-EAP_COGME_v3.0_MF1_Fundacao.drawio.png
│   │   │   ├── [legacy]-EAP_COGME_v3.0_MF2_Construcao.drawio
│   │   │   ├── [legacy]-EAP_COGME_v3.0_MF2_Construcao.drawio.png
│   │   │   ├── [legacy]-EAP_COGME_v3.0_MF3_Consolidacao.drawio
│   │   │   ├── [legacy]-EAP_COGME_v3.0_MF3_Consolidacao.drawio.png
│   │   │   ├── [legacy]-EAP_COGME_v3.0_Principal.drawio
│   │   │   └── [legacy]-EAP_COGME_v3.0_Principal.drawio.png
│   │   ├── fig-4-controle-mudancas.svg
│   │   ├── integracao
│   │   │   ├── fig-02-matriz-rastreabilidade-dependencias.png
│   │   │   ├── fig-02-matriz-rastreabilidade-dependencias.svg
│   │   │   ├── fig-1-governanca-hibrida.svg
│   │   │   └── fig-3-cfd-saudavel-vs-gargalo.svg
│   │   ├── mermaid-config.json
│   │   └── qualidade
│   │       ├── [legacy]-fig-01-fluxo-qualidade.png
│   │       ├── [legacy]-fig-01-fluxo-qualidade.svg
│   │       ├── [legacy]-fig-05-ishikawa-coverage.png
│   │       ├── [legacy]-fig-05-ishikawa-coverage.svg
│   │       ├── [legacy]-fig-06-ishikawa-uat.png
│   │       ├── [legacy]-fig-06-ishikawa-uat.svg
│   │       ├── [legacy]-fig-07-ishikawa-cycletime.png
│   │       └── [legacy]-fig-07-ishikawa-cycletime.svg
│   ├── docx
│   ├── md
│   │   └── TAP
│   │       └── EAP
│   ├── metricas
│   │   └── baseline.md
│   ├── planos
│   │   ├── plano-comunicacoes.md
│   │   ├── plano-cronograma.md
│   │   ├── plano-custos.md
│   │   ├── plano-escopo.md
│   │   ├── plano-integracao.md
│   │   ├── plano-qualidade.md
│   │   ├── plano-recursos.md
│   │   └── plano-riscos.md
│   ├── requisitos
│   │   └── requisitos.md
│   ├── tap
│   │   ├── TAP.docx
│   │   └── TAP.md
│   └── xml
│       └── EAP_TAP
│           └── correcao
├── estrutura-de-diretorios.md
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── src
│   ├── backend
│   │   ├── main.py
│   │   ├── models
│   │   │   └── __init__.py
│   │   ├── routers
│   │   │   └── __init__.py
│   │   └── services
│   │       └── __init__.py
│   ├── frontend
│   │   ├── static
│   │   └── templates
│   │       └── index.html
│   └── shared
│       └── schemas.py
└── tests
    ├── integration
    │   └── __init__.py
    └── unit
        └── __init__.py

48 directories, 142 files

# NOTAS ADJACENTES — Projeto COGME
## Documento de Registro Operacional, Governança Visual, Configuração SSOT e Ações Ad-Hoc
### Versão 2.0 — Revisão Completa com Conteúdo Integral

> **Natureza:** Anotações adjacentes ao projeto, de uso diário e ações ad-hoc. Conteúdo preservado integralmente; duplicidades removidas; inconsistências ontológicas sanadas; estruturação temporal/histórica para rastreabilidade de raciocínio.
>
> **Hierarquia de autoridade:** TAP v3 > OKB v3.0+Aditivo > Glossário v3.1 > ADRs 001–005 > **Notas Adjacentes (este documento)** > Drafts
>
> **Data de referência:** 19–22/09/2026 (MF1 — Fundação, pré-M1)

---

## SEÇÃO 0 — METADADOS E CONTEXTO

| Campo | Valor |
| --- | --- |
| Projeto | COGME — Conversor de Ganhos em Moeda Estrangeira |
| Instituição | Fatec Taquaritinga — ADS |
| GP | Leonardo David Silva Setti |
| Equipe | Leonardo David Silva Setti, Fabricio de Lima Cabral, Edson Luis Silva |
| Stakeholder-Avaliador | Prof. Dr. Nivaldo Carleto |
| Período coberto | 19/09/2026 (Backlog M1) → 22/09/2026 (LA-001) |
| Marco ativo | M1 — Entrega Parcial Documental (22/09/2026) |
| Artefatos gráficos | 14 SVGs (13 únicos + 1 refação por overlap) |
| Configuração SSOT | 27 labels, 5 milestones, 21 cards M1, Padrões A/B |
| Estrutura de repositório | Proposta formal + estrutura atual real mapeada |

**Linha do tempo sintética:**

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

## SEÇÃO 1 — FLAG DE ESTADO: REVISÃO DIFERIDA (PDCA FUTURO)

> **Natureza:** Metadado de sessão não canônico. Não integra a documentação formal do projeto. Registra decisão de postergar revisão integral para ciclo PDCA futuro.

### 1.1 Veredito Sumário

Nota registrada como metadado de sessão não canônico. A produção das seções do Plano de Gerenciamento prossegue sem interrupção; a revisão integral será alocada como item de entrada para um ciclo PDCA futuro, sem contaminar a saída formal atual.

### 1.2 Reformulação Crítica

A instrução não é uma solicitação de análise, mas um flag de estado. A questão operacional subjacente é: como processar essa diretiva de revisão diferida sem gerar ruído ou inconsistência na documentação canônica que está sendo produzida agora.

### 1.3 Análise de Risco (Técnico + Humano)

- **Técnico:** Risco de deriva de escopo (scope creep) se a "revisão integral" futura não possuir critérios de aceitação e limites de tempo definidos no momento do PDCA.
- **Humano/Organizacional:** Risco de stakeholders consumirem a versão atual como definitiva, gerando atrito político quando a revisão ocorrer. A mitigação exige versionamento explícito (ex: `v0.x-draft-revisão-pendente`).

### 1.4 Recomendação Justificada

Isolar esta diretiva no contexto da conversa atual. Prosseguir com a geração diligente das seções do plano solicitadas, mantendo a rastreabilidade lógica das decisões tomadas. Isso garante que, quando o gatilho do PDCA for ativado, a "análise abrangente" tenha um baseline claro para comparar as incongruências, alinhando-se à experiência em governança de testes e transição para SDET/Lead.

### 1.5 Condições de Validade e Gatilhos

- **Validade:** Indefinida, até a ativação do ciclo PDCA.
- **Gatilho de Reavaliação:** Comando explícito do usuário: "Iniciar revisão integral do Plano de Gerenciamento (PDCA)".

### 1.6 Premissas Assumidas

- Esta nota é um estado transitório de projeto, não um traço persistente de persona.
- O usuário iniciará o ciclo PDCA com critérios objetivos, evitando a armadilha de "revisão por revisão" sem ganho de valor de negócio.
- A produção atual das seções deve manter o padrão de concisão e foco em portabilidade (FOSS/CLI vs. MS) já estabelecido.

---

## SEÇÃO 2 — LITERATURA DE APOIO: QUESTÕES ADJACENTES

> **Contexto:** Decisões técnicas fundamentadas em literatura PMBOK® e boas práticas, utilizadas como apoio às decisões de configuração do GitHub e governança do COGME.

### 2.1 Área de Conhecimento para Rede de Projeto e Caminho Crítico

**Questão:** Segundo PMI PMBOK ed 7 e 6, qual área de conhecimento deve conter a rede de projeto contendo a sequência de tarefas do projeto conforme progressão e tempo para cálculo das tabelas de precedência e caminhos críticos?

**Resposta técnica:**

| Edição | Resposta |
| --- | --- |
| PMBOK® 6ª (Dicionário) | Gerenciamento do Cronograma do Projeto — Processos 6.4 (Sequenciar as Atividades) e 6.6 (Desenvolver o Cronograma) |
| PMBOK® 7ª (Governança Primária) | Domínio de Desempenho de Planejamento (evolução progressiva do cronograma) + Domínio de Desempenho de Medição (monitoramento do progresso temporal) |

**Aplicação no COGME:**

Conforme ADR-003 e Plano de Integração §1.6.2, o projeto declara formalmente a obsolescência operacional do uso de redes de projeto detalhadas (CPM/Gantt) para o gerenciamento do fluxo de trabalho diário.

| Nível | Abordagem |
| --- | --- |
| Macro (Marcos M1–M4) | Sequenciamento temporal fixo; lógica de precedência do PMBOK 6ª (Processo 6.5) usada apenas para validar viabilidade acadêmica |
| Operacional (Tarefas da EAP) | Sequenciamento gerenciado pelo Pull System no GitHub Projects (ADR-002); "caminho crítico" identificado empiricamente por gargalos no CFD e Cycle Time (ADR-003) |

**Trade-off declarado:** Abre-se mão da formalidade preditiva (CPM/EVM) em favor de métricas de fluxo ágil nativas, conforme o Domínio de Medição do PMBOK 7ª e o método Kanban.

### 2.2 Estruturação do Cumulative Flow Diagram (CFD) para Demonstração Formal

**Questão:** Como estruturar no documento o Cumulative Flow Diagram (CFD) para demonstração formal ao orientador?

**Localização documental recomendada:**

| Artefato | Seção | Função |
| --- | --- | --- |
| Plano de Integração | §1.6.1 (Métricas de Fluxo) | Definição formal + cadência |
| Plano de Cronograma | §2.3 (Monitoramento Temporal) | Substituto do Gantt/EVM |
| Plano de Comunicações | §3.2 (Relatórios Semanais) | Evidência visual de progresso |

**Regra GMV:** Não criar artefato separado. O CFD é métrica nativa do GitHub Insights — qualquer documentação adicional seria burocracia.

**Definição formal:**

O Cumulative Flow Diagram (CFD) é a visualização gráfica do fluxo de trabalho acumulado ao longo do tempo, onde cada banda horizontal representa uma coluna do quadro Kanban (Backlog, Ready, In Progress, Code Review, Done). A largura de cada banda em um determinado instante indica a quantidade de cards naquela etapa.

- **Eixo X:** Tempo (dias/semanas)
- **Eixo Y:** Quantidade acumulada de cards
- **Bandas** (de baixo para cima): Done (verde), Code Review (azul), In Progress (amarelo), Ready (laranja), Backlog (cinza)
- **Fonte de dados:** GitHub Projects → GitHub Insights → Aba "Charts" → "Cumulative Flow Diagram"
- **Frequência:** Semanal (toda segunda-feira, 09:00)
- **Responsável:** GP Leonardo David Silva Setti

**Meta de desempenho:**
- CFD saudável: Bandas paralelas e de largura constante (fluxo estável)
- CFD com gargalo: Bandas que se alargam progressivamente (acúmulo em uma etapa)
- Ação corretiva: Se uma banda ultrapassar 2× a largura média das demais por 2 semanas consecutivas, acionar Retrospectiva extraordinária (ADR-002)

**Interpretação visual (como explicar ao orientador):**

Cenário ideal (fluxo saudável):
~~~
Cards
  ↑
  │         ╭───────────────────────────── Done (verde)
  │      ╭──┤
  │   ╭──┤  │ Code Review (azul)
  │╭──┤  │  │
  ││  │  │  │ In Progress (amarelo)
  ││  │  │  │
  ││  │  │  │ Ready (laranja)
  ││  │  │  │
  ││  │  │  │ Backlog (cinza)
  └┴──┴──┴──┴──────────────────────────→ Tempo
~~~
Leitura: Bandas paralelas = fluxo equilibrado. Throughput estável.

Cenário com gargalo:
~~~
Cards
  ↑
  │         ╭───────────────────────────── Done (verde)
  │      ╭──┤
  │   ╭──┤  │ Code Review (azul) ← BANDAS SE ALARGAM
  │╭──┤  │  │                        (gargalo em Code Review)
  ││  │  │  │ In Progress (amarelo)
  ││  │  │  │
  ││  │  │  │ Ready (laranja)
  ││  │  │  │
  ││  │  │  │ Backlog (cinza)
  └┴──┴──┴──┴──────────────────────────→ Tempo
~~~
Leitura: Banda de Code Review se alarga = cards acumulando nessa etapa. Ação: Reduzir WIP em Code Review, redistribuir revisores, ou ajustar DoD.

**Blindagem acadêmica (defesa técnica):**

Se o Prof. Dr. Nivaldo Carleto questionar a ausência de Gantt:

"Conforme ADR-003 (Métricas de Fluxo), o projeto COGME declara a obsolescência operacional do Diagrama de Gantt e de métricas EVM (SPI/CPI) para monitoramento de progresso. Esta decisão é fundamentada em três pilares:
1. Domínio de Medição do PMBOK 7ª: Prioriza métricas de fluxo sobre métricas preditivas
2. Restrição de Orçamento Zero (TAP §11): Inviabiliza EVM (AC = 0 → CPI indeterminado)
3. Natureza do Fluxo Contínuo (ADR-002): CFD fornece visibilidade em tempo real sem overhead"

**Evidência de conformidade:**

| Critério TAP §3 | Evidência no CFD |
| --- | --- |
| Cycle Time ≤ 3 dias | Distância horizontal entre "In Progress" e "Done" |
| Throughput ≥ 5 cards/semana | Inclinação da banda "Done" |
| Sem gargalos | Bandas paralelas (sem alargamento progressivo) |

**Recomendação final:** Não criar diagramas manuais do CFD. O GitHub Projects gera o CFD automaticamente na aba "Insights". Para o Marco M1, como o período de calibração ainda não começou (início em 23/09), incluir apenas a definição formal e declarar que o primeiro CFD será publicado no relatório semanal de 06/10/2026.

### 2.3 Resolução da Inconsistência de Fronteira do M1

**Questão:** O TAP §6 M1 declara 5 planos, mas o OKB v2.2 lista 8 planos. Esta informação sana a inconsistência TAP?

**Resposta técnica:** Sim, esta informação sana totalmente a inconsistência e valida a governança híbrida sob a ótica do PMBOK®.

| Artefato | Leitura Anterior (Incorreta) | Leitura Corrigida (Governança Híbrida) |
| --- | --- | --- |
| TAP §6 | "Incompleto" por citar apenas 5 áreas | Correto: Define a linha de base faseada do Marco M1 (Fundação) |
| OKB v2.2 §3.1 | "Contraditório" por listar 8 planos | Correto: Define o inventário total de artefatos do projeto ao longo de todo o ciclo de vida |
| Plano de Integração | Ambiguidade sobre "7 planos subsequentes" | Atualizado para explicitar a estratégia de entrega faseada |

**Princípio PMBOK 7ª Aplicado:** Personalização (Tailoring) da Abordagem de Desenvolvimento. Entregar todos os 8 planos no M1 geraria overhead burocrático inicial desnecessário (anti-ágil). Deferir Recursos, Comunicações e Riscos para quando o fluxo de trabalho estiver mais maduro é uma decisão de tailoring legítima e defensável academicamente.

**Impacto imediato nos Cards do M1:** Os cards de Recursos, Comunicações e Riscos são removidos do escopo obrigatório do M1 e realocados para o Backlog do M2.

**Ação corretiva no Plano de Integração (§1.4):** Incluir parágrafo sobre Elaboração Progressiva e Personalização.

---

## SEÇÃO 3 — CONFIGURAÇÃO OPERACIONAL DO GITHUB (SSOT)

> **Contexto:** Formalização das decisões de configuração do GitHub como SSOT do COGME, conforme ADR-002. Esta seção é orientante para toda a documentação e operação do projeto.

### 3.1 Sistema de Tags (Labels) — 27 Labels em 5 Categorias

**Fundamentação:** As tags abaixo foram desenhadas para operar no GitHub Issues + GitHub Projects (SSOT, ADR-002), com três objetivos:
1. Rastreabilidade TAP → EAP → Card (cada card vincula-se a fase, área e requisito)
2. Métricas de fluxo (Throughput e Cycle Time por tipo/área, ADR-003)
3. Controle de mudanças e riscos (labels operacionais do Plano de Integração §1.7 e §1.9)

**Princípio aplicado:** GMV — cada tag existe apenas se for útil para filtragem, métrica ou governança.

**Categoria 1 — Tipo de Trabalho (6 tags)**

| Tag | Descrição | Cor sugerida |
| --- | --- | --- |
| feat | Nova funcionalidade do MVP | #0E8A16 (verde) |
| bug | Defeito em funcionalidade existente | #D73A4A (vermelho) |
| docs | Artefatos textuais: planos, TAP, OKB, Glossário, lições aprendidas | #0075CA (azul) |
| test | Testes unitários, de integração e UAT | #BFD4F2 (azul claro) |
| ci | Configuração e manutenção do pipeline GitHub Actions | #FBCA04 (amarelo) |
| chore | Tarefas operacionais que não alteram código nem docs | #E4E669 (cinza-esverdeado) |

**Categoria 2 — Macro-Fase EAP (3 tags)**

| Tag | Descrição | Cor sugerida |
| --- | --- | --- |
| MF1-fundacao | Fases N1 a N4, N8, N9, N10 (parcial) | #D4C5F9 (roxo claro) |
| MF2-construcao | Fases N5 a N7, N10 | #C5DEF5 (azul claro) |
| MF3-consolidacao | Fases N11 e N12 | #BFDADC (rosa claro) |

**Categoria 3 — Área de Conhecimento (8 tags)**

| Tag | Descrição | Cor sugerida |
| --- | --- | --- |
| area:integracao | Coordenação entre planos, controle de mudanças, SSOT | #1D76DB (azul) |
| area:escopo | Requisitos, EAP, DoR/DoD, fronteira IN/OUT, YAGNI | #006B75 (teal) |
| area:cronograma | Marcos M1–M4, fluxo contínuo, baseline de métricas | #5319E7 (roxo) |
| area:custos | Orçamento zero, conformidade FOSS | #B60205 (vermelho escuro) |
| area:qualidade | Coverage ≥ 80%, UAT, 12 PDCAs, Ishikawa 6M | #008672 (verde-azulado) |
| area:recursos | Equipe de 3, hardware, prevenção de burnout | #D93F0B (laranja) |
| area:comunicacoes | Daily assíncrona, Refinement, Retrospectiva | #F9D0C4 (salmão) |
| area:riscos | R1–R5, risk backlog, gatilhos de escalation | #B60205 (vermelho escuro) |

**Categoria 4 — Status Operacional (4 tags)**

| Tag | Descrição | Cor sugerida |
| --- | --- | --- |
| change-request | Solicitação formal de mudança. Aciona fluxo CCB em ≤ 48h | #FF0000 (vermelho) |
| risk | Risco identificado ou materializado (R1–R5) | #FFFF00 (amarelo) |
| blocked | Card bloqueado por dependência externa ou interna | #B60205 (vermelho escuro) |
| sdd-ia | Artefato ou código gerado com apoio de IA generativa (SDD) | #A2EEEF (ciano) |

**Categoria 5 — Prioridade (6 tags: MoSCoW + P0–P3)**

| Tag | Descrição | Cor sugerida |
| --- | --- | --- |
| must | Requisito indispensável ao MVP | #B60205 (vermelho escuro) |
| should | Requisito importante mas não bloqueante | #FBCA04 (amarelo) |
| P0 | Crítico / Caminho crítico | #B60205 (vermelho escuro) |
| P1 | Alto | #D93F0B (laranja) |
| P2 | Médio | #FBCA04 (amarelo) |
| P3 | Baixo | #0E8A16 (verde) |

**Regras de Aplicação:**
1. Todo card deve ter no mínimo 3 tags: 1 tipo + 1 macro-fase + 1 área.
2. Cards de código devem ter obrigatoriamente `feat` ou `bug` + tag de macro-fase.
3. Cards de documentação devem ter `docs` + `area:X` correspondente.
4. Cards com `sdd-ia` exigem que o commit vinculado declare co-autoria (DoD, Plano de Escopo §2.6).
5. Cards com `change-request` não migram para `In Progress` até aprovação do GP.
6. Cards com `blocked` devem registrar a dependência no corpo da Issue.

**Tags Explicitamente Excluídas (decisão GMV):**

| Tag rejeitada | Motivo da exclusão |
| --- | --- |
| N1 … N12 (fases individuais) | 12 tags redundantes; fase já consta no título padronizado |
| REQ-01 … REQ-15 | Rastreabilidade via corpo do card, não via tag |
| could, wont | Classes vazias no escopo atual |
| epic | MVP é único; não há múltiplos épicos |
| spike | Não há pesquisa exploratória formal no escopo |
| good first issue | Equipe de 3 pessoas; onboarding não se aplica |
| help wanted | Mesmo motivo |

### 3.2 Milestones do Projeto — 5 Milestones

**Decisão GMV:** 5 milestones no total. O GitHub não suporta hierarquia nativa de milestones, portanto as subfases da EAP são rastreadas via labels de macro-fase dentro de cada milestone.

| # | Milestone | Due Date | Abertura | Macro-Fase | Tipo | Cards Associados |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | M1 — Entrega Parcial Documental | 22/09/2026 | 01/09/2026 | MF1 | Marco oficial | M1-01 a M1-21 |
| 2 | M2 — Ambiente e Modelagem Concluídos | 30/09/2026 | 23/09/2026 | MF1 (encerramento) | Marco oficial | N3.x, N4.x, N2.3 |
| 3 | Calibração — Baseline de Métricas | 03/10/2026 | 23/09/2026 | MF1 → MF2 (transição) | Auxiliar | Baseline + ADR de metas |
| 4 | M3 — MVP Funcional (Beta) | 15/11/2026 | 04/10/2026 | MF2 | Marco oficial | N5.x, N6.x, N7.1, N10.x |
| 5 | M4 — Encerramento e Validação Acadêmica | 15/12/2026 | 16/11/2026 | MF3 | Marco oficial | N11.x, N12.x |

**Regras de Aplicação no GitHub:**
1. Cada Issue deve estar associada a exatamente uma milestone. Cards sem milestone são tratados como `Backlog` não planejado.
2. A milestone não pode ser fechada enquanto houver Issues abertas com label `blocked` ou `change-request`.
3. O fechamento da milestone exige: (i) todos os critérios de fechamento atendidos, (ii) registro de lições aprendidas da fase, (iii) comunicação ao Prof. Dr. Nivaldo Carleto quando aplicável (M1, M3, M4).
4. Alteração de data de milestone exige `change-request` + aprovação do CCB (GP Leonardo) + ADR se alterar marco oficial.
5. A milestone auxiliar (Calibração) não substitui M2 — são complementares. M2 encerra MF1; Calibração estabelece baseline para MF2.

### 3.3 Padrão de Redação de Cards Ubíquos

**Princípio do Card Ubíquo:** Um card ubíquo é autossuficiente: qualquer membro da equipe (ou o Prof. Dr. Nivaldo Carleto, em avaliação) deve conseguir compreender o quê, por quê, como será aceito e a quem pertence sem abrir nenhum outro artefato.

**Três propriedades obrigatórias:**
1. Autocontextualização — o card declara sua finalidade em linguagem própria
2. Critério de aceite mensurável — checklist binário (atingido/não atingido)
3. Rastreabilidade dupla — vínculo vertical (TAP → EAP → REQ) e horizontal (área + macro-fase + milestone)

**Padrão A — Card Documental / Governança / Infraestrutura**

Aplica-se a: `docs`, `ci`, `chore`.

| Campo | Função | Regra de preenchimento |
| --- | --- | --- |
| 1. Título | Identificação padronizada | Formato N{X}.{Y} — Descrição curta |
| 2. Contexto Ubíquo | Por que este card existe | 2 a 3 frases autocontidas |
| 3. Descrição da Entrega | O que será produzido | Verbo no infinitivo + artefato + localização |
| 4. Critérios de Aceite | Checklist binário | Mínimo 3 itens mensuráveis |
| 5. Rastreabilidade | Elo de auditoria | TAP §X + EAP NX.Y + REQ-XX + Domínio PMBOK 7ª |
| 6. Dependências | Pré-requisitos explícitos | Listar cards ou artefatos bloqueantes |
| 7. Atribuição | Responsável + esforço | Nome completo + estimativa ≤ 8h |
| 8. Estado | Tags + milestone + status | Mínimo 3 tags + milestone + status operacional |

**Padrão B — Card User Story (GWT) — padrão projetivo para M2**

Aplica-se a: `feat`, `bug`, `test`.
Status normativo: Padrão definido nesta data, com aplicação efetiva a partir do marco M2 (30/09/2026).

| Campo | Função | Regra de preenchimento |
| --- | --- | --- |
| 1. Título | Identificação padronizada | Formato N{X}.{Y} — US-{NN}: Descrição |
| 2. User Story | Narrativa de valor | Como [papel], quero [ação], para [benefício mensurável] |
| 3. Contexto Ubíquo | Dor de negócio endereçada | 1 a 2 frases ligando a história ao público-alvo |
| 4. Critérios de Aceite (GWT) | Comportamento verificável | Blocos Dado / Quando / Então; mínimo 2 cenários |
| 5. Regras de Negócio | Restrições de domínio | Spread, IOF, precisão decimal, regimes |
| 6. Rastreabilidade | Elo de auditoria | REQ-XX + EAP NX.Y + Domínio PMBOK 7ª |
| 7. Dependências | Pré-requisitos técnicos | Cards de arquitetura, DER ou API bloqueantes |
| 8. Atribuição | Responsável + esforço | Nome completo + estimativa ≤ 8h |
| 9. Estado | Tags + milestone + status | Mínimo 3 tags + milestone + status operacional |

### 3.4 Sistema de Prioridade P0–P3

**Definição:** Escala complementar ao MoSCoW (que classifica valor de escopo) e foca em urgência temporal e criticidade de bloqueio.

| Peso | Definição | Critério objetivo | Ação no Kanban |
| --- | --- | --- | --- |
| P0 | Crítico / Caminho crítico | Sem este card, o marco não é atingido ou ele bloqueia ≥ 2 outros cards | Execução imediata; WIP reservado; Daily obrigatória |
| P1 | Alto | Essencial para o marco, mas não bloqueia outros cards diretamente | Execução na janela do marco |
| P2 | Médio | Importante, mas pode deslizar para o marco seguinte | Execução pós-marco atual |
| P3 | Baixo | Desejável; postergável sem impacto formal | Backlog priorizado; puxar apenas se capacidade sobrar |

**Regra de desempate:** Se dois cards têm o mesmo peso, prioriza-se aquele que desbloqueia mais cards subsequentes.

**Trade-off declarado:** Um card `must` (MoSCoW) pode ser P2 se sua entrega puder deslizar para M2 sem violar o critério de aceite do M1.

---

## SEÇÃO 4 — BACKLOG DO MARCO M1 — CONSOLIDADO (21 CARDS)

### 4.1 Resumo dos 21 Cards

| # | Card | Tipo | Macro-Fase | Área | MoSCoW | Temporal | Milestone | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M1-01 | Plano de Integração | docs | MF1 | area:integracao | must | P0 | M1 | 🔄 pair-review |
| M1-02 | Plano de Escopo | docs | MF1 | area:escopo | must | P0 | M1 | 🔄 pair-review |
| M1-03 | Plano de Cronograma | docs | MF1 | area:cronograma | must | P0 | M1 | ⏳ 21/09 |
| M1-04 | Plano de Custos | docs | MF1 | area:custos | must | P0 | M1 | ⏳ 21/09 |
| M1-05 | Plano Qualidade + PDCAs + Ishikawa | docs | MF1 | area:qualidade | must | P0 | M1 | ⏳ 21/09 |
| M1-06 | Requisitos Funcionais | docs | MF1 | area:escopo | must | P1 | M1 | 🔄 pair-review |
| M1-07 | Requisitos Não Funcionais | docs | MF1 | area:qualidade | must | P1 | M1 | 🔄 pair-review |
| M1-08 | Arquitetura da Solução | docs | MF1 | area:escopo | must | P2 | M2 | ⏳ 30/09 |
| M1-09 | Protótipo UX/UI | docs | MF1 | area:escopo | should | P3 | M2 | ⏳ 30/09 |
| M1-10 | Modelagem de Dados (DER) | docs | MF1 | area:escopo | must | P2 | M2 | ⏳ 30/09 |
| M1-11 | Seleção Stack FOSS (ADR-001) | docs | MF1 | area:recursos | must | P1 | M1 | 🔄 in-review |
| M1-12 | Repositório Git + CI/CD | ci | MF1 | area:integracao | must | P0 | M1 | ⏳ 22/09 |
| M1-13 | Setup Local e Homologação | chore | MF1 | area:recursos | must | P1 | M1 | ⏳ 22/09 |
| M1-14 | Auditoria de Licenças FOSS | docs | MF1 | area:qualidade | must | P2 | M2 | ⏳ 30/09 |
| M1-15 | ADR-001 Stack | docs | MF1 | area:integracao | must | P1 | M1 | 🔄 in-review |
| M1-16 | ADR-002 Kanban | docs | MF1 | area:integracao | must | P1 | M1 | 🔄 in-review |
| M1-17 | ADR-003 Métricas | docs | MF1 | area:cronograma | must | P1 | M1 | 🔄 in-review |
| M1-18 | Lições Aprendidas MF1 | docs | MF1 | area:integracao | should | P3 | M2 | ⏳ 30/09 |
| M1-19 | Matriz RACI | docs | MF1 | area:comunicacoes | should | P2 | M1 | ⏳ 22/09 |
| M1-20 | Canais Oficiais | docs | MF1 | area:comunicacoes | should | P2 | M1 | ⏳ 22/09 |
| M1-21 | Labels + change-request | chore | MF1 | area:integracao | must | P1 | M1 | ⏳ 22/09 |

**Total:** 21 cards · 15 `must` · 6 `should` · 6 P0 · 8 P1 · 5 P2 · 2 P3

### 4.2 Cards que Receberão Tasklist (ADR-004)

**Regra de aplicação (ADR-004):**
- Obrigatória para cards com estimativa ≥ 6h ou múltiplos entregáveis.
- Proibida para cards atômicos (≤ 4h) ou em status `Code Review`/`Done`.
- Formato canônico: Mínimo 3 itens, máximo 7 itens; último item obrigatoriamente "Validação final".
- Natureza binária: Itens são "feito/não feito" (`- [ ]` / `- [x]`), sem status intermediário.

| Card | Estimativa | Justificativa | Nº de Itens |
| --- | --- | --- | --- |
| M1-01 (Plano de Integração) | 6h | Múltiplas seções; requer validação cruzada | 5 |
| M1-02 (Plano de Escopo) | 6h | Múltiplas seções; requer validação cruzada | 5 |
| M1-05 (Plano Qualidade + PDCAs + Ishikawa) | 8h | Múltiplos entregáveis (plano + 12 PDCAs + diagrama) | 6 |
| M1-08 (Arquitetura da Solução) | 6h | Diagrama + validação de componentes | 4 |
| M1-09 (Protótipo UX/UI) | 8h | Wireframes + validação de usabilidade | 5 |
| M1-10 (Modelagem de Dados DER) | 6h | Entidades + cardinalidades + validação SQLite | 4 |
| M1-12 (Repositório Git + CI/CD) | 6h | Repositório + pipeline + Projects + labels | 6 |

**Total:** 7 cards com tasklist · 35 itens de checklist · 0 subissues criadas.

### 4.3 Mecanismo de Contorno: Tasklist como Substituto de Subissue

**Problema:** Cards complexos (≥ 6h) exigem visibilidade de progresso interno. A solução tradicional seria criar subissues (Issues filhas), mas isso foi formalmente rejeitado pela ADR-004 porque:
- Fragmenta o backlog no GitHub Projects (cada subissue vira um card independente)
- Distorce métricas de fluxo (Throughput e Cycle Time contariam sub-tarefas, não o entregável real)
- Viola o princípio GMV (overhead de gestão de múltiplas Issues para um único entregável)

**Contorno adotado:** Tasklist Markdown nativa do GitHub (`- [ ]` / `- [x]`) dentro do corpo da Issue.

| Propriedade | Subissue (VETADA) | Tasklist Markdown (ADOTADA) |
| --- | --- | --- |
| Cria nova Issue no repositório? | ✅ Sim | ❌ Não |
| Aparece como card no GitHub Projects? | ✅ Sim (fragmenta) | ❌ Não (permanece no card pai) |
| Afeta métricas de fluxo (ADR-003)? | ✅ Sim (distorce) | ❌ Não (card pai é a unidade) |
| Fornece visibilidade de progresso? | ✅ Sim | ✅ Sim (barra de progresso nativa) |
| Exige gestão de dependências entre Issues? | ✅ Sim (overhead) | ❌ Não |
| Overhead de gestão | Alto | Zero |

**Exemplo prático (Card M1-05 — Plano de Qualidade):**

~~~markdown
## Tasklist (ADR-004)
- [ ] Estrutura do Plano de Qualidade redigida (seções 1-8)
- [ ] 12 ciclos PDCA consolidados (um por fase da EAP)
- [ ] Diagrama de Ishikawa 6M desenhado e versionado
- [ ] Critérios de aceite vinculados a REQ-08, REQ-09, REQ-10
- [ ] Revisão em pares solicitada (Fabricio ou Leonardo)
- [ ] Validação final
~~~

**Regras operacionais:**
1. A tasklist é criada no momento da abertura do card (antes de migrar para `In Progress`).
2. Cada item é marcado como concluído (`- [x]`) somente quando o critério daquele passo for objetivamente atendido.
3. O card só migra para `Code Review` quando 100% dos itens estiverem marcados (DoD, Plano de Escopo §2.6 item 8).
4. O GitHub exibe automaticamente uma barra de progresso no card (ex: "4 of 6 tasks complete"), fornecendo visibilidade sem fragmentação.

**Fundamentação PMBOK 7ª:** Domínio de Trabalho do Projeto — "O trabalho do projeto é executado por meio de atividades que produzem entregas. A decomposição do trabalho deve ser suficiente para permitir o controle, sem gerar overhead desnecessário."

**Trade-off aceito (ADR-004):** Simplicidade (GMV) > Granularidade de status de sub-tarefas. A unidade atômica de métrica permanece sendo o card pai, não os itens da tasklist.

### 4.4 Distribuição de Trabalho por Membro

| Membro | Cards P0 | Cards P1 | Cards P2/P3 | Carga Total Estimada |
| --- | --- | --- | --- | --- |
| Leonardo | M1-01, M1-12 | M1-15, M1-16, M1-17, M1-21 | M1-20 | ~14h |
| Fabricio | M1-02, M1-03, M1-04 | M1-06, M1-13 | M1-10 | ~13h |
| Edson | M1-05 | M1-07 | M1-19 | ~11h |

**Verificação:** Todos os membros estão dentro do limite de 20h/semana (Premissa P5) e do WIP limit de 3 cards/pessoa em `In Progress` (ADR-002).

---

## SEÇÃO 5 — POLÍTICA DE ADRs E INTEGRAÇÃO DOCUMENTAL (ADITIVO OKB)

> **Domínio PMBOK 7ª:** Trabalho do Projeto + Incerteza + Abordagem de Desenvolvimento
> **Processo PMBOK 6ª (dicionário):** 4.4 — Gerenciar o Conhecimento do Projeto
> **Rastreabilidade:** TAP §3 (Inovação) + REQ-12 + Plano de Integração §1.5.2 + ADR-002
> **Princípio norteador:** GMV (Governança Mínima Viável)

### 5.1 Gatilhos para Criação de Novas ADRs

**Matriz de Gatilhos (Teste de 4 Perguntas):**

Uma decisão exige ADR se atender a pelo menos 2 dos 4 critérios abaixo. Se atender a apenas 1, registra-se em commit message. Se não atender a nenhum, não se registra formalmente.

| # | Critério | Exemplo no COGME | Domínio PMBOK 7ª |
| --- | --- | --- | --- |
| G1 | **Impacto transversal:** Afeta ≥ 2 fases da EAP ou ≥ 2 planos de área | ADR-003 (métricas) impacta Cronograma + Integração + Qualidade | Planejamento + Medição |
| G2 | **Irreversibilidade prática:** Reverter a decisão custaria > 8h de retrabalho | ADR-001 (stack) — trocar FastAPI por Flask reescreve backend | Abordagem de Desenvolvimento |
| G3 | **Questionabilidade acadêmica:** O Prof. Dr. Nivaldo Carleto poderia questionar a decisão na avaliação de um marco | ADR-004 (tasklists vs subissues) — "por que não usaram subissues?" | Stakeholders |
| G4 | **Trade-off não óbvio:** A decisão abre mão de uma alternativa viável em favor de outra, e a justificativa não é trivial | ADR-002 (Kanban sem sprints) — abre mão de iterações time-boxed | Abordagem de Desenvolvimento |

**Regra GMV:** Se a decisão atende a apenas 1 critério → commit message com prefixo `decision:`. Se atende a 0 → não se registra.

**Gatilhos Específicos por Fase do Ciclo de Vida:**

| Fase | Gatilho Provável | Exemplo |
| --- | --- | --- |
| MF1 (Fundação) | Seleção de stack, método de execução, métricas, configuração SSOT | ADRs 001–004 (já emitidas) |
| MF2 (Construção) | Troca de biblioteca, padrão arquitetural, estratégia de teste, decisão de API externa | Ex: "Adotar httpx vs requests para chamadas assíncronas" |
| MF3 (Consolidação) | Estratégia de release, formato de documentação final, decisão de licenciamento | Ex: "MIT vs GPLv3 para release final" |
| Transversal | Mudança de marco, alteração de escopo do MVP, contingência de risco materializado | Ex: "Reduzir REQ-06 para MVP se M3 estiver em risco" |

**Gatilhos Negativos (Quando NÃO Criar ADR):**

| Situação | Ação Correta | Justificativa GMV |
| --- | --- | --- |
| Decisão de formatação de código (lint, indentação) | Configuração no .editorconfig + commit | Não afeta ≥ 2 fases |
| Escolha de nome de variável ou função | Commit message | Reversível em < 5min |
| Ajuste de texto em plano (sem mudança de escopo) | Commit docs(plano-X): ajuste §Y | Não é decisão arquitetural |
| Decisão já coberta por ADR existente | Referência à ADR no commit | Evita proliferação |
| Decisão operacional do dia a dia | Daily assíncrona | Não é decisão de projeto |

### 5.2 ADR Tardia — Trade-offs e Política de Regularização

**Matriz de Trade-offs:**

| Dimensão | ADR Tempestiva (antes da execução) | ADR Tardia (após a execução) |
| --- | --- | --- |
| Rastreabilidade | ✅ Plena — decisão precede ação | ⚠️ Parcial — ação precede registro |
| Custo de produção | Baixo (contexto fresco) | Médio (requer reconstrução do raciocínio) |
| Risco de perda de contexto | Baixo | Alto (detalhes da deliberação se perdem) |
| Blindagem acadêmica | ✅ Máxima | ⚠️ Reduzida (pode parecer racionalização post hoc) |
| Overhead burocrático | Baixo (integra-se ao fluxo natural) | Médio (exige parada para documentar) |
| Valor para a equipe | Alto (guia a execução) | Médio (documenta o que já foi feito) |

**Política de Regularização (Regra GMV):**

| Condição | Ação | Prazo |
| --- | --- | --- |
| Decisão implementada há ≤ 48h e atende ≥ 2 gatilhos | Emitir ADR tardia com nota "Regularização" | ≤ 24h após identificação |
| Decisão implementada há > 48h e atende ≥ 2 gatilhos | Emitir ADR tardia + registrar lição aprendida | ≤ 72h |
| Decisão implementada e atende apenas 1 gatilho | NÃO emitir ADR; registrar em commit com prefixo decision: | Imediato |
| Decisão implementada e atende 0 gatilhos | Não registrar formalmente | — |

**Estrutura Obrigatória da ADR Tardia:**

Além dos campos padrão (Contexto, Opções, Decisão, Consequências, Trade-offs), a ADR tardia deve incluir:

~~~
**Tipo:** Regularização tardia
**Data da decisão efetiva:** [data em que foi aplicada]
**Data da formalização:** [data de emissão da ADR]
**Motivo da tardança:** [ex: "priorização de entrega do M1 sobre documentação"]
**Lição aprendida:** [ação preventiva para evitar recorrência]
~~~

**Trade-off declarado:** Aceita-se a ADR tardia como mal menor em relação à ausência total de registro, mas desincentiva-se sua recorrência. Se > 30% das ADRs do projeto forem tardias, o GP deve revisar o fluxo de trabalho na Retrospectiva.

### 5.3 Arquitetura de Integração Documental

**Princípio Diretor:** Documentos de governança são standalone; planos de área são coordenados; cross-references substituem duplicação.

**Estrutura de Diretórios Canônica no Repositório:**

~~~
/docs/
 ├── planos/
 │   ├── plano-integracao.md        ← Coordenador (referencia todos os demais)
 │   ├── plano-escopo.md
 │   ├── plano-cronograma.md
 │   ├── plano-custos.md
 │   ├── plano-qualidade.md
 │   ├── plano-recursos.md          ← M2
 │   ├── plano-comunicacoes.md      ← M2
 │   └── plano-riscos.md            ← M2
 ├── decisoes/
 │   ├── ADR-001-stack.md
 │   ├── ADR-002-kanban.md
 │   ├── ADR-003-metricas.md
 │   ├── ADR-004-tasklists.md
 │   └── ADR-005-freeze.md
 ├── conhecimento/
 │   ├── OKB.md                     ← Operational Knowledge Base
 │   ├── glossario.md               ← Glossário
 │   └── licoes-aprendidas/
 │       ├── MF1-licoes.md
 │       ├── MF2-licoes.md
 │       └── MF3-licoes.md
 ├── metricas/
 │   └── baseline.md                ← Pós-calibração (03/10)
 └── requisitos/
     └── requisitos.md              ← REQ-01 a REQ-15 (consolidados)
~~~

**Estratégia de Integração:**

| Documento | Estratégia | Justificativa GMV |
| --- | --- | --- |
| ADRs | Standalone em /docs/decisoes/ + tabela-resumo no Plano de Integração | ADRs são autocontidas; duplicá-las nos planos violaria SSOT |
| OKB | Standalone em /docs/conhecimento/OKB.md + referência no Plano de Integração §1.1 | Documento de governança transversal |
| Glossário | Standalone em /docs/conhecimento/glossario.md + referência no Plano de Integração §1.1 | Infraestrutura linguística do projeto |
| Lições Aprendidas | Standalone em /docs/conhecimento/licoes-aprendidas/ + resumo no encerramento de cada MF | Acumulação temporal |
| Baseline de Métricas | Standalone em /docs/metricas/baseline.md + referência no Plano de Cronograma §2.3 | Dado empírico; não é texto normativo |

**Anti-Padrões (o que NÃO fazer):**

| Anti-Padrão | Por que viola GMV | Ação Correta |
| --- | --- | --- |
| Copiar o texto integral da ADR-003 dentro do Plano de Cronograma | Duplicação; se a ADR for atualizada, o plano fica desatualizado | Referenciar: "Conforme ADR-003 (/docs/decisoes/ADR-003-metricas.md)" |
| Criar uma seção "Anexos" no final de cada plano | Infla extensão; viola limite de 4 páginas (GMV) | Cross-reference inline |
| Embutir o Glossário como seção do Plano de Integração | Glossário é transversal a todos os planos | Standalone + referência |
| Criar um "Super-Documento" que contém TAP + todos os planos + ADRs + Glossário | Viola SSOT; impossibilita versionamento granular | Documentos separados, coordenados pelo Plano de Integração |

**Mecanismo de Cross-Reference (Padrão Canônico):**

~~~markdown
Conforme [ADR-003 — Métricas de Fluxo](/docs/decisoes/ADR-003-metricas.md), 
as métricas EVM são declaradas LEGADO.

Conforme [OKB v3.0 §1.4 — Estratégia de Entrega Faseada](/docs/conhecimento/OKB.md#14), 
o M1 contempla 5 planos.
~~~

**Tabela-Resumo no Plano de Integração (Seção 1.4.1 — Índice de Documentos):**

| Documento | Localização | Função | Última Versão |
| --- | --- | --- | --- |
| OKB | /docs/conhecimento/OKB.md | Base de conhecimento operacional | v3.0 |
| Glossário | /docs/conhecimento/glossario.md | Vocabulário padronizado | v3.1 |
| ADR-001 | /docs/decisoes/ADR-001-stack.md | Stack tecnológica FOSS | Aprovada |
| ADR-002 | /docs/decisoes/ADR-002-kanban.md | Kanban como método | Aprovada |
| ADR-003 | /docs/decisoes/ADR-003-metricas.md | Métricas de fluxo | Aprovada |
| ADR-004 | /docs/decisoes/ADR-004-tasklists.md | Tasklists Markdown | Aprovada |
| ADR-005 | /docs/decisoes/ADR-005-freeze.md | Regime de freeze do TAP | ⏳ Antes do M2 |
| Baseline | /docs/metricas/baseline.md | Dados empíricos de fluxo | ⏳ Pós 03/10 |
| Lições MF1 | /docs/conhecimento/licoes-aprendidas/MF1.md | Aprendizados da Fundação | ⏳ 30/09 |

### 5.4 Ciclo de Vida da ADR no Fluxo Kanban

| Evento Kanban | Ação sobre ADR |
| --- | --- |
| Card com label change-request aprovado pelo CCB | Se a mudança atende ≥ 2 gatilhos → criar card de ADR |
| Card de ADR criado | Tipo: docs · Área: area:integracao · Macro-fase: vigente |
| ADR em In Progress | GP redige (estimativa ≤ 2h por ADR) |
| ADR em Code Review | Revisão por 1 par (Fabricio ou Edson) |
| ADR em Done | Commit docs(adr): ADR-0XX — [título] + atualização da tabela no OKB §4 |

**Limite de ADRs por Marco (GMV):**

| Marco | Máximo de ADRs novas | Justificativa |
| --- | --- | --- |
| M1 (22/09) | 4 (já emitidas: 001–004) | Fundação completa; não adicionar mais |
| M2 (30/09) | ≤ 2 | Ex: ADR de baseline de métricas + eventual ajuste de stack |
| M3 (15/11) | ≤ 3 | Ex: padrão de API, estratégia de teste, fallback de API externa |
| M4 (15/12) | ≤ 1 | Ex: decisão de licenciamento final |

**Total projetado:** ≤ 10 ADRs ao longo do ciclo de vida. Acima disso, o GP deve questionar se o projeto está burocratizando decisões menores.

---

## SEÇÃO 6 — PRODUÇÃO VISUAL: RODADAS DE DIAGRAMAS

> **Diretrizes de padronização:** Paleta convergente (fundo #FFFFFF, Arial, MF1 #1F3A5F, MF2 #2E7D32, MF3 #6A1B9A), sem overlaps, legendas ABNT externas ao SVG.

### 6.1 RODADA 1 — EAP FRACIONADA (4 SVGs) — 20/09/2026

**Justificativa do fracionamento:** A geração de um diagrama único contendo as 12 fases e 37 pacotes de trabalho exigiria um `viewBox` excessivamente largo (ex: `3000x1000`), resultando em fontes minúsculas (<10px) e quebra da regra de legibilidade.

**Arquivos gerados:**
1. `fig-eap-nivel-0-macro.svg` — Visão Macro (N0 e Macro-Fases)
2. `fig-eap-mf1-fundacao.svg` — Detalhamento MF1 (6 fases, 20 pacotes)
3. `fig-eap-mf2-construcao.svg` — Detalhamento MF2 (4 fases, 12 pacotes)
4. `fig-eap-mf3-consolidacao.svg` — Detalhamento MF3 (2 fases, 5 pacotes)

*(SVGs completos preservados no documento-fonte — ver notas_adjacentes.md §Rodada 1)*

**Nota de Governança NA-01:**
- Assunto: Padronização Gráfica e Fracionamento da EAP
- Data: 21/09/2026
- Decisão: A EAP foi fracionada em 4 camadas lógicas. Esta ação não constitui mudança de escopo, mas sim refinamento de artefato de suporte (GMV).

### 6.2 RODADA 2 — GOVERNANÇA E MUDANÇAS (2 SVGs) — 21/09/2026

**Arquivos gerados:**
1. `fig-1-governanca-hibrida.svg` — Modelo de Governança Híbrida Trifásico
2. `fig-4-controle-mudancas.svg` — Fluxo de Controle Integrado de Mudanças

*(SVGs completos preservados no documento-fonte)*

### 6.3 RODADA 3 — CFD E SEQUENCIAMENTO (2 SVGs) — 21/09/2026

**Arquivos gerados:**
1. `fig-3-cfd-saudavel-vs-gargalo.svg` — CFD: Padrão Saudável vs. Gargalo
2. `fig-1-sequenciamento-macro-caminho-critico.svg` (v1 — SUPERSEDED)

### 6.4 CORREÇÃO 3.5 — FIX DE OVERLAP (1 SVG REFEITO) — 21/09/2026

**Problema:** O overlap grosseiro no diagrama anterior ocorreu devido a uma falha de ancoragem: múltiplas setas convergiam para um único ponto cartesiano (`500, 200`), empilhando as pontas das flechas, somado a um viewBox subdimensionado.

**Correções aplicadas:**
1. Canvas Expandido: `viewBox` ajustado para `1200 x 700`
2. Ancoragem Distribuída: Setas dos 4 detectores apontam para pontos distintos
3. Tipografia Blindada: Substituição de textos soltos por blocos `<tspan>` com dy controlado
4. Fluxo de Feedback Orgânico: Seta curva tracejada conectando camada operacional à macro

**Arquivo:** `fig-1-sequenciamento-macro-caminho-critico.svg` (v2 — CANÔNICA)

### 6.5 NOTAS TÉCNICAS ABNT RETROATIVAS (7 FIGURAS) — 21/09/2026

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
Nota: Ilustração da hierarquia normativa que rege o projeto COGME. A seta de realimentação representa o ciclo contínuo de lições aprendidas.
Fonte: Elaborado pelos autores (2026).

**Figura 6** – Fluxo de Controle Integrado de Mudanças.
Nota: Materialização do Processo 4.6 do PMBOK® 6ª (dicionário) adaptado ao fluxo contínuo Kanban.
Fonte: Elaborado pelos autores (2026).

**Figura 7** – Cumulative Flow Diagram (CFD) — Padrão Saudável vs. Padrão com Gargalo.
Nota: Ferramenta visual de monitoramento temporal que substitui formalmente o Gráfico de Gantt e o EVM (ADR-003).
Fonte: Elaborado pelos autores (2026).

### 6.6 RODADA 4 — FLUXO KANBAN (1 SVG) — 21/09/2026

**Arquivo:** `fig-2-fluxo-kanban-oficial.svg`
**Nota Técnica ABNT (Figura 8):** O diagrama materializa operacionalmente a ADR-002 e a ADR-004. As cinco colunas representam o fluxo contínuo do trabalho com quatro gates de qualidade intermediários.

### 6.7 RODADA 5 — CUSTOS (2 SVGs) — 21/09/2026

**Arquivos:**
1. `fig-5-fluxo-prevencao-custos.svg` — Fluxo de Prevenção de Custos
2. `fig-6-matriz-rastreabilidade-dependencias.svg` — Matriz de Rastreabilidade de Dependências

### 6.8 RODADA 6 — ESCOPO (2 SVGs) — 21/09/2026

**Arquivos:**
1. `fig-eap-visao-executiva.svg` — EAP Visão Executiva Consolidada
2. `fig-2-cadeia-decomposicao-escopo.svg` — Cadeia de Decomposição do Escopo e Gates

### 6.9 MATRIZ CONSOLIDADA DE RASTREABILIDADE DE DIAGRAMAS (FINAL)

| ID | Arquivo | Descrição | Plano / Seção | Rodada |
| --- | --- | --- | --- | --- |
| FIG-EAP-01 | fig-eap-nivel-0-macro.svg | Visão Macro (N0 e Macro-Fases) | Escopo §2.5 | R1 |
| FIG-EAP-02 | fig-eap-mf1-fundacao.svg | Detalhamento MF1 | Escopo §2.5 | R1 |
| FIG-EAP-03 | fig-eap-mf2-construcao.svg | Detalhamento MF2 | Escopo §2.5 | R1 |
| FIG-EAP-04 | fig-eap-mf3-consolidacao.svg | Detalhamento MF3 | Escopo §2.5 | R1 |
| FIG-GOV-01 | fig-1-governanca-hibrida.svg | Governança Híbrida Trifásico | Integração §1.2 | R2 |
| FIG-MUD-01 | fig-4-controle-mudancas.svg | Fluxo de Controle de Mudanças | Integração §1.7.2 | R2 |
| FIG-CFD-01 | fig-3-cfd-saudavel-vs-gargalo.svg | CFD Saudável vs. Gargalo | Integração §1.6.1 | R3 |
| FIG-SEQ-01 | fig-1-sequenciamento-macro-caminho-critico.svg | Sequenciamento + Caminho Crítico | Cronograma §3.4 | R3→R3.5 |
| FIG-KAN-01 | fig-2-fluxo-kanban-oficial.svg | Fluxo Kanban com Gates e WIP | Integração §1.3.1 | R4 |
| FIG-CUST-01 | fig-5-fluxo-prevencao-custos.svg | Fluxo de Prevenção de Custos | Custos §4.2 | R5 |
| FIG-CUST-02 | fig-6-matriz-rastreabilidade-dependencias.svg | Matriz de Rastreabilidade | Custos §4.5.2 | R5 |
| FIG-ESC-01 | fig-eap-visao-executiva.svg | EAP Visão Executiva | Escopo §2.5 | R6 |
| FIG-ESC-02 | fig-2-cadeia-decomposicao-escopo.svg | Cadeia de Decomposição + Gates | Escopo §2.5 | R6 |

**Total: 13 diagramas canônicos** (14 SVGs produzidos; 1 refação por overlap na R3.5).

---

## SEÇÃO 7 — ESTRUTURA DO REPOSITÓRIO

> **Contexto:** Esta seção é orientante para toda a documentação e operação do projeto. A estrutura de diretórios tem a pretensão de ser imutável o quanto possível, salvo necessidades justificadas. Todo arquivo deve ser mapeado e endereçado ao diretório responsável. Não são permitidos arquivos órfãos na raiz exceto aqueles que sabidamente devem à raiz pertencer.

### 7.1 Estrutura Canônica Proposta

~~~
COGME/
 ├── .ai/                              # Contexto SDD (lido pela IA — Glossário §5)
 │   ├── personas/                     # Personas SDD (symlinks → active.md)
 │   │   ├── _base.md
 │   │   ├── pm.md
 │   │   ├── coder.md
 │   │   ├── reviewer.md
 │   │   ├── tester.md
 │   │   └── active.md → pm.md
 │   ├── specs/                        # Especificações imutáveis
 │   │   ├── tap.md
 │   │   ├── eap.md
 │   │   └── requisitos.md
 │   ├── handoffs/                     # Artefatos entre fases SDD
 │   │   └── 001-tap-foundation.md
 │   └── workflows/                    # Automação bash do ciclo SDD
 │       └── sdd-cycle.sh
 │
 ├── docs/                             # Documentação humana
 │   ├── planos/                       # 8 planos de gerenciamento
 │   │   ├── plano-integracao.md
 │   │   ├── plano-escopo.md
 │   │   ├── plano-cronograma.md
 │   │   ├── plano-custos.md
 │   │   ├── plano-qualidade.md
 │   │   ├── plano-recursos.md         ← M2
 │   │   ├── plano-comunicacoes.md     ← M2
 │   │   └── plano-riscos.md           ← M2
 │   ├── decisoes/                     # ADRs
 │   │   ├── ADR-001-stack.md
 │   │   ├── ADR-002-kanban.md
 │   │   ├── ADR-003-metricas.md
 │   │   ├── ADR-004-tasklists.md
 │   │   └── ADR-005-freeze.md
 │   ├── conhecimento/                 # Base de conhecimento
 │   │   ├── OKB.md
 │   │   ├── glossario.md
 │   │   ├── drafts/                   # Arquivos de trabalho (não canônicos)
 │   │   └── licoes-aprendidas/
 │   │       ├── MF1-licoes.md
 │   │       ├── MF2-licoes.md
 │   │       └── MF3-licoes.md
 │   ├── dependencias/
 │   │   └── registro.md
 │   ├── diagramas/                    # Diagramas dos planos
 │   │   ├── cronograma/
 │   │   ├── custos/
 │   │   ├── eap/
 │   │   ├── integracao/
 │   │   ├── qualidade/
 │   │   └── mermaid-config.json
 │   ├── metricas/
 │   │   └── baseline.md
 │   ├── planos/
 │   ├── requisitos/
 │   │   └── requisitos.md
 │   ├── tap/
 │   │   ├── TAP.md
 │   │   └── TAP.docx
 │   └── archive/                      # Artefatos históricos
 │       ├── diagramas-deprecated/
 │       ├── docx/
 │       ├── eap-legacy/
 │       ├── images-legacy/
 │       └── tap-sections/
 │
 ├── src/                              # Código-fonte (MVP — M2/M3)
 │   ├── backend/
 │   │   ├── main.py
 │   │   ├── models/
 │   │   ├── routers/
 │   │   └── services/
 │   ├── frontend/
 │   │   ├── static/
 │   │   └── templates/
 │   └── shared/
 │       └── schemas.py
 │
 ├── tests/
 │   ├── integration/
 │   └── unit/
 │
 ├── .github/
 │   └── workflows/
 │       └── ci.yml
 │
 ├── README.md
 ├── LICENSE
 ├── pyproject.toml
 ├── requirements.txt
 └── .gitignore
~~~

### 7.2 Estrutura Atual Real do Repositório (Mapeamento)

~~~
.
├── docs
│   ├── archive
│   │   ├── diagramas-deprecated/
│   │   │   ├── [legacy]-fig-01-governanca-hibrida.png
│   │   │   ├── [legacy]-fig-02-fluxo-kanban_alt.png
│   │   │   ├── [legacy]-fig-02-fluxo-kanban_alt.svg
│   │   │   ├── [legacy]-fig-02-fluxo-kanban.png
│   │   │   ├── [legacy]-fig-02-fluxo-kanban.svg
│   │   │   ├── [legacy]-fig-03-cfd-comparativo.png
│   │   │   ├── [legacy]-fig-03-cfd-comparativo.svg
│   │   │   ├── [legacy]-fig-04-fluxo-mudancas.png
│   │   │   ├── [legacy]-fig-04-fluxo-mudancas.svg
│   │   │   └── [legacy]-fig-1-fluxo-qualidade.png
│   │   ├── docx/
│   │   │   ├── AC1_Integracao.docx
│   │   │   ├── AC2_Escopo.docx
│   │   │   ├── AC3_cronograma.docx
│   │   │   ├── AC4_Custos.docx
│   │   │   ├── AC_qualidade.docx
│   │   │   └── _archive/
│   │   ├── eap-legacy/
│   │   │   ├── correcao/
│   │   │   └── inicial/
│   │   ├── images-legacy/
│   │   │   └── diagramas/
│   │   │       ├── custos/
│   │   │       └── escopo/
│   │   └── tap-sections/
│   ├── conhecimento
│   │   ├── drafts/
│   │   │   ├── analise_arquitetural.md
│   │   │   ├── Canon_Stack_SDD.md
│   │   │   ├── estrutura-de-diretorios.md
│   │   │   ├── glossario.md
│   │   │   ├── hardware.md
│   │   │   ├── [legacy]-redacao_progressiva.md
│   │   │   ├── llm_base_persona.md
│   │   │   ├── monitoramenteo_inconsistencias.md
│   │   │   ├── notas_adjacentes.md
│   │   │   ├── OKB_COGME_v3.0.md
│   │   │   ├── premissas.md
│   │   │   ├── principais_requisitos_entregas.md
│   │   │   ├── proposta_estrutural.md
│   │   │   ├── reestrutura_EAP.md
│   │   │   ├── refac_prompt.md
│   │   │   ├── relatorio_avaliacao_critica_TAP.md
│   │   │   ├── Relat_Transicao_TAP_AreasConhecimento.md
│   │   │   ├── req_1.0.docx
│   │   │   ├── sec_4_EAP.docx
│   │   │   └── support_research.md
│   │   ├── glossario.md
│   │   ├── licoes-aprendidas/
│   │   │   ├── MF1-licoes.md
│   │   │   ├── MF2-licoes.md
│   │   │   └── MF3-licoes.md
│   │   └── OKB.md
│   ├── decisoes/
│   │   ├── ADR-001-stack.md
│   │   ├── ADR-002-kanban.md
│   │   ├── ADR-003-metricas.md
│   │   ├── ADR-004-tasklists.md
│   │   └── ADR-005-freeze.md
│   ├── dependencias/
│   │   └── registro.md
│   ├── diagramas/
│   │   ├── cronograma/
│   │   │   └── fig-01-sequenciamento-macro-caminho-critico.svg
│   │   ├── custos/
│   │   │   ├── fig-01-fluxo-prevencao-custos.png
│   │   │   └── fig-01-fluxo-prevencao-custos.svg
│   │   ├── eap/
│   │   │   ├── fig-01-eap-executiva.svg
│   │   │   ├── fig-eap-mf1-fundacao.svg
│   │   │   ├── fig-eap-mf2-construcao.svg
│   │   │   ├── fig-eap-mf3-consolidacao.svg
│   │   │   ├── fig-eap-nivel-0-macro.png
│   │   │   ├── fig-eap-nivel-0-macro.svg
│   │   │   └── [legacy]-EAP_COGME_v3.0_*.drawio*
│   │   ├── fig-4-controle-mudancas.svg
│   │   ├── integracao/
│   │   │   ├── fig-02-matriz-rastreabilidade-dependencias.png
│   │   │   ├── fig-02-matriz-rastreabilidade-dependencias.svg
│   │   │   ├── fig-1-governanca-hibrida.svg
│   │   │   └── fig-3-cfd-saudavel-vs-gargalo.svg
│   │   ├── mermaid-config.json
│   │   └── qualidade/
│   │       └── [legacy]-fig-*.svg/png
│   ├── metricas/
│   │   └── baseline.md
│   ├── planos/
│   │   ├── plano-comunicacoes.md
│   │   ├── plano-cronograma.md
│   │   ├── plano-custos.md
│   │   ├── plano-escopo.md
│   │   ├── plano-integracao.md
│   │   ├── plano-qualidade.md
│   │   ├── plano-recursos.md
│   │   └── plano-riscos.md
│   ├── requisitos/
│   │   └── requisitos.md
│   ├── tap/
│   │   ├── TAP.docx
│   │   └── TAP.md
│   └── xml/
│       └── EAP_TAP/correcao/
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
├── src/
│   ├── backend/
│   │   ├── main.py
│   │   ├── models/__init__.py
│   │   ├── routers/__init__.py
│   │   └── services/__init__.py
│   ├── frontend/
│   │   ├── static/
│   │   └── templates/index.html
│   └── shared/schemas.py
└── tests/
    ├── integration/__init__.py
    └── unit/__init__.py

48 directories, 142 files
~~~

### 7.3 Mapeamento: Arquivo Atual → Novo Local (Principais)

**Planos de Gerenciamento:**

| Arquivo Atual | Novo Local |
| --- | --- |
| docs/md/planos/AC_integracao/AC1_Integracao.md | docs/planos/plano-integracao.md |
| docs/md/planos/AC_Escopo/AC2_Escopo.md | docs/planos/plano-escopo.md |
| docs/md/planos/AC_Cronograma/AC3_cronograma.md | docs/planos/plano-cronograma.md |
| docs/md/planos/AC_custos/AC4_Custos.md | docs/planos/plano-custos.md |
| docs/md/planos/AC_qualidade/AC_qualidade.md | docs/planos/plano-qualidade.md |

**Arquivos de Trabalho (→ drafts):**

| Arquivo Atual | Novo Local |
| --- | --- |
| redacao_progressiva.md | docs/conhecimento/drafts/[legacy]-redacao_progressiva.md |
| notas_adjacentes.md | docs/conhecimento/drafts/notas_adjacentes.md |
| estrutura-de-diretorios.md | docs/conhecimento/drafts/estrutura-de-diretorios.md |

---

## SEÇÃO 8 — REGISTRO DE INCIDENTE: LA-001

> **Data:** 22/09/2026
> **Macro-Fase:** MF1 (Fundação)
> **Domínio PMBOK 7ª:** Trabalho do Projeto + Entrega

### 8.1 Acknowledgment

Recebo sua comunicação. A decisão de executar a reestruturação em paralelo com produção ativa de artefatos é um trade-off consciente que você assumiu como GP. Não há julgamento — há aprendizado. O que importa agora é recuperar o máximo possível e registrar a lição para que o PDCA do projeto absorva essa experiência.

### 8.2 Análise de Impacto

**Diagramas Recentes (Alta Probabilidade de Perda Parcial):**

| Arquivo Original | Status na Reestruturação | Risco |
| --- | --- | --- |
| docs/diagrams/fig-1-eap-executiva.svg | Movido para docs/diagramas/eap/fig-01-eap-executiva.svg | ⚠️ Verificar |
| docs/diagrams/fig-1-sequenciamento-macro-caminho-critico.svg | Movido para docs/diagramas/cronograma/ | ⚠️ Verificar |
| docs/diagrams/fig-eap-mf1-fundacao.svg | Movido para docs/diagramas/eap/ | ⚠️ Verificar |
| docs/diagrams/fig-eap-mf2-construcao.svg | Movido para docs/diagramas/eap/ | ⚠️ Verificar |
| docs/diagrams/fig-eap-mf3-consolidacao.svg | Movido para docs/diagramas/eap/ | ⚠️ Verificar |
| docs/diagrams/fig-eap-nivel-0-macro.svg/.png | Movido para docs/diagramas/eap/ | ⚠️ Verificar |
| docs/diagrams/fig-3-cfd-saudavel-vs-gargalo.svg | Arquivado em docs/archive/diagramas-deprecated/ | ⚠️ Pode conter refinamentos |
| docs/diagrams/fig-4-controle-mudancas.svg | Arquivado em docs/archive/diagramas-deprecated/ | ⚠️ Pode conter refinamentos |
| docs/diagrams/1.svg | Nunca classificado (Anomalia A1) | 🔴 Provavelmente perdido |
| docs/diagrams/fig-02-fluxo-kanban.mmd.png | Deletado, sem correspondente canônico | 🔴 Perdido |

**Textos de Projeto Recentes (Média Probabilidade):**

| Arquivo | Movido Para | Risco |
| --- | --- | --- |
| docs/md/relatorios/analise_arquitetural.md | docs/conhecimento/drafts/ | ⚠️ |
| docs/md/relatorios/Canon_Stack_SDD.md | docs/conhecimento/drafts/ | ⚠️ |
| docs/md/relatorios/hardware.md | docs/conhecimento/drafts/ | ⚠️ |
| docs/md/relatorios/llm_base_persona.md | docs/conhecimento/drafts/ | ⚠️ |
| redacao_progressiva.md (raiz) | docs/conhecimento/drafts/ | ⚠️ |
| notas_adjacentes.md (raiz) | docs/conhecimento/drafts/ | ⚠️ |

**Arquivos Potencialmente Perdidos (Sem Rastro):**

| Arquivo | Evidência | Status |
| --- | --- | --- |
| docs/diagrams/1.svg | Aparecia como untracked no git status anterior | 🔴 Provavelmente perdido |
| docs/diagrams/fig-02-fluxo-kanban.mmd.png | Aparecia como deleted, sem correspondente | 🔴 Perdido |

### 8.3 Estratégia de Recuperação

~~~bash
# 1. Verificar histórico recente (últimas 48h)
git log --since="2026-09-20" --oneline --all

# 2. Ver reflog para encontrar estados anteriores
git reflog --since="2026-09-20"

# 3. Se encontrar um commit anterior à reestruturação com trabalho recente:
# git show <hash>:<caminho-do-arquivo> > /tmp/recovered_file.ext

# 4. Listar todos os arquivos deletados nos últimos commits
git log --diff-filter=D --summary --since="2026-09-20" --name-only

# 5. Recuperar um arquivo específico de um commit anterior
# git checkout <hash> -- <caminho-do-arquivo>
~~~

### 8.4 Priorização do Retrabalho

| Prioridade | Item | Esforço | Justificativa |
| --- | --- | --- | --- |
| P0 | Verificar docs/diagrams/1.svg (Anomalia A1) | 5 min | Pode ser diagrama crítico não identificado |
| P0 | Regenerar fig-02-fluxo-kanban.mmd.png | 15 min | Renderização Mermaid do fluxo Kanban |
| P1 | Verificar CFD deprecated vs canônico | 10 min | Pode conter versão mais detalhada |
| P1 | Verificar controle-mudancas deprecated vs canônico | 10 min | Pode conter versão mais detalhada |
| P1 | Revisar drafts reestrutura_EAP.md e proposta_estrutural.md | 30 min | Podem conter decisões recentes |
| P2 | Revisar analise_arquitetural.md | 20 min | Relevante para M2 |
| P2 | Revisar llm_base_persona.md | 15 min | Base para personas SDD |
| P3 | Varredura geral de drafts | 1h | Conteúdo recuperável |

### 8.5 Lição Aprendida — LA-001

**O que aconteceu:** A reestruturação formal do repositório foi executada em paralelo com produção ativa de diagramas e textos de projeto. Durante a movimentação de arquivos, alguns artefatos recentes foram perdidos ou deslocados.

**Causa raiz:**
1. Ausência de branch dedicada para reestruturação (operação em `main` direta)
2. Uso de `mv` do sistema em vez de `git mv` (perda de rastreabilidade de rename)
3. Execução de `git add -A` sem verificação prévia da árvore de destino
4. Produção ativa de artefatos durante a janela de reestruturação

**Impacto:**
- Perda de 1-2 diagramas recentes
- Deslocamento temporário de diagramas canônicos para archive
- Necessidade de retrabalho estimado em 2-3h

**Ação corretiva (imediata):**
- Commit corretivo `fix(diagramas)` para restaurar localização canônica
- Verificação via `git reflog` para recuperação de artefatos perdidos
- Retrabalho priorizado dos itens P0-P2

**Ação preventiva (futuro):**
- **Regra:** Reestruturações de diretório SEMPRE em branch dedicada (`chore/restructure-*`)
- **Regra:** Usar `git mv` em vez de `mv` para qualquer movimentação de arquivo versionado
- **Regra:** Congelar produção de artefatos durante reestruturação (janela de manutenção)
- **Regra:** Verificar `tree` da estrutura de destino ANTES de `git add -A`
- **Regra:** Commit único de reestruturação com mensagem descritiva + tag de rollback

**Rastreabilidade:**
- Commits: `7121d12`, `1aa1515`
- OKB v3.0 §3.2 (SSOT documental)
- Glossário §5 (Stack SDD)

**Localização canônica:** `docs/conhecimento/licoes-aprendidas/MF1-licoes.md`

### 8.6 Recomendação Imediata ao GP

1. Execute os comandos da seção 8.3 para verificar se há commits recuperáveis via `git reflog`
2. Execute as comparações para verificar versões arquivadas vs canônicas
3. Retrabalhe os itens P0 (5-20 min) antes de prosseguir com qualquer nova produção
4. Registre LA-001 em `docs/conhecimento/licoes-aprendidas/MF1-licoes.md`
5. Prosseguir com o Plano de Qualidade (Área 5) apenas após confirmar que os diagramas de Ishikawa estão íntegros em `docs/diagramas/qualidade/`

---

## SEÇÃO 9 — CONSOLIDAÇÃO DE INCONSISTÊNCIAS SANADAS

| # | Inconsistência | Localização Original | Resolução |
| --- | --- | --- | --- |
| I1 | Matriz de rastreabilidade repetida 6 vezes | Rodadas 1–6 | Consolidada em versão final única (Seção 6.9) |
| I2 | SVG v1 do sequenciamento com overlap | Rodada 3 | Marcado como SUPERSEDED; versão canônica = v2 |
| I3 | Notas ABNT das Figuras 1-4 apareciam soltas | Rodada 1 + retroativas | Consolidadas em Seção 6.5 |
| I4 | Nota de Governança NA-01 mencionava diagramas futuros | Rodada 1 | Contextualizada como referência futura |
| I5 | Contagem de pacotes na Nota da Figura 11 | Rodada 6 | Verificada: MF1=20, MF2=12, MF3=5, Total=37 ✓ |
| I6 | Fronteira M1 ambígua (5 vs 8 planos) | TAP §6 vs OKB v2.2 | Resolvida: Entrega Faseada (5 M1 + 3 M2) |
| I7 | Estrutura de diretórios proposta vs atual divergente | Proposta vs real | Ambas documentadas; mapeamento de migração fornecido |

---

## NOTA DE ENCERRAMENTO

**Status:** Documento reorganizado, desduplicado e sequenciado temporalmente com conteúdo integral preservado. Seções de configuração operacional (labels, milestones, padrões de cards, prioridade), backlog M1 (21 cards), política de ADRs, estrutura de repositório (proposta + atual) e literatura de apoio incluídas.

**Sinalizações ao GP:**
1. **Estrutura de diretórios:** Seção 7 documenta tanto a estrutura canônica proposta quanto a estrutura atual real, com mapeamento de migração. Esta seção é orientante para toda a documentação.
2. **Backlog M1:** 21 cards detalhados com distribuição de trabalho, tasklists ADR-004 e verificação de capacidade.
3. **Configuração SSOT:** 27 labels, 5 milestones, Padrões A/B e P0–P3 formalizados.
4. **Política de ADRs:** Gatilhos, ADR tardia, integração documental e limites por marco.
5. **LA-001:** Incidente registrado com ações preventivas para evitar recorrência.

**Próxima ação sugerida:** Confirmar integridade dos diagramas em `docs/diagramas/` e executar os comandos de recuperação da Seção 8.3 antes de prosseguir com novas produções.

**Fim do documento — Notas Adjacentes v2.0 | COGME | Fatec Taquaritinga | 19–22/09/2026**