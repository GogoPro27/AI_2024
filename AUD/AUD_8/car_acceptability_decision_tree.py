import csv

from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder


def read_file(file_name):
    with open(file_name) as doc:
        # tuka e otvoren fajlot
        csv_reader = csv.reader(doc, delimiter=",")
        # [print(l) for l in list(csv_reader)[1:]]
        ds = list(csv_reader)

    # tuka e zatvoren
    return ds


def remove_attribute(train_x, test_x, idx):
    train_x_2 = list()
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != idx]
        train_x_2.append(row)

    test_x_2 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != idx]
        test_x_2.append(row)

    return train_x_2, test_x_2


def calculate_accuracy(test_x, test_y, classifier):
    accuracy = 0
    for entry, label in zip(test_x, test_y):
        predicted_label = classifier.predict([entry])[0]
        if predicted_label == label:
            accuracy += 1
    accuracy = accuracy / len(test_x)
    return accuracy


if __name__ == '__main__':
    dataset = read_file('car.csv')
    features = dataset[0]
    dataset = dataset[1:]

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier.fit(train_x, train_y)

    print(f"Depth: {classifier.get_depth()}")
    print(f"Num of leaves: {classifier.get_n_leaves()}")

    accuracy = calculate_accuracy(test_x,test_y,classifier)

    print(f"Accuracy: {accuracy * 100} %")
    print()

    feature_importances = list(classifier.feature_importances_)
    # print(features)
    # print(feature_importances)

    most, least = 0, 100
    f1, f6 = "", ""
    idx_most, idx_least = 0, 0
    i = 0
    for feature, feature_importance in zip(features, feature_importances):
        print(f"{feature} : {feature_importance * 100} %")
        if feature_importance < least:
            least = feature_importance
            f6 = feature
            idx_least = i
        if feature_importance > most:
            most = feature_importance
            f1 = feature
            idx_most = i
        i += 1

    print()
    print("Most important feature is " + f1 + " at " + str(idx_least) + " position")
    print("Least important feature is " + f6 + " at " + str(idx_most) + " position")
    print()

    # da probame so brisenje na najvazniot i najnevazniot atribut
    train_x_2, test_x_2 = remove_attribute(train_x, test_x, idx_most)
    classifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier2.fit(train_x_2, train_y)
    accuracy2 = calculate_accuracy(test_x_2,test_y,classifier2)
    print(f"Accuracy without the most important feature: {accuracy2*100} %")
    print(f"Depth: {classifier2.get_depth()}")
    print(f"Num of leaves: {classifier2.get_n_leaves()}")

    print()

    train_x_3, test_x_3 = remove_attribute(train_x, test_x, idx_least)
    classifier3 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier3.fit(train_x_3, train_y)
    accuracy3 = calculate_accuracy(test_x_3, test_y, classifier3)
    print(f"Accuracy without the least important feature: {accuracy3 * 100} %")
    print(f"Depth: {classifier3.get_depth()}")
    print(f"Num of leaves: {classifier3.get_n_leaves()}")



