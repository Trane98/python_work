import time
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

'### Models of your choosing ###'


def train_SVM_model(input, labels, name):
    '''
    param input:
        input data for the model to train on
    :param labels:
        true labels for the model to calculate error
    :param name:
        :type String
            giving your model name, to discern between them
    :return:
        trained model
    '''
    print(f"training model {name}.. ")
    current_time = time.time() # ready set go
    svm_model = SVC(kernel='poly', degree=5) # Instantiate Support Vector Machine Classifier
    svm_model.fit(input, labels)
    end_time = time.time()
    print(f"model training time: {end_time - current_time:.3f} seconds")
    return svm_model

def train_RANDOMFORREST_model(input, labels, name):
    '''
        param input:
            input data for the model to train on
        :param labels:
            true labels for the model to calculate error
        :param name:
            :type String
                giving your model name, to discern between them
        :return:
            trained model
        '''
    print(f"training model {name}.. ")
    current_time = time.time()  # ready set go
    rf_classifier = RandomForestClassifier(random_state=42)
    rf_classifier.fit(input, labels)
    end_time = time.time()
    print('model training time: ' + str(end_time - current_time))
    return rf_classifier

def train_logisitc_regression(input, labels, name):
    pass

