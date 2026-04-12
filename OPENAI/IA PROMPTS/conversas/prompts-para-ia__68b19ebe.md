---
source: DATAGPT
conversation_id: 68b19ebe-a688-8322-910b-b6893c0280a1
title: "Prompts para IA"
theme: IA PROMPTS
created: 2025-08-29T12:39:55.573520Z
message_count: 6
attachments_count: 0
---

# Prompts para IA

- Tema: `IA PROMPTS`
- Conversation ID: `68b19ebe-a688-8322-910b-b6893c0280a1`

## Transcrição

### user

Estou desenvolvendo  um aplicativo de geração de texto através da IA. Nesse aplicativo apresento um conjunto de conteúdos sobre determinado assunto. A IA precisa analisar esses conteúdos, organizar esses conteúdos sem alterar o texto original. Além disso deve produzir textos alargando e aprofundando cada um dos blocos de conteúdo, produzir texto para vincular um conteúdo ao outro. PAra tanto, preciso de prompts específicos para cada uma dessas funções: generateAIInsights()
generateTransition()
generateImprovementSuggestions()

### assistant

Paulo, abaixo vão três prompts “prontos-para-usar”, pensados para acoplar no seu app nas funções:

- `generateAIInsights()` → analisar, organizar (sem alterar) e **ampliar/aprofundar** cada bloco.
- `generateTransition()` → **conectar** blocos com textos-ponte.
- `generateImprovementSuggestions()` → **sugerir melhorias** editoriais/estruturais sem modificar o original.

Cada prompt inclui: objetivo, entradas esperadas, regras de segurança (não alterar o original; evitar alucinação), formato de saída e critérios de qualidade. Estão em português e prontos para colar como “system/developer prompts” do seu orquestrador.  


# Prompt para `generateAIInsights()`

**Objetivo**
Você é um analisador e redator técnico. Recebe um **conjunto de blocos de conteúdo** sobre um tema.  
1) **Organize** os blocos (sem alterar o texto original).  
2) **Extraia** ideias-chave, termos, claims e relações entre blocos.  
3) **Aprimore** cada bloco com um texto adicional que **expande e aprofunda** o conteúdo, mantendo coerência, neutralidade e sem inserir fatos externos não inferíveis.  
4) **Não reescreva nem edite** o conteúdo original.

**Entradas (JSON)**
```json
{
  "goal": "Finalidade do texto composto",
  "audience": "Público-alvo",
  "style_constraints": ["neutralidade", "precisão", "sinteticidade"],
  "blocks": [
    {
      "id": "B1",
      "title": "Título opcional",
      "text": "Conteúdo integral do bloco",
      "metadata": {"source": "nome_ou_id", "order_hint": 1}
    }
    // ... B2, B3, ...
  ]
}
```

**Regras**
- Não alterar `text` dos blocos.  
- Toda inferência deve ser **ancorada** em trechos explícitos; quando não for possível, rotule como `"status": "insufficient_evidence"`.  
- Terminologia: preservar a usada nos blocos; se padronizar termos, registrar no glossário de saída.  
- Estilo: informativo, sem adjetivação e sem juízos de valor.  
- Sem citações externas; se indispensável, marcar como “sugerir referência” no campo apropriado.

**Saída (JSON)**
```json
{
  "normalized_order": ["B1","B3","B2"], 
  "crosslinks": [
    {"from":"B1","to":"B3","relation":"complementa","evidence":"trecho..."},
    {"from":"B3","to":"B2","relation":"causa-efeito","evidence":"trecho..."}
  ],
  "per_block_insights": [
    {
      "id":"B1",
      "key_points":[ "…", "…" ],
      "assumptions":[ "…", "…" ],
      "gaps":[ "…", "…" ],
      "expanded_text":"<texto que amplia e aprofunda B1, 150–400 palavras, neutro, sem repetir o original>",
      "citations_to_blocks":[ "B1", "B3" ],
      "status":"ok | insufficient_evidence"
    }
  ],
  "glossary":[ {"term":"…","definition":"…","source_blocks":["B2"]} ],
  "suggested_references":[ {"topic":"…","why":"…"} ]
}
```

**Critérios de qualidade**
- Coerência entre “key_points” e “expanded_text”.  
- “expanded_text” deve **adensar** (exemplos, implicações, escopo/limites) sem trazer fatos não suportados.  
- “crosslinks” com evidência textual (citar trechos curtos).  
- Se algo for incerto, usar `"status": "insufficient_evidence"`.


# Prompt para `generateTransition()`

**Objetivo**
Gerar **parágrafos de transição** que conectem dois blocos (ou seções) preservando terminologia e lógica do conjunto.

**Entradas (JSON)**
```json
{
  "from_block": {
    "id":"B1",
    "title":"…",
    "summary":"Resumo objetivo de 2–3 frases do bloco de origem",
    "keywords":["k1","k2"]
  },
  "to_block": {
    "id":"B2",
    "title":"…",
    "summary":"Resumo objetivo de 2–3 frases do bloco de destino",
    "keywords":["k3","k4"]
  },
  "rhetorical_purpose": "continuidade|contraste|causa-efeito|síntese|problema-solução",
  "style_constraints": ["neutralidade","clareza","brevidade"],
  "length": "curta|média|longa"
}
```

**Regras**
- Não introduzir conceitos novos nem alterar conteúdo dos blocos.  
- Usar conectores adequados ao `rhetorical_purpose`.  
- Manter neutralidade e concisão.

**Saída (JSON)**
```json
{
  "transition":{
    "text":"<parágrafo único, 1–5 frases conforme length>",
    "purpose_used":"…",
    "terms_preserved":["k1","k3"]
  },
  "alternatives":[
    {"text":"<variação 1>","purpose_used":"…"},
    {"text":"<variação 2>","purpose_used":"…"}
  ]
}
```

