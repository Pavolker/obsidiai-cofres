---
source: DATAGPT
conversation_id: 67c191b9-cbb4-8002-8da6-51433117676e
title: "Agente PDF Flowise"
theme: IA PROMPTS
created: 2025-02-28T10:36:42.178464Z
message_count: 12
attachments_count: 0
---

# Agente PDF Flowise

- Tema: `IA PROMPTS`
- Conversation ID: `67c191b9-cbb4-8002-8da6-51433117676e`

## Transcrição

### user

Meu objetivo é criar um agente na plataforma flowise, que seja capaz de consultar um arquivo PDF para conversas com usuários sobre o assunto do PDF

### assistant

Para criar um agente no Flowise que consulte um arquivo PDF e interaja com os usuários sobre seu conteúdo, siga este passo a passo:

---

### **Passo 1: Configuração Inicial**
1. **Acesse o Flowise** na sua instância hospedada na Railway.
2. **Crie um novo fluxo de trabalho** clicando em "New Flow".

---

### **Passo 2: Adicionar o Componente de Entrada (Chat)**
1. Adicione um **nó "Chat Input"** para receber as perguntas dos usuários.
   - Esse nó permitirá que o usuário envie mensagens ao agente.

---

### **Passo 3: Processamento do PDF**
1. **Adicione um nó "Load Document" (PDF Loader)**:
   - Escolha a opção para carregar um PDF e faça o upload do seu arquivo.
   - Esse nó processará o texto do PDF para ser usado posteriormente.

2. **Adicione um nó "Text Splitter"** (Opcional, mas recomendado):
   - Esse nó divide o texto do PDF em partes menores para melhorar a recuperação de informações.

---

### **Passo 4: Criar o Banco de Conhecimento**
1. **Adicione um nó "Vector Store"**:
   - Utilize uma base vetorial como FAISS, Chroma ou Pinecone.
   - Esse nó armazena os fragmentos do PDF como vetores para busca eficiente.

2. **Conecte o nó "Text Splitter" ao "Vector Store"**:
   - Isso garante que o conteúdo do PDF seja indexado corretamente.

---

### **Passo 5: Criar um Sistema de Busca Inteligente**
1. **Adicione um nó "Retrieval"**:
   - Esse nó buscará as informações mais relevantes no PDF conforme a pergunta do usuário.

2. **Conecte o "Chat Input" ao "Retrieval"**:
   - Isso permite que a pergunta do usuário seja usada para buscar as informações corretas no PDF.

---

### **Passo 6: Criar a Resposta com um Modelo de IA**
1. **Adicione um nó "LLM"** (como OpenAI GPT, Mistral ou LLama):
   - Esse nó processará a consulta e gerará respostas mais naturais.

2. **Conecte o nó "Retrieval" ao "LLM"**:
   - Assim, o modelo recebe o contexto certo do PDF para formular a resposta.

---

### **Passo 7: Exibir a Resposta ao Usuário**
1. **Adicione um nó "Chat Output"**:
   - Esse nó envia a resposta final ao usuário.

2. **Conecte o "LLM" ao "Chat Output"**:
   - Isso finaliza o fluxo e entrega a resposta baseada no PDF.

---

### **Passo 8: Testar e Ajustar**
1. **Execute o fluxo** e faça perguntas relacionadas ao conteúdo do PDF.
2. **Ajuste o processamento** (como dividir melhor o texto ou melhorar a busca) se necessário.

---

### **Passo 9: Integrar com uma Interface (Opcional)**
- **Se quiser disponibilizar o agente em um site**, use um webhook ou conecte ao WhatsApp, Telegram ou uma API para comunicação com usuários.

---

Isso criará um agente capaz de responder perguntas sobre o PDF. Caso precise de ajustes mais avançados, podemos explorar filtros, embeddings personalizados ou otimização do fluxo. 🚀

### user

No caso do passo 3, posso usar o "Document Store (Vector)?

### assistant

Sim, no **Passo 3**, você pode usar o **"Document Store (Vector)"** ao invés do "Vector Store" separado. Isso pode simplificar o fluxo e facilitar o gerenciamento dos dados extraídos do PDF. 

### **Como usar o "Document Store (Vector)"?**
1. **Adicione o nó "Document Store (Vector)"** ao fluxo.
2. **Configure o armazenamento vetorial** (como FAISS, Chroma ou Pinecone).
3. **Conecte o nó "Load Document" (PDF Loader) diretamente ao "Document Store (Vector)"**.
   - Isso garantirá que o conteúdo do PDF seja armazenado e indexado corretamente.

