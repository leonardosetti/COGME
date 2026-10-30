# ADR-012 — Constituição como Artefato Normativo Supremo e Mecanismo de Restauração Constitucional

| Campo                                         | Valor                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Versão**                             | 1.0.1                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Status**                              | Aprovado (ratificado pelo CCB-002 em 29/10/2026)                                                                                                                                                                                                                                                                                                                                                                         |
| **Data da decisão**                    | 29/10/2026                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Data de formalização do documento** | 29/10/2026                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Decisor**                             | GP Leonardo (CCB único — TAP v3 §1.c, Premissa P7)                                                                                                                                                                                                                                                                                                                                                                    |
| **Gatilhos G1–G4**                     | G1 (impacto transversal — define a validade de TODOS os outros artefatos), G2 (irreversibilidade prática — corrupção ou perda da Constituição invalida o ecossistema inteiro), G3 (questionabilidade acadêmica — "por que uma Constituição separada do Plano de Gerenciamento?"), G4 (trade-off não óbvio — rigidez normativa × segurança contra deriva algorítmica)                                    |
| **Rastreabilidade**                     | TAP §1 (Identidade) + §2 (Restrições Éticas/Legais); EAP N1.1 (Definição do Projeto); REQ-12 (ADRs); ADRs correlatas: ADR-005 (fundamenta o freeze do TAP, mas a Constituição está ACIMA dele), ADR-008 (grafia canônica blindada constitucionalmente), ADR-011 (MCPs e L1/L2/L3 subordinados à Constituição); CCB-001 e CCB-002 (instrumentos de ratificação); Monografia Cap. 3 (Governança Híbrida) |
| **Domínio PMBOK 7ª**                  | Integração + Trabalho do Projeto + Incerteza                                                                                                                                                                                                                                                                                                                                                                           |
| **Processo PMBOK 6ª (dicionário)**    | 4.1 Desenvolver Plano de Gerenciamento do Projeto; 4.6 Realizar Mudanças Integradas; 13.2 Gerenciar Engajamento das Partes Interessadas                                                                                                                                                                                                                                                                                 |

## Contexto

O projeto COGME opera sob uma dualidade complexa: é simultaneamente um produto de software (conversor cambial FOSS) e um laboratório experimental de engenharia assistida por IA (SDD com agentes autônomos locais). Nessa configuração, surgiram riscos críticos de **deriva normativa**:

1. **Fragmentação de Autoridade:** Inicialmente, tentou-se gerir a governança exclusivamente via TAP e Planos. Contudo, a chegada de modelos generativos exigiu regras mais estritas sobre soberania de dados, precisão linguística e limites éticos que transcendem o escopo técnico tradicional.
2. **Corrupção Institucional Detectada:** Em rodadas anteriores, identificou-se que a `constitution.md` v1.1.0 sofreu degradação semântica e estrutural (contradições internas, referências obsoletas, ausência de reconhecimento de MCPs/Docker), tornando-a inviável como fonte única de verdade. Isso evidenciou a fragilidade de confiar a integridade sistêmica a um arquivo passível de edição acidental ou maliciosa sem salvaguardas robustas.
3. **Subordinação de Inputs Canônicos:** Modelos locais tendem a tratar prompts extensos ("inputs canônicos") como normas supremas se não houver uma barreira clara estabelecendo que tais prompts são meramente derivativos. Sem essa distinção constitucional explícita, há risco de alucinação normativa onde o agente inventa regras baseadas em contexto temporário.

A situação exigia a elevação da `constitution.md` ao patamar de **Lei Suprema Imutável Exceto Por Emenda Formal**, dotada de mecanismos próprios de detecção de corrupção e restauração integral, distinta dos planos executáveis e das especificações técnicas.

## Opções Consideradas

