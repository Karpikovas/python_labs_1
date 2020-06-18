list1 = ['R', 'T']
list2 = [[1, 2], [4, 5, 6]]

square_area = lambda x: x*x
triangle_area = lambda a, b: a * b * 0.5
trapezoid_area = lambda a, b, h: (a + b) * h * 0.5


length = lambda x: 2 if x == 'R' else (3 if x == 'T' else 1)

while True:
    L = []

    L.append(list(input('Введите команды через пробел: ').split()))
    L.append([list(map(int, input('Введите {0} значения: '.format(length(i))).split())) for i in L[0]])

    result = list(map(lambda x, y:
                      triangle_area(y[0], y[1]) if x == 'R'
                      else (
                          trapezoid_area(y[0], y[1], y[2]) if x == 'T'
                          else square_area(y[0])), L[0], L[1]))

    print(result)

    L.clear()
