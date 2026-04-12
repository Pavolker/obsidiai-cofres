---
source: DATAGPT
conversation_id: 694bd0fb-1e80-8325-b203-ee889afed5a1
title: "App Leitura PDF"
theme: TECNOLOGIA
created: 2025-12-24T11:41:06.611484Z
message_count: 2
attachments_count: 0
---

# App Leitura PDF

- Tema: `TECNOLOGIA`
- Conversation ID: `694bd0fb-1e80-8325-b203-ee889afed5a1`

## Transcrição

### user

quero criar um app de leitura de PDF, que tenha a funcionalidade de simular um livro, com passagens de páginas, marcar texto, extrair citações, escrever e guardar notas sobre o livro que estou lendo e as notas feitas em outras leituras. Faça o prompt para esse app, preferencialmente em HTML+CSS+JS

### assistant

Paulo, abaixo vai um prompt completo para gerar um app (single-page) em HTML+CSS+JS que lê PDF e simula livro (virar páginas), permite marcação (highlight), extrair citações, criar notas e manter uma “biblioteca” de notas por livro (e reutilizar/consultar notas de outras leituras). O prompt força uma implementação viável só com bibliotecas CDN e armazenamento local (IndexedDB/localStorage), sem backend.

PROMPT (cole em outra IA para gerar o código)

Você é um engenheiro full-stack focado em front-end. Gere um aplicativo web de página única (single file) em HTML+CSS+JS, sem frameworks (sem React/Vue), com dependências apenas via CDN. O app deve rodar abrindo o arquivo .html localmente (file://) e também em qualquer hospedagem estática.

Objetivo do app
Criar um leitor de PDF com experiência de “livro”: navegação com animação de virar página, suporte a seleção de texto, marcação (highlight), extração de citações, criação/armazenamento de notas por livro, e uma área para consultar notas feitas em outros livros.

Bibliotecas permitidas (CDN)
1) PDF.js (Mozilla) para renderizar PDF e extrair texto.
2) Opcional: uma biblioteca leve para efeito de virar página (ex.: StPageFlip) ou implementar o efeito manualmente com CSS transform + canvas duplo. Se usar biblioteca, inclua via CDN; se não for possível, implemente o efeito com CSS/JS (duas “folhas” e transição).
3) IndexedDB (nativo) como armazenamento principal; use localStorage apenas para preferências de UI.

Requisitos funcionais (MVP obrigatório)
A) Importação de PDF
- Botão “Abrir PDF” com input type="file" aceitando .pdf.
- Ao abrir, criar um identificador do livro (hash simples do arquivo: nome + tamanho + lastModified; ou hash parcial do ArrayBuffer).
- Guardar metadados do livro: título (se disponível), nome do arquivo, nº de páginas, data de abertura.

B) Visualização tipo livro
- Mostrar duas páginas lado a lado (modo “spread”) quando largura permitir; em telas menores, mostrar uma página.
- Animação de virar página ao avançar/voltar (setas, clique nas bordas, e teclado: ← →, PgUp PgDn).
- Controles: zoom (50%–200%), ir para página (campo numérico), indicador “página atual / total”.
- Alternar “modo rolagem” vs “modo livro” (toggle).

C) Camada de texto selecionável
- A renderização deve permitir seleção de texto real (text layer do PDF.js sobre o canvas).
- Selecionar texto e aparecer um mini-menu contextual com ações:
  1) “Marcar” (highlight)
  2) “Citar”
  3) “Anotar”
  4) “Copiar”

D) Marcação (highlights)
- Ao clicar “Marcar”, criar highlight persistente para aquela seleção:
  - Guardar: livroId, pageNumber, texto selecionado, coordenadas relativas (bounding boxes), cor (padrão amarelo), timestamp.
- Renderizar highlights ao reabrir o livro e ao mudar de página.
- UI para listar highlights do livro em uma lateral (“Marcações”), com clique levando à página correspondente.
- Permitir remover highlight individual.

E) Citações
- Ao clicar “Citar”, abrir um modal “Extrair citação” com:
  - Texto selecionado (editável)
  - Campo “Referência” automático: Autor (se usuário preencher no cadastro do livro), Título, Página, e um formato ABNT básico (não precisa ser perfeito).
  - Botão “Salvar citação” (salva como item em “Citações” do livro e também em uma “Biblioteca de Citações” global pesquisável).
