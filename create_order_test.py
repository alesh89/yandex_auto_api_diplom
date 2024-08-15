# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

# Функция для проверки создания заказа
def check_status(body):
    response_get_order = sender_stand_request.get_order()
    # Проверяется, что код ответа равен 200
    assert response_get_order.status_code == 200

# Проверям, что заказ был успешно создан
def test_create_order_corect_data():
    check_status(data.order_body)
