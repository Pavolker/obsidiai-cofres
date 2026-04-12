# Botcripto

## Objetivo

Documentar o CryptoAlgoBot para Binance e seus controles de risco.

## Status

- atual: documentado a partir do README
- prioridade: a definir
- ultima atualizacao: 2026-04-09

## Contexto

O README detalha configuracao de API Binance, variaveis de ambiente, modo paper trading, estrategia e dashboard React.

## Arquivos relevantes

- `BOTCRIPTO/README.md`
- `BOTCRIPTO/server.ts`
- `BOTCRIPTO/src/`
- `BOTCRIPTO/vite.config.ts`
- `BOTCRIPTO/trading_bot.db`

## Fatos

- o bot inicia em paper trading por padrao
- a estrategia usa EMA, RSI, ATR e filtros de volume
- a seguranca das chaves e um ponto importante

## Decisoes

- manter a simulacao como padrao
- evitar expor credenciais no codigo

## Prompts que funcionaram

- "Resuma o bot de trading e os pontos de risco"

## Session log

- 2026-04-09: nota atualizada com base no README