### **Benefícios dessa abordagem**
✅ **Menos nós no fluxo**, pois esse nó já combina armazenamento e recuperação.  
✅ **Melhor organização dos documentos**, já que ele pode armazenar múltiplos PDFs.  
✅ **Facilidade para atualizações**, pois você pode adicionar novos documentos sem precisar reindexar tudo do zero.

---

Se você quiser que o sistema busque informações no PDF de maneira eficiente, **certifique-se de ativar a opção de "Similarity Search" dentro do "Document Store (Vector)"**. Isso garantirá que ele encontre os trechos mais relevantes para responder às perguntas dos usuários. 🚀

### user

Especificamente, no passo 3, qual tipo de text splitter: Character text Splitter ou code text splitter ou token text splitter ?

### assistant

No **Passo 3**, o melhor tipo de **Text Splitter** a ser usado depende do tipo de conteúdo do seu PDF. Aqui está a recomendação para cada caso:

### 🔹 **Qual "Text Splitter" usar para um PDF?**
1. **Character Text Splitter** (📌 **Recomendado para PDFs comuns**)  
   ✅ Melhor opção para documentos com texto corrido, como artigos, relatórios e livros.  
   ✅ Divide o conteúdo por caracteres, garantindo que os trechos não fiquem incompletos.  
   ✅ Configurável para cortar por parágrafos, frases ou número de caracteres.  

2. **Token Text Splitter** (📌 **Para PDFs muito longos e com IA GPT/OpenAI**)  
   ✅ Divide o texto baseado no número de tokens, útil para otimizar chamadas para APIs de IA.  
   ✅ Evita que o modelo processe trechos muito grandes, reduzindo custos.  
   ✅ Melhor opção quando o PDF contém muito texto e precisa ser otimizado para IA.  

3. **Code Text Splitter** (⚠️ **Não recomendado para PDFs comuns**)  
   🔹 Esse splitter é mais indicado para documentos que contenham código-fonte, como arquivos técnicos ou manuais de programação.  
   🔹 Se o PDF for sobre código, pode ser útil, mas para textos normais, não é necessário.  

---

### **Conclusão: Qual escolher?**
- **Se o PDF for um documento textual normal** → **Character Text Splitter**  
- **Se o PDF for muito longo e for processado por IA** → **Token Text Splitter**  
- **Se o PDF contiver código-fonte** → **Code Text Splitter**  

Para a maioria dos casos, o **Character Text Splitter** com um tamanho de chunk entre **500 e 1000 caracteres** e sobreposição de **100 a 200 caracteres** deve funcionar bem. 🚀

### user

No passo 4 fiz a opção pelo "SingleStore", pode ser?

### assistant

Sim! Você pode usar o **SingleStore** no **Passo 4** para armazenar e recuperar os embeddings do seu PDF. Essa escolha é válida e pode trazer benefícios dependendo do seu caso de uso. Aqui estão os principais pontos:

---

### **📌 Vantagens de usar SingleStore**
✅ **Banco de dados escalável** – Pode lidar com grandes volumes de dados rapidamente.  
✅ **Recuperação eficiente** – Permite buscas vetoriais otimizadas para consultas rápidas.  
✅ **Persistência dos dados** – Diferente de soluções como FAISS, que são apenas em memória, o SingleStore mantém os dados salvos de forma permanente.  
✅ **Boa integração com Fluxos de IA** – Funciona bem para armazenar e consultar embeddings usados para busca semântica.

---

### **🔹 Como configurar o SingleStore no Flowise?**
1. **Adicione o nó "SingleStore"** no Flow.
2. **Conecte-o ao nó "Text Splitter"** (Character ou Token Text Splitter, dependendo da sua escolha anterior).
3. **Escolha a configuração adequada**:
   - Defina um **índice vetorial** para armazenar os embeddings.
   - Escolha um **método de similaridade** (como distância de cosseno ou Euclidean).
   - Certifique-se de que está configurado para buscar os resultados mais relevantes.

4. **Conecte o "Chat Input" ao SingleStore**  
   - Isso garantirá que a consulta do usuário seja usada para encontrar as partes mais relevantes do PDF.

5. **Conecte o SingleStore ao modelo LLM (ex: OpenAI, Mistral, Llama, etc.)**  
   - Isso permitirá que o modelo gere respostas baseadas nos trechos recuperados do PDF.

