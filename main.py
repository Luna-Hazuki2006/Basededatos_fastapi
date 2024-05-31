from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

import crud, models, schemas
from bd.basededatos import SessionLocal, engine

app = FastAPI()

@app.post('/item')
async def crear_item(): 
    return 'Un item :D'

@app.get('/items')
async def listar_items(): 
    return 'Muchos items :D'

@app.get('/item/{id}')
async def buscar_item(id : str): 
    return f'Este item: {id}'

@app.put('/item/{id}')
async def actualizar_item(id : str): 
    return f'Este item {id}'

@app.delete('/item/{id}')
async def borrar_item(id : str): 
    return f'Este item {id} :\'v'