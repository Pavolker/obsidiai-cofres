---
source: DATAGPT
conversation_id: 69679a57-8f60-8332-9043-ac272ee4c3e3
title: "Prompt comunidade diálogo IA"
theme: IA PROMPTS
created: 2026-01-14T13:30:08.577479Z
message_count: 4
attachments_count: 0
---

# Prompt comunidade diálogo IA

- Tema: `IA PROMPTS`
- Conversation ID: `69679a57-8f60-8332-9043-ac272ee4c3e3`

## Transcrição

### user

ola

### assistant

Olá, Paulo.  
Como posso ajudar agora?

### user

Preciso de um prompt para um agente de IA criar uma comunidade de diálogo onde a Angélica e o Paulo conversam sobre a vida e a filosofia e os usuários postam comentários e perguntas. Somente a Angélica e o Paulo podem postar textos, os usuários só comentam. A página tem um menu lateral à esquerda, com botões com links para Livro, ebook, site, blog, curso, palestra. A página tem um design limpo e bem programado, com cor azulada

### assistant

Paulo, segue um **prompt completo e operacional**, pensado para ser usado diretamente por um **agente de IA desenvolvedor** (no-code ou low-code), com foco em arquitetura, regras de interação, UI e governança do diálogo. Linguagem neutra, sem conclusões, sem adjetivações valorativas.

---

## PROMPT PARA AGENTE DE IA — COMUNIDADE DE DIÁLOGO FILOSÓFICO

**Papel do agente**  
Você é um agente de IA especializado em design de produtos digitais, arquitetura de comunidades online e desenvolvimento front-end e back-end. Seu objetivo é criar uma comunidade digital de diálogo filosófico estruturado.

---

### 1. Conceito da Comunidade
Criar uma **plataforma de diálogo contínuo** onde dois autores fixos — **Angélica** e **Paulo** — publicam textos reflexivos sobre vida, filosofia e experiência humana.  
Os usuários da plataforma **não publicam textos principais**, apenas **comentam e fazem perguntas** nos espaços associados a cada diálogo.

---

### 2. Regras de Publicação e Papéis
Defina claramente os seguintes papéis no sistema:

- **Autores (papel fixo)**  
  - Angélica  
  - Paulo  
  - Permissões:
    - Criar novos diálogos (posts principais)
    - Editar seus próprios textos
    - Responder comentários

- **Usuários registrados**
  - Permissões:
    - Comentar textos existentes
    - Fazer perguntas nos campos de comentário
  - Restrições:
    - Não podem criar novos diálogos
    - Não podem editar textos principais

- **Visitantes**
  - Permissões:
    - Leitura pública dos diálogos e comentários
  - Restrições:
    - Não podem comentar sem cadastro

Implemente controle de permissões de forma explícita no código ou na lógica da plataforma.

---

### 3. Estrutura da Página (Layout)
Desenvolva uma **página única principal**, com a seguinte organização:

#### 3.1 Menu Lateral Esquerdo (fixo)
Menu vertical, alinhado à esquerda, com botões ou links para:

- Livro  
- Ebook  
- Site  
- Blog  
- Curso  
- Palestra  

Cada item deve permitir link externo configurável.

---

#### 3.2 Área Central de Conteúdo
- Exibição cronológica dos diálogos
- Cada diálogo contém:
  - Nome do autor (Angélica ou Paulo)
  - Data de publicação
  - Texto principal
  - Área de comentários abaixo

---

#### 3.3 Área de Comentários
- Comentários em formato de lista encadeada
- Campo de pergunta/comentário por usuário
- Indicação clara de autor x usuário
- Possibilidade de resposta dos autores aos comentários

---

### 4. Design e Identidade Visual
- Estilo visual:
  - Design limpo
  - Interface clara e legível
- Paleta de cores:
  - Base em tons azulados
- Tipografia:
  - Fontes sem serifa
  - Boa hierarquia visual entre títulos, textos e comentários
- Layout responsivo:
  - Desktop, tablet e mobile

---

### 5. Arquitetura Técnica (orientação)
Implemente a solução preferencialmente em:

- **Front-end:** HTML, CSS e JavaScript ou framework equivalente  
- **Back-end:** sistema simples de autenticação e permissões  
- **Banco de dados:**
  - Tabela de usuários
  - Tabela de diálogos (posts principais)
  - Tabela de comentários vinculados aos diálogos

---

### 6. Funcionalidades Essenciais
- Autenticação de usuários
- Controle de papéis (autor / usuário / visitante)
- Publicação restrita de diálogos
- Comentários moderados automaticamente (spam básico)
- Interface fluida e organizada

---

### 7. Objetivo do Sistema
Criar um espaço digital de diálogo estruturado, com centralidade autoral clara e participação reflexiva dos usuários por meio de perguntas e comentários, sem publicação livre de textos principais.

---

Se quiser, no próximo passo posso:
- adaptar esse prompt para **Bubble**, **FlutterFlow**, **Webflow**, **Softr** ou **Stack HTML+JS puro**  
- ou transformar isso em **especificação técnica em checklist** para desenvolvimento incremental.
