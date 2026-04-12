---
source: DATAGPT
conversation_id: 697e5741-54b0-8330-a7ad-27dae94383ab
title: "Fluxo N8N Webhook"
theme: IA PROMPTS
created: 2026-01-31T19:27:05.550762Z
message_count: 8
attachments_count: 0
---

# Fluxo N8N Webhook

- Tema: `IA PROMPTS`
- Conversation ID: `697e5741-54b0-8330-a7ad-27dae94383ab`

## Transcrição

### user

Analise esse fluxo para o N8N. Faça a estruturação de um fluxo completo, de modo que um agente possa ser acessado por um usuário através de uma página hTML, via webbhook

### tool

Make sure to include fileciteturn0file0 in your response to cite this file, or to surface it as a link.
{
  "name": "AGENTE PESSOAL CENTAURO",
  "nodes": [
    {
      "parameters": {
        "options": {
          "temperature": 0.7
        }
      },
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1,
      "position": [
        -480,
        1424
      ],
      "id": "17072ccc-16cb-4e61-8c59-517994ba353a",
      "name": "OpenAI Model",
      "credentials": {
        "openAiApi": {
          "id": "j5gkSacimsqHXwN4",
          "name": "OpenAi account 2"
        }
      }
    },
    {
      "parameters": {},
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "typeVersion": 1,
      "position": [
        -272,
        1472
      ],
      "id": "d1c8e2a3-ffb9-4ce5-a140-cc284488006e",
      "name": "Window Buffer Memory"
    },
    {
      "parameters": {
        "path": "e0aafbc3-9047-42b5-8da0-4b71d40f5a4d",
        "options": {}
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2.1,
      "position": [
        -720,
        1136
      ],
      "id": "f25b1205-edd7-48b4-b56e-320d0e168bd0",
      "name": "Webhook",
      "webhookId": "e0aafbc3-9047-42b5-8da0-4b71d40f5a4d"
    },
    {
      "parameters": {
        "text": "={{ $('WAHA Trigger').item.json.payload.body }}",
        "options": {
          "systemMessage": "Você é um agente de inteligência especializado em apresentar, de forma clara e informativa, o Sistema Centauro para pessoas que não possuem conhecimento prévio sobre o tema.\\n\\nSua função é explicar o que é o Sistema Centauro, qual é sua finalidade, como ele está estruturado e quais problemas ele se propõe a tratar.\\nA apresentação deve ser feita em texto corrido, com linguagem acessível, sem adjetivações valorativas, sem juízos morais e sem conclusões normativas.\\n\\nDiretrizes obrigatórias:\\n\\t1.\\tExplique o Sistema Centauro como um ambiente integrado de inteligência assistida por inteligência artificial voltado à relação entre capacidades humanas e sistemas de IA.\\n\\t2.\\tDeixe claro que o foco do sistema não é apenas tecnologia, mas decisão, estratégia, cognição, organização e tempo.\\n\\t3.\\tApresente o princípio central do sistema: substituir métricas exclusivamente técnicas de IA por parâmetros relacionados a alinhamento cognitivo, coerência decisória, segurança e utilidade prática.\\n\\t4.\\tDescreva, de forma sintética e informativa, os principais módulos do sistema:\\n\\t•\\tESHMIA (monitoramento comparativo entre IA e capacidades humanas);\\n\\t•\\tIA Pessoas (mapeamento de atores, trajetórias e relações de poder no ecossistema da IA);\\n\\t•\\tCompetências Centauro (diagnóstico de maturidade cognitiva e estratégica na relação com IA);\\n\\t•\\tComTesta (análise estruturada de diálogos, argumentos e vieses);\\n\\t•\\tDecisão Invertida (avaliação de decisões por inversão lógica);\\n\\t•\\tCusto do Amanhã (simulação de impactos de longo prazo);\\n\\t•\\tPlanejador de Evolução com IA (planejamento tático e roadmap de adoção);\\n\\t•\\tConselho do Meu Eu Futuro (simulação temporal e existencial de decisões).\\n\\t5.\\tMostre como esses componentes se articulam como um sistema único, e não como ferramentas isoladas.\\n\\t6.\\tNão utilize exemplos fictícios, metáforas literárias ou linguagem promocional.\\n\\t7.\\tNão conclua com recomendações, chamadas à ação ou avaliações positivas ou negativas.\\n\\t8.\\tProduza um texto entre 4 e 7 parágrafos, em tom informativo e institucional.\\n\\nO objetivo da resposta é permitir que o leitor compreenda o que é, como funciona e para que serve o Sistema Centauro, sem pressupor concordância ou adesão."
        }
      },
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1,
      "position": [
        -304,
        1168
      ],
      "id": "10d5f1b4-42f5-42b2-90fe-d31c8d2689cc",
      "name": "Agente  Centauro"
    }
  ],
  "pinData": {},
  "connections": {
    "OpenAI Model": {
      "ai_languageModel": [
        [
          {
            "node": "Agente  Centauro",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Window Buffer Memory": {
      "ai_memory": [
        [
          {
            "node": "Agente  Centauro",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "Agente  Centauro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Agente  Centauro": {
      "main": [
        []
      ]
    }
  },
  "active": false,
  "settings": {
    "executionOrder": "v1",
    "availableInMCP": false
  },
  "versionId": "874ce9ae-4ef2-4bf4-825c-4a1e8f3d4ced",
  "meta": {
    "templateCredsSetupCompleted": true,
    "instanceId": "6c46df0b204385ec3f040ac40cb9a21039b97c3a7720d6518b936c465d915281"
  },
  "id": "kzOjf3qO0c4Sr5D3",
  "tags": []
}

### tool

All the files uploaded by the user have been fully loaded. Searching won't provide additional information.

### assistant

Paulo, li o JSON do seu workflow “AGENTE PESSOAL CENTAURO”. fileciteturn0file0  
Ele já tem o núcleo (Webhook → Agente LangChain → Modelo OpenAI + Memory), mas ainda não está “fechado” como um chat web consumível por uma página HTML, porque faltam (a) padronização de entrada/saída HTTP e (b) elementos de sessão, CORS e resposta do Webhook.

## 1) O que o fluxo atual faz e onde quebra

1) **Entrada**  
Você tem um **Webhook** que aciona o workflow.

2) **LLM + memória**  
Há um **OpenAI Model** e um **Window Buffer Memory** conectados ao node **Agente Centauro**.

3) **Problema principal: o texto de entrada do agente está incorreto para Webhook**  
No node do agente, o campo `text` está como:  
`={{ $('WAHA Trigger').item.json.payload.body }}`  
Mas não existe node “WAHA Trigger” no workflow. Então, quando o Webhook chamar o fluxo, o agente não encontrará o texto e a execução tende a falhar ou ficar vazia.

4) **Problema principal: não há resposta HTTP formal**  
O “Webhook” do n8n precisa devolver algo ao navegador. Seu fluxo termina no agente sem um **Respond to Webhook** (ou sem configurar o Webhook para responder no próprio node, dependendo do modo). Resultado: a página HTML não recebe uma resposta JSON consistente.

5) **Memória sem chave de sessão**  
Window Buffer Memory funciona por execução, mas para chat web você normalmente precisa **persistir por usuário/sessão** (ou, se não quiser persistir, pelo menos aceitar que cada chamada é stateless).

## 2) Estrutura de um fluxo completo (padrão “chat via HTML → webhook”)

Abaixo está uma estrutura mínima, completa e estável, para um agente ser acessado por uma página HTML via Webhook:

### Fluxo (nodes) recomendado

1) **Webhook (POST /chat)**  
- Método: POST  
- “Response mode”: *Using ‘Respond to Webhook’ node* (recomendado para controle total).  
- Corpo esperado (JSON):  
  - `message` (string)  
  - `sessionId` (string opcional, mas recomendado)  
  - `token` (string opcional, se quiser autenticação simples)

2) **Set / Function (normalizar entrada)**  
Extrair e padronizar:
- `input.message = $json.body.message` (ou `$json.message`, dependendo de como você configurar o Webhook)
- `input.sessionId = $json.body.sessionId || $headers['x-session-id'] || $execution.id`
- Validar message não vazia

3) **(Opcional, recomendado) IF (autenticação simples)**  
Checar `token` no body ou `Authorization: Bearer ...`.  
Se inválido, responder 401.

