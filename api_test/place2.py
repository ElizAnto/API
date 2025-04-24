import requests

base_url = "https://rahulshettyacademy.com"  # Базовая URL
key = "?key=qaclick123"  # Параметр для всех запросов

class TestNewLocation():

    """Работа с локацией"""

    def test_delete_new_location(self, i):

        """Чтение place_id локации из файла"""

        places = open('place_id.txt', 'r')
        place_ids = places.readlines()
        place_id = place_ids[i - 1].strip()
        places.close()

        """Удаление локации"""

        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print("Удаление локации №" + str(i) + ", URL для метода POST: " + delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = requests.delete(delete_url, json=json_for_delete_new_location)
        print(result_delete.text)

        print("Статус код: " + str(result_delete.status_code))
        assert 200 == result_delete.status_code
        print("Успешно! Удаление локации прошло успешно")

        check_status = result_delete.json()
        check_status_info = check_status.get("status")
        print("Сообщение: " + check_status_info)
        assert check_status_info == "OK"
        print("Сообщение верно")

    def test_get_new_location(self, i):

        """Чтение place_id локации из файла"""

        places = open('place_id.txt', 'r')
        place_ids = places.readlines()
        place_id = place_ids[i - 1].strip()
        places.close()

        """Проверка существования локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print("Проверка существования локации №" + str(i) + ", URL для метода GET: " + get_url)
        result_get = requests.get(get_url)
        print(result_get.text)

        print("Статус код: " + str(result_get.status_code))
        try:
            assert 200 == result_get.status_code
            print("Успешно! Проверка существования локации прошла успешно")

            """Запись в файл place_id2 существующей локации"""

            places = open('place_id2.txt', 'a')
            places.write(place_id + '\n')
            places.close()

        except AssertionError:
            print("Локации не существует!")

new_place = TestNewLocation()

"""Очистка файла после последнего использования"""

place = open('place_id2.txt', 'w')
place.close()

"""Удаление локаций"""

new_place.test_delete_new_location(2)
new_place.test_delete_new_location(4)

"""Запуск 5 тестов"""

for i in range(1, 6):
    new_place.test_get_new_location(i)

print("Тестирование TestNewLocation завершено.")