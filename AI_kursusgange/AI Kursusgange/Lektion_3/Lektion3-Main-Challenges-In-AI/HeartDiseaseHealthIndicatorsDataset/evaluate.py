from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def evaluate_model(model, test_input_data, test_output_data):
    '''
    param model:
        the model you want to evaluate
    :param test_input_data:
        input data that is allocated for testing the model
    :param test_output_data:
        the true labeled data
    :return:
        accuracy
    '''
    '### Evaluate model ###'
    print('predicting on test set .. ')
    y_pred = model.predict(test_input_data)
    accuracy = accuracy_score(test_output_data, y_pred)
    #cm = confusion_matrix(test_output_data, y_pred)
    #disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                  #display_labels=model.classes_)
    #disp.plot()
    #plt.show()
    return accuracy