- Cada citação deve guardar: livroId, pageNumber, quoteText, createdAt, tags (lista), e opcional “contexto” (trecho anterior/posterior se possível via textContent do PDF.js; se não, não implementar).

F) Notas
- Ao clicar “Anotar”, abrir um painel/ modal com editor de nota (textarea) e:
  - Linkar a nota à seleção (texto + página) ou permitir nota solta do livro.
  - Tags, e campo “tipo”: leitura / insight / resumo / questão.
- Salvar notas por livro e também em um índice global.
- Ao reabrir o livro, listar notas do livro; clique leva à página (se vinculada).

G) Biblioteca (multi-livros)
- Tela “Biblioteca” (aba) com lista de livros já abertos.
- Para cada livro: título/arquivo, páginas, última leitura, contagem de notas/citações/highlights.
- Campo de busca global que pesquise em notas e citações de todos os livros (full-text simples).
- Exportação:
  - Exportar JSON do livro (metadados + notas + citações + highlights).
  - Exportar JSON de tudo.
  - Importar JSON (merge por livroId).

Requisitos de armazenamento
- Use IndexedDB com object stores:
  1) books (key: bookId)
  2) highlights (key: auto; index por bookId e pageNumber)
  3) notes (key: auto; index por bookId e pageNumber)
  4) quotes (key: auto; index por bookId e pageNumber; e index fullText para busca simples, se possível)
- Implementar funções utilitárias:
  - idbOpen(), idbPut(), idbGet(), idbGetAllByIndex(), idbDelete()
- Ao carregar o app, abrir DB e carregar lista de livros.

UI/UX (obrigatório)
- Layout em 3 áreas:
  1) Topbar com controles (Abrir, Biblioteca, Zoom, Página, Modo, Export/Import).
  2) Área central de leitura (livro com páginas).
  3) Sidebar direita com abas: “Notas”, “Citações”, “Marcações”, “Busca”.
- Design neutro, legível, sem ícones externos.
- Atalhos:
  - Ctrl/Cmd+F abre busca global
  - Ctrl/Cmd+S salva nota quando modal aberto
  - Esc fecha modais/menus

Detalhes técnicos do PDF.js (obrigatório)
- Carregar PDF via ArrayBuffer com FileReader.
- Renderizar páginas com canvas.
- Criar textLayer (div) para seleção:
  - use pdfjsLib.renderTextLayer (ou equivalente na versão atual) e posicionamento correto.
- Para highlights, transformar DOMRange da seleção em bounding boxes relativas ao textLayer/canvas; salvar como lista de retângulos normalizados (x,y,w,h em % do container).
- Ao renderizar, criar divs absolutas sem bloquear seleção (pointer-events none).

Efeito “virar página”
- Preferência:
  - Se usar biblioteca (StPageFlip), integrar com dois canvases por página e controle de eventos.
  - Se implementar manual: usar dois containers (página atual e próxima) com CSS transform origin + transição; o efeito não precisa ser perfeito, mas deve ser perceptível.
- Deve funcionar com mouse e teclado.

Robustez mínima
- Tratar erros (PDF inválido, falha ao renderizar, DB indisponível).
- Não travar UI: usar requestAnimationFrame ou async/await; renderização por demanda (somente páginas visíveis).
- Cache simples das últimas páginas renderizadas (ex.: Map pageNumber -> canvas bitmap).

Entrega do código
- Entregar um único arquivo HTML completo, com CSS no <style> e JS no <script>.
- Colocar comentários claros nas funções principais.
- No topo do arquivo, incluir uma seção “Como usar” (comentário HTML) com passos.

Critérios de aceite (auto-check)
- Abrir PDF e navegar páginas com animação.
- Selecionar texto e criar highlight persistente.
- Salvar citação com página e buscar depois.
- Criar nota vinculada a seleção e visualizar na sidebar.
- Fechar e reabrir o arquivo HTML e ver os dados persistidos (IndexedDB).

Agora gere o arquivo completo.

Fim do prompt.

Se você quiser, eu também posso te entregar uma versão “MVP mínimo” (sem efeito de virar página, mas com tudo de notas/citações/highlights funcionando) e depois uma versão 2 com o page-flip.
