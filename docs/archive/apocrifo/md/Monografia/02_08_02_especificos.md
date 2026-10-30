# 2.8.2 Específicos

[Planejamento e índice](../../../PLANEJAMENTO.md)

> **Nota de conferência:** As situações de encerramento e mitigação são declarações da monografia. A afirmação de restrição à comercialização por licenciamento aberto deve ser revista conforme a licença efetivamente adotada; não foi validada nesta organização documental. A aprovação da stack também precisa ser conciliada com a implementação antes de encerrar esse risco.

Como riscos específicos do COGME, destacam-se: a indefinição da stack tecnológica, originalmente o risco mais severo do projeto, com probabilidade estimada em 80% e potencial de bloqueio integral da fase de desenvolvimento, encerrado pela formalização do ADR-002; a dessincronização entre a EAP e o quadro Kanban, com probabilidade de 60%, mitigada por mapeamento um para um entre pacotes de trabalho e cartões; a confusão conceitual entre TAP, EAP e ciclos PDCA, endereçada pelo ADR-004; o não atendimento das metas de desempenho pela inferência local de modelos de linguagem, mitigado pela existência de modelo alternativo de menor porte previamente validado; a dependência crítica de APIs externas gratuitas de cotação cambial, cuja indisponibilidade compromete a função central do produto, mitigada pela adoção da API do Banco Central do Brasil como fonte oficial e pelo cache local de cotações; a desatualização das tarifas e dos spreads dos provedores de pagamento internacional, nem sempre expostos por interface pública, endereçada por base parametrizável com data de vigência e revisão manual periódica; a divergência entre a cotação PTAX e a taxa efetivamente praticada pelo provedor, tratada pela exibição explícita da fonte e da data de cada cotação; e a exigência de licenciamento integralmente aberto do produto final, que restringe sua comercialização futura. Registre-se ainda o risco de que o orientador venha a exigir cronograma em formato tradicional de Gantt, considerado mitigado pela possibilidade de derivá-lo a partir do quadro Kanban.

## Fonte documental

- [Modelo-Projeto-COGME.docx](../../docx/Monografia/Modelo-Projeto-COGME.docx), seção 2.8.2.

## Incrementos necessários ao material

Proposta de desenvolvimento para este tema; os itens abaixo ainda precisam ser elaborados ou verificados e não representam execução ou aprovação.

Os riscos específicos decorrem da dependência de cotações e tarifas, da precisão dos cálculos e do desenvolvimento assistido por IA.

- [ ] Detalhar tratamento de API indisponível, limite de requisições, cotação de referência antiga, tarifa desatualizada e diferenças entre estimativa e valor praticado pelo provedor.
- [ ] Planejar cenários de teste e resposta para falhas de cálculo e código gerado por IA; definir como detectar e comunicar cada problema.
- [ ] Reavaliar riscos declarados encerrados apenas por existência de ADR e revisar premissas de licenciamento com base nas dependências efetivamente escolhidas.

**Entrega esperada:** Registro dos riscos do domínio e da solução, com ações proporcionais ao MVP.
