---
source: DATAGPT
conversation_id: 68e64540-e374-832b-8de9-d0b30bd38885
title: "Lista de empresas JSON"
theme: NEGOCIOS
created: 2025-10-08T11:05:20.908305Z
message_count: 2
attachments_count: 0
---

# Lista de empresas JSON

- Tema: `NEGOCIOS`
- Conversation ID: `68e64540-e374-832b-8de9-d0b30bd38885`

## Transcrição

### user

Refaça esse código JASON, de modo que ele apresente apenas uma lista de 10 empresas: "{
  "type": "Card",
  "size": "lg",
  "confirm": {
    "action": {
      "type": "view.details"
    },
    "label": "View details"
  },
  "cancel": {
    "action": {
      "type": "close"
    },
    "label": "Close"
  },
  "children": [
    {
      "type": "Row",
      "children": [
        {
          "type": "Text",
          "value": "Company Name",
          "width": 150,
          "color": "tertiary",
          "size": "sm"
        },
        {
          "type": "Text",
          "value": "Apex Systems Inc.",
          "color": "secondary"
        }
      ]
    },
    {
      "type": "Divider",
      "flush": true
    },
    {
      "type": "Row",
      "children": [
        {
          "type": "Text",
          "value": "Industry",
          "width": 150,
          "weight": "semibold",
          "color": "tertiary",
          "size": "sm"
        },
        {
          "type": "Text",
          "value": "Information Technology Services",
          "color": "secondary"
        }
      ]
    },
    {
      "type": "Divider",
      "flush": true
    },
    {
      "type": "Row",
      "children": [
        {
          "type": "Text",
          "value": "Headquarters",
          "width": 150,
          "weight": "semibold",
          "color": "tertiary",
          "size": "sm"
        },
        {
          "type": "Text",
          "value": "Austin, Texas, United States",
          "color": "secondary"
        }
      ]
    },
    {
      "type": "Divider",
      "flush": true
    },
    {
      "type": "Row",
      "children": [
        {
          "type": "Text",
          "value": "Company Size",
          "width": 150,
          "weight": "semibold",
          "color": "tertiary",
          "size": "sm"
        },
        {
          "type": "Text",
          "value": "1,000–5,000 employees",
          "color": "secondary"
        }
      ]
    },
    {
      "type": "Divider",
      "flush": true
    },
    {
      "type": "Row",
      "children": [
        {
          "type": "Text",
          "value": "Website",
          "width": 150,
          "weight": "semibold",
          "color": "tertiary",
          "size": "sm"
        },
        {
          "type": "Button",
          "label": "Company website",
          "style": "primary"
        }
      ]
    },
    {
      "type": "Divider",
      "flush": true
    },
    {
      "type": "Row",
      "children": [
        {
          "type": "Text",
          "value": "Founded Year",
          "width": 150,
          "weight": "semibold",
          "color": "tertiary",
          "size": "sm"
        },
        {
          "type": "Text",
          "value": "1995",
          "color": "secondary"
        }
      ]
    },
    {
      "type": "Divider",
      "flush": true
    },
    {
      "type": "Row",
      "children": [
        {
          "type": "Text",
          "value": "Description",
          "width": 150,
          "weight": "semibold",
          "color": "tertiary",
          "size": "sm"
        },
        {
          "type": "Text",
          "value": "Apex Systems is a leading provider of technology services, specializing in IT staffing, consulting, and workforce management solutions across multiple industries. The company partners with organizations to deliver end-to-end solutions in digital transformation, software development, and enterprise IT modernization.",
          "color": "secondary"
        }
      ]
    }
  ]
} "

### assistant

Aqui está a versão simplificada do JSON, ajustada para apresentar **apenas uma lista de 10 empresas**, sem os outros detalhes (indústria, sede, etc.). Cada empresa aparece como um item de linha (`Row`) com nome e separador (`Divider`):

```json
{
  "type": "Card",
  "size": "lg",
  "children": [
    {
      "type": "Row",
      "children": [
        { "type": "Text", "value": "1. Apex Systems Inc.", "color": "secondary" }
      ]
    },
    { "type": "Divider", "flush": true },
    {
      "type": "Row",
      "children": [
        { "type": "Text", "value": "2. GlobalTech Solutions", "color": "secondary" }
      ]
    },
    { "type": "Divider", "flush": true },
    {
      "type": "Row",
      "children": [
        { "type": "Text", "value": "3. Horizon Analytics", "color": "secondary" }
      ]
    },
    { "type": "Divider", "flush": true },
    {
      "type": "Row",
      "children": [
        { "type": "Text", "value": "4. NovaSoft Digital", "color": "secondary" }
      ]
    },
    { "type": "Divider", "flush": true },
    {
      "type": "Row",
      "children": [
        { "type": "Text", "value": "5. Vertex Consulting", "color": "secondary" }
      ]
    },
    { "type": "Divider", "flush": true },
    {
      "type": "Row",
      "children": [
        { "type": "Text", "value": "6. Quantum Enterprises", "color": "secondary" }
      ]
    },
    { "type": "Divider", "flush": true },
    {
      "type": "Row",
      "children": [
        { "type": "Text", "value": "7. Orion Manufacturing", "color": "secondary" }
      ]
    },
    { "type": "Divider", "flush": true },
    {
      "type": "Row",
      "children": [
        { "type": "Text", "value": "8. Zenith Capital Group", "color": "secondary" }
      ]
    },
    { "type": "Divider", "flush": true },
    {
      "type": "Row",
      "children": [
        { "type": "Text", "value": "9. Polaris Media House", "color": "secondary" }
      ]
    },
    { "type": "Divider", "flush": true },
    {
      "type": "Row",
      "children": [
        { "type": "Text", "value": "10. Atlas Innovations", "color": "secondary" }
      ]
    }
  ]
}
```

Esse formato mantém apenas os nomes das empresas em uma lista simples e numerada.  

Quer que eu mantenha botões de ação (como "View details" ou "Website") para cada empresa ou prefere que seja apenas uma lista estática de nomes?
