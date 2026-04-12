---
source: DATAGPT
conversation_id: 6880dae0-5950-832a-895f-3680fbce5fe5
title: "App para criação de eBooks"
theme: TECNOLOGIA
created: 2025-07-23T12:51:45.673804Z
message_count: 4
attachments_count: 0
---

# App para criação de eBooks

- Tema: `TECNOLOGIA`
- Conversation ID: `6880dae0-5950-832a-895f-3680fbce5fe5`

## Transcrição

### user

faça o prompt para  um agente de IA criar um aplicativo que  cria ebooks a partir dos seguintes  inputs: 1- tema; 2- abordagem; 3- tópicos; 4- autores de referência; 5- obras de referência; 6- número palavras do ebook.  Esses inputs deverão ser inseridos em janelas onde se digita as informações ou através de upload de documentos.  Os ebooks deverão ser formatados dentro de um padrão pré-estabelecido, com capa, contra-capa, ficha catalográfica, epigrafes, sumário, prefácio, entre outros itens padrões da industria editorial

### assistant

Segue o prompt solicitado, Paulo, estruturado para um agente de IA criador de aplicativos no-code ou low-code:

---

**Prompt para Criação de Aplicativo – Gerador de eBooks com Padrão Editorial**

Você é um agente de inteligência artificial especializado no desenvolvimento de aplicativos no-code/low-code com integração de banco de dados e geração automatizada de documentos em padrão editorial. Sua tarefa é construir um aplicativo web que possibilite a criação de eBooks com base nos seguintes inputs fornecidos pelo usuário:

### FUNCIONALIDADES ESSENCIAIS

**1. Coleta de Inputs do Usuário**  
O aplicativo deverá permitir ao usuário inserir os seguintes dados de duas formas:  
a) por campos de texto digitável  
b) por upload de documentos (em formatos .txt, .docx ou .pdf)

Campos obrigatórios:
- Tema do eBook  
- Abordagem (científica, filosófica, educativa, etc.)  
- Lista de tópicos ou estrutura sugerida  
- Autores de referência  
- Obras de referência  
- Número de palavras desejadas (mínimo de 2.000)

**2. Geração do eBook**  
O sistema deverá transformar os dados fornecidos em um eBook estruturado automaticamente com os seguintes elementos editoriais:

- Capa (com título, subtítulo e nome do autor)  
- Contra-capa (com resumo e informações complementares)  
- Ficha catalográfica (com estrutura padrão da Biblioteca Nacional)  
- Epígrafes (opcional, selecionadas automaticamente a partir dos autores indicados ou do tema)  
- Sumário automático  
- Prefácio (gerado com base na abordagem escolhida)  
- Corpo do texto dividido por tópicos  
- Referências bibliográficas (estilo ABNT ou APA, com base nos autores e obras informados)  
- Página de direitos autorais  
- Sobre o autor

**3. Formatação e Exportação**  
- O eBook deverá seguir um template editorial padronizado (tipografia, margens, estilos de cabeçalho, paginação etc.).  
- Exportação final em formato PDF (para impressão e leitura) e EPUB (para leitura digital).  
- Os arquivos gerados devem ser armazenados temporariamente para download.

**4. Interface do Aplicativo**  
- Interface limpa, intuitiva, com progressão em etapas (wizard-style)  
- Estética visual compatível com publicações editoriais e acadêmicas  
- Responsivo para uso em desktop e dispositivos móveis

**5. Backend e Banco de Dados**  
- Todos os dados dos usuários devem ser armazenados com segurança (usar Supabase, Firebase ou banco compatível com a plataforma escolhida)  
- Deve permitir que o usuário recupere versões anteriores e acompanhe status da geração do eBook

---

Se desejar, posso transformar esse prompt em um documento técnico (especificação de produto ou ficha funcional) ou converter para um formato compatível com plataformas como **Glide**, **FlutterFlow**, **Bubble**, **WeWeb** ou **Retool**.

Deseja avançar nesse sentido?

### user

