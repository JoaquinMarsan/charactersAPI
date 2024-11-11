from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import character

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Character API",
    description="A simple API to manage characters with CRUD operations.",
    version="1.0.0",
)

# Root route
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Character API"}


app.include_router(character.router)
