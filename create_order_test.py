# Алёшинский Виктор, 20-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

def post_new_order(body):
    response_order=requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)
    track_number = response_order.json()['track']
    return track_number

def get_order():
    track_number = post_new_order(data.order_body)
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_STATUS , params={"t":track_number})

def check_status(body):
    response_get_order = get_order()
    # Проверяется, что код ответа равен 200
    assert response_get_order.status_code == 200

def test_create_order_corect_data():
    check_status(data.order_body)
