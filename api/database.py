# api/database.py

import sqlite3

# Define o nome do arquivo do banco de dados
DATABASE_FILE = "passageiros.db"

def create_db_and_tables():
    """
    Cria o banco de dados e a tabela 'passageiros' se eles não existirem.
    """
    # Conecta ao banco de dados (cria o arquivo se não existir)
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # SQL para criar a tabela. A estrutura espelha o modelo Pydantic 'Passageiro'.
    # Usamos 'IF NOT EXISTS' para evitar erros se a tabela já foi criada.
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

    # Salva as alterações e fecha a conexão
    conn.commit()
    conn.close()
    print("Banco de dados e tabela 'passageiros' verificados/criados com sucesso.")