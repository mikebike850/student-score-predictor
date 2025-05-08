import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Data
data = {'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'Scores': [35, 45, 50, 60, 65, 70, 75, 85, 95]}
df = pd.DataFrame(data)

# Step 2: Visualize
plt.scatter(df['Hours'], df['Scores'])
plt.title('Hours Studied vs Score')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.show()

# Step 3: Train/Test Split
X = df[['Hours']]
y = df['Scores']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predict + Evaluate
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse:.2f}")

# Step 6: New Prediction
new_data = [[6.5]]
predicted_score = model.predict(new_data)
print(f"Predicted Score for 6.5 hours of study: {predicted_score[0]:.2f}")
