---
source: DATAGPT
conversation_id: 6978e36d-5600-8329-a858-dc0c3845c9b3
title: "Instalar Clawdbot Railway"
theme: IA PROMPTS
created: 2026-01-27T16:10:47.136476Z
message_count: 2
attachments_count: 0
---

# Instalar Clawdbot Railway

- Tema: `IA PROMPTS`
- Conversation ID: `6978e36d-5600-8329-a858-dc0c3845c9b3`

## Transcrição

### user

Como instalar o Clawdbot no Railway ?

### assistant

Paulo, abaixo está um **procedimento técnico padrão** para instalar o **Clawdbot no Railway**, considerando o cenário mais comum (bot Node.js hospedado em repositório GitHub). Onde houver variação possível, eu deixo explicitado.

---

## 1. Pré-requisitos

1. **Conta no Railway**  
   https://railway.app  

2. **Repositório do Clawdbot no GitHub**  
   - Público ou privado (Railway suporta ambos).
   - Verifique se o repositório contém:
     - `package.json`
     - script `"start"` ou `"dev"`
     - arquivo `.env.example` ou documentação de variáveis

3. **Credenciais usadas pelo Clawdbot**
   - Token da API que o bot consome (ex.: Discord, Telegram, WhatsApp, OpenAI etc.)
   - URLs de webhook (se houver)
   - Chaves de banco de dados (se houver)

---

## 2. Preparação do repositório

Antes do deploy, confira no repositório:

### 2.1 `package.json`
Deve conter algo como:

```json
{
  "scripts": {
    "start": "node index.js"
  }
}
```

ou

```json
{
  "scripts": {
    "start": "npm run build && node dist/index.js"
  }
}
```

O Railway **sempre executa o script `start`**.

---

### 2.2 Porta (se for HTTP)

Se o Clawdbot expõe servidor HTTP (Express, Fastify, etc.), o código deve usar:

```js
const PORT = process.env.PORT || 3000;
app.listen(PORT);
```

No Railway, **a porta é sempre injetada via `process.env.PORT`**.

---

## 3. Criar o projeto no Railway

### Passo a passo

1. Acesse o **Dashboard do Railway**
2. Clique em **New Project**
3. Escolha **Deploy from GitHub Repo**
4. Conecte sua conta GitHub (se ainda não estiver conectada)
5. Selecione o repositório do **Clawdbot**

O Railway irá:
- Detectar Node.js automaticamente
- Criar o serviço
- Iniciar o build

---

## 4. Configurar variáveis de ambiente

No painel do projeto:

1. Clique no serviço criado
2. Vá em **Variables**
3. Adicione todas as variáveis exigidas pelo Clawdbot

Exemplo típico:

```text
BOT_TOKEN=xxxxxxxx
OPENAI_API_KEY=xxxxxxxx
DATABASE_URL=xxxxxxxx
WEBHOOK_URL=xxxxxxxx
```

Se existir um `.env.example`, replique exatamente os nomes.

---

## 5. Banco de dados (se aplicável)

Se o Clawdbot usar banco:

### 5.1 Criar banco no Railway

1. No projeto, clique em **Add Plugin**
2. Escolha:
   - PostgreSQL
   - MySQL
   - Redis
3. O Railway criará automaticamente:
   - `DATABASE_URL`
   - ou variáveis específicas (`PGHOST`, `PGUSER`, etc.)

4. Ajuste o código do bot para usar essas variáveis.

---

## 6. Deploy e execução

Após configurar as variáveis:

1. Clique em **Deploy**
2. Acompanhe os logs em **View Logs**

Logs esperados:
- Instalação de dependências (`npm install`)
- Execução de `npm start`
- Mensagem de inicialização do bot

---

## 7. Webhooks e URLs públicas (se usados)

Se o Clawdbot depender de webhook:

1. Vá em **Settings → Networking**
2. Copie a **Public URL** gerada pelo Railway
3. Configure essa URL:
   - No painel da API externa (Discord, Telegram, WhatsApp etc.)
   - Ou como variável de ambiente (`WEBHOOK_URL`)

---

## 8. Problemas comuns

### Bot inicia e encerra imediatamente
- Falta de variável obrigatória
- Token inválido
- Script `start` ausente ou incorreto

### Erro de porta
- Código não usando `process.env.PORT`

### Loop de crash
- Dependência nativa incompatível
- Versão de Node incorreta

Nesse caso, fixe a versão do Node criando um arquivo:

```text
.nvmrc
```

com:

```text
18
```

ou no `package.json`:

```json
"engines": {
  "node": ">=18"
}
```

---

## 9. Checklist final

- Repositório no GitHub funcional localmente  
- Script `start` configurado  
- Variáveis de ambiente completas  
- Porta via `process.env.PORT` (se HTTP)  
- Logs limpos no Railway  

---

Se quiser, no próximo passo posso:
- Adaptar esse fluxo **exatamente** ao repositório específico do Clawdbot que você está usando  
- Analisar os logs de erro do Railway  
- Ajustar o bot para execução contínua (worker, cron ou webhook)
