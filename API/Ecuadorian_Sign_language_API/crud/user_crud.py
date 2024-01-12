from fastapi import APIRouter, Response, HTTPException
from config.db import engine
from models.user import users, palabra, caracter
from schemas.user import User, Palabra, Caracter, UserLogin, UserResponse
from cryptography.fernet import Fernet
from starlette import status
from sqlalchemy.sql import select
from fastapi import APIRouter, Response, FastAPI,File, UploadFile
from fastapi.responses import FileResponse
from datetime import datetime
import re
import os
import shutil
import pandas as pd
import json
from typing import List

user_crud = APIRouter()

@user_crud.post("/users/", response_model=User, tags=["users"])
async def create_user(item: User):
    conn = engine.connect()
    try:
        new_item = {
            "name": item.name,
            "email": item.email,
            "password": item.password  # Considera usar hashing antes de guardar contraseñas.
        }
        result = conn.execute(users.insert().values(**new_item))
        item.id = result.inserted_primary_key[0]
        
        # Realizar commit para guardar los cambios
        conn.commit()
    finally:
        conn.close()
    
    return item


@user_crud.get("/users/", response_model=List[User], tags=["users"])
def get_users():
    conn = engine.connect()
    result = conn.execute(users.select()).fetchall()
    conn.close()
    return result

@user_crud.get("/users/{user_id}", response_model=User, tags=["users"])
async def get_user_by_id(user_id: int):
    conn = engine.connect()
    result = conn.execute(users.select().where(users.c.id == user_id)).first()
    conn.close()
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result

@user_crud.put("/users/{user_id}", response_model=User, tags=["users"])
async def update_user(user_id: int, item: User):
    conn = engine.connect()
    try:
        result = conn.execute(users.update().where(users.c.id == user_id).values(
            name=item.name, email=item.email, password=item.password
        ))
        
        # Realizar commit para guardar los cambios
        conn.commit()
    finally:
        conn.close()
    
    if not result.rowcount:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {**item.dict(), "id": user_id}


@user_crud.delete("/users/{user_id}", tags=["users"])
async def delete_user(user_id: int):
    conn = engine.connect()
    try:
        result = conn.execute(users.delete().where(users.c.id == user_id))
        
        # Realizar commit para guardar la eliminación
        conn.commit()
    finally:
        conn.close()
    
    if not result.rowcount:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"status": "User deleted successfully"}


palabra_crud = APIRouter()

@palabra_crud.post("/palabra/", response_model=Palabra, tags=["palabra"])
async def create_palabra(palabraAux: str, descripcionAux: str, gif: UploadFile = File(...)):
    conn = engine.connect()
    try:
        print("palabra",palabraAux)
        print("descripcion",descripcionAux)
        print("gif",palabraAux.upper()+".gif")

        nameGif = palabraAux.upper()+".gif"
        
        # Guardar el archivo en la carpeta deseada
        with open(f"gifs/palabras/{nameGif}", "wb") as buffer:
            shutil.copyfileobj(gif.file, buffer)
        
        # Ruta donde se guarda el gif
        gif_path = f"/gifs/palabras/{nameGif}"
        
        new_item = {
            "palabra": palabraAux,
            "descripcion": descripcionAux,
            "gif": nameGif  # Guardamos la ruta en la base de datos
        }
        result = conn.execute(palabra.insert().values(**new_item))
        conn.commit()  # Aquí es donde agregamos el commit
        
        new_item["id_palabra"] = result.inserted_primary_key[0]  # Establece el id_palabra antes de crear el objeto Palabra
        item = Palabra(**new_item)
        
        return item
    finally:
        conn.close()


@palabra_crud.get("/palabra/", response_model=List[Palabra], tags=["palabra"])
def get_palabras():
    conn = engine.connect()
    result = conn.execute(palabra.select()).fetchall()
    conn.close()
    return result

@palabra_crud.get("/palabra/{palabra_id}", response_model=Palabra, tags=["palabra"])
def get_palabra_by_id(palabra_id: int):
    conn = engine.connect()
    result = conn.execute(palabra.select().where(palabra.c.id_palabra == palabra_id)).first()
    conn.close()
    if not result:
        raise HTTPException(status_code=404, detail="Palabra not found")
    return result

@palabra_crud.get("/palabra/exist/{palabraAux}", tags=["palabra"])
async def check_word_exists(palabraAux: str):
    conn = engine.connect()
    result = conn.execute(palabra.select().where(palabra.c.palabra == palabraAux)).first()
    conn.close()
    if result:
        return {"exists": True}
    return {"exists": False}

from pathlib import Path

