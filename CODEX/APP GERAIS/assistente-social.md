# Assistente Social

## Objetivo

Documentar o app de IA da Assistente Social criado como aplicativo AI Studio.

## Status

- atual: documentado a partir do README
- prioridade: a definir
- ultima atualizacao: 2026-04-09

## Contexto

O README e curto: trata-se de um app AI Studio com instrucoes basicas para instalar dependencias, definir `GEMINI_API_KEY` e rodar localmente.

## Arquivos relevantes

- `ASSISTENTE SOCIAL/README.md`
- `ASSISTENTE SOCIAL/src/`
- `ASSISTENTE SOCIAL/public/`
- `ASSISTENTE SOCIAL/package-lock.json`

## Fatos

- o projeto foi gerado a partir do AI Studio
- a chave Gemini e obrigatoria para executar localmente

## Decisoes

- manter a configuracao de secrets fora do codigo
- preservar o fluxo de dev local simples

## Prompts que funcionaram

- "Resuma o app Assistente Social e como executa-lo localmente"

## Session log

- 2026-04-09: nota atualizada com base no README

## Historico cru

### `ASSISTENTE SOCIAL.md`
```text
os usuários desse app estão reclamando que o agente é muito lento e muito fraco na respostas



13 mensagens anteriores
Vou inspecionar a estrutura do app e identificar onde o agente está sendo configurado, porque lentidão e respostas fracas normalmente vêm de modelo, prompt, streaming ou cadeia de ferramentas.

Encontrei o backend do chat em netlify/functions/chat.ts e um wrapper em src/services/gemini.ts. Vou ler esses pontos junto com o README e o package.json para ver se o problema é modelo, contexto excessivo ou chamada síncrona sem streaming.

Já há um sinal claro de inconsistencia: o README fala em Gemini, mas o backend do chat usa OpenRouter com claude-3.5-sonnet. Vou checar o servidor e o fluxo do chat para ver se isso está gerando latência desnecessária ou prompts muito pesados.

A raiz pode estar mais no backend do que no UI: o chat manda todo o histórico a cada turno e usa um modelo caro/lento por padrão. Vou confirmar como o histórico é montado e se há redundância entre server.ts e netlify/functions, porque isso afeta tanto velocidade quanto qualidade.

Estou confirmando o roteamento porque um segundo problema comum é o app falar com um endpoint diferente no local e no deploy. Se houver divergência entre server.ts e Netlify, isso também pode explicar inconsistência de desempenho.

Já identifiquei três causas prováveis: histórico inteiro demais, papéis de mensagem incompatíveis com OpenRouter e prompt pouco prescritivo. Vou corrigir isso nos dois caminhos do app, local e Netlify, para reduzir latência e melhorar a consistência da resposta.

Vou aplicar a correção agora. O foco é reduzir o payload de contexto, corrigir o formato das mensagens para o provedor e deixar o agente mais objetivo sem perder o tom profissional.

As mudanças principais estão aplicadas. Agora vou validar com o TypeScript para pegar qualquer regressão de tipagem antes de te entregar o resultado.

O TypeScript e o build ainda estão rodando. Se algo quebrar, eu ajusto em seguida; se passar, eu te devolvo um resumo direto do que mudou e do impacto esperado.

O build passou, mas o lint revelou dois problemas existentes no app e três em handlers do Netlify por tipos unknown. Vou corrigir isso para não deixar o código em estado quebrado.

Tem um import duplicado em App.tsx e três leituras de JSON sem cast nos handlers. Vou limpar isso e rodar o lint de novo.

O build já está avançando de novo. Estou só aguardando o resultado final para confirmar que não ficou nenhuma regressão depois da limpeza dos tipos.

A validação passou. Vou conferir o diff final para te devolver exatamente o que foi ajustado e qual efeito esperar no comportamento do agente.

Corrigi os principais gargalos que estavam derrubando a experiência do agente.

O que mudei:

Em /Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/src/App.tsx, o histórico agora é enviado só com as últimas 8 mensagens e o papel da resposta do bot foi ajustado para assistant em vez de model.
Em /Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/src/services/gemini.ts, normalizei o histórico antes de mandar para a API e adicionei timeout de 45s para não deixar o usuário preso indefinidamente.
Em /Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/server.ts e /Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE-SOCIAL/netlify/functions/chat.ts, corrigi a montagem das mensagens para OpenRouter, limitei o contexto, deixei o prompt mais direto e defini max_tokens/temperature para respostas mais objetivas.
Também ajustei os handlers de Netlify em /Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/netlify/functions/research.ts e /Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/netlify/functions/save-research.ts para limpar erros de tipo.
Pontos que estavam prejudicando o agente:

O histórico era enviado inteiro, o que deixa a requisição mais lenta conforme a conversa cresce.
As mensagens do bot estavam indo como model, mas o provedor espera assistant.
O prompt estava genérico demais para um uso profissional, então a resposta tendia a vir menos direta.
Validação:

npm run lint passou.
npm run build passou.
Se quiser, o próximo passo mais efetivo é eu implementar streaming de resposta para o usuário ver o texto chegando aos poucos, o que melhora muito a sensação de velocidade.


sim, implemente



8 mensagens anteriores
Streaming implementado.

O que mudou:

O chat agora envia a resposta em chunks, em vez de esperar o texto completo.
A UI mostra a resposta crescendo em tempo real.
Mantive o histórico curto e o prompt objetivo, para continuar reduzindo latência.
O endpoint foi ajustado no servidor local e no handler do Netlify.
Arquivos principais:

/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/src/App.tsx
/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/src/services/gemini.ts
/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/server.ts
/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/netlify/functions/chat.ts
Validação:

npm run lint passou
npm run build passou
Referência técnica usada:

Netlify Functions streaming docs
Se quiser, o próximo passo mais útil é eu adicionar um botão de parar geração durante a resposta.


vamos agora resolver o problema da seção "Documentos" . Nessa seção a busca é muito semelhando abusca do agente. A verdadeira função desse seção é buscar documentos, seja PDF ou sites, como se fosse uma busca do google. Mas ele apresenta textos sobre os documentos e não os documentos



17 mensagens anteriores
Reestruturei a aba Documentos para buscar fontes reais, não texto de agente.

O que mudou:

A seção agora faz busca por PDFs, sites e documentos locais.
Os resultados aparecem como cards com título, URL, tipo e snippet.
A biblioteca local ficou separada da busca web.
A busca externa usa resultados reais do Bing, em vez de resumir a pergunta.
A listagem de documentos foi mantida em /api/documents.
Arquivos alterados:

/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/src/App.tsx
/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/src/services/documents.ts
/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/server.ts
/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/netlify/functions/documents.ts
Validação:

npm run lint passou
npm run build passou
Observação prática:

No servidor local, os documentos salvos podem ser abertos via rota de download.
Nos resultados da web, o clique vai direto para a fonte externa.
Se quiser, eu posso fazer o próximo ajuste e adicionar:

filtro por PDF / site
busca por domínio, tipo planalto.gov.br
preview do PDF dentro da aba.

conferir se ficou garantido "salvar o documento" , de modo que, nessa seção haja uma lista de documentos salvos



6 mensagens anteriores
Sim. Agora o salvamento ficou amarrado de ponta a ponta.

O que está garantido:

A pesquisa salva passa por /api/save-research no frontend.
No backend local, eu adicionei o endpoint correspondente em /Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/server.ts.
O salvamento grava um registro em documents e fragmenta o conteúdo em doc_chunks.
A aba Documentos lê /api/documents, então a lista de salvos aparece ali.
As entradas do tipo research agora aparecem como Pesquisa salva, sem link quebrado.
Para pesquisas salvas no backend local, o download agora reconstrói o texto salvo a partir dos chunks.
Também ajustei a aba para deixar isso explícito:

O bloco principal virou Documentos salvos.
A busca continua separada, como fonte web.
A biblioteca local mostra o que foi salvo de fato.
Validação:

npm run lint passou
npm run build passou
Se quiser, o próximo passo útil é eu fazer a aba Documentos mostrar:

filtros por salvo, web, PDF
um preview do conteúdo salvo ao clicar em um item
botão de excluir documento salvo

sim , vamos para os proximos passos



8 mensagens anteriores
Feito. A seção Documentos agora está organizada em torno de documentos realmente salvos.

O que foi adicionado:

Lista de documentos salvos com filtro por Todos, Pesquisas, PDFs e Outros
Painel de pré-visualização do documento selecionado
Botão para excluir documento salvo
Botão para baixar o arquivo ou a pesquisa salva
Endpoints de preview e delete no backend local e no Netlify
Fluxo garantido:

saveResearch(...) grava no banco
/api/documents lista os salvos
/api/documents/:id/preview mostra o conteúdo salvo
/api/documents/:id com DELETE remove o documento
A aba não mistura mais busca web com acervo salvo
Arquivos principais:

/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/src/App.tsx
/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/src/services/documents.ts
/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/server.ts
/Users/pvolkermini/APLICATIVO-MINI/ASSISTENTE SOCIAL/netlify/functions/documents.ts
Validação:

npm run lint passou
npm run build passou
Se quiser, no próximo passo eu posso melhorar a busca de documentos salvos com:

ordenação por data/nome
busca dentro do acervo salvo
tags por assunto para facilitar navegação.

vamos encerrar. Vamos fazer o commit e ver como fica a publicação no Netlify. Commit no github: Username: Pavolker. URL: github.com/Pavolker/assistente-social.



4 mensagens anteriores
Commit feito e enviado para o GitHub.

Commit: 311e52b — Improve chat speed and document search
Branch: main
Remote: https://github.com/Pavolker/assistente-social.git
O push foi concluído com sucesso, então, se esse repositório estiver conectado ao Netlify, a publicação deve disparar automaticamente.

O que eu não consigo confirmar daqui:

o status do deploy dentro do Netlify
se o build do Netlify passou ou falhou
Próximo passo prático:

Abrir o painel do Netlify e conferir o deploy mais recente.
Se quiser, eu posso te ajudar a interpretar o log do deploy se você me mandar o erro ou o link do build.

publicado. Quando vou na seção documentos a página aparece e some imediatamente



5 mensagens anteriores
O problema mais provável era instabilidade na renderização da aba Documentos com dados incompletos. Eu endureci o componente para não quebrar se vier algum registro sem filename, mime_type ou file_path.

O que ajustei agora:

Proteção extra no filtro de documentos salvos.
Proteção extra no render dos cards.
Normalização segura de filename, file_path e mime_type.
Validação:

npm run lint passou
npm run build passou
Se a aba ainda “piscar” no Netlify depois desse ajuste, a próxima suspeita é a rota aninhada de preview/download em /api/documents/:id/... no redirect do Netlify, e eu resolveria isso simplificando as rotas para evitar path segments profundos.
```
