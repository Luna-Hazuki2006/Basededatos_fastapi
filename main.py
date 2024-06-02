from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

import crud, modelos, schemas
from bd.basededatos import SessionLocal, engine

modelos.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Dependenncia
def get_bd():
    bd = SessionLocal()
    try:
        yield bd
    finally:
        bd.close()

@app.post('/item', response_model=schemas.Item)
async def crear_item(item: schemas.ItemCreate, bd: Session = Depends(get_bd)): 
    return crud.create_item(bd, item)

@app.get('/items', response_model=list[schemas.Item])
async def listar_items(request: Request, bd: Session = Depends(get_bd)): 
    items = crud.get_items(bd)
    return templates.TemplateResponse(
        request=request, name="inicio.html", context={"items": items}
    )

@app.get('/item/{id}', response_model=schemas.Item)
async def encontrar_item(id : int, bd: Session = Depends(get_bd)):
    print(id) 
    este = crud.buscar_item(bd, id)
    print(este)
    return este

@app.put('/item/{id}', response_model=schemas.Item)
async def actualizar_item(id : int): 
    return f'Este item {id}'

@app.delete('/item/{id}', response_model=schemas.Item)
async def borrar_item(id : int): 
    return f'Este item {id} :\'v'