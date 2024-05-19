import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
from dataset_script import dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder

if __name__ == '__main__':
    X = float(input())
    X /= 100
    crit = input()

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[int(len(dataset) * (1.0 - X)):]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    train_X = encoder.transform(train_X)

    test_set = dataset[:int(len(dataset) * (1.0 - X))]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]
    test_X = encoder.transform(test_X)

    decision_tree_classifier = DecisionTreeClassifier(criterion=crit, random_state=0)
    decision_tree_classifier.fit(train_X, train_Y)

    print(f"Depth: {decision_tree_classifier.get_depth()}")
    print(f"Num of leaves: {decision_tree_classifier.get_n_leaves()}")

    accuracy = 0
    for to_predict, actual_class in zip(test_X, test_Y):
        prediction = decision_tree_classifier.predict([to_predict])[0]
        if prediction == actual_class:
            accuracy += 1
    accuracy /= len(test_Y)
    print(f"Accuracy: {accuracy}")

    featire_importances = decision_tree_classifier.feature_importances_
    max_idx = max(list(featire_importances))
    min_idx = min(list(featire_importances))

    for i, importance in enumerate(featire_importances):
        if importance == max_idx:
            print("Most important feature: " + str(i))
        if importance == min_idx:
            print("Least important feature: " + str(i))

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    # submit_classifier(decision_tree_classifier)

    # submit na encoderot
    # submit_encoder(encoder)
