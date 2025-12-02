# --------------------------------------------
# Topic 5: IMDb Dataset Handling (Pandas)
# --------------------------------------------

import pandas as pd

# Load Dataset (ensure imdb_data.csv is in the same folder)
df = pd.read_csv("imdb_data.csv")
print("IMDb Dataset Loaded Successfully!")

# Basic details
print("\nShape of dataset:", df.shape)
print("\nFirst 3 rows:\n", df.head(3))
print("\nLast 3 rows:\n", df.tail(3))

# Column overview
print("\nColumns in dataset:\n", df.columns)

# Null check
print("\nNull values in each column:\n", df.isnull().sum())

# Summary statistics
print("\nNumerical Summary:\n", df.describe())

# Language specific filtering
languages = df["original_language"].unique()
print("\nAvailable Languages:\n", languages)

# Hindi Movies extraction
hindi_movies = df[df["original_language"] == "hi"]
print("\nHindi Movies Found:", len(hindi_movies))

# Save extracted data
hindi_movies.to_csv("hindi_movies.csv", index=False)
print("\nSaved hindi_movies.csv successfully!")

# Extract top 10 movies based on revenue
top10 = df.sort_values(by="revenue", ascending=False).head(10)
print("\nTop 10 highest revenue movies:\n", top10[["title", "revenue"]])

# Movies with missing budgets
missing_budget = df[df["budget"].isnull()]
print("\nMovies with missing budget:", len(missing_budget))

# Display random records
print("\nSample 8 Movies:\n", df.sample(8))
