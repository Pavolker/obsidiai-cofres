# Planejamento: Criar um Obsidian Próprio

**Data:** 2026-04-12

---

## Contexto

Ambiente atual: 2.106 arquivos .md organizados em 9 vaults (~33 MB de texto puro), com
scripts Python já existentes para processamento. Já existe infraestrutura de AI no vault
`second-brain`. Objetivo: criar uma alternativa ao Obsidian original com **IA integrada**
e **automações**, acessível via **web browser**.

---

## Vaults Existentes

| Vault | Arquivos .md | Conteúdo |
|---|---|---|
| DADOS | 1.069 | Base de conhecimento pessoal (17 categorias) |
| OPENAI | 843 | Conversas ChatGPT exportadas e categorizadas |
| LIVROS | 78 | Rascunhos de livros por gênero/tema |
| VIDA | 32 | Diário pessoal e memórias |
| CODEX | 50 | Documentação de projetos |
| CENTAURO | 12 | Filosofia, hobbies, cotidiano |
| DATAGPT | 5 | Exportações brutas do GPT |
| arqtec | 9 | Notas técnicas/arquitetura |
| second-brain | 8 | Infraestrutura do sistema AI |

---

## O que o Obsidian faz hoje (a replicar)

1. Leitura e edição de arquivos .md
2. Grafo visual de conexões entre notas (por `[[links]]` e tags)
3. Busca por texto em todos os arquivos
4. Organização em vaults/pastas
5. Preview do markdown formatado

---

## O que QUEREMOS adicionar (o Obsidian não tem)

1. IA respondendo perguntas sobre as notas
2. Sugestão automática de conexões entre notas
3. Categorização/organização automática de novas notas
4. Resumos e insights gerados por IA
5. Pipelines automáticos (ex: exportar conversa do GPT → nota categorizada)
6. **Integração nativa entre vaults** — os cofres devem se comunicar e compartilhar conexões entre si; uma nota em VIDA pode se conectar a uma nota em LIVROS ou DADOS sem barreiras, e o grafo deve mostrar essas conexões cruzadas; a busca e a IA operam sobre todos os vaults simultaneamente como se fossem um único espaço de conhecimento

---

## Análise de Viabilidade: Alta

Já existem no ambiente:
- Scripts Python funcionando (`process_docs_to_obsidian.py`, `process_files_with_gemini.py`)
- Estrutura de dados bem organizada (DADOS com 17 categorias numéricas)
- Acesso ao Claude API via Claude Code
- ~2.100 arquivos .md como base de dados já estruturada

---

## Abordagem Recomendada: App Web com Python + Claude API

### Stack Tecnológica

| Camada | Tecnologia | Motivo |
|---|---|---|
| Backend | Python (FastAPI) | Scripts Python já existentes |
| Frontend | HTML + JS (ou React) | App web no browser |
| Grafo | D3.js ou Cytoscape.js | Visualização de conexões |
| Busca semântica | ChromaDB + embeddings | Busca por significado, não só texto |
| IA | Claude API (Haiku/Sonnet) | Já integrado no ambiente |
| Armazenamento | Arquivos .md existentes | Sem migração necessária |

---

## Roadmap por Fases

### Fase 1 — MVP (base funcional)
- [ ] Servidor local que lê os .md existentes
- [ ] Interface web com lista de notas + visualizador markdown
- [ ] Busca por texto
- [ ] Grafo simples de conexões por `[[links]]`

### Fase 2 — IA Integrada
- [ ] Chat com as notas ("O que escrevi sobre Kant?")
- [ ] Busca semântica com ChromaDB + embeddings
- [ ] Sugestão de notas relacionadas ao abrir uma nota

### Fase 3 — Automações
- [ ] Pipeline: texto de entrada → IA categoriza → cria nota no vault correto
- [ ] Resumo automático de notas longas
- [ ] Detecção de conexões não mapeadas entre notas

---

## Pontos de Atenção

1. **Edição**: Continuar editando no Obsidian original, ou editar também no app próprio?
2. **Grafo colorido**: Replicar o estilo visual do Obsidian é a parte mais complexa
3. **Escopo inicial**: Começar pelo MVP é mais sustentável do que querer tudo de uma vez

---

## Estimativa de Complexidade

| Escopo | Complexidade |
|---|---|
| MVP (leitura + busca + chat IA) | Baixa |
| Com grafo visual | Média |
| Com automações completas | Alta |
