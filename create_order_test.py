# Алёшинский Виктор, 20-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import sender_request
import data

def check_status(body):
    track_number = sender_request.post_new_order(data.order_body)
    response_get_order = sender_request.get_order(track_number)
    # Проверяется, что код ответа равен 200
    assert response_get_order.status_code == 200

def test_create_order_corect_data():    
    check_status(data.order_body)