# Verificação Final da Configuração SDD

## 1. Validação de Funções de Agentes
- Executar `agent-cli validate-role --role <nome_rol>` para verificar permissões e configurações de cada agente
- Verificar logs de autenticação em `/var/log/agent/auth.log` para erros de atribuição de funções
- Testar execução de tarefas básicas com `agent-cli run-task --task <nome_tarefa> --agent <id>`

## 2. Verificação de Integração de Modelos
- Executar `model-api check-integration --model <id_modelo>` para validar conexão com API de modelo
- Verificar arquivo de configuração `/etc/sdd/model-config.json` para endpoints corretos
- Executar teste de inferência com `model-api test-inference --model <id_modelo> --sample <dados_entrada>`

## 3. Verificação de Fluxo de Trabalho DAG
- Visualizar estrutura DAG com `dag-engine visualize --workflow <id_fluxo>`
- Executar validação de dependências com `dag-engine validate --workflow <id_fluxo>`
- Verificar registros de execução em `/var/log/dag/execution.log` para falhas

## 4. Testes de Comunicação Prime-Nexus-Ultimate
- Executar `comm-tester ping --system Prime --timeout 30s` para verificação de latência
- Verificar integridade de mensagens com `comm-tester verify-pipeline --source Prime --target Ultimate` 
- Analisar logs de comunicação em `/var/log/prime-nexus/comm.log` para erros de sequenciamento

> **Nota:** Substituir `<parametros>` pelos valores específicos da instalação antes da execução.