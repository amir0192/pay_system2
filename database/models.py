from database import Base
from sqlalchemy import Column, String, BigInteger, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship

# таблицы пользователя
class User(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, autoincrement=True, primary_key=True)
    profile_photo: Column(String)
    name: Column(String, nullable=False)
    surname: Column(String, nullable=False)
    phone_number: Column(String)
    email: Column(BigInteger, nullable=False)
    city: Column(String)
    reg_dat: Column(DateTime)
    password: Column(String, nullable=False)

# таблица карт
class Card(Base):
    __tablename__ = 'cards'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id: Column(BigInteger, ForeignKey('user.id'), nullable=False)
    card_number: Column(BigInteger, nullable=False, unique=True)
    exp_date: Column(Integer, nullable=False)
    card_balance: Column(Float, nullable=15000)
    card_name: Column(String, default='My card')

    reg_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery' )
# таблица платежей
class Transaction(Base):
    __tablename__ = 'user_transactions'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    card_from = Column(BigInteger, ForeignKey('cards.card_number'))
    amount = Column(Float)
    card_to = Column(BigInteger, ForeignKey('cards.card_number'))
    transfer_time = Column(DateTime)

    card_from_fk = relationship(Card, lazy='subquery')

    card_to_fk = relationship(Card, lazy='subquery')
# таблица категорий платежей
class PayCategory(Base):
    __tablename__ = 'pay_categories'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    category_name = Column(String, nullable=False)

    reg_date = Column(DateTime)
