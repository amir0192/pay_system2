from main import app
from .transfers_models import P2PDent
from database.transfer_service import get_card_history

# ЗАПРОС НА ПЕРЕВОД ДЕНЕГ
@app.post('/api/register-money')
async def money_transfer(transfer_data: P2PDent):
    result = transfer_data
    print(result)
    # если перевод успешный то статус: 1
    return {'status': 1, 'message': result}

# функция получения последних транзакций пользователя
@app.get('/api/monitoring')
async def user_payment(user_id: int):

        result = get_card_history(user_id)

        print(result)

        return {'status': 1, 'message': result}