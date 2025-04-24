import base_person
import warrior
man = base_person.Person("Алекс", 30, 180)
man.description_person()
war = warrior.Warrior("Конан", 32, 200)
print("Нового человека зовут " + war.description_person())