**Critérios de qualidade**
- Progressão lógica clara do `from_block` ao `to_block`.  
- Vocabulário consistente com “keywords”.  
- Sem juízo de valor; sem adjetivação ornamental.


# Prompt para `generateImprovementSuggestions()`

**Objetivo**
Apresentar **sugestões de melhoria** (estrutura, clareza, coerência, lacunas, ordem, sinalização de seções, títulos, tabelas/figuras úteis), **sem editar o texto original**. Quando útil, oferecer **exemplo de reescrita** apenas como ilustração.

**Entradas (JSON)**
```json
{
  "goal":"Objetivo do documento",
  "audience":"Público-alvo",
  "global_constraints":["neutralidade","precisão","sinteticidade"],
  "blocks":[{"id":"B1","title":"…","text":"…"}, {"id":"B2","title":"…","text":"…"}]
}
```

**Regras**
- Classificar cada sugestão por **prioridade** (alta/média/baixa), **impacto esperado** (1–5) e **esforço estimado** (1–5).  
- Localizar a sugestão: bloco, parágrafo (se possível), ou “global”.  
- Não introduzir julgamentos; justificar tecnicamente (coerência, redundância, ordenação, definição de termos, necessidade de quadro/tabela).  
- Quando fornecer “exemplo de reescrita”, marcar explicitamente como **opcional** e **ilustrativo**.

**Saída (JSON)**
```json
{
  "global_findings":[
    {"issue":"inconsistência terminológica","evidence":"termos X/Y","suggestion":"padronizar por…","impact":4,"effort":2,"priority":"alta"}
  ],
  "block_level_suggestions":[
    {
      "id":"B2",
      "findings":[
        {
          "issue":"ordem de argumentos",
          "evidence":"parágrafos 2→1 alteram causalidade",
          "suggestion":"inverter subseções 1.2 e 1.3",
          "impact":5,"effort":2,"priority":"alta",
          "example_rewrite_optional":"[exemplo ilustrativo, 3–5 frases]"
        }
      ]
    }
  ],
  "checklist_next_actions":[
    "Padronizar termos com glossário",
    "Inserir tabela de definições no início da seção 1"
  ]
}
```

**Critérios de qualidade**
- Sugestões concretas, localizadas e justificadas por evidência do texto.  
- Priorização clara (impacto × esforço).  
- Nenhuma alteração direta do corpus original; apenas recomendações.


---

## Observações de implementação

- **Temperatura** recomendada: 0.2–0.4 para consistência.  
- **Limites de tamanho**: defina `max_tokens` por bloco conforme orçamento.  
- **Validação**: aplique um verificador que rejeite saídas sem o JSON esperado.  
- **Auditoria de alterações**: ao publicar, sempre referenciar apenas os textos de “expanded_text” e “transitions”; o corpus original permanece imutável.

Se quiser, já posso rodar um teste com 2–3 blocos reais seus e ajustar os campos.

### user

