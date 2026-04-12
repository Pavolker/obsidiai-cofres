import os
import json
from sqlalchemy import create_engine, Column, String, Text, text
from sqlalchemy.orm import declarative_base, sessionmaker
from pgvector.sqlalchemy import Vector

# Exemplo de DATABASE_URL pro Railway: postgresql://postgres:password@host:port/railway
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/obsidiai")
# Ajeita URL de postgres se vier apenas postgres://
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id = Column(String, primary_key=True, index=True) # Pode ser um hash do vault+filepath+chunk_index
    vault = Column(String, index=True)
    filepath = Column(String, index=True)
    content = Column(Text)
    metadata_json = Column(Text) # Tags, links encontrados, etc
    embedding = Column(Vector(1536)) # Dimensionamento para text-embedding-3-small (OpenAI)

    @property
    def parsed_metadata(self):
        try:
            return json.loads(self.metadata_json) if self.metadata_json else {}
        except json.JSONDecodeError:
            return {}

def init_db():
    # Garante que a extensao pgvector existe
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        conn.commit()
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