Refaça esse prompt definindo os seguintes parametros: 1- aplicativo de uso local, sem conexão com banco de dados externo; 2- aplicativo com um único usuário, o escritor Paulo Volker, que irá usar o aplicativo para produzir a sua obra; 3- o ebook deverá ser em PDF, exclusivamente; 4- a definição do número de palavras do ebook é uma parte impórtante do escopo do livro

### assistant

Claro, Paulo. Abaixo está o prompt reformulado conforme os novos parâmetros definidos:

---

**Prompt para Criação de Aplicativo Local — Gerador de eBooks para Escritor Único**

Você é um agente de inteligência artificial especializado em desenvolvimento de aplicativos de uso local (standalone), sem necessidade de conexão com servidores externos ou bancos de dados remotos. Sua tarefa é criar um aplicativo desktop ou web local para uso exclusivo do escritor **Paulo Volker**, com a finalidade de gerar eBooks completos em **formato PDF**, com estrutura editorial profissional.

### ESCOPO DO APLICATIVO

**1. Finalidade e Usuário Único**  
- O aplicativo será utilizado unicamente por **Paulo Volker**.  
- Não haverá necessidade de autenticação, múltiplos perfis ou armazenamento em nuvem.  
- Todos os dados devem ser processados e salvos localmente (disco rígido do usuário).  

**2. Funcionalidade Principal**  
- O aplicativo deverá gerar um eBook estruturado, exclusivamente em **formato PDF**, a partir dos seguintes inputs preenchidos por Paulo:

  **Inputs obrigatórios:**
  - **Tema do eBook**  
  - **Abordagem desejada** (ex.: filosófica, científica, ensaística, narrativa, etc.)  
  - **Tópicos ou capítulos planejados**  
  - **Autores de referência**  
  - **Obras de referência**  
  - **Número de palavras desejadas para o eBook** *(este dado será utilizado para calibrar a extensão de cada seção, a profundidade do conteúdo e a coerência interna do livro)*

  **Modo de entrada:**
  - Por campos de texto digitáveis
  - Ou por upload de documentos de apoio (formatos: .txt, .docx, .pdf)

**3. Estrutura Editorial do eBook**  
O eBook gerado deverá conter os seguintes elementos padrão da indústria editorial:

- **Capa** (com título, subtítulo, nome do autor, visual editorial básico)
- **Contra-capa** (com sinopse da obra e minibio do autor)
- **Ficha catalográfica** (preenchida automaticamente com dados inseridos)
- **Epígrafes** (sugeridas com base nos autores e tema ou inseridas manualmente)
- **Sumário automático**
- **Prefácio** (baseado na abordagem e no propósito do livro)
- **Corpo do texto**, dividido pelos tópicos definidos
- **Referências bibliográficas** (formatação ABNT ou APA, conforme escolha do autor)
- **Página de direitos autorais**
- **Sobre o autor** (inserido manualmente ou a partir de template)

**4. Geração e Salvamento do Arquivo PDF**  
- O arquivo final será gerado **exclusivamente em formato PDF**, pronto para publicação ou impressão.  
- O arquivo será salvo diretamente em diretório local indicado pelo usuário.  
- O sistema deve permitir a geração de múltiplas versões/editais do mesmo projeto.

**5. Operação Offline**  
- Todo o funcionamento do aplicativo deve ocorrer em ambiente **local/offline**, sem dependência de internet.  
- Não deve haver integração com banco de dados externo, serviços de nuvem, APIs remotas ou ferramentas de autenticação.

**6. Interface do Usuário**  
- Interface clara, sequencial e com foco na experiência de escrita e montagem editorial.  
- Design orientado para fluxo em etapas (wizard) com visualização de progresso.  
- Deve permitir salvar e reabrir projetos em andamento.

---

Se desejar, posso converter este prompt em uma especificação técnica completa ou fornecer o código inicial para implementação local (por exemplo, em **Electron.js**, **Python com Tkinter**, ou **PyQt**). Deseja isso?
