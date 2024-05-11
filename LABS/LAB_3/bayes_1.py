import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
from dataset_script_1 import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

if __name__ == '__main__':
    # dataset direktno go zemam
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.75 * len(dataset))]
    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]
    train_X_encoded = encoder.transform(train_X)  # encodirano

    test_set = dataset[int(0.75 * len(dataset)):]
    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]
    test_X_encoded = encoder.transform(test_X)  # encodirano

    classifier = CategoricalNB()
    classifier.fit(train_X_encoded, train_Y)

    accuracy = 0

    for test_x, test_y in zip(test_X_encoded, test_Y):
        prediction = classifier.predict([test_x])[0]
        if prediction == test_y:
            accuracy += 1

    print(accuracy / len(test_X))

    # [print(i,end=" ") for i in dataset_sample[0][:-1]]

    input_test = [i for i in input().split(" ")]
    input_test_x_encoded = encoder.transform([input_test])

    prediction_input = classifier.predict(input_test_x_encoded)[0]
    predictions_input_probabilities = classifier.predict_proba(input_test_x_encoded)


    print(prediction_input)
    print(predictions_input_probabilities)


    # submit_train_data(train_X_encoded, train_Y)
    #
    # submit_test_data(test_X_encoded, test_Y)
    #
    # submit_classifier(classifier)
    #
    # submit_encoder(encoder)
    #
    # from submission_script import *
