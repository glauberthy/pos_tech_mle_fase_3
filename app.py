import streamlit as st
import pandas as pd
import requests # Importamos a biblioteca para fazer chamadas à API

# --- CONFIGURAÇÃO DA PÁGINA E TÍTULO ---
st.set_page_config(
    page_title="Satisfação de Clientes",
    page_icon="✈️",
    layout="wide"
)

st.title("Tech Challenge: Predição de Satisfação de Clientes ✈️")

# --- FUNÇÃO PARA CRIAR O FORMULÁRIO (REUTILIZÁVEL) ---
def criar_formulario():
    """Cria e exibe os widgets do formulário, retornando os dados inseridos."""
    gender = st.selectbox('Gênero', ['Male', 'Female'])
    customer_type = st.selectbox('Tipo de Cliente', ['Loyal Customer', 'disloyal Customer'])
    type_of_travel = st.selectbox('Tipo de Viagem', ['Business travel', 'Personal Travel'])
    flight_class = st.selectbox('Classe', ['Business', 'Eco', 'Eco Plus'])

    age = st.slider('Idade', 7, 85, 40)
    flight_distance = st.number_input('Distância do Voo (milhas)', min_value=30, value=1000)
    departure_delay = st.number_input('Atraso na Partida (minutos)', min_value=0, value=0)
    
    st.subheader('Avaliações dos Serviços (0-5)')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        wifi = st.slider('Serviço de Wi-Fi', 0, 5, 3)
        online_booking = st.slider('Facilidade de Reserva', 0, 5, 3)
        food_drink = st.slider('Comida e Bebida', 0, 5, 3)
        entertainment = st.slider('Entretenimento', 0, 5, 3)
        baggage = st.slider('Manuseio de Bagagem', 0, 5, 3)
        inflight_service = st.slider('Serviço de Bordo', 0, 5, 3)
    with col2:
        departure_arrival_time = st.slider('Conveniência do Horário', 0, 5, 3)
        gate_location = st.slider('Localização do Portão', 0, 5, 3)
        online_boarding = st.slider('Embarque Online', 0, 5, 3)
        onboard_service = st.slider('Atendimento a Bordo', 0, 5, 3)
        checkin = st.slider('Serviço de Check-in', 0, 5, 3)
        cleanliness = st.slider('Limpeza', 0, 5, 3)
    with col3:
        seat_comfort = st.slider('Conforto do Assento', 0, 5, 3)
        leg_room = st.slider('Espaço para as Pernas', 0, 5, 3)

    # --- ALTERAÇÃO AQUI ---
    # As chaves do dicionário agora correspondem exatamente aos nomes dos
    # campos no nosso modelo Pydantic (minúsculas e com underscores).
    dados = {
        'gender': gender,
        'customer_type': customer_type,
        'age': age,
        'type_of_travel': type_of_travel,
        'class_': flight_class, # Mapeado para o atributo 'class_' no Pydantic
        'flight_distance': flight_distance,
        'inflight_wifi_service': wifi,
        'departure_arrival_time_convenient': departure_arrival_time,
        'ease_of_online_booking': online_booking,
        'gate_location': gate_location,
        'food_and_drink': food_drink,
        'online_boarding': online_boarding,
        'seat_comfort': seat_comfort,
        'inflight_entertainment': entertainment,
        'on_board_service': onboard_service,
        'leg_room_service': leg_room,
        'baggage_handling': baggage,
        'checkin_service': checkin,
        'inflight_service': inflight_service,
        'cleanliness': cleanliness,
        'departure_delay_in_minutes': departure_delay,
        'arrival_delay_in_minutes': 0
    }
    return dados

# --- SELEÇÃO DE PÁGINA (NAVEGAÇÃO) ---
st.sidebar.title("Navegação")
pagina_selecionada = st.sidebar.radio("Escolha uma página:", ["Simulador de Satisfação", "Registrar Nova Pesquisa"])

# --- PÁGINA 1: SIMULADOR DE SATISFAÇÃO ---
if pagina_selecionada == "Simulador de Satisfação":
    st.header("Simulador de Satisfação de Clientes (Ferramenta Gerencial)")
    st.markdown("Preencha os dados abaixo para simular a satisfação de um passageiro.")
    
    dados_formulario = criar_formulario()
    
    if st.button('Fazer Previsão'):
        api_url = 'http://127.0.0.1:8000/predict'
        
        response = requests.post(api_url, json=dados_formulario)
        
        if response.status_code == 200:
            resultado = response.json()
            prediction = resultado['prediction']
            prob_satisfeito = resultado['probability_satisfied']
            prob_insatisfeito = resultado['probability_neutral_or_dissatisfied']
            
            st.subheader('Resultado da Predição:')
            if prediction == 'satisfied':
                st.success('Cliente Satisfeito 😊')
            else:
                st.warning('Cliente Neutro ou Insatisfeito 😐')

            col1, col2 = st.columns(2)
            col1.metric("Probabilidade de Satisfação", f"{prob_satisfeito:.2%}")
            col2.metric("Probabilidade de Insatisfação", f"{prob_insatisfeito:.2%}")
        else:
            st.error(f"Erro ao fazer a predição. Status: {response.status_code} - {response.text}")

# --- PÁGINA 2: REGISTRAR NOVA PESQUISA ---
elif pagina_selecionada == "Registrar Nova Pesquisa":
    st.header("Formulário de Pesquisa de Satisfação")
    st.markdown("Preencha os dados da pesquisa para registrar no nosso banco de dados.")

    dados_formulario = criar_formulario()

    if st.button('Enviar Pesquisa'):
        api_url = 'http://127.0.0.1:8000/adicionar_passageiro'

        response = requests.post(api_url, json=dados_formulario)

        if response.status_code == 201:
            st.success("Pesquisa enviada e registrada com sucesso!")
        else:
            st.error(f"Erro ao enviar a pesquisa. Status: {response.status_code} - {response.text}")
