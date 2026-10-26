# Technical Manual: SDD Configuration

## 1. Agent Roles & Hierarchy
```
Root (Prime-Nexus-Ultimate)
├── Orchestrator (Session Manager)
├── RAG-Calibrator (Data Pipeline)
├── DAG-Manager (Task Scheduler)
└── Artifact-Handler (Model Registry)
```

## 2. Opencode Configuration Guidelines
- Use `tools.opencode.models()` to select optimal variants
- Configure sessions with `tools.opencode.session_move()`
- Set `MCP_SERVER=local` for local model execution

## 3. Alternative Models
```bash
# OpenClaude alternatives
tools.opencode.models(query='claude')

# ChatGPT alternatives
tools.opencode.models(query='gpt-4')
```

## 4. Multi-Platform Adaptability
- Use `tools.shell(command='cross-platform-command')`
- Implement OS-specific environment variables
- Test with `tools.grep(pattern='platform', include='*.py')`

## 5. Calibration Prompts
```yaml
# RAG Configuration
rag_prompt: 'Retrieve relevant documents from {{context}}'

# DAG Configuration
dag_prompt: 'Distribute tasks across {{nodes}} with priority {{priority}}'
```

## 6. Artifact Creation
1. Train models with `tools.shell(command='train_model.sh')`
2. Package with `tools.write(path='artifacts/model.tar.gz', content=...)`
3. Register via `tools.opencode.models(register=True)`

## 7. Prime-Nexus-Ultimate Protocol
- Use `tools.webfetch(url='https://prime-nexus-ultimate/api')`
- Implement JSON-RPC for inter-agent communication
- Monitor with `tools.grep(pattern='NexusError', path='logs/')`
