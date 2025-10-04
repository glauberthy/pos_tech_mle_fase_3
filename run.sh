#!/bin/bash

# Inicia a API (api/main.py) em segundo plano
echo "🚀 Iniciando a API..."
uvicorn api.main:app --host 0.0.0.0 --port 8000 &

# Aguarda 10 segundos para dar tempo da API iniciar
echo "⏳ Aguardando a API..."
sleep 10

# Inicia o App Streamlit (app.py)
echo "🚀 Iniciando o App front-end..."
streamlit run app.py --server.port 7860 --server.address 0.0.0.0