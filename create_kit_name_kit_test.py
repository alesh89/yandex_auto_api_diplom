# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# Функция для проверки создания заказа
def check_status(body):
    # В переменной token_number сохранен 
    response_get_order = sender_stand_request.get_order()
    # Проверяется, что код ответа равен 200
    assert response_get_order.status_code == 200

# Тест 1. Допустимое количество символов (1)
def test_create_order_corect_data():
    check_status(data.order_body)
