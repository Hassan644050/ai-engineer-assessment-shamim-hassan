
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