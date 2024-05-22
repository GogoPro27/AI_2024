import csv
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler

from wine_quality_neural_network import read_dataset, divide_sets

if __name__ == '__main__':
    dataset, features = read_dataset()
    # [print(l) for l in dataset]
    train_set, val_set, test_set = divide_sets(dataset)

    train_x = [l[:-1] for l in train_set]
    train_y = [l[-1] for l in train_set]

    val_x = [l[:-1] for l in val_set]
    val_y = [l[-1] for l in val_set]

    test_x = [l[:-1] for l in test_set]
    test_y = [l[-1] for l in test_set]

    scaler1 = StandardScaler()
    scaler1.fit(train_x)

    scaler2 = MinMaxScaler()
    scaler2.fit(train_x)

    classifier1 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier1.fit(train_x, train_y)
    classifier2.fit(scaler1.transform(train_x), train_y)
    classifier3.fit(scaler2.transform(train_x), train_y)

    val_acc1 = 0
    val_predictions = classifier1.predict(val_x)
    for true, pred in zip(val_y, val_predictions):
        if true == pred:
            val_acc1 += 1
    val_acc1 = val_acc1 / len(val_y)

    val_accuracies = [0, 0, 0]
    for i, c in enumerate([classifier1, classifier2, classifier3]):
        val_predictions = None
        if i == 0:
            val_predictions = c.predict(val_x)
        elif i == 1:
            val_predictions = c.predict(scaler1.transform(val_x))
        else:
            val_predictions = c.predict(scaler2.transform(val_x))

        for true, pred in zip(val_y, val_predictions):
            if true == pred:
                val_accuracies[i] += 1
        val_accuracies[i] = val_accuracies[i] / len(val_y)

    print(f"Bez normalizacija imame tochnost so validacisko mnozestvo of {val_accuracies[0] * 100} %")
    print(f"So Standardna normalizacija imame tochnost so validacisko mnozestvo of {val_accuracies[1] * 100} %")
    print(f"So MinMax normalizacija imame tochnost so validacisko mnozestvo of {val_accuracies[2] * 100} %")

    tp, fp, tn, fn = 0, 0, 0, 0
    predictions = classifier3.predict(scaler2.transform(test_x))

    for pred, true in zip(predictions, test_y):
        if true == 'good':
            if pred == true:
                tp += 1
            else:
                fn += 1
        else:
            if pred == true:
                tn += 1
            else:
                fp += 1
    acc = (tp + tn) / (tp + fp + tn + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    print('Evaluacija:')
    print(f"Tochnost: {acc}")
    print(f"Preciznost: {precision}")
    print(f"Odziv: {recall}")