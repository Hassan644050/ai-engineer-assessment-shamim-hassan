from fastapi import APIRouter
from app.services.superhero import search_superhero
from app.models.ask import AskRequest, AskResponse

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
def ask(request: AskRequest):
    #superhero_data = search_superhero(request.question)
    superhero_data = search_superhero("Batman")
    # return {
    #     "question": request.question,
    #     "answer": f"You asked: {request.question}"
    # }
    return {
        "question": request.question,
        "answer": str(superhero_data)
    }