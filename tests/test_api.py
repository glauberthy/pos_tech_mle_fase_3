# tests/test_api.py

# Teste de Integração para a API FastAPI usando TestClient

from fastapi.testclient import TestClient
from api.main import app 

# Criamos um cliente de teste que usará nossa aplicação FastAPI
client = TestClient(app)

# Teste de Sanidade (Health Check)
def test_read_root():
    """Testa se o endpoint raiz retorna a mensagem de boas-vindas corretamente."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bem-vindo à API de Satisfação de Passageiros!"}

# Teste de Caminho Feliz (Happy Path)
def test_adicionar_passageiro_sucesso():
    """
    Testa o cenário de sucesso (happy path): enviar dados válidos de um passageiro.
    Verifica se a API retorna o status 201 (Created) e a mensagem de sucesso.
    """
    # Dados de um passageiro válido para o teste
    passageiro_valido = {
        "Gender": "Male",
        "Customer_Type": "Loyal Customer",
        "Age": 35,
        "Type_of_Travel": "Business travel",
        "Class": "Business",
        "Flight_Distance": 500,
        "Inflight_wifi_service": 5,
        "Departure_Arrival_time_convenient": 5,
        "Ease_of_Online_booking": 5,
        "Gate_location": 5,
        "Food_and_drink": 5,
        "Online_boarding": 5,
        "Seat_comfort": 5,
        "Inflight_entertainment": 5,
        "On_board_service": 5,
        "Leg_room_service": 5,
        "Baggage_handling": 5,
        "Checkin_service": 5,
        "Inflight_service": 5,
        "Cleanliness": 5,
        "Departure_Delay_in_Minutes": 0,
        "Arrival_Delay_in_Minutes": 0
    }
    
    # Faz uma requisição POST para o endpoint
    response = client.post("/adicionar_passageiro", json=passageiro_valido)
    
    # Asserts: verificamos se o resultado é o esperado
    assert response.status_code == 201
    assert response.json() == {"status": "sucesso", "mensagem": "Passageiro adicionado com sucesso!"}

# Teste de Caminho Triste (Unhappy Path)
def test_adicionar_passageiro_erro_validacao():
    """
    Testa o cenário de erro (unhappy path): enviar dados inválidos.
    Verifica se a API retorna o status 422 (Unprocessable Entity).
    """
    # Dados de um passageiro com idade inválida (0)
    passageiro_invalido = {
        "Gender": "Female",
        "Customer_Type": "disloyal Customer",
        "Age": 0, # Idade inválida
        "Type_of_Travel": "Personal Travel",
        "Class": "Eco",
        "Flight_Distance": 100,
        "Inflight_wifi_service": 1,
        "Departure_Arrival_time_convenient": 1,
        "Ease_of_Online_booking": 1,
        "Gate_location": 1,
        "Food_and_drink": 1,
        "Online_boarding": 1,
        "Seat_comfort": 1,
        "Inflight_entertainment": 1,
        "On_board_service": 1,
        "Leg_room_service": 1,
        "Baggage_handling": 1,
        "Checkin_service": 1,
        "Inflight_service": 1,
        "Cleanliness": 1,
        "Departure_Delay_in_Minutes": 10,
        "Arrival_Delay_in_Minutes": 10
    }
    
    # Faz a requisição POST
    response = client.post("/adicionar_passageiro", json=passageiro_invalido)
    
    # Assert: verificamos se a API barrou os dados corretamente
    assert response.status_code == 422
    # Verificamos se a mensagem de erro detalha o problema no campo 'Age'
    assert "Input should be greater than 0" in response.text