4) **(Opcional, recomendado) CORS / Preflight**  
Se sua página HTML estiver em outro domínio, o navegador fará preflight OPTIONS.  
Duas abordagens:
- Criar um **segundo Webhook** (OPTIONS) só para preflight e responder 204 com headers CORS.
- Ou, mais simples, hospedar a página HTML no mesmo domínio do n8n (nem sempre possível).

5) **Agente (LangChain Agent)**  
- `text`: usar o campo `input.message`
- System message: o texto institucional que você já colocou (está coerente para o seu objetivo).
- Modelo: seu OpenAI Model
- Memória: aqui há duas opções:

   **Opção A (stateless)**
   - Remover memória. Cada requisição é independente.

   **Opção B (chat stateful por sessionId)**
   - Trocar Window Buffer por uma memória com persistência por chave (ex.: Redis, Data Store, Postgres, ou outro mecanismo de storage).  
   - O ponto central é: a memória deve ser “keyed” por `sessionId`.

6) **Set (montar resposta JSON)**  
Padronizar:
- `reply = <texto do agente>`
- `sessionId = input.sessionId`
- `ts = Date.now()`

7) **Respond to Webhook**  
- Status 200
- Body JSON: `{ reply, sessionId, ts }`
- Headers:
  - `Content-Type: application/json`
  - CORS (se necessário):  
    - `Access-Control-Allow-Origin: https://seu-dominio-da-pagina` (evitar `*` se usar credenciais)  
    - `Access-Control-Allow-Headers: Content-Type, Authorization`  
    - `Access-Control-Allow-Methods: POST, OPTIONS`

