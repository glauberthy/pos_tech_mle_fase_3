# api/main.py

from fastapi import FastAPI
from contextlib import asynccontextmanager
from .models import Passageiro
from . import database 

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando a API...")
    database.create_db_and_tables()
    yield
    print("Desligando a API...")

app = FastAPI(
    title="API do Tech Challenge",
    description="Uma API modular para coletar dados de satisfação de passageiros.",
    version="0.3.0", 
    lifespan=lifespan
)

@app.get("/")
def read_root():
    """
    Endpoint raiz que retorna uma mensagem de boas-vindas.
    """
    return {"message": "Bem-vindo à API de Satisfação de Passageiros!"}

@app.post("/adicionar_passageiro", status_code=201)
def adicionar_passageiro(passageiro: Passageiro):
    """
    Recebe os dados de um novo passageiro e os valida.
    """
    print("Novo passageiro recebido:")
    print(passageiro.model_dump())
    
    
    return {"status": "sucesso", "dados_recebidos": passageiro.model_dump()}