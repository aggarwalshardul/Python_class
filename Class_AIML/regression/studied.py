from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# Step 1: Data
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [35, 40, 50, 55, 65, 70, 75, 85]

# Step 2: Split data (UNSEEN DATA CREATED HERE)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 3: Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 4: Predict on unseen data
y_pred = model.predict(X_test)

print("Test Data:", X_test)
print("Actual:", y_test)
print("Predicted:", y_pred)

# Step 5: Metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)
accuracy = r2 * 100

print("\n--- Metrics on Unseen Data ---")
print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)
print("Accuracy (%):", accuracy)