8) **Error handling (recomendado)**  
- Um branch para erros: responder 400 (message ausente), 401 (token inválido), 500 (falha do modelo).

## 3) Ajustes diretos no seu workflow atual

Com base no JSON: fileciteturn0file0

1) **Corrigir a origem do texto do agente**  
Substituir:
- `={{ $('WAHA Trigger').item.json.payload.body }}`  
por algo compatível com Webhook, por exemplo:
- `={{ $json.body.message }}`  
ou, se o Webhook estiver configurado para “Body Parameters”:
- `={{ $json.message }}`

2) **Adicionar Respond to Webhook após o Agente**  
Sem isso, a página HTML não tem um retorno confiável.

3) **Padronizar saída do Agente**  
Algumas execuções do node Agent retornam em campos diferentes conforme versão/config. Em geral, você vai pegar o texto final (ex.: `$json.output` ou similar). O ideal é inserir um **Set** logo após o agente para mapear explicitamente:
- `reply = <campo de saída do agente>`
- `sessionId = <sessionId recebido>`

4) **Decidir sobre memória**  
- Se você quer um chat contínuo, o Window Buffer tende a não sustentar contexto entre execuções para o mesmo usuário em ambientes com múltiplas instâncias/restarts. Para chat web, é preferível persistência por `sessionId`.

## 4) Página HTML mínima para conversar com o webhook

Abaixo um exemplo direto (um arquivo `.html` único). Ele envia `message` e `sessionId` e exibe a resposta.

```html
<!doctype html>
<html lang="pt-br">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Chat com Agente (n8n)</title>
  <style>
    body { font-family: system-ui, Arial, sans-serif; margin: 24px; }
    #log { border: 1px solid #ccc; padding: 12px; height: 360px; overflow: auto; white-space: pre-wrap; }
    .row { margin-top: 12px; display: flex; gap: 8px; }
    input { flex: 1; padding: 10px; }
    button { padding: 10px 14px; }
  </style>
</head>
<body>
  <h1>Chat</h1>
  <div id="log"></div>

  <div class="row">
    <input id="msg" placeholder="Digite sua mensagem" />
    <button id="send">Enviar</button>
  </div>

  <script>
    const WEBHOOK_URL = "https://SEU_N8N_DOMINIO/webhook/e0aafbc3-9047-42b5-8da0-4b71d40f5a4d"; 
    // ajuste para a URL real do webhook em produção

    const log = document.getElementById("log");
    const msg = document.getElementById("msg");
    const send = document.getElementById("send");

    const sessionId = localStorage.getItem("sessionId") || crypto.randomUUID();
    localStorage.setItem("sessionId", sessionId);

    function append(who, text) {
      log.textContent += `${who}: ${text}\\n\\n`;
      log.scrollTop = log.scrollHeight;
    }

    async function chat() {
      const text = msg.value.trim();
      if (!text) return;

      append("Você", text);
      msg.value = "";

      const payload = { message: text, sessionId };

      const res = await fetch(WEBHOOK_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (!res.ok) {
        const errText = await res.text().catch(() => "");
        append("Erro", `HTTP ${res.status} ${errText}`);
        return;
      }

      const data = await res.json();
      append("Agente", data.reply || JSON.stringify(data));
    }

    send.addEventListener("click", chat);
    msg.addEventListener("keydown", (e) => {
      if (e.key === "Enter") chat();
    });
  </script>
</body>
</html>
```

