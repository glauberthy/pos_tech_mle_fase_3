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
        gender TEXT,
        customer_type TEXT,
        age INTEGER,
        type_of_travel TEXT,
        class TEXT,
        flight_distance INTEGER,
        inflight_wifi_service INTEGER,
        departure_arrival_time_convenient INTEGER,
        ease_of_online_booking INTEGER,
        gate_location INTEGER,
        food_and_drink INTEGER,
        online_boarding INTEGER,
        seat_comfort INTEGER,
        inflight_entertainment INTEGER,
        on_board_service INTEGER,
        leg_room_service INTEGER,
        baggage_handling INTEGER,
        checkin_service INTEGER,
        inflight_service INTEGER,
        cleanliness INTEGER,
        departure_delay_in_minutes INTEGER,
        arrival_delay_in_minutes REAL
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
            gender, customer_type, age, type_of_travel, class, flight_distance,
            inflight_wifi_service, departure_arrival_time_convenient,
            ease_of_online_booking, gate_location, food_and_drink, online_boarding,
            seat_comfort, inflight_entertainment, on_board_service, leg_room_service,
            baggage_handling, checkin_service, inflight_service, cleanliness,
            departure_delay_in_minutes, arrival_delay_in_minutes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            passageiro.gender, passageiro.customer_type, passageiro.age,
            passageiro.type_of_travel, passageiro.class_, passageiro.flight_distance,
            passageiro.inflight_wifi_service, passageiro.departure_arrival_time_convenient,
            passageiro.ease_of_online_booking, passageiro.gate_location,
            passageiro.food_and_drink, passageiro.online_boarding,
            passageiro.seat_comfort, passageiro.inflight_entertainment,
            passageiro.on_board_service, passageiro.leg_room_service,
            passageiro.baggage_handling, passageiro.checkin_service,
            passageiro.inflight_service, passageiro.cleanliness,
            passageiro.departure_delay_in_minutes, passageiro.arrival_delay_in_minutes
        )
    )
    
    conn.commit()
    conn.close()