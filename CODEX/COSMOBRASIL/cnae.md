# CNAE

## Objetivo

Documentar o Radar CNAECIR, que cruza bases CNAE, CNAECIR e EABR para gerar diagnosticos territoriais de circularidade.

## Status

- atual: documentado a partir do README
- prioridade: a definir
- ultima atualizacao: 2026-04-09

## Contexto

O README descreve um pipeline que normaliza dados, marca CNAECIR por empresa, calcula indicadores e gera saidas para dashboard.

## Arquivos relevantes

- `CNAE/README.md`
- `config/territories.json`
- `scripts/build_dashboard_data.py`
- `app/data/territories.json`
- `outputs/territories/<slug>/summary.json`

## Fatos

- o projeto responde perguntas sobre circularidade de um territorio
- as entradas principais sao `CNAE2026.csv`, `CNAECIR.csv` e arquivos territoriais EABR
- o fluxo gera dashboard HTML e resumos analiticos por territorio

## Decisoes

- manter o pipeline como memoria operacional do projeto
- tratar o diagnostico territorial como saida central

## Prompts que funcionaram

- "Resuma o objetivo do Radar CNAECIR e os arquivos de operacao"

## Session log

- 2026-04-09: nota atualizada com base no README