@palabra_crud.put("/palabra/{palabra_id}", response_model=Palabra, tags=["palabra"])
def update_palabra(
    palabra_id: int, 
    palabra_text: str,
    descripcion: str,    
    gif: UploadFile = File(...)
):
    conn = engine.connect()
    
    # Paso 1: Consulta el nombre del archivo GIF anterior
    current_gif_data = get_palabra_by_id(palabra_id)
    current_gif_name = current_gif_data["gif"]

    # Paso 2: Si el nombre del archivo GIF anterior existe, elimínalo
    if current_gif_name:
        current_gif_path = Path(f"gifs/palabras/{current_gif_name}")
        if current_gif_path.exists():
            current_gif_path.unlink()

    # Paso 3: Carga y guarda el nuevo GIF
    nameGif = palabra_text.upper() + ".gif"
    with open(f"gifs/palabras/{nameGif}", "wb") as buffer:
        shutil.copyfileobj(gif.file, buffer)

    result = conn.execute(palabra.update().where(palabra.c.id_palabra == palabra_id).values(
        palabra=palabra_text, descripcion=descripcion, gif=nameGif
    ))
    
    conn.close()
    
    if not result.rowcount:
        raise HTTPException(status_code=404, detail="Palabra not found")
    
    return {"palabra": palabra_text, "descripcion": descripcion, "gif": nameGif, "id_palabra": palabra_id}

@palabra_crud.delete("/palabra/{palabra_id}", tags=["palabra"])
async def delete_palabra(palabra_id: int):
    conn = engine.connect()
    result = conn.execute(palabra.delete().where(palabra.c.id_palabra == palabra_id))
    conn.close()
    if not result.rowcount:
        raise HTTPException(status_code=404, detail="Palabra not found")
    return {"status": "Palabra deleted successfully"}

caracter_crud = APIRouter()

@caracter_crud.post("/caracter/", response_model=Caracter, tags=["caracter"])
async def create_caracter(item: Caracter):
    conn = engine.connect()
    new_item = {
        "caracter": item.caracter,
        "gif": item.gif
    }
    result = conn.execute(caracter.insert().values(**new_item))
    item.id_caracter = result.inserted_primary_key[0]
    conn.close()
    return item

@caracter_crud.get("/caracter/", response_model=List[Caracter], tags=["caracter"])
def get_caracteres():
    conn = engine.connect()
    result = conn.execute(caracter.select()).fetchall()
    conn.close()
    return result

@caracter_crud.get("/caracter/{caracter_id}", response_model=Caracter, tags=["caracter"])
def get_caracter_by_id(caracter_id: int):
    conn = engine.connect()
    result = conn.execute(caracter.select().where(caracter.c.id_caracter == caracter_id)).first()
    conn.close()
    if not result:
        raise HTTPException(status_code=404, detail="Caracter not found")
    return result

@caracter_crud.put("/caracter/{caracter_id}", response_model=Caracter, tags=["caracter"])
def update_caracter(
    caracter_id: int, 
    caracter_text: str,
    gif: UploadFile = File(...)
):
    conn = engine.connect()
    
    # Paso 1: Consulta el nombre del archivo GIF anterior usando get_caracter_by_id
    current_gif_data = get_caracter_by_id(caracter_id)
    current_gif_name = current_gif_data["gif"]

    # Paso 2: Si el nombre del archivo GIF anterior existe, elimínalo
    if current_gif_name:
        current_gif_path = Path(f"gifs/caracteres/{current_gif_name}")
        if current_gif_path.exists():
            current_gif_path.unlink()

    # Paso 3: Carga y guarda el nuevo GIF
    nameGif = caracter_text.upper() + ".gif"
    with open(f"gifs/caracteres/{nameGif}", "wb") as buffer:
        shutil.copyfileobj(gif.file, buffer)

    result = conn.execute(caracter.update().where(caracter.c.id_caracter == caracter_id).values(
        caracter=caracter_text, gif=nameGif
    ))
    
    conn.close()
    
    if not result.rowcount:
        raise HTTPException(status_code=404, detail="Caracter not found")
    
    return {"caracter": caracter_text, "gif": nameGif, "id_caracter": caracter_id}

@caracter_crud.delete("/caracter/{caracter_id}", tags=["caracter"])
async def delete_caracter(caracter_id: int):
    conn = engine.connect()
    result = conn.execute(caracter.delete().where(caracter.c.id_caracter == caracter_id))
    conn.close()
    if not result.rowcount:
        raise HTTPException(status_code=404, detail="Caracter not found")
    return {"status": "Caracter deleted successfully"}


