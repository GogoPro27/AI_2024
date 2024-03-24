if __name__ == '__main__':
    # Ana
    # Marija
    # Stefan
    # Aleksandar
    my_dic = {"Ana": "01/17/1991", "Bob": "01/17/3333", "David": "01/17/2022",  "Peter": "01/17/1111"}
    print("Dobredojdovte do rechnikot za rodendeni. Nie gi znaeme rodendenite na:")
    for key in my_dic.keys():
        print(key)

    i1 = input("Koj rodenden e potrebno da se prebara?\n")
    print("Rodendenot na "+i1+" e "+my_dic[i1])

