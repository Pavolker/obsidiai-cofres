---
source: DATAGPT
conversation_id: 69332872-da1c-8333-851b-b822bbfbcc72
title: "API pública CNPJ"
theme: IA PROMPTS
created: 2025-12-05T18:46:11.358803Z
message_count: 6
attachments_count: 0
---

# API pública CNPJ

- Tema: `IA PROMPTS`
- Conversation ID: `69332872-da1c-8333-851b-b822bbfbcc72`

## Transcrição

### user

O Cadastro Nacional da Pessoa Jurídica - CNPJ tem API publica ?

### assistant

Paulo — sim: existe uma API pública para consulta do entity["registry_key", "CNPJ", 0]. Aqui estão os detalhes principais:

---

### ✅ Serviço oficial  
A entity["organization", "Receita Federal do Brasil", 0] (RFB) disponibiliza no catálogo de APIs do governo o serviço chamado **“Consulta CNPJ”**. citeturn0search0  
- A versão listada é 2.0.2 (em 22/01/2021). citeturn0search0  
- Trata-se de um serviço REST com retorno em JSON. citeturn0search0  
- O serviço contempla informações cadastrais de pessoas jurídicas e outros arranjos jurídicos. citeturn0search0  
- O acesso exige autenticação, via OAuth, segundo a descrição de “Controle de acesso” no catálogo. citeturn0search0  

Portanto: **há uma API oficial**, mas não totalmente “livre e aberta” no sentido de sem autenticação nem limite.

---

### 🔍 Alternativas públicas/comerciais  
Além da API oficial, existem APIs privadas ou semi-públicas que permitem consulta de CNPJ com diferentes níveis de restrição:

- entity["brand", "CNPJ.ws", 0]: oferece API de consulta de CNPJ. citeturn0search1  
- entity["brand", "CNPJá", 0] (“open”): disponibiliza API gratuita, sem cadastro ou autenticação, com limite (por exemplo, 5 consultas/minuto) e defasagem de atualização. citeturn0search5turn0search12  
- entity["brand", "ReceitaWS", 0]: outro serviço que promove consultas via API. citeturn0search8  

---

### 📌 Observações importantes para uso  
- Mesmo que o serviço oficial exista, **o acesso pode estar restrito** (chave, limite, autenticação).  
- APIs “gratuitas” privadas podem ter **defasagem de atualização** ou cobertura parcial (ex: somente dados públicos agregados). Por exemplo, o CNPJá indica que os dados podem ter até 45 dias de defasagem. citeturn0search5turn0search12  
- Verificar termos de uso, licenciamento e limites de requisição é indispensível.  
- Para integração e análises, é importante considerar que nem todos os campos podem estar disponíveis ou atualizados em tempo real.

---

Se quiser, posso buscar **a documentação técnica completa** da API oficial da Receita (endpoints, parâmetros, esquemas JSON) e envio para você — quer isso, Paulo?

### user

para conjunto de dados, por exemplo CNPJ com maior incidencia em São paulo, qual seviço de API é mais indicado ?

### assistant

Paulo — para um cenário em que você quer encontrar **conjunto de dados** (por exemplo: os CNPJs com maior incidência em entity["place", "São Paulo", 0]) e não apenas consultar individualmente cada CNPJ, vale considerar os prós e contras das principais opções de APIs/datasets. A seguir listo duas abordagens + recomendação:

---

### ✅ APIs e datasets disponíveis  
**1. entity["software", "Brasil API", 0]**  
- Projeto que disponibiliza endpoints públicos para consulta de informações empresariais via CNPJ. citeturn0search5turn0search26  
- Vantagem: simples de usar, sem necessidade complexa de autenticação (em muitos casos).  
- Limitação: orientado à consulta de empresa por empresa — não necessariamente oferece “lista completa” ou “ranking por número de empresas por município”.

**2. entity["software", "CNPJ.ws", 0]**  
- API que permite consultar dados de um CNPJ individual, versão pública com limite de requisições (ex: 3 consultas/minuto) citeturn0search8turn0search9  
- Vantagem: bom nível de detalhe nos dados retornados.  
- Limitação: para “incidência em São Paulo” você teria de iterar ou compor uma lista de muitos CNPJs — não é um endpoint “agrupado”.

**3. Dataset aberto de base completa do entity["organization", "Receita Federal do Brasil", 0] / entity["organization", "Secretaria Especial da Receita Federal do Brasil", 0] (“Cadastro Nacional da Pessoa Jurídica”)**  
- Existe como conjunto de dados aberto: “Cadastro Nacional da Pessoa Jurídica – CNPJ” no portal dados.gov.br. citeturn0search1  
- Vantagem: permite baixar ou consultar em lote, fazer análise de incidência (quantos CNPJs por município, por CNAE, etc).  
- Limitação: pode exigir tratamento/limpeza de dados, e talvez não estar atualizado em tempo real; pode haver restrições de uso.

**4. Serviços comerciais de “lista segmentada de empresas”**  
- Exemplos como entity["organization", "DBDireto", 0] oferecem “lista segmentada de empresas” por filtros. citeturn0search20  
- Vantagem: já estruturado para análise de mercado.  
- Limitação: custo, menos transparência de cobertura.

---

