from sqlalchemy.orm import Session
from . import models, schemas

def get_character(db: Session, character_id: int):
    return db.query(models.Character).filter(models.Character.id == character_id).first()

def get_characters(db: Session):
    return db.query(models.Character).all()

def create_character(db: Session, character: schemas.CharacterCreate):
    db_character = models.Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

def delete_character(db: Session, character_id: int):
    character = get_character(db, character_id)
    if character:
        db.delete(character)
        db.commit()
        return True
    return False
