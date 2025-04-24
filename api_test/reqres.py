import requests
import json

# URL для отправки запроса
url = "https://swapi.dev/api/people/4/"

# Тело запроса
json_post = [
    {
        "email": "peter@klaven"
    }
]

json_put = [
    {
        "name": "morpheus",
        "job": "zion resident"
    }
]

# # Отправка POST-запроса
# response = requests.post(url, json=json_post)

# Отправка GET-запроса
response = requests.get(url)

# # Отправка PUT-запроса
# response = requests.put(url, json=json_put)

# # Отправка DELETE-запроса
# response = requests.delete(url)

# # Получение данных из ответа
response_data = response.json()
print(response_data)
#
# check = response.json()
# check_info = check.get('message')
# summer = 0
# for i in check_info:
#     if "hound-english" in i:
#         summer += 1
# print(summer)

# # Статус-код ответа
# status_code = response.status_code

# # Количество символов значения поля token:
# token = len(response_data['token'])

# # Тип данных поля id
# id_type = type(response_data['id']).__name__
#
# # Первые 4 символа значения поля createdAt
# created_at_first_4 = response_data['createdAt'][:4]
#
# # Вывод значений
# print(f"Статус-код: {status_code}")
# print(f"Тип данных поля id: {id_type}")
# print(f"Первые 4 символа значения поля createdAt: {created_at_first_4}")

print(f"Статус-код: {status_code}")
# print("Длина токена: " + str(token))