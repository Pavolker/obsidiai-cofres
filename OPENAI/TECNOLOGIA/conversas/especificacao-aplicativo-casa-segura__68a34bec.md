---
source: DATAGPT
conversation_id: 68a34bec-c58c-8331-a9c1-c58ac830fcd5
title: "Especificação aplicativo Casa Segura"
theme: TECNOLOGIA
created: 2025-08-18T15:54:14.681807Z
message_count: 2
attachments_count: 0
---

# Especificação aplicativo Casa Segura

- Tema: `TECNOLOGIA`
- Conversation ID: `68a34bec-c58c-8331-a9c1-c58ac830fcd5`

## Transcrição

### user

Quero criar um aplicativo chamado "Casa Segura". Esse aplicativo é composto pelas seguintes partes: 1- educação de segurança: um conjunto de informações uteis, práticas e aplicáveis  sobre segurança domestica. 2- diagnóstico de segurança: um conjunto de perguntas para a pessoa saber qual é o nível de segurança da sua casa; 3- acidentes de segurança: um notificador de acidentes de segurança doméstica, onde o usuário identifica um acidente, que é plotado em um mapa (tipo google maps), de modo que outros usuários do aplicativo possam saber da recorrência de acidentes em determinada região; 4- plano de segurança doméstica: a partir de perguntas e respostas, o aplicativo monta um "Plano de Segurança Doméstica" para o usuário, que poderá implanta-lo, passo a passo, tendo o aplicativo como gerenciador.  A partir dessa descrição, faça a explicitação desse aplicativo

### assistant

Paulo, segue uma especificação técnica inicial e completa do aplicativo “Casa Segura”, organizada para orientar produto, conteúdo, design e engenharia.

# 1) Visão, escopo e princípios
- **Propósito**: reduzir riscos e impactos de incidentes domésticos por meio de educação, diagnóstico, vigilância comunitária de acidentes e plano de ação personalizado.
- **Escopo MVP**: iOS/Android (React Native), backend com API REST, banco relacional, mapas com camadas de calor e pins, questionários de diagnóstico e gerador de plano passo a passo.
- **Princípios**: utilidade prática, conteúdo verificável, privacidade por padrão, baixo atrito de uso, acessibilidade, linguagem simples.

# 2) Perfis de usuário e casos de uso
- **Morador(a) padrão**: consulta conteúdos, responde diagnóstico e executa plano.
- **Cuidador(a)/responsável** (crianças, idosos, PCD): configura perfis de risco no domicílio, recebe alertas direcionados.
- **Colaborador(a) da comunidade**: notifica acidentes no mapa.
- **Administrador(a) de conteúdo**: publica/atualiza conteúdos e questionários (CMS).

Casos de uso essenciais:  
1) Aprender práticas de segurança; 2) Avaliar risco da residência; 3) Registrar acidentes com localização; 4) Gerar e gerenciar um Plano de Segurança Doméstica com tarefas, prazos e checklists.

# 3) Módulos funcionais

## 3.1 Educação de Segurança (Conteúdo prático)
- **Categorias**: elétrica; gás e combustíveis; incêndio; quedas; cortes e perfurações; intoxicações/medicamentos; água e afogamentos; animais/infestações; ergonomia; cibersegurança doméstica; preparação para emergências.
- **Formato**: fichas breves (o quê, por quê, como fazer), checklists, vídeos curtos, infográficos e FAQs.
- **Mecanismos**: busca, favoritos, trilhas recomendadas com base no diagnóstico, salvamento offline.
- **Metadados**: nível de risco associado, tempo de leitura, equipamentos necessários, custo estimado (campo opcional visível, sem preços no MVP), normas de referência.

## 3.2 Diagnóstico de Segurança (Questionários e score)
- **Estrutura**: 6 a 8 seções por ambiente (cozinha, área de serviço, quartos, sala, banheiro, garagem/externo) e por tema transversal (elétrica, gás, incêndio, armazenamento de químicos, acessibilidade).
- **Tipos de pergunta**: sim/não; múltipla escolha; escala de frequência; upload opcional de foto.
- **Exemplos**:
  - “Há disjuntor DR instalado e testado nos últimos 6 meses?” (Elétrica)
  - “Cilindro de gás está fora de ambientes fechados e com mangueira dentro da validade?” (Gás)
  - “Há tapetes antiderrapantes no box e barras de apoio conforme necessidade do morador?” (Quedas/Acessibilidade)
- **Pontuação**: pesos por risco e probabilidade. Score 0–100 por seção e um **Índice Casa Segura (ICS)** global ponderado.
  - Fórmula base: ICS = Σ (peso_seção × score_seção) / Σ pesos.
  - Classificação: Baixo, Moderado, Alto risco (faixas 0–39/40–69/70–100).
