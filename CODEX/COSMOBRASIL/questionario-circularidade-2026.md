# Questionario Circularidade 2026

## Objetivo

Documentar o painel de gerencia para respostas e HTMLs de relatorios de circularidade.

## Status

- atual: documentado a partir do README
- prioridade: a definir
- ultima atualizacao: 2026-04-09

## Contexto

O README descreve um painel HTML simples, com bloqueio por senha e endpoints backend para listar respostas e abrir os HTMLs.

## Arquivos relevantes

- `QUESTIONARIO-CIRCULARIDADE-2026/README.md`
- `QUESTIONARIO-CIRCULARIDADE-2026/index.html`
- `QUESTIONARIO-CIRCULARIDADE-2026/backend/server.js`
- `QUESTIONARIO-CIRCULARIDADE-2026/APPS.md`

## Fatos

- o acesso do painel e protegido por senha no front-end
- o backend expõe endpoints administrativos para respostas

## Decisoes

- preservar o bloqueio e a vizualizacao de respostas
- manter a estrutura simples de painel administrativo

## Prompts que funcionaram

- "Resuma o painel de gerencia e seus endpoints principais"

## Session log

- 2026-04-09: nota atualizada com base no README

## Historico cru

### `DASHBOARD CIRCULARIDADE.md`
```text
analise esse app



4 mensagens anteriores
O app é um dashboard estático, sem package.json ou build step, feito em HTML + CSS + JS puro. O que existe no HEAD é bem direto: index.html monta a UI, styles.css define o tema escuro, app.js faz todo o fetch/render, e netlify.toml configura deploy e proxy para a API.

Ponto importante primeiro: no workspace atual, os arquivos do app estão deletados no working tree. Então a análise abaixo é do conteúdo do HEAD, não do estado atual do diretório.

O que o app faz

Carrega filtros de setor, produto, cidade, UF e período.
Busca dados em GET /api/dashboard/filters e GET /api/dashboard/overview.
Renderiza KPIs e 4 visões gráficas com Chart.js carregado via CDN.
Atualiza manualmente e também por auto-refresh a cada 60 segundos.
Mostra recomendações estratégicas baseadas nos tópicos com menor score.
Pontos fortes

Arquitetura simples e fácil de publicar no Netlify.
Sem dependências de build, então o deploy é barato e rápido.
Proxy em netlify.toml evita CORS no frontend.
Separação razoável entre UI, estilo e lógica.
O código já trata ausência de cosmobIndicadores e converte valores com segurança básica.
Riscos e fragilidades

O estado atual do repositório está inconsistente: os arquivos principais foram removidos no working tree. Isso impede rodar o app daqui sem restaurar os arquivos.
A UI depende de Chart.js via CDN. Se o CDN falhar ou bloquear, o dashboard quebra.
O tratamento de erro é fraco: quando a API falha, o usuário recebe só um alert, sem estado de carregamento, fallback visual ou retry.
Cada mudança de filtro dispara carregarFiltros() e atualizarDashboard(), sem debounce nem cancelamento. Em mudanças rápidas, pode haver corrida de requisições e renderização de dados fora de ordem.
result.success falso é tratado com return silencioso. Isso pode deixar a tela com dados antigos sem indicar claramente o problema.
Há uma possível divergência metodológica entre a proposta e o processamento antigo. Em scripts/processar_baseantiga.py, OUTPUT inclui Q3 até Q6 e VIDA inclui Q7 até Q9. Já docs/PROPOSTA_DASHBOARD.md menciona outra divisão em parte do texto. Se o backend seguir a lógica do script, a documentação e o dashboard podem divergir.
Leitura técnica

É um frontend enxuto, mais próximo de uma página analítica do que de uma aplicação complexa.
O risco principal não é arquitetura, é consistência de contrato com o backend e robustez de UX.
O maior ponto de atenção funcional é garantir que os agregados da API batam com a metodologia esperada do questionário.
Se quiser, eu posso seguir por um destes caminhos:

Fazer uma revisão do contrato frontend/backend e apontar exatamente onde pode quebrar.
Restaurar/inspecionar os arquivos deletados e validar se o app ainda sobe localmente.
Propor uma versão mais robusta do dashboard, com estados de loading, erro e cancelamento de requisições.

nosso problema aqui é garantir que o relatório gerado pelo formulário (/Users/pvolkermini/APLICATIVO-MINI/COSMOBRASIL/QUESTIONARIO-CIRCULARIDADE-2026) logo após o usuário preencher, seja disponibilizado aqui nesse dashboard em formato HTML



10 mensagens anteriores
Implementei o caminho para o HTML do relatório aparecer no dashboard.

O que mudou:

No backend principal, a listagem admin agora pode ser filtrada pelos mesmos parâmetros do dashboard e também informa se cada relatório tem HTML disponível.
O endpoint de HTML recebeu Cache-Control: no-store para evitar cache de preview antigo.
No dashboard-circularidade, recriei a página com:
filtros analíticos,
KPIs e gráficos,
lista de relatórios recentes,
preview inline do HTML gerado pelo formulário via iframe.
O dashboard também aceita token admin no próprio painel e usa isso para acessar:
GET /api/admin/respostas
GET /api/admin/respostas/:id/html
Arquivos principais:

backend/server.js
dashboard-circularidade/index.html
dashboard-circularidade/app.js
dashboard-circularidade/styles.css
dashboard-circularidade/netlify.toml
Validação:

node --check passou no backend e no JS do dashboard.
Ponto central da solução:

o HTML do relatório já é salvo no banco no POST /api/questionario, então o dashboard não depende de PDF nem do Google Drive para mostrar o relatório. Ele lê direto do PostgreSQL e renderiza o HTML na tela.
Se quiser, eu posso fazer o próximo passo:

adicionar um deep-link para abrir automaticamente o último relatório salvo,
ou integrar um botão “Abrir relatório do último envio” na tela final do formulário.

rodar o app



7 mensagens anteriores
O app já está rodando na porta 3000.

Painel principal: http://127.0.0.1:3000/
Dashboard circularidade: http://127.0.0.1:3000/dashboard-circularidade/
Eu não subi uma segunda instância porque a porta 3000 já estava ocupada por um processo node ativo (PID 33041), e as duas URLs acima responderam 200 OK.

Também faltava o módulo backend/google-drive-service.js; eu criei um stub mínimo para o backend conseguir carregar sem quebrar nessa dependência.


O nome PDF ainda aparece na tabela, substituir por "Relatório HTML"



3 mensagens anteriores
Troquei a tabela do painel raiz para HTML:

O cabeçalho PDF virou Relatório HTML.
Os links da tabela agora apontam para /api/admin/respostas/:id/html em vez de /pdf.
Arquivo alterado:

index.html
Como o servidor local já está rodando na porta 3000, a mudança já fica visível em:

http://127.0.0.1:3000/
Se quiser, eu também posso alinhar o texto do README.md raiz para deixar de mencionar PDF.


Ao clicar na visualização do relatorio aparece esse mensagem: {"success":false,"error":"Endpoint não encontrado."}



7 mensagens anteriores
O 404 {"success":false,"error":"Endpoint não encontrado."} vinha de uma instância antiga do backend que ainda estava rodando. Eu reiniciei o servidor com a versão atual e a rota HTML agora responde.

O que acontece agora:

GET /api/admin/respostas/:id/html já existe e está ativo.
A resposta atual é 401 Unauthorized porque o painel admin exige ADMIN_PANEL_TOKEN.
Ou seja, o erro mudou de “rota inexistente” para “acesso não autorizado”.

Como usar:

No painel raiz, preencha o campo Token admin antes de clicar em Visualizar ou Baixar.
Se você quiser acesso aberto no ambiente local, deixe ADMIN_PANEL_TOKEN vazio no backend/.env.
Se quiser, eu posso fazer o próximo ajuste para:

remover a exigência de token só no ambiente local, ou
deixar o botão Visualizar desabilitado até o token ser preenchido.

faça o commit do app. Username: cosmobrasil. URL:  github.com/cosmobrasil/painel-gerencia



4 mensagens anteriores
Commit feito no repositório raiz.

Commit: f0c9047
Mensagem: Expose HTML report view in admin panel
O commit inclui:

troca da tabela para Relatório HTML,
endpoint HTML no backend com suporte ao recorte,
stub do backend/google-drive-service.js para o servidor subir sem quebrar.
O repositório ficou ahead 1 em relação ao remoto painel-gerencia/main.

Observação:

existem vários arquivos não rastreados no workspace, incluindo .env, node_modules, backups e o subprojeto dashboard-circularidade/; eu não incluí isso no commit.
Se quiser, eu posso fazer o push desse commit para git@github.com:cosmobrasil/painel-gerencia.git.


faça o push



2 mensagens anteriores
Push concluído.

Remote: git@github.com:cosmobrasil/painel-gerencia.git
Branch enviada: push-painel-gerencia -> main
Commit: f0c9047
Se quiser, eu também posso alinhar o repositório dashboard-circularidade em outro push separado, porque ele está em outro remoto (dash-circular) e hoje está com alterações próprias não commitadas.
```

