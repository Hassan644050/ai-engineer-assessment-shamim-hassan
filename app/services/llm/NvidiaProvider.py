from openai import OpenAI

from app.config import get_env_meta_info
from app.services.llm.base import LLMProvider

class NvidiaProvider(LLMProvider):

    def __init__(self):
        env = get_env_meta_info()

        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=env.llm_api_key
        )

        self.model = env.llm_model

    def generate(self, prompt: str) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=1024,
            extra_body={
                "chat_template_kwargs": {
                    "enable_thinking": False
                }
            }
        )

        return response.choices[0].message.content