- **Saídas**: relatório com pontos críticos, ranking por ambiente, recomendações priorizadas (alto impacto/baixa complexidade primeiro).

## 3.3 Acidentes de Segurança (Mapa colaborativo)
- **Registro**: tipo do acidente (queda, choque elétrico, incêndio leve, intoxicação etc.), data/hora, local aproximado (geohash com arredondamento), breve descrição, opcional foto, indicativo de atendimento médico.
- **Privacidade**: anonimização; geolocalização aproximada por padrão; ocultação de dados pessoais; termos de uso claros.
- **Visualização**: pins por tipo; **heatmap** de recorrência; filtros por período (7/30/90 dias), tipo e severidade.
- **Qualidade de dados**: detecção de duplicatas por proximidade temporal/espacial; reputação do usuário; moderação com fila.
- **Uso prático**: ao tocar no cluster/pin, exibir checklist preventivo contextual e links para conteúdos da biblioteca.

## 3.4 Plano de Segurança Doméstica (PSd)
- **Geração**: a partir do diagnóstico, criar um plano com tarefas priorizadas, prazos sugeridos, responsáveis, recursos e evidências de conclusão (foto, observação).
- **Estrutura de tarefa**: título, descrição, motivo, passos, tempo estimado, dependências, materiais, risco mitigado, tag de ambiente/tema.
- **Gerenciamento**: checklists, lembretes, reavaliações periódicas, histórico de execução, exportação em PDF.
- **Adaptação**: se há crianças/idosos/PCD, inserir tarefas específicas (ex.: travas de armário, sinalização tátil, iluminação de circulação).

# 4) Fluxos de usuário (alto nível)
1) **Onboarding** → seleção de perfis no domicílio → consentimentos LGPD → tutorial breve.  
2) **Diagnóstico inicial** → ICS e relatório → geração do PSd.  
3) **Execução do plano** → lembretes e reavaliações.  
4) **Consulta de conteúdo** → trilhas recomendadas por risco.  
5) **Registro de acidente** → confirmação de geolocalização aproximada → moderação → mapa/heatmap.

# 5) Modelo de dados (esboço)

**users**(id, email, hash, perfil_doméstico, consentimentos, região, reputação)  
**households**(id, user_id, composição, tipo_imóvel, data_criação)  
**content_items**(id, categoria, título, resumo, corpo_md, nível_risco, tags, atualizado_em)  
**questionnaires**(id, título, versão, seção, ativo)  
**questions**(id, questionnaire_id, texto, tipo, peso, categoria_risco)  
**answers**(id, question_id, user_id, household_id, valor, evidência_url, respondido_em)  
**scores**(id, household_id, seção, score, ics_global, calculado_em)  
**plans**(id, household_id, versão, status, criado_em)  
**tasks**(id, plan_id, título, descrição, prioridade, prazo, responsável, status, evidência_url)  
**incidents**(id, user_id, geohash, tipo, severidade, descrição, mídia_url, data_ocorrência, moderado)  
**norms_refs**(id, código, descrição, link, tema)  
**content_x_norms**(content_id, norm_id)

# 6) Arquitetura e tecnologia (sugestão)
- **App**: React Native + Expo; armazenamento local para offline (MMKV/SQLite); push notifications.  
- **Backend**: Node.js/TypeScript (NestJS/Express); API REST; autenticação OIDC/e-mail magic link; rate limiting.  
- **Banco**: PostgreSQL + PostGIS (consultas espaciais, clusters); Redis para filas de moderação e notificações.  
- **Mapas**: Mapbox/Google Maps SDK; tiles com heatmap e clusterização.  
- **CMS**: Headless (Strapi/Directus) para conteúdos e questionários versionados.  
- **Analytics**: eventos de uso e conversão de tarefas com anonimização.  
- **Infra**: contêineres; observabilidade (logs, métricas e traços).  
- **Exportações**: geração de PDF no backend.

# 7) Privacidade, LGPD e moderação
- **Base legal**: consentimento para geodados e analytics; execução de contrato para funcionalidades essenciais; legítimo interesse para aprimoramento, com opt-out.  
- **Minimização**: coletar apenas o necessário; geolocalização arredondada por padrão; retenção por períodos definidos.  
- **Direitos do titular**: acesso, correção, portabilidade, exclusão.  
- **Segurança**: criptografia em trânsito/repouso; segregação de dados; controle de acesso por função.  
- **Moderação**: fila humana + heurísticas (texto/imagem); detecção de spam/duplicatas; botões de denúncia.

# 8) Conteúdo inicial (backlog editorial)
- **Guias base**: “Checklist da cozinha segura”, “Eletricidade residencial: cuidados básicos”, “Gás de cozinha: instalação e validade”, “Quedas no banheiro: prevenção essencial”, “Armazenamento seguro de produtos químicos”, “Plano de emergência domiciliar”.  
- **Trilhas**: “Casa com crianças”, “Casa com idosos”, “Animais de estimação”, “Primeiros socorros básicos”, “Preparação para quedas de energia”.  
- **Referências normativas**: campos no CMS para citar normas técnicas e fontes públicas reconhecidas.