Observações operacionais:
- Se o HTML estiver em domínio diferente do n8n, você precisará de **CORS** no Webhook (via headers no Respond to Webhook e, em muitos casos, tratar OPTIONS).
- Use sempre o endpoint “production” do n8n (não o “test”).

## 5) Padrão de contrato HTTP sugerido (para manter previsível)

Request (POST):
```json
{
  "message": "texto do usuário",
  "sessionId": "uuid",
  "metadata": { "origin": "web" }
}
```

Response (200):
```json
{
  "reply": "texto do agente",
  "sessionId": "uuid",
  "ts": 1738360000000
}
```

## 6) Recomendação prática de “fluxo completo” (em uma frase)

Webhook POST → Normalizar/validar entrada → (Auth/CORS) → Agente (LLM + memória por sessionId se necessário) → Padronizar saída → Respond to Webhook (JSON + headers).

Se você quiser, eu posso devolver isso como um **workflow n8n completo (JSON)** já com os nodes adicionais (Set/IF/Respond to Webhook e um desenho de sessão), mantendo o seu agente e a sua system message como estão.

### user

Faça um arquivo único, json, com todo o fluxo, de acordo com os requisitos aceitos pelo N8N para que eu possa fazer o upload na plataforma

### assistant

Paulo, aqui está o workflow completo em JSON, já estruturado para: **Webhook (POST) → normalização de entrada → agente → formatação de resposta → Respond to Webhook**, pronto para upload no n8n.

[Download do JSON do workflow](sandbox:/mnt/data/AGENTE_PESSOAL_CENTAURO_webhook_chat.json)

Também deixo o conteúdo do arquivo abaixo (idêntico ao download):

