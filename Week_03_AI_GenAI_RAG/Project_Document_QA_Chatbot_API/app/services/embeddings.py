from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL
model = SentenceTransformer(EMBEDDING_MODEL)

def embed_text(text):
    embeddings = model.encode(text)
    return embeddings