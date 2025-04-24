import requests

def user_input() -> str:
    answer = input("Напишите категорию, на которую вы хотели бы получить шутку.\n")
    return answer

class TestNewJoke():
    """Создание новой шутки"""

    def test_get_categories_joke(self):

        """Получение списка тем с шутками"""

        print("Получение списка тем с шутками\n")

        url_categories = "https://api.chucknorris.io/jokes/categories"
        print(url_categories)
        result = requests.get(url_categories)

        print("Статус код: " + str(result.status_code))
        assert 200 == result.status_code
        print("Успешно! Получен список категорий")

        categories = result.json()
        print(categories)
        return categories

    def test_category_in_categories(self, category, categories):
        try:
            assert category in categories
            print(f"Категория '{category}' есть в списке шуток!")
        except AssertionError:
            print("Вы ввели категорию, которой нет в списке!")
            exit()

    def test_get_random_jokes_category(self, category):

        """Получение случайной шутки на тему"""

        print(f"\nПолучение случайной шутки на тему {category}")

        url = f"https://api.chucknorris.io/jokes/random?category={category}"
        print(url)

        result = requests.get(url)
        print("Статус код: " + str(result.status_code))
        assert 200 == result.status_code
        print("Успешно! Получена новая шутка")

        # Ответ на запрос
        print(f"Ответ: {result.text}")

        check = result.json()
        # Шутка из ответа
        joke_value = check.get("value")
        print(f"Шутка: {joke_value}")

        check_info = check.get("categories")
        print(f"Проверка категории: {check_info}")

        assert category in check_info
        print(f"Категория '{category}' верна")


joke = TestNewJoke()
# Получаем от пользователя название категории
category = user_input()
# Получаем список тем
categories = joke.test_get_categories_joke()
# Проверка наличия темы
joke.test_category_in_categories(category, categories)
# Получаем шутку по теме
joke.test_get_random_jokes_category(category)
