import streamlit as st
import joblib
import pandas as pd

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Predição de Satisfação de Clientes",
    page_icon="✈️",
    layout="wide"
)

# --- FUNÇÕES ---
@st.cache_resource
def carregar_modelo():
    """
    Função para carregar nosso pipeline de modelo.
    Usa o cache do Streamlit para não recarregar o modelo a cada interação.
    """
    pipeline = joblib.load('models/modelo_satisfacao_passageiros_v1.joblib')
    return pipeline

def coletar_dados_sidebar():
    """
    Cria os widgets na barra lateral para coletar os dados do passageiro
    e retorna um dicionário com os valores.
    """
    st.sidebar.header('Preencha os Dados do Passageiro')

    # --- Dados Categóricos ---
    gender = st.sidebar.selectbox('Gênero', ['Male', 'Female'])
    customer_type = st.sidebar.selectbox('Tipo de Cliente', ['Loyal Customer', 'disloyal Customer'])
    type_of_travel = st.sidebar.selectbox('Tipo de Viagem', ['Business travel', 'Personal Travel'])
    flight_class = st.sidebar.selectbox('Classe', ['Business', 'Eco', 'Eco Plus'])

    # --- Dados Numéricos ---
    age = st.sidebar.slider('Idade', 7, 85, 40)
    flight_distance = st.sidebar.number_input('Distância do Voo (milhas)', min_value=30, value=1000)
    departure_delay = st.sidebar.number_input('Atraso na Partida (minutos)', min_value=0, value=0)
    
    st.sidebar.subheader('Avaliações dos Serviços (0-5)')
    
    wifi = st.sidebar.slider('Serviço de Wi-Fi a bordo', 0, 5, 3)
    departure_arrival_time = st.sidebar.slider('Conveniência do Horário', 0, 5, 3)
    online_booking = st.sidebar.slider('Facilidade de Reserva Online', 0, 5, 3)
    gate_location = st.sidebar.slider('Localização do Portão', 0, 5, 3)
    food_drink = st.sidebar.slider('Comida e Bebida', 0, 5, 3)
    online_boarding = st.sidebar.slider('Embarque Online', 0, 5, 3)
    seat_comfort = st.sidebar.slider('Conforto do Assento', 0, 5, 3)
    entertainment = st.sidebar.slider('Entretenimento a Bordo', 0, 5, 3)
    onboard_service = st.sidebar.slider('Serviço a Bordo', 0, 5, 3)
    leg_room = st.sidebar.slider('Espaço para as Pernas', 0, 5, 3)
    baggage = st.sidebar.slider('Manuseio de Bagagem', 0, 5, 3)
    checkin = st.sidebar.slider('Serviço de Check-in', 0, 5, 3)
    inflight_service = st.sidebar.slider('Serviço de Bordo (voo)', 0, 5, 3)
    cleanliness = st.sidebar.slider('Limpeza', 0, 5, 3)
    
    dados = {
        'Gender': gender,
        'Customer Type': customer_type,
        'Age': age,
        'Type of Travel': type_of_travel,
        'Class': flight_class,
        'Flight Distance': flight_distance,
        'Inflight wifi service': wifi,
        'Departure/Arrival time convenient': departure_arrival_time,
        'Ease of Online booking': online_booking,
        'Gate location': gate_location,
        'Food and drink': food_drink,
        'Online boarding': online_boarding,
        'Seat comfort': seat_comfort,
        'Inflight entertainment': entertainment,
        'On-board service': onboard_service,
        'Leg room service': leg_room,
        'Baggage handling': baggage,
        'Checkin service': checkin,
        'Inflight service': inflight_service,
        'Cleanliness': cleanliness,
        'Departure Delay in Minutes': departure_delay,
        'Arrival Delay in Minutes': 0 # Usamos 0 como placeholder, pois o modelo precisa deste campo
    }
    
    return dados

# --- LAYOUT DO APP ---

modelo = carregar_modelo()
st.title("Dashboard de Predição de Satisfação de Clientes ✈️")
st.markdown("Use a barra lateral para inserir os dados do passageiro e clique em 'Fazer Previsão'.")

dados_passageiro = coletar_dados_sidebar()

if st.sidebar.button('Fazer Previsão'):
    input_df = pd.DataFrame([dados_passageiro])
    
    # --- LÓGICA DE PREVISÃO E EXIBIÇÃO ---
    
    # Faz a predição
    prediction = modelo.predict(input_df)[0]
    prediction_proba = modelo.predict_proba(input_df)[0]
    
    # Extrai as probabilidades
    prob_insatisfeito = prediction_proba[0]
    prob_satisfeito = prediction_proba[1]
    
    st.subheader('Resultado da Predição:')
    
    # Exibe o resultado de forma condicional
    if prediction == 'satisfied':
        st.success('Cliente Satisfeito 😊')
    else:
        st.warning('Cliente Neutro ou Insatisfeito 😐')
        
    # Exibe as probabilidades em colunas
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Probabilidade de Insatisfação", f"{prob_insatisfeito:.2%}")
    with col2:
        st.metric("Probabilidade de Satisfação", f"{prob_satisfeito:.2%}")

    # Exibe um gráfico de barras com as probabilidades
    st.write("---")
    st.subheader("Visualização das Probabilidades")
    prob_df = pd.DataFrame({
        'Classe': ['Neutro ou Insatisfeito', 'Satisfeito'],
        'Probabilidade': [prob_insatisfeito, prob_satisfeito]
    })
    st.dataframe(prob_df)
    st.bar_chart(prob_df.set_index('Classe'))