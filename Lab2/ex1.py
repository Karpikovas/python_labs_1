from math import *


def get_float_value(msg):
    value = input(msg)
    func = lambda a: float(a) if a.isdigit() else print('Ошибка')
    return func(value)


func = lambda x, y, n: pow(sin(pow(x, n) + pow(y, 1 / n)) + pow((exp(pow(x, 4)) / cos(y)), 1 / 3), 1 / 5)


x = get_float_value('Введите значение x: ')
y = get_float_value('Введите значение y: ')
n = get_float_value('Введите значение n: ')

calculate_func = lambda x, y, n: func(x, y, n) if exp(pow(x, 4)) / cos(y) > 0 and y > 0 else 'Ошибка'

print('Результат вычисления = ', calculate_func(x, y, n))