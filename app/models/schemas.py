
from enum import Enum

class QuestionSource(str, Enum):
    SUPERHERO = "superhero"
    DATASET = "dataset"
    BOTH = "both"

class EnvMetaInfo:
    def __init__(self,super_hero_api_token,llm_api_key,llm_model,llm_provider):
        self.super_hero_api_token=super_hero_api_token
        self.llm_api_key=llm_api_key
        self.llm_model=llm_model
        self.llm_provider=llm_provider