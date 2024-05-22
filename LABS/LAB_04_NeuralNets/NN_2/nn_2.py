import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'
import warnings
from sklearn.exceptions import ConvergenceWarning
from dataset import data


from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
def calculate_accuracy_and_recall(test_x, test_y, classifier: MLPClassifier):
    tp, fp, tn, fn = 0, 0, 0, 0
    predictions = classifier.predict(test_x)
    for pred, true in zip(predictions, test_y):
        if true == 1:
            if pred == true:
                tp += 1
            else:
                fp += 1
        else:
            if pred == true:
                tn += 1
            else:
                fn += 1
    # acc = tp / (tp + fp)
    # recall = tp / (tp + fn)
    acc = tp / (tp + fn)
    recall = tp / (tp + fp)
    return acc, recall


def divide_dataset(dataset):
    m_s = [row for row in dataset if row[0] == 1]
    b_s = [row for row in dataset if row[0] == 0]

    train_set = m_s[:int(len(m_s) * 0.7)] + b_s[:int(len(b_s) * 0.7)]
    test_set = m_s[int(len(m_s) * 0.7):] + b_s[int(len(b_s) * 0.7):]

    return train_set, test_set


if __name__ == '__main__':
    dataset = list()
    for row in data:
        new_row = list()
        if row[0] == 'B':
            new_row = [0] + row[1:]
        else:
            new_row = [1] + row[1:]
        dataset.append(new_row)
    warnings.filterwarnings('ignore', category=ConvergenceWarning)

    num_hidden_neurons = int(input())
    learning_rate = 0.001
    epochs = 20
    activation_f = 'relu'

    train_set, test_set = divide_dataset(dataset)

    train_X = [row[1:] for row in train_set]
    train_Y = [row[0] for row in train_set]

    test_X = [row[1:] for row in test_set]
    test_Y = [row[0] for row in test_set]

    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(train_X)

    train_X = scaler.transform(train_X)
    test_X = scaler.transform(test_X)

    classifier = MLPClassifier(num_hidden_neurons,
                               learning_rate_init=learning_rate,
                               max_iter=epochs,
                               activation=activation_f,
                               random_state=0)
    classifier.fit(train_X, train_Y)

    accuracy_1,recall_1 = calculate_accuracy_and_recall(train_X, train_Y, classifier)
    accuracy_2,recall_2 = calculate_accuracy_and_recall(test_X, test_Y, classifier)

    print(f"Preciznost so trenirachkoto mnozhestvo: {accuracy_1}")
    print(f"Odziv so trenirachkoto mnozhestvo: {recall_1}")

    print(f"Preciznost so testirachkoto mnozhestvo: {accuracy_2}")
    print(f"Odziv so testirachkoto mnozhestvo: {recall_2}")

