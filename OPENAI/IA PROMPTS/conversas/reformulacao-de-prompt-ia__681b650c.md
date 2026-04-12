---
source: DATAGPT
conversation_id: 681b650c-c700-8002-b979-5b5d650ca897
title: "Reformulação de prompt IA"
theme: IA PROMPTS
created: 2025-05-07T13:50:05.361113Z
message_count: 12
attachments_count: 0
---

# Reformulação de prompt IA

- Tema: `IA PROMPTS`
- Conversation ID: `681b650c-c700-8002-b979-5b5d650ca897`

## Transcrição

### user

sse é um prompt básico de um agente de ia que deverá responder a partir de um documento:

"

Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.

Chat History:
{chat_history}
Follow Up Input: {question}
Standalone Question:

"

Refaça esse prompt, para ele acessar o documento disponível e respoder as perguntas do usuário

### assistant

Claro, Paulo. Segue a reformulação do prompt, com foco em um agente de IA que acessa um **documento de referência** para responder diretamente às perguntas do usuário, garantindo que ele interprete o conteúdo de forma contextualizada:

---

**Prompt reformulado para agente de IA baseado em documento:**

> You are an intelligent assistant with access to the following document:
> 
> **Document Content:**  
> {document_content}
> 
> Your task is to accurately answer user questions based on the content of this document. If the question requires clarification, rephrase it to make it standalone and specific. Always ensure your response is grounded in the document.
> 
> **User Question:**  
> {question}
> 
> **Answer based on the document:**

---

Se quiser, posso adaptar esse mesmo prompt para múltiplos documentos, perguntas em cadeia ou integração com histórico de conversa. Deseja ampliar o modelo para esses casos?

### user

Reescreva o prompt em português e coloque como instrução que ele deve responder em português do Brasil

### assistant

Claro, Paulo. Segue o prompt reescrito em **português do Brasil**, com instruções claras para que o agente responda exclusivamente nesse idioma:

---

**Prompt em português para agente de IA com base em documento:**

> Você é um assistente inteligente com acesso ao seguinte documento:
> 
> **Conteúdo do Documento:**  
> {documento}
> 
> Sua tarefa é responder com precisão às perguntas do usuário com base exclusivamente no conteúdo deste documento. Caso a pergunta esteja vaga ou dependa de contexto implícito, reformule-a para torná-la autônoma e específica. Suas respostas devem ser sempre fundamentadas no documento.
> 
> **Importante:** Responda sempre em português do Brasil, com linguagem clara, objetiva e adequada ao tema tratado.
> 
> **Pergunta do Usuário:**  
> {pergunta}
> 
> **Resposta com base no documento:**

---

Deseja incluir algum padrão de estilo (ex: resposta em tópicos, síntese inicial, citação direta do documento) nas instruções do agente?

### user

Faça o mesmo trabalho com "response prompt":  " I want you to act as a document that I am having a conversation with. Your name is "AI Assistant". Using the provided context, answer the user's question to the best of your ability using the resources provided.
If there is nothing in the context relevant to the question at hand, just say "Hmm, I'm not sure" and stop after that. Refuse to answer any question not about the info. Never break character.
------------
{context}
------------
REMEMBER: If there is no relevant information within the context, just say "Hmm, I'm not sure". Don't try to make up an answer. Never break character.  "

### assistant

Perfeito, Paulo. Abaixo está o **prompt traduzido e adaptado para o português do Brasil**, mantendo as instruções essenciais e o tom de agente que responde apenas com base no conteúdo fornecido:

---

**Prompt de resposta em português para agente com base em documento:**

> Quero que você atue como se fosse um documento com o qual estou conversando. Seu nome é **"Assistente IA"**. Usando apenas o conteúdo fornecido abaixo como contexto, responda à pergunta do usuário da melhor forma possível, com base nas informações disponíveis.
> 
> Se não houver nada no contexto que seja relevante para a pergunta, diga apenas: **"Hmm, não tenho certeza"** — e pare por aí. Recuse-se a responder qualquer pergunta que não esteja relacionada às informações fornecidas. Nunca saia do personagem.
> 
> ------------
> **{contexto}**
> ------------
> 
> **LEMBRE-SE:** Se não houver informação relevante no contexto, diga apenas: **"Hmm, não tenho certeza"**. **Não invente uma resposta. Nunca saia do personagem.**

---

Se quiser, posso preparar uma versão para uso em ferramentas como LangChain, RAG ou agentes autônomos. Deseja essa adaptação técnica?

### user

O ultimo prompt gerou esse erro : Missing value for input variable contexto

Troubleshooting URL:
https://js.langchain.com/docs/troubleshooting/errors/INVALID_PROMPT_INPUT/

### assistant

Esse erro ocorre porque o sistema que está executando o prompt (como o LangChain) espera que todas as **variáveis de entrada estejam corretamente nomeadas e fornecidas**. No seu caso, o erro indica que a variável `contexto` **não foi preenchida** na hora da execução.

### Solução:

Você deve alterar a variável de entrada para seguir exatamente o padrão esperado pelo seu pipeline (geralmente em inglês, a não ser que a ferramenta tenha sido totalmente configurada em português). O nome mais comum é `context`.

### Prompt corrigido (em português, com variável em inglês `context`):

```plaintext
Quero que você atue como se fosse um documento com o qual estou conversando. Seu nome é "Assistente IA". Usando apenas o conteúdo fornecido abaixo como contexto, responda à pergunta do usuário da melhor forma possível, com base nas informações disponíveis.

Se não houver nada no contexto que seja relevante para a pergunta, diga apenas: "Hmm, não tenho certeza" — e pare por aí. Recuse-se a responder qualquer pergunta que não esteja relacionada às informações fornecidas. Nunca saia do personagem.

------------
{context}
------------

LEMBRE-SE: Se não houver informação relevante no contexto, diga apenas: "Hmm, não tenho certeza". Não invente uma resposta. Nunca saia do personagem.
```

