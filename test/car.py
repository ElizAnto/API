"""Первая часть задания"""

class Car():
    """Создаем класс машины"""
    def __init__(self, model, year, capacity, price, mileage):
        """Инициализируем атрибуты машины"""
        self.model = model
        self.year = year
        self.capacity = capacity
        self.price = price
        self.mileage = mileage
        self.wheels = 4

    def description(self):
        """Описание машины"""
        description = (
            f"Модель машины - {self.model}, год выпуска - {self.year}, объем двигателя - {self.capacity} л., цена - {self.price} руб., пробег - {self.mileage} км, количество колес - {self.wheels} шт.")
        return description

kia = Car("Kia Rio III", 2016, 1.6, 1_000_000, 83_000)
print("Опубликован новый автомобиль: " + kia.description())

"""Вторая часть задания"""

class Truck(Car):
    """Создаем класс грузовика"""
    def __init__(self, model, year, capacity, price, mileage):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(model, year, capacity, price, mileage) # Настраиваем связь метода init потомка с методом init родителя
        self.wheels = 8 # Колеса

    def description(self):
        """Описание грузовика"""
        description = (
            f"Модель грузовика - {self.model}, год выпуска - {self.year}, объем двигателя - {self.capacity} л., цена - {self.price} руб., пробег - {self.mileage} км, количество колес - {self.wheels} шт.")
        return description

truck = Truck("Scania P-series", 2019, 12.7, 8_800_000, 311_600)
print("Опубликован новый грузовик: " + truck.description())