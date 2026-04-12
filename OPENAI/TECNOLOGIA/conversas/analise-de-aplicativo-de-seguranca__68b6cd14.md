---
source: DATAGPT
conversation_id: 68b6cd14-f68c-8321-9e15-836c958f9acc
title: "Análise de aplicativo de segurança"
theme: TECNOLOGIA
created: 2025-09-02T10:55:17.898019Z
message_count: 12
attachments_count: 0
---

# Análise de aplicativo de segurança

- Tema: `TECNOLOGIA`
- Conversation ID: `68b6cd14-f68c-8321-9e15-836c958f9acc`

## Transcrição

### user

Quero criar  um aplicativo  para ajudar as pessoas em assuntos relacionados com a segurança doméstica . O aplicativa vai ter as seguintes funcionalidades: 1- registrar ocorrências de roubo, furtos, invasão da residência, além de acidentes como vazamento de gaz, descarga elétrica, entre outros. Esse registro deverá ser georeferenciado, para que os usuários observem em um mapa as plotagens de acidentes mais comuns por região; 2- diagnóstico de risco de acidente da casa. O usuário responde algumas perguntas e o aplicativo apresenta um "painel diagnóstico" que aponta o nível de risco e os pontos de melhoramento urgente, para diminuir esses rsicos; 3- um sistema de consultas sobre vários temas relativos à segurança da casa (os temas do diagnóstico), que poderão ser consultados e aprofundados. Nessa parte o usuário vai tomar contato com uma abordagem de "Filosofia da Segurança", que esclarece a questão da segurança como uma cultura intrínseca da habitação.  Analise essa proposição

### assistant

Paulo, a ideia é ótima e coerente com o “Casa Segura”. Dá para transformar em um produto útil, com impacto social real. Segue uma análise direta, com sugestões práticas para um MVP sólido e escalável.

# 1) Proposta de valor e público-alvo
- **Valor central:** reduzir riscos e danos em casa por meio de (a) inteligência coletiva georreferenciada, (b) diagnóstico personalizado e (c) educação aplicada (“filosofia da segurança” como cultura doméstica).
- **Quem se beneficia:** famílias, síndicos/condomínios, prefeituras/Defesa Civil, seguradoras, escolas técnicas, idosos/cuidadores.

# 2) Módulos do app (visão funcional)
1) **Mapa de Ocorrências**
   - Registro de roubos/furtos/invasões e acidentes (gás, choque, incêndio, quedas etc.).
   - Georreferenciamento com **privacidade por agregação** (hexágonos/quadricículas, p.ex. H3 7–8) e *blur* de endereço.
   - Heatmap, filtros por tipo/data, alertas configuráveis por raio/tema.
   - Mecanismos de **qualidade de dado**: foto opcional, descrição estruturada, verificação por reputação do usuário, detecção de duplicatas, “sinais de confiança” (consistência, proximidade temporal, confirmação comunitária).

2) **Diagnóstico de Risco da Casa**
   - Questionário guiado por cômodo e por tema (elétrica, gás, incêndio, quedas, água/mofo, química/venenos, digital/IoT, estrutural).
   - **Score composto** (0–100) por categoria + nível geral (Baixo/Médio/Alto).
   - **Painel diagnóstico**: semáforos, “3 urgências” e plano de melhorias em passos (custo/complexidade estimados, impacto).
   - Reavaliações periódicas para medir evolução (antes/depois) e gerar “índice de maturidade” do lar.

3) **Base de Conhecimento + Filosofia da Segurança**
   - Conteúdo curto, acionável e indexado pelos mesmos temas do diagnóstico.
   - “Filosofia da segurança” = **princípios** (prevenção, redundância, responsabilidade compartilhada, cultura do cuidado) aplicados à rotina.
   - Modo “aprender + fazer”: cada artigo termina com 1–3 ações práticas verificáveis (checklist).

# 3) Requisitos de confiança, ética e LGPD
- **LGPD by design:** consentimento, finalidade clara, portabilidade, exclusão; apenas dados mínimos; **anonimização/seudonimização** de localização (agregado por célula/quadra, nunca endereço exato).
- **Risco de uso indevido:** ocultar localização exata de ocorrências sensíveis; atrasar publicação (time-lag) em crimes em andamento; *rate limiting* para scraping.
- **Moderação e fraude:** fila automática (classificador de anomalia + validação comunitária + curadoria); política contra calúnia/identificação de terceiros.
- **Avisos críticos:** o app **não é canal de emergência**; botão rápido “Ligar 190/193/199” destacado.

