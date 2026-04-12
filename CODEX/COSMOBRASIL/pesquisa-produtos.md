# Pesquisa Produtos

## Objetivo

Documentar a pesquisa de produtos com ACCIO e o proxy local para a API da plataforma.

## Status

- atual: documentado a partir do README
- prioridade: a definir
- ultima atualizacao: 2026-04-09

## Contexto

O README descreve uma interface de busca, proxy local para a ACCIO e uso de dados de demo quando a API nao esta configurada.

## Arquivos relevantes

- `PESQUISA PRODUTOS/README.md`
- `PESQUISA PRODUTOS/server.js`
- `PESQUISA PRODUTOS/src/`
- `PESQUISA PRODUTOS/package.json`

## Fatos

- a API da ACCIO exige configuracao via `.env`
- o sistema normaliza a resposta e pode usar dados de demonstracao

## Decisoes

- manter o contrato da API parametrizavel
- preservar o modo demo para desenvolvimento local

## Prompts que funcionaram

- "Resuma o projeto de pesquisa de produtos com ACCIO"

## Session log

- 2026-04-09: nota atualizada com base no README