Analise esse código: "use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AIAgent = void 0;
const openai_1 = __importDefault(require("openai"));
const dotenv = __importStar(require("dotenv"));
// Carrega variáveis de ambiente
dotenv.config();
class AIAgent {
    constructor(model) {
        this.model = model || new OpenAIModel();
    }
    analyzeMarkdown(markdownContent) {
        return __awaiter(this, void 0, void 0, function* () {
            try {
                console.log(`Ágente IA analisando conteúdo: "${markdownContent.title}"...`);
                return yield this.model.generateInsights(markdownContent);
            }
            catch (error) {
                console.error('Erro na análise do markdown:', error);
                throw error;
            }
        });
    }
    generateContent(insights) {
        let generatedContent = '';
        // Gera conteúdo baseado nos insights sem marcações
        if (insights.introduction) {
            generatedContent += `${insights.introduction}\\n\\n`;
        }
        if (insights.connections.length > 0) {
            insights.connections.forEach((connection) => {
                generatedContent += `${connection}\\n\\n`;
            });
        }
        if (insights.expansions.length > 0) {
            insights.expansions.forEach((expansion) => {
                generatedContent += `${expansion}\\n\\n`;
            });
        }
        if (insights.conclusions.length > 0) {
            insights.conclusions.forEach((conclusion) => {
                generatedContent += `${conclusion}\\n\\n`;
            });
        }
        return generatedContent;
    }
    generateTransitions(sections) {
        return __awaiter(this, void 0, void 0, function* () {
            const sectionTitles = sections.map(s => s.title);
            return yield this.model.generateTransitions(sectionTitles);
        });
    }
    generateTransitionsFromTitles(titles) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield this.model.generateTransitions(titles);
        });
    }
    suggestImprovements(content) {
        return __awaiter(this, void 0, void 0, function* () {
            return yield this.model.suggestImprovements(content);
        });
    }
}
exports.AIAgent = AIAgent;
// Implementação real do modelo OpenAI
class OpenAIModel {
    constructor() {
        if (!process.env.OPENAI_API_KEY) {
            throw new Error('OPENAI_API_KEY não encontrada nas variáveis de ambiente');
        }
        this.openai = new openai_1.default({
            apiKey: process.env.OPENAI_API_KEY,
        });
    }
    generateInsights(content) {
        var _a, _b;
        return __awaiter(this, void 0, void 0, function* () {
            try {
                const prompt = this.buildInsightsPrompt(content);
                const completion = yield this.openai.chat.completions.create({
                    model: "gpt-3.5-turbo",
                    messages: [
                        {
                            role: "system",
                            content: "Você é um assistente especializado em análise de conteúdo e geração de insights educacionais. Responda sempre em português brasileiro."
                        },
                        {
                            role: "user",
                            content: prompt
                        }
                    ],
                    max_tokens: 1500,
                    temperature: 0.7
                });
                const response = ((_b = (_a = completion.choices[0]) === null || _a === void 0 ? void 0 : _a.message) === null || _b === void 0 ? void 0 : _b.content) || '';
                return this.parseInsightsResponse(response, content);
            }
            catch (error) {
                console.error('Erro ao gerar insights com OpenAI:', error);
                // Fallback para mock em caso de erro
                const mockModel = new MockAIModel();
                return mockModel.generateInsights(content);
            }
        });
    }
    generateTransitions(sections) {
        var _a, _b, _c;
        return __awaiter(this, void 0, void 0, function* () {
            try {
                const transitions = [];
                for (let i = 0; i < sections.length - 1; i++) {
                    const current = sections[i];
                    const next = sections[i + 1];
                    const prompt = `Crie uma transição natural e educativa entre as seções "${current}" e "${next}". A transição deve conectar os temas de forma fluida e pedagógica. Responda apenas com o texto da transição, sem formatação adicional.`;
                    const completion = yield this.openai.chat.completions.create({
                        model: "gpt-3.5-turbo",
                        messages: [
                            {
                                role: "system",
                                content: "Você é um especialista em redação educacional. Crie transições claras e envolventes entre seções de conteúdo."
                            },
                            {
                                role: "user",
                                content: prompt
                            }
                        ],
                        max_tokens: 200,
                        temperature: 0.6
                    });
                    const transition = ((_c = (_b = (_a = completion.choices[0]) === null || _a === void 0 ? void 0 : _a.message) === null || _b === void 0 ? void 0 : _b.content) === null || _c === void 0 ? void 0 : _c.trim()) || '';
                    if (transition) {
                        transitions.push(transition);
                    }
                }
                return transitions;
            }
            catch (error) {
                console.error('Erro ao gerar transições com OpenAI:', error);
                // Fallback para mock em caso de erro
                const mockModel = new MockAIModel();
                return mockModel.generateTransitions(sections);
            }
        });
    }
    suggestImprovements(content) {
        var _a, _b;
        return __awaiter(this, void 0, void 0, function* () {
            try {
                const prompt = `Analise o seguinte conteúdo e sugira 3-5 melhorias específicas para torná-lo mais claro, envolvente e educativo:\\n\\n${content.substring(0, 1000)}...`;
                const completion = yield this.openai.chat.completions.create({
                    model: "gpt-3.5-turbo",
                    messages: [
                        {
                            role: "system",
                            content: "Você é um consultor educacional especializado em melhoria de conteúdo. Forneça sugestões práticas e específicas."
                        },
                        {
                            role: "user",
                            content: prompt
                        }
                    ],
                    max_tokens: 500,
                    temperature: 0.5
                });
                const response = ((_b = (_a = completion.choices[0]) === null || _a === void 0 ? void 0 : _a.message) === null || _b === void 0 ? void 0 : _b.content) || '';
                return this.parseSuggestions(response);
            }
            catch (error) {
                console.error('Erro ao gerar sugestões com OpenAI:', error);
                // Fallback para mock em caso de erro
                const mockModel = new MockAIModel();
                return mockModel.suggestImprovements(content);
            }
        });
    }
    buildInsightsPrompt(content) {
        const sectionsText = content.sections.map(s => `${s.heading}: ${s.content.substring(0, 200)}...`).join('\\n');
        return `Analise o seguinte conteúdo sobre "${content.title}" e forneça insights educacionais estruturados:\\n\\n${sectionsText}\\n\\nPor favor, forneça:\\n1. Uma introdução envolvente (2-3 frases)\\n2. 2-3 conclusões principais\\n3. 2-3 conexões entre os temas\\n4. 2-3 sugestões de expansão do conteúdo\\n\\nFormate sua resposta de forma clara e organizada.`;
    }
    parseInsightsResponse(response, content) {
        // Parser simples para extrair insights da resposta da IA
        const lines = response.split('\\n').filter(line => line.trim());
        let introduction = '';
        const conclusions = [];
        const connections = [];
        const expansions = [];
        let currentSection = '';
        for (const line of lines) {
            const trimmed = line.trim();
            if (trimmed.toLowerCase().includes('introdução') || trimmed.toLowerCase().includes('introduction')) {
                currentSection = 'introduction';
                continue;
            }
            else if (trimmed.toLowerCase().includes('conclus') || trimmed.toLowerCase().includes('conclusion')) {
                currentSection = 'conclusions';
                continue;
            }
            else if (trimmed.toLowerCase().includes('conexõ') || trimmed.toLowerCase().includes('connection')) {
                currentSection = 'connections';
                continue;
            }
            else if (trimmed.toLowerCase().includes('expansão') || trimmed.toLowerCase().includes('expansion')) {
                currentSection = 'expansions';
                continue;
            }
            if (trimmed && !trimmed.match(/^\\d+\\./)) {
                switch (currentSection) {
                    case 'introduction':
                        if (!introduction)
                            introduction = trimmed;
                        break;
                    case 'conclusions':
                        if (conclusions.length < 3)
                            conclusions.push(trimmed.replace(/^[-*]\\s*/, ''));
                        break;
                    case 'connections':
                        if (connections.length < 3)
                            connections.push(trimmed.replace(/^[-*]\\s*/, ''));
                        break;
                    case 'expansions':
                        if (expansions.length < 3)
                            expansions.push(trimmed.replace(/^[-*]\\s*/, ''));
                        break;
                }
            }
        }
        // Fallback para valores padrão se o parsing falhar
        if (!introduction) {
            introduction = `Este documento sobre "${content.title}" apresenta uma análise abrangente do tema com insights valiosos.`;
        }
        return {
            introduction,
            conclusions: conclusions.length > 0 ? conclusions : [`Análise detalhada de ${content.sections.length} seções principais.`],
            connections: connections.length > 0 ? connections : ['Conexões identificadas entre os temas principais.'],
            expansions: expansions.length > 0 ? expansions : ['Oportunidades de expansão do conteúdo identificadas.']
        };
    }
    parseSuggestions(response) {
        const lines = response.split('\\n').filter(line => line.trim());
        const suggestions = [];
        for (const line of lines) {
            const trimmed = line.trim();
            if (trimmed && (trimmed.match(/^\\d+\\./) || trimmed.match(/^[-*]/))) {
                suggestions.push(trimmed.replace(/^\\d+\\.\\s*/, '').replace(/^[-*]\\s*/, ''));
            }
        }
        return suggestions.length > 0 ? suggestions : ['Considere adicionar mais exemplos práticos.', 'Melhore a estrutura com subtítulos.', 'Adicione resumos ao final de cada seção.'];
    }
}
// Implementação mock do modelo de IA
class MockAIModel {
    generateInsights(content) {
        return __awaiter(this, void 0, void 0, function* () {
            const themes = this.extractThemesFromContent(content);
            return {
                introduction: this.generateIntroduction(content),
                conclusions: this.generateConclusions(content, themes),
                connections: this.generateConnections(content),
                expansions: this.generateExpansions(content, themes)
            };
        });
    }
    generateTransitions(sections) {
        return __awaiter(this, void 0, void 0, function* () {
            const transitions = [];
            for (let i = 0; i < sections.length - 1; i++) {
                const current = sections[i];
                const next = sections[i + 1];
                const transitionTemplates = [
                    `Tendo explorado ${current}, vamos agora examinar ${next} e como se relaciona com o tópico anterior.`,
                    `A partir do que foi discutido sobre ${current}, é natural prosseguirmos para ${next}.`,
                    `Construindo sobre os conceitos de ${current}, chegamos a ${next}.`,
                    `A compreensão de ${current} nos prepara para aprofundar ${next}.`
                ];
                const randomTemplate = transitionTemplates[Math.floor(Math.random() * transitionTemplates.length)];
                transitions.push(randomTemplate);
            }
            return transitions;
        });
    }
    suggestImprovements(content) {
        return __awaiter(this, void 0, void 0, function* () {
            const suggestions = [];
            // Analisa o conteúdo e sugere melhorias
            if (content.length < 500) {
                suggestions.push('Considere expandir o conteúdo com mais detalhes e exemplos.');
            }
            if (!content.includes('exemplo') && !content.includes('caso')) {
                suggestions.push('Adicionar exemplos práticos pode melhorar a compreensão.');
            }
            if (!content.match(/\\d+\\./)) {
                suggestions.push('Listas numeradas podem melhorar a estrutura do conteúdo.');
            }
            if (content.split('\\n\\n').length < 3) {
                suggestions.push('Dividir o conteúdo em parágrafos menores melhora a legibilidade.');
            }
            return suggestions;
        });
    }
    generateIntroduction(content) {
        const introTemplates = [
            `Este documento sobre "${content.title}" apresenta uma abordagem abrangente do tema, explorando ${content.sections.length} aspectos fundamentais. A análise que segue busca conectar os conceitos apresentados e fornecer insights adicionais para uma compreensão mais profunda.`,
            `"${content.title}" é um tópico de grande relevância que merece uma exploração detalhada. Este conteúdo foi estruturado para oferecer uma visão clara e organizada dos principais conceitos envolvidos.`,
            `A compreensão adequada de "${content.title}" requer uma abordagem sistemática e bem estruturada. Este material foi desenvolvido para facilitar o aprendizado e a aplicação prática dos conceitos apresentados.`
        ];
        return introTemplates[Math.floor(Math.random() * introTemplates.length)];
    }
    generateConclusions(content, themes) {
        const conclusions = [];
        if (themes.length > 0) {
            conclusions.push(`Os temas principais identificados (${themes.join(', ')}) demonstram a complexidade e abrangência do assunto.`);
        }
        conclusions.push(`A estruturação em ${content.sections.length} seções permite uma progressão lógica do aprendizado.`);
        if (content.sections.some(s => s.content.includes('exemplo'))) {
            conclusions.push('A inclusão de exemplos práticos fortalece a compreensão teórica.');
        }
        conclusions.push('Este conteúdo serve como base sólida para aprofundamento futuro no tema.');
        return conclusions;
    }
    generateConnections(content) {
        const connections = [];
        // Analisa conexões entre seções
        for (let i = 0; i < content.sections.length - 1; i++) {
            const current = content.sections[i];
            const next = content.sections[i + 1];
            connections.push(`A seção "${current.heading}" estabelece fundamentos que são desenvolvidos em "${next.heading}".`);
        }
        // Adiciona conexões temáticas
        const themes = this.extractThemesFromContent(content);
        if (themes.length >= 2) {
            connections.push(`Existe uma relação sinérgica entre ${themes[0]} e ${themes[1]} ao longo do documento.`);
        }
        return connections;
    }
    generateExpansions(content, themes) {
        const expansions = [];
        themes.forEach((theme, index) => {
            const expansionTemplates = [
                `O tema ${theme} merece maior exploração, especialmente considerando suas aplicações práticas e implicações futuras. Pesquisas adicionais nesta área podem revelar insights valiosos para a compreensão completa do assunto.`,
                `${theme} representa um aspecto fundamental que se conecta com diversas outras áreas do conhecimento. Uma análise mais profunda pode revelar oportunidades de inovação e desenvolvimento.`,
                `A importância de ${theme} se estende além do escopo inicial, sugerindo a necessidade de uma abordagem interdisciplinar para sua completa compreensão.`
            ];
            if (index < 3) { // Limita a 3 expansões
                expansions.push(expansionTemplates[index % expansionTemplates.length]);
            }
        });
        return expansions;
    }
    extractThemesFromContent(content) {
        const themes = new Set();
        // Extrai temas dos títulos das seções
        content.sections.forEach(section => {
            const words = section.heading.toLowerCase().split(' ');
            words.forEach(word => {
                if (word.length > 4) { // Palavras com mais de 4 caracteres
                    themes.add(word);
                }
            });
        });
        return Array.from(themes).slice(0, 5); // Limita a 5 temas
    }
}

