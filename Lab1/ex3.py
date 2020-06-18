menu = '''
    R - площаль прямоугольного треугольника;
    Т - площаль трапеции;
    S - площадь квадрата;

    E. Выход.
'''
def get_float_value(msg):
    while True:
        try:
            value = float(input(msg))
        except ValueError:
            print('Значение должно быть типа float!')
        else:
            break
    return value

while True:
    print(menu)

    command = input('Введите команды: ')

    if command == "R":
        a = get_float_value('Введите длину катета а: ')
        b = get_float_value('Введите длину катета b: ')

        print('Площадь прямоугольного треугольника = ', 0.5 * a * b)


    elif command == "T":
        a = get_float_value('Введите длину основания а: ')
        b = get_float_value('Введите длину основания b: ')
        h = get_float_value('Введите длину высоты h: ')

        print('Площадь трапеции = ', 0.5 * (a + b) * h)


    elif command == "S":
        a = get_float_value('Введите длину стороны a: ')

        print('Площадь квадрата = ', a * a)


    elif command == "E":
        exit(0)

    else:
        print('Неверная команда')