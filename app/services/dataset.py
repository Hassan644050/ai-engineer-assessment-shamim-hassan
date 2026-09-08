from pathlib import Path

DATASET_PATH = Path(__file__).parent.parent / "data" / "dataset.txt"

STOP_WORDS = {
    "what",
    "is",
    "the",
    "a",
    "an",
    "are",
    "how",
    "why",
    "when",
    "where",
    "who",
    "tell",
    "me",
    "about",
}

def load_dataset() -> str:
    return DATASET_PATH.read_text(encoding="utf-8")

# def search_dataset(question: str) -> str:
#     dataset = load_dataset()
#     question_words = question.lower().split()
#     matching_lines = []

#     for line in dataset.splitlines():
#         line_lower = line.lower()

#         if any(word in line_lower for word in question_words):
#             matching_lines.append(line)

#     return "\n".join(matching_lines)

def search_dataset(question: str) -> str:
    dataset = load_dataset()

    question_words = {
        word.strip(".,?!").lower()
        for word in question.split()
        if word.strip(".,?!").lower() not in STOP_WORDS
    }

    # matching_lines = []

    # for line in dataset.splitlines():
    #     line_lower = line.lower()

    #     if any(word in line_lower for word in question_words):
    #         matching_lines.append(line)

    # return "\n".join(matching_lines)

    best_line = ""
    best_score = 0

    for line in dataset.splitlines():
        line_lower = line.lower()

        score = sum(
            1 for word in question_words
            if word in line_lower
        )

        if score > best_score:
            best_score = score
            best_line = line
    if best_score == 0:
        return "I couldn't find relevant information in the dataset."

    return best_line