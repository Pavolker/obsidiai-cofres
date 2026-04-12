# Sapientia

## Objetivo

Documentar o MVP do Sapientia e sua primeira implementacao pratica.

## Status

- atual: documentado a partir do README
- prioridade: a definir
- ultima atualizacao: 2026-04-09

## Contexto

O README do app descreve uma pagina unica com backend Node, seis cards progressivos, persistencia opcional no Postgres e proximo passo de orquestracao via Symphony.

## Arquivos relevantes

- `SAPIENTIA/app/README.md`
- `SAPIENTIA/BACKEND-AGENTS.md`
- `SAPIENTIA/CONCEPT-V1.md`
- `SAPIENTIA/PROTOCOLO-SAPIENTIA.md`
- `SAPIENTIA/PRODUCTION-ARCHITECTURE.md`

## Fatos

- o app gera uma pagina unica a partir de um tema
- existe fallback local quando a IA nao esta disponivel
- o proximo passo e integrar ao Symphony

## Decisoes

- manter o MVP simples e incrementavel
- preservar o contrato `POST /api/compositions` como base

## Prompts que funcionaram

- "Resuma o MVP do Sapientia e os proximos passos"

## Session log

- 2026-04-09: nota atualizada com base no README
