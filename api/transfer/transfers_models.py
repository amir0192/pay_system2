from datetime import datetime
from pydantic import BaseModel

# модель перевода с карты на карту
class P2PDent(BaseModel):
    card_from: int
    amount: float
    card_to: int
    transfer_time: datetime