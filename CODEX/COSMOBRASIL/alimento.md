# Alimento

## Objetivo

Documentar o gerador Radar Foresight para inteligencia territorial a partir de CSV do EmpresaAqui.

## Status

- atual: documentado a partir do README
- prioridade: a definir
- ultima atualizacao: 2026-04-09

## Contexto

O README do subdiretorio `RADAR INTELIGENCIA` descreve um gerador em Streamlit que produz HTML pronto para Netlify.

## Arquivos relevantes

- `ALIMENTO/RADAR INTELIGENCIA/README.md`
- `ALIMENTO/RADAR INTELIGENCIA/core/pipeline.py`
- `ALIMENTO/RADAR INTELIGENCIA/core/generator.py`
- `ALIMENTO/RADAR INTELIGENCIA/app.py`

## Fatos

- o fluxo usa CSV do EmpresaAqui como entrada
- o resultado e uma pagina HTML autocontida para publicacao

## Decisoes

- manter a entrada CSV e a saida HTML separadas
- preservar os pesos de score configuraveis na interface

## Prompts que funcionaram

- "Resuma o Radar Foresight e seu fluxo principal"

## Session log

- 2026-04-09: nota atualizada com base no README
