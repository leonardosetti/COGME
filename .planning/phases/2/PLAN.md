# PLAN — Fase 2: Pré-produção CR-009 (17 BLOQ → 15 BLOQ ativos)

## Fase
Número: 2 | Slug: `pre-producao-cr-009` | Status: planejado

## Goal
Deixar a implementação liberada para produção (pré-produção CR-009): fechar **15 BLOQ** (B-01 a B-15; B-16 e B-17 já corrigidos em main) e os **12 ALTO** (H-01 a H-12), de acordo com a auditoria `docs/auditorias/aud-cr-009-2026-11-17-pre-producao.md` v1.1.0 (veredito REPROVADO).

## Contexto
- Fase 1 (saneamento compliance) CONCLUÍDA e pushada (a1e7196, ce7a513, ab90840, fce28ed). Working tree limpo.
- Auditoria CR-009 v1.1.0: 17 BLOQ → 15 ativos (B-16/B-17 já em main), 12 ALTO, 6 MÉDIO, 10 possíveis, 6 drifts.
- Nenhum BLOQ pode virar débito pós-produção (regras da auditoria).
- Cobertura de testes: 72% (hook 70%).
- Pipeline Auditoria de Compliance: VERDE.
- Suíte local: 1270 passed, 0 failed. Nenhum teste cobre os fluxos de segurança da auditoria.
- TA-0061..TA-0065 (specs/integridade) ficam em fase separada (Fase 1.5), não entram na Fase 2 de código.

## Escopo — Fase 2

### BLOQ (bloqueiam produção — todos entram na Fase 2)

| ID | Item | Correção resumida | Critérios de aceite |
|---|---|---|---|
| B-01 | PII em log de cadastro | remover identifier/name do log; logar só user_id + kind | caplog sucesso/conflito/erro; nenhum valor de entrada no log |
| B-02 | Hash identidade não-HMAC / sem sal | HMAC-SHA-256(pepper, "kind:value"); internal_username_hash HMAC uuid4 | vetor HMAC conhecido; hash não varia com identificador |
| B-03 | PBKDF2; Argon2id inativo | PasswordHasher(type=Type.ID); persistir encoded hash; rehash legado | prefixo `$argon2id$`; login funciona; rehash PBKDF2; startup falha sem argon2-cffi |
| B-04 | Colisão numeração invoice | unique (issuer_tax_id_digits, invoice_number); remover uq global | 2 usuários CNPJ distintos mesma mês → ambas 001; sem 500 |
| B-05 | Cross-owner client_id/simulation_id | carregar por (id, owner_user_id); 404 se ausente | usuário B não acessa cliente/simulação de A; snapshot do banco |
| B-06 | CSRF HttpOnly / logout isento | cookie sem HttpOnly; JS envia X-CSRF-Token; logout sem header → 403 | sem header 403, com header 201; logout 403 sem header |
| B-07 | Reset senha não entrega / link 404 | SMTP fake + template email; GET /auth/reset?token=; confirm troca senha | request 202; token no SMTP; segundo uso falha; fallback dev 0600 |
| B-08 | Exclusão corrompe unicidade / não apaga | anonimizar compatível com índices parciais; aposentar identificadores | 2 exclusões distintas ok; mesma 2x sem colisão; nenhum ID antigo autentica |
| B-09 | Reativação dormente impossível | POST /v1/account/reactivate público + rate limit login | dormente + credenciais → 200 + sessão; erradas → 401 |
| B-10 | Sessão não revalida status | juntar users.status na validação; revogar ao dormência | sessão + usuário dormant/deleted → 401/403 |
| B-11 | Alembic > varchar(32) | renomear revisão 0009 (≤32 chars); teste len(revision) | alembic upgrade head do zero e existente; downgrade |
| B-12 | Secure cookie sobre HTTP | COGME_ENV=development permite Secure=false só localhost; TLS prod | login via http://localhost persiste |
| B-13 | Clientes internacionais impossíveis | tax_id_digits VARCHAR(32) NULLABLE; tax_id_type foreign | cliente US sem tax_id → 200; país inválido → 400; email/phone devolvidos |
| B-14 | Rate limits ausentes fora auth | limites SPEC-025 §6.4 nas rotas não-auth | rajada acima do limite → 429 em simulate/invoice/invoices/clients/provider/account |
| B-15 | Rate limit vê IP proxy | uvicorn --proxy-headers --forwarded-allow-ips | 2 origens distintas não compartilham contador |

