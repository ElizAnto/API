from utils.api import GoogleMapsAPI

"""Создание, изменение и удаление новой локации"""

class TestCreatePlace():

    def test_create_new_place(self):
        print("Метод POST")
        result_post = GoogleMapsAPI.create_new_place()  # Вызов метода по созданию новой локации