| #  | Opção                                                                                | Prós                                                                                                                                                                  | Contras                                                                                                                                                                                             |
| -- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| O1 | Manter governança integrada no TAP e Planos                                           | Simplicidade aparente; menos arquivos                                                                                                                                  | Mistura matéria autorizativa (TAP) com operacional (Planos) e ética/normativa (Constituição); difícil de auditar separadamente; vulnerável a edições indevidas de escopo durante execução |
| O2 | Criar uma "Cartilha de Agentes" separada da Constituição                             | Foca na interação humana-agente                                                                                                                                      | Deixa lacuna jurídica para o produto em si; cria duas fontes de verdade concorrentes; ignora requisitos legais (LGPD) e éticos universais                                                         |
| O3 | Elevar `constitution.md` a Artefato Normativo Supremo com protocolo de restauração | Clareza hierárquica absoluta; proteção contra deriva; mecanismo robusto de recuperação de desastres normativos; subordinação clara de todos os demais artefatos | Rigidez inicial; exige disciplina rigorosa de versionamento e hashing; overhead de manutenção da integridade textual                                                                              |

## Decisão

**Aprovar a opção O3.**

Fica instituída a **ADR-012**, declarando a `constitution.md` como o ápice incontestável da hierarquia normativa do COGME, regida pelos seguintes princípios fundamentais:

### 1. Supremacia e Imutabilidade Condicional

A Constituição prevalece sobre qualquer outro artefato (TAP, ADRs, OKB, Planos, Specs, Código). Nenhuma ADR, CR ou Input Canônico pode contradizê-la. Alterações somente ocorrem via **Emenda Constitucional** aprovada pelo CCB humano (GP Leonardo), seguida de bump de versão (`MAJOR.MINOR.PATCH`) e registro de co-assinatura com hash SHA-256 do conteúdo normativo (excluindo o bloco de assinatura para evitar autorreferência).

### 2. Hierarquia Trifásica Explícita

Para eliminar ambiguidades, a Constituição estabelece duas vertentes de autoridade distintas, porém complementares:

* **Hierarquia de Projeto (Matéria de Negócio/Escopo):**
  `Constitution` > `TAP v3 (Congelado)` > `ADRs Técnicas` > `OKB` > `Planos` > `Glossário` > `Inputs Canônicos` > `Código`.
* **Hierarquia de Forja (Matéria de Agentes/SDD):**
  `Constitution` > `Diretiva AFA-ULTIMATE` > `Roster de Agentes` > `Personas/MCPs` > `Scripts`.

Esta separação garante que decisões de escopo (ex.: adicionar feature X) sigam o fluxo TAP→EAP→Card, enquanto decisões de comportamento do modelo (ex.: alterar persona Y) sigam o fluxo AFA→Registry→Persona, ambas ancoradas na mesma lei suprema.

### 3. Subordinação Rígida de Inputs Canônicos e Prompts

Qualquer prompt de sistema, input consolidado, memória ubíqua ou handoff JSON é classificado como **artefato derivativo**. Ele operacionaliza a vontade expressa na Constituição, mas não cria norma autônoma. Em caso de conflito interpretativo entre um input longo e um artigo constitucional curto, prevalece sempre o artigo constitucional. Os agentes devem ser programados para rejeitar instruções implícitas em contextos que violem artigos explícitos da Constituição (ex.: envio de dados sensíveis para cloud não whitelistada).

### 4. Protocolo de Detecção e Restauração de Corrupção

Diante do histórico de degradação do arquivo, institui-se o **Protocolo de Integridade Constitucional**:

* **Hash de Referência:** Cada versão promulgada possui um hash SHA-256 calculado sobre o corpo normativo (sem metadados variáveis como timestamps de edição recentes).
* **Backup Forense Automático:** Antes de qualquer modificação proposta pelo circuito SDD, a versão vigente deve ser copiada para `docs/archive/corrupted/` ou `docs/archive/history/`, garantindo rastreabilidade reversa.
* **Restauração Integral:** Se for detectada inconsistência lógica, truncamento ou violação de hierarquia na `constitution.md` ativa, o processo de correção não é via "patch", mas via **restauração completa** a partir da última versão validada e assinada pelo CCB. Isso elimina o risco de fusões semânticas errôneas.
* **Kill Switch Constitucional:** Qualquer tentativa de modificar a Constituição fora do fluxo de Emenda Formal (Art. 9 da própria Constituição) dispara abortamento imediato das operações do circuito SDD e escalonamento obrigatório ao CCB humano.

