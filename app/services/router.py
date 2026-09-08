from app.models.schemas import QuestionSource

SUPERHERO_NAMES = [
    "batman",
    "superman",
    "spider-man",
    "spiderman",
    "iron man",
    "hulk",
    "thor",
    "captain america",
    "wonder woman",
]

DATASET_KEYWORDS = [
    "fastapi",
    "pydantic",
    "uvicorn",
    "python",
    "rest api",
    "docker",
    "etl",
    "data engineering",
    "snowflake",
    "airflow",
]

def is_superhero_question(question: str) -> bool:
    question_lower = question.lower()

    return any(
        superhero in question_lower
        for superhero in SUPERHERO_NAMES
    )

def extract_superhero_name(question: str) -> str | None:
    question_lower = question.lower()

    for superhero in SUPERHERO_NAMES:
        if superhero in question_lower:
            return superhero

    return None

def determine_source(question: str) -> QuestionSource:
    superhero = is_superhero_question(question)

    question_lower = question.lower()

    dataset = any(
        keyword in question_lower
        for keyword in DATASET_KEYWORDS
    )

    if superhero and dataset:
        return QuestionSource.BOTH

    if superhero:
        return QuestionSource.SUPERHERO

    return QuestionSource.DATASET