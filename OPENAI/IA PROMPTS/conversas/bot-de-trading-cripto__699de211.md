---
source: DATAGPT
conversation_id: 699de211-dc50-8333-b3d2-d95b51dcf1bc
title: "Bot de Trading Cripto"
theme: IA PROMPTS
created: 2026-02-24T17:38:51.661492Z
message_count: 2
attachments_count: 0
---

# Bot de Trading Cripto

- Tema: `IA PROMPTS`
- Conversation ID: `699de211-dc50-8333-b3d2-d95b51dcf1bc`

## Transcrição

### user

Faça um prompt  para a criação de um bots de trading de criptomoedas  com capacidade  para executar estratégias de negociação em conecção  com  a corretoras (exchanges)  Binance, por meio de APIs de modo a poder  monitorar o mercado e enviar ordens de compra e venda sem intervenção manual contínua.

### assistant

Paulo, segue um **prompt completo** (pronto para colar) para um agente de IA criar um bot de trading de cripto na Binance via API, com monitoramento de mercado e envio de ordens com mínimo de intervenção manual.

```text
Você é um agente desenvolvedor sênior de sistemas de trading algorítmico para criptoativos, com experiência em:
- APIs de exchanges (especialmente Binance: Spot e, opcionalmente, Futures)
- Arquitetura de sistemas em tempo real (WebSocket + REST)
- Gestão de risco, execução de ordens, monitoramento e observabilidade
- Segurança de credenciais e boas práticas de engenharia

OBJETIVO
Construir um bot de trading automatizado que:
1) Conecte-se à Binance por API para ler dados de mercado e enviar ordens
2) Execute estratégias de negociação parametrizáveis (regras claras de entrada/saída)
3) Monitore posições/ordens continuamente e reaja a eventos do mercado
4) Tenha operação segura: logs, validações, limites, tratamento de falhas
5) Seja operável com pouca intervenção manual (painel/CLI de controle e configuração)

RESTRIÇÕES E PRINCÍPIOS
- Não prometer performance ou retornos.
- Separar claramente: dados (market data), sinais (strategy), risco (risk), execução (execution), persistência (storage), monitoramento (observability).
- Implementar modo PAPER TRADING / SIMULAÇÃO primeiro (sem enviar ordens reais), e só depois habilitar modo REAL.
- Garantir segurança: credenciais fora do código (ENV/Secrets), permissões mínimas, rotação, e sem registrar chaves nos logs.
- Respeitar limites de taxa (rate limits) e implementar backoff/retry.
- Implementar validações para evitar ordens fora de parâmetros.

ESCOPO FUNCIONAL (MVP)
A. Conectividade e Dados
- Consumir preços e candles via WebSocket (tickers e klines) e REST quando necessário.
- Sincronizar relógio com servidor (timestamp/recvWindow).
- Manter um cache local do estado: últimas cotações, candles, spreads, volatilidade simples.

B. Estratégias (mínimo 2, parametrizáveis)
1) Tendência: cruzamento de médias (EMA curta vs EMA longa) em timeframe configurável.
2) Reversão: RSI com gatilhos de sobrecompra/sobrevenda e confirmação simples.
Cada estratégia deve produzir sinais padronizados: BUY/SELL/HOLD com “confidence” e motivo textual.

C. Gestão de Risco (obrigatória)
- Tamanho da posição por regra (ex: % do saldo, ou risco fixo por trade).
- Stop-loss e take-profit (fixo e/ou baseado em ATR simples).
- Limite diário de perdas (circuit breaker).
- Limite de trades por período e bloqueio por alta volatilidade (configurável).
- Verificação de saldo/margem e “max exposure” por ativo.
- Slippage e taxas: estimar impacto para validar se trade faz sentido.

D. Execução de Ordens
- Criar ordens de mercado e limite (MVP: mercado + limite).
- Confirmar execução (fills) e lidar com ordens parciais.
- Cancelar/atualizar ordens conforme regras.
- Idempotência: evitar duplicação em caso de retry.
- Modo REAL só com “chave” de habilitação explícita e checklist de segurança.

E. Persistência e Auditoria
- Registrar: sinais gerados, ordens enviadas, fills, PnL, erros, decisões de risco.
- Usar um armazenamento simples no MVP (SQLite) com esquema bem definido.
- Possibilitar exportação CSV de trades e métricas.

F. Operação e Observabilidade
- Logs estruturados (níveis INFO/WARN/ERROR).
- Métricas básicas: trades/dia, win rate, PnL, drawdown, latência de execução, reconexões.
- Alertas (MVP: console e arquivo; opcional: webhook/Telegram/Email).
- Watchdog de conexão e reconexão automática WebSocket.

G. Interface de Controle (MVP)
- CLI com comandos: iniciar, pausar, status, trocar estratégia, alterar parâmetros, ver métricas, exportar.
- Arquivo de configuração (YAML/JSON) para: ativos, timeframe, parâmetros de estratégia, risco, modo (paper/real).

REQUISITOS TÉCNICOS
- Linguagem: Python (preferencial) ou Node.js (se justificar). Escolha uma e seja consistente.
- Bibliotecas sugeridas (Python): websockets, requests/httpx, pandas/numpy (opcional), pydantic, sqlite3, loguru (ou logging padrão).
- Encapsular Binance API via cliente (pode usar biblioteca oficial/ccxt se justificar; documentar decisões).
- Código organizado em módulos:
  /config
  /data
  /strategy
  /risk
  /execution
  /storage
  /monitoring
  main.py (ou equivalente)
- Testes mínimos:
  - unit tests para cálculo de indicadores e regras de estratégia
  - testes de “dry-run” para geração e validação de ordens
  - simulação em dados históricos (backtest simplificado) antes do paper trading online

ENTREGÁVEIS
1) Arquitetura: diagrama textual dos módulos e fluxo de dados.
2) Especificação de configuração (exemplo de arquivo YAML/JSON).
3) Implementação do MVP completa e executável:
   - Paper trading funcionando
   - Estratégias implementadas
   - Risk manager funcionando
   - Executor com Binance (paper: simulado; real: pronto mas desabilitado por padrão)
4) Guia de uso:
   - Como obter e configurar API keys na Binance (sem imagens, só passos)
   - Como rodar em modo paper e como habilitar modo real com segurança
   - Como interpretar logs, métricas e exportações
5) Checklist de segurança e operação (antes de colocar em real)
6) Limitações conhecidas do MVP + backlog priorizado (próximas melhorias)

CRITÉRIOS DE QUALIDADE
- Robustez a falhas de rede e reconexão
- Sem credenciais no código
- Sem ordens fora de limite (quantidade/preço)
- “Fail safe”: ao detectar condição anômala, o bot pausa e registra motivo
- Código legível, documentado e com exemplos de configuração

COMECE AGORA
1) Apresente a arquitetura e o plano de implementação em etapas.
2) Em seguida, gere o código do MVP (com comentários).
3) Inclua um exemplo de configuração e comandos da CLI.
4) Inclua um modo de simulação local (paper) por padrão.
```

Se você quiser, eu também posso te entregar uma segunda versão do prompt voltada para “produção” (segurança, contêiner Docker, execução em VPS, observabilidade com Prometheus/Grafana, segregação de chaves, e modo multi-estratégia), mantendo o mesmo padrão de neutralidade e sem suposições de performance.