### 🔍 Qual usar para “maior incidência em São Paulo”  
Se seu objetivo é **identificar quais CNPJs (ou quantos/que tipo de empresas) ocorrem em São Paulo com frequência** ou “ranking de incidência”, o mais indicado seria:

- Utilizar o dataset aberto “Cadastro Nacional da Pessoa Jurídica” para **análise em lote**, pois essa dá liberdade para filtrar por UF/município, CNAE, etc.  
- Complementar com uma API de consulta (BrasilAPI ou CNPJ.ws) se precisar de **detalhes específicos** de empresas selecionadas.  
- Se a solução for comercial e você precisa de acesso estruturado, considerar serviço pago (“lista segmentada”) que já agrega.

---

### 🎯 Minha recomendação técnica para você  
Para seu contexto (análise, tendências, cenário, filosofia dos dados):

1. Baixe o dataset “Cadastro Nacional da Pessoa Jurídica – CNPJ” no portal de dados abertos.  
2. Trate os dados para extrair:
   - Município ou UF (São Paulo)  
   - Número de empresas por município ou CNAE  
   - Outras métricas de incidência (porte, natureza jurídica, etc)  
3. Depois, se quiser investigar empresas específicas com alta incidência, utilize API como BrasilAPI ou CNPJ.ws para puxar dados individuais.  
4. Se for volume muito grande ou quiser acesso comercial, avaliar contrato com serviço pago.

Se quiser, posso localizar **links diretos e esquema de download** do dataset da Receita Federal + mostrar como filtrar para São Paulo (com código de exemplo Python/SQL) — quer que eu monte isso, Paulo?

### user

para conjunto de dados, por exemplo CNAEs  com maior incidencia em São paulo, qual serviço de API é mais indicado ?

### assistant

Paulo — para trabalhar com **incidência de códigos entity["classification_scheme", "CNAE", 0] em uma localidade (como o município ou estado de entity["place", "São Paulo", 0])**, algumas observações e recomendações de serviços/API para atender essa demanda:

---

### 🔍 O que é necessário para o objetivo  
Você pretende algo como “quais CNAEs ocorrem com maior frequência em São Paulo” ou “ranking de atividades econômicas por número de empresas no estado/município”. Para isso vai precisar de:  
- Base ou API que permita obter, para cada empresa, o seu código CNAE (primário ou secundário) e localização (UF, município).  
- Ou agregados que já façam a contagem dessas empresas por CNAE e localidade.  
- Capacidade de tratar volume de dados (não apenas consulta individual empresa-por-empresa).  
- Preferencialmente, dados relativamente atualizados.

---

### ✅ Serviços/API adequados  
Aqui estão algumas boas opções:

1. **entity["organization", "Instituto Brasileiro de Geografia e Estatística", 0] (IBGE) — API de CNAE**  
   - Existe a API “CNAE” do IBGE que permite consultar a estrutura da classificação (seções, divisões, grupos, classes, subclasses). citeturn0search2turn0search9turn0search14  
   - Essa API *não* provê por si só o número de empresas por CNAE+município. Ela é mais para o código/descrição da classificação.  
   - Portanto, útil para entender os códigos CNAE, mas não suficiente sozinho para a incidência em São Paulo.

2. **entity["dataset", "Cadastro Nacional da Pessoa Jurídica – CNPJ", 0] – base pública do cadastro de empresas**  
   - No portal de dados abertos existe o conjunto “Cadastro Nacional da Pessoa Jurídica – CNPJ”. citeturn0search15  
   - Essa base permite filtre por natureza jurídica, CNAE principal, localidade (UF/município), etc. Assim você poderia extrair todas as empresas no município de São Paulo, agrupar por CNAE e contar incidência.  
   - Essa abordagem exige download/tratamento de dados em lote (não necessariamente “consulta API instantânea de ranking”).  
   - Para seu perfil analítico isso pode ser bastante adequado.

3. **APIs comerciais ou semi-públicas com consulta por empresa**  
   - Exemplos: entity["brand", "CNPJá", 0] (“open” versão) permite consulta de CNPJ incluindo CNAE. citeturn0search16  
   - Essa abordagem permite consultar empresa por empresa, mas para ranking de incidência você teria que iterar muitas empresas — menos eficiente para “análise agregada”.  
   - Então é menos recomendado se o objetivo for “conjunto” ou “ranking”.

---

### 🎯 Qual recomendar para o seu caso  
Para seu objetivo (análise, tendência, cenário) de “CNAEs com maior incidência em São Paulo”, a abordagem mais indicada é:

- Utilizar a base “Cadastro Nacional da Pessoa Jurídica – CNPJ” para fazer **processamento em lote**: filtrar empresas por município/UF = São Paulo; agrupar por CNAE principal; calcular contagens; ordenar para verificar quais CNAEs têm maior número de empresas.  
- Utilizar a API do IBGE apenas para obter metadados da classificação CNAE, se precisar enriquecer (ex: descrição ou hierarquia).  
- Se for necessária automação ou atualização frequente, combinar com API comercial para consulta seletiva de empresas específicas.

---

Se você quiser, posso buscar **especificamente um conjunto de dados preparado (por exemplo “empresas por CNAE e município”) já disponível** ou **verificar se existe um endpoint público que devolva diretamente “número de empresas por CNAE por município”** — quer que eu faça isso, Paulo?
