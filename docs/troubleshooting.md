## Seção de Troubleshooting

### 5 Problemas Comuns
1. **Erro de Configuração do Ambiente**:
   - Verifique variáveis de ambiente com `echo $PATH`
   - Reinstale dependências com `npm install`

2. **Falha na Conexão com MCP**:
   - Teste com `ping mcp-server`
   - Verifique firewall e permissões

3. **Erro de Tokenização**:
   - Valide tokens com `token validate`
   - Atualize modelo com `model update`

4. **Conflito de Versão**:
   - Compare `git log` com documentação
   - Use `git checkout v1.2.3`

5. **Falha na Calibração RAG/DAG**:
   - Verifique configurações em `config/rag.yaml`
   - Execute `calibrate --type rag`

### Configurações Específicas por Plataforma

**Linux**:
~~~bash
# Instalação de Dependências
sudo apt-get install -y build-essential libssl-dev

# Variáveis de Ambiente
export MCP_SERVER="mcp.example.com"
~~~

**Windows**:
~~~powershell
# Instalação de Dependências
Install-WindowsFeature -Name Web-Server

# Variáveis de Ambiente
[Environment]::SetEnvironmentVariable("MCP_SERVER", "mcp.example.com", [EnvironmentVariableTarget]::Machine)
~~~

**macOS**:
~~~bash
# Instalação de Dependências
brew install openssl

# Variáveis de Ambiente
export MCP_SERVER="mcp.example.com"
~~~

### Exemplos de Calibração RAG/DAG (Português)

**RAG Calibration**:
~~~yaml
pipeline:
  - name: "rag_pipeline"
    steps:
      - type: "retrieve"
        config:
          k: 5
      - type: "rank"
        config:
          model: "bm25"
~~~

**DAG Calibration**:
~~~yaml
graph:
  nodes:
    - id: "data_source"
      type: "source"
    - id: "process"
      type: "transform"
  edges:
    - from: "data_source"
      to: "process"
~~~