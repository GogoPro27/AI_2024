import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from dataset_script import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB


def split_dataset(dataset):
    train_set = dataset[:int(0.75 * len(dataset))]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_set = dataset[int(0.75 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    return train_X, train_Y, test_X, test_Y


def calculate_accuracy(test_X, test_Y, classifier: CategoricalNB):
    acc = 0
    predictions = classifier.predict(test_X)
    for pred, actual in zip(predictions, test_Y):
        if pred == actual:
            acc += 1
    return acc / len(test_X)


if __name__ == '__main__':
    to_predict = input().split(" ")
    encoder = OrdinalEncoder()

    train_X, train_Y, test_X, test_Y = split_dataset(dataset)
    encoder.fit([row[:-1] for row in dataset])
    train_X = encoder.transform(train_X)
    test_X = encoder.transform(test_X)

    classifier = CategoricalNB()
    classifier.fit(train_X, train_Y)

    accuracy = calculate_accuracy(test_X, test_Y, classifier)
    print(accuracy)

    to_predict = encoder.transform([to_predict])

    prediction = classifier.predict(to_predict)[0]
    print(prediction)
    print(classifier.predict_proba(to_predict))
