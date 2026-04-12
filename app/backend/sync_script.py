import os
import re
import json
import hashlib
from dotenv import load_dotenv
from openai import OpenAI
from sqlalchemy.orm import Session
from database import SessionLocal, DocumentChunk, init_db

load_dotenv()

openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Regex para achar [[links]] e #tags
WIKI_LINK_PATTERN = re.compile(r"\[\[(.*?)\]\]")
TAG_PATTERN = re.compile(r"(?<!#)#([a-zA-Z0-9_\-]+)")

def parse_markdown_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    links = WIKI_LINK_PATTERN.findall(content)
    tags = TAG_PATTERN.findall(content)

    return content, {"links": list(set(links)), "tags": list(set(tags))}

def get_embedding(text):
    if not text.strip():
        return None
    try:
        response = openai_client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"Erro ao gerar embedding: {e}")
        return None

def chunk_text(text, max_chars=1000, overlap=100):
    chunks = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = min(start + max_chars, text_len)
        # Tenta não quebrar no meio de uma palavra (busca ultimo espaco)
        if end < text_len:
            last_space = text.rfind(' ', start, end)
            if last_space != -1 and last_space > start + max_chars/2:
                 end = last_space
        chunks.append(text[start:end])
        start = end - overlap
        if start < 0:
            start = 0
        if end >= text_len:
            break
    return chunks

def sync_vaults(root_dir):
    print("Iniciando sincronização...")
    db: Session = SessionLocal()
    
    # Limpa dados antigos da sincronização anterior caso queira "recriar"
    # db.query(DocumentChunk).delete() 
    # db.commit()

    exclude_dirs = {'.git', 'app', 'second-brain', 'OPENAI', 'DATAGPT'} # Ignorando arquivos pesados de raw chat
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Filtra diretórios
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs and not d.startswith('.')]
        
        vault_name = os.path.basename(dirpath)
        if dirpath == root_dir:
             vault_name = "ROOT"

        for filename in filenames:
            if filename.endswith(".md"):
                filepath = os.path.join(dirpath, filename)
                rel_path = os.path.relpath(filepath, root_dir)
                
                print(f"Processando: {rel_path}...")
                content, metadata = parse_markdown_file(filepath)
                
                # Vamos simplificar e inserir o documento como 1 unico chunk se for pequeno,
                # e multiplos chunks se for grande.
                chunks = chunk_text(content)
                for idx, chunk_text_content in enumerate(chunks):
                    # O id precisa ser unico, hasheando o caminho + index
                    string_id = f"{rel_path}_{idx}".encode('utf-8')
                    chunk_id = hashlib.md5(string_id).hexdigest()
                    
                    # Verifica se já existe para nao processar atoa, senao processa
                    existing = db.query(DocumentChunk).filter(DocumentChunk.id == chunk_id).first()
                    if existing:
                        continue # Pula se ja processou antes e nada mudou. Futuramente adicionar check de data.

                    embedding = get_embedding(chunk_text_content)
                    if embedding:
                         doc_chunk = DocumentChunk(
                             id=chunk_id,
                             vault=vault_name,
                             filepath=rel_path,
                             content=chunk_text_content,
                             metadata_json=json.dumps(metadata),
                             embedding=embedding
                         )
                         db.add(doc_chunk)
                         db.commit()

    print("Sincronização concluída!")

if __name__ == "__main__":
    init_db()
    # Pega diretório acima da pasta app/backend
    root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    sync_vaults(root_directory)
