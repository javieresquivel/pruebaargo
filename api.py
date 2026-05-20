from fastapi import FastAPI
from typing import Optional

# Inicializamos la aplicación
app = FastAPI()

# Ruta principal (nos devuelve un JSON)
@app.get("/")
def read_root():
    return {"mensaje": "¡Hola Mundo desde FastAPI!"}