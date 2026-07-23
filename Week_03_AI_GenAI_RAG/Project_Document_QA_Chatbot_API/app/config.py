from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
MODEL_NAME = os.getenv("MODEL_NAME")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")