from pydantic import BaseModel

from datetime import datetime


# модель входных данных
class UserDent(BaseModel):
    profile_photo: str
    name: str
    surname: str
    phone_number: int
    email: str
    city: str
    reg_dat: datetime
    password: str


# модель для карты пользователя
class CardDent(BaseModel):
    user_id: int
    card_number: str
    cardholder: str
    exp_date: int
    card_balance: float
    card_name: str
