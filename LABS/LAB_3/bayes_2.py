import os
from sklearn.naive_bayes import GaussianNB

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
from dataset_script_2 import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka
    dataset = [[float(i) for i in row]for row in dataset]

    train_set = dataset[:int(0.85 * len(dataset))]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_set = dataset[int(0.85 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_X, train_Y)

    accuracy = 0

    for test_x, test_y in zip(test_X, test_Y):
        predicted = classifier.predict([test_x])[0]
        if predicted == test_y:
            accuracy += 1

    print(accuracy / len(test_set))

    input_test = [float(i) for i in input().split(" ")]

    prediction_from_input = classifier.predict([input_test])[0]
    print(prediction_from_input)
    print(classifier.predict_proba([input_test]))

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    # submit_classifier(classifier)

    # povtoren import na kraj / ne ja otstranuvajte ovaa linija
    # from submission_script import *