### `DASHBOARD GERENCIAL.md`
```text
Vou inspecionar a estrutura do projeto e buscar referências diretas a postgres, pg, prisma, supabase e variáveis de conexão para confirmar se o dashboard realmente fala com banco.

A busca textual não encontrou nenhum indício imediato de driver, ORM ou URL de banco. Agora vou listar os arquivos do projeto para ver se ele é só frontend, API separada, ou se a conexão fica escondida em configuração.

Encontrei um projeto bem pequeno: só README.md, index.html e netlify.toml. Vou ler os três em paralelo para confirmar se há backend implícito, env vars, ou apenas chamadas a uma API externa.

Já dá para concluir a arquitetura: este repositório é só frontend estático com proxy para uma API externa. Vou pegar as linhas exatas para te mostrar onde isso aparece.

Sim, mas com uma ressalva importante: neste repositório eu não encontrei conexão direta com PostgreSQL.

O que existe aqui é só um frontend estático que consome uma API externa:

README.md (line 5) mostra apenas os endpoints GET /api/admin/respostas e GET /api/admin/respostas/:id/pdf.
index.html (line 155) define API_BASE apontando para http://localhost:3000, '' no Netlify, ou https://formulario-production-8df7.up.railway.app.
netlify.toml (line 5) faz proxy de /api/* para esse backend no Railway.
Resumo prático:

Este dashboard não fala com Postgres diretamente.
Se houver PostgreSQL, ele está no backend (formulario-production-8df7.up.railway.app), não neste frontend.
Se você quiser, eu posso seguir e tentar identificar no backend se ele usa pg, Prisma, Supabase ou outra camada de acesso ao Postgres.
```

