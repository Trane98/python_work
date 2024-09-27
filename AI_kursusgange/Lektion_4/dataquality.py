import time
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from evaluate import evaluate_model
from balance_dataset import balance_data
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from model import train_SVM_model, train_RANDOMFORREST_model

'### Load data from folder and inspect ###'
dataset = pd.read_csv('HeartDiseaseHealthIndicatorsDataset/heart_disease_health_indicators_BRFSS2015.csv')
print('showing the first part of the dataset ..')
print(dataset.head())
#print(dataset.apply(pd.value_counts))

## Do some corrupted stuff to the data
columns = ['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'Diabetes', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']
#cols_to_drop = ['HighBP', 'GenHlth', 'DiffWalk', 'Age', 'PhysHlth', 'Stroke'] # choose som columns to drop
#dataset = dataset.drop(cols_to_drop, axis=1)

# correlation matrix to see if some features explain the same variance
plt.figure(figsize=(12,10))
sns.heatmap(dataset.corr(), annot=True, cmap="magma", fmt='.2f')
plt.title('Correlation map')
plt.show() # uncomment this to show the correlation map

'### Preprocess data ###'
## balance data
print('Balancing data')
dataset = balance_data(dataset, rows_in_each_class=23893) # there are 229787 entries with label 1 and 23893 entries with label 0 --> max value in balance_data function must be 23893 to balance data

## create input and ouput from dataset ##
input = dataset.drop('HeartDiseaseorAttack', axis=1)
output = dataset['HeartDiseaseorAttack']

# allocate a static test set 20% of len(dataset). We want to test on the same test set for different models.
X_train, X_test, y_train, y_test = train_test_split(input, output, test_size=0.20, random_state=42)
print("length of training set: " + str(len(X_train)))
print("length of test set: " + str(len(X_test)))

# change amount of training instances based on previous split (it takes too much time to train on laptop to use the entire dataset)
# If you have a powerful laptop, use X_train instead
X_train_reduced, _, y_train_reduced, _ = train_test_split(X_train, y_train, test_size=0.50, random_state=42)
print("length of reduced training set: " + str(len(X_train_reduced)))


print('Scaling data ..')
minmax_scalar = MinMaxScaler() # instantiate MinMaxScaler
X_train_minmax = minmax_scalar.fit_transform(X_train_reduced) # transform data
X_test_minmax = minmax_scalar.transform(X_test) # transform data

'### Train model ###'
svm_model = train_SVM_model(X_train_reduced, y_train_reduced, 'SVM model: no feature scaling') # train model without feature scaling
svm_model_scaling = train_SVM_model(X_train_minmax, y_train_reduced, 'SVM model: feature scaling min_max') # train model with scaling
#rf_model = train_RANDOMFORREST_model(X_train_reduced, y_train_reduced, 'RF model: no feature scaling') # uncomment to train random forrest classifier
#rf_model_scaling = train_RANDOMFORREST_model(X_train_minmax, y_train_reduced, 'RF model: feature scaling min_max')  # uncomment to train random forrest with minmax scalar

# Calculate feature importance in random forest and plot
#importances = rf_model.feature_importances_
#labels = dataset.columns
#feature_df = pd.DataFrame(list(zip(labels, importances)), columns = ["feature","importance"])
#feature_df = feature_df.sort_values(by='importance', ascending=False,)

# image formatting
#axis_fs = 18 #fontsize
#title_fs = 22 #fontsize
#sns.set(style="whitegrid")

#ax = sns.barplot(x="importance", y="feature", data=feature_df)
#ax.set_xlabel('Importance',fontsize = axis_fs)
#ax.set_ylabel('Feature', fontsize = axis_fs)#ylabel
#ax.set_title('Random forest\nfeature importance', fontsize = title_fs)
#plt.show()


'### Evaluate model ###'
accuracy_svm = evaluate_model(svm_model, X_test, y_test)
accuracy_scaled_svm = evaluate_model(svm_model_scaling, X_test_minmax, y_test)
#accuracy_rf = evaluate_model(rf_model, X_test, y_test)
#accuracy_scaled_rf = evaluate_model(rf_model_scaling, X_test_minmax, y_test)

print(f"accuracy not scaled SVM: {accuracy_svm*100:.3f}"  + '%' + '\n'
      f"accuracy scaled SVM: {accuracy_scaled_svm*100:.3f}" + '%' + '\n')
      #f"accuracy not scaled RF: {accuracy_rf*100:.3f}"  + '%' + '\n'
      #f"accuracy scaled RF: {accuracy_scaled_rf*100:.3f}" + '%'))

