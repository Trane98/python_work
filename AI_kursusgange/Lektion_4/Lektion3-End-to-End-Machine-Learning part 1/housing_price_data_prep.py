import gzip
import pandas as pd
from matplotlib import pyplot as plt

'## open file and read contents ##'
with gzip.open('housing.tgz', 'rb') as file:
    housing = pd.read_csv(file)
    housing.rename(columns={'housing/': 'longitude'}, inplace=True)

'## Take a look at the data ##'
head_of_data = housing.head()
description_of_data = housing.describe()
information_of_data = housing.info()


housing.hist(bins=50, figsize=(12,8))
plt.title('Histograms of attributes')

#
housing.plot(kind="scatter", x="longitude", y="latitude", grid=True, alpha=0.2)
plt.title('Housing placement')

housing.plot(kind="scatter", x="longitude", y="latitude", grid=True,
             s=housing["population"] / 100, label="population",
             c="median_house_value", cmap="viridis", colorbar=True,
             legend=True, sharex=False, figsize=(10, 7))
plt.title('Housing placement with median house value and population (size of circles -> bigger circle = bigger population)')

# compute the pearson r correlation (assuming bivariate normal distribution)
'''
The Pearson correlation coefficient, often denoted as "r" or "Pearson's r," is a statistic that measures the 
linear relationship between two continuous variables. It quantifies the strength and direction of the linear 
association between two variables. The value of "r" ranges from -1 to 1:

The Pearson correlation coefficient measures the degree to which the data points in a scatterplot cluster around a straight line.

'''
corr_matrix = housing.corr()

# what correlates with median house value --> the value we want to make a model to predict.
print(corr_matrix['median_house_value'].sort_values(ascending=False))




# look at the most correlating attribute with median house value
housing.plot(kind="scatter", x="median_income", y="median_house_value", alpha=0.1, grid=True)
plt.title('most correlating attribute with median house value')

plt.show()