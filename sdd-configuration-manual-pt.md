### Manual de Configuração SDD - Versão 2.0

#### 1. Definições de Papéis de Agentes
```mermaid
hierarchyDiagram
  root ["Sistema SDD"]
  root --> GerenteSDD
  root --> Configurador
  root --> ModeloAgent
  Configurador --> OpencodeAgent
  Configurador --> RAGAgent
  ModeloAgent --> OpenClaude
  ModeloAgent --> ChatGPT
  ModeloAgent --> Claude
``` 

#### 2. Configuração Opencode
```yaml
opencode:
  session:
    id: ses_12345
    directory: /lab/FATEC/202602/ger_proj/COGME
  worktree: default
  model: local/qwen30b-moe
``` 

#### 3. Comandos de Configuração por Modelo
**OpenClaude**: `tools.opencode.models({query: 'OpenClaude'})`
**ChatGPT**: `tools.opencode.models({query: 'ChatGPT'})`
**Claude**: `tools.opencode.models({query: 'Claude'})`

#### 4. Fluxos de Trabalho por Plataforma
```bash
# Linux
sudo apt install opencode-cli
# Windows
choco install opencode
# macOS
brew install opencode
``` 

#### 5. Modelos de Calibração RAG/DAG
```json
{
  "prompt_template": "Contexto: {{context}}\n\nQuestão: {{question}}\n\nResposta: ",
  "parameters": {
    "max_tokens": 2048,
    "temperature": 0.7
  }
}
``` 

#### 6. Checklist de Criação de Artefatos
- [ ] Validar configuração YAML
- [ ] Testar modelos com dados de exemplo
- [ ] Gerar diagramas Mermaid atualizados
- [ ] Documentar fluxos de trabalho

#### 7. Protocolos de Integração Prime-Nexus-Ultimate
```python
import prime_nexus
client = prime_nexus.Client(api_key="YOUR_KEY")
response = client.query("Configuração SDD")
```