from pydantic import BaseModel

class ItemBase(BaseModel):
    nombre: str
    descripcion: str 
    recomendado: bool

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True