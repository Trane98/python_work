import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Program Files (x86)\\python_work\\AI_kursusgange\\Lektion_9\\Lektion8-Basic-clustering\\Mall Customer Segmentation Data\\Mall_Customers.csv")

#Ser de første og sidste 5
print(df.head())
print(df.tail())

#Leder efter manglende data
print(df.isnull().sum())


# 2. Vælg kolonner (Annual Income og Spending Score)
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# 3. Split data i trænings- og testdata (80% træning, 20% test)
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# 4. Inspicer features og undersøg naturlige klynger ved at bruge silhouette score

# Liste til at gemme silhouette scores
silhouette_scores = []

# Prøv forskellige antal klynger fra 2 til 10 for at finde det bedste antal
for n_clusters in range(2, 11):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(X_train)
    
    # Beregn silhouette score
    score = silhouette_score(X_train, cluster_labels)
    silhouette_scores.append(score)
    print(f'Antal klynger: {n_clusters}, Silhouette Score: {score}')

# Plot silhouette scores for forskellige antal klynger
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Silhouette Scores for forskellige antal klynger')
plt.xlabel('Antal klynger')
plt.ylabel('Silhouette Score')
plt.show()

# 5. Brug det bedste antal klynger til at træne KMeans-modellen
best_n_clusters = silhouette_scores.index(max(silhouette_scores)) + 2  # +2 fordi range starter fra 2
kmeans = KMeans(n_clusters=best_n_clusters, random_state=42)
kmeans.fit(X_train)

# Forudsige klynger for trænings- og testdata
train_clusters = kmeans.predict(X_train)
test_clusters = kmeans.predict(X_test)

# 6. Visualisering af træningsdata med klynger
plt.scatter(X_train['Annual Income (k$)'], X_train['Spending Score (1-100)'], c=train_clusters, cmap='viridis', marker='o')
plt.title(f'Træningsdata klynger (Antal klynger: {best_n_clusters})')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

# 7. Visualisering af testdata med klynger
plt.scatter(X_test['Annual Income (k$)'], X_test['Spending Score (1-100)'], c=test_clusters, cmap='viridis', marker='o')
plt.title(f'Testdata klynger (Antal klynger: {best_n_clusters})')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()