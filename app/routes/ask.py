from fastapi import APIRouter
from app.services.llm.factory import get_llm_provider
from app.services.llm.prompt import build_prompt
from app.services.superhero import search_superhero,format_superhero_response
from app.models.ask import AskRequest, AskResponse
from app.models.schemas import QuestionSource
from app.services.router import (
    determine_source,
    extract_superhero_name,
)
from app.services.dataset import search_dataset
from app.exceptions.exceptions import LLMException
import time

router = APIRouter()

@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):

    start = time.perf_counter()

    source = determine_source(request.question)
    print(f"Router: {time.perf_counter() - start:.2f}s")

    context_parts = []
    sources = []

    if source in (
        QuestionSource.SUPERHERO,
        QuestionSource.BOTH,
    ):

        superhero_name = extract_superhero_name(
            request.question
        )

        superhero_start = time.perf_counter()

        superhero_data = search_superhero(
            superhero_name
        )

        print(
            f"Superhero API: "
            f"{time.perf_counter() - superhero_start:.2f}s"
        )

        if superhero_data.get("response") == "success":

            superhero_answer = format_superhero_response(
                superhero_data
            )

            context_parts.append(
                f"Superhero information:\n"
                f"{superhero_answer}"
            )

            sources.append("superhero_api")


    if source in (
        QuestionSource.DATASET,
        QuestionSource.BOTH,
    ):

        dataset_start = time.perf_counter()

        dataset_answer = search_dataset(
            request.question
        )

        print(
            f"Dataset search: "
            f"{time.perf_counter() - dataset_start:.2f}s"
        )

        context_parts.append(
            f"Dataset information:\n"
            f"{dataset_answer}"
        )

        sources.append("dataset")

    context = "\n\n".join(context_parts)

    prompt = build_prompt(
        question=request.question,
        context=context
    )

    llm_start = time.perf_counter()

    llm = get_llm_provider()
    answer = ""
    try:

        answer = llm.generate(prompt)

        sources.append("llm")

        print(
            f"LLM: "
            f"{time.perf_counter() - llm_start:.2f}s"
        )

    except LLMException as exc:
        print(f"LLM error: {exc}")

        return AskResponse(
            question=request.question,
            answer=(
                "The AI service is temporarily unavailable. "
                "Please try again shortly."
            ),
            sources=sources,
        )

    print(
        f"Total: "
        f"{time.perf_counter() - start:.2f}s"
    )

    return AskResponse(
        question=request.question,
        answer=answer,
        sources=sources,
    )