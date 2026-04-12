---
source: DATAGPT
conversation_id: 6814d1ab-d644-8002-9845-d772438f58b4
title: "Erro 400 FlowiseAI"
theme: IA PROMPTS
created: 2025-05-02T14:07:40.679001Z
message_count: 2
attachments_count: 0
---

# Erro 400 FlowiseAI

- Tema: `IA PROMPTS`
- Conversation ID: `6814d1ab-d644-8002-9845-d772438f58b4`

## Transcrição

### user

No flowiseai, que tipo de erro é esse: Error buildAgentGraph - Error: 400 Invalid 'tools[0].function.name': empty string. Expected a string with minimum length 1, but got an empty string instead.

### assistant

Paulo, esse erro do FlowiseAI:

```
Error buildAgentGraph - Error: 400 Invalid 'tools[0].function.name': empty string. Expected a string with minimum length 1, but got an empty string instead.
```

indica um problema específico na construção do **grafo do agente**, relacionado a uma **função personalizada (tool/function)** mal configurada. O Flowise usa ferramentas (tools/functions) como parte dos nós do agente, e neste caso, o erro significa:

- **`tools[0].function.name` está vazio**, ou seja, o nome da função esperada no primeiro item da lista de ferramentas não foi definido.
- O sistema espera que esse campo tenha **pelo menos um caractere** (mínimo 1), mas recebeu uma string vazia (`""`), o que causa o erro 400 (requisição malformada).

### Causas comuns:

1. **Você adicionou um nó de função personalizada (Tool) sem preencher o campo “Function Name”**.
2. **Está usando um template JSON para configuração do agente e deixou o campo `name` da função em branco**.
3. **Copiou/colou um nó que perdeu dados internos durante a importação/exportação.**

### Como resolver:

1. **Verifique todos os nós do tipo "Tool"** (ou "Custom Tool", "Function Tool", etc.).
2. Clique neles e confirme se o campo **"Function Name"** (ou "Tool Name", dependendo da versão/interface) **está preenchido** com um identificador válido, como: `getUserData`, `fetchInsights`, etc.
3. Se estiver usando JSON para importar um agente, verifique no trecho correspondente:
   ```json
   "tools": [
     {
       "function": {
         "name": "aqui_deve_ter_um_nome"
       }
     }
   ]
   ```
   Preencha esse nome com uma string válida e salve novamente.

Deseja que eu analise ou corrija um trecho de JSON ou diagrama que você esteja usando?