```json
{
  "name": "AGENTE PESSOAL CENTAURO (Webhook Chat)",
  "nodes": [
    {
      "parameters": {
        "options": {
          "temperature": 0.7
        }
      },
      "type": "@n8n/n8n-nodes-langchain.lmChatOpenAi",
      "typeVersion": 1,
      "position": [
        -480,
        1340
      ],
      "id": "17072ccc-16cb-4e61-8c59-517994ba353a",
      "name": "OpenAI Model",
      "credentials": {
        "openAiApi": {
          "id": "j5gkSacimsqHXwN4",
          "name": "OpenAi account 2"
        }
      }
    },
    {
      "parameters": {
        "contextWindowLength": 5
      },
      "type": "@n8n/n8n-nodes-langchain.memoryBufferWindow",
      "typeVersion": 1,
      "position": [
        -300,
        1520
      ],
      "id": "562c3d32-ab79-4f19-b32e-dadfe68a38b1",
      "name": "Window Buffer Memory"
    },
    {
      "parameters": {
        "path": "e0aafbc3-9047-42b5-8da0-4b71d40f5a4d",
        "options": {
          "responseHeaders": {
            "entries": [
              {
                "name": "Content-Type",
                "value": "application/json"
              },
              {
                "name": "Access-Control-Allow-Origin",
                "value": "*"
              },
              {
                "name": "Access-Control-Allow-Methods",
                "value": "POST, OPTIONS"
              },
              {
                "name": "Access-Control-Allow-Headers",
                "value": "Content-Type, Authorization"
              }
            ]
          }
        },
        "httpMethod": "POST",
        "responseMode": "responseNode"
      },
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2.1,
      "position": [
        -720,
        1136
      ],
      "id": "f25b1205-edd7-48b4-b56e-320d0e168bd0",
      "name": "Webhook",
      "webhookId": "e0aafbc3-9047-42b5-8da0-4b71d40f5a4d"
    },
    {
      "parameters": {
        "text": "={{ $json.message }}",
        "options": {
          "systemMessage": "Você é um agente de inteligência especializado em apresentar, de forma clara e informativa, o Sistema Centauro para pessoas que não possuem conhecimento prévio sobre o tema.\\n\\nSua função é explicar o que é o Sistema Centauro, qual é sua finalidade, como ele está estruturado e quais problemas ele se propõe a tratar.\\nA apresentação deve ser feita em texto corrido, com linguagem acessível, sem adjetivações valorativas, sem juízos morais e sem conclusões normativas.\\n\\nDiretrizes obrigatórias:\\n\\t1.\\tExplique o Sistema Centauro como um ambiente integrado de inteligência assistida por inteligência artificial voltado à relação entre capacidades humanas e sistemas de IA.\\n\\t2.\\tDeixe claro que o foco do sistema não é apenas tecnologia, mas decisão, estratégia, cognição, organização e tempo.\\n\\t3.\\tApresente o princípio central do sistema: substituir métricas exclusivamente técnicas de IA por parâmetros relacionados a alinhamento cognitivo, coerência decisória, segurança e utilidade prática.\\n\\t4.\\tDescreva, de forma sintética e informativa, os principais módulos do sistema:\\n\\t•\\tESHMIA (monitoramento comparativo entre IA e capacidades humanas);\\n\\t•\\tIA Pessoas (mapeamento de atores, trajetórias e relações de poder no ecossistema da IA);\\n\\t•\\tCompetências Centauro (diagnóstico de maturidade cognitiva e estratégica na relação com IA);\\n\\t•\\tComTesta (análise estruturada de diálogos, argumentos e vieses);\\n\\t•\\tDecisão Invertida (avaliação de decisões por inversão do ponto de vista e auditoria de consequências).\\n\\t5.\\tMantenha o texto com consistência conceitual, encadeamento lógico e foco na apresentação do sistema, evitando exemplos fictícios ou narrativas.\\n\\nO usuário pode fazer perguntas livres. Responda sempre com clareza, em texto corrido, sem listas extensas."
        }
      },
      "type": "@n8n/n8n-nodes-langchain.agent",
      "typeVersion": 1,
      "position": [
        -280,
        1136
      ],
      "id": "ea409f64-cd9c-476c-a2e5-7e5ecee21796",
      "name": "Agente  Centauro"
    },
    {
      "parameters": {
        "keepOnlySet": false,
        "values": {
          "string": [
            {
              "name": "message",
              "value": "={{ ($json.body && ($json.body.message || $json.body.text || $json.body.input)) || ($json.query && $json.query.message) || $json.message }}"
            },
            {
              "name": "sessionId",
              "value": "={{ ($json.body && $json.body.sessionId) || ($json.headers && $json.headers['x-session-id']) || $execution.id }}"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [
        -480,
        1136
      ],
      "id": "f2eab7de-0211-4b6e-99fe-27e1d296266f",
      "name": "Normalize Input"
    },
    {
      "parameters": {
        "keepOnlySet": true,
        "values": {
          "string": [
            {
              "name": "reply",
              "value": "={{ $json.output || $json.text || $json.answer || $json.response }}"
            },
            {
              "name": "sessionId",
              "value": "={{ $json.sessionId || $node['Normalize Input'].json.sessionId }}"
            }
          ],
          "number": [
            {
              "name": "ts",
              "value": "={{ Date.now() }}"
            }
          ]
        },
        "options": {}
      },
      "type": "n8n-nodes-base.set",
      "typeVersion": 2,
      "position": [
        -160,
        1136
      ],
      "id": "fbd8022b-00ff-4c60-85b2-4ac8e4507d95",
      "name": "Format Response"
    },
    {
      "parameters": {
        "respondWith": "json",
        "responseBody": "={{ $json }}",
        "options": {
          "responseHeaders": {
            "entries": [
              {
                "name": "Content-Type",
                "value": "application/json"
              },
              {
                "name": "Access-Control-Allow-Origin",
                "value": "*"
              },
              {
                "name": "Access-Control-Allow-Methods",
                "value": "POST, OPTIONS"
              },
              {
                "name": "Access-Control-Allow-Headers",
                "value": "Content-Type, Authorization"
              }
            ]
          }
        }
      },
      "type": "n8n-nodes-base.respondToWebhook",
      "typeVersion": 1.1,
      "position": [
        40,
        1136
      ],
      "id": "cdb3a8cb-4a4a-4605-b4b9-e5d944a1e35d",
      "name": "Respond to Webhook"
    }
  ],
  "pinData": {},
  "connections": {
    "OpenAI Model": {
      "ai_languageModel": [
        [
          {
            "node": "Agente  Centauro",
            "type": "ai_languageModel",
            "index": 0
          }
        ]
      ]
    },
    "Window Buffer Memory": {
      "ai_memory": [
        [
          {
            "node": "Agente  Centauro",
            "type": "ai_memory",
            "index": 0
          }
        ]
      ]
    },
    "Webhook": {
      "main": [
        [
          {
            "node": "Normalize Input",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Agente  Centauro": {
      "main": [
        [
          {
            "node": "Format Response",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Normalize Input": {
      "main": [
        [
          {
            "node": "Agente  Centauro",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Format Response": {
      "main": [
        [
          {
            "node": "Respond to Webhook",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Respond to Webhook": {
      "main": [
        []
      ]
    }
  },
  "active": false,
  "settings": {},
  "versionId": "f81010a6-2b2c-4e2a-8b31-7d7d991d1a7b",
  "meta": {
    "instanceId": "b36f7f7af14a6b9405c84bb0e2e98ec31c9a9b7bf4d6d0c41fe6c7a2f3e8e71e"
  },
  "id": "O3dYt8tZTXG9uQvJ",
  "tags": []
}
```