### 5. Relação com AFA-ULTIMATE e CCB

* **AFA-ULTIMATE:** Atua como executor técnico da governança, validando contratos de agentes e roteamento, mas está estritamente subordinado à Constituição. Não tem poder legislativo próprio.
* **CCB (Comitê de Controle de Mudanças):** Representado exclusivamente pelo GP Leonardo, detém o monopólio da interpretação final e da aprovação de emendas. Agentes podem sugerir emendas, mas jamais aprová-las autonomamente.

## Consequências

- Positivas: Eliminação definitiva de dúvidas sobre qual artefato manda em caso de conflito; proteção robusta contra alucinações normativas dos LLMs; capacidade de recuperação rápida após incidentes de corrupção documental; alinhamento perfeito entre exigências acadêmicas (formalidade) e necessidades práticas (agilidade controlada).
- Negativas: Aumento da burocracia para mudanças radicais (embora necessário); necessidade de ferramentas auxiliares (scripts de hash/validation) para manter a integridade; curva de aprendizado para novos membros entenderem a diferença entre "alterar plano" e "emendar constituição".
- Neutras: A Constituição torna-se o ponto focal de auditorias externas e avaliações do Prof. Dr. Nivaldo Carleto, simplificando a demonstração de maturidade de gestão.

## Trade-offs Declarados

| Aspecto                              | Ganho                                   | Perda/Risco                                   | Mitigação                                                                    |
| ------------------------------------ | --------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------ |
| Supremacia Absoluta                  | Segurança jurídica e técnica máxima | Rigidez percebida                             | Cláusulas de exceção claras (Bypass Protocol) já previstas nos Arts. 3 e 7 |
| Restauração Integral vs. Patch     | Coerência total pós-recuperação     | Perda de nuances de edições intermediárias | Backups forenses detalhados preservam histórico completo                      |
| Separação Hierarquia Projeto/Forja | Clareza epistemológica                 | Complexidade cognitiva inicial                | Diagramas de fluxo e exemplos práticos no OKB v3.3+                           |

## Sobreposição de Decisões

| ADR Sobreposta | Natureza | Motivo                                                                                                                                                                                                                                                   | Domínio PMBOK 7ª | Data       |
| -------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ---------- |
| —             | —       | Esta ADR não sobrepõe outra diretamente; ela **consolida e institucionaliza** os princípios dispersos nas ADRs 001, 005, 008 e 011, elevando-os a status constitucional. Reforça a ADR-005 ao colocar a Constituição acima do TAP congelado. | Integração       | 29/10/2026 |

> **Nota Crítica:** Embora não haja sobreposição direta de texto, esta ADR resolve implicitamente contradições potenciais entre a liberdade de ação dos agentes (ADR-006/011) e as restrições éticas/legais (TAP/Constituição), deixando claro que a restrição constitucional vence a eficiência agêntica.

## kill_switch

Ativado automaticamente se:

1. For detectada alteração manual ou automática na `constitution.md` sem o devido commit de Emenda aprovado pelo CCB.
2. O hash SHA-256 do conteúdo normativo divergir do valor registrado na última co-assinatura válida, sem justificativa de emenda pendente.
3. Um agente tentar executar uma instrução presente em um Input Canônico que contradiga explicitamente um artigo da Constituição (ex.: pedir para ignorar LGPD).
4. Falha na verificação de integridade durante o boot do circuito SDD.

Ao disparar, o sistema entra em estado `BLOCKED_CONSTITUTIONAL_INTEGRITY`, exigindo intervenção humana imediata para restauração ou validação da emenda.

## Governança

- **Custódia:** GP Leonardo (Guardião da Constituição).
- **Validação Técnica:** Script `validate_constitution_integrity.py` roda em CI e pré-commit.
- **Auditoria:** `project-auditor` gera relatório mensal de conformidade constitucional.
- **Sucessão:** Em caso de indisponibilidade do Guardião, a posse da chave privada de assinatura ou acesso ao repositório protegido determina a legitimidade das emendas futuras. Atualmente, apenas o CCB Único possui essa prerrogativa.