# 4) Arquitetura técnica (sugestão)
- **App:** Flutter ou React Native; mapas (Mapbox/Google); notificações nativas.
- **Back-end:** Node/TypeScript (NestJS) ou Python (FastAPI); banco Postgres + **PostGIS**; fila (RQ/Sidekiq/BullMQ); cache (Redis).
- **Geo:** index H3/Quadkey; *tiling server* para heatmaps; consultas por bounding box/hex.
- **Conteúdo:** CMS headless (Strapi/Directus) com versionamento e *feature flags*.
- **Observabilidade:** logs estruturados, auditoria de eventos, métricas de segurança.

# 5) Modelo de dados (essencial)
- **Incident**: id, user_id (hash), category {furto, invasão, gás, elétrica, incêndio, queda, outro}, timestamp, **geo_cell_id**, evidence_url?, trust_score, status {pending, published, flagged}.
- **ResidenceProfile** (opcional para usuários logados): tipo de moradia, ano, nº moradores, pets, idosos/crianças, devices IoT (sim/não).
- **Assessment**: id, user_id, residence_id?, answers{…}, scores{elétrica, gás, incêndio, quedas…}, overall_score, recommendations[ids].
- **Content**: id, topic, subtype {guia, checklist, vídeo}, difficulty, actions[ ].
- **Reputation**: user_id, points, badges, strikes.

# 6) Metodologia do diagnóstico (base técnica)
- **Estrutura do questionário** (por cômodo e por tema). Exemplos:
  - Elétrica: DR/IDR presente? Extensão improvisada? Aterramento? Quadro com disjuntores identificados?
  - Gás: teste de espuma realizado? Mangueira dentro do prazo? Ventilação adequada?
  - Incêndio: detectores de fumaça? Extintor válido? Rotas desobstruídas?
  - Quedas: barras de apoio? Tapetes fixados? Iluminação noturna?
  - Digital/IoT: Wi-Fi com WPA2+/senha forte? Atualizações automáticas? Câmeras com 2FA?
- **Scoring**: peso por severidade/likelihood; perguntas *knock-out* (falhas críticas = risco alto imediato).  
  Fórmula simples (MVP): `score_tema = 100 - Σ(peso_pergunta × não_conformidade)`.  
  **Nível geral** via média ponderada + rebaixamento por qualquer *knock-out*.

# 7) UX e acessibilidade
- **Onboarding** por histórias de risco + checklists “5 minutos”.
- **Mapa** com filtros simples (tipo, período, raio) + legenda clara.
- **Painel**: cartões por tema (semáforo), call-to-action “Corrigir agora”.
- **Acessibilidade:** tamanho de fonte, alto contraste, voz-over, vídeos curtos.
- **Offline-first** para registrar ocorrência sem rede (sincroniza depois).

# 8) Incentivos e engajamento
- **Reputação e selos** (“Casa com Diagnóstico Atualizado”, “Semáforo Verde Elétrica”).
- **Metas mensais** (ex.: “3 melhorias de baixo custo”).
- **Parcerias**: Corpo de Bombeiros/Defesa Civil, seguradoras (descontos com checklist cumprido), lojas de materiais (cupom responsável), escolas técnicas.

# 9) Indicadores de sucesso (KPI)
- % casas reavaliadas em 90 dias; variação média do score; tempo médio de correção das “3 urgências”; taxa de incidentes por 1.000 domicílios por região; precisão do modelo de confiança; uso do conteúdo por tema; NPS.

# 10) Riscos e mitigação
- **Dados sensíveis/segurança pessoal:** agregar e atrasar localização, proibir fotos que identifiquem rotinas/placas; *privacy budget* por área.
- **Ruído nas ocorrências:** reputação + heurísticas anti-spam + “confirmar/contestar”.
- **Responsabilidade legal:** textos de isenção, fontes técnicas nas recomendações, alinhamento com normas (ABNT/NBR, Instruções Bombeiros) — sem substituir profissional habilitado.

