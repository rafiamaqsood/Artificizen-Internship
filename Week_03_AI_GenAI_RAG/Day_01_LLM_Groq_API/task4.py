import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from wrapper_function import ask

response = ask("Explain what is Transformer")
print(response)