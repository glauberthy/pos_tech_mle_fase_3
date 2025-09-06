# api/main.py

from fastapi import FastAPI, HTTPException
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
    version="0.4.0",
    lifespan=lifespan
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de Satisfação de Passageiros!"}


@app.post("/adicionar_passageiro", status_code=201)
def adicionar_passageiro(passageiro: Passageiro):
    """
    Recebe os dados de um novo passageiro, valida e os insere no banco de dados.
    """
    try:
        # Chama a função do módulo de banco de dados para inserir os dados
        database.insert_passageiro(passageiro)
        return {"status": "sucesso", "mensagem": "Passageiro adicionado com sucesso!"}
    except Exception as e:
        # Em caso de erro, levanta uma exceção HTTP com status 500
        print(f"Erro ao inserir passageiro: {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor ao salvar os dados.")