import os
from dotenv import load_dotenv
from app.models.schemas import EnvMetaInfo




def get_env_meta_info():
    load_dotenv()
    super_hero_api_token=os.getenv("SUPERHERO_API_TOKEN")
    llm_api_key=os.getenv("LLM_API_KEY")

    env_meta_info=EnvMetaInfo(super_hero_api_token=super_hero_api_token,llm_api_key=llm_api_key)
    return env_meta_info
