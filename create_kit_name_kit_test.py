# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Функция для позитивной проверки
def positive_assert(name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    auth_token = sender_stand_request.post_new_user(data.user_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

# Функция для негативной проверки
def negative_assert_symbol(name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    auth_token = sender_stand_request.post_new_user(data.user_body)
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400

# Функция для негативной проверки (отсутствует имя)
def negative_assert_no_name(kit_body):
    # В переменную response сохраняется результат запроса на создание набора:
    auth_token = sender_stand_request.post_new_user(data.user_body)
    response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    # Проверяется, что код ответа равен 400
    assert response.status_code == 400

# Тест 1. Допустимое количество символов (1)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

# Тест 2. Допустимое количество символов (511)
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#Тест 3. Количество символов меньше допустимого (0)
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_no_name(kit_body)

#Тест 4. Количество символов больше допустимого (512)
def test_create_kit_512_letter_in_name_get_success_response():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Тест 5. Разрешены английские буквы
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Тест 6. Разрешены русские буквы
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Тест 7. Разрешены спецсимволы
def test_create_kit_name_has_special_symbol_get_success_response():
    positive_assert('"№%@",')

# Тест 8. Разрешены пробелы
def test_create_kit_name_has_space_get_success_response():
    positive_assert(" Человек и КО ")

# Тест 9. Разрешены цифры
def test_create_kit_name_has_numbers_get_success_response():
    positive_assert("123")

# Тест 10. Параметр name не передан в запросе
def test_create_user_no_name_kit_get_error_response():
    kit_body = data.kit_body.copy()
    # Удаление параметра name из запроса
    kit_body.pop("name")
    # Проверка полученного ответа
    negative_assert_no_name(kit_body)

#Тест 11. Передан другой тип параметра (число)
def test_create_number_type_name_kit_get_error_response():
    kit_body = get_kit_body(12)
    auth_token = sender_stand_request.post_new_user(data.user_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    assert kit_response.status_code == 400
