from pydantic import BaseModel

class CharacterBase(BaseModel):
    name: str
    height: int
    mass: int
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: int

class CharacterSummary(BaseModel):
    id: int
    name: str
    height: int
    mass: int
    birth_year: int
    eye_color: str

class CharacterCreate(CharacterBase):
    id: int

class CharacterOut(CharacterBase):
    id: int

    class Config:
        orm_mode = True