### assistant

Paulo, segue uma análise objetiva do código com pontos de risco, melhorias sugeridas e pequenos patches prontos.

# Problemas e riscos imediatos

1) Acesso a propriedades sem “guard”
- Uso de `insights.connections.length`, `insights.expansions.length`, etc., sem garantir que existam. Isso pode lançar erro quando a IA falhar no parse.
  
Patch:
```js
generateContent(insights) {
  const safe = {
    introduction: insights?.introduction ?? "",
    connections: Array.isArray(insights?.connections) ? insights.connections : [],
    expansions: Array.isArray(insights?.expansions) ? insights.expansions : [],
    conclusions: Array.isArray(insights?.conclusions) ? insights.conclusions : [],
  };
  return [
    safe.introduction,
    ...safe.connections,
    ...safe.expansions,
    ...safe.conclusions
  ].filter(Boolean).join("\\n\\n");
}
```

2) Parser frágil (perde itens numerados)
- `parseInsightsResponse` ignora linhas numeradas (`^\\d+\\.`), mas boa parte dos modelos retorna listas numeradas. Resultado: você descarta conteúdo válido.

Patch (aceitar bullets e números):
```js
const isList = (s) => /^\\s*(?:[-*]|\\d+\\.)\\s*/.test(s);
...
if (trimmed) {
  const clean = trimmed.replace(/^\\s*(?:[-*]|\\d+\\.)\\s*/, '');
  switch (currentSection) {
    case 'introduction':
      if (!introduction) introduction = clean;
      break;
    case 'conclusions':
      if (conclusions.length < 3) conclusions.push(clean);
      break;
    case 'connections':
      if (connections.length < 3) connections.push(clean);
      break;
    case 'expansions':
      if (expansions.length < 3) expansions.push(clean);
      break;
  }
}
```

