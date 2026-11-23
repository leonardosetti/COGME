---
id: docs-analise-parecer-juridico-cnpj-dado-pessoal
title: Parecer Jurídico — CNPJ como Dado Pessoal (LGPD Art. 5º II)
type: relatorio
version: 1.0.0
status: ativo
owner: agent-compliance-governance
derived-from:
- docs/analise/parecer-juridico-lgpd-gdpr-cogme.md
- docs/decisoes/ccb-lgpd-decisoes.md (DEC-01/02)
- docs/decisoes/ccb-auditoria-CR-002.md (AI-01)
- LGPD Lei 13.709/2018 (Art. 5º II, 11)
- GDPR Regulamento (UE) 2016/679 (Considerando 26, Art. 4º.1)
last-revised: '2026-11-16'
lgpd-class: n/a
tags:
- juridico
- lgpd
- cnpj
- dado-pessoal
- compliance
- ai-01
---

# Parecer Jurídico — CNPJ como Dado Pessoal (LGPD Art. 5º II)

## 1. Objeto

Parecer sobre se o **CNPJ (Cadastro Nacional da Pessoa Jurídica)** constitui dado pessoal sujeito à LGPD (Lei 13.709/2018) quando capaz de identificar pessoa natural, ou indiretamente, em combinação com outras informações.

Suscitado pelo **Action Item AI-01** da ratificação Gate 1 CR-002 (docs/decisoes/ccb-auditoria-CR-002.md:64). Prazo: 2026-11-30.

## 2. Contexto Fático

No COGME, o CNPJ é coletado em:

- Cadastro da **prestadora** (SPEC-018): `provider_profiles.cnpj`, obrigatório quando `category = 'legal_entity'`.
- **Alias de login** (SPEC-017): rotacionado quando o CNPJ da prestadora muda (mesma transação).

O CNPJ identifica a **pessoa jurídica** (empresa), e não diretamente uma pessoa natural. Entretanto, para MEI (Microempreendedor Individual) e pequenas sociedades, o CNPJ está vinculado ao CPF do titular/responsável, permitindo a identificação da pessoa natural.

## 3. Fundamento Legal

### LGPD

**Art. 5º II:** dado pessoal é "informação relacionada a pessoa natural identificada ou identificável".

Pessoa natural é identificável quando é possível, por meios diretos ou indiretos, identificá-la. O CNPJ de uma empresa unipessoal/MEI permite, por consulta a fontes públicas (Receita Federal), identificar o titular (CPF). Logo, nesses casos, o CNPJ **indiretoramente identifica pessoa natural** e é dado pessoal.

**Art. 11:** tratamento de dados pessoais para fins exclusivamente particulares de uma pessoa natural não se aplica ao COGME (atividade profissional/econômica — Art. 4º I não se aplica).

### GDPR

**Considerando 26:** dados pseudonimizados que permitam a reidentificação continuam sendo dados pessoais.

O CNPJ, combinado com outras informações (nome fantasia, endereço, sócios na Receita), permite reidentificar a pessoa natural por trás da empresa. Assim, está coberto pelo GDPR quando houver conexão com o Espaço Econômico Europeu/Reino Unido (oferta/monitoramento).

## 4. Conclusão do Pareer

| Situação | CNPJ é dado pessoal? | Fundamento |
|----------|---------------------|------------|
| CNPJ de empresa com sócios múltiplos, sem vinculação direta a CPF único | Não é dado pessoal direto | Identifica pessoa jurídica |
| CNPJ de MEI/empresa unipessoal vinculado a CPF do titular | **Sim** (indireto) | Identifica pessoa natural via consulta pública |
| CNPJ combinado com nome/endereço/sócios | **Sim** (indireto) | Reidentificação possível |

**Decisão:** O COGME trata o CNPJ como **dado pessoal em todas as situações** (posição mais restritiva e segura), aplicando:

- Minimização (coleta só quando necessário — SPEC-018, SPEC-021).
- Base legal Art. 7º V (execução de contrato) para CNPJ da prestadora (DEC-01/02).
- Sem PII em logs (CP-2, SPEC-015).
- Rotação de alias HMAC quando o CNPJ muda (SPEC-017, SPEC-018).
- Anonimização em caso de exclusão de conta (SPEC-022 §3.5).

## 5. Impacto no COGME

- Nenhuma mudança de código requerida: o CNPJ já é tratado como dado sensível (campos NULLable, sem logs, cifragem de dados bancários associados).
- Documentação de treinamento da equipe sobre o tratamento do CNPJ como dado pessoal.
- Revisão anual do presente parecer (alinhada à rotação anual do pepper HMAC, SPEC-022 §3.6).

## 6. Assinatura

| Campo | Valor |
|-------|-------|
| Parecer | AI-01 — CNPJ como dado pessoal |
| Responsável | agent-compliance-governance |
| Data | 2026-11-16 |
| Status | Concluído (não bloqueia Onda 1) |
