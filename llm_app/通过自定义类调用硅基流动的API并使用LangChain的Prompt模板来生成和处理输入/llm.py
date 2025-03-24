import os
import requests
from langchain.llms.base import LLM
from pydantic import BaseModel, Field

class SiliconFlow(LLM, BaseModel):
    api_key: str = os.getenv("API_KEY")  # 显式地从环境变量中读取
    base_url: str = "https://api.siliconflow.cn/v1/chat/completions"

    @property
    def _llm_type(self) -> str:
        return "siliconflow"

    def _call(self, prompt: str, stop: list = None, model: str = "default-model") -> str:
        if not self.api_key:
            raise ValueError("API_KEY environment variable is not set.")
        
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {self.api_key}"
        }

        response = requests.post(self.base_url, json=payload, headers=headers)
        response.raise_for_status()
        print(response.json())
        response_content = response.json()["choices"][0]["message"]["content"]

        if stop is not None:
            response_content = self.enforce_stop_tokens(response_content, stop)
        return response_content

    @staticmethod
    def enforce_stop_tokens(text: str, stop_tokens: list) -> str:
        for token in stop_tokens:
            if token in text:
                text = text[:text.index(token)]
        return text