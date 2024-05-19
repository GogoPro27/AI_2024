import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
from sklearn.ensemble import RandomForestClassifier
from dataset_script import dataset

if __name__ == '__main__':
    col_index = int(input())
    num_trees = int(input())
    crit = input()
    input_to_predict = [el for i,el in enumerate(list(map(float, input().split(" ")))) if i !=col_index]

    dataset_deleted_col = list()
    for row in dataset:
        dataset_deleted_col.append([row[i] for i in range(0, len(row)) if i != col_index])
    dataset = dataset_deleted_col

    train_set = dataset[:int(len(dataset) * 0.85)]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_set = dataset[int(len(dataset) * 0.85):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    classifier = RandomForestClassifier(
        criterion=crit,
        random_state=0,
        n_estimators=num_trees
    )
    classifier.fit(train_X, train_Y)

    accuracy = 0
    for to_predict, actual_class in zip(test_X, test_Y):
        prediction = classifier.predict([to_predict])[0]
        if prediction == actual_class:
            accuracy += 1
    accuracy /= len(test_Y)
    print(f"Accuracy: {accuracy}")

    prediction_from_input = classifier.predict([input_to_predict])[0]
    print(prediction_from_input)
    print(classifier.predict_proba(input_to_predict)[0])

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    # submit_classifier(classifier)
