import requests

base_url = "https://rahulshettyacademy.com"  # Базовая URL
key = "?key=qaclick123"  # Параметр для всех запросов

class TestNewLocation():

    """Работа с новой локацией"""

    def test_create_new_location(self, i):

        """Создание новой локации"""

        post_resource = "/maps/api/place/add/json" # Ресурс метода post
        post_url = base_url + post_resource + key
        print("Создание локации №" + str(i) + ", URL для метода POST: " + post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)

        print("Статус код: " + str(result_post.status_code))
        assert 200 == result_post.status_code
        print("Успешно! Создана новая локация")

        check_post = result_post.json()
        check_info_post = check_post.get("status")
        print("Статус код ответа: " + check_info_post)
        assert check_info_post == "OK"
        print("Статус ответа верен")
        place_id = check_post.get("place_id")
        print("Place_id: " + place_id)

        """Запись в файл place_id новой локации"""

        places = open('place_id.txt', 'a')
        places.write(place_id + '\n')
        places.close()

    def test_get_new_location(self, i):

        """Чтение place_id локации из файла"""

        places = open('place_id.txt', 'r')
        place_ids = places.readlines()
        place_id = place_ids[i - 1].strip()
        places.close()

        """Проверка создания новой локации"""

        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print("Проверка создания локации №" + str(i) + ", URL для метода GET: " + get_url)
        result_get = requests.get(get_url)
        print(result_get.text)

        print("Статус код: " + str(result_get.status_code))
        assert 200 == result_get.status_code
        print("Успешно! Проверка создания новой локации прошла успешно")
        print("Place_id: " + place_id)

new_place = TestNewLocation()

"""Очистка файла после последнего использования"""

place = open('place_id.txt', 'w')
place.close()

"""Создание 5 локаций с записью place_id в файл"""

for i in range(1, 6):
    new_place.test_create_new_location(i)

"""Чтение 5 place_id из файла с проверкой их существования"""

for i in range(1, 6):
    new_place.test_get_new_location(i)

print("Тестирование TestNewLocation завершено успешно")