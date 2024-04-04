def createMinesweeper(matrix):
    n = len(matrix)
    return [[checkAround(y, x, matrix) for x in range(n)] for y in range(n)]


def checkAround(x, y, matrix):
    counter = 0
    if matrix[x][y] == '#':
        return matrix[x][y]
    n = len(matrix)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < n and 0 <= y + j < n:
                if matrix[x + i][y + j] == '#':
                    counter += 1
    return counter


if __name__ == '__main__':
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(input().split("   "))

    matrix = createMinesweeper(matrix)

    for row in matrix:
        print("   ".join(str(col) for col in row))
