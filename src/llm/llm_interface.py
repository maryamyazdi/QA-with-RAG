from http.client import responses
from typing import List

from openai import OpenAI
from src.llm.prompts import RAG_prompt_template


class LLMInterface:
    def __init__(self):
        self.client = OpenAI(
            base_url="http://localhost:11434/v1/",
            api_key="ollama",
        )

    def query(
        self,
        retrieved_responses: List[str],
        user_query: str,
        llm_name: str = "gemma:2b",
        system_role: str = "You are a helpful assistant.",
        temperature: int = 0,
    ) -> str:
        prompt = RAG_prompt_template.format(
            question=user_query, context=retrieved_responses
        )
        messages = [
            {"role": "system", "content": system_role},
            {"role": "user", "content": prompt},
        ]
        try:
            completion = self.client.chat.completions.create(
                model=llm_name, messages=messages, temperature=temperature
            )
            response = completion.choices[0].message["content"]
        except Exception as e:
            print(f"OpenAI error:{e}")
            response = "API call got an error."

        return response
