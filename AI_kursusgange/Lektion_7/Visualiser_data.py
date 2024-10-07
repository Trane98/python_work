import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Læs data
df = pd.read_csv("C:\\Program Files (x86)\\python_work\\AI_kursusgange\\Lektion_7\\CO2data.csv")

# Features og target variabel
X = df[['Weight', 'Volume']].values
y = df['CO2'].values

# Træn modellen
model = LinearRegression()
model.fit(X, y)

# Forudsigelser og MSE
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
print(f'Model MSE: {mse}')

# Visualiser regressionen i 3D
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X[:, 0], X[:, 1], y, c='b', marker='o', label='Data')

# Opret overflade for regression
x_grid, y_grid = np.meshgrid(np.linspace(X[:, 0].min(), X[:, 0].max(), 20),
                             np.linspace(X[:, 1].min(), X[:, 1].max(), 20))
z_grid = model.intercept_ + model.coef_[0] * x_grid + model.coef_[1] * y_grid

ax.plot_surface(x_grid, y_grid, z_grid, cmap='viridis', alpha=0.5)
ax.set_xlabel('Weight')
ax.set_ylabel('Volume')
ax.set_zlabel('CO2')
plt.show()



# Træn model med kun 'Weight'
weight_model = LinearRegression().fit(X[:, 0].reshape(-1, 1), y)
y_pred_weight = weight_model.predict(X[:, 0].reshape(-1, 1))
mse_weight = mean_squared_error(y, y_pred_weight)
print(f'Weight model MSE: {mse_weight}')

# Træn model med kun 'Volume'
volume_model = LinearRegression().fit(X[:, 1].reshape(-1, 1), y)
y_pred_volume = volume_model.predict(X[:, 1].reshape(-1, 1))
mse_volume = mean_squared_error(y, y_pred_volume)
print(f'Volume model MSE: {mse_volume}')



# Sammenlign MSE for modellerne
print(f'MSE for kun vægt: {mse_weight}')
print(f'MSE for kun volume: {mse_volume}')
print(f'MSE for begge features: {mse}')
