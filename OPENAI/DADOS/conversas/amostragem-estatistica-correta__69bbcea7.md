---
source: DATAGPT
conversation_id: 69bbcea7-fcfc-8331-9b84-79b8ca2e4f8d
title: "Amostragem Estatística Correta"
theme: DADOS
created: 2026-03-19T10:23:48.552440Z
message_count: 2
attachments_count: 0
---

# Amostragem Estatística Correta

- Tema: `DADOS`
- Conversation ID: `69bbcea7-fcfc-8331-9b84-79b8ca2e4f8d`

## Transcrição

### user

Considerando um universo de 1000 empresas, quais são os parâmetros para tirar uma mostra estatisticamente correta, que represente esse universo ?

### assistant

Para definir uma amostra estatisticamente válida a partir de um universo de **1000 empresas**, é necessário especificar e calcular alguns parâmetros fundamentais da **teoria de amostragem**.

---

## 1. Parâmetros necessários

### a) Tamanho da população (N)
- N = 1000 empresas

### b) Nível de confiança (Z)
Valores usuais:
- 90% → Z = 1,645  
- 95% → Z = 1,96  
- 99% → Z = 2,576  

### c) Margem de erro (e)
Valores usuais:
- 5% (0,05)
- 3% (0,03)
- 10% (0,10)

### d) Proporção estimada (p)
- Quando desconhecida: **p = 0,5**  
(assume máxima variabilidade → maior tamanho de amostra)

### e) Complemento (q)
- q = 1 − p

---

## 2. Fórmula (população finita)

O tamanho da amostra (n) é calculado por:

\\[
n = \\frac{Z^2 \\cdot p \\cdot q \\cdot N}{e^2 \\cdot (N - 1) + Z^2 \\cdot p \\cdot q}
\\]

---

## 3. Exemplo padrão (mais utilizado)

Parâmetros:
- N = 1000  
- Z = 1,96 (95% confiança)  
- e = 0,05 (5% erro)  
- p = 0,5  

Substituindo:

\\[
n \\approx 278
\\]

---

## 4. Tabela de referência (para N = 1000)

| Nível de confiança | Margem de erro | Tamanho da amostra |
|------------------|---------------|--------------------|
| 90%              | 5%            | ~214               |
| 95%              | 5%            | ~278               |
| 95%              | 3%            | ~516               |
| 99%              | 5%            | ~400               |
| 95%              | 10%           | ~88                |

---

## 5. Tipos de amostragem (estrutura)

Além do tamanho, a **forma de seleção** define a representatividade:

### a) Aleatória simples
- Todas as empresas têm igual probabilidade

### b) Estratificada
- Divide o universo em grupos homogêneos (ex: porte, setor, região)
- Amostra proporcional por estrato

### c) Sistemática
- Seleção por intervalo (ex: a cada 3 empresas)

### d) Por conglomerados
- Seleção por grupos (ex: cidades, clusters)

---

## 6. Parâmetros de controle de qualidade

Para garantir representatividade:

- Cobertura do universo (lista completa das empresas)
- Taxa de resposta (não-resposta controlada)
- Distribuição proporcional (quando estratificada)
- Controle de viés (seleção e resposta)

---

## 7. Interpretação operacional

Para um universo de 1000 empresas:

- **Amostra padrão robusta**: ~278 empresas  
- **Amostra mais precisa (3%)**: ~516 empresas  
- **Amostra exploratória (10%)**: ~88 empresas  

---

Se quiser, posso estruturar isso dentro do seu modelo de diagnóstico (por exemplo: aplicação no app de circularidade ou em matriz foresight), incluindo definição de estratos por CNAE, porte e território.