3) Transições fazem N−1 chamadas à API
- `generateTransitions` chama a API por par de títulos, elevando latência e risco de rate limit.

Patch (uma chamada única):
```js
async generateTransitions(sections) {
  try {
    const prompt = [
      "Gere transições curtas, uma por par sequencial, apenas texto. Retorne como JSON:",
      " { \\"transitions\\": [\\"...\\", \\"...\\"] }",
      "",
      "Títulos:",
      ...sections.map((t, i) => `${i+1}. ${t}`)
    ].join("\\n");
    const completion = await this.openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: [
        { role: "system", content: "Especialista em redação educacional. Responda em JSON válido." },
        { role: "user", content: prompt }
      ],
      temperature: 0.4,
      max_tokens: 600
    });
    const content = completion.choices?.[0]?.message?.content ?? "{}";
    const parsed = JSON.parse(content);
    return Array.isArray(parsed.transitions) ? parsed.transitions : [];
  } catch (e) {
    console.error("Erro ao gerar transições:", e);
    const mockModel = new MockAIModel();
    return mockModel.generateTransitions(sections);
  }
}
```

4) Prompt de insights não pede saída estruturada
- Você parseia texto livre. Isso é frágil. Melhor exigir **JSON** na saída.

Patch (construção do prompt):
```js
buildInsightsPrompt(content) {
  const sectionsText = content.sections
    .map(s => `${s.heading}: ${s.content.substring(0, 400)}...`)
    .join('\\n');

  return [
    `Analise o conteúdo sobre "${content.title}" e RETORNE ESTRITAMENTE EM JSON com o schema:`,
    `{"introduction": "string", "conclusions": ["string"], "connections": ["string"], "expansions": ["string"]}`,
    "",
    sectionsText,
    "",
    "Regras:",
    "- Não reescreva o texto original.",
    "- Seja sintético e técnico, sem juízos de valor.",
    "- Limites: conclusions/connections/expansions com 2–4 itens cada.",
  ].join("\\n");
}
```

E o parse pode virar um `try { JSON.parse(...) } catch { fallback }`:
```js
const response = completion.choices?.[0]?.message?.content ?? '{}';
let parsed;
try { parsed = JSON.parse(response); } catch { parsed = null; }
return {
  introduction: parsed?.introduction ?? `Este documento sobre "${content.title}" ...`,
  conclusions: Array.isArray(parsed?.conclusions) && parsed.conclusions.length ? parsed.conclusions : [`Análise de ${content.sections.length} seções.`],
  connections: Array.isArray(parsed?.connections) && parsed.connections.length ? parsed.connections : ['Conexões entre temas principais.'],
  expansions: Array.isArray(parsed?.expansions) && parsed.expansions.length ? parsed.expansions : ['Oportunidades de expansão identificadas.'],
};
```

5) Dependência forte de `gpt-3.5-turbo`
- Modelo hardcoded. Sugestão: tornar modelo configurável por parâmetro/ENV e aceitar “response_format: { type: 'json_object' }” quando disponível. Evita regressões de parsing.

