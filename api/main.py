from fastapi import FastAPI

# Cria uma instância da aplicação FastAPI
app = FastAPI(
    title="API do Tech Challenge",
    description="Uma API para coletar dados de satisfação de passageiros e prever a satisfação.",
    version="0.1.0",
)

# Cria o endpoint raiz ("/") que aceita requisições GET
@app.get("/")
def read_root():
    """
    Endpoint raiz que retorna uma mensagem de boas-vindas.
    """
    return {"message": "Bem-vindo à API de Satisfação de Passageiros!"}