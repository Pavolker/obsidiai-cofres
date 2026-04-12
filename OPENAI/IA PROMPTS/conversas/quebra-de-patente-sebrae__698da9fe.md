---
source: DATAGPT
conversation_id: 698da9fe-4f48-8327-aa72-ce16116d53bf
title: "Quebra de patente Sebrae"
theme: IA PROMPTS
created: 2026-02-12T10:24:05.995268Z
message_count: 4
attachments_count: 0
---

# Quebra de patente Sebrae

- Tema: `IA PROMPTS`
- Conversation ID: `698da9fe-4f48-8327-aa72-ce16116d53bf`

## Transcrição

### user

Fizemos um aplicativo sobre Circularidade de produto, para identificar o nível de circularidade de um produto de uma empresa, a partir de uma metodologia especifica da empresa italiana Cosmob - que é a nossa parceira nesse desenvolvimento. Depois de usar esse aplicativo em vários territórios para o Sebrae, fomos informados que essa empresa (o Sebrae) que nos contratou, que ela  agora  não precisa mais do nosso trabalho porque ela mesma irá desenvolver um aplicativo para medir a circularidade. Eu entendo que há ai uma clara "quebra de patente", já que a metodologia é nossa. Analise esse problema e liste os tópicos claramente ilegais dessa atitude do Sebrae

### assistant

Paulo, organizo a análise em três níveis: (1) natureza jurídica da metodologia e do aplicativo; (2) possíveis fundamentos de proteção; (3) hipóteses de ilicitude que poderiam existir caso determinados requisitos estejam presentes.

---

## 1. Natureza jurídica do objeto

Há três dimensões distintas:

1. **Metodologia de circularidade (modelo conceitual / critérios / indicadores)**  
2. **Aplicativo desenvolvido (software, código-fonte, arquitetura, banco de dados)**  
3. **Base de dados gerada nos territórios (respostas, relatórios, indicadores)**  

No direito brasileiro, cada uma dessas dimensões é protegida por regimes diferentes.

---

## 2. Regimes jurídicos aplicáveis

### 2.1 Patente – entity["law","Lei nº 9.279/1996","lei de propriedade industrial brasil"]  

A Lei de Propriedade Industrial (LPI) estabelece que:

- Métodos matemáticos, planos, regras e métodos de negócio **não são patenteáveis em si**.
- Para haver patente, é necessário: novidade, atividade inventiva e aplicação industrial.
- Patente exige **depósito prévio no INPI**.

Se não houve depósito e concessão de patente, juridicamente **não há “quebra de patente”**, pois patente só existe após concessão.

Mesmo que houvesse pedido em andamento, ainda não haveria direito exclusivo pleno até a concessão.

---

### 2.2 Software – entity["law","Lei nº 9.609/1998","lei de software brasil"]  

Protege:

- Código-fonte
- Código-objeto
- Estrutura original do programa

Não protege:

- Ideias
- Funcionalidades abstratas
- Conceitos metodológicos

Se o Sebrae desenvolver **novo código**, mesmo com funcionalidade semelhante, isso em regra não configura violação de direito autoral, salvo se houver cópia substancial do código ou engenharia reversa proibida contratualmente.

---

### 2.3 Direito Autoral – entity["law","Lei nº 9.610/1998","lei de direitos autorais brasil"]  

Protege:

- Textos da metodologia
- Relatórios
- Redação específica das perguntas
- Estrutura original do conteúdo

Não protege:

- Ideias em si
- Conceitos técnicos
- Modelos analíticos abstratos

---

### 2.4 Segredo industrial / concorrência desleal

A LPI também protege:

- Informações confidenciais
- Know-how protegido por cláusula contratual
- Uso indevido de informação estratégica obtida sob confidencialidade

Aqui entra um ponto central: **o contrato firmado com o Sebrae**.

---

## 3. Possíveis hipóteses de ilegalidade

A atitude do Sebrae pode ser juridicamente questionável **apenas se ocorrer uma das situações abaixo**:

---

### 3.1 Violação contratual

Se houver no contrato:

- Cláusula de exclusividade
- Cláusula de não replicação
- Cláusula de não concorrência
- Cláusula de confidencialidade
- Proibição de desenvolvimento derivado

E o Sebrae decidir desenvolver aplicativo com base direta na metodologia contratada, pode haver:

- Inadimplemento contratual
- Violação de obrigação de confidencialidade
- Uso indevido de know-how contratado

Sem essas cláusulas, o contratante pode, em regra, usar o aprendizado obtido.

---

### 3.2 Apropriação de código ou estrutura técnica

Se houver:

- Uso do mesmo código-fonte
- Reprodução de arquitetura proprietária
- Cópia de banco de dados
- Replicação estrutural comprovável

Pode haver violação da Lei de Software.

Isso exige perícia técnica comparativa.

---

### 3.3 Uso indevido de base de dados

Se o Sebrae utilizar:

- Dados coletados via seu sistema
- Indicadores proprietários
- Algoritmo específico desenvolvido por vocês

