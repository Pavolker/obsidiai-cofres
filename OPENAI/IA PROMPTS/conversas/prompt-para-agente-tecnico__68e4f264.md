---
source: DATAGPT
conversation_id: 68e4f264-e118-832f-8ce6-6ce632169c5c
title: "Prompt para agente técnico"
theme: IA PROMPTS
created: 2025-10-07T11:00:23.789182Z
message_count: 4
attachments_count: 0
---

# Prompt para agente técnico

- Tema: `IA PROMPTS`
- Conversation ID: `68e4f264-e118-832f-8ce6-6ce632169c5c`

## Transcrição

### user

Faça um prompt para uma agente especializado em desenvolver capítulos de relatórios técnicos. Esse agende deverá consultar a internet, bases de dados disponibilizadas, com arquivos de conteúdos (PF, docx, planilhas, entre outros) e escrever capítulos coerentes, com começo, meio e fim. Os artigos deverão fazer referência bibliográfica, sempre que consultarem uma fonte, no estilo ABNT. Os capítulos não deverão ultrapassar 2.000 palavras.

### assistant

Segue o **prompt para um agente de IA especializado em desenvolver capítulos de relatórios técnicos**, conforme solicitado:

---

### 🧠 Prompt Mestre: Agente IA de Redação Técnica com Consulta a Fontes

**Nome do Agente:** `Agente Redator Técnico com Referência ABNT`

**Missão do Agente:**  
Redigir capítulos técnicos de relatórios com coerência textual, estrutura argumentativa completa (introdução, desenvolvimento e conclusão), e fundamentação com base em dados atualizados e fontes confiáveis, acessadas na internet e/ou em bases documentais fornecidas (PDF, DOCX, planilhas etc.).

---

### 🧩 Instruções Estruturais

1. **Objetivo:** Redigir um **capítulo técnico completo**, com até **2.000 palavras**, tratando de forma aprofundada o tema solicitado.
2. **Estrutura Obrigatória:**
   - **Introdução:** contextualize o tema com base em dados disponíveis e justificativa de relevância.
   - **Desenvolvimento:** aprofunde a análise com base em evidências, dados, documentos, estudos ou benchmarks nacionais/internacionais.
   - **Conclusão:** sistematize os achados e prepare o terreno para o próximo capítulo (sem fechamento definitivo).
3. **Linguagem:** técnica, formal e precisa. Sem adjetivação subjetiva ou juízos de valor.
4. **Referências:** todas as fontes consultadas devem ser citadas conforme **normas da ABNT** (NBR 6023), em notas de rodapé ou seção de referências ao final do capítulo.
5. **Fontes de dados:** o agente deve:
   - Realizar **pesquisas online** atualizadas para embasar os conteúdos (dados estatísticos, legislação, publicações científicas, relatórios setoriais, etc.).
   - Acessar e utilizar **documentos fornecidos pelo usuário** (PDFs, DOCX, planilhas etc.).
   - Indicar claramente a origem de cada dado relevante.

---

### 🔍 Comportamento de Busca

- Sempre que o tema exigir **atualização**, usar mecanismos de busca com foco em sites científicos, institucionais ou especializados (ex: IBGE, IPEA, SciELO, Google Scholar, OCDE, ONU, etc.).
- Se houver **bases de dados conectadas pelo usuário** (ex: Google Drive), o agente deverá consultá-las e utilizá-las como fonte primária.
- Referenciar qualquer dado, citação ou estatística com indicação clara de fonte e ano.

---

### 🛠 Comandos adicionais possíveis

- `"Tema: [insira aqui o título ou escopo do capítulo]"` → define o conteúdo principal a ser desenvolvido.
- `"Base de dados: [indique se deve consultar documentos específicos ou Drive]"` → orienta a fonte prioritária.
- `"Formato: Markdown | PDF | DOCX"` → define o formato de entrega do capítulo.
- `"Foco especial em: [ex: benchmarking internacional, dados quantitativos, legislação]"` → define o eixo prioritário da abordagem.

---

### 🧾 Exemplo de chamada para ativação:

```txt
Agente Redator Técnico, preciso de um capítulo sobre “Economia Circular no Setor Têxtil Brasileiro”, com até 2.000 palavras, baseado em relatórios atualizados do Sebrae, OCDE e dados da Abit. Utilize a documentação em meu Drive se disponível. Formato de saída: Markdown com referências ABNT.
```

---

Se desejar, posso criar um _template automático_ para ativar esse agente no Flowise, Typebot ou outra ferramenta de orquestração. Deseja isso, Paulo?

### user

Para  a configuração do "file search" do agente, na configuração do "vector store", há uma janela "Query", com a orientação de " enter file search input. Use {{curly braces}} to insert variables. Para que serve essa janela de configuração ?

### assistant

Paulo, a janela **“Query”** na configuração do **file search** dentro do componente **Vector Store** (como no Flowise ou em agentes no-code semelhantes) serve para **definir a consulta base** que será feita ao buscar informações em arquivos (PDF, DOCX, planilhas etc.) indexados em uma fonte conectada — por exemplo, Google Drive ou banco de dados vetorial.

### ✅ Finalidade da janela "Query":

Ela define **o conteúdo da busca que será executada no momento da consulta**, ou seja, **o input do usuário que será interpretado como uma pergunta ou instrução de busca textual** sobre os arquivos disponíveis.

---

### 🧠 Como funciona:

A string inserida nesta janela será usada como **entrada para o mecanismo de busca vetorial** (ex: similarity search + keyword search) dentro dos documentos carregados. Quando você usa **variáveis dinâmicas entre `{{chaves}}`**, você está dizendo ao sistema para preencher aquele espaço com um valor **dinâmico em tempo real**, geralmente vindo de outro bloco (por exemplo, do input do usuário ou do histórico de conversa).

---

### 🧩 Exemplos práticos:

#### 1. Consulta direta com variável:
```txt
{{question}}
```
> Aqui, você está dizendo ao sistema: “Use o que o usuário escreveu (variável `question`) como a query para buscar nos arquivos conectados”.

Esse é o caso **mais comum** e funcional. Você pode configurar o seu agente para, por exemplo:
- Receber a pergunta do usuário via Typebot ou Flowise Input;
- A variável `{{question}}` será automaticamente preenchida com essa entrada;
- O file search usará isso para procurar a resposta nos documentos.

#### 2. Consulta fixa (não recomendada, mas possível):
```txt
relatório sobre economia circular no setor de moda
```
> Isso fará com que todas as buscas procurem esse tema **fixo**, ignorando inputs dinâmicos.

---

### 🔧 Dica prática para configuração eficiente:

Na maioria dos casos, **você deve deixar a query configurada assim**:
```txt
{{question}}
```
Ou, caso use outro nome para o campo de input no seu Flowise, como:
```txt
{{user_input}}
```
A variável precisa **corresponder exatamente ao nome do campo anterior no fluxo**.

---

### 📎 Observações:

- O que é preenchido aqui **alimenta o motor de busca vetorial/documental** (não é uma prompt de LLM diretamente).
- Esse campo é **obrigatório** para que o mecanismo de file search saiba o que buscar nos arquivos.

Se quiser, posso te ajudar a configurar isso diretamente em um agente Flowise (com nome da variável, nodes anteriores e posteriores, etc.).

Deseja isso?
