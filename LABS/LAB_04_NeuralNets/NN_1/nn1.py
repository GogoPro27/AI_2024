import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

import warnings
from sklearn.neural_network import MLPClassifier
from LABS.LAB_04_NeuralNets.NN_1.dataset import data

warnings.filterwarnings("ignore")


def calculate_accuracy(test_x, test_y, classifier: MLPClassifier):
    accuracy = 0
    predictions = classifier.predict(test_x)
    for pred, true in zip(predictions, test_y):
        if pred == true:
            accuracy += 1
    return accuracy / len(test_y)


def divide_dataset(dataset):
    ones = [row for row in dataset if row[-1] == 1]
    zeros = [row for row in dataset if row[-1] == 0]

    train_set = ones[:int(len(ones) * 0.8)] + zeros[:int(len(zeros) * 0.8)]
    validation_set = ones[int(len(ones) * 0.8):] + zeros[int(len(zeros) * 0.8):]

    return train_set, validation_set


if __name__ == '__main__':
    dataset = data
    learning_rate = float(input())
    epoch_num = int(input())

    train_set, validation_set = divide_dataset(dataset)
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    val_X = [row[:-1] for row in validation_set]
    val_Y = [row[-1] for row in validation_set]

    classifier = MLPClassifier(6,
                               activation='tanh',
                               max_iter=epoch_num,
                               learning_rate_init=learning_rate,
                               random_state=0)

    classifier.fit(train_X, train_Y)

    accuracy_train = calculate_accuracy(train_X, train_Y, classifier)
    accuracy_validation = calculate_accuracy(val_X, val_Y, classifier)

    if accuracy_train > accuracy_validation * 1.15:
        print("Se sluchuva overfitting")
    else:
        print("Ne se sluchuva overfitting")

    print(f"Tochnost so trenirachko mnozhestvo: {accuracy_train}")
    print(f"Tochnost so validacisko mnozhestvo: {accuracy_validation}")
