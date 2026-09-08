# def build_prompt(question: str, context: str) -> str:
#     return f"""
# You are a helpful assistant.

# Answer the user's question using only the information provided in the context.

# User question:
# {question}

# Context:
# {context}

# Instructions:
# - Give a clear and concise answer.
# - Use only the information provided in the context.
# - Do not invent or assume facts that are not in the context.
# - If the context does not contain enough information to answer the question, say:
#   "I don't have enough information to answer that."
# - When information comes from multiple sources, combine it into one coherent answer.
# - Do not mention the internal source names unless necessary.
# """

def build_prompt(question: str, context: str) -> str:
    return f"""
Answer the question using only the context below.

Question:
{question}

Context:
{context}

If the context does not contain enough information, say:
"I don't have enough information to answer that."
"""