### `QUESTIONARIO CIRCULARIDADE.md`
```text
identifique o banco de dados desse app, faça a busca nas sub-pastas "dashboard-circularidade" e "dashboard-gerencial"



8 mensagens anteriores
O banco de dados do app é PostgreSQL, hospedado no Railway.

O que encontrei nas duas subpastas:

dashboard-circularidade e dashboard-gerencial são frontends estáticos; ambos apontam para a API do backend e não definem banco local.
dashboard-circularidade usa GET /api/dashboard/filters e GET /api/dashboard/overview via https://formulario-production-8df7.up.railway.app ou localhost:3000 em desenvolvimento. Veja app.js (line 4) e README.md (line 15).
dashboard-gerencial usa GET /api/admin/respostas e GET /api/admin/respostas/:id/pdf na mesma API. Veja index.html (line 157) e README.md (line 5).
A confirmação do banco vem do backend:

O servidor cria Pool do pacote pg, com PGHOST, PGPORT, PGDATABASE, PGUSER e PGPASSWORD, ou seja, PostgreSQL. Veja backend/server.js (line 5) e backend/server.js (line 57).
O schema em SQL é explicitamente PostgreSQL e define as tabelas empresas e questionarios, além da view vw_dados_dashboard. Veja backend/database/schema.sql (line 1).
O backend README também descreve o projeto como “Backend em Node.js + Express para conectar o frontend ao PostgreSQL Railway”. Veja backend/README.md (line 1).
Observação importante:

Em dashboard-circularidade, existe um fluxo local de Excel para CSV: baseantiga.xlsx é processado para data/baseantiga_processada.csv. Isso é dado de apoio/legado, não o banco do app. Veja processar_baseantiga.py (line 11).
Se quiser, eu também posso seguir e te dizer qual é o nome do banco/tabelas reais em uso no backend ou localizar onde estão as credenciais de conexão no projeto.


Faça uma cópia completa desse banco, acredito que a melhor forma deva ser csv, armazenado aqui mesmo no computador. É a melhor forma ?



13 mensagens anteriores
Fiz a cópia local do banco em:

local-db-backup-2026-03-25T0000
O que ficou salvo lá:

database.sql: dump completo do PostgreSQL, com schema e dados, pronto para restauração.
*.csv: um CSV por tabela do schema público.
vw_dados_dashboard.csv: export da view do dashboard.
tables.txt: lista das tabelas exportadas.
Resposta curta à sua pergunta: não, CSV sozinho não é a melhor forma de cópia completa.
CSV é bom para análise, mas perde:

tipos de dados
chaves estrangeiras
constraints
índices
views e triggers
Para uma cópia completa e recuperável, o melhor é:

database.sql como backup principal
CSVs como complemento prático
Também confirmei que esse banco é maior do que só empresas e questionarios: o schema público exportado tem 39 tabelas.

Se quiser, eu posso fazer o próximo passo e:

compactar essa cópia em .zip
gerar uma versão “somente dados principais” em CSV
montar um backup separado só das tabelas do questionário (empresas e questionarios)

voce fez o backup de todo o banco de dados, de todos os projetos, não só do banco desse formulário de circularidade. Mantenha a cópia do banco completo já feita, mas o que nos interessa nesse momento são somente s tabelas do aplicativo de dashboard, que é composto de um formulário, um dashboard geral e um dashboard gerencial. Identifique esse conjunto



1 mensagem anterior
O conjunto que interessa para esse aplicativo é este:

empresas
questionarios
E, para consumo do dashboard, existe ainda a view:

vw_dados_dashboard
Isso não é tabela, mas é a forma consolidada usada para exportação/consulta do painel.
Por que esse é o recorte correto:

O schema do app define só empresas e questionarios, com a view vw_dados_dashboard em cima delas. Veja backend/database/schema.sql (line 7).
Os endpoints do formulário e dos dois dashboards consultam exatamente questionarios + empresas com JOIN. Veja:
backend/server.js (line 1043)
backend/server.js (line 1068)
backend/server.js (line 1118)
backend/server.js (line 1272)
backend/server.js (line 1331)
Então, para o backup que vamos usar daqui para frente, eu recomendo separar assim:

Base do aplicativo: empresas.csv + questionarios.csv
Opcional para dashboard: vw_dados_dashboard.csv
Não incluir as demais tabelas do banco compartilhado, porque elas não pertencem a esse app
Se quiser, eu já faço agora uma cópia limpa só desse subconjunto em uma pasta nova, sem mexer no backup completo que já ficou salvo.


não apague a pasta "local-db-backup-2026-03-25TOOOO". Deixe como esta. Crie outra pasta para o backup do banco dos applicativos de circularidade, como recomendado



4 mensagens anteriores
Mantive a cópia completa intacta e criei um backup novo e focado em:

circularidade-db-backup-2026-03-25
Esse backup contém só o recorte do aplicativo de circularidade:

empresas.csv
questionarios.csv
vw_dados_dashboard.csv
circularidade.sql com schema + dados apenas dessas partes
A pasta completa anterior foi mantida sem alterações:

local-db-backup-2026-03-25T0000
Se quiser, no próximo passo eu posso:

renomear a nova pasta para algo mais limpo, como backup-circularidade
compactar essa nova pasta em .zip
gerar um CSV único consolidado para análise rápida

Perfeito, agora vamos apagar todos os  dados das tabelas : empresas ; questionarios ; além da  a view: vw_dados_dashboard . Vamos manter todas as estruturas dessas tabelas, para elas receberem novos dados. O aplicativo do formulario de circularidade vai começasr a ser usado em uma nova fase e precisamos ter o banco de dados desse sistema de circularidade limpor, mas operacional, pronto para começar a funcionar imediatamente com novos dados. Não faça nada ainda, apenas me diga se entendeu


Entendi.

Você quer limpar apenas os dados do aplicativo de circularidade, mantendo a estrutura operacional do banco:

apagar os registros de empresas
apagar os registros de questionarios
remover/recriar a vw_dados_dashboard conforme necessário, mas sem quebrar a estrutura do sistema
deixar o banco pronto para receber novos formulários imediatamente
Não vou executar nada ainda.


Se tudo  ficou entendido, pode limpar os registros das tabelas: empresas; questionários e vw_dados_dashboard [ no caso da visualização "vw_dados_dashboard", ela precisa estar disponível imediatamente após ao primeiro formulário ser respondido]




1 mensagem anterior
Feito.

Limpei os dados das tabelas do aplicativo de circularidade e mantive a estrutura:

empresas: 0 registros
questionarios: 0 registros
A vw_dados_dashboard foi preservada como definição de view, e agora retorna 0 linhas porque depende dessas tabelas-base. Ela ficará disponível normalmente assim que o primeiro formulário for respondido.

Verificação concluída:

empresas=0
questionarios=0
vw_dados_dashboard=0

rodar o formulario



4 mensagens anteriores
O formulário já está rodando em:

http://localhost:3000/index.html
O backend também subiu em:

http://localhost:3000
Validação que fiz:

a página principal responde 200 OK
a rota de health responde, mas com erro de banco:
{"status":"error","message":"The server does not support SSL connections"}
Isso significa que o app front-end abriu corretamente, mas o salvamento no PostgreSQL local não vai funcionar sem ajustar as variáveis de conexão do banco. Se quiser, eu posso fazer o próximo passo e corrigir essa conexão para você rodar o fluxo completo.


mensagem de erro: ❌ Token da API EmpresaAqui não configurado no servidor.



1 mensagem anterior
A mensagem vem da consulta de CNPJ, não do envio do formulário.

O backend lê a variável EMPRESAQUI_TOKEN em backend/server.js (line 768).
Como não existe .env local com essa variável, a rota /api/cnpj/:cnpj responde com esse erro.
O botão de consulta chama esse endpoint em app-postgres.js (line 118).
Para corrigir localmente:

Crie um arquivo .env na raiz do projeto.
Adicione:
EMPRESAQUI_TOKEN=seu_token_aqui
Reinicie o backend.
Se você não tiver esse token agora, o formulário continua funcionando sem a consulta de CNPJ. Nesse caso, basta não usar o botão Consultar.

Se quiser, eu posso fazer uma melhoria no app para que, quando o token não existir, o botão de consulta fique desativado e a mensagem deixe de aparecer.


Se voce não faz a busca correta, voce não acha: /Users/pvolkermini/APLICATIVO-MINI/COSMOBRASIL/QUESTIONARIO-CIRCULARIDADE-2026/backend/.env



6 mensagens anteriores
Você tinha razão: o token está em backend/.env, e o problema era o carregamento do .env errado.

Corrigi o backend para ler explicitamente backend/.env em backend/server.js.

Validei assim:

o backend sobe lendo 12 variáveis do .env de backend/
a rota de CNPJ não responde mais com “Token da API EmpresaAqui não configurado no servidor”
agora ela retorna CNPJ inválido. Informe 14 dígitos válidos. para um CNPJ de teste, o que confirma que o token foi carregado
Também deixei o servidor rodando em:

http://localhost:3000
Se quiser, eu posso agora testar a rota com um CNPJ válido para confirmar a consulta real na EmpresaAqui.


correto, vamos preparar para fazer o commit do app do formulario



4 mensagens anteriores
Commit feito: e166b4d
Mensagem: Consolidate material circularity profile

O commit inclui as alterações do formulário, backend, dashboard e painel de relatórios. Os arquivos soltos que já estavam no tree continuam fora do commit, como APPS.md, QUESTIONARIO app.md, backend/backups/, dashboard-gerencial/, relatorios app macapa/, selocosmob.pdf e tmp/.

Se quiser, no próximo passo eu posso:

criar uma branch de release a partir desse commit;
preparar a mensagem de pull request;
te passar um resumo executivo do que entrou no commit.

faça o push



3 mensagens anteriores
Push concluído em origin/main.

Repositório: git@github.com:cosmobrasil/formulario.git
Commit enviado: e166b4d
Range atualizado: 1a654ca..e166b4d
Se quiser, eu posso agora preparar o próximo commit separado para o restante dos arquivos soltos que ficaram fora deste push.


Identifique se no dshboard gerencial (/Users/pvolkermini/APLICATIVO-MINI/COSMOBRASIL/QUESTIONARIO-CIRCULARIDADE-2026/dashboard-gerencial) ainda estamos usando o antigo indicador IME



3 mensagens anteriores
Sim. No dashboard-gerencial, ainda há uso do indicador antigo IME em dois pontos:

Cabeçalho da tabela em /Users/pvolkermini/APLICATIVO-MINI/COSMOBRASIL/QUESTIONARIO-CIRCULARIDADE-2026/dashboard-gerencial/index.html (line 144)
Célula de exibição dos valores em /Users/pvolkermini/APLICATIVO-MINI/COSMOBRASIL/QUESTIONARIO-CIRCULARIDADE-2026/dashboard-gerencial/index.html (line 214)
Não encontrei outro arquivo dentro de dashboard-gerencial/ com referência a IME. O README.md também não fala desse indicador.

Se quiser, eu posso já trocar esse painel para PCM agora.


faça a troca



2 mensagens anteriores
Troca feita no dashboard-gerencial.

O cabeçalho agora mostra IGC / PCM em dashboard-gerencial/index.html (line 144)
A linha de dados agora lê item.pcm, com fallback para item.ime só para compatibilidade com registros antigos em dashboard-gerencial/index.html (line 214)
Se quiser, eu também posso padronizar o restante dos textos do dashboard-gerencial para usar PCM em vez de IME em toda a interface e documentação.


sim, faça a padronização  dos textos e depois faça o commit com a correção . Username: cosmobrasil. URL:  github.com/cosmobrasil/painel-gerencia.



15 mensagens anteriores
Padronização concluída e publicada no repositório github.com/cosmobrasil/painel-gerencia.

Commit local/publicado: 9294b8c
Mensagem: Standardize gerencial dashboard PCM labels
Push: 197b320..9294b8c em main
O ajuste ficou em:

index.html
README.md
Se quiser, eu posso agora revisar o dashboard-gerencial em busca de qualquer texto remanescente de IME fora da interface principal.


Não mudou nada. O texto da tabela continua o mesmo: IGC / IME




7 mensagens anteriores
O ajuste anterior estava no arquivo errado. O painel do painel-gerencia serve o index.html da raiz, e foi nele que corrigi a tabela.

O que mudou:

Cabeçalho da coluna: IGC / PCM
Valor exibido: item.pcm, com fallback para item.ime apenas para compatibilidade com dados antigos
Commit publicado:

d4b0b66 - fix: update gerencial table label to PCM
Push concluído em:

github.com/cosmobrasil/painel-gerencia branch main
Se você abrir o painel e ainda enxergar IGC / IME, então é cache/deploy antigo. Nesse caso eu posso validar a versão publicada no Netlify e apontar exatamente onde ele está servindo a página desatualizada.
```
