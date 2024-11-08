'''Задание 1
Пользователь вводит с клавиатуры строку.
Проверьте является ли введенная строка палиндромом.
Палиндром - слово или текст, которые одинаково читаются слева направо и справа налево.
Например, кок; А роза упала на лапу Азора; доход; А буду я у дуба.'''

# x = input("Введите Вашу строку: ")
# y = ''.join(x.split())              # Удаление пробелов из введенной строки
# r = y.lower()                       # Приведение строки к нижнему регистру для сравнения без учета регистра
# if r == r[::-1]:                    # Сравниваем строку с обратной строкой, чтобы определить, является ли она палиндромом
#     print("Введенная Вами строка является палиндромом.")
# else:
#     print("Введенная Вами строка не является палиндромом.")

'''Задание 2
Пользователь вводит с клавиатуры некоторый текст, 
после чего пользователь вводит список зарезервированных слов. 
Необходимо найти в тексте все зарезервированные слова и изменить их регистр на верхний. 
Вывести на экран измененный текст.'''

# x = input("Введите Ваш текст: ")
# y = input("Введите список зарезервированных слов через пробел: ").split()
# c = x.split()                            # Разделяем введенный текст и список зарезервированных слов на отдельные слова
#
# for i in range(len(c)):                  # Проходим по каждому слову в тексте
#     if c[i] in y:                        # Если слово присутствует в списке зарезервированных слов...
#         c[i] = c[i].upper()              # ...преобразуем это слово в верхний регистр
#
# text = ' '.join(c)                       # Объединяем измененные слова обратно в предложение
# print("Ваш измененный текст: ", text)

'''Задание 3
Есть некоторый текст. 
Посчитайте в этом тексте количество предложений и выведите на экран полученный результат. '''

text = input("Введите Ваш текст: ")
y = False                       # Флаг для проверки наличия текста с буквами

for i in text:                  # Проверяем каждый символ в тексте
    if i.isalpha():             # Проверяем, является ли символ буквой
        y = True                # Если находим букву, устанавливаем флаг в True
        break                   # Прерываем цикл, если нашли хотя бы одну букву

if y:              # Если есть текст с буквами
    c = text.count('.') + text.count('!') + text.count('?')     # Считаем количество знаков препинания в тексте

    if c != 0:     # Если найдены знаки препинания
        print("Количество предложений в тексте:", c)
    else:
        print("Отсутствуют знаки препинания в тексте. Пожалуйста, введите текст, содержащий предложения.")
else:
    print("Просьба использовать грамотность, включая буквы и знаки препинания, при вводе текста. Введите текст корректно.")
