---
source: DATAGPT
conversation_id: 67acd2c2-dd70-8002-bbfa-8ae69789dd27
title: "Enviar dados entre workflows"
theme: DADOS
created: 2025-02-12T16:56:35.522958Z
message_count: 2
attachments_count: 0
---

# Enviar dados entre workflows

- Tema: `DADOS`
- Conversation ID: `67acd2c2-dd70-8002-bbfa-8ae69789dd27`

## Transcrição

### user

Dentro do aplicativo  N8N como eu envio o resultado de um workflow para outro ?

### assistant

No N8N, você pode enviar o resultado de um workflow para outro utilizando a funcionalidade de **Call Workflow**. Isso permite que um workflow seja chamado dentro de outro, passando os dados entre eles. Para isso, siga os passos abaixo:

1. **Criar o Workflow de Origem**:
   - No seu primeiro workflow (workflow de origem), defina as etapas e os dados que você deseja enviar.
   - No final do fluxo, use um nó de saída para enviar os dados (como um **HTTP Request** ou outro tipo de nó dependendo da sua configuração).

2. **Criar o Workflow de Destino**:
   - Crie o segundo workflow (workflow de destino) que irá receber os dados.
   - O workflow de destino pode ter um nó de **Webhook** configurado para receber os dados.

3. **Chamar o Workflow de Destino**:
   - No workflow de origem, adicione um nó de **HTTP Request** (ou **Call Workflow**, dependendo da sua configuração) e configure-o para fazer uma requisição para o Webhook ou API do workflow de destino.
   - A URL de requisição será fornecida pelo Webhook do workflow de destino.

4. **Configuração do Nó de Webhook no Workflow de Destino**:
   - No workflow de destino, adicione um nó **Webhook** e configure-o para aceitar as requisições vindas do workflow de origem. Esse nó vai receber os dados e continuar o processamento no workflow de destino.

5. **Passar Dados entre os Workflows**:
   - Ao chamar o segundo workflow a partir do primeiro, você pode enviar os dados como parâmetros na requisição HTTP, usando variáveis do workflow de origem.
   - O workflow de destino pode acessar esses dados diretamente através das variáveis recebidas pelo Webhook.

### Resumo:
1. No workflow de origem, use um nó HTTP Request ou Call Workflow para fazer a chamada.
2. No workflow de destino, use um nó Webhook para receber os dados.
3. Envie as variáveis necessárias entre os workflows utilizando os parâmetros da requisição.

Essa abordagem facilita a orquestração de múltiplos workflows no N8N, promovendo uma interação entre eles e permitindo a criação de processos mais complexos e dinâmicos.