# 11) Roadmap de entrega (macro)
- **MVP**: registro de incidentes (com agregação geográfica), diagnóstico básico com painel + base de conhecimento enxuta por tema, notificações e perfis.  
- **V1**: reputação, moderação semiautomática, conteúdo “filosofia” expandido, parcerias piloto.  
- **V2**: recomendações personalizadas com *ranking* custo/impacto, campanhas locais, integrações (Defesa Civil/seguradoras), experimentos de predição.

# 12) Próximos passos práticos
- Definir **taxonomia de incidentes** e **perguntas do diagnóstico** (versão 1).  
- Escolher **agregação geográfica** (p.ex. H3 nível 8) e políticas de privacidade.  
- Especificar **painel** (cards, semáforos, “3 urgências”, checklist) e os **critérios de peso**.  
- Montar **guia editorial** da “Filosofia da Segurança” com 6–8 princípios e *playbooks* por tema.  
- Criar **política de moderação** e **termos de uso/LGPD**.

Se quiser, já redijo: (a) a primeira versão do questionário por tema/cômodo; (b) o esquema do banco (DDL Postgres/PostGIS) e (c) os rascunhos de telas do MVP.

### user

Analise a tabela temática anexada

### assistant

Paulo, analisei a tabela da planilha **Casa Segura – Análise Completa**. A estrutura está muito bem organizada e cobre aspectos essenciais da segurança doméstica. Aqui vai uma leitura crítica:

---

## Estrutura observada
Cada tema apresenta:
- **Nome** → área temática (Ex.: Ergonomia e Mobiliário, Prevenção de Incêndios).
- **Definição Geral** → contextualização e relevância do risco.
- **Nível de Risco** → classificação qualitativa (baixo, médio, alto) com explicação.
- **Itens de Atenção** → fatores críticos que precisam de observação.
- **Acidentes Mais Comuns** → exemplos de ocorrências típicas.
- **Política de Cuidado com Idosos** → medidas específicas de proteção.
- **Política de Cuidado com Crianças** → medidas específicas de proteção.
- **Uma Boa Ideia** → práticas preventivas ou rotinas de inspeção.
- **Mensagem Final** → síntese motivacional de alerta.

---

## Pontos Fortes
1. **Abrangência**: cobre riscos múltiplos (ergonomia, fogo, quedas, químicos, elétrica etc.).
2. **Didática**: cada tema é autossuficiente e segue um padrão de apresentação.
3. **Foco em públicos vulneráveis**: idosos e crianças bem contemplados.
4. **Cultura preventiva**: “Uma Boa Ideia” e “Mensagem Final” ajudam a internalizar hábitos.

---

## O que pode ser melhorado
1. **Uniformidade nos campos**: em alguns temas (ex.: Incêndios), o campo “Acidentes Mais Comuns” está vazio. Isso quebra o padrão.
2. **Escala de risco**: hoje é textual (“Alto Risco”). Poderia ser transformada em **escala visual/numérica (0–100 ou 1–5)** para facilitar uso no aplicativo.
3. **Conexão com diagnóstico**: os **Itens de Atenção** já podem servir de base para perguntas no módulo de “Painel Diagnóstico” do app. Isso precisa ser mapeado de forma estruturada.
4. **Padronização terminológica**: alguns títulos usam numeração (“3.1 Escadas”), outros não. Uma padronização ajudaria para exportar ao sistema.
5. **Ausência de indicadores de impacto**: por exemplo, estatísticas nacionais ou internacionais para dar mais força (ex.: % de acidentes domésticos relacionados a quedas).
6. **Integração com a “Filosofia da Segurança”**: seria interessante que cada tema terminasse com um “Princípio Filosófico da Segurança” (ex.: prevenção, redundância, cuidado coletivo), alinhado à cultura do projeto.

---

## Sugestão de próximos passos
- **Criar um dicionário de riscos estruturados** → cada “Item de Atenção” deve virar uma questão objetiva para o diagnóstico do app.
- **Adicionar escala de risco numérica + visual** (ex.: semáforo ou pontuação).
- **Completar lacunas** (como “Acidentes Mais Comuns” em Incêndios).
- **Relacionar cada tema com a filosofia** → um princípio guia no final de cada capítulo.
- **Pensar em indicadores mensuráveis** (estatísticas, nº de ocorrências, etc.) para reforçar impacto.

---

