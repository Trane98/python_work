#import the libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt #Data Visualization
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.model_selection import train_test_split

# Load datafile
df = pd.read_csv('Mall Customer Segmentation Data/Mall_Customers.csv')
# look at datafile
print(df.head(20))
print(df.info())



# Extract features for K-means algorithm to cluster
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]


'### make a split of data for training and for later test ###'
# Define the split ratio
split_ratio = 0.7  # Adjust as needed
# Randomly shuffle the rows in the DataFrame
df_shuffled = X.sample(frac=1, random_state=42)
# Calculate the number of rows for each split
split_index = int(split_ratio * len(df_shuffled))
# Split the DataFrame into two based on the ratio
X_train = df_shuffled.iloc[:split_index]
X_test = df_shuffled.iloc[split_index:]
# Reset the index for both DataFrames if needed
X_train = X_train.reset_index(drop=True)
X_test = X_test.reset_index(drop=True)


'### Look at the feature ###'
X.plot(kind='scatter', x='Annual Income (k$)', y='Spending Score (1-100)')
plt.title('2-dimensional featurespace')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
#plt.show()
'### find out how many clusters is the optimal amount ###'
# elbow and silhouette method
inertia_array = []
silhouettescore_array = []
max_s_score = 0
k = 0
for i in range(2,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0, n_init=10)
    kmeans.fit(X_train)
    inertia_array.append(kmeans.inertia_)
    s_score = silhouette_score(X_train, kmeans.labels_)
    silhouettescore_array.append(s_score)
    '### find best cluster number based on silhouette score ###'
    if s_score > max_s_score:
        max_s_score = s_score
        k = i

'### Visualize Elbow method and silhouette score ###'
plt.figure()
plt.subplot(1,4,1)
plt.plot(range(2,11), inertia_array)
plt.title('Elbow Method')
plt.xlabel('# clusters')
plt.ylabel('intertia')
plt.subplot(1, 4, 2)
plt.plot(range(2,11), silhouettescore_array)
plt.title('Silhouette score')
plt.xlabel('# clusters')
plt.ylabel('Silhouette score')


'### perform clustering based on optimal clusters ###'
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=0)
y_pred = kmeans.fit_predict(X_train)
cluster_center = kmeans.cluster_centers_

'### Visualize the best Kmeans clustering method with decision boundaries ### '
# Define a meshgrid to create the decision boundaries
x_min, x_max = X_train['Annual Income (k$)'].min() - 0.1, X_train['Annual Income (k$)'].max() + 0.1
y_min, y_max = X_train['Spending Score (1-100)'].min() - 0.1, X_train['Spending Score (1-100)'].max() + 0.1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 1000), np.linspace(y_min, y_max, 1000))

# Predict cluster labels for each point in the meshgrid
meshgrid_points = np.c_[xx.ravel(), yy.ravel()] # combines flattened arrays into 2D
Z = kmeans.predict(meshgrid_points)
Z = Z.reshape(xx.shape)

# Create a contour plot to visualize decision boundaries
plt.subplot(1,4,3)
plt.contourf(xx, yy, Z, alpha=0.5, cmap='viridis') # colors regions of clusters

# Scatter plot data points, color-coded by cluster
for i in range(k):
    cluster_data = X_train[y_pred == i]
    plt.scatter(cluster_data['Annual Income (k$)'], cluster_data['Spending Score (1-100)'], label=f'Cluster {i}')

plt.scatter(x=cluster_center[:, 0], y=cluster_center[:, 1], marker='*', s=300)
plt.title(f"{k} K-Means Clusters with Decision Boundaries")
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()


'### Try Kmeans with new datapoints ###'
kmeans_test = kmeans.predict(X_test)
plt.subplot(1,4,4)
for i in range(k):
    cluster_data_test = X_test[kmeans_test == i]
    plt.scatter(cluster_data_test['Annual Income (k$)'], cluster_data_test['Spending Score (1-100)'], label=f'Cluster {i}')
plt.title('Cluster affiliation of new data')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()

