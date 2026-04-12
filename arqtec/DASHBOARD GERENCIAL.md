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