from fastapi import APIRouter
from app.services.superhero import search_superhero,format_superhero_response
from app.models.ask import AskRequest, AskResponse
from app.services.router import (
    is_superhero_question,
    extract_superhero_name,
)
from app.services.dataset import search_dataset

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    # superhero_data = search_superhero(request.question)
    # # return {
    # #     "question": request.question,
    # #     "answer": f"You asked: {request.question}"
    # # }
    # return {
    #     "question": request.question,
    #     "answer": str(superhero_data)
    # }

    if is_superhero_question(request.question):
        superhero_name = extract_superhero_name(request.question)
        superhero_data = search_superhero(superhero_name)

        return {
            "question": request.question,
            "answer": format_superhero_response(superhero_data)
        }
    dataset_result = search_dataset(request.question)
    return {
        "question": request.question,
        "answer": dataset_result
    }