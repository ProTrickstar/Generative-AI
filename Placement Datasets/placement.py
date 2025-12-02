# --------------------------------------------
# Topic 6: Placement Dataset Exploration
# --------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (ensure placement.csv is in same folder)
df = pd.read_csv("placement.csv")
print("Dataset Loaded Successfully!")

# View basic structure
print("\nColumns:", df.columns)
print("\nHead:\n", df.head())
print("\nNull values:\n", df.isnull().sum())

# Basic Scatter Plot
plt.scatter(df["cgpa"], df["package"])
plt.xlabel("CGPA")
plt.ylabel("Package (LPA)")
plt.title("CGPA vs Placement Package")
plt.grid(True)
plt.show()
