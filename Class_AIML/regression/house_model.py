import pandas as pd
import numpy as np

# Step 1: Load dataset
df = pd.read_csv("regression/house_data.csv")   # change if needed

# Step 2: Inspect data
print("First 5 rows:\n", df.head())
print("\nDataset Info:\n")
print(df.info())

# Step 3: Handle missing values (only numeric columns)
df = df.fillna(df.select_dtypes(include=np.number).mean())

# Step 4: Remove duplicates
df = df.drop_duplicates()

# Step 5: Select features (X) and target (y)
X = df[['area', 'bedrooms', 'bathrooms']]
y = df['price']

# Step 6: Split data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 7: Train model
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Make predictions
y_pred = model.predict(X_test)

print("\nPredictions:\n", y_pred)

# Step 9: Evaluate model
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)

# Step 10: Model parameters
print("\nIntercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Step 11: Predict new house (BEST PRACTICE)
new_house = pd.DataFrame([[2000, 3, 2]], 
                         columns=['area', 'bedrooms', 'bathrooms'])

predicted_price = model.predict(new_house)
print("\nPredicted Price for new house:", predicted_price[0])

import matplotlib.pyplot as plt

# Scatter plot
plt.scatter(y_test, y_pred)

# Labels
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")

# Title
plt.title("Actual vs Predicted House Prices")

# Line (perfect prediction line)
plt.plot(y_test, y_test)

# Show graph
plt.show()