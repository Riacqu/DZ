'''Задание 1
Пользователь вводит с клавиатуры три цифры. Необходимо создать число, содержащее эти цифры.
Например, если с клавиатуры введено 1, 5, 7, тогда нужно сформировать число 157.'''

# x1 = input("Введите первую цифру: ")
# x2 = input("Введите вторую цифру: ")
# x3 = input("Введите третью цифру: ")
# x = x1+x2+x3
# y = int(x)
# print('Сформированное число =', y)

'''Задание 2
Пользователь вводит с клавиатуры число, состоящее из четырех цифр. 
Требуется найти произведение цифр. 
Например, если с клавиатуры введено 1324, тогда результат произведения 1*3*2*4 = 24'''

# x = int(input('Введите четырёхзначное число: '))
# y1 = x // 1000
# y2 = x // 100 % 10
# y3 = x // 10 % 10
# y4 = x % 10
# print('Произведение цифр из числа', x, '=' ,(y1 * y2 * y3 * y4))



'''Задание 3
Пользователь вводит с клавиатуры количество метров. 
Требуется вывести результат перевода метров в сантиметры, 
дециметры, миллиметры, мили.'''

# meters = float(input("Введите количество метров: "))
#
# centimeters = meters * 100
# decimeters = meters * 10
# millimeters = meters * 1000
# miles = meters * 0.000621371
#
# print("метров       -", meters)
# print("сантиметров  -", centimeters)
# print("дециметров   -", decimeters)
# print("миллиметров  -", millimeters)
# print("миль         -", miles)

'''Задание 4
Напишите программу, вычисляющую площадь треугольника. 
Пользователь с клавиатуры вводит размер основания треугольника и размер высоты.'''

# a = float(input("Введите размер основания треугольника (в метрах): "))
# h = float(input("Введите размер высоты треугольника (в метрах): "))
#
# S = 0.5 * a * h
#
# print("Площадь треугольника с основанием", a, "м и высотой", h, "м равна", S, "квадратных метров.")

'''Задание 5
Пользователь с клавиатуры вводит четырёхзначное число. 
Необходимо перевернуть число и отобразить результат. 
Например, если введено 4512, результат 2154.'''

x = int(input('Введите четырёхзначное число: '))
y1 = x % 10
y2 = x // 10 % 10
y3 = x // 100 % 10
y4 = x // 1000
x1 = str(y1)+str(y2)+str(y3)+str(y4)
g = int(x1)
print('Число в обратном порядке из', x, '=', g)