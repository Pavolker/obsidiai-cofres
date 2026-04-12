---
source: DATAGPT
conversation_id: edddb2df-c7cd-4778-81f6-c57a11a8071e
title: "Racionalismo e suas Sub-escolas"
theme: IA PROMPTS
created: 2023-06-19T18:59:52.661084Z
message_count: 6
attachments_count: 0
---

# Racionalismo e suas Sub-escolas

- Tema: `IA PROMPTS`
- Conversation ID: `edddb2df-c7cd-4778-81f6-c57a11a8071e`

## Transcrição

### user

Considerando a concepção de escolas de pensamento como o Racionalismo, por exemplo, fazer o diagrama das várias sub-escolas vinculadas a esse paradigma

### assistant

{
  "diagramGuidelines": "mermaid_mindmap"
}

### tool

{"diagramGuidelines":"\\nA mind map is a diagram used to visually organize information into a hierarchy, showing relationships among pieces of the whole. It is often created around a single concept, drawn as an image in the center of a blank page, to which associated representations of ideas such as images, words and parts of words are added. Major ideas are connected directly to the central concept, and other ideas branch out from those major ideas\\n\\nRules when using mindmap diagrams in mermaid syntax:\\n- Mermaid mindmaps can show nodes using different shapes. When specifying a shape for a node the syntax is similar to flowchart nodes, with an id followed by the shape definition and with the text within the shape delimiters. Where possible try to keep the same shapes as for flowcharts, even though they are not all supported from the start.\\n\\n- Mindmap can show the following shapes:\\n```\\nmindmap\\n    id[I am a square]\\n    id(I am a rounded square)\\n    id((I am a circle))\\n    id))I am a bang((\\n    id)I am a cloud(\\n    id{{I am a hexagon}}\\n    I am the default shape\\n``` \\n\\n- The \\"Markdown Strings\\" feature enhances mind maps by offering a more versatile string type, which supports text formatting options such as bold and italics, and automatically wraps text within labels.\\n```\\nmindmap\\n    id1[\\"`**Root** with\\na second line\\nUnicode works too: 🤓`\\"]\\n      id2[\\"`The dog in **the** hog... a *very long text* that wraps to a new line`\\"]\\n      id3[Regular labels still works]\\n``` \\n\\n- Formatting: For bold text, use double asterisks ** before and after the text. For italics, use single asterisks * before and after the text. With traditional strings, you needed to add tags for text to wrap in nodes. However, markdown strings automatically wrap text when it becomes too long and allows you to start a new line by simply using a newline character instead of a tag.\\n \\nExamples:\\nUser asks: \\"Show me a mindmap about a mindmap\\"\\n```\\nmindmap\\n  root((mindmap))\\n    Origins\\n      Long history\\n      Popularisation\\n        British popular psychology author Tony Buzan\\n    Research\\n      On effectiveness and features\\n      On Automatic creation\\n        Uses\\n            Creative techniques\\n            Strategic planning\\n            Argument mapping\\n    Tools\\n      Pen and paper\\n      Mermaid\\n```\\n","diagramThemes":"\\nmermaid themes:\\n```\\ndefault - This is the default theme for all diagrams.\\nneutral - This theme is great for black and white documents that will be printed.\\ndark - This theme goes well with dark-colored elements or dark-mode.\\nforest - This theme contains shades of green.\\nbase - This is the only theme that can be modified. Use this theme as the base for customizations.\\n```\\n\\nTo customize the theme of an individual diagram, use the init directive:\\n```\\n%%{init: {'theme':'forest'}}%%\\n```\\n  "}

### assistant

{
  "openApiSchemaVersion": "1.0",
  "diagramLanguage": "mermaid",
  "diagramType": "mindmap",
  "diagram": "mindmap\\n  Racionalismo\\n    Descartes\\n      Dualismo\\n      Cogito Ergo Sum\\n    Spinoza\\n      Monismo\\n      Ética\\n    Leibniz\\n      Monadologia\\n      Princípio da Razão Suficiente"
}

### tool

{"results":[{"image":"https://showme.redstarplugin.com/d/1hbS2Pzq","editDiagramOnline":"https://showme.redstarplugin.com/s/d7SUNUlX (can autofill: yes)","contributeToOpenSourceProject":"https://github.com/bra1nDump/show-me-chatgpt-plugin/issues"}]}

### assistant

Aqui está um diagrama de mente que representa as várias sub-escolas de pensamento vinculadas ao Racionalismo:

![Diagrama de Mente do Racionalismo](https://showme.redstarplugin.com/d/1hbS2Pzq)

Este diagrama mostra como o Racionalismo se ramifica em diferentes filósofos, como Descartes, Spinoza e Leibniz, cada um com suas próprias contribuições e conceitos únicos.

[Você pode visualizar este diagrama em uma nova aba.](https://showme.redstarplugin.com/d/1hbS2Pzq)

Se desejar fazer alterações, [você pode editar este diagrama online.](https://showme.redstarplugin.com/s/d7SUNUlX)

O tipo do diagrama é um mapa mental na linguagem Mermaid. Para melhorar o diagrama, você pode considerar adicionar mais detalhes sobre cada filósofo ou conceito, ou talvez explorar outras sub-escolas de pensamento dentro do Racionalismo.

Para explorar outros tipos de diagramas e linguagens, use a frase-chave "*explorar diagramas*".
