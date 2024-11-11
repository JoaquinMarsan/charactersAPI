from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, crud
from ..database import SessionLocal

router = APIRouter(
    prefix="/character",
    tags=["characters"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/getAll", response_model=List[schemas.CharacterSummary])
def read_characters(db: Session = Depends(get_db)):
    characters = crud.get_characters(db)
    return characters

@router.get("/get/{id}", response_model=schemas.CharacterOut)
def read_character(id: int, db: Session = Depends(get_db)):
    character = crud.get_character(db, id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.post("/add", response_model=schemas.CharacterOut)
def add_character(character: schemas.CharacterCreate, db: Session = Depends(get_db)):
    if crud.get_character(db, character.id):
        raise HTTPException(status_code=400, detail="Character ID already exists")
    new_character = crud.create_character(db, character)
    return new_character

@router.delete("/delete/{id}")
def delete_character(id: int, db: Session = Depends(get_db)):
    success = crud.delete_character(db, id)
    if not success:
        raise HTTPException(status_code=400, detail="Character not found")
    return {"detail": f"Character with id {id} deleted successfully"}
