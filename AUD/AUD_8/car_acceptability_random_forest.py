import csv

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder


def read_file(file_name):
    with open(file_name) as doc:
        # tuka e otvoren fajlot
        csv_reader = csv.reader(doc, delimiter=",")
        # [print(l) for l in list(csv_reader)[1:]]
        ds = list(csv_reader)

    # tuka e zatvoren
    return ds


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

    classifier = RandomForestClassifier(n_estimators=50,criterion='entropy',random_state=0)
    classifier.fit(train_x, train_y)

    accuracy = calculate_accuracy(test_x, test_y, classifier)

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
