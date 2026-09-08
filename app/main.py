from fastapi import FastAPI

from app.routes.ask import router as ask_router
from app.routes.health import router as health_router


app = FastAPI(
    title="AI Engineer Assessment API",
    version="1.0.0"
)

app.include_router(ask_router)
app.include_router(health_router)



