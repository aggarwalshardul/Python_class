import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load dataset (fix path if needed)
df = pd.read_csv("regression/house_data.csv")

# Step 2: Inspect columns
print("Columns in dataset:", df.columns)

# Step 3: Convert column names to lowercase (IMPORTANT FIX)
df.columns = df.columns.str.lower()

print("Updated Columns:", df.columns)

# Step 4: Data Cleaning
print("\nMissing Values:\n", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())

df = df.drop_duplicates()
df = df.fillna(df.select_dtypes(include=np.number).mean())

# Step 5: Feature Selection (after lowercase fix)
X = df[['area', 'bedrooms', 'bathrooms']]
y = df['price']

# Step 6: Split Data (90% train, 10% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42
)

# Step 7: Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 8: Predictions
y_pred = model.predict(X_test)

print("\nActual values:", y_test.values)
print("Predicted values:", y_pred)

# Step 9: Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
accuracy = r2 * 100

print("\n--- Model Evaluation ---")
print("RMSE:", rmse)
print("R2 Score:", r2)
print("Accuracy (%):", accuracy)

# Step 10: Model Equation
print("\n--- Model Equation ---")
print("Intercept (b0):", model.intercept_)
print("Coefficients (b1, b2, b3):", model.coef_)