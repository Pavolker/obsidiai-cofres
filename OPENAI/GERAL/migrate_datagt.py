#!/usr/bin/env python3
import csv
import json
import os
import re
import shutil
import subprocess
from collections import defaultdict
from datetime import datetime
from pathlib import Path


SRC = Path("/Users/pvolkermini/APLICATIVO-MINI/OBSIDIAN/DATAGPT")
DST = Path("/Users/pvolkermini/APLICATIVO-MINI/OBSIDIAN/OPENAI")

THEMES = [
    "01_IA_prompts_automacao",
    "02_Tecnologia_apps_desenvolvimento",
    "03_Negocios_estrategia_empreendedorismo",
    "04_Dados_estatistica_indicadores",
    "05_Setores_produtivos_cadeias_circularidade",
    "06_Filosofia_humanidades_pensamento",
    "07_Linguagem_etimologia_texto",
    "08_Educacao_aprendizagem",
    "09_Arte_literatura_musica_mitologia",
    "10_Saude_corpo_emocao_morte",
    "11_Geografia_territorio_economia_regional",
    "12_Pessoas_familias_genealogia",
    "13_Design_imagem_apresentacoes",
    "14_Documentos_relatorios_arquivos",
    "15_Rascunhos_genricos",
]

GENERIC_TITLES = {
    "new chat",
    "saudacao inicial",
    "nada",
    "antes de mais nada",
    "data carregamento conversa",
}

RULES = [
    (
        "01_IA_prompts_automacao",
        [
            r"\bia\b",
            r"\bgpt\b",
            r"\bopenai\b",
            r"prompt",
            r"\bagente\b",
            r"flowise",
            r"\bn8n\b",
            r"chatgpt",
            r"\bapi\b",
            r"deepseek",
            r"github spark",
            r"turing test",
            r"modelo",
        ],
    ),
    (
        "02_Tecnologia_apps_desenvolvimento",
        [
            r"\bapp\b",
            r"aplicativo",
            r"\bsite\b",
            r"desenvolvimento",
            r"software",
            r"github",
            r"codespaces",
            r"netlify",
            r"webhook",
            r"resend",
            r"firebase",
            r"frontend",
            r"backend",
            r"interface",
            r"ux",
            r"ui",
            r"erro",
        ],
    ),
    (
        "04_Dados_estatistica_indicadores",
        [
            r"estatistic",
            r"planilha",
            r"\bcsv\b",
            r"\bexcel\b",
            r"dados",
            r"indicador",
            r"amostragem",
            r"correlacao",
            r"calculo",
            r"indice",
            r"matriz",
            r"graf(ic|i)co",
            r"benchmarking",
            r"despesa",
        ],
    ),
    (
        "03_Negocios_estrategia_empreendedorismo",
        [
            r"empresa",
            r"empreendedor",
            r"estrateg",
            r"mercado",
            r"competitiv",
            r"governanc",
            r"consultor",
            r"negocio",
            r"projeto",
            r"financiamento",
            r"editais",
            r"branding",
            r"conselho empresarial",
        ],
    ),
    (
        "05_Setores_produtivos_cadeias_circularidade",
        [
            r"cadeia",
            r"circular",
            r"construcao civil",
            r"madeira",
            r"moveis",
            r"moda",
            r"nautic",
            r"agroind",
            r"apicultur",
            r"\babelha\b",
            r"\bmel\b",
            r"biogas",
            r"solar",
            r"cosmetic",
            r"caf[eé]",
            r"\bleite\b",
            r"industri",
            r"\bcnae\b",
            r"frigorif",
            r"sucro",
            r"mandioca",
            r"produto",
            r"circularidade",
        ],
    ),
    (
        "08_Educacao_aprendizagem",
        [
            r"\bescola\b",
            r"\bbncc\b",
            r"atividade",
            r"ensino",
            r"aprendiz",
            r"educa",
            r"sala de aula",
            r"competencias?",
            r"formacao",
            r"curso",
            r"aula",
        ],
    ),
    (
        "09_Arte_literatura_musica_mitologia",
        [
            r"musica",
            r"\blivro\b",
            r"\bconto\b",
            r"poesia",
            r"romance",
            r"mitolog",
            r"flauta magica",
            r"mozart",
            r"shakespeare",
            r"gabo",
            r"banquete",
            r"iliada",
            r"odisseia",
            r"sinfonia",
            r"literatura",
            r"epigrafe",
        ],
    ),
    (
        "06_Filosofia_humanidades_pensamento",
        [
            r"filosof",
            r"platao",
            r"caverna",
            r"alegoria",
            r"espinosa",
            r"freud",
            r"bachelard",
            r"castoriad",
            r"heraclito",
            r"socrat",
            r"aristot",
            r"metafis",
            r"ontolog",
            r"epistem",
            r"humanidade",
            r"\bmorte\b",
            r"\bvida\b",
            r"alma",
            r"paideia",
            r"sabedoria",
            r"pensamento",
        ],
    ),
    (
        "07_Linguagem_etimologia_texto",
        [
            r"pergunta",
            r"etimolog",
            r"palavras?",
            r"definicao",
            r"significado",
            r"dicionario",
            r"traduca",
            r"idioma",
            r"\btexto\b",
            r"lingu",
            r"n-grams",
            r"discurso",
            r"resumo",
            r"fonte texto",
            r"questao",
        ],
    ),
    (
        "10_Saude_corpo_emocao_morte",
        [
            r"saude",
            r"medic",
            r"angioedema",
            r"corpo humano",
            r"emocao",
            r"\bmedo\b",
            r"cancer",
            r"farmacia",
            r"farmac",
            r"bem-estar",
            r"psicolog",
        ],
    ),
    (
        "11_Geografia_territorio_economia_regional",
        [
            r"\bbrasil\b",
            r"parana",
            r"apucarana",
            r"municip",
            r"cidade",
            r"bairro",
            r"territor",
            r"regiao",
            r"exporta",
            r"global",
            r"mundo",
            r"pais",
            r"geograf",
        ],
    ),
    (
        "12_Pessoas_familias_genealogia",
        [
            r"genealog",
            r"familia",
            r"heranca",
            r"\bpessoa\b",
            r"familiar",
            r"stockler",
            r"luiza",
            r"helena",
            r"jvolker",
            r"quadro familia",
        ],
    ),
    (
        "13_Design_imagem_apresentacoes",
        [
            r"imagem",
            r"\bslide\b",
            r"apresenta",
            r"diagrama",
            r"mapa mental",
            r"capa",
            r"logo",
            r"carrossel",
            r"flyer",
            r"visual",
            r"infograf",
            r"arte\b",
        ],
    ),
    (
        "14_Documentos_relatorios_arquivos",
        [
            r"\bpdf\b",
            r"\bdocx\b",
            r"documento",
            r"relatorio",
            r"arquivo",
            r"leitura de pdf",
            r"report",
            r"resposta a notifica",
            r"artigo",
        ],
    ),
]


