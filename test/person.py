class Person():
    """Модель человека"""
    def __init__(self, name, age):
        """Инициализация атрибутов человека - имя, возраст"""
        self.name = name
        self.age = age
        print("Человек создан")

    def sing(self):
        """Просим человека спеть"""
        print(self.name + " поет")

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + " танцует")

man = Person("Алекс", 30)
# print(man.name)
woman = Person("Nasty", 28)

man.dance()
woman.sing()