👉 Pergunto: você gostaria que eu já faça **um quadro estruturado** transformando os **Itens de Atenção** em **perguntas diretas para o diagnóstico do aplicativo**? Isso faria a ponte entre o conteúdo conceitual da planilha e a parte prática do app.

### user

Melhore inicialmente a tabela, de forma que ela  esteja completa

### assistant

Paulo, a tabela está praticamente completa — só há **um campo vazio**:  

- **Tema:** *Prevenção de Incêndios*  
- **Coluna faltante:** *Acidentes Mais Comuns*  

---

## Sugestão de preenchimento (baseado em dados de organismos como NFPA e Corpo de Bombeiros):

**Acidentes Mais Comuns – Prevenção de Incêndios**
- Incêndios iniciados por curto-circuito em instalações elétricas antigas ou mal conservadas.  
- Fogões e panelas esquecidas no fogo, especialmente à noite ou em cozinhas sem supervisão.  
- Velas acesas sem suporte adequado ou próximas a cortinas e papéis.  
- Cigarros descartados incorretamente em sofás, camas ou lixeiras.  
- Superaquecimento de equipamentos elétricos (ferros de passar, aquecedores, carregadores).  

---

Assim, a tabela ficaria **completa e uniforme** em todos os temas.  

Quer que eu já **reescreva a tabela inteira, com esse complemento incluído**, para você ter a versão final revisada em formato pronto para exportação (Excel ou CSV)?

### user

sim reescreva e faça a exportação em excel

### assistant

A tabela foi revisada e está agora **completa e padronizada**.  
Você pode baixar a versão finalizada aqui:  

📂 [Casa_Segura_Analise_Completa_Revisada.xlsx](sandbox:/mnt/data/Casa_Segura_Analise_Completa_Revisada.xlsx)  

Quer que eu também prepare uma **visualização resumida** (em quadro ou infográfico) para facilitar a leitura dentro do app?

### user

Faça agora o PRD do aplicativo, deixando claro:  1- uso gratuito e aberto ao público da funcionalidade de georeferenciamento; 2- uso para assinantes das funcionalidades de diagnóstico e  da "Biblioteca da Segurança" ; 3- Descrição das  3 funcionalidades básicas: georeferenciamento, diagnóstico e biblioteca

### assistant

Perfeito, Paulo. Vou estruturar o **PRD – Product Requirements Document** do aplicativo *Casa Segura*, alinhado ao modelo profissional de especificação de produto digital, destacando os pontos que você pediu.  

---

# 📄 PRD – Casa Segura  

## 1. Visão Geral  
O **Casa Segura** é um aplicativo voltado à **prevenção e redução de riscos domésticos**, promovendo a cultura da segurança no lar. Ele integra inteligência coletiva (georreferenciamento de ocorrências), diagnóstico personalizado de riscos e uma biblioteca de conhecimento aplicada (“Filosofia da Segurança”).  

---

## 2. Público-Alvo  
- Famílias que buscam aumentar a segurança de suas residências.  
- Síndicos e administradores de condomínios.  
- Idosos, cuidadores e pais com crianças pequenas.  
- Profissionais de prevenção (Corpo de Bombeiros, Defesa Civil).  
- Seguradoras e empresas de manutenção residencial.  

---

## 3. Modelo de Uso e Acesso  
- **Uso Gratuito (aberto ao público):**  
  - Acesso total ao **Mapa Georreferenciado de Ocorrências**, permitindo visualizar e registrar acidentes e crimes domésticos.  
  - Sem necessidade de assinatura ou login obrigatório (opcional para cadastro e histórico pessoal).  

- **Uso Pago (para assinantes):**  
  - Acesso completo ao **Diagnóstico de Risco Doméstico** com geração de painel personalizado e recomendações práticas.  
  - Acesso exclusivo à **Biblioteca da Segurança**, com conteúdos aprofundados sobre prevenção, boas práticas e a “Filosofia da Segurança”.  
  - Recursos adicionais de monitoramento de progresso (comparar diagnósticos ao longo do tempo, salvar relatórios).  

---

## 4. Funcionalidades Principais  

