menu = '''
    1. Вывести список;
    2. Добавить элемент;
    3. Удалить элемент;
    4. Нечетные позиции списка;
    5. Произведение вещественных элементов списка;
    6. Количество арифметическиъ операций;
    7. Пересечение множеств;
    8. Вывести словарь;
    
    0. Выход.
'''
list_of_elements = [1, 'два', 3.0, 4, 'пять', 6.0, '+-/**']

def get_typed_variable(value, type):
    if type == 'int':
        return int(value)
    elif type == 'float':
        return float(value)
    else:
        return value

while True:
    print(menu)

    command = int(input('Введите команду: '))

    # показать значения списка на экране;

    if command == 1:
        print(list_of_elements)

    # добавление нового элементов в конец списка(добавлять элементы разных типов);

    elif command == 2:
        value = input('Введите новый элемент: ')
        value_type = input('Введите тип нового элемента (int, str, float): ')
        list_of_elements.append(get_typed_variable(value, value_type))

    # удаление указанного пользователем элемента из списка;

    elif command == 3:
        value = input('Введите удаляемый элемент: ')
        value_type = input('Введите тип удаляемого элемента (int, str, float): ')
        list_of_elements.remove(get_typed_variable(value, value_type))

    # сформировать кортеж, состоящий из элементов, стоящих на нечетных позициях списка;
    # вывести содержимое кортежа на экран;

    elif command == 4:
        print(tuple(list_of_elements[1::2]))

    # найти произведение всех вещественных элементов списка;

    elif command == 5:

        float_list = []
        for item in list_of_elements:
            if isinstance(item, float):
                float_list.append(item)


        result = 1
        for item in float_list:
            result *= item

        print(result)

    # сформировать строку из значений элементов списка и посчитать количество
    # арифметических операций в строке;

    elif command == 6:
        str_list = []
        for item in list_of_elements:
            str_list.append(str(item))

        str_list = " ".join(str_list)
        result = str_list.count('+') + str_list.count('-') + str_list.count('*') + str_list.count('/')
        print(result)

    # задать с клавиатуры множество M1, сформировать множество M2 из списка; вывести на экран
    # множество, полученное путем пересечения множеств M1 и M2;

    elif command == 7:
        print('Введите значения множества М1, для окончания ввода просто нажмите enter')

        set_M1 = []
        while True:
            value = input('Введите новый элемент: ')

            if value == "":
                break

            value_type = input('Введите тип нового элемента (int, str, float): ')
            set_M1.append(get_typed_variable(value, value_type))

        set_M1 = set(set_M1)
        set_M2 = set(list_of_elements)

        print('Пересечение множеств M1 и M2: ', set_M1 & set_M2)

    # получить из списка словарь, ключом каждого элемента сделать позицию элемента в словаре;
    # построчно отобразить на экране элементы словаря с ключом меньше 3

    elif command == 8:

        idx_list = []
        for idx, item in enumerate(list_of_elements):
            idx_list.append(idx)

        dict_list = dict(zip(idx_list, list_of_elements))

        for key, value in dict_list.items():
            if (key > 2):
                break
            print(key, ': ', value)

    elif command == 0:
        exit(0)

    else:
        print('Неверная команда')