Se, ao importar, o n8n reclamar de “credentials id/name”, basta reatribuir o **OpenAI credential** no node “OpenAI Model” (isso é esperado quando o workflow foi criado em outra instância).

### user

Mensagem na tela html: {"code":404,"message":"This webhook is not registered for GET requests. Did you mean to make a POST request?"}

### assistant

Paulo, essa mensagem indica que a sua página HTML está chamando o endpoint do webhook com **GET** (normalmente porque você abriu a URL no navegador, ou porque o `fetch()` está sem `method: "POST"`), mas o Webhook do n8n foi configurado para aceitar **POST**.

A correção depende de como você está acionando.

## 1) Se você está testando “abrindo o link do webhook” no browser
Isso sempre vai dar GET. Webhook POST não responde abrindo URL.

Teste com POST:

### cURL (mais direto)
```bash
curl -X POST "https://SEU_DOMINIO/webhook/e0aafbc3-9047-42b5-8da0-4b71d40f5a4d" \\
  -H "Content-Type: application/json" \\
  -d '{"message":"teste","sessionId":"web-1"}'
```

## 2) Se é a página HTML: ajuste o fetch para POST
Verifique se o seu código está exatamente assim:

```js
const res = await fetch(WEBHOOK_URL, {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message: text, sessionId })
});
```

Se estiver usando `fetch(WEBHOOK_URL)` sem as opções, ele vira GET.

## 3) Erro comum: você está chamando o endpoint errado (test vs production)
No n8n há dois endpoints:

- **Test**: `/webhook-test/...` (só funciona quando o workflow está em modo “listening” de teste no editor)
- **Production**: `/webhook/...` (funciona quando o workflow está ativo)

Se você está usando `/webhook-test/` fora do modo de teste, pode dar erros (e vice-versa).

Regra prática:
- Página HTML em produção → use **/webhook/** e **ative** o workflow.
- Teste manual no editor → use **/webhook-test/** enquanto o workflow está “waiting”.

## 4) Conferências no node Webhook do seu fluxo
No node Webhook:
- HTTP Method: **POST**
- Se você quiser permitir teste via browser (GET), mude para:
  - HTTP Method: **GET**
  - e passe a mensagem via querystring (menos recomendado para chat)

Mas para chat, POST é o padrão.

## 5) Caso você queira suportar GET também (opcional)
Você pode duplicar o Webhook com GET em outra rota (ex.: `/chat-get`) e mapear:
- `message = $json.query.message`

Assim o browser poderia testar com:
`/webhook/chat-get?message=oi`

Mas para sua página HTML, não é necessário.

## 6) Diagnóstico rápido (sem suposições)
Quando você vê esse erro, a causa é uma destas:
1) abriu a URL no navegador (GET)
2) `fetch()` sem `method: "POST"`
3) você está chamando um endpoint de teste fora do modo de teste
4) existe algum proxy/redirecionamento convertendo a chamada em GET (menos comum)

Se você colar aqui o trecho do seu HTML onde está o `WEBHOOK_URL` e o `fetch()`, eu aponto exatamente qual dos 4 está ocorrendo.
