---
source: DATAGPT
conversation_id: 694433c0-07cc-8330-95ab-53ca4197f8f0
title: "Prompt para app escritor"
theme: IA PROMPTS
created: 2025-12-18T17:09:20.037774Z
message_count: 2
attachments_count: 0
---

# Prompt para app escritor

- Tema: `IA PROMPTS`
- Conversation ID: `694433c0-07cc-8330-95ab-53ca4197f8f0`

## Transcrição

### user

Faça um prompt para um agente deverá no code  desenvolver um app para um escritor escrever contos, poemas, crônicas, pequenos textos. Esse app dever ser especializado em apoiar esse escritor no processo de escrita. Além de um editor de texto simples e eficiente, o app deverá ter uma coluna com uma janelas para consulta ortográfica e de significado de palavras, logo abaixo outra janela para consulta sobre rimas, baixo outra janela para consulta sobre autores e obra literárias, entre outras janelas úteis para um escritor. Ou seja, um verdadeira mesa de trabalho para um escritor contemporâneo que usa tecnologias para auxilia-lo no seu processo criativo. Ao final do trabalho, os textos deverão ser enviados para uma banco de dados, baixados como text, pdf ou .md. A mesa de trabalho do escritor deve ter um design condizente e significativo para o propósito da escrita

### assistant

Paulo, segue um **prompt completo**, pensado para ser usado diretamente com um **agente no-code** (ex.: Bubble, FlutterFlow, WeWeb, Softr, Retool, Appgyver, Glide ou equivalente), com foco exclusivo em **apoio técnico ao processo de escrita**.

---

## PROMPT — AGENTE NO-CODE  
**Desenvolvimento de App: Mesa de Trabalho Digital para Escritores**

Você é um **agente especializado em desenvolvimento de aplicações no-code**, com domínio de UX para escrita, arquitetura de informação, integração de APIs linguísticas e persistência de dados.  
Sua tarefa é **projetar e implementar um aplicativo web** destinado a **escritores de contos, poemas, crônicas e textos curtos**, atuando como uma **mesa de trabalho digital integrada** para o processo criativo contemporâneo.

### 1. OBJETIVO DO APLICATIVO
Desenvolver um ambiente único de escrita que:
- centralize ferramentas linguísticas, literárias e editoriais;
- reduza a fragmentação do processo criativo;
- funcione como apoio técnico, não como substituição autoral;
- permita escrita, consulta, revisão e arquivamento em um único fluxo.

### 2. PERFIL DO USUÁRIO
- Escritores de ficção, poesia e crônica;
- Uso intensivo de linguagem;
- Interesse em precisão semântica, referências literárias e ritmo textual;
- Escrita autoral, não automatizada.

### 3. ESTRUTURA GERAL DA INTERFACE (LAYOUT)
Interface em **duas colunas principais**:

#### COLUNA A — EDITOR CENTRAL
Editor de texto:
- Simples, responsivo e sem distrações;
- Suporte a textos longos;
- Contagem de palavras, caracteres e parágrafos;
- Marcação básica (itálico, negrito, título);
- Modo foco (ocultar barra lateral);
- Salvamento automático.

Formato interno preferencial: **Markdown**.

---

#### COLUNA B — PAINEL DE APOIO À ESCRITA (JANELAS EMPILHADAS)
Painel lateral fixo com janelas independentes:

1. **Consulta Ortográfica e Semântica**
   - Verificação ortográfica contextual;
   - Definição de palavras;
   - Etimologia (quando disponível);
   - Sinônimos e antônimos.

2. **Consulta de Rimas**
   - Rimas consonantes e toantes;
   - Classificação por tonicidade;
   - Filtro por número de sílabas.

3. **Consulta de Autores e Obras**
   - Mini-base de dados literária;
   - Busca por autor, obra ou movimento;
   - Dados sintéticos: período, estilo, temas recorrentes;
   - Possibilidade de expansão futura.

4. **Outras Janelas Úteis**
   - Dicionário de figuras de linguagem;
   - Métrica poética (opcional);
   - Notas laterais do autor;
   - Histórico de versões do texto.

Cada janela deve:
- Ser recolhível;
- Ter rolagem independente;
- Não interferir no editor central.

---

### 4. FUNCIONALIDADES DE ARMAZENAMENTO
Ao final (ou durante) o processo de escrita, permitir:

- Salvamento automático em **banco de dados** (estrutura simples: usuário, texto, data, tipo, versão);
- Exportação dos textos nos formatos:
  - `.txt`
  - `.pdf`
  - `.md`
- Organização por:
  - tipo de texto (conto, poema, crônica);
  - data;
  - projeto ou coleção.

---

### 5. ARQUITETURA TÉCNICA (NO-CODE)
- Backend no-code com banco de dados nativo da plataforma;
- APIs externas permitidas apenas para:
  - dicionários;
  - rimas;
  - bases literárias públicas;
- Separação clara entre:
  - camada de escrita;
  - camada de consulta;
  - camada de armazenamento.

---

### 6. PRINCÍPIOS DE DESIGN (UX/UI)
O design deve ser:
- Sóbrio;
- Silencioso visualmente;
- Tipografia legível e confortável;
- Paleta neutra (tons de papel, grafite, sépia ou cinza);
- Inspiração em:
  - mesas de trabalho;
  - cadernos de escrita;
  - ambientes de estudo e biblioteca.

Evitar:
- Gamificação;
- Elementos chamativos;
- Ícones desnecessários;
- Cores saturadas.

---

### 7. PRINCÍPIOS CONCEITUAIS
- O aplicativo **não escreve pelo autor**;
- Atua como **infraestrutura cognitiva de apoio**;
- Centraliza ferramentas que normalmente estariam dispersas;
- Valoriza o tempo, o silêncio e a concentração.

---

### 8. RESULTADO ESPERADO
Ao final do desenvolvimento, o app deve funcionar como:
- uma **mesa de trabalho digital completa para escritores**;
- um ambiente integrado de escrita, consulta e organização textual;
- uma base sólida para futuras expansões editoriais e analíticas.

---

Se quiser, no próximo passo posso:
- adaptar esse prompt para uma plataforma específica (Bubble, FlutterFlow, WeWeb etc.);
- detalhar o modelo de banco de dados;
- propor wireframe textual da interface;
- transformar esse prompt em documentação técnica para desenvolvedor no-code.
