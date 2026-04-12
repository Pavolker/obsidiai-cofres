---
source: DATAGPT
conversation_id: 6898ef30-6038-832a-9580-7cd0383e308b
title: "Fórmula dos primos de Mersenne"
theme: TECNOLOGIA
created: 2025-08-10T19:12:49.474016Z
message_count: 4
attachments_count: 0
---

# Fórmula dos primos de Mersenne

- Tema: `TECNOLOGIA`
- Conversation ID: `6898ef30-6038-832a-9580-7cd0383e308b`

## Transcrição

### user

Qual é a formula de Marin Mersnne pra os numeros primos

### assistant

A fórmula associada a **Marin Mersenne** não é exatamente uma fórmula “geradora” de todos os números primos, mas uma expressão que define um tipo especial de primo: o **primo de Mersenne**.  

A forma geral é:  

\\[
M_p = 2^p - 1
\\]

onde:  
- \\(p\\) **precisa ser um número primo**;  
- \\(M_p\\) **pode ser primo ou não** — nem todo \\(p\\) primo gera um \\(M_p\\) primo.  

**Exemplos:**  
1. \\(p = 2\\) → \\(M_2 = 2^2 - 1 = 3\\) (primo)  
2. \\(p = 3\\) → \\(M_3 = 2^3 - 1 = 7\\) (primo)  
3. \\(p = 5\\) → \\(M_5 = 2^5 - 1 = 31\\) (primo)  
4. \\(p = 11\\) → \\(M_{11} = 2047 = 23 \\times 89\\) (**não é primo**)  

Esses primos de Mersenne têm importância especial porque estão diretamente ligados aos **números perfeitos** (pela fórmula de Euclides: \\(N = 2^{p-1}(2^p - 1)\\) quando \\(M_p\\) é primo).  

Se quiser, posso te listar todos os \\(p\\) conhecidos que geram primos de Mersenne até hoje e explicar como Mersenne errou e acertou na lista original dele. Quer que eu faça?

### user

Como Mersenne errou ?

### assistant

O erro de Marin Mersenne está ligado à lista que ele publicou em 1644, na obra *Cogitata Physico-Mathematica*, onde tentou identificar **todos os primos de Mersenne** para \\( p \\) até 257.  

Ele **acertou alguns**, mas **errou outros**, por duas razões principais:  
1. **Falta de métodos rápidos de teste de primalidade** na época.  
2. **Confusão entre “p ser primo” e “2^p − 1 ser primo”**, que nem sempre acontece.  

---

## 📜 A lista original de Mersenne
Ele afirmou que \\( 2^p - 1 \\) era primo **apenas** para os seguintes \\( p \\):  

\\[
p = 2, 3, 5, 7, 13, 17, 19, 31, 67, 127, 257
\\]

---

## ✅ Acertos
- Ele realmente incluiu vários corretos: \\( p = 2, 3, 5, 7, 13, 17, 19, 31, 127 \\) geram primos de Mersenne.  
- Esses valores são usados até hoje na lista dos primos confirmados.  

---

## ❌ Erros
- **Falsos positivos**:  
  - \\( p = 67 \\) → \\( 2^{67} - 1 \\) **não é primo** (fatorado em 193707721 × 761838257287).  
  - \\( p = 257 \\) → também **não é primo**.  

- **Omissões (falsos negativos)**: ele deixou de fora alguns que realmente geram primos, como:  
  - \\( p = 61 \\)  
  - \\( p = 89 \\)  
  - \\( p = 107 \\)  
  - e outros descobertos depois.  

---

## 🧠 Por que o erro é compreensível?
Em 1644:
- Não existiam testes como o **Lucas–Lehmer** (criado só em 1856 e aprimorado no século XX).  
- Números como \\( 2^{257} - 1 \\) têm **78 dígitos**, impossível de verificar na época sem fatoração manual gigantesca.  

---

Se quiser, posso te montar uma **tabela comparando a lista original de Mersenne com a lista correta de hoje**, mostrando onde ele acertou e onde errou. Isso deixa bem claro os enganos dele. Quer que eu faça essa comparação?
