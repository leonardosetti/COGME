# Auditoria ponytail (FOSS) — COGME

Data: 2026-11-06
Escopo: src/ (runtime), tests/, config de build/deploy, scripts de segurança.
Não lidos: docs/, .archive/, .ai/, .opencode/, scripts/ fora do escopo de segurança, graphify-out/.

## O que o repo faz

COGME é conversor cambial FOSS (USD/EUR → BRL), projeto acadêmico da Fatec Taquaritinga. Backend FastAPI em /v1 com /rates/{currency}, /simulate, /invoice, /health. Cotações de Frankfurter (primária) e PTAX/BCB (reserva), cache em PostgreSQL. Cálculo em Decimal exato, spread e IOF informados pelo usuário (nada embutido). Invoice PDF via WeasyPrint. Camada front Jinja2 + proxy nginx em docker-compose. LGPD primária: nada de PII persistido nem em log. CPU-only por regra de governança.

Carga assumida: usuário único acadêmico ou concorrência pequena atrás do proxy em 127.0.0.1:8080. Não é serviço público de alto tráfego.

## Resultados

Suite de testes: verde. 1402 passou, 13 (Postgres real) ignoradas por falta de banco, 0 falhas, em 12 s.

Sem bugs, buracos de segurança ou perda de dados na carga assumida.

## Deve consertar

1. Frontend duplica formatação do backend; date_br/datetime_br não fazem nada
   src/frontend/app.py:L47-73
   app.py reimplementa brl, percent_br, rate_br, date_br, datetime_br que já existem em
   src/backend/services/invoice_service.py:L93-164. date_br e datetime_br só devolvem str(value) —
   mostram data ISO crua, não dd/mm/aaaa. Duplicação que deve ficar sincronizada e filtros quebrados.
   Conserto: apague os filtros duplicados do front (o caminho de PDF do back já renderiza invoice.html com os
   filtros corretos; as rotas do front usam money() em JS, não esses filtros Jinja).
   Se pular: código morto e divergente persiste; um template futuro ligado a date_br mostra data ISO ao usuário brasileiro.

2. Caminhos de template/estático do front dependem do diretório de trabalho
   src/frontend/app.py:L19,23
   StaticFiles(directory="src/frontend/static") e FileSystemLoader("src/frontend/templates") são relativos ao cwd.
   O back resolve de __file__ (invoice_service.py:L30) e funciona de qualquer cwd. O front não.
   Conserto: resolva de __file__, tipo Path(__file__).resolve().parent / "static", igual ao back.
   Se pular: o front só funciona de um cwd; qualquer outro ponto de entrada quebra assets/templates silenciosamente.

## Pode consertar (nice to have)

3. percent_br diverge entre camadas
   src/frontend/app.py:L54-58 vs src/backend/services/invoice_service.py:L129-140
   Back trim zeros depois de 2 casas (0,0125 %); front mostra sempre 4 (2,0000 %). Mesmo percentual renderiza diferente na página e no PDF.
   Conserto: alinhe o front ao back ou remova o filtro duplicado (com o conserto 1).

4. Teto do pool de conexões não documentado para a carga assumida
   src/backend/models/database.py:L35-37
   Pool default asyncpg = 5 conexões; POOL_TIMEOUT_SECONDS = 0.25. Mais que ~5 requisições simultâneas com cache vencido (batem no DB) serializam ou estouram. Na carga assumida (TTL 1h, pouco usuário) nunca dispara. Só limita escala futura.
   Conserto: documente o limite no spec/ADR e aumente pool_size se o app for exposto a mais usuários.

## Veredito

Saudável. Conserte 1 e 2 primeiro.

## Lean

- ~30 linhas, 0 dependências possíveis.

## Não verificado

docs/ (rascunhos, ADRs, auditorias, planos), .archive/, .ai/, .opencode/agents/, scripts/ fora do escopo de segurança, graphify-out/, migrations alembic além da migração única. São documentação/orquestração, não código de runtime. O .env real não foi lido (arquivo de segredo protegido); usei apenas .env.example para nomes de variáveis.
