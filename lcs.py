def lcs(A: list, B: list):
    """ Считает длину и значения наибольшей общей подпоследовательности двух отсортированных массивов.
    """
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    result = []
    for i in range(len(A), 0, -1):
        for j in range(len(B), 0, -1):
            if F[i][j] != F[i - 1][j] and F[i][j] != F[i][j - 1]:
                result.append(A[i - 1])
    result = result[::-1]
    return F[-1][-1], result

A = [1, 2, 4, 7, 8, 9, 10, 11, 15, 17, 20]
B = [1, 2, 4, 5, 6, 8, 9, 10, 12, 15]
print(lcs(A, B))