# 9) Lógica de pontuação e priorização (detalhe)
- **Peso de risco (WR)** por pergunta: {alto=3, médio=2, baixo=1}.  
- **Score da pergunta (SP)**: sim=1, não=0, parcial=0,5.  
- **Score da seção** = Σ(SP×WR) / Σ(WR).  
- **Prioridade de tarefa** = f(risco_mitigado, esforço_estimado, dependências). Heurística inicial:  
  - P1: risco alto e baixo esforço;  
  - P2: risco alto e médio/alto esforço;  
  - P3: risco médio;  
  - P4: risco baixo.

# 10) Mapas e análises espaciais
- **Visualização**: clusterização de marcadores por zoom; heatmap temporal.  
- **Sinais**: taxa de incidentes por 1.000 residências (quando disponível), sazonalidade (ex.: maior incidência em fins de semana), tipos frequentes por região.  
- **Algoritmo sugerido**: DBSCAN/HDBSCAN para detectar áreas de densidade de incidentes em janelas deslizantes (7/30 dias).

# 11) Acessibilidade e usabilidade
- Texto claro, leitura em voz, alto contraste, tamanhos ajustáveis, navegação por teclado/leitor de tela, descrições de imagens.  
- Fluxos curtos, salvamento automático, opção offline do conteúdo e do plano.

# 12) Notificações e rotinas
- Lembretes de tarefas do plano; revalidação do diagnóstico a cada 90 dias; alertas contextuais quando o app detectar aumento regional de determinado tipo de incidente (opt-in).

# 13) Indicadores de sucesso (KPIs)
- Conclusão do diagnóstico (%).  
- Melhora do ICS entre ciclos (%).  
- Tarefas concluídas por plano.  
- Incidentes registrados/mês e taxa de moderação aprovada.  
- Engajamento em conteúdos recomendados pós-diagnóstico.

# 14) Roadmap sugerido

**Fase 1 — MVP (8–10 semanas)**  
- Educação de Segurança (conteúdo inicial + CMS).  
- Diagnóstico v1 (seções essenciais, ICS).  
- Plano de Segurança v1 (tarefas P1/P2, lembretes).  
- Mapa de acidentes v1 (registro básico, pins, moderação simples).  

**Fase 2 — Iteração (8–12 semanas)**  
- Heatmap temporal e clusters.  
- Perfis por domicílio (crianças/idosos/PCD).  
- Exportação PDF, histórico e reavaliação programada.  
- Acessibilidade avançada e offline completo.

**Fase 3 — Maturidade**  
- Recomendação personalizada de conteúdo por ICS e perfil.  
- Integração com sensores domésticos (opcional, via parceiros).  
- Benchmark e relatórios agregados regionais anonimizados.

# 15) Requisitos não funcionais
- **Desempenho**: 95º percentil < 300 ms nas APIs críticas.  
- **Disponibilidade**: ≥ 99,5% mensal.  
- **Compatibilidade**: Android 9+, iOS 15+.  
- **Observabilidade**: métricas, logs estruturados, tracing distribuído.  
- **Testes**: unitários, integração, end-to-end de fluxos principais; revisão de segurança antes de lançamentos.

# 16) Estruturas de dados de exemplo (JSON)

**Resposta de diagnóstico (trecho)**
```json
{
  "household_id": "H123",
  "responses": [
    {"q": "DR_instalado", "value": "sim"},
    {"q": "gas_mangueira_validade_ok", "value": "nao"},
    {"q": "barra_apoio_banheiro", "value": "parcial"}
  ]
}
```

**Tarefa do Plano**
```json
{
  "task_id": "T789",
  "title": "Instalar DR no quadro elétrico",
  "priority": "P1",
  "due_date": "2025-09-15",
  "dependencies": [],
  "risk_mitigated": "choque_eletrico"
}
```

**Incidente**
```json
{
  "incident_id": "I456",
  "type": "queda",
  "severity": "moderada",
  "geohash": "6gkzq",
  "occurred_at": "2025-08-10T17:30:00Z"
}
```

# 17) Políticas e termos essenciais (resumo)
- Termos de uso com regras para relatos, proibição de dados sensíveis de terceiros e de imagens identificáveis sem consentimento.  
- Política de privacidade com tratamento de dados, finalidades, base legal, prazos de retenção, contatos do controlador e DPO.  
- Botão de exclusão de conta e dados.

---

Se quiser, transformo esta especificação em: 1) backlog no formato de user stories; 2) questionário completo versão 1 com pesos e ICS; 3) esquema de banco de dados SQL inicial; 4) protótipo de telas com fluxo end-to-end.