---

### **🟢 Conclusão**
Sim, usar **SingleStore** no **Passo 4** é uma excelente escolha se você quer um banco de dados vetorial escalável e persistente. Se precisar de ajuda na configuração, me avise! 🚀

### user

O singlestore tem duas saidas, o singlestore retriever e o singlestore vector store, ligo qual delas e onde ?

### assistant

Ótima pergunta! O **SingleStore** tem duas saídas principais no Flowise:  

1. **SingleStore Vector Store** – Para armazenar embeddings (indexação do PDF).  
2. **SingleStore Retriever** – Para recuperar os trechos relevantes quando um usuário faz uma pergunta.  

### **📌 Como conectar corretamente no Flowise?**

#### **1️⃣ Armazenando os Dados no SingleStore**
📌 **Objetivo:** Indexar o PDF para permitir buscas futuras.  
✅ **Conecte o "Text Splitter" → ao "SingleStore Vector Store"**  
- O "Text Splitter" divide o conteúdo do PDF em partes menores.  
- O "SingleStore Vector Store" armazena esses trechos no banco vetorial.  

#### **2️⃣ Recuperando Dados para Responder o Usuário**
📌 **Objetivo:** Quando o usuário perguntar algo, recuperar os trechos relevantes do PDF.  
✅ **Conecte o "Chat Input" → ao "SingleStore Retriever"**  
✅ **Conecte o "SingleStore Retriever" → ao Modelo de IA (LLM, ex: OpenAI, Llama, etc.)**  
- O "Retriever" busca os trechos mais relevantes baseados na pergunta.  
- O modelo de IA usa esses trechos para formular a resposta ao usuário.  

---

### **🔹 Fluxo Final**
1️⃣ **PDF Loader** → 2️⃣ **Text Splitter** → 3️⃣ **SingleStore Vector Store** (armazenar embeddings)  
4️⃣ **Chat Input** → 5️⃣ **SingleStore Retriever** → 6️⃣ **LLM (OpenAI, Mistral, etc.)** → 7️⃣ **Chat Output**  

Esse é o fluxo ideal para que seu agente possa buscar informações no PDF e responder corretamente! 🚀

### user

O modelo de IA, p.exe, ChatOpenAi, não tem entrada para o SingleStore Retriever. A única entrada é Cache

### assistant

Ótima observação! O nó **ChatOpenAI** no Flowise não aceita diretamente a saída do **SingleStore Retriever**, porque ele espera uma entrada de texto e não um conjunto de embeddings diretamente. Para resolver isso, você precisa de um intermediário que transforme os resultados do **Retriever** em um contexto compreensível para o modelo de IA. Aqui está como fazer:

---

### **📌 Como conectar o SingleStore Retriever ao ChatOpenAI?**
Já que o **ChatOpenAI** não aceita diretamente a saída do **SingleStore Retriever**, precisamos de um nó intermediário, que pode ser:

✅ **"Combine Documents"**  
✅ **"Format Documents to String"**  

### **🔹 Fluxo Correto**
1️⃣ **PDF Loader** → 2️⃣ **Text Splitter** → 3️⃣ **SingleStore Vector Store** *(para armazenar o texto indexado do PDF)*  
4️⃣ **Chat Input** → 5️⃣ **SingleStore Retriever** *(busca os trechos mais relevantes do PDF)*  
6️⃣ **Format Documents to String** *(transforma os trechos recuperados em um texto único)*  
7️⃣ **ChatOpenAI** *(usa esse texto como contexto para gerar a resposta)*  
8️⃣ **Chat Output** *(exibe a resposta final para o usuário)*  

---

### **📌 Como configurar o "Format Documents to String"?**
1. Adicione o nó **"Format Documents to String"**.
2. Conecte a saída do **SingleStore Retriever** à entrada do **Format Documents to String**.
3. Conecte a saída do **Format Documents to String** à entrada do **ChatOpenAI** (na porta "Cache" ou "Input").

---

### **🟢 Conclusão**
🔹 O **Retriever** busca os trechos relevantes do PDF.  
🔹 O **Format Documents to String** transforma esses trechos em um texto contínuo.  
🔹 O **ChatOpenAI** usa esse texto como contexto para gerar a resposta correta.  

Agora seu agente estará pronto para responder perguntas com base no PDF! 🚀 Se precisar de ajustes, me avise!
