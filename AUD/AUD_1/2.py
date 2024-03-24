def transform(l1):
    return l1[0], l1[-1]


if __name__ == '__main__':
    l1 = list(range(1, 100))
    print(transform(l1))
