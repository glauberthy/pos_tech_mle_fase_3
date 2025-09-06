# api/database.py

import sqlite3
from .models import Passageiro 

DATABASE_FILE = "passageiros.db"

def create_db_and_tables():
    """
    Cria o banco de dados e a tabela 'passageiros' se eles não existirem.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS passageiros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Gender TEXT,
        Customer_Type TEXT,
        Age INTEGER,
        Type_of_Travel TEXT,
        Class TEXT,
        Flight_Distance INTEGER,
        Inflight_wifi_service INTEGER,
        Departure_Arrival_time_convenient INTEGER,
        Ease_of_Online_booking INTEGER,
        Gate_location INTEGER,
        Food_and_drink INTEGER,
        Online_boarding INTEGER,
        Seat_comfort INTEGER,
        Inflight_entertainment INTEGER,
        On_board_service INTEGER,
        Leg_room_service INTEGER,
        Baggage_handling INTEGER,
        Checkin_service INTEGER,
        Inflight_service INTEGER,
        Cleanliness INTEGER,
        Departure_Delay_in_Minutes INTEGER,
        Arrival_Delay_in_Minutes REAL
    )
    """)
    conn.commit()
    conn.close()
    print("Banco de dados e tabela 'passageiros' verificados/criados com sucesso.")


def insert_passageiro(passageiro: Passageiro):
    """
    Insere um novo registro de passageiro no banco de dados.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # O SQL INSERT usa '?' como placeholders para segurança (evita SQL Injection)
    cursor.execute(
        """
        INSERT INTO passageiros (
            Gender, Customer_Type, Age, Type_of_Travel, Class, Flight_Distance,
            Inflight_wifi_service, Departure_Arrival_time_convenient,
            Ease_of_Online_booking, Gate_location, Food_and_drink, Online_boarding,
            Seat_comfort, Inflight_entertainment, On_board_service, Leg_room_service,
            Baggage_handling, Checkin_service, Inflight_service, Cleanliness,
            Departure_Delay_in_Minutes, Arrival_Delay_in_Minutes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            passageiro.Gender, passageiro.Customer_Type, passageiro.Age,
            passageiro.Type_of_Travel, passageiro.Class, passageiro.Flight_Distance,
            passageiro.Inflight_wifi_service, passageiro.Departure_Arrival_time_convenient,
            passageiro.Ease_of_Online_booking, passageiro.Gate_location,
            passageiro.Food_and_drink, passageiro.Online_boarding,
            passageiro.Seat_comfort, passageiro.Inflight_entertainment,
            passageiro.On_board_service, passageiro.Leg_room_service,
            passageiro.Baggage_handling, passageiro.Checkin_service,
            passageiro.Inflight_service, passageiro.Cleanliness,
            passageiro.Departure_Delay_in_Minutes, passageiro.Arrival_Delay_in_Minutes
        )
    )
    
    conn.commit()
    conn.close()