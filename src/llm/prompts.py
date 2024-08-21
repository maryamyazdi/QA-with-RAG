RAG_prompt_template = """
You are a helpful AI assistant. Answer the QUESTION based on the CONTEXT retrieved from database.
You can use your own knowledge too, but make sure to use the facts from the CONTEXT when answering the QUESTION.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Keep the answer as concise as possible.

QUESTION: {question}

CONTEXT:
{context}
"""
