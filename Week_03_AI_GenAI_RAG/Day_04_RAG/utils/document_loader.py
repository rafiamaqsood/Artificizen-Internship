from pathlib import Path
import sys
CURRENT_FILE = Path(__file__).resolve()
sys.path.append(str(CURRENT_FILE.parents[2]))
import pymupdf4llm
from utils.chunking import chunk_text
from Day_03_Embeddings_Semantic_Search.question_6.utility_function import embed_and_store


def prepare_document(pdf):
    text = pymupdf4llm.to_markdown(str(pdf))
    chunks = chunk_text(text)
    metadata = [
        {
            "source": pdf.name,
            "chunk_index": i
        }
        for i in range(len(chunks))
    ]
    embed_and_store(
        texts=chunks,
        metadata_list=metadata,
        collection_name="chunks"
    )