Patch:
```js
constructor({ modelName, jsonPreferred = true } = {}) {
  if (!process.env.OPENAI_API_KEY) {
    throw new Error('OPENAI_API_KEY não encontrada nas variáveis de ambiente');
  }
  this.modelName = modelName || process.env.OPENAI_MODEL || "gpt-3.5-turbo";
  this.jsonPreferred = jsonPreferred;
  this.openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
}
```
E nas chamadas:
```js
const opts = {
  model: this.modelName,
  messages,
  max_tokens: 1500,
  temperature: 0.4,
};
if (this.jsonPreferred) opts.response_format = { type: "json_object" };
const completion = await this.openai.chat.completions.create(opts);
```

6) Ausência de validação do input
- Estrutura esperada de `content` não é validada.

Patch (validação mínima):
```js
function assertContentShape(content) {
  if (!content || typeof content.title !== "string" || !Array.isArray(content.sections)) {
    throw new Error("Formato inválido de content: esperado { title: string, sections: {heading, content}[] }");
  }
}
...
generateInsights(content) {
  assertContentShape(content);
  ...
}
```

7) Tratamento de erros e retentativas
- Sem retentativas exponenciais, nem timeouts configuráveis.

Patch (retentativa simples):
```js
async function withRetry(fn, attempts = 3) {
  let last;
  for (let i = 0; i < attempts; i++) {
    try { return await fn(); } catch (e) { last = e; await new Promise(r => setTimeout(r, (2 ** i) * 250)); }
  }
  throw last;
}
...
const completion = await withRetry(() => this.openai.chat.completions.create(opts));
```

8) Logging
- `console.log` pode expor conteúdo sensível. E há um acento: `"Ágente"`.

Patch:
```js
console.log(`Agente IA analisando: "${markdownContent.title}" (${markdownContent.sections?.length ?? 0} seções)`);
```
Sugestão: injetar um logger e suportar níveis (info/warn/error) e mascaramento.

9) `suggestImprovements` trunca o conteúdo
- `substring(0, 1000)` pode cortar contexto crucial. Melhor resumir antes (ou iterar por seções) e também exigir saída em JSON.

Patch de prompt:
```js
const prompt = [
  "Analise o conteúdo a seguir (resumido por seções) e sugira 3–5 melhorias específicas.",
  "Retorne ESTRITAMENTE em JSON: {\\"suggestions\\":[{\\"issue\\":\\"...\\",\\"suggestion\\":\\"...\\",\\"impact\\":1-5,\\"effort\\":1-5,\\"priority\\":\\"alta|media|baixa\\"}]}",
  "",
  ...content.sections.map(s => `### ${s.heading}\\n${s.content.substring(0, 500)}...`)
].join("\\n");
```
E parse via `JSON.parse`.

10) Duplicação de método
- `generateTransitions` e `generateTransitionsFromTitles` fazem o mesmo. Mantenha apenas um e aceite `sections: string[] | {title:string}[]`.

Patch:
```js
async generateTransitions(input) {
  const titles = Array.isArray(input) && typeof input[0] === "string"
    ? input
    : input.map(s => s.title);
  return this.model.generateTransitions(titles);
}
```

# Recomendações arquiteturais

- **Saída estruturada em JSON** em todas as funções da IA (insights, transições, sugestões). Reduz parsing frágil.
- **Camada de “schema-check”**: valide a estrutura do JSON retornado (Zod/Yup) antes de usar.
- **Configuração externa**: modelo, temperatura, tokens, “jsonPreferred”, tempo de timeout e número de retentativas por ENV.
- **Batching** quando possível (ex.: transições).
- **Separar prompts** em arquivos/versionar (ex.: `prompts/insights.v1.md`), facilitando A/B e rollback.
- **Mock determinístico**: remova aleatoriedade do `MockAIModel` para testes reproduzíveis.

# Exemplo: contrato de saída único para `generateAIInsights()`

```ts
// Tipo alvo
type Insights = {
  introduction: string;
  conclusions: string[];
  connections: string[];
  expansions: string[];
};

// Validação simples (runtime)
function normalizeInsights(x: any): Insights {
  return {
    introduction: typeof x?.introduction === "string" ? x.introduction : "",
    conclusions: Array.isArray(x?.conclusions) ? x.conclusions.filter(Boolean) : [],
    connections: Array.isArray(x?.connections) ? x.connections.filter(Boolean) : [],
    expansions: Array.isArray(x?.expansions) ? x.expansions.filter(Boolean) : [],
  };
}
```

# Melhorias de prompts (alinhado às suas funções)

- `generateAIInsights()` → Exigir JSON com chaves explícitas e limites (2–4 itens), pedir neutralidade e proibir reescrever original.
- `generateTransition()` → Uma chamada única com lista de títulos, retorno `{"transitions":["..."]}`.
- `generateImprovementSuggestions()` → Exigir JSON com `issue`, `suggestion`, `impact`, `effort`, `priority`; localizar por seção quando possível.

# Pequenas correções adicionais

- Corrigir “Ágente” → “Agente”.
- Garantir `dotenv.config()` ocorra cedo, mas permitir override via parâmetros do construtor.
- Tratar `max_tokens` de modo proporcional ao tamanho do input (e.g., reduzir quando muitas seções).

Se quiser, eu adapto o seu arquivo completo com esses patches (mantendo CommonJS) ou entrego a versão TypeScript tipada com interfaces e validações.

### user

Quero que voce faça as correções necessárias, o prompt para o agente deve conter: 1- não faça nenhuma marcação ou inserção de títulos no texto final do tipo : " # Insights e Análises da IA;  ### Análise e Contexto; ### Análise Estruturada por Seção; #### Seção sem título, entre outras" . Preciso de texto limpos, sequenciais, parágrafo por parágrafo, apenas com os tópicos capitulares. Faça o código correto para ser inserido no arquivo

### assistant

Paulo, segue um patch pronto para colar no seu arquivo, alinhado ao requisito: **o agente não deve inserir NENHUM título/heading no texto final** (sem “#”, “Introdução:”, “Conclusões:”, etc.). O prompt agora exige saída **em JSON** e já pede um campo `clean_paragraphs` com **parágrafos limpos, sequenciais**, sem marcação. O método `generateContent` prioriza esses parágrafos. Incluí também correções de robustez (guards, batching de transições, configuração de modelo, retry simples).

```js
// === PATCH: util de retry simples ===
async function withRetry(fn, attempts = 3) {
  let last;
  for (let i = 0; i < attempts; i++) {
    try {
      return await fn();
    } catch (e) {
      last = e;
      await new Promise(r => setTimeout(r, (2 ** i) * 250));
    }
  }
  throw last;
}