### 4.1 Georreferenciamento de Ocorrências (Gratuito)  
- **Descrição:** Registro e visualização em mapa de ocorrências de roubos, furtos, invasões, acidentes domésticos (vazamento de gás, choque elétrico, quedas, incêndios etc.).  
- **Características:**  
  - Sistema de plotagem anônima e agregada (respeitando LGPD).  
  - Visualização em mapa com filtros por tipo de ocorrência, período e localização.  
  - Alertas configuráveis por raio (ex.: “acidentes de gás em 2km”).  
- **Valor para o usuário:** Informação comunitária para identificar áreas de maior risco e adotar medidas preventivas.  

---

### 4.2 Diagnóstico de Risco Doméstico (Assinante)  
- **Descrição:** Avaliação personalizada do nível de risco da casa, com base em um questionário estruturado (elétrica, gás, incêndio, quedas, químicos, ergonomia etc.).  
- **Características:**  
  - Painel diagnóstico com níveis de risco (baixo, médio, alto).  
  - Destaque de “3 melhorias urgentes” para rápida correção.  
  - Relatórios comparativos em reavaliações periódicas.  
  - Recomendação de ações práticas por custo/impacto.  
- **Valor para o usuário:** Orientação clara e objetiva para reduzir riscos domésticos e aumentar a segurança familiar.  

---

### 4.3 Biblioteca da Segurança (Assinante)  
- **Descrição:** Repositório de conteúdos temáticos sobre segurança doméstica, organizado pelos mesmos eixos do diagnóstico.  
- **Características:**  
  - Guias rápidos, checklists e tutoriais visuais.  
  - Princípios da “Filosofia da Segurança” aplicados ao dia a dia.  
  - Atualizações contínuas com base em normas nacionais e internacionais (ABNT, NFPA, WHO, CDC).  
  - Sugestões de práticas mensais (ex.: inspeção elétrica, treino de evacuação familiar).  
- **Valor para o usuário:** Transformar o conhecimento técnico em cultura de segurança no lar.  

---

## 5. Requisitos Não Funcionais  
- **Privacidade e LGPD by design** (anonimização de dados e localização).  
- **Alta usabilidade e acessibilidade** (fontes legíveis, contraste, suporte a leitores de tela).  
- **Escalabilidade** para receber registros comunitários em tempo real.  
- **Compatibilidade cross-platform** (Android, iOS, versão web progressiva).  

---

## 6. Indicadores de Sucesso (KPI)  
- Nº de ocorrências registradas e confirmadas por mês.  
- Nº de diagnósticos realizados e reavaliados.  
- Taxa de conversão para assinantes.  
- Evolução do “nível de risco médio” das casas cadastradas.  
- Engajamento com a Biblioteca (artigos lidos, checklists completados).  

---

Paulo, este PRD já estrutura o produto para:  
- **atração em massa** (uso gratuito do mapa);  
- **retenção e monetização** (diagnóstico + biblioteca para assinantes).  

Quer que eu prepare também um **roadmap de desenvolvimento em fases (MVP → V1 → V2)**, mostrando como implementar cada funcionalidade em etapas?

### user

Faça agora o SCHEMA PRISMA do app

### assistant

Perfeito! Abaixo está um **schema Prisma** completo (PostgreSQL) para o app *Casa Segura*, cobrindo: usuários/assinaturas, georreferenciamento de ocorrências (com privacidade por célula), diagnóstico (avaliação, respostas e recomendações), e Biblioteca da Segurança (conteúdos, tópicos, tags), além de reputação, alertas e moderação.

> **Notas de design**
> - **Geo**: usamos `geoCellId` (ex.: H3 nível 7–9) para agregação + `latitude/longitude` opcionais (se coletados).  
> - **LGPD**: relacionamentos minimizados; PII opcional; `deletedAt` para *soft delete*.  
> - **Diagnóstico**: perguntas/alternativas versionadas; respostas normalizadas + payload JSON para flexibilidade.  
> - **Biblioteca**: conteúdo versionável, com tópicos e tags.  
> - **Escalabilidade**: índices essenciais nos campos de filtro (categoria, período, célula geográfica, status).  

---

