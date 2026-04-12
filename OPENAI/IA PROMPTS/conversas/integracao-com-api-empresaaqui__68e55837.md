---
source: DATAGPT
conversation_id: 68e55837-410c-8333-a59e-03f3fad06a46
title: "Integração com API Empresaaqui"
theme: IA PROMPTS
created: 2025-10-07T18:15:46.176042Z
message_count: 2
attachments_count: 0
---

# Integração com API Empresaaqui

- Tema: `IA PROMPTS`
- Conversation ID: `68e55837-410c-8333-a59e-03f3fad06a46`

## Transcrição

### user

Quero fazer um aplicativo que faça a busca de dados em uma empresa denominada "Empresaaqui", que assino para ter acesso a dados de empresas brasileiras. A mepresa permite integração com API e fornece a seguinte orientação para essa coneção: "Utilização Prática da API
Veja abaixo como utilizar os dados via requisição JSON:

Como realizar a requisição via PHP:

// ---- INICIE AS REQUISIÇÕES
$ch = curl_init();
				
// ---- DEFINA O ENDPOINT, INCLUINDO SEU TOKEN, E O CNPJ DA EMPRESA A SER RETORNADO SEM PONTUAÇÃO
$Caminho="https://www.empresaqui.com.br/api/SEU_TOKEN/CNPJ_SEM_PONTUACAO;

// ---- DÊ O SET NAS CONFIGURAÇÕES PADRÕES DE CURL
curl_setopt($ch, CURLOPT_URL, $Caminho);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($ch, CURLOPT_HEADER, FALSE);

// ---- EXECUTE O CURL PARA UMA VARIÁVEL
$response = curl_exec($ch);

// ---- FECHE A CONEXÃO EXTERNA
curl_close($ch);

// ---- DECODIFIQUE OS DADOS JSON PARA ARRAY PHP
$objeto=json_decode($response);
				
Quais os nomes das variáveis e como identificá-las:

// ---- DADOS BÁSICOS DE CADASTRO E CONTATO

$objeto->cnpj;
$objeto->razao;
$objeto->fantasia;
$objeto->email;
$objeto->ddd_1;
$objeto->tel_1;
$objeto->ddd_2;
$objeto->tel_2;
$objeto->email;
$objeto->site;

// ---- DADOS DE ENDEREÇO E LOCALIZAÇÃO

$objeto->log_tipo;
$objeto->log_nome;
$objeto->log_num;
$objeto->log_comp;
$objeto->log_bairro;
$objeto->log_municipio;
$objeto->log_uf;

// ---- DADOS ESPECÍFICOS E TRIBUTÁRIOS

$objeto->cnae_principal;
$objeto->cnae_secundario;
$objeto->matriz; // 1 - MATRIZ; 2 - FILIAL; 
$objeto->situacao_cadastral; // 1 - NULA; 2 ATIVA; 3 SUSPENSA; 4 INAPTA; 8 BAIXADA;
$objeto->data_sit_cad;
$objeto->natureza_juridica; // CÓDIGO CORRESPONDENTE A TABELA DE NATUREZA JURÍDICA
$objeto->data_abertura;
$objeto->opcao_mei;
$objeto->data_mei;
$objeto->data_exc_mei;
$objeto->opcao_simples;
$objeto->data_simples;
$objeto->data_exc_simples;
$objeto->porte; // 0 - NÃO INFORMADO; 1 - MICROEMPRESA; 3 - PEQUENO PORTE; 5 - MÉDIO/GRANDE PORTE
$objeto->capital_social;
$objeto->regime_tributario;
$objeto->faturamento;
$objeto->quadro_funcionarios;
				
Variáveis em array:


// ---- PROGRAMAS ESPECIAIS

$objeto->programas_especiais; // possíveis valores: "EMPRESA CIDADÃ", "IMPORTAÇÃO E EXPORTACAO", "PAT", "RECUPERACAO JUDICIAL".

*importante:* Uma empresa pode fazer parte de vários programas especiais ou de nenhum, caso nenhum o array estará vazio.

// ---- DADOS DO QUADRO SOCIETÁRIO EM ARRAY

$objeto->socios_nome;
$objeto->socios_cpf_cnpj;
$objeto->socios_entrada;
$objeto->socios_qualificacao;
$objeto->socios_faixa_etaria;

FAIXA ETÁRIA É DENIFIDA POR CÓDIGOS QUE SIGNIFICAM:
CÓDIGO 1 EQUIVALE A: "0 A 12 ANOS";
CÓDIGO 2 EQUIVALE A: "13 A 20 ANOS";
CÓDIGO 3 EQUIVALE A: "21 A 30 ANOS";
CÓDIGO 4 EQUIVALE A: "31 A 40 ANOS";
CÓDIGO 5 EQUIVALE A: "41 A 50 ANOS";
CÓDIGO 6 EQUIVALE A: "51 A 60 ANOS";
CÓDIGO 7 EQUIVALE A: "61 A 70 ANOS";
CÓDIGO 8 EQUIVALE A: "71 A 80 ANOS";
CÓDIGO 9 EQUIVALE A: "ACIMA DE 80 ANOS";
CÓDIGO 0 EQUIVALE A: "NÃO SE APLICA";

