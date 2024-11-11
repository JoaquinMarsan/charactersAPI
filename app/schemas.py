from pydantic import BaseModel

# Modelo base para los datos comunes de un personaje
class CharacterBase(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int

# Resumen de personaje, mostrando solo datos requeridos en el punto especificado para el /getAll
class CharacterSummary(BaseModel):
    id: int
    name: str
    height: int
    mass: int
    birth_year: int
    eye_color: str

# Modelo para crear un personaje, incluye el ID
class CharacterCreate(CharacterBase):
    id: int
# Modelo de salida para mostrar datos completos de un personaje
class CharacterOut(CharacterBase):
    id: int

    # Configuración para habilitar la conversión ORM (Object-Relational Mapping)
    class Config:
        orm_mode = True