def normalize(text: str) -> str:
    import unicodedata

    text = text.lower()
    text = unicodedata.normalize("NFD", text)
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")
    return text


def slugify(text: str, max_len: int = 80) -> str:
    text = normalize(text)
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    text = re.sub(r"-{2,}", "-", text)
    if not text:
        text = "sem-titulo"
    return text[:max_len].strip("-")


def parse_conversation_messages(conversation: dict):
    mapping = conversation.get("mapping", {})
    current = conversation.get("current_node")
    messages = []
    while current:
        node = mapping.get(current)
        if not node:
            break
        msg = node.get("message") or {}
        content = msg.get("content") or {}
        parts = content.get("parts") or []
        text_parts = [p for p in parts if isinstance(p, str) and p.strip()]
        if msg.get("author", {}).get("role") and text_parts:
            messages.append(
                {
                    "role": msg["author"]["role"],
                    "text": "\n".join(text_parts).strip(),
                }
            )
        current = node.get("parent")
    messages.reverse()
    return messages


def classification_text(title: str, messages) -> str:
    snippets = [title]
    user_count = 0
    for msg in messages:
        snippets.append(msg["text"])
        if msg["role"] == "user":
            user_count += 1
            if user_count >= 2:
                break
    return normalize(" ".join(snippets))


def is_generic_title(title: str) -> bool:
    return normalize(title).strip() in GENERIC_TITLES


def classify_text(text: str, fallback: str = "15_Rascunhos_genricos") -> str:
    if text.strip() in GENERIC_TITLES:
        return fallback
    for theme, patterns in RULES:
        if any(re.search(pattern, text) for pattern in patterns):
            return theme
    return fallback


