# --------------------------------------------
# Topic 7: Linear Regression on Placement Data
# --------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("placement.csv")
print("Dataset Loaded Successfully!")

# Check null values
print("\nNull Values:\n", df.isnull().sum())

# Splitting Independent (CGPA) & Dependent (Package)
X = df.iloc[:, 0].values.reshape(-1, 1)  # CGPA → 2D array
y = df.iloc[:, 1]  # Package

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Model coefficients
m = lr.coef_[0]
b = lr.intercept_

print("\nModel Training Complete!")
print(f"Slope (m): {m}")
print(f"Intercept (b): {b}")

# Predict on test data
y_pred = lr.predict(X_test)

# Accuracy
accuracy = r2_score(y_test, y_pred)
print(f"\nModel Accuracy (R² Score): {accuracy:.3f}")

# Prediction Example for CGPA = 9.5
cgpa = 9.5
predicted_package = lr.predict(np.array([[cgpa]]))[0]
print(f"\nPredicted Package for CGPA {cgpa}: {predicted_package:.2f} LPA")

# Visualization
plt.scatter(df["cgpa"], df["package"], label="Actual Data")
plt.plot(df["cgpa"], lr.predict(df["cgpa"].values.reshape(-1, 1)), label="Regression Line")
plt.xlabel("CGPA")
plt.ylabel("Package (LPA)")
plt.title("Linear Regression: CGPA vs Package")
plt.legend()
plt.grid(True)
plt.show()