// === PATCH: AIAgent.generateContent com guards e uso de parágrafos limpos ===
generateContent(insights) {
  // Prioriza parágrafos limpos, sem headings/marcações
  const cleanParagraphs = Array.isArray(insights?.clean_paragraphs)
    ? insights.clean_paragraphs.filter(p => typeof p === "string" && p.trim())
    : [];

  if (cleanParagraphs.length > 0) {
    return cleanParagraphs.join("\\n\\n");
  }

  // Fallback: concatena campos estruturados em parágrafos, sem títulos
  const safe = {
    introduction: typeof insights?.introduction === "string" ? insights.introduction : "",
    connections: Array.isArray(insights?.connections) ? insights.connections : [],
    expansions: Array.isArray(insights?.expansions) ? insights.expansions : [],
    conclusions: Array.isArray(insights?.conclusions) ? insights.conclusions : [],
  };

  return [
    safe.introduction,
    ...safe.connections,
    ...safe.expansions,
    ...safe.conclusions
  ].filter(Boolean).map(s => String(s).replace(/^\\s*(?:#+|\\*\\*?[^\\w]|[-*]|\\d+\\.)\\s*/g, "")).join("\\n\\n");
}

// === PATCH: implementação do modelo OpenAI com config e JSON ===
class OpenAIModel {
  constructor({ modelName, jsonPreferred = true } = {}) {
    if (!process.env.OPENAI_API_KEY) {
      throw new Error('OPENAI_API_KEY não encontrada nas variáveis de ambiente');
    }
    this.openai = new (require("openai"))({
      apiKey: process.env.OPENAI_API_KEY,
    });
    this.modelName = modelName || process.env.OPENAI_MODEL || "gpt-3.5-turbo";
    this.jsonPreferred = jsonPreferred !== false; // padrão true
  }

  // === PATCH: validação mínima do input ===
  static assertContentShape(content) {
    if (
      !content ||
      typeof content.title !== "string" ||
      !Array.isArray(content.sections) ||
      !content.sections.every(s => typeof s?.heading === "string" && typeof s?.content === "string")
    ) {
      throw new Error("Formato inválido de content: esperado { title: string, sections: {heading, content}[] }");
    }
  }

  // === PATCH: prompt de insights com exigência de JSON e parágrafos limpos, sem headings ===
  buildInsightsPrompt(content) {
    const sectionsText = content.sections
      .map(s => `TÍTULO: ${s.heading}\\nTEXTO: ${s.content.substring(0, 800)}\\n`)
      .join('\\n');

    return [
      `Tarefa: analisar o conteúdo sobre "${content.title}" e retornar ESTRITAMENTE em JSON.`,
      `Schema de saída obrigatório:`,
      `{
  "introduction": "string",
  "conclusions": ["string", ...],
  "connections": ["string", ...],
  "expansions": ["string", ...],
  "clean_paragraphs": ["string", ...]
}`,
      `Regras editoriais obrigatórias:`,
      `- NÃO inserir títulos, headings ou marcações no texto final (ex.: "#", "##", "Introdução:", "Conclusões:", "Análise:", "###", etc.).`,
      `- "clean_paragraphs" deve conter SOMENTE parágrafos limpos, sequenciais, sem qualquer rótulo, heading, bullet ou numeração.`,
      `- Os parágrafos devem apresentar o conteúdo de forma contínua, neutra e técnica, respeitando o material-fonte, sem reescrever os trechos originais.`,
      `- Não usar markdown, bullets, listas ou numeração nos parágrafos de "clean_paragraphs".`,
      `- Use a terminologia dos blocos; evite introduzir fatos externos não sustentados pelos trechos fornecidos.`,
      `- Tamanho recomendado por parágrafo: 2–6 frases.`,
      ``,
      `Conteúdo (amostrado por seção):`,
      sectionsText
    ].join("\\n");
  }

  // === PATCH: generateInsights com response_format JSON e parse robusto ===
  async generateInsights(content) {
    OpenAIModel.assertContentShape(content);
    try {
      const prompt = this.buildInsightsPrompt(content);
      const messages = [
        {
          role: "system",
          content: "Você é um analisador/redator técnico. Retorne estritamente em JSON válido (um único objeto)."
        },
        { role: "user", content: prompt }
      ];

      const opts = {
        model: this.modelName,
        messages,
        max_tokens: 1600,
        temperature: 0.3
      };
      if (this.jsonPreferred) {
        // Alguns modelos suportam esse parâmetro; se não, o parse abaixo lida com texto JSON puro.
        opts.response_format = { type: "json_object" };
      }

      const completion = await withRetry(() => this.openai.chat.completions.create(opts));
      const raw = completion.choices?.[0]?.message?.content ?? "{}";

      let parsed;
      try { parsed = JSON.parse(raw); } catch { parsed = null; }

      return this.normalizeInsights(parsed, content);
    } catch (error) {
      console.error('Erro ao gerar insights com OpenAI:', error);
      const mockModel = new MockAIModel();
      return mockModel.generateInsights(content);
    }
  }

  // === PATCH: normalizador da saída ===
  normalizeInsights(x, content) {
    const defIntro = `Este documento sobre "${content.title}" apresenta uma análise técnica do tema.`;
    const safeArr = a => Array.isArray(a) ? a.filter(v => typeof v === "string" && v.trim()) : [];

    const cleanParagraphs = safeArr(x?.clean_paragraphs).map(p =>
      p.replace(/^\\s*(?:#+|[-*]|\\d+\\.)\\s*/g, '').trim()
    );

    return {
      introduction: typeof x?.introduction === "string" ? x.introduction : defIntro,
      conclusions: safeArr(x?.conclusions),
      connections: safeArr(x?.connections),
      expansions: safeArr(x?.expansions),
      clean_paragraphs: cleanParagraphs
    };
  }

  // === PATCH: generateTransitions em uma única chamada, com JSON ===
  async generateTransitions(sectionTitles) {
    try {
      const titles = sectionTitles.map(String);
      const prompt = [
        "Gere transições curtas (1–3 frases), uma para CADA par sequencial de títulos abaixo.",
        "Retorne ESTRITAMENTE em JSON: {\\"transitions\\":[\\"...\\",\\"...\\", ...]}",
        "Regras:",
        "- Não use headings, bullets, listas ou markdown.",
        "- Não introduza novos conceitos; apenas conecte o que é esperado de um título ao seguinte.",
        "",
        "Títulos:",
        ...titles.map((t, i) => `${i + 1}. ${t}`)
      ].join("\\n");

      const messages = [
        { role: "system", content: "Especialista em redação técnica. Responda em JSON válido (um único objeto)." },
        { role: "user", content: prompt }
      ];

      const opts = {
        model: this.modelName,
        messages,
        temperature: 0.3,
        max_tokens: 600
      };
      if (this.jsonPreferred) {
        opts.response_format = { type: "json_object" };
      }

      const completion = await withRetry(() => this.openai.chat.completions.create(opts));
      const raw = completion.choices?.[0]?.message?.content ?? "{}";
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed?.transitions) ? parsed.transitions : [];
    } catch (error) {
      console.error('Erro ao gerar transições com OpenAI:', error);
      const mockModel = new MockAIModel();
      return mockModel.generateTransitions(sectionTitles);
    }
  }

  // === PATCH: suggestImprovements retornando JSON estruturado ===
  async suggestImprovements(content) {
    try {
      const head = (s, n) => (s || "").substring(0, n);
      const sectionsSumm = Array.isArray(content?.sections)
        ? content.sections.map(s => `### ${s.heading}\\n${head(s.content, 800)}\\n`).join("\\n")
        : head(String(content || ""), 2000);

      const prompt = [
        "Analise o conteúdo (resumido) e sugira 3–5 melhorias específicas.",
        "Retorne ESTRITAMENTE em JSON com o schema:",
        "{\\"suggestions\\":[{\\"issue\\":\\"...\\",\\"suggestion\\":\\"...\\",\\"impact\\":1,\\"effort\\":1,\\"priority\\":\\"alta|media|baixa\\"}]}",
        "Regras:",
        "- Justifique tecnicamente (coerência, clareza, ordem, definições).",
        "- Localize por seção quando possível, sem editar o original.",
        "",
        sectionsSumm
      ].join("\\n");

      const messages = [
        { role: "system", content: "Consultor editorial técnico. Responda em JSON válido (um único objeto)." },
        { role: "user", content: prompt }
      ];

      const opts = {
        model: this.modelName,
        messages,
        temperature: 0.3,
        max_tokens: 700
      };
      if (this.jsonPreferred) {
        opts.response_format = { type: "json_object" };
      }

      const completion = await withRetry(() => this.openai.chat.completions.create(opts));
      const raw = completion.choices?.[0]?.message?.content ?? "{}";
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed?.suggestions) ? parsed.suggestions : [];
    } catch (error) {
      console.error('Erro ao gerar sugestões com OpenAI:', error);
      const mockModel = new MockAIModel();
      return mockModel.suggestImprovements(content);
    }
  }
}

// === PATCH: corrigir log na AIAgent.analyzeMarkdown ===
analyzeMarkdown(markdownContent) {
  return (async () => {
    try {
      console.log(`Agente IA analisando: "${markdownContent.title}" (${markdownContent.sections?.length ?? 0} seções)`);
      return await this.model.generateInsights(markdownContent);
    } catch (error) {
      console.error('Erro na análise do markdown:', error);
      throw error;
    }
  })();
}

// === PATCH: unificar generateTransitions para aceitar títulos ou objetos ===
async generateTransitions(sectionsOrTitles) {
  const titles = Array.isArray(sectionsOrTitles) && typeof sectionsOrTitles[0] === "string"
    ? sectionsOrTitles
    : sectionsOrTitles.map(s => s.title);
  return await this.model.generateTransitions(titles);
}
```

**O que mudou para atender seu requisito central**
- O **prompt de insights** agora exige `clean_paragraphs` e especifica: **não usar headings/markdown**; produzir **parágrafos limpos, sequenciais**, sem “Introdução:”, “Conclusões:” ou similares.
- `generateContent` passa a **priorizar `clean_paragraphs`**. Se o modelo não retornar esse campo, faz fallback para os demais campos, ainda assim **removendo qualquer marcação** residual.
- As **transições** e **sugestões** também foram ajustadas para responder em **JSON** e sem headings.

Se quiser, eu preparo uma versão TypeScript tipada (interfaces para `Insights`, `Suggestion`, etc.) ou adapto à sua arquitetura de injeção de prompts (arquivos em `prompts/`).
