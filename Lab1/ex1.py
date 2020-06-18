from math import *


def get_float_value(msg):
    while True:
        try:
            value = float(input(msg))
        except ValueError:
            print('Значение должно быть типа float!')
        else:
            break
    return value


def calculate_func(x, y, n):
    return pow(sin(pow(x, n) + pow(y, 1 / n)) + pow((exp(pow(x, 4)) / cos(y)), 1 / 3), 1 / 5)


while True:
    x = get_float_value('Введите значение x: ')
    y = get_float_value('Введите значение y: ')
    n = get_float_value('Введите значение n: ')

    if y > 0:
        print('Результат вычисления = ', calculate_func(x, y, n))
    else:
        print('Ошибка')


    flag_continue = input('Чтобы продолжить введите "да": ')

    func = lambda x: True if x % 2 == 0 else False
    if flag_continue == "да":
        continue
    else:
        break
