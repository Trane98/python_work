import pandas as pd
from sklearn.model_selection import train_test_split

# Read data
data = pd.read_csv("C:\\Program Files (x86)\\python_work\\AI_kursusgange\\Lektion_8\\titanic.csv")

# Preprocessing
data.drop(['PassengerId', 'Name', 'Cabin', 'Ticket', 'Embarked'], axis=1, inplace=True)  # Drop columns we don't need
data.dropna(inplace=True)  # Drop nan rows
data['Sex'].replace(['male', 'female'], [1, 0], inplace=True)  # Replace strings with 0 and 1

# Define data
X = data[['Age', 'Sex', 'Pclass', 'SibSp', 'Parch', 'Fare']].values
y = data.Survived.values

# Split data into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)




from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Define classifiers
knn_classifier = KNeighborsClassifier(n_neighbors=20)  # Change hyperparameters
decision_tree_classifier = DecisionTreeClassifier(max_depth=3, min_samples_leaf=10, random_state=42)  # Change hyperparameters
random_forest_classifier = RandomForestClassifier(n_estimators=500, bootstrap=True, min_samples_leaf=10, random_state=42)  # Change hyperparameters

# Train classifiers
knn_classifier.fit(X_train, y_train)
decision_tree_classifier.fit(X_train, y_train)
random_forest_classifier.fit(X_train, y_train)

# Make predictions on both training and testing sets
y_pred_knn_train = knn_classifier.predict(X_train)
y_pred_knn_test = knn_classifier.predict(X_test)

y_pred_tree_train = decision_tree_classifier.predict(X_train)
y_pred_tree_test = decision_tree_classifier.predict(X_test)

y_pred_rf_train = random_forest_classifier.predict(X_train)
y_pred_rf_test = random_forest_classifier.predict(X_test)

# Calculate training and testing accuracy
accuracy_knn_train = accuracy_score(y_train, y_pred_knn_train)
accuracy_knn_test = accuracy_score(y_test, y_pred_knn_test)

accuracy_tree_train = accuracy_score(y_train, y_pred_tree_train)
accuracy_tree_test = accuracy_score(y_test, y_pred_tree_test)

accuracy_rf_train = accuracy_score(y_train, y_pred_rf_train)
accuracy_rf_test = accuracy_score(y_test, y_pred_rf_test)

# Print out the results
print('Model accuracy')
print('\nKNN')
print(f' - Training: {accuracy_knn_train * 100:.2f}%')
print(f' - Test: {accuracy_knn_test * 100:.2f}%')
print('\nDecision tree')
print(f' - Training: {accuracy_tree_train * 100:.2f}%')
print(f' - Test: {accuracy_tree_test * 100:.2f}%')
print('\nRandom forest')
print(f' - Training: {accuracy_rf_train * 100:.2f}%')
print(f' - Test: {accuracy_rf_test * 100:.2f}%')
