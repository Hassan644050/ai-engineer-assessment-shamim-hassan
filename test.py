
# #Get provider class name
# from app.services.llm.factory import get_llm_provider
# provider = get_llm_provider()
# print(type(provider).__name__)

# from app.services.llm.gemini import GeminiProvider

# provider = GeminiProvider()
# answer = provider.generate("Explain FastAPI in one sentence.")
# print(answer)

from app.services.llm.factory import get_llm_provider

llm = get_llm_provider()

prompt = """
Answer the user's question using the provided information.

User question:
Tell me about Batman and FastAPI

Available information:
Superhero information:
Batman (Bruce Wayne) is a good superhero. Powerstats: intelligence=100, strength=26, speed=27.

Dataset information:
FastAPI is a modern Python web framework used for building APIs. It is based on Python type hints and provides automatic API documentation through OpenAPI.

Instructions:
- Answer clearly and concisely.
- Use only the provided information.
- Do not invent facts.
- If the information is insufficient, say so.
"""

answer = llm.generate(prompt)

print("===== GEMINI RESPONSE =====")
print(answer)