from utils.http_methods import HttpMethod

"""Методы для тестирования Google Maps API"""

base_url = "https://rahulshettyacademy.com" # Базовая URL
key = "?key=qaclick123" # Параметр для всех запросов, ? - обозначение параметр

class GoogleMapsAPI():

    """Метод для создания новой локации"""
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
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

        post_resource = "/maps/api/place/add/json" # Ресурс метода POST
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethod.post(post_url, json_for_create_new_place)
        print(result_post.json())
        return result_post