import csv
from sklearn.naive_bayes import GaussianNB


def read_file(file_name):
    with open(file_name) as doc:
        # tuka e otvoren fajlot
        csv_reader = csv.reader(doc, delimiter=",")
        # [print(l) for l in list(csv_reader)[1:]]
        ds = list(csv_reader)[1:]
        ds = [[int(i) for i in l1] for l1 in ds]

    # tuka e zatvoren
    return ds


if __name__ == '__main__':
    dataset = read_file('medical_data.csv')
    # [print(i) for i in list(dataset)]

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]  # vlezovi
    train_y = [row[-1] for row in train_set]  # izlezi

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]  # vlezovi
    test_y = [row[-1] for row in test_set]  # izlezi

    # [print(t) for t in train_set]
    # [print(t) for t in test_set]

    classifier = GaussianNB()
    classifier.fit(train_x,train_y)

    correct = 0
    for entry,result in zip(test_x,test_y):
        predicted_result = classifier.predict([entry])[0]
        # print(predicted_result,result)
        if predicted_result == result:
            correct+=1
    print(correct/len(test_set))