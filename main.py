
# print("Hello world!!!", 1, 2, 3, sep="|", end="\n") - print выводит текст в консоль
# # print("Hello world!!!", 4, 5, 6, sep="|")
# print (10.1%5)   //  аргумент sep вполняет разделение каким-то символом в выводе

# input("Please input some text") -  функция input приостнавливает выполнение кода до ввода какого-то
# дополнительного текста или кода

# name = input("Please input your name")
# print(name)

# namex = "Vasia"
# namey = "Petia"
# namex, namey = namey, namex
# print(namex, namey)
# можно поменять местами присваивание


# variable = "1"
# print(type(variable))
# type - выводит тип данных в консоль


                                       # INFO
# snake_case - имена переменных, функций, методов модулей
#
# CamelCase - имена классов
#
# yet-another-package - названия пакетов
#
# CONST - константы


# my_int = 1
# my_float = float(my_int)
# print(my_float)
#
# аргумент float изменил цифру 1 и перевел в тип float при выводе в консоль



# my_float = 1.788
# my_int = int(my_float)
# print(my_int)
#
# # аргумент int изменил цифру 1.788 и перевел в тип int при выводе в консоль, просто обрезав все, что после запятой



# my_float = 1.788
# my_int = round(my_float)
# print(my_int)
#
# аргумент round изменил цифру 1.788 и округлил число в тип int при выводе в консоль


# first Home_work - 16m 45s

# flatNumber = int(input("Please input flat number"))
# entrance_number =(flatNumber - 1) // 20 + 1
# flat_entrance = (flatNumber - 1) % 20 + 1
# floor_number = (flat_entrance - 1) // 4 + 1
#
# print(f"Квартира № {flatNumber} находится на {floor_number} этаже, в {entrance_number} подъезде.")


                                           # сравнение данных

# x = 10
# y = 11
# print(x == y)

# x = 11
# y = 12
# not_equal = x != y
# print(not_equal)



# !=     не равно
# >      больше
# <      меньше
# >=     больше либо равно
# <=     меньше либо равно


# x = 2
# print(x < 1 or x > 1)


# x = 10
# if not x > 20:
#     print("x не больше 20")
# if not x < 20:
#     print("x меньше 20")


# is_active = False
# if not is_active:
#     print("Аккаунт не активен")


                                         # УСЛОВНЫЕ ОПЕРАТОРЫ

# проверка с одной переменной
#
# x = 0.09
# if x > 0:
#     print("X больше 0")
# elif x == 0:
#     print("x равно 0")
# else:
#     print("x меньше нуля")



# проверка с двумя переменными
#

# x = 0.09
# y = 1
# if x > 0 and y <= 0:
#     print("X и Y подходят по условиям")
# elif x > 0 and y < 0:
#     print("X и Y не подходят по условиям")
# else:
#     print("попробуйте ввести другие данные")




# проверка с текстовыми данными, пустое ли значение

# message = ""
# if message:
#     print("Привет!!!")
# else:
#     print("Сообщение пустое! Пожалуйста создай сообщение!")



                                                    # СТРОКИ

# first_name = "Alice"
# second_name = "Smith"
# full_name = first_name + "   " + second_name
# print(full_name)
#
# # длина строки
# length = len(full_name)
# print(length)


# перевод с int на str

# my_integer = 100
# my_string = str(my_integer)
# print(type(my_string))



# перевод с str на int

# my_str = "100"
# my_integer = int(my_str)
# print(type(my_integer))



# меняет стрингу на цифру при вводе текста
# my_string = int(input("Enter a number:"))
# print(type(my_string))


# считаем кол-во цифр в большом числе с помощью функции len, для этого
# переводим цифры в строку

# my_big_number = 2 ** 10000
# print(my_big_number)
# print(len(str(my_big_number)))


# поиск, входит ли определеный текст в коде при помощи оператора "in"

# my_code = "England - Switzerland"
# print("Englank" in my_code)


# Различные методы

# метод upper или lower позволяет перевести строку в большие или маленькие буквы

# my_string = "daniel"
# print(my_string.upper())
#
# my_string = "DASHA"
# print(my_string.lower())



# уменьшение (обрезание) лишних пробелов, метод "strip"

# message = "      My text   !!!!    "
# print(len(message))
# print(len(message.strip()))
# print(message.strip())


# замена одного текста на другой. Метод "replase"

# message = "Netherlands - the champion of Euro 2024!!!"
# print(message.replace("Netherlands", "Spain"))



# подсчет кол-ва символов в строке. Метод "count"

# message = "Netherlands - the champion of Euro 2024!!!"
# print(message.count("e"))



# проверка типа введенного текста. Метод "isdigit"
#
# message = input("Enter number: ")
# if message.isdigit():
#     message = int(message)
#
# print(type(message))


                                                  # ФОРМАТИРОВАНИЕ

# метод "f"

# name = "Viacheslav"
# age = 45
# print(f"Hello, my name is {name} and I am {age} years old")


# my_string = input("Enter a number: ")
# if my_string.isdigit():
#     my_integer = int(my_string)
#     print(f"{my_string} is accepted")
# else:
#     print(f"{my_string} is not a number")



# new_string = "I love {} {} and watch {}."                 #2 {} заменителя
# print(new_string.format("red", "oranges", "football"))


# или при помощи индексов, начиная с "0"
# print("Tom is a {3}, {2}, and {1} {0}!".format("happy", "smiling", "tall", "man"))


# Кроме позиционных аргументов существуют также именованные аргументы. Эти аргументы можно вызвать по имени. Например:
# print("Tom {pr} {1} a {0}.".format("has", "made", pr = "pull request"))




# В фигурные скобки можно добавить больше параметров. Попробуйте использовать синтаксис {field_name:conversion}, где field_name задаёт индекс аргумента метода str.format(), а conversion – тип данных с помощью односимвольного кода, который использует Python. Здесь мы используем такой код:
#
# s – строки (string)
# d – десятичные числа (decimal)
# f – число с плавающей точкой (float)
# Попробуйте передать с помощью метода целое число как число с плавающей точкой, добавив тип f.

# print("Sam ate {0:f} percent of a {1}!".format(75, "pizza"))


# Пример форматирования через "%"
# name = "Alice"
# age = 30
# formatted_string = "Hello, my name is %s and I am %d years old." % (name, age)
# print(formatted_string)