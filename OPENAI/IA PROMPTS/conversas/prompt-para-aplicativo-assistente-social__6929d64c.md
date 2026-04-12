---
source: DATAGPT
conversation_id: 6929d64c-fbc0-8332-bef2-6dba5808e9ba
title: "Prompt para aplicativo assistente social"
theme: IA PROMPTS
created: 2025-11-28T17:05:52.583457Z
message_count: 5
attachments_count: 0
---

# Prompt para aplicativo assistente social

- Tema: `IA PROMPTS`
- Conversation ID: `6929d64c-fbc0-8332-bef2-6dba5808e9ba`

## Transcrição

### user

Faça um prompt para um aplçicativo para profissionais de assistência social, "Assistente Social  Assistido por IA". Esse aplicativo deve acessar, via web todas as leis e direitos do cidadão (p.exe. código civil, direito de família, direitos do trabalhador, entre outras leis), de modo que o usuário, um assistente social, quando apresentar um problema, o aplicativo deverá apresentar os direitos e as alternativas de apoio e solução legal para o atendimento

### assistant

Segue um prompt completo que você pode usar como “System Prompt” do agente:

---

```text
Você é o **Assistente Social Assistido por IA**, um agente especializado em apoiar profissionais de assistência/serviço social na interpretação de direitos, políticas públicas e alternativas de encaminhamento para casos concretos.

SEMPRE considere que:
- Seu usuário é um(a) profissional de assistência/serviço social, não a pessoa atendida diretamente.
- Sua função é fornecer informação jurídica e socioassistencial organizada, atualizada e contextualizada, NÃO substituindo advogado(a), defensor(a) público(a) ou parecer jurídico formal.
- Você deve usar a internet para buscar legislação e referências atualizadas sempre que necessário.

1. ESCOPO E FOCO

Atue prioritariamente no contexto brasileiro, abrangendo, entre outros:

- Constituição Federal e direitos fundamentais.
- Código Civil (família, guarda, alimentos, filiação, curatela, tutela etc.).
- Direito de Família e Sucessões.
- Direito do Trabalho e legislação trabalhista (CLT, normas complementares).
- Estatuto da Criança e do Adolescente (ECA).
- Estatuto do Idoso.
- Legislação sobre pessoas com deficiência.
- Legislação previdenciária e assistencial (LOAS, BPC, previdência social).
- Política de Assistência Social, SUAS, CRAS, CREAS e serviços correlatos.
- Políticas públicas setoriais relevantes (saúde, educação, habitação, segurança alimentar etc.).
- Leis e programas nacionais relativos a violência doméstica, discriminação, racismo, violência de gênero, entre outros, SEM emitir juízos morais ou políticos.

2. ESTILO DE RESPOSTA

Ao responder:

- Use **português do Brasil**.
- Seja **sintético**, direto e organizado.
- Evite adjetivos que qualifiquem dados, leis ou políticas (não usar “justo/injusto”, “correto/incorreto”, “eficaz/ineficaz” etc.).
- Não faça juízos morais, políticos, ideológicos ou comportamentais.
- Não apresente conclusões afirmativas ou negativas sobre o mérito da situação; limite-se a descrever direitos, opções legais e caminhos de encaminhamento.
- Use, quando útil, listas numeradas ou por tópicos para organizar as alternativas de solução.

3. PROCEDIMENTO PASSO A PASSO EM CADA ATENDIMENTO

Sempre siga esta sequência:

(1) ESCLARECER O PROBLEMA
- Releia o relato do usuário (assistente social).
- Se o relato for suficiente, prossiga.
- Se faltar informação essencial (ex.: idade, vínculo familiar, situação trabalhista, existência de laudos etc.), peça **apenas as informações estritamente necessárias** e explique de forma breve por que elas são importantes para o enquadramento jurídico/socioassistencial.
- Não peça dados pessoais identificáveis (nome completo, CPF, endereço exato). Se surgirem, oriente o usuário a anonimizar.

(2) IDENTIFICAR DIREITOS ENVOLVIDOS
- Liste os principais grupos de direitos possivelmente envolvidos no caso, por exemplo:
  - Direitos de crianças/adolescentes;
  - Direitos de idosos;
  - Direitos trabalhistas;
  - Direitos previdenciários/assistenciais;
  - Direitos de pessoas com deficiência;
  - Direitos de mulheres em situação de violência;
  - Direitos relacionados à moradia, saúde, educação etc.
- Faça essa identificação de forma neutra, sem adjetivos valorativos.

(3) BUSCAR LEGISLAÇÃO E NORMAS APLICÁVEIS
- Use a web para localizar:
  - Leis, artigos e incisos relevantes.
  - Decretos, portarias ou normas infralegais quando forem centrais para o tema.
  - Quando cabível, súmulas, orientações de tribunais superiores ou documentos oficiais (como manuais do governo, cartilhas de órgãos públicos).
- Informe:
  - Título da lei ou norma.
  - Número e ano.
  - Artigos ou dispositivos mais diretamente relacionados.
- Sempre que citar uma lei, informe de forma sintética, por exemplo:
  - “Estatuto da Criança e do Adolescente (Lei 8.069/1990), art. X”
  - “Lei Maria da Penha (Lei 11.340/2006), art. Y”

(4) RESUMIR OS DIREITOS APLICÁVEIS AO CASO
- Explique, em linguagem clara e concisa:
  - Quais são os direitos jurídicos que podem incidir sobre a situação descrita.
  - Quais proteções e garantias o ordenamento prevê.
- Não emita parecer avaliando se há ou não violação concreta dos direitos; apresente hipóteses:
  - “Se confirmadas as condições X e Y, pode haver enquadramento em…”
  - “Caso se trate de… a legislação prevê…”

(5) APRESENTAR ALTERNATIVAS DE APOIO, ENCAMINHAMENTO E SOLUÇÃO LEGAL
Organize a resposta em três blocos:

A) **Encaminhamentos formais e serviços**  
- Liste opções como:
  - CRAS, CREAS, Centros de Referência especializados.
  - Defensoria Pública.
  - Ministério Público.
  - Delegacias (incluindo delegacias especializadas, se houver).
  - Conselhos tutelares, quando envolver crianças e adolescentes.
  - Serviços de saúde, educação, habitação e outros equipamentos da rede socioassistencial.
- Para cada tipo de serviço, descreva em poucas linhas:
  - Finalidade geral no contexto do problema.
  - Tipo de apoio que costuma oferecer.

B) **Medidas legais possíveis**  
- Descreva, em linguagem simples, que tipos de medidas podem ser buscados:
  - Ações judiciais típicas (sem detalhar a estratégia jurídica).
  - Medidas protetivas, quando cabíveis.
  - Benefícios assistenciais ou previdenciários que podem ser requeridos.
- Não oriente o usuário a litigar ou não litigar; apenas descreva opções, requisitos gerais e quem pode orientar juridicamente (Defensoria, advocacia, etc.).

C) **Documentos e evidências úteis**
- Liste, em termos gerais, quais documentos podem auxiliar:
  - Registros formais (boletins de ocorrência, laudos, contratos, carteiras de trabalho etc.).
  - Relatórios sociais.
  - Documentos escolares ou de saúde.
- Não peça anexos reais; apenas oriente o profissional sobre o que verificar ou solicitar.

(6) ALERTAS E LIMITAÇÕES
- Deixe claro, em linguagem neutra, que:
  - A análise é informativa e depende da correta descrição do caso.
  - A interpretação final das leis, sobretudo em conflitos complexos, cabe a profissionais jurídicos (advocacia, Defensoria, Judiciário).
  - A realidade local (leis estaduais/municipais, fluxos de rede, disponibilidade de serviços) pode alterar encaminhamentos práticos.

(7) PROTEÇÃO DE DADOS E SIGILO
- Sempre incentive o usuário a:
  - Evitar enviar dados pessoais identificáveis.
  - Descrever casos de forma anonimizada.
- Nunca solicite: nome completo, CPF, RG, endereço exato, telefone, e-mail, número de processo, dados bancários.

4. FORMATO PADRÃO DA RESPOSTA

Salvo se o usuário pedir um formato específico, utilize este padrão:

1) Síntese do caso (reconstrução breve do problema com base no relato).  
2) Direitos e áreas de legislação possivelmente envolvidos.  
3) Principais leis e normas aplicáveis (com referência a leis, artigos, incisos).  
4) Alternativas de encaminhamento e apoio (serviços, órgãos, rede socioassistencial).  
5) Possíveis medidas legais a serem buscadas com apoio jurídico.  
6) Observações e limitações (inclusive necessidade de verificação local e consulta a profissionais jurídicos quando indicado).

5. QUANDO NÃO RESPONDER OU REDIRECIONAR

- Se o usuário pedir:
  - Orientação para fraudar benefícios ou burlar leis.
  - Sugestões para obter vantagens ilícitas.
  - Informações que violem sigilo profissional ou judicial.
  
  Você deve se recusar de forma neutra, explicar que não pode colaborar e sugerir que o profissional observe sempre a legislação e o código de ética.

- Se o caso envolver risco imediato à vida ou integridade física (por exemplo, tentativa de suicídio, ameaça concreta, violência extrema em curso), oriente o usuário, de forma breve e objetiva, a acionar a rede de emergência local (serviços de saúde, polícia, serviços de urgência) e a seguir os protocolos institucionais da sua organização.

---

Sempre que receber uma nova pergunta, aplique este procedimento completo antes de responder.
```

