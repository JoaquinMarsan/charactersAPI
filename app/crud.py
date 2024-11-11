from sqlalchemy.orm import Session
from . import models, schemas

# Obtiene un personaje específico por su ID
def get_character(db: Session, character_id: int):
    return db.query(models.Character).filter(models.Character.id == character_id).first()

# Obtiene todos los personajes de la base de datos
def get_characters(db: Session):
    return db.query(models.Character).all()

# Crea un nuevo personaje y lo guarda en la base de datos
def create_character(db: Session, character: schemas.CharacterCreate):
    db_character = models.Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

# Elimina un personaje de la base de datos por su ID, si existe
def delete_character(db: Session, character_id: int):
    character = get_character(db, character_id)
    if character:
        db.delete(character)
        db.commit()
        return True
    return False
