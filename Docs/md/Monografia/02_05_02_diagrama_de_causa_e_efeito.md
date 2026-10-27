# 2.5.2 Diagrama de causa e efeito

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** As causas abaixo são hipóteses descritas na monografia. O diagrama por ocorrência, com evidências e ações verificadas, permanece pendente. As declarações sobre resolução por ADR e validação do ambiente são da fonte, não resultados de uma nova verificação.

Complementarmente ao PDCA, o projeto aplica o Diagrama de Causa e Efeito (Diagrama de Ishikawa) segundo o modelo dos 6M — Método, Máquina, Mão de obra, Material, Medida e Meio ambiente —, para investigação sistemática das causas-raiz de não conformidades identificadas durante os testes e a homologação. A aplicação do modelo ao contexto do COGME identifica, como causas potenciais recorrentes: em Método, a imaturidade da abordagem SDD e a ausência de linha de base para as métricas de fluxo; em Máquina, os limites de desempenho da inferência local de modelos de linguagem e a instabilidade das APIs externas gratuitas; em Mão de obra, a disponibilidade restrita de 20 horas semanais por integrante e a acumulação de papéis; em Material, a indefinição inicial da stack tecnológica, posteriormente resolvida pelo ADR-002; em Medida, a ausência de linha de base de tempo de ciclo e vazão, endereçada por período de calibração entre 23 de setembro e 3 de outubro de 2026; e em Meio ambiente, as restrições do calendário letivo noturno. O diagrama formal, com o detalhamento das espinhas por ocorrência, integra o Plano de Qualidade.

## Fonte documental

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.5.2.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

O diagrama organiza hipóteses de causa; a investigação deve produzir evidências para confirmar ou descartar cada hipótese. O efeito precisa ser específico, como “resultado diferente do cálculo de referência”.

- [ ] Construir o diagrama 6M para uma ocorrência selecionada e registrar data, contexto e dados usados para reproduzi-la.
- [ ] Relacionar hipóteses do COGME: regra ambígua, arredondamento, cotação antiga, tarifa desatualizada, ambiente e falha na revisão, nas categorias adequadas.
- [ ] Ligar cada hipótese ao teste de verificação, resultado, ação corretiva e PDCA correspondente.

**Entrega esperada:** Diagrama e tabela de investigação que distingam causas possíveis de causas verificadas.

**Apoio metodológico:** [ASQ — Diagrama de causa e efeito](https://asq.org/quality-resources/fishbone).
