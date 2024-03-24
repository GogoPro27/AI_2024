if __name__ == '__main__':
    n = int(input())
    m = int(input())

    matrix = []
    for i in range(0, n):
        input_tmp_array = [int(el) for el in input(f"Fill the {i + 1}'th row").split(" ")]
        matrix.append(input_tmp_array)

    # matrix = [[elem * 2 for elem in row] for row in matrix]
    # print(matrix)
    matrix = [elem * 2 for row in matrix for elem in row]
    print(matrix)