### Observações:
- Substituí `{contexto}` por `{context}`, que é o nome padrão da variável que ferramentas como LangChain esperam.
- Mantenha todas as variáveis em inglês se estiver usando ambientes configurados dessa forma.

Deseja que eu revise seu pipeline para garantir que todos os nomes de variáveis estejam consistentes?

### user

Agora deu esse erro: (f-string) Missing value for input documento

### assistant

Paulo, esse novo erro indica que, **em algum lugar do seu código ou ferramenta (provavelmente LangChain ou similar), o prompt está usando a variável `documento`**, mas você não está fornecendo esse valor no momento da execução.

### Duas possibilidades de erro e suas soluções:

---

### **1. O prompt está usando `{documento}` mas você forneceu `{context}` (ou vice-versa)**

**Solução:** Uniformize a variável. Escolha **`document`** ou **`context`**, que são mais comuns em ferramentas como LangChain.

### Prompt corrigido usando `{context}` (padrão internacional mais comum):

```plaintext
Quero que você atue como se fosse um documento com o qual estou conversando. Seu nome é "Assistente IA". Usando apenas o conteúdo fornecido abaixo como contexto, responda à pergunta do usuário da melhor forma possível, com base nas informações disponíveis.

Se não houver nada no contexto que seja relevante para a pergunta, diga apenas: "Hmm, não tenho certeza" — e pare por aí. Recuse-se a responder qualquer pergunta que não esteja relacionada às informações fornecidas. Nunca saia do personagem.

------------
{context}
------------

LEMBRE-SE: Se não houver informação relevante no contexto, diga apenas: "Hmm, não tenho certeza". Não invente uma resposta. Nunca saia do personagem.
```

---

### **2. Seu código/função está chamando a variável `documento`, mas o prompt não a usa**

**Solução alternativa:** Se sua pipeline ou JSON de entrada está estruturado com a variável `documento`, altere o prompt para:

```plaintext
Quero que você atue como se fosse um documento com o qual estou conversando. Seu nome é "Assistente IA". Usando apenas o conteúdo fornecido abaixo como documento de referência, responda à pergunta do usuário da melhor forma possível, com base nas informações disponíveis.

Se não houver nada no documento que seja relevante para a pergunta, diga apenas: "Hmm, não tenho certeza" — e pare por aí. Recuse-se a responder qualquer pergunta que não esteja relacionada às informações fornecidas. Nunca saia do personagem.

------------
{documento}
------------

LEMBRE-SE: Se não houver informação relevante no documento, diga apenas: "Hmm, não tenho certeza". Não invente uma resposta. Nunca saia do personagem.
```

---

### Conclusão

Verifique **como está nomeada a variável no código que executa o prompt** (LangChain, Node.js, Python etc.). A variável dentro do prompt deve **bater exatamente** com o nome da variável no dicionário passado à função (como `.format(context="...")` ou `input_variables=["context"]`).

Deseja que eu revise um exemplo de código da sua função para garantir compatibilidade total?

### user

Agora apareceu esse erro: " Error: Expected a Runnable, function or object. Instead got an unsupported type."

### assistant

Esse novo erro — **“Expected a Runnable, function or object. Instead got an unsupported type.”** — indica que **algum componente da sua cadeia (provavelmente no LangChain ou Flowise) está esperando uma função executável (como um `Runnable`), mas recebeu um tipo incorreto (como uma string ou um dicionário puro).**

---

### Causa mais comum:
Você provavelmente **passou o prompt como uma `string` diretamente**, em um local onde o sistema espera um objeto estruturado, como um `PromptTemplate`, `Runnable`, `LLMChain`, etc.

---

### Como resolver (LangChain v0.1+ como referência):

#### ✅ Exemplo correto com `PromptTemplate`:

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    """
    Quero que você atue como se fosse um documento com o qual estou conversando. Seu nome é "Assistente IA". Usando apenas o conteúdo fornecido abaixo como contexto, responda à pergunta do usuário da melhor forma possível, com base nas informações disponíveis.

    Se não houver nada no contexto que seja relevante para a pergunta, diga apenas: "Hmm, não tenho certeza" — e pare por aí. Recuse-se a responder qualquer pergunta que não esteja relacionada às informações fornecidas. Nunca saia do personagem.

    ------------
    {context}
    ------------

    LEMBRE-SE: Se não houver informação relevante no contexto, diga apenas: "Hmm, não tenho certeza". Não invente uma resposta. Nunca saia do personagem.
    """
)
```

Depois, você pode usá-lo com:

```python
chain = prompt | llm  # se estiver usando o operador `|` do LangChain v0.1+
```

---

### Em Flowise (se for esse o caso):

No Flowise, **você deve selecionar o nó "Prompt Template"** e colar o texto dentro da caixa **como um `template`, não como `Raw Input`**, e garantir que o campo de variável seja declarado como `context`.

---

### Checklist para evitar o erro:
- [ ] O prompt está instanciado como `PromptTemplate` (não apenas uma string).
- [ ] O objeto `PromptTemplate` está sendo passado a um `Runnable`, `LLMChain` ou outra estrutura compatível.
- [ ] As variáveis usadas no template (ex: `{context}`) estão sendo fornecidas no dicionário de entrada.
- [ ] Você não está passando dicionários puros ou strings diretas onde o sistema espera objetos.

---

Se quiser, posso revisar o trecho de código ou fluxo visual que você está usando. Deseja colar aqui o trecho de código ou descrever os nós configurados no Flowise?
