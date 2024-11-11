from sqlalchemy import Column, Integer, String
from .database import Base

# Define el modelo de base de datos para los personajes
class Character(Base):
    __tablename__ = "characters"

    # Definición de columnas con sus tipos y restricciones
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, nullable=False)
    height = Column(Integer, nullable=False)
    mass = Column(Integer, nullable=False)
    hair_color = Column(String, nullable=False)
    skin_color = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)
