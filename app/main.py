from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import character

# Crea todas las tablas en la base de datos si no existen
Base.metadata.create_all(bind=engine)

# Inicializa la aplicación FastAPI con título, descripción y versión
app = FastAPI(
    title="Character API",
    description="Python API Challange",
    version="1.0.0",
)

# Root route
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Character API"}

# Incluye el router para las rutas de personajes
app.include_router(character.router)
