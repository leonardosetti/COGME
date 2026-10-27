## ADR-006: SDD Intelligence Module

**Status:** Draft
**CCB Approval:** 2026-10-26
**Date:** 2026-10-26

**Constitutional Compliance:** Art. 4.3 - FOSS-first policy adherence

### Problem
Implementing SDD intelligence capabilities

### Decision
Qwen30b-moe with custom routing

### Alternatives Considered
- Llama3
- Mistral

### Impacted Components
- Agent router
- Task dispatcher

### Rollback Plan
Revert to basic routing