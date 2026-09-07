from fastapi import FastAPI
from app.config import get_env_meta_info
from pydantic import BaseModel,Field

from app.routes.ask import router as ask_router
from app.routes.health import router as health_router

env_meta_info=get_env_meta_info()


app = FastAPI(
    title="AI Engineer Assessment API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "FastAPI is running"}

app.include_router(ask_router)
app.include_router(health_router)