```prisma
// schema.prisma — Casa Segura

generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

/// ===== Enums =====
enum Role {
  USER
  ADMIN
  MODERATOR
}

enum SubscriptionStatus {
  NONE
  ACTIVE
  PAST_DUE
  CANCELED
}

enum IncidentCategory {
  ROUBO
  FURTO
  INVASAO
  GAS
  ELETRICA
  INCENDIO
  QUEDA
  QUIMICOS
  OUTRO
}

enum IncidentStatus {
  PENDING
  PUBLISHED
  FLAGGED
  REMOVED
}

enum ModerationReason {
  SPAM
  DUPLICATE
  OFFENSIVE
  PRIVACY_RISK
  MISLEADING
  OTHER
}

enum RiskLevel {
  LOW
  MEDIUM
  HIGH
  CRITICAL
}

enum ContentType {
  GUIA
  CHECKLIST
  ARTIGO
  VIDEO
  PODCAST
}

enum Difficulty {
  BASIC
  INTERMEDIATE
  ADVANCED
}

enum QuestionType {
  BOOLEAN
  SINGLE_CHOICE
  MULTI_CHOICE
  SCALE
  NUMBER
  TEXT
}

enum AlertType {
  INCIDENT_NEARBY
  THEME_UPDATE
  DIAG_REMINDER
}

enum ReputationEvent {
  INCIDENT_PUBLISHED
  INCIDENT_CONFIRMED
  ASSESSMENT_COMPLETED
  CONTENT_CONTRIBUTION
  REPORT_VALID
  REPORT_REJECTED
}

/// ===== Core: Users & Auth =====
model User {
  id              String              @id @default(cuid())
  email           String?             @unique
  phone           String?
  passwordHash    String?
  role            Role                @default(USER)
  createdAt       DateTime            @default(now())
  updatedAt       DateTime            @updatedAt
  deletedAt       DateTime?

  // profile (minimiza PII)
  displayName     String?
  city            String?
  state           String?
  country         String?
  locale          String?             // ex: "pt-BR"

  subscriptions   Subscription[]
  residences      ResidenceProfile[]
  incidents       Incident[]          @relation("UserIncidents")
  assessments     Assessment[]
  reputation      ReputationAccount?
  alerts          AlertSubscription[]
  moderationFlags ModerationEvent[]   @relation("ModeratorEvents")

  @@index([role])
  @@index([createdAt])
}

model Subscription {
  id            String             @id @default(cuid())
  userId        String
  user          User               @relation(fields: [userId], references: [id], onDelete: Cascade)
  status        SubscriptionStatus @default(ACTIVE)
  provider      String?            // ex: stripe
  providerRef   String?            @unique
  startedAt     DateTime           @default(now())
  currentPeriodEnd DateTime?
  canceledAt    DateTime?
  createdAt     DateTime           @default(now())
  updatedAt     DateTime           @updatedAt

  @@index([userId, status])
}

/// ===== Geo & Incidents (Mapa Gratuito) =====
model Incident {
  id            String           @id @default(cuid())
  userId        String?
  user          User?            @relation("UserIncidents", fields: [userId], references: [id], onDelete: SetNull)

  category      IncidentCategory
  status        IncidentStatus    @default(PENDING)
  title         String?
  description   String?
  mediaUrl      String?           // foto/vídeo opcional

  // geolocalização
  geoCellId     String            // ex: H3 "87283472bffffff"
  latitude      Decimal?          @db.Decimal(9,6)  // opcional, se coletado
  longitude     Decimal?          @db.Decimal(9,6)  // opcional, se coletado

  trustScore    Int               @default(0)
  source        String?           // "user", "partner", etc.

  occurredAt    DateTime          @default(now())
  publishedAt   DateTime?
  createdAt     DateTime          @default(now())
  updatedAt     DateTime          @updatedAt
  deletedAt     DateTime?

  confirmations IncidentConfirmation[]
  flags         IncidentFlag[]

  @@index([category, occurredAt])
  @@index([geoCellId, occurredAt])
  @@index([status, occurredAt])
  @@index([trustScore])
}

model IncidentConfirmation {
  id          String    @id @default(cuid())
  incidentId  String
  incident    Incident  @relation(fields: [incidentId], references: [id], onDelete: Cascade)
  userHash    String    // hash anônimo p/ confirmar sem identificar
  createdAt   DateTime  @default(now())

  @@unique([incidentId, userHash])
  @@index([incidentId])
}

model IncidentFlag {
  id          String            @id @default(cuid())
  incidentId  String
  incident    Incident          @relation(fields: [incidentId], references: [id], onDelete: Cascade)
  reason      ModerationReason
  details     String?
  reporterId  String?
  reporter    User?             @relation(fields: [reporterId], references: [id], onDelete: SetNull)
  createdAt   DateTime          @default(now())

  @@index([incidentId, reason])
}

/// ===== Diagnóstico (Assinante) =====
model ResidenceProfile {
  id             String    @id @default(cuid())
  userId         String
  user           User      @relation(fields: [userId], references: [id], onDelete: Cascade)
  type           String?   // casa/apto/condomínio
  buildYear      Int?
  occupants      Int?
  pets           Boolean?
  elderly        Boolean?
  children       Boolean?
  iotDevices     Boolean?
  createdAt      DateTime  @default(now())
  updatedAt      DateTime  @updatedAt
  deletedAt      DateTime?

  assessments    Assessment[]

  @@index([userId])
}

model Assessment {
  id               String      @id @default(cuid())
  userId           String
  user             User        @relation(fields: [userId], references: [id], onDelete: Cascade)
  residenceId      String?
  residence        ResidenceProfile? @relation(fields: [residenceId], references: [id], onDelete: SetNull)

  version          Int         @default(1)  // versão do questionário
  overallScore     Int?                    // 0–100
  riskLevel        RiskLevel?              // LOW/MEDIUM/HIGH/CRITICAL
  knockouts        Json?                   // perguntas críticas acionadas
  summary          String?

  createdAt        DateTime    @default(now())
  updatedAt        DateTime    @updatedAt

  answers          AssessmentAnswer[]
  recommendations  Recommendation[]

  @@index([userId, createdAt])
  @@index([residenceId])
}

model Question {
  id            String        @id @default(cuid())
  version       Int           @default(1)
  code          String        @unique  // ex: "ELE-DR-001"
  theme         String        // "ELETRICA", "GAS", "INCENDIO", "QUEDAS", etc.
  title         String
  description   String?
  type          QuestionType
  required      Boolean       @default(true)
  weight        Int           @default(10)  // impacto no score
  isKnockout    Boolean       @default(false)
  options       QuestionOption[]

  createdAt     DateTime      @default(now())
  updatedAt     DateTime      @updatedAt

  @@index([theme, version])
}

model QuestionOption {
  id          String    @id @default(cuid())
  questionId  String
  question    Question  @relation(fields: [questionId], references: [id], onDelete: Cascade)
  label       String
  value       String    // ex: "YES", "NO", "N/A", ou texto da alternativa
  scoreDelta  Int       @default(0) // ajuste no score
  order       Int       @default(0)
}

model AssessmentAnswer {
  id            String     @id @default(cuid())
  assessmentId  String
  assessment    Assessment @relation(fields: [assessmentId], references: [id], onDelete: Cascade)
  questionId    String
  question      Question   @relation(fields: [questionId], references: [id], onDelete: Restrict)
  value         String?    // armazenar valor bruto
  values        Json?      // p/ MULTI_CHOICE, payloads
  scoreImpact   Int        @default(0)
  createdAt     DateTime   @default(now())

  @@unique([assessmentId, questionId])
  @@index([questionId])
}

model Recommendation {
  id            String     @id @default(cuid())
  assessmentId  String
  assessment    Assessment @relation(fields: [assessmentId], references: [id], onDelete: Cascade)
  theme         String     // ex: "ELETRICA"
  title         String
  description   String?
  priority      Int        @default(0) // ranking interno
  costLevel     Int?       // 1–5 (estimativa)
  impactLevel   Int?       // 1–5
  isUrgent      Boolean    @default(false)
  createdAt     DateTime   @default(now())

  @@index([assessmentId, isUrgent, priority])
}

/// ===== Biblioteca da Segurança (Assinante) =====
model Topic {
  id          String     @id @default(cuid())
  slug        String     @unique
  title       String
  description String?
  parentId    String?
  parent      Topic?     @relation("TopicToTopic", fields: [parentId], references: [id], onDelete: SetNull)
  children    Topic[]    @relation("TopicToTopic")

  createdAt   DateTime   @default(now())
  updatedAt   DateTime   @updatedAt

  contents    Content[]
}

model Tag {
  id        String    @id @default(cuid())
  slug      String    @unique
  name      String
  createdAt DateTime  @default(now())
  contents  ContentTag[]
}

model Content {
  id            String        @id @default(cuid())
  version       Int           @default(1)
  type          ContentType
  difficulty    Difficulty    @default(BASIC)
  title         String
  slug          String        @unique
  summary       String?
  body          Json          // armazenar rich text/MD estruturado
  principle     String?       // “Filosofia da Segurança” associada

  topicId       String?
  topic         Topic?        @relation(fields: [topicId], references: [id], onDelete: SetNull)

  createdAt     DateTime      @default(now())
  updatedAt     DateTime      @updatedAt
  publishedAt   DateTime?

  actions       ContentAction[]
  tags          ContentTag[]

  @@index([topicId, publishedAt])
  @@index([type, difficulty])
}

model ContentAction {
  id         String   @id @default(cuid())
  contentId  String
  content    Content  @relation(fields: [contentId], references: [id], onDelete: Cascade)
  label      String   // “Verificar DR”, “Teste espuma gás”, etc.
  order      Int      @default(0)
  payload    Json?    // metadados executáveis/checklist
}

model ContentTag {
  contentId String
  tagId     String
  content   Content @relation(fields: [contentId], references: [id], onDelete: Cascade)
  tag       Tag     @relation(fields: [tagId], references: [id], onDelete: Cascade)

  @@id([contentId, tagId])
}

/// ===== Reputação, Moderação, Alertas =====
model ReputationAccount {
  userId     String  @id
  user       User    @relation(fields: [userId], references: [id], onDelete: Cascade)
  points     Int     @default(0)
  badges     String[] @db.Text[] // lista simples de “selos”
  updatedAt  DateTime @updatedAt
  events     ReputationEventLog[]
}

model ReputationEventLog {
  id        String           @id @default(cuid())
  userId    String
  user      User             @relation(fields: [userId], references: [id], onDelete: Cascade)
  event     ReputationEvent
  points    Int              @default(0)
  meta      Json?
  createdAt DateTime         @default(now())

  @@index([userId, createdAt])
}

model ModerationEvent {
  id          String            @id @default(cuid())
  moderatorId String?
  moderator   User?             @relation("ModeratorEvents", fields: [moderatorId], references: [id], onDelete: SetNull)
  incidentId  String?
  incident    Incident?         @relation(fields: [incidentId], references: [id], onDelete: Cascade)
  reason      ModerationReason
  details     String?
  createdAt   DateTime          @default(now())

  @@index([incidentId, createdAt])
}

model AlertSubscription {
  id         String    @id @default(cuid())
  userId     String
  user       User      @relation(fields: [userId], references: [id], onDelete: Cascade)
  type       AlertType
  radiusKm   Int?      // para geofence (ex.: 2 km)
  topics     String[]  @db.Text[] // temas do interesse: ["GAS","ELETRICA",...]
  createdAt  DateTime  @default(now())
  updatedAt  DateTime  @updatedAt

  @@index([userId, type])
}

/// ===== Auditoria Básica =====
model AuditLog {
  id        String   @id @default(cuid())
  actorId   String?
  actor     User?    @relation(fields: [actorId], references: [id], onDelete: SetNull)
  action    String
  entity    String   // "Incident", "Assessment", etc.
  entityId  String?
  ip        String?
  meta      Json?
  createdAt DateTime @default(now())

  @@index([entity, createdAt])
}
```

---

### Dicas de implantação

1. **Extensões Postgres úteis**  
   - `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";` (se usar UUID)  
   - `CREATE EXTENSION IF NOT EXISTS "pg_trgm";` (busca textual na biblioteca)  
   - `CREATE EXTENSION IF NOT EXISTS "btree_gin";`  

2. **Índices adicionais (migr. SQL)**  
   - GIN para buscas por `body` (se usar JSON com texto indexável)  
   - Parcial por `Incident(status='PUBLISHED')` para mapas públicos  

3. **H3**  
   - Armazene `geoCellId` como `text` (string H3). A agregação visual no mapa usa esse campo, evitando endereço exato.  

4. **Versionamento de diagnóstico/biblioteca**  
   - `Question.version` e `Content.version` permitem evoluir sem quebrar respostas antigas.

Se quiser, eu já preparo:
- **migrations SQL** com índices GIN/parciais,  
- **seed** (tópicos, tags, perguntas base),  
- **exemplos de consultas** (incidentes por célula/período; score médio por tema; recomendação “3 urgências”).
