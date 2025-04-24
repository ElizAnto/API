# Типы данных

# print("Hello, World!")
#
# int - целостные числа 5, 10, 200
# float - числа с плавающей запятой 5.5, 10.02
# str - строки "hello"
# boolean - булево значение true, false
#
# num_1 = 2
# num_2 = 5
# result = (num_1+num_2)
# res = bool(True)
# print(res)

# Числовые типы данных
# num_1 = 5
# print(num_1)
# print(type(num_1))
# num_1 = 10
# print(num_1)

# Строковый тип данных
# str_1 = "Hello"
# str_2 = "WORLD"
# print(str_1)
# print(dir(str_1))
# print(str_1.upper())
# print(str_1.title())
# print(str_2)
# print(str_2.lower())

# name = "Ivan"
# name = "Alex"
# a = "Hello {}"
# result = a.format(name)
# print(result)
#
# first_name = "Ivan"
# last_name = "Ivanov"
# a = '{} {}'
# print(a.format(first_name, last_name))
# result = a.format(first_name, last_name)
# print("Меня зовут: " + result)
#
# result = f'{first_name} {last_name}'
# print(result)

# F-String
# name = "Alex"
# age = 30
# # print("Меня зовут " + name + ", Мне " + str(age) + " лет")
# # print(f"Меня зовут {name}, Мне {age} лет")
# num_1 = 10
# num_2 = 20
# print(f"Сумма чисел равна {num_1 + num_2}")

# Функции
# num_1 = 10
# num_2 = 20
# def summ(num_1, num_2):
#     result =  num_1 + num_2
#     print(result)
#
# summ(20, 40)
# summ("Hello", "World")
#
# def hi(name):
#     print("Hello " + name)
#
# hi("Alex")
#
# def hi(name, age):
#     print("Меня зовут " + name + " мне " + age + " года")
#
# name = "Алекс"
# hi(name, "32")
#
# name = input()
# def hi(name, age):
#     print("Меня зовут " + name + " мне " + age + " лет")
# hi(name, "27")

# name = "Alex"
# age = "32"
# def hi(name, age):
#     result = name + " " + age
#     return result
#
# h = hi(name, age)
# print(h)

# var_1 = 100
# var_2 = 20
# def summ():
#     result = var_1 + var_2
#     print(result)
#
# def sub():
#     var_2 = 30
#     result = var_1 - var_2
#     print(result)

# summ()
# sub()

# Функции
# age = 24
# name = "Alex"
# if age == 25 or name == "Alex":
#     print("Мне 25 лет и меня зовут Alex")
# elif age > 25:
#     print("Мне больше 25 лет")
# else:
#     print("Мне меньше 25 лет")

# name = "Alex"
# if "A" in name:
#     print("Меня зовут Alex")
# else:
#     print("Меня не зовут Alex")

# pin = 1234
# print("Введите пожалуйста ваш pin-код")
# user_pin = int(input())
#
# if pin == user_pin:
#     print("Какую сумму вы хотите снять?")
# else:
#     print("Ошибка. Введите корректный pin-код, у вас осталось 2 попытки")
#     user_pin = int(input())
#     if pin == user_pin:
#         print("Какую сумму вы хотите снять?")
#     else:
#         print("Ошибка. Введите корректный pin-код, у вас осталась 1 попытка")
#         user_pin = int(input())
#         if pin == user_pin:
#             print("Какую сумму вы хотите снять?")
#         else:
#             print("Ошибка, Ваша карта заблокирована. Пожалуйста, обратитесь в банк.")

# # Списки
# personal = ["Alex", "Ivan", "Nasty", "Olga"]
# # print(personal[2])
# # result = personal[0] + " " + personal[2]
# # print(result + " - лучшая пара")
#
# # number = [1, 12, 23, 4]
# # print(number[2])
# # result_num = number[1] + number[3]
# # print(result_num)
# # num_1 = number[1]
# # print(num_1)
#
# # print(len(personal))
# # print(personal[-1])
# # print(personal[0:3])
# # print(personal[1:])
#
# personal.append("Fedor")
# print(personal)
#
# number = [1, 12, 23, 4]
# pn = []
# pn.append(personal)
# pn.append(number)
# print(pn)

# Циклы
# students = ["Alex", "Ivan", "Olga"]
# for f in students:
#     # var = "Инженер " + f
#     # print(var)
#     if f == "Olga":
#         var = "Инженер " + f
#         print(var)
# # for f in students[:2]:
# #     print(f)
# # for f in students[2:]:
# #     print(f)
# # for f in students[1:3]:
# #     print(f)
# for f in students:
#     print(len(f))

# while
# a = 10
# while a > 1:
#     print(a)

# a = 10
# while a >= 1:
#     a -= 1
#     print(a)

# break continue
# list = [1, 4, 6, 10, 12]
# for i in list:
#     if i == 6:
#         print("Ура 6")
#         break
#     print(i)
#
# login = input("Введите ваш логин: ")
# while True:
#     if login == "Alex":
#         print("Вы ввели верный пароль")
#         password = input("Введите ваш пароль: ")
#     else:
#         print("Вы ввели некорректный логин")

# list = [1, 4, 6, 8, 10, 12]
# for i in list:
#     if i == 10:
#         print("Плохо 10")
#         break
#     elif i == 4:
#         print("Ура 4")
#
#     elif i == 6:
#         print("Ура 6")
#         continue
#     print(i)

# numbers = list(map(int, input().split()))
# i = 0
# while i < len(numbers):
#     if numbers[i] > 7:
#         print(numbers[i])
#         i += 1

# numbers = list(map(int, input().split()))
# summer = 0
# for num in numbers:
#     if num < 0:
#         break
#     summer += num
# print(summer)
#
# numbers = list(map(int, input().split()))
#
# total = 0
# for num in numbers:
#     if num < 0:
#         break
#     total += num
#
# print(total)

# Работа с файлами

# Запись
# var = input("Напиши что-нибудь : ")
# fw = open('doc/file.txt', 'a')
# # fw.write("Hello world\n")
# fw.write(var)
# fw.close()

# a - запись новых данных в файл и помещение новых данных в конец файла
# w - запись новых данных, но с удалением старых
# r - чтение данных

# fw = open('doc/file2.txt', 'w')
# fw.write("privet!!!")
# fw.close()

# Чтение
# fr = open('doc/file.txt', 'r')
# text = fr.read()
# fr.close()
# print(text)

# Или портативнее:
import os

fw = open(f"{os.getcwd()}/doc_file.txt", 'a')
fw.write("hello\n")
fw.close()

fr = open(f"{os.getcwd()}/doc_file.txt", 'r')
text = fr.read()
fr.close()

print(text)
