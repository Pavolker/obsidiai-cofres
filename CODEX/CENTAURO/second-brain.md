# Second Brain

## Objetivo

Documentar a infraestrutura que conecta Obsidian e Claude Code para uso como memoria local de trabalho.

## Status

- atual: em uso como referencia
- prioridade: media
- ultima atualizacao: 2026-04-09

## Contexto

O repositorio `second-brain/` descreve uma stack de Obsidian + Claude Code com:

- vault local em Markdown
- slash commands para contexto
- scripts para processar PDFs e arquivos com Gemini
- template de `CLAUDE.md`

## Arquivos relevantes

- `second-brain/README.md`
- `second-brain/CLAUDE.md`
- `second-brain/memory.md`
- `second-brain/scripts/README.md`
- `second-brain/scripts/process_docs_to_obsidian.py`
- `second-brain/scripts/process_files_with_gemini.py`
- `second-brain/skills/vault-setup/SKILL.md`

## Fatos

- O repositorio propoe um vault com `inbox`, `daily`, `projects`, `research` e `archive`
- O setup inclui comandos `/vault-setup`, `/daily`, `/tldr` e `/file-intel`
- O fluxo usa Gemini para sintetizar arquivos externos quando desejado
- O projeto e orientado a Obsidian + Claude Code
- O foco e leitura local de arquivos e escrita de memoria no vault
- O setup original protege as notas existentes e adiciona apenas estrutura nova

## Decisoes

- usar o repo apenas como referencia de arquitetura, nao como vault principal
- adaptar a ideia ao contexto local real do usuario
- tratar o repositorio `second-brain` como template de referencia

## Prompts que funcionaram

- "Entenda a arquitetura do vault e resuma o fluxo de uso"
- "Leia o README e explique como o setup funciona"
- "Aponte o que pode ser aproveitado como memoria operacional"

## Session log

- 2026-04-09: lido o README e as instrucoes do vault setup
- 2026-04-09: identificado como base para a memoria do Codex
- 2026-04-09: consolidado em um unico arquivo por projeto

