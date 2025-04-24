import requests

"""Отправка GET-запроса"""
def method_get(url):
    # Отправка GET-запроса
    print("Отправка GET-запроса по url: " + url)
    response = requests.get(url)
    # Проверка на статус-код
    print("Статус код: " + str(response.status_code))
    assert 200 == response.status_code
    # Получение данных ответа
    response_data = response.json()
    return response_data

"""Чтение файла и проверка на наличие имени"""
def read_file(name):
    with open('names.txt', 'r') as file:
        data_file = file.read()
        if name in data_file:
            return True
        else:
            return False

"""Запись в файл нового имени"""
def write_file(name):
    with open('names.txt', 'a', encoding='utf-8') as file:
        file.write(name + '\n')
        print("Внесено имя: " + name)

"""1. Очистка файла после последнего использования"""
with open('names.txt', 'w') as file:
    pass

"""2. Запрос данных о Дарт Вейдере"""
url = "https://swapi.dev/api/people/4/"
response_data = method_get(url)

"""3. Выделение фильмов, в которых снимался Дарт Вейдер"""
films = response_data.get('films')

"""4. Получение ID персонажей из фильмов"""
for film in films:
    response_data = method_get(film)
    peoples = response_data.get('characters')
    """5. Получение информации о персонажах"""
    for people in peoples:
        response_data = method_get(people)
        """6. Получение имени персонажа"""
        name = response_data.get('name')
        """7. Проверка, есть ли имя персонажа в файле"""
        flag = read_file(name)
        if flag == True:
            continue
        else:
            """8. Запись в файл нового персонажа"""
            write_file(name)

print("Запись имен в файл names.txt прошла успешно!")


