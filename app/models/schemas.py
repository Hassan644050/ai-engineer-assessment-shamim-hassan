
from enum import Enum

class QuestionSource(str, Enum):
    SUPERHERO = "superhero"
    DATASET = "dataset"
    BOTH = "both"

class EnvMetaInfo:
    def __init__(self,super_hero_api_token,llm_api_key):
        self.super_hero_api_token=super_hero_api_token
        self.llm_api_key=llm_api_key