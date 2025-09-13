# api/models.py

from pydantic import BaseModel, Field # Importe o 'Field'
from typing import Optional
# --- Nomes das colunas padronizados ---
# Index(['unnamed:_0', 'id', 'gender', 'customer_type', 'age', 'type_of_travel',
#        'class_', 'flight_distance', 'inflight_wifi_service',
#        'departure_arrival_time_convenient', 'ease_of_online_booking',
#        'gate_location', 'food_and_drink', 'online_boarding', 'seat_comfort',
#        'inflight_entertainment', 'on_board_service', 'leg_room_service',
#        'baggage_handling', 'checkin_service', 'inflight_service',
#        'cleanliness', 'departure_delay_in_minutes', 'arrival_delay_in_minutes',
#        'satisfaction'],
#       dtype='object')
class Passageiro(BaseModel):
    """
    Define a estrutura de dados de um passageiro com validação de valor.
    """
    gender: str
    customer_type: str
    age: int = Field(
        ...,
        gt=0,
        lt=120,
        description="A idade do passageiro deve ser maior que 0 e menor que 120."
    )
    type_of_travel: str
    class_: str
    flight_distance: int
    inflight_wifi_service: int = Field(..., ge=0, le=5)
    departure_arrival_time_convenient: int = Field(..., ge=0, le=5)
    ease_of_online_booking: int = Field(..., ge=0, le=5)
    gate_location: int = Field(..., ge=0, le=5)
    food_and_drink: int = Field(..., ge=0, le=5)
    online_boarding: int = Field(..., ge=0, le=5)
    seat_comfort: int = Field(..., ge=0, le=5)
    inflight_entertainment: int = Field(..., ge=0, le=5)
    on_board_service: int = Field(..., ge=0, le=5)
    leg_room_service: int = Field(..., ge=0, le=5)
    baggage_handling: int = Field(..., ge=0, le=5)
    checkin_service: int = Field(..., ge=0, le=5)
    inflight_service: int = Field(..., ge=0, le=5)
    cleanliness: int = Field(..., ge=0, le=5)
    departure_delay_in_minutes: int
    arrival_delay_in_minutes: Optional[float] = None