import time

from app.services.llm.factory import get_llm_provider

provider = get_llm_provider()

prompt = """
Answer briefly.

Tell me about Batman and FastAPI
"""

start = time.perf_counter()

answer = provider.generate(prompt)

elapsed = time.perf_counter() - start

print(answer)
print(f"Gemini time: {elapsed:.2f}s")