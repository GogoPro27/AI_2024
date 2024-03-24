def swap_list(l1):
    return [(b, a) for a, b in l1]


if __name__ == '__main__':
    list_1 = [('a', 1), ('b', 2), ('c', 3)]
    list_2 = swap_list(list_1)
    print(list_2)