def conversation_theme(conversation: dict) -> str:
    title = (conversation.get("title") or "").strip()
    messages = parse_conversation_messages(conversation)
    title_norm = normalize(title)
    if not is_generic_title(title):
        title_theme = classify_text(title_norm, fallback="")
        if title_theme and title_theme != "15_Rascunhos_genricos":
            return title_theme
    body_text = classification_text("", messages)
    return classify_text(body_text)


def extract_docx_text(docx_path: Path) -> str:
    try:
        result = subprocess.run(
            ["textutil", "-convert", "txt", "-stdout", str(docx_path)],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except Exception:
        return ""


def csv_preview(csv_path: Path, limit: int = 20) -> str:
    with csv_path.open("r", encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        return "(arquivo CSV vazio)"
    headers = rows[0]
    sample = rows[1 : 1 + limit]
    lines = []
    lines.append(f"Linhas: {max(len(rows) - 1, 0)}")
    lines.append("")
    lines.append("Cabeçalhos:")
    for h in headers:
        lines.append(f"- {h}")
    lines.append("")
    lines.append("Amostra:")
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")
    for row in sample:
        row = row + [""] * (len(headers) - len(row))
        lines.append("| " + " | ".join(cell.replace("|", "\\|") for cell in row[: len(headers)]) + " |")
    return "\n".join(lines)


def markdown_escape(text: str) -> str:
    return text.replace("\\", "\\\\")


def conversation_markdown(conversation: dict) -> str:
    title = (conversation.get("title") or "Sem título").strip()
    messages = parse_conversation_messages(conversation)
    theme = conversation_theme(conversation)
    created = conversation.get("create_time")
    created_iso = ""
    if isinstance(created, (int, float)):
        created_iso = datetime.utcfromtimestamp(created).isoformat() + "Z"
    attachments = set()
    for node in (conversation.get("mapping") or {}).values():
        files = node.get("files") or []
        for f in files:
            attachments.add(f)
    frontmatter = [
        "---",
        "source: DATAGPT",
        f"conversation_id: {conversation.get('conversation_id', '')}",
        f"title: {json.dumps(title, ensure_ascii=False)}",
        f"theme: {theme}",
        f"created: {created_iso}",
        f"message_count: {len(messages)}",
        f"attachments_count: {len(attachments)}",
        "---",
        "",
        f"# {title}",
        "",
        f"- Tema: `{theme}`",
        f"- Conversation ID: `{conversation.get('conversation_id', '')}`",
        "",
    ]
    if attachments:
        frontmatter += ["## Anexos", ""]
        for a in sorted(attachments):
            frontmatter.append(f"- `{a}`")
        frontmatter.append("")
    frontmatter.append("## Transcrição")
    frontmatter.append("")
    for msg in messages:
        role = msg["role"]
        text = markdown_escape(msg["text"])
        frontmatter.append(f"### {role}")
        frontmatter.append("")
        frontmatter.append(text)
        frontmatter.append("")
    return "\n".join(frontmatter).rstrip() + "\n"


def write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def copy_file(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def file_theme(path: Path, content_hint: str = "") -> str:
    title_theme = classify_text(normalize(path.name), fallback="")
    if title_theme and title_theme != "15_Rascunhos_genricos":
        return title_theme
    text = normalize(path.name + " " + content_hint)
    return classify_text(text)


def ensure_theme_dirs():
    for theme in THEMES:
        (DST / theme / "conversas").mkdir(parents=True, exist_ok=True)
        (DST / theme / "arquivos").mkdir(parents=True, exist_ok=True)


def load_conversations():
    conversations = []
    for path in sorted(SRC.glob("conversations-*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for conv in data:
            conv["_source_file"] = path.name
            conversations.append(conv)
    return conversations


def existing_note_index():
    return {}


def generate_theme_index(theme: str, conversation_paths, file_paths):
    lines = [
        f"# {theme}",
        "",
        f"- Conversas: {len(conversation_paths)}",
        f"- Arquivos: {len(file_paths)}",
        "",
        "## Conversas",
        "",
    ]
    for p in sorted(conversation_paths):
        rel = p.relative_to(DST)
        lines.append(f"- [{p.stem}]({rel.as_posix()})")
    lines.extend(["", "## Arquivos", ""])
    for p in sorted(file_paths):
        rel = p.relative_to(DST)
        lines.append(f"- [{p.name}]({rel.as_posix()})")
    lines.append("")
    write_text(DST / theme / "index.md", "\n".join(lines))


def update_root_index(theme_counts):
    lines = [
        "# OPENAI Vault",
        "",
        "Cofre temático migrado a partir de `DATAGPT`.",
        "",
        "## Temas",
        "",
    ]
    for theme in THEMES:
        count = theme_counts.get(theme, {"conversations": 0, "files": 0})
        lines.append(
            f"- [{theme}]({theme}/index.md): {count['conversations']} conversas, {count['files']} arquivos"
        )
    lines.append("")
    write_text(DST / "00_INDEX.md", "\n".join(lines))


def main():
    ensure_theme_dirs()
    theme_conversation_paths = defaultdict(list)
    theme_file_paths = defaultdict(list)
    theme_counts = defaultdict(lambda: {"conversations": 0, "files": 0})

    # Migrate conversations into markdown notes.
    for conv in load_conversations():
        theme = conversation_theme(conv)
        title = (conv.get("title") or "Sem título").strip()
        filename = f"{slugify(title)}__{conv.get('conversation_id','')[:8]}.md"
        out = DST / theme / "conversas" / filename
        write_text(out, conversation_markdown(conv))
        theme_conversation_paths[theme].append(out)
        theme_counts[theme]["conversations"] += 1

    # Migrate text/data files.
    for src in sorted(SRC.iterdir()):
        if src.is_dir():
            continue
        if re.match(r"^conversations-\d+\.json$", src.name):
            continue
        if src.name in {"chat.html", "export_manifest.json", "shared_conversations.json", "user_settings.json", "user.json"}:
            continue

        suffix = src.suffix.lower()
        if suffix == ".md":
            content = src.read_text(encoding="utf-8", errors="replace")
            theme = file_theme(src, content[:1500])
            dst = DST / theme / "arquivos" / src.name
            copy_file(src, dst)
            theme_file_paths[theme].append(dst)
            theme_counts[theme]["files"] += 1
        elif suffix == ".docx":
            text = extract_docx_text(src)
            theme = file_theme(src, text[:1500])
            raw_dst = DST / theme / "arquivos" / src.name
            copy_file(src, raw_dst)
            theme_file_paths[theme].append(raw_dst)
            theme_counts[theme]["files"] += 1

            md_name = f"{slugify(src.stem)}__extracto.md"
            md_dst = DST / theme / "arquivos" / md_name
            body = [
                "---",
                "source: DATAGPT",
                f"original_file: {src.name}",
                f"theme: {theme}",
                "---",
                "",
                f"# {src.stem}",
                "",
                text if text else "(texto nao extraido)",
                "",
            ]
            write_text(md_dst, "\n".join(body))
            theme_file_paths[theme].append(md_dst)
            theme_counts[theme]["files"] += 1
        elif suffix == ".csv":
            content = src.read_text(encoding="utf-8", errors="replace")
            theme = file_theme(src, content[:1000])
            raw_dst = DST / theme / "arquivos" / src.name
            copy_file(src, raw_dst)
            theme_file_paths[theme].append(raw_dst)
            theme_counts[theme]["files"] += 1

            preview = csv_preview(src)
            md_name = f"{slugify(src.stem)}__csv.md"
            md_dst = DST / theme / "arquivos" / md_name
            body = [
                "---",
                "source: DATAGPT",
                f"original_file: {src.name}",
                f"theme: {theme}",
                "---",
                "",
                f"# {src.stem}",
                "",
                preview,
                "",
            ]
            write_text(md_dst, "\n".join(body))
            theme_file_paths[theme].append(md_dst)
            theme_counts[theme]["files"] += 1
        else:
            # Ignore media exports for now; the user asked specifically for thematic organization.
            continue

    for theme in THEMES:
        generate_theme_index(theme, theme_conversation_paths[theme], theme_file_paths[theme])

    update_root_index(theme_counts)

    print(json.dumps(
        {
            "conversations": sum(v["conversations"] for v in theme_counts.values()),
            "files": sum(v["files"] for v in theme_counts.values()),
            "themes": {k: v for k, v in theme_counts.items()},
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
