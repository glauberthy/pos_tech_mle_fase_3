# api/main.py

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException, Request # Importamos o Request
from contextlib import asynccontextmanager
from .models import Passageiro
from . import database

# --- LÓGICA DE STARTUP/SHUTDOWN (LIFESPAN) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Iniciando a API e carregando o modelo...")
    # Carrega o modelo e anexa-o ao estado da aplicação
    app.state.model = joblib.load('models/modelo_final_otimizado_v1.joblib')
    database.create_db_and_tables()
    yield
    print("Desligando a API...")

# --- APLICAÇÃO FastAPI ---
app = FastAPI(
    title="API de Predição de Satisfação de Passageiros",
    description="Uma API que serve um modelo de Machine Learning para prever a satisfação de clientes.",
    version="1.1.0", # Aumentamos a versão para refletir a correção
    lifespan=lifespan
)

# --- ENDPOINTS ---
@app.get("/")
def read_root():
    return {"message": "API de Predição de Satisfação de Passageiros está no ar!"}

@app.post("/predict")
def predict(passageiro: Passageiro, request: Request): # Adicionamos o 'request'
    """
    Recebe os dados de um passageiro, faz a predição com o modelo carregado
    e retorna o resultado.
    """
    try:
        # Acedemos ao modelo a partir do estado da aplicação através do 'request'
        model = request.app.state.model
        
        input_df = pd.DataFrame([passageiro.model_dump()])

        prediction = model.predict(input_df)[0]
        prediction_proba = model.predict_proba(input_df)[0]

        prob_insatisfeito = prediction_proba[0]
        prob_satisfeito = prediction_proba[1]
        
        return {
            "prediction": prediction,
            "probability_neutral_or_dissatisfied": float(prob_insatisfeito),
            "probability_satisfied": float(prob_satisfeito)
        }
    except AttributeError:
        raise HTTPException(status_code=500, detail="O modelo não parece estar carregado.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao fazer a predição: {str(e)}")


@app.post("/adicionar_passageiro", status_code=201)
def adicionar_passageiro(passageiro: Passageiro):
    """
    Recebe os dados de um novo passageiro e os insere no banco de dados.
    """
    try:
        database.insert_passageiro(passageiro)
        return {"status": "sucesso", "mensagem": "Passageiro adicionado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno do servidor ao salvar os dados.")