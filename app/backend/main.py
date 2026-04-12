import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from pydantic import BaseModel
from openai import OpenAI
from typing import List, Optional

from database import get_db, DocumentChunk

app = FastAPI(title="Obsidiai-Cofres API")

# Setup CORS para o frontend no netlify poder conversar com a porta
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Trocar pro do Netlify quando fazer deploy
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai_client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY"),
)

class SearchQuery(BaseModel):
    query: str
    limit: int = 5
    vault: Optional[str] = None

class ChatQuery(BaseModel):
    messages: List[dict] # [{role: "user", content: "..."}, ...]

def get_embedding(text_str):
    try:
        response = openai_client.embeddings.create(
            input=text_str,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
    except Exception as e:
         raise HTTPException(status_code=500, detail="Erro no provedor de Embeddings AI")

@app.get("/")
def read_root():
    return {"status": "ok", "app": "Obsidiai Backend"}

@app.get("/api/stats")
def get_stats(db: Session = Depends(get_db)):
    total_chunks = db.query(DocumentChunk).count()
    return {"total_chunks": total_chunks}

@app.post("/api/search")
def search_notes(payload: SearchQuery, db: Session = Depends(get_db)):
    """Busca vetorial de notas"""
    query_emb = get_embedding(payload.query)
    
    # Busca com pgvector (usando L2 distance <->)
    query = db.query(DocumentChunk).order_by(DocumentChunk.embedding.l2_distance(query_emb))
    if payload.vault:
        query = query.filter(DocumentChunk.vault == payload.vault)
        
    results = query.limit(payload.limit).all()
    
    return {
        "results": [
            {
                "id": r.id, 
                "filepath": r.filepath, 
                "vault": r.vault,
                "content": r.content,
                "metadata": r.parsed_metadata,
                "distance": 0 # pgvector suporta extrair distancia mas simplificaremos pro MVP
            }
            for r in results
        ]
    }

@app.post("/api/chat")
def chat(payload: ChatQuery, db: Session = Depends(get_db)):
    """Endpoint simplificado para Chat/RAG"""
    # 1. Pega a ultima mensagem do usuario
    user_msgs = [m for m in payload.messages if m.get("role") == "user"]
    if not user_msgs:
        raise HTTPException(status_code=400, detail="Sem mensagens de usuario.")
        
    last_query = user_msgs[-1]["content"]
    
    # 2. Busca conteudo relevante
    query_emb = get_embedding(last_query)
    docs = db.query(DocumentChunk).order_by(DocumentChunk.embedding.l2_distance(query_emb)).limit(3).all()
    
    context = "\n\n---\n\n".join([f"Path: {d.filepath}\nContent:\n{d.content}" for d in docs])
    
    # 3. Chama AI para gerar resposta baseada no contexto
    system_prompt = (
        "Você é o assistente inteligente do 'Obsidiai-Cofres', um segundo cérebro. "
        "Responda ao usuário utilizando o contexto a seguir que foi recuperado de suas anotações pessoais. "
        "Não invente respostas se não estiver no contexto.\n\n"
        f"CONTEXTO RECUPERADO:\n{context}"
    )
    
    messages = [{"role": "system", "content": system_prompt}] + payload.messages
    
    response = openrouter_client.chat.completions.create(
        model="anthropic/claude-3-haiku",  # Modelo padrão via OpenRouter, pode ajustar depois.
        messages=messages
    )
    
    return {"reply": response.choices[0].message.content, "sources": [d.filepath for d in docs]}
