class Medicament(object):

    vendor_code = None
    name = None
    cost = None
    has_prescription = False
    description = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def print(self):
        print('Артикул:', self.vendor_code)
        print('Название: ', self.name)
        print('Стоимость:', self.cost)
        print('Наличие рецепта:', 'да' if self.has_prescription else 'нет')
        print('Описание:', self.description)
        print('\n')

    def without_prescription(self):
        if not self.has_prescription:
            self.print()


menu = '''
    1. Добавить лекарство;
    2. Удалить лекарство (по артикулу);
    3. Все лекарства;
    4. Лекарства без рецепта;

    0. Выход.
'''

medicaments = []

while True:
    print(menu)

    command = int(input('Введите команду: '))

    if command == 1:
        vendor_code = input('Введите артикул: ')
        name = input('Введите название: ')
        cost = input('Введите стоимость: ')
        has_prescription = True if input('Введите наличие рецепта (да/Нет): ') == 'да' else False
        description = input('Введите описание: ')

        medicaments.append(Medicament(
            vendor_code=vendor_code,
            name=name,
            cost=cost,
            has_prescription=has_prescription,
            description=description)
        )

    elif command == 2:
        vendor_code = input('Введите артикул удаляемого лекарства: ')
        medicaments = [item for item in medicaments if item.vendor_code != vendor_code]

    elif command == 3:
        for item in medicaments:
            item.print()

    elif command == 4:
        for item in medicaments:
            item.without_prescription()

    elif command == 0:
        exit(0)

    else:
        print('Неверная команда!')


