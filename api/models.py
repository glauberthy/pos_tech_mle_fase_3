# api/models.py

from pydantic import BaseModel, Field # Importe o 'Field'
from typing import Optional

class Passageiro(BaseModel):
    """
    Define a estrutura de dados de um passageiro com validação de valor.
    """
    Gender: str
    Customer_Type: str
    Age: int = Field(
        ...,
        gt=0,
        lt=120,
        description="A idade do passageiro deve ser maior que 0 e menor que 120."
    )
    Type_of_Travel: str
    Class: str
    Flight_Distance: int
    Inflight_wifi_service: int = Field(..., ge=0, le=5)
    Departure_Arrival_time_convenient: int = Field(..., ge=0, le=5)
    Ease_of_Online_booking: int = Field(..., ge=0, le=5)
    Gate_location: int = Field(..., ge=0, le=5)
    Food_and_drink: int = Field(..., ge=0, le=5)
    Online_boarding: int = Field(..., ge=0, le=5)
    Seat_comfort: int = Field(..., ge=0, le=5)
    Inflight_entertainment: int = Field(..., ge=0, le=5)
    On_board_service: int = Field(..., ge=0, le=5)
    Leg_room_service: int = Field(..., ge=0, le=5)
    Baggage_handling: int = Field(..., ge=0, le=5)
    Checkin_service: int = Field(..., ge=0, le=5)
    Inflight_service: int = Field(..., ge=0, le=5)
    Cleanliness: int = Field(..., ge=0, le=5)
    Departure_Delay_in_Minutes: int
    Arrival_Delay_in_Minutes: Optional[float] = None