// ---- DADOS DAS DÍVIDAS FEDERAIS ATIVAS

$objeto->dividas_numero;
$objeto->dividas_tipo_devedor;
$objeto->dividas_tipo_situacao;
$objeto->dividas_inscricao;
$objeto->dividas_receita;
$objeto->dividas_data;
$objeto->dividas_indicador;
$objeto->dividas_valor;

$objeto->historicoDividasPorTrimestre; // Histórico de dívidas trimestrais desde 2020. Cada item do array representa um trimestre, contendo os campos trimestreAno e valor.
				
$objeto->historicoRegimePorAno; // Histórico de regime tributário por ano. Cada item do array representa um ano, contendo os campos Ano e Regime." . Como posso conecar com essa empres e ter acesso aos dados via API ?

### assistant

Para conectar-se à plataforma **Empresaaqui** via API e acessar os dados de empresas brasileiras, como informado, você precisa:

---

## **1. Ter um Token de Acesso**
Você deve possuir um token de autenticação fornecido pela Empresaaqui. Ele é inserido diretamente na URL da requisição.

---

## **2. Fazer uma Requisição HTTP (via `curl`, `fetch`, `axios`, etc.)**

### Exemplo em PHP (como fornecido):
```php
$ch = curl_init();

$cnpj = "12345678000190"; // Sem pontuação
$token = "SEU_TOKEN"; // Substitua pelo seu token
$url = "https://www.empresaqui.com.br/api/$token/$cnpj";

curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($ch, CURLOPT_HEADER, FALSE);

$response = curl_exec($ch);
curl_close($ch);

$objeto = json_decode($response);

// Exemplo de uso
echo $objeto->razao;
```

---

## **3. Alternativa com JavaScript (Node.js com `axios`):**
```js
const axios = require('axios');

const token = 'SEU_TOKEN';
const cnpj = '12345678000190'; // sem pontuação
const url = `https://www.empresaqui.com.br/api/${token}/${cnpj}`;

axios.get(url)
  .then(response => {
    const dados = response.data;
    console.log(dados.razao);
  })
  .catch(error => {
    console.error('Erro ao buscar dados:', error);
  });
```

---

## **4. Estrutura de Resposta Esperada**
A resposta da API vem em **JSON**, com os seguintes dados disponíveis (organizados por grupos):

### a) **Dados Cadastrais**
- `cnpj`, `razao`, `fantasia`, `email`, `site`, `tel_1`, `tel_2`, `ddd_1`, `ddd_2`

### b) **Endereço**
- `log_tipo`, `log_nome`, `log_num`, `log_comp`, `log_bairro`, `log_municipio`, `log_uf`

### c) **Informações Tributárias**
- `cnae_principal`, `cnae_secundario`, `matriz`, `situacao_cadastral`, `data_sit_cad`, `natureza_juridica`, `data_abertura`

### d) **Regimes Especiais**
- `opcao_mei`, `data_mei`, `data_exc_mei`, `opcao_simples`, `data_simples`, `data_exc_simples`, `regime_tributario`, `porte`

### e) **Quadro Societário** (arrays):
- `socios_nome`, `socios_cpf_cnpj`, `socios_entrada`, `socios_qualificacao`, `socios_faixa_etaria`

### f) **Dívidas** (arrays):
- `dividas_numero`, `dividas_tipo_devedor`, `dividas_tipo_situacao`, `dividas_valor`, etc.

### g) **Históricos**:
- `historicoDividasPorTrimestre[]` → campos `trimestreAno`, `valor`
- `historicoRegimePorAno[]` → campos `ano`, `regime`

---

## **5. Considerações Técnicas**
- O CNPJ deve ser passado **sem pontuação**.
- O token deve estar correto e ativo, senão a resposta será um erro HTTP (ex: 403 ou 401).
- A API é pública apenas para assinantes do serviço. Consulte os termos de uso ou suporte técnico da Empresaaqui para limites de requisições ou uso em produção.

---

## **6. Boas Práticas**
- Implemente **tratamento de erros** (CNPJ inválido, empresa inexistente, token expirado).
- Cache local (ex: em Redis ou DB) pode reduzir chamadas repetidas.
- Evite ultrapassar limites de rate limit que o serviço possa impor.

---

Se quiser, posso gerar um script completo em JavaScript, Python, PHP ou integrável a um backend (ex: Express, Flask) para que você use diretamente no seu aplicativo. Deseja?
