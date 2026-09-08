from google import genai
from app.config import get_env_meta_info
from app.services.llm.base import LLMProvider
from app.exceptions.exceptions import (
    LLMRateLimitException,
    LLMProviderException,
)

class GeminiProvider(LLMProvider):
    def __init__(self):
        env_meta_info = get_env_meta_info()
        self.client = genai.Client(
            api_key=env_meta_info.llm_api_key
        )
        self.model = env_meta_info.llm_model

    def generate(self, prompt: str) -> str:
        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt,
            )

            return response.text

        except Exception as exc:

            error_message = str(exc)

            if "429" in error_message or "RateLimit" in error_message:
                raise LLMRateLimitException(
                    "LLM rate limit exceeded."
                ) from exc

            raise LLMProviderException(
                "LLM provider request failed."
            ) from exc

