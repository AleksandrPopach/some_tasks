def fill(a, b, depth=0):
    """
    Заполняет матрицу по спирали размером n на m числами от 1 до n * m
    :param a: количество строк на данной глубине
    :param b: количество столбцов на данной глубине
    :param depth: глубина заполнения
    """
    if depth == max_depth:  # достигнута макс. глубина
        return
    digits = d[depth]
    if len(digits) == 1:
        matrix[n // 2][m // 2] = digits[0]
        return
    if a == 1:  # осталась 1 строчка
        i = n // 2
        for j in range(depth, m - depth):
            matrix[i][j] = digits[j - depth]
        return
    if b == 1:  # остался 1 столбец
        j = m // 2
        for i in range(depth, n - depth):
            matrix[i][j] = digits[i - depth]
        return
    for i in range(depth, n - depth):
        for j in range(depth, m - depth):
            if i == depth:
                matrix[i][j] = digits[j - depth]
            if j == m - depth - 1 and i != depth:
                matrix[i][j] = digits[i + j - depth * 2]
            if i == n - depth - 1 and j != m - depth - 1:
                matrix[i][j] = digits[b + a - j + b - 3 + depth]
            if j == depth and i != depth and i != n - depth - 1:
                matrix[i][j] = digits[b + b + a - i + a - 4 + depth]
    fill(a - 2, b - 2, depth + 1)

n, m = [int(i) for i in input().split()]  # n строк, m столбцов
matrix = [[0] * m for _ in range(n)]
numbers = [i for i in range(1, n * m + 1)]

d = {}  # ключи - глубина заполнения матрицы, значения - список чисел для каждой глубины
i = 0
a = n
b = m
while numbers:
    if len(numbers) == 1:
        d[i] = numbers[:]
        break
    x = 2 * b + 2 * (a - 2)
    d[i] = numbers[:x]
    del numbers[:x]
    a -= 2
    b -= 2
    i += 1

max_depth = len(d)
fill(n, m)

for i in range(n):
    print(*[str(j).ljust(3) for j in matrix[i]])