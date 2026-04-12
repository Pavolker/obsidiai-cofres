[[kuma]]
# Memoria do Codex

## Objetivo

Guardar o historico de trabalho feito no Codex para retomar contexto sem depender de memoria de conversa.

## Status

- atual: em construcao
- prioridade: alta
- ultima atualizacao: 2026-04-09

## Contexto

Este cofre foi criado depois de a analise mostrar que o Obsidian local precisava de uma camada propria para o trabalho no Codex.
Ele serve como memoria operacional para:

- fatos
- decisoes
- sessoes
- arquivos relevantes
- prompts uteis

## Arquivos relevantes

- `CODEX/README.md`
- `CODEX/99_Indice/Mapa do cofre.md`
- `CODEX/Bem-vindo.md`

## Fatos

- O usuario quer usar o Obsidian como organizador do trabalho no Codex
- O cofre precisa guardar memoria por projeto
- O enfoque correto e contexto util, nao transcricao integral
- O cofre `CODEX` e a memoria de trabalho local do Codex
- O modelo recomendado e por projeto, com fatos e decisoes separados
- O material deve ser resumido para facilitar recuperacao
- A gravacao em `.md` deve acontecer somente quando o usuario disser que o trabalho foi encerrado
- Durante o trabalho, manter apenas rascunhos e contexto temporario na conversa, nao consolidar a memoria final

## Decisoes

- usar o Obsidian como memoria de trabalho do Codex
- o historico de conversa sozinho nao resolve retomada de contexto
- o trabalho passa a ter memoria local e navegavel
- somente apos o encerramento declarado pelo usuario e que o conteudo deve ser consolidado nos arquivos `.md`
- antes do encerramento, nao criar gravacao final do trabalho nos arquivos do cofre

## Prompts que funcionaram

- "Crie a estrutura do cofre CODEX para memoria operacional"
- "Preencha o cofre com memoria existente do Obsidian"
- "Transforme o Obsidian em memoria de trabalho do Codex"

## Session log

- 2026-04-09: preenchida a estrutura do `CODEX` com memoria existente
- 2026-04-09: criados indice mestre e notas iniciais de projeto
- 2026-04-09: consolidado em um unico arquivo por projeto
- 2026-04-09: fixado o protocolo de gravacao apenas ao encerramento do trabalho pelo usuario
