from app.config import get_env_meta_info
from app.services.llm.base import LLMProvider
from app.services.llm.gemini import GeminiProvider
from app.services.llm.NvidiaProvider import NvidiaProvider


_llm_provider: LLMProvider | None = None

def get_llm_provider() -> LLMProvider:
    global _llm_provider

    if _llm_provider is None:
        env_meta_info = get_env_meta_info()

        if env_meta_info.llm_provider == "gemini":
            _llm_provider = GeminiProvider()
        elif env_meta_info.llm_provider == "nvidia":
            _llm_provider = NvidiaProvider()
        else:
            raise ValueError(
                f"Unsupported LLM provider: {env_meta_info.llm_provider}"
            )

    return _llm_provider