'''Задание 1
Пользователь вводит с клавиатуры число. Необходимо проверить его на четность и нечетность.
Если число четное требуется вывести на экран число и надпись Evennumber.
Если число нечетное выведите на экран число и надпись Odd number.'''

number = int(input('Введите число: '))
if number % 2 == 0:
    print('Even number')
else:
    print('Odd number')

'''Задание 2
Пользователь вводит с клавиатуры число. Необходимо проверить его на кратность 7. 
Если число кратно требуется вывести на экран число и надпись Number is multiple 7. 
Если число не кратно выведите на экран число и надпись Number is not multiple 7.'''

number = int(input('Введите число: '))
if number % 7 == 0:
    print('Number is multiple 7')
else:
    print('Number is not multiple 7')