### ALTO (H-01 a H-12 — recomendado incluir na Fase 2)

| ID | Item | Critérios de aceite resumido |
|---|---|---|
| H-01 | Sliding expiration | atualiza expires_at + cookie; não só last_seen_at |
| H-02 | IntegrityError → 500 | capturar e retornar 409 conflict |
| H-03 | CNPJ por usuário / provider_cnpjs | CNPJ duplicado → 409; checksum; provider_cnpjs |
| H-04 | Dados bancários texto simples | criptografar antes de produção |
| H-05 | CSP / HSTS / Permissions-Policy | adicionar headers; HSTS só TLS |
| H-06 | Google Fonts remoto | remover; pilha local |
| H-07 | Navbar deslogada / rotas ausentes | navbar logada; rotas /dashboard, /perfil, /clientes, /sobre |
| H-08 | #sobre inline / HTML malformado | extrair para /sobre; HTML válido |
| H-09 | Snapshot do payload | derivar do banco; rejeitar divergência |
| H-10 | Aliases fictícios | aliases reais mascarados ou endpoint removido |
| H-11 | /me email=None para CNPJ | devolve email/telefone/identificadores reais |
| H-12 | Scripts inline | externalizar static/js/ |

### Fora de escopo (explicitamente excluídos da Fase 2)
- MÉDIO M-01..M-06 (M-01 = duplicata B-16; M-02 = duplicata B-08; M-03 duplo opt-in; M-04 schema RegisterRequest; M-05 total simulações; M-06 comentário Argon2).
- Possíveis P-07..P-10.
- Drifts SD-01..SD-06 (cobertos por B-02/B-03 ou exigência específica de BLOQ).
- Migração rate limit → Redis (P-09, mitigação documentada).
- Gates não-código: G1 aprovação CCB, G2 ratificação SPEC-024/025/026, G5 parecer LGPD, G7 aceitação visual, G8 TLS produção.
- TA-0061..TA-0065 (specs/integridade) → fase separada (Fase 1.5).

## Critérios de aceite globais (checkáveis)

- [ ] Nenhum BLOQ restante (B-01 a B-15) com evidência de reprodução.
- [ ] Cada BLOQ coberto por pelo menos um teste de aceite novo no suíte local.
- [ ] ALTO H-01 a H-12 implementados (ou explícita exclusão com registro de risco).
- [ ] `alembic upgrade head` do zero e em banco existente (B-11).
- [ ] `python3 -m pytest tests/unit` verde no CI (hook 70%).
- [ ] Pipeline Auditoria de Compliance verde após as mudanças.
- [ ] Relatório de auditoria CR-009 atualizado (veredito: APROVADO para pré-produção ou RESIDUAL documentado).

## Riscos
1. **Suíte verde não valida segurança:** nenhum teste cobre os fluxos da auditoria. Cada BLOQ precisa de teste de aceite novo, senão o gate é ilusório.
2. **9 failed / 18 errors locais** na execução da auditoria: `test_openapi` (4 rotas esperadas vs API maior), `test_api_contract` (500 sem vazamento), seletores frontend, lifespan, auth sem `COGME_TEST_DATABASE_URL`. `test_openapi` e `test_api_contract` são reais e devem ser ajustados na Fase 2.
3. **G6 falha:** `alembic upgrade head` falha (bloqueia deploy). B-11 resolve, mas precisa ser verificado.
4. **G8 só HTTP:** cookie `Secure` quebra login fora localhost (B-12 depende de TLS ou exceção dev).
5. **Rate limit em memória (P-09):** não compartilhado entre workers/restart. Mitigação documentada; Redis fica para onda seguinte.
6. **TA-0061..TA-0065** não entram na Fase 2; se a equipe quiser, devem ser uma fase separada (especs/integridade).

## Próximo comando
`/gsd-execute-phase 2` — executar as tarefas B-01 a B-15 e H-01 a H-12 deste PLAN.md, depois atualizar o relatório de auditoria CR-009.