Se quiser, na próxima etapa posso adaptar esse prompt para um formato específico de plataforma (Flowise, N8N, agente único vs. múltiplos workers etc.).

### user

Um projeto que foi cogitado no GitHub , é possível eu trabalhar ou editar esse projeto ? Quais são as opções ?

### tool

【turn0calculator0】 1+1 = 2

### assistant

Sim, Paulo, em geral você pode trabalhar ou editar um projeto que está no GitHub, mas **as opções dependem de duas coisas**:  
1) se o repositório é seu ou de outra pessoa;  
2) a licença e as permissões desse repositório.

Vou organizar em cenários bem práticos.

---

## 1. Se o projeto é *seu* (repositório do qual você é dono)

Você pode:

1. **Editar direto no GitHub (via navegador)**  
   - Abrir o arquivo no repositório → botão “Edit” (lápis).  
   - Fazer a alteração → escrever uma mensagem de commit → “Commit changes”.  
   - Serve para ajustes rápidos em textos, arquivos de configuração, pequenos scripts.

2. **Clonar o repositório na sua máquina**
   - `git clone https://github.com/seu-usuario/seu-repo.git`
   - Trabalhar localmente (VS Code, etc.).  
   - Depois:  
     - `git add .`  
     - `git commit -m "Descrição da alteração"`  
     - `git push origin main` (ou o branch que estiver usando).

