import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder


# za kompatibilnost so CategoricalNB


def read_file(file_name):
    with open(file_name) as doc:
        # tuka e otvoren fajlot
        csv_reader = csv.reader(doc, delimiter=",")
        # [print(l) for l in list(csv_reader)[1:]]
        ds = list(csv_reader)[1:]

    # tuka e zatvoren
    return ds


if __name__ == '__main__':
    dataset = read_file('car.csv')

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]  # vlezovi
    train_y = [row[-1] for row in train_set]  # izlezi
    train_x = encoder.transform(train_x)  # vo celobrojni

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]  # vlezovi
    test_y = [row[-1] for row in test_set]  # izlezi
    test_x = encoder.transform(test_x)

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y)

    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy += 1

    print(str((accuracy / len(test_x)) * 100) + "% na poslednite 30% od podatocijte predikcija")

    entry = [el for el in input().split(" ")]

    entry = encoder.transform([entry])

    print(classifier.predict(entry)[0])
