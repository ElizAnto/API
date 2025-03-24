from utils.api import GoogleMapsAPI

"""Создание, изменение и удаление новой локации"""

class TestCreatePlace():

    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_place()  # Вызов метода по созданию новой локации
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Метод GET POST")
        result_get = GoogleMapsAPI.get_new_place(place_id)  # Вызов метода для проверки новой локации
