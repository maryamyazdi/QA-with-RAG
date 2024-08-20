RAG_prompt_template = """
You are a helpful AI assistant. Answer the QUESTION based on the CONTEXT retrieved from database.
You can use your own knowledge too, but make sure to use the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
"""
