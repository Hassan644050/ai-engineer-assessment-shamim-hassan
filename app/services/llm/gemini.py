from google import genai
from app.config import get_env_meta_info
from app.services.llm.base import LLMProvider

class GeminiProvider(LLMProvider):
    def __init__(self):
        env_meta_info = get_env_meta_info()
        self.client = genai.Client(
            api_key=env_meta_info.llm_api_key
        )
        self.model = env_meta_info.llm_model

    def generate(self, prompt: str) -> str:
        response = self.client.interactions.create(
            model=self.model,
            input=prompt,
            generation_config={
                "thinking_level": "minimal"
            }
        )

        return response.output_text 

