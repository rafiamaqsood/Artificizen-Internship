import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from config import GROQ_API_KEY

print(GROQ_API_KEY)