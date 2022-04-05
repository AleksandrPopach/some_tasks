from copy import deepcopy


def num_grid(field: list):
    """Функция считает количество символов '#' среди соседей каждого элемента '-' матрицы и заменяет этот элемент
    на число - количество таких соседей.
    :param field: list  Двумерный массив, состоящий из символов '-' и '#'.
    :return: list  Этот же массив, только изменённый.
    """
    n = len(field)
    m = len(field[0])
    # создаём копию исходного массива и добавляем в неё барьерные пустые элементы:
    # 2 строки(в начало и в конец) и 2 столбца(в начало и в конец)
    extended_field = deepcopy(field)
    extended_field.insert(0, ['-'] * m)
    extended_field.append(['-'] * m)
    for ind in range(len(extended_field)):
        extended_field[ind].insert(0, '-')
        extended_field[ind].append('-')

    # пробегаемся по соседям всех пустых элементов и считаем, сколько среди них символов '#'
    # в конце каждой основной итерации изменяем элементы в исходном массиве
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            current = extended_field[i][j]
            if current == '#':
                continue
            counter = 0
            for k in [-1, 0, 1]:
                for x in [-1, 0, 1]:
                    neighbour = extended_field[i + k][j + x]
                    if neighbour == '#':
                        counter += 1
            field[i - 1][j - 1] = str(counter)
    return field


matrix = num_grid([['-', '-', '-', '#', '#'],
                   ['-', '#', '-', '-', '-'],
                   ['-', '-', '#', '-', '-'],
                   ['-', '#', '#', '-', '-'],
                   ['-', '-', '-', '-', '-']
                   ])
for i in range(len(matrix)):
    print(matrix[i])