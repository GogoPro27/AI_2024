def multiplyElement(el, i, n):
    if i < n / 2:
        return el * 2
    else:
        return el * 3


if __name__ == '__main__':
    n = int(input())
    m = int(input())

    matrix = []

    for i in range(0, n):
        row = []
        for j in range(0, m):
            row.append(j + 1)
        matrix.append(row)

    print(matrix)
    matrix = [[multiplyElement(matrix[i][j], i, n) for j in range(0, n)] for i in range(0, m)]
    print(matrix)
