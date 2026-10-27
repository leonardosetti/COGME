# 3.1 Tecnologias

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** A tabela registra a stack declarada na monografia, incluindo sua alegação de aprovação por ADR-002. A correspondência com o código atual e a aprovação efetiva não foram verificadas nesta extração. A afirmação de conformidade FOSS de todo o conjunto requer auditoria individual de licenças; planos gratuitos e serviços hospedados não comprovam essa conformidade.

Em atendimento à premissa P2, todo o ciclo de vida do projeto — gerenciamento, modelagem, desenvolvimento, testes, documentação, integração contínua e hospedagem — é conduzido exclusivamente com ferramentas gratuitas e de código aberto, com licenças aprovadas pela Open Source Initiative (MIT, Apache 2.0, BSD e GPL). A definição da stack, originalmente o risco mais severo do projeto, foi formalizada pelo registro de decisão arquitetural ADR-002, que estabeleceu a arquitetura da aplicação e o ambiente de desenvolvimento assistido por IA. O Quadro 16 sintetiza a stack aprovada.

**Quadro 16 — Stack tecnológica aprovada**

| Camada | Tecnologia | Função no COGME |
| --- | --- | --- |
| Backend | Python 3.12 + FastAPI | Lógica de negócio (câmbio, spread, IOF) e API da aplicação |
| Banco de dados | SQLite 3 | Persistência e cache local de cotações cambiais |
| Frontend | HTML + HTMX + Tailwind CSS | Interface web responsiva e simulações interativas |
| Geração de documentos | WeasyPrint | Emissão de invoices em formato PDF |
| Testes | pytest + coverage.py | Testes unitários, de integração e medição de cobertura |
| Versionamento e CI/CD | Git + GitHub Actions | Repositório, pipeline de lint e testes, e implantação |
| Gestão do projeto | GitHub Projects | Backlog, quadro Kanban e métricas de fluxo (fonte única de verdade) |
| Inferência local de IA | llama.cpp (Vulkan e AVX-512) | Servidor local de modelos de linguagem para apoio ao SDD |
| Modelos de linguagem | Qwen 32B Instruct Q4_K_M (principal) e Qwen 14B Instruct Q4_K_M (rápido) | Geração e revisão assistida de artefatos e de código |
| Interface de desenvolvimento | OpenCode | Ambiente de desenvolvimento integrado ao servidor local de IA |
| Base de conhecimento | Obsidian + repositório Git | Organização das especificações, prompts e decisões arquiteturais |
| Sistema operacional | Arch Linux (kernel Zen) | Ambiente de desenvolvimento e homologação local |
| Fonte oficial de câmbio | API Olinda — Banco Central do Brasil (PTAX) | Cotação oficial de referência para USD e EUR e base do comparativo de taxas |

Fonte: elaborado pelos autores (2026).

A abordagem de Specification-Driven Development (SDD) adotada no projeto organiza-se em três camadas ortogonais, que evoluem de forma independente. A camada de infraestrutura de inferência compreende o servidor local de modelos de linguagem, executado com aceleração por GPU integrada e fallback em CPU, exposto por interface compatível com o padrão OpenAI. A camada de personas e contexto define os papéis especializados de programador, revisor, testador e gerente, todos compartilhando o mesmo modelo base — a especialização ocorre por prompt, e não por modelo, o que elimina consumo adicional de memória e a necessidade de recarregamento. A camada de metodologia reúne as especificações imutáveis, os artefatos de transição entre fases e os fluxos de automação, todos versionados no repositório do projeto, o que assegura a rastreabilidade exigida pela premissa P3 e pelo critério de inovação controlada do TAP. Essa arquitetura viabiliza a utilização de IA generativa a custo marginal de energia, sem dependência de serviços pagos de nuvem.

## Fonte documental

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 3.1.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

O inventário tecnológico precisa refletir o código realmente utilizado. A tabela da monografia só pode ser apresentada como implementação após comparação com arquivos de configuração e dependências.

- [ ] Conferir a stack declarada em Python/FastAPI/SQLite com o repositório atual e documentar divergências ou decisões de migração.
- [ ] Registrar componente, versão, função, licença, justificativa, alternativa considerada e dependências externas; distinguir software livre de serviço gratuito.
- [ ] Descrever arquitetura, fluxo dos dados, configuração do ambiente e procedimento de implantação sem expor credenciais.

**Entrega esperada:** Tabela tecnológica verificada, diagrama da arquitetura efetiva e instruções reproduzíveis de execução.
