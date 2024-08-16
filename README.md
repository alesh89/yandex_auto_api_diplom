# Финальный проект. Практический блок: часть вторая

### Задание 1.
Выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). 
```
SELECT c.login,COUNT(o.id) AS delivery 
FROM "Couriers" as c 
INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery"='t' 
GROUP BY c.login;
```

### Задание 2.
Выведи все трекеры заказов и их статусы. 
```
SELECT track,
        CASE 
            WHEN finished = 't' THEN '2' 
            WHEN cancelled = 't' THEN '-1' 
            WHEN "inDelivery" = 't' THEN '1' 
            ELSE '0' 
        END AS status
FROM "Orders"; 
```

### Задание 3. Автоматизация теста к API

##### Тесты на проверку создания заказа в  API Яндекс.Самокат.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest

##### Описание проекта
Проект содержит следующие файлы:
- configuration.py: URL и пути запросов;
- data.py: файл с данными;
- create_order_test.py: файл с написанными тестами;
- README.md;
- .gitignore.

##### Функция для создания заказа
```sh
def post_new_order(body):
    response_order=requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)
    track_number = response_order.json()['track']
    return track_number
```
##### Функция для запроса информации о созданном заказе
```sh
def get_order(track_number):    
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_STATUS , params={"t":track_number})
```
##### Автотест проверки создания заказа
```sh
def test_create_order_corect_data():    
    track_number = sender_request.post_new_order(data.order_body)
    response_get_order = sender_request.get_order(track_number)
    # Проверяется, что код ответа равен 200
    assert response_get_order.status_code == 200
```

##### Результат выполнения теста
![Диплом  Результат теста](https://github.com/user-attachments/assets/e7640348-55da-4eac-a396-49eba3d7c9fb)


