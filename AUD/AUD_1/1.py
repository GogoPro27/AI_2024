def calculate(a, operand, b):
    if operand == '+':
        return a + b
    elif operand == '-':
        return a - b
    elif operand == '*':
        return a * b
    elif operand == '/':
        return a / b
    elif operand == '//':
        return a // b
    elif operand == '%':
        return a % b
    elif operand == '**':
        return a ** b
    else:
        return 0


if __name__ == '__main__':

    array = input().split(" ")

    print(calculate(int(array[0]), array[1], int(array[2])))

