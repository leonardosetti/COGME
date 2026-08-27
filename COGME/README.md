# COGME — Conversor de Ganhos em Moeda Estrangeira

MVP inicial do projeto descrito no Termo de Abertura do Projeto. Esta etapa entrega a experiência web de login, dashboard, simulação USD/EUR, encargos simulados, cotação PTAX do Banco Central com fallback e geração de invoice via impressão do navegador (Salvar como PDF).

## Escopo desta etapa

- Middleware protegendo as rotas de dashboard, simulações, invoices e cotação.
- Sessão em cookie httpOnly, assinado com HMAC-SHA256 e expiração de 8 horas.
- Senha validada com PBKDF2-SHA256, 120.000 iterações. Nenhuma senha é armazenada em texto puro.
- Credenciais e segredo configuráveis por variáveis de ambiente.
- Simulações salvas no MySQL, isoladas por usuário autenticado.
- Invoice exportável por window.print(); no diálogo de impressão, selecione “Salvar como PDF”.

## Executar localmente

Requer Node.js 18.17 ou superior.

    npm install
    Copy-Item .env.example .env.local
    npm run db:setup
    npm run dev

Abra http://localhost:3000. O ambiente de demonstração usa admin@cogme.local e COGME2026!. Antes de qualquer publicação, altere AUTH_SECRET, ADMIN_EMAIL e ADMIN_PASSWORD_HASH.

## Banco de dados MySQL

O backend usa MySQL para persistir as simulações e invoices exibidas na aplicação. Por padrão, a conexão usa localhost:3306, usuário root e banco cogme. Defina MYSQL_PASSWORD no .env.local e execute npm run db:setup uma vez para criar o banco e a tabela. A senha do banco nunca deve ser colocada no código ou commitada.

## Notícias econômicas e job de atualização

O dashboard possui quatro cards reservados para CNN Brasil, UOL Economia, G1 Economia e Record/R7 Economia. O job acessa as páginas oficiais de Economia, extrai os metadados mais recentes e envia somente título, descrição, data e URL para o modelo configurado no OpenRouter. A resposta da LLM é validada contra as URLs coletadas antes de ser gravada no cache.

Configure no .env.local:

    OPENROUTER_API_KEY=sua_chave_no_servidor
    OPENROUTER_MODEL=nvidia/nemotron-3.5-lightning:free
    OPENROUTER_FALLBACK_API_KEY=sua_chave_de_reserva
    OPENROUTER_FALLBACK_MODEL=dots-studio/dots-3-note-preview:free
    OPENROUTER_RESERVE_API_KEY=sua_chave_de_ultima_reserva
    OPENROUTER_RESERVE_MODEL=poolside/laguna-s-2.1:free
    NEWS_JOB_SECRET=um_segredo_longo
    NEWS_JOB_URL=http://localhost:3000

Com a aplicação em execução, rode npm run news:update. Em produção, agende esse comando em um scheduler externo (cron, Task Scheduler ou o scheduler da hospedagem) a cada 4 horas. O dashboard também verifica o cache ao ser aberto e, se ele estiver vencido, dispara a coleta e a chamada da LLM; com a página aberta, faz nova verificação a cada 4 horas. A rota POST /api/news/update também pode ser chamada diretamente com Authorization: Bearer NEWS_JOB_SECRET. Se a chamada ao modelo principal falhar, o job tenta automaticamente o fallback e, depois, a última reserva. O arquivo data/news.json é um cache local de primeira etapa; em hospedagem serverless, use um armazenamento persistente na segunda etapa.

O modelo informado é chamado pela API compatível de chat completions do OpenRouter. O modelo não recebe response_format; por isso o JSON é solicitado no prompt e validado no servidor. Não coloque a chave no frontend, no repositório ou em mensagens de log.

## Próxima etapa: persistência

O contrato entre a interface e a regra de negócio está isolado em lib/simulation.ts, enquanto as simulações são persistidas no MySQL por usuário autenticado. Em uma próxima etapa, podem ser adicionados cadastro e múltiplos usuários, autorização por papel, auditoria e uma biblioteca de PDF com geração server-side, se isso for necessário para o aceite final.
