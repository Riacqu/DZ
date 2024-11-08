'''Задание 1
Пользователь вводит с клавиатуры арифметическое выражение.
Например, 23+12. Необходимо вывести на экран результат выражения.
В нашем примере это 35.
Арифметическое выражение может состоять только из трёх частей: число, операция, число.
Возможные операции: +, -,*,/'''

# x = input("Пожалуйста, введите выражение с только использованием операторов +, -, *, или / (например, 23+12): ")
# operators = ['+', '-', '*', '/']
# y = 0
# for i in operators:
#     if i in x:
#         y = i              # Находим оператор в выражении
#         break
# if y:                      # Если нашли оператор
#     n1, n2 = x.split(y)    # Разбиваем строку на два операнда по найденному оператору
#     n1 = int(n1)           # Преобразуем первый операнд в целое число
#     n2 = int(n2)           # Преобразуем второй операнд в целое число
#     if y == '+':
#         r = n1 + n2        # Сложение
#     elif y == '-':
#         r = n1 - n2        # Вычитание
#     elif y == '*':
#         r = n1 * n2        # Умножение
#     elif y == '/':
#         r = n1 / n2        # Деление
#     else:
#         r = "Введите корректное выражение"
#
#     print("Результат введенного выражения", x, "=", r)
# else:
#     print("Введите корректное выражение")

'''Задание 2
В списке целых, заполненном случайными числами, определить минимальный и максимальный элементы,
посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать количество нулей.
Результаты вывести на экран.'''

import random                       # Импорт модуля random для генерации случайных чисел
x = []                              # Создаем пустой список для хранения случайных чисел
for i in range(10):                 # Генерируем и добавляем 10 случайных целых чисел в диапазоне от -70 до 100 в список x
    r = random.randint(-70, 100)
    x.append(r)
min = min(x)                        # Находим минимальное  число в списке x
max = max(x)                        # Находим максимальное число в списке x

minus = 0       # Переменная для подсчета отрицательных чисел
plus = 0        # Переменная для подсчета положительных чисел
zero = 0        # Переменная для подсчета нулей

for y in x:
    if y < 0:
        minus += 1      # Перебираем числа в списке x и подсчитываем количество отрицательных чисел
    elif y > 0:
        plus += 1       # Перебираем числа в списке x и подсчитываем количество положительных чисел
    else:
        zero += 1       # Перебираем числа в списке x и подсчитываем количество нулей

print("Список случайных чисел:", x)
print("Минимальное число в списке: ", min)
print("Максимальное число в списке: ", max)
print("Количество отрицательных чисел в списке: ", minus)
print("Количество положительных чисел в списке: ", plus)
print("Количество нулей в списке: ", zero)