Sem cessão formal desses direitos, pode haver violação de direito patrimonial.

---

### 3.4 Uso de metodologia protegida como segredo industrial

Se a metodologia:

- Não era pública
- Era confidencial
- Foi compartilhada apenas sob cláusula de sigilo

E agora é replicada internamente, pode configurar concorrência desleal.

---

## 4. O que provavelmente NÃO é ilegal

É importante separar juridicamente:

- Desenvolver um novo aplicativo com mesma finalidade
- Criar ferramenta própria após experiência contratada
- Internalizar conhecimento adquirido

Se não houver patente concedida, nem cláusula restritiva, nem cópia de código, a internalização do aprendizado pelo contratante não é automaticamente ilícita.

---

## 5. Ponto estratégico central

A questão jurídica não é “quebra de patente”, mas sim:

- Há patente concedida?
- O contrato restringia replicação?
- A metodologia é protegida como segredo industrial?
- Houve cessão de direitos patrimoniais?
- O código pertence a quem segundo o contrato?

Sem esses elementos, o caso tende a ser caracterizado como internalização tecnológica pelo contratante.

---

## 6. Próximo passo técnico-jurídico

Para análise objetiva, é necessário:

1. Examinar o contrato integral
2. Identificar cláusulas de propriedade intelectual
3. Verificar cessão de direitos
4. Verificar cláusulas de confidencialidade
5. Avaliar titularidade do código
6. Verificar eventual registro no INPI ou Biblioteca Nacional

Se quiser, posso estruturar um checklist técnico-jurídico detalhado para auditoria do seu contrato com o Sebrae.

### user

O conteúdo do aplicativo, a metodologia, as 12 perguntas que o aplicativo processa, podem ser copiados pela empresa ?

### assistant

Paulo, a resposta depende da natureza jurídica de cada elemento. Organizo em três camadas: (1) metodologia, (2) perguntas, (3) estrutura do aplicativo.

---

## 1. Metodologia (modelo conceitual)

Regra geral no Brasil:

- Ideias, métodos, modelos conceituais e sistemas de avaliação **não são protegidos como exclusividade automática**.
- A proteção só existe se:
  - houver **patente concedida** (entity["law","Lei nº 9.279/1996","lei de propriedade industrial brasil"]),
  - ou se estiverem protegidos como **segredo industrial sob contrato**,
  - ou se houver cláusula contratual limitando uso.

Sem patente concedida ou cláusula contratual restritiva, a metodologia pode ser replicada conceitualmente.

---

## 2. As 12 perguntas

Aqui a análise muda.

Segundo a entity["law","Lei nº 9.610/1998","lei de direitos autorais brasil"]:

- Ideias não são protegidas.
- A **forma de expressão textual específica é protegida**.

Portanto:

### Podem copiar:
- O conceito por trás das perguntas.
- O tipo de indicador avaliado.
- O critério lógico de medição.

### Não podem copiar:
- A redação literal das perguntas.
- A organização textual original.
- A estrutura criativa específica se houver originalidade.

Se as perguntas forem copiadas palavra por palavra, há risco de violação autoral.

Se forem reformuladas mantendo a mesma lógica, tende a não haver infração autoral.

---

## 3. Estrutura lógica e algoritmo

Segundo a entity["law","Lei nº 9.609/1998","lei de software brasil"]:

- Código-fonte é protegido.
- Algoritmo enquanto ideia abstrata não é protegido.
- Implementação concreta do algoritmo é protegida.

Se o Sebrae:

- Copiar o código → possível infração.
- Criar código novo com mesma lógica → em regra, permitido.
- Reproduzir estrutura muito específica e distintiva → pode gerar discussão técnica.

---

## 4. Elemento decisivo: contrato

A questão central não é apenas autoral, mas contratual.

Se o contrato:

- Não previa cessão de direitos,
- Não previa transferência de metodologia,
- Não autorizava uso posterior,
- Não previa desenvolvimento derivado,

Então o uso pode ser discutido sob violação contratual.

Se o contrato previa:

- Entrega da metodologia,
- Transferência de know-how,
- Cessão ampla de direitos,

Então o contratante pode internalizar.

---

## 5. Resumo objetivo

Eles podem:

- Criar novo aplicativo próprio.
- Desenvolver metodologia similar.
- Reformular perguntas com base nos mesmos critérios.

Eles não podem:

- Copiar literalmente as 12 perguntas.
- Copiar o código-fonte.
- Usar base de dados proprietária.
- Descumprir cláusulas contratuais de confidencialidade.

---

## 6. Ponto estrutural

O conflito jurídico só se sustenta se houver:

- Violação autoral textual,
- Violação de software,
- Violação contratual,
- Uso indevido de segredo industrial.

Sem esses elementos, a replicação conceitual tende a ser juridicamente possível.

Se quiser, posso montar uma matriz de risco jurídico específica para o seu caso, separando risco baixo, médio e alto conforme o tipo de reprodução.
