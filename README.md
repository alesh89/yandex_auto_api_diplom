# Тесты на проверку параметра name при создании набора продуктов в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest

## Описание проекта
Проект содержит следующие файлы:
- configuration.py: URL и пути запросов;
- sender_stand_request.py: файл отправки запросов;
- data.py: файл с данными;
- create_kit_name_kit_test.py: файл с написанными тестами;
- README.md;
- .gitignore.

## Проверки выполнялись по следующему чек-листу:
| №                                                          | Описание | ОР      |
|-----------------------------------------------------------------------------|---------------|-------------------|
|   1                                                        | Допустимое количество символов (1): kit_body = {"name": "a"}  | Код ответа — 201. В ответе поле name совпадает с полем name в запросе      |
|   2                                                        | Допустимое количество символов (511): kit_body = {"name":"Тестовое значение для этой проверки будет ниже"}  | Код ответа — 201. >В ответе поле name совпадает с полем name в запросе   |
|   3                                                        | Количество символов меньше допустимого (0): kit_body = {"name": ""}  | Код ответа — 400   |
|   4                                                        | Количество символов больше допустимого (512): kit_body = {"name":"Тестовое значение для этой проверки будет ниже"} | Код ответа — 400   |
|   5                                                        | Разрешены английские буквы: kit_body = {"name": "QWErty"}  | Код ответа — 201. В ответе поле name совпадает с полем name в запросе   |
|   6                                                        | Разрешены русские буквы: kit_body = {"name": "Мария"}  | Код ответа — 201. В ответе поле name совпадает с полем name в запросе   |
|   7                                                        | Разрешены спецсимволы: kit_body = {"name": ""№%@","}  | Код ответа — 201. В ответе поле name совпадает с полем name в запросе   |
|   8                                                        | Разрешены пробелы: kit_body = {"name": " Человек и КО "}  | Код ответа — 201. В ответе поле name совпадает с полем name в запросе   |
|   9                                                        | Разрешены цифры: kit_body = {"name": "123"}  | Код ответа — 201. В ответе поле name совпадает с полем name в запросе   |
|   10                                                        | Параметр не передан в запросе: kit_body = {}  | Код ответа — 400   |
|   11                                                        | Передан другой тип параметра (число): kit_body = {"name": 123}  | Код ответа — 400   |

_Тестовые значения для проверок №2 и №4:_

Допустимое количество символов (511):

kit_body = {    "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"}

Количество символов больше допустимого (512):

kit_body = {  "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"}
# Правила запуска тестов

В файле create_kit_name_kit_test.py созданы функции, являющиеся вспомогательными для выполнения тестов.

## Функция для замены содержимого тела запроса
```sh
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body
```
## Функция для позитивной проверки
```sh
def positive_assert(name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)

    # Проверяется, что код ответа равен 201
    assert kit_response.status_code == 201
    # Проверяется, что возвращаемое имя равно имени, передаваемое в запросе
    assert kit_response.json()["name"] == name
```
## Функция для негативной проверки
```sh
def negative_assert_symbol(name):
    # В переменную kit_body сохраняется обновлённое тело запроса
    kit_body = get_kit_body(name)
    # В переменную kit_response сохраняется результат запроса на создание набора:
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    # Проверяется, что код ответа равен 400
    assert kit_response.status_code == 400
```

## Функция для негативной проверки (отсутствует имя)
```sh
def negative_assert_no_name(kit_body):
    # В переменную response сохраняется результат запроса на создание набора:
    response = sender_stand_request.post_new_client_kit(kit_body)
    # Проверяется, что код ответа равен 400
    assert response.status_code == 400
```
После описания данных функций расписаны тесты, позволяющие выполнить проверки по каждому пункту чек-листа. Каждый новый тест начинается с префикса test_ и в нем применяется та или иная функция, в зависимости от позитивности проверки.<br>
Все проверки можно увидеть в файле **[create_kit_name_kit_test.py](https://github.com/alesh89/yandex_api_stand_project10/blob/master/create_kit_name_kit_test.py)**.
