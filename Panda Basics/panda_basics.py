# --------------------------------------------
# Topic 4: Pandas Basics
# --------------------------------------------

import pandas as pd

# Creating a Series
my_series = pd.Series(["Apple", "Banana", "Orange", "Watermelon"], name="Fruit")
print("Series:\n", my_series)

# Creating a DataFrame from list of lists
list_of_list = [["Amar", 15], ["Akbar", 14], ["Anthony", 13]]
df = pd.DataFrame(list_of_list, columns=["Name", "Age"])
print("\nDataFrame:\n", df)

# Loading a CSV file (sample path given)
print("\nReading IMDb Data (CSV)...")
df = pd.read_csv("imdb_data.csv")  # path relative for GitHub repository
print(df)

# Basic info
print("\nShape (Rows, Columns):", df.shape)
print("\nTop 5 records:\n", df.head())
print("\nLast 5 records:\n", df.tail())
print("\nRandom 5 sample records:\n", df.sample(5))

# Data info
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:\n", df.describe())

# Columns list
print("\nColumns:", df.columns)

# Duplicate values count
print("\nDuplicate rows:", df.duplicated().sum())

# Null values count
print("\nNull Values:\n", df.isnull().sum())

# Indexing & Slicing
print("\nAccess Column: Title\n", df["title"])
print("\nSelect multiple columns:\n", df[["title", "budget", "revenue"]])

print("\nSlice first 4 rows\n", df[0:4])
print("\niloc row & column slicing:\n", df.iloc[0:4, 0:3])
print("\nloc slicing with specific column names:\n", df.loc[0:4, ["title", "budget", "revenue"]])

# Unique values in a particular column
print("\nUnique languages:", df["original_language"].unique())

# Filtering
hindi_movie = df[df["original_language"] == "hi"]
print("\nHindi Movies:\n", hindi_movie)

# Save filtered data
hindi_movie.to_csv("hindi_movie.csv", index=False)
print("\nHindi movies saved as hindi_movie.csv")
