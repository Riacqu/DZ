'''Задание 1
Пользователь вводит с клавиатуры номер дня недели (1-7).
Необходимо вывести на экран названия дня недели.
Например, если 1, то на экране надпись понедельник, 2 - вторник и т.д.'''

# x = int(input("Введите номер дня недели от 1 до 7: "))

# if 0 != x == 1:
#     print('Понедельник')
# elif x == 2:
#     print('Вторник')
# elif x == 3:
#     print('Среда')
# elif x == 4:
#     print('Четверг')
# elif x == 5:
#     print('Пятница')
# elif x == 6:
#     print('Суббота')
# elif x == 7:
#     print('Воскресенье')
# else:
#     print('Некорректное значение. Пожалуйста, введите число от 1 до 7.')

'''Задание 2
Пользователь вводит с клавиатуры номер месяца (1-12). 
Необходимо вывести на экран название месяца.
Например, если 1, то на экране надпись январь, 2 — февраль и т.д. '''

# x = int(input("Введите номер дня недели от 1 до 12: "))
#
# if 0 != x == 1:
#     print('Январь')
# elif x == 2:
#     print('Февраль')
# elif x == 3:
#     print('Март')
# elif x == 4:
#     print('Апрель')
# elif x == 5:
#     print('Май')
# elif x == 6:
#     print('Июль')
# elif x == 7:
#     print('Июнь')
# elif x == 8:
#     print('Август')
# elif x == 9:
#     print('Сентябрь')
# elif x == 10:
#     print('Октябрь')
# elif x == 11:
#     print('Ноябрь')
# elif x == 12:
#     print('Декабрь')
# else:
#     print('Некорректное значение. Пожалуйста, введите число от 1 до 12.')

'''Задание 3
Пользователь вводит с клавиатуры число. 
Если число больше нуля нужно вывести надпись «Numberis positive»,
если меньше нуля «Number is negative», 
если равно  нулю «Number is equal to zero»'''

# x = int(input("Введите число: "))
#
# if x > 0:
#     print('«Numberis positive»')
# elif x < 0:
#     print('«Number is negative»')
# else:
#     print('«Number is equal to zero»')

'''Задание 4
Пользователь вводит два числа. 
Определить, равны ли эти числа, и, если нет, 
вывести их на экран в порядке возрастания.'''

x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

if x == y:
    print('Числа равны')
else:
    max = max(x, y)
    min = min(x, y)
    print("Числа в порядке возрастания", min, max)