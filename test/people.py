# Родительский класс
class Person():
    """Создаем человека"""
    def __init__(self, name, age, height):
        """Инициализируем атрибуты человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описания человека"""
        description = self.name + ", ему " + str(self.age) + ", его рост " + str(self.height) + ", его вес " + str(self.weight)
        print("Нового человека зовут " + description)

    def get_weight(self):
        """Получение веса человека"""
        print("Вес нашего человека: " + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg

# man = Person("Алекс", 30, 180)
# # man.description_person()
# # # Первый способ смены веса
# # man.weight = 110
# # Второй способ
# man.update_weight(110)
# man.get_weight()

# Класс - наследник (воин)
class Warrior(Person):
    """Создаем класс воина"""
    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height) # Настраиваем связь метода init потомка с методом init родителя
        self.rage = 100 # Ярость

    def get_rage(self):
        """Получение заряда ярости"""
        print("Заряд ярости равен: " + str(self.rage))

    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + ", ему " + str(self.age) + ", его заряд ярости " + str(self.rage)
        # print("Нового человека зовут " + description)
        return description

warrior = Warrior("Конан", 32, 200)
# warrior.description_person()
# warrior.update_weight(150)
print("Нового человека зовут " + warrior.description_person())
# warrior.description_person()
# warrior.get_rage()

