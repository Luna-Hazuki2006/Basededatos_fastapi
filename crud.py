from sqlalchemy.orm import Session
from sqlalchemy import select
import modelos, schemas

# def get_user(bd: Session, user_id: int):
#     return bd.query(modelos.User).filter(modelos.User.id == user_id).first()

# def get_user_by_email(bd: Session, email: str):
#     print("bd: ", bd, "Email: ", email)
#     return bd.query(modelos.User).filter(modelos.User.email == email).first()

# def get_users(bd: Session, skip: int = 0, limit: int = 100):
#     return bd.query(modelos.User).offset(skip).limit(limit).all()

# def create_user(bd: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     bd_user = modelos.User(email=user.email, hashed_password=fake_hashed_password)
#     bd.add(bd_user)
#     bd.commit()
#     bd.refresh(bd_user)
#     return bd_user

def get_items(bd: Session, skip: int = 0, limit: int = 100):
    return bd.query(modelos.Item).offset(skip).limit(limit).all()

def create_item(bd: Session, item: schemas.ItemCreate):
    bd_item = modelos.Item(**item.model_dump())
    print("bd item: ", bd_item)
    bd.add(bd_item)
    bd.commit()
    bd.refresh(bd_item)
    print("bd items: ", bd_item)
    return bd_item

def buscar_item(bd: Session, id: int, skip: int = 0, limit: int = 100): 
    lista = bd.query(modelos.Item).offset(skip).limit(limit).all()
    for este in lista: 
        if este.id == id: 
            return este