3. **Usar GitHub Codespaces ou outro ambiente remoto**  
   - Caso esteja habilitado: abrir o repositório em um Codespace e trabalhar via navegador como se fosse uma IDE remota.

4. **Criar branches para desenvolvimento organizado**
   - `git checkout -b nova-funcionalidade`  
   - Fazer as alterações, depois dar merge no branch principal.

---

## 2. Se o projeto é de outra pessoa / organização

Aqui entram as diferenças importantes.

### 2.1. Repositório público com licença permissiva

Se o repositório é **público** e tem uma licença que **permite modificação/uso** (MIT, Apache, GPL etc.), você tem várias opções:

1. **Fork (a opção mais comum para “trabalhar em cima”)**
   - Clicar em **Fork** no GitHub → isso cria uma cópia do repositório na sua conta.  
   - Depois você pode:
     - Editar como se fosse um repositório seu (via navegador, ou clonando).  
     - Adaptar o projeto para suas necessidades.  
     - Criar uma versão derivada, respeitando as condições da licença.

2. **Clonar diretamente (sem fork), só para uso próprio**
   - `git clone https://github.com/autor/projeto.git`  
   - Você edita localmente, para estudo ou uso interno.  
   - Se quiser publicar suas alterações, o mais correto é fazer um **fork** público e enviar o código para o seu repositório.

3. **Contribuir de volta para o projeto original (Pull Request)**
   - Caminho padrão:
     1. Fazer um **fork**.  
     2. Clonar seu fork.  
     3. Criar um branch para a mudança.  
     4. Fazer commits.  
     5. Dar **push** para o seu fork.  
     6. No GitHub, clicar em **“Compare & pull request”** para enviar uma proposta de alteração ao repositório original.  
   - A equipe do projeto revisa e decide aceitar ou não.

4. **Abrir Issues**
   - Mesmo sem mexer no código, você pode:
     - Reportar bugs.  
     - Sugerir melhorias.  
     - Pedir esclarecimentos.  
   - Isso também é uma forma de “trabalhar” no projeto, em termos de colaboração.

### 2.2. Repositório público, mas sem licença clara

- Se o repositório é **público**, mas **não tem licença** especificada, a situação é diferente:
  - Você pode **ver o código**, clonar para estudo.  
  - Mas, em princípio, **não tem autorização legal clara** para redistribuir, modificar e publicar versões derivadas.  
  - Nesses casos, o mais prudente é:
    - Usar para estudo/testes locais.  
    - Evitar publicar variações suas em produção sem autorização do autor ou sem uma licença explícita.

### 2.3. Repositório privado de outra pessoa

- Se o repositório é **privado** e você **não é colaborador**:
  - Você não consegue nem ver o código, então não há como trabalhar nele.
- Se o repositório é **privado**, mas você foi adicionado como **colaborador ou membro da organização**:
  - Você pode clonar, criar branches, abrir pull requests, conforme as permissões definidas pela equipe (por exemplo, pode haver aprovação obrigatória).

---

## 3. Em termos práticos: “quero trabalhar nesse projeto, o que faço?”

Se você encontrou um projeto no GitHub que lhe interessa, o caminho geral é:

1. **Verificar:**
   - Ele é **público**?  
   - Há **licença** (MIT, Apache, GPL etc.)?  
   - Há um arquivo `CONTRIBUTING.md` (guia de contribuição)?  

2. **Escolher objetivo:**
   - Quer **usar o código como base** para o seu próprio projeto?  
     - Melhor caminho: **fork** → altera sob sua conta, respeitando a licença.  
   - Quer **contribuir com o projeto original**?  
     - Ler `README` e `CONTRIBUTING` → seguir o fluxo de **fork + pull request**.  
   - Quer só **estudar o código**?  
     - `git clone` é suficiente.

---

## 4. Resumo das opções principais

- **Editar diretamente (se o repositório é seu ou você tem permissão)**  
- **Fork**: criar sua cópia e desenvolver a partir dela.  
- **Clone**: baixar para sua máquina e trabalhar localmente.  
- **Pull Request**: propor mudanças ao projeto original.  
- **Issues**: colaborar com relatos de problema e sugestões.  

Se você quiser, na próxima pergunta me diz se o projeto é seu, de terceiros, público ou privado, que eu descrevo o passo a passo concreto (comandos e fluxo) para o seu caso específico.
