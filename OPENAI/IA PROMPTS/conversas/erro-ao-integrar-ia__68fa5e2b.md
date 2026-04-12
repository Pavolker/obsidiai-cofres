---
source: DATAGPT
conversation_id: 68fa5e2b-d5b8-8330-91a4-97c9dbff5b0e
title: "Erro ao integrar IA"
theme: IA PROMPTS
created: 2025-10-23T16:56:14.588827Z
message_count: 2
attachments_count: 0
---

# Erro ao integrar IA

- Tema: `IA PROMPTS`
- Conversation ID: `68fa5e2b-d5b8-8330-91a4-97c9dbff5b0e`

## Transcrição

### user

Eu desenvolvo um agente de IA com a Openai. Recebo o código Python para fazer a integração  (from openai import OpenAI
client = OpenAI()

response = client.responses.create(
  prompt={
    "id": "pmpt_68e8ddfb6f2c819698437482babb66660e95b7f3ea012e56",
    "version": "3"
  }
) ), entretanto não consigo colocar esse agente em uma página HTML de modo que um usuário possa usar o agente. Qual é o erro que estou cometendo ?

### assistant

Paulo, o “erro” não é do agente em si — é de **arquitetura**. Esse trecho em Python usa a API da OpenAI no **backend**. Tentar “colocar” isso direto numa página HTML implica dois problemas típicos:

1) **Código e chave no cliente (navegador)**  
Não é seguro chamar a API da OpenAI direto do browser porque você exporia sua chave. A prática recomendada é ter **um endpoint de servidor** que chama a OpenAI e a sua página HTML apenas **faz requisições** a esse endpoint. Isso está alinhado com a documentação da OpenAI (usar SDK/REST no servidor; streaming opcional para o cliente). citeturn5search10turn5search0turn5search1

2) **Contrato correto da Responses API**  
Na Responses API, a chamada padrão usa `input` (ou itens de input) e pode incluir **prompts armazenados** (ex.: `pmpt_...`) como item do input. Se você enviar estruturas que o endpoint não espera (por exemplo, um campo `prompt` no lugar errado), a API responde erro. Verifique o formato da sua chamada de acordo com a referência da **Responses API** e, se for usar prompt salvo, faça-o via **input items**. citeturn5search2turn5search0

---

## Como publicar seu agente numa página HTML (padrão mínimo)

### 1) Backend (Python + FastAPI) — chama a OpenAI
```python
# server.py
from fastapi import FastAPI, Body
from fastapi.responses import StreamingResponse
from openai import OpenAI
import asyncio

app = FastAPI()
client = OpenAI()  # usa OPENAI_API_KEY do ambiente

@app.post("/api/respond")
async def respond(payload: dict = Body(...)):
    user_text = payload.get("input", "")

    # Exemplo A: usando prompt armazenado (pmpt_...) como item do input
    # e adicionando a fala do usuário em seguida
    stream = client.responses.stream(
        # modelos atuais na Responses API; ajuste conforme seu plano/modelo
        model="gpt-4.1-mini",
        input=[
            {"type": "prompt", "id": "pmpt_68e8ddfb6f2c819698437482babb66660e95b7f3ea012e56", "version": "3"},
            {"role": "user", "content": user_text}
        ]
    )

    async def generator():
        with stream as s:
            for event in s:
                if event.type == "response.output_text.delta":
                    yield event.delta  # envia pedaços de texto
                elif event.type == "response.completed":
                    break
                # (trate outros eventos se necessário)
            s.close()

    return StreamingResponse(generator(), media_type="text/plain")
```
Pontos-chave:
- Mantém a **chave** só no servidor.  
- Usa **Responses Streaming** para experiência “digitando”. citeturn5search5turn5search3

### 2) Frontend (HTML + JS) — consome seu endpoint
```html
<!doctype html>
<html>
  <body>
    <textarea id="q" placeholder="Digite sua pergunta"></textarea>
    <button id="go">Enviar</button>
    <pre id="out"></pre>

    <script>
      document.getElementById("go").onclick = async () => {
        const q = document.getElementById("q").value;
        const res = await fetch("/api/respond", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({ input: q })
        });

        const reader = res.body.getReader();
        const decoder = new TextDecoder();
        const out = document.getElementById("out");
        out.textContent = "";
        while (true) {
          const {value, done} = await reader.read();
          if (done) break;
          out.textContent += decoder.decode(value, {stream: true});
        }
      };
    </script>
  </body>
</html>
```

---

## Checklist de integração correta
- **Servidor obrigatório**: nunca exponha `OPENAI_API_KEY` no cliente. citeturn5search10  
- **Endpoint próprio**: `/api/respond` recebe o input do usuário e chama a **Responses API** no servidor. citeturn5search2  
- **Streaming** (opcional, recomendado): use o fluxo de eventos da Responses API para enviar **deltas** ao cliente. citeturn5search5  
- **Prompt armazenado (pmpt_)**: se usar prompts versionados, inclua como **item de input**; mantenha a versão se quiser reprodutibilidade. citeturn5search2  
- **CORS/Deploy**: se frontend e backend estiverem em origens diferentes, habilite CORS no servidor.  
- **Modelo**: escolha um modelo suportado pela Responses API (ex.: família GPT-4.1/mini) e ajuste parâmetros no backend. citeturn5search0

---

## Por que seu código não “entra” na página HTML
- O trecho `from openai import OpenAI ... client.responses.create(...)` é **Python de servidor**. Em HTML/JS puro no navegador isso **não roda** e **quebraria a segurança**.  
- A página HTML deve apenas **enviar** o texto do usuário para o seu endpoint; o servidor é quem **executa** a chamada à OpenAI e **devolve** o resultado (idealmente em streaming). citeturn5search10turn5search1

Se quiser, adapto o exemplo para Flask, Next.js (API Routes), Node/Express, ou insiro variáveis do seu prompt `pmpt_...` conforme o formato de **input items** da Responses API. citeturn5search2