@palabra_crud.post("/palabra/video/", response_model=Palabra, tags=["palabra"])
async def create_palabra_video(palabraAux: str, descripcionAux: str, video: UploadFile = File(...)):
    conn = engine.connect()
    try:
        nameVideo = palabraAux.upper() + ".mp4"
        
        # Guardar el archivo en la carpeta deseada
        with open(f"videos/palabras/{nameVideo}", "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)
        
        new_item = {
            "palabra": palabraAux,
            "descripcion": descripcionAux,
            "video": nameVideo  # Guardamos solo el nombre del video en la base de datos
        }
        result = conn.execute(palabra.insert().values(**new_item))
        conn.commit() 
        
        new_item["id_palabra"] = result.inserted_primary_key[0]
        item = Palabra(**new_item)
        
        return item
    finally:
        conn.close()

@caracter_crud.post("/caracter/video/", tags=["caracter"])
async def create_caracter_video(caracter_text: str, video: UploadFile = File(...)):
    conn = engine.connect()
    nameVideo = caracter_text.upper() + ".mp4"
    
    # Guardar el archivo en la carpeta deseada
    with open(f"videos/caracteres/{nameVideo}", "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
    
    new_item = {
        "caracter": caracter_text,
        "gif": nameVideo  # Guardamos solo el nombre del video en la base de datos
    }
    result = conn.execute(caracter.insert().values(**new_item))
    conn.close()
    
    return {"caracter": caracter_text, "gif": nameVideo, "id_caracter": result.inserted_primary_key[0]}

@palabra_crud.get("/palabra/video/exist/{palabraAux}", tags=["palabra"])
async def check_word_exists_video(palabraAux: str):
    conn = engine.connect()
    result = conn.execute(palabra.select().where(palabra.c.palabra == palabraAux)).first()
    conn.close()
    if result:
        return {"exists": True}
    return {"exists": False}

@palabra_crud.put("/palabra/video/{palabra_id}", response_model=Palabra, tags=["palabra"])
def update_palabra_video(
    palabra_id: int, 
    palabra_text: str,
    descripcion: str,    
    video: UploadFile = File(...)
):
    conn = engine.connect()
    trans = conn.begin()  # Iniciar la transacción
    
    try:
        # Paso 1: Consulta el nombre del archivo video anterior
        current_video_data = get_palabra_by_id(palabra_id)
        columns = ["id_palabra", "palabra", "descripcion", "video"]
        current_video_data_dict = dict(zip(columns, current_video_data))
        current_video_name = current_video_data_dict["video"]

        # Paso 2: Si el nombre del archivo video anterior existe, elimínalo
        if current_video_name:
            current_video_path = Path(f"videos/palabras/{current_video_name}")
            if current_video_path.exists():
                current_video_path.unlink()

        # Paso 3: Carga y guarda el nuevo video
        nameVideo = palabra_text.upper() + ".mp4"
        with open(f"videos/palabras/{nameVideo}", "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)

        result = conn.execute(palabra.update().where(palabra.c.id_palabra == palabra_id).values(
            palabra=palabra_text, descripcion=descripcion, video=nameVideo
        ))

        # Realizar commit para asegurar los cambios en la base de datos
        trans.commit()
        
    except Exception as e:
        trans.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        conn.close()
    
    if not result.rowcount:
        raise HTTPException(status_code=404, detail="Palabra not found")
    
    return {"palabra": palabra_text, "descripcion": descripcion, "video": nameVideo, "id_palabra": palabra_id}

@caracter_crud.put("/caracter/video/{caracter_id}", response_model=Caracter, tags=["caracter"])
def update_caracter_video(
    caracter_id: int, 
    caracter_text: str, 
    video: UploadFile = File(...)
):
    conn = engine.connect()
    trans = conn.begin()  # Iniciar la transacción
    
    try:
        # Paso 1: Consulta el nombre del video anterior
        current_video_data = get_caracter_by_id(caracter_id)
        columns = ["id_caracter", "caracter", "video"]
        current_video_data_dict = dict(zip(columns, current_video_data))
        current_video_name = current_video_data_dict["video"]

        # Paso 2: Si el nombre del video anterior existe, elimínalo
        if current_video_name:
            current_video_path = Path(f"videos/caracteres/{current_video_name}")
            if current_video_path.exists():
                current_video_path.unlink()

        # Paso 3: Carga y guarda el nuevo video
        nameVideo = caracter_text.upper() + ".mp4"
        with open(f"videos/caracteres/{nameVideo}", "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)

        result = conn.execute(caracter.update().where(caracter.c.id_caracter == caracter_id).values(
            caracter=caracter_text, video=nameVideo
        ))

        # Realizar commit para asegurar los cambios en la base de datos
        trans.commit()
        
    except Exception as e:
        trans.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    
    finally:
        conn.close()
    
    if not result.rowcount:
        raise HTTPException(status_code=404, detail="Caracter not found")
    
    return {"caracter": caracter_text, "video": nameVideo, "id_caracter": caracter_id}

@user_crud.post("/login/", response_model=UserResponse, tags=["users"])
async def login(user: UserLogin):
    conn = engine.connect()
    
    result = conn.execute(users.select().where(users.c.email == user.email)).first()
    conn.close()
    
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user = {
        "id": result[0],
        "name": result[1],
        "email": result[2],
        "password": result[3]
    }
    
    if db_user["password"] != user.password:
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    return {"email": user.email, "role": "admin"}

