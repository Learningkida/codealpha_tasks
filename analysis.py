import pandas as pd
import os

# =====================================
# 1. LOAD DATASET
# =====================================

df = pd.read_csv(
    "output/books_dataset.csv",
    encoding="utf-8-sig"
)

print("Dataset loaded successfully!")

# =====================================
# 2. BASIC DATA EXPLORATION
# =====================================

print("\n========== DATASET SHAPE ==========")
print("Rows and Columns:", df.shape)

print("\n========== FIRST 10 RECORDS ==========")
print(df.head(10))

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

# =====================================
# 3. DATA QUALITY CHECK
# =====================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE RECORDS ==========")
print("Duplicate rows:", df.duplicated().sum())

print("Duplicate URLs:", df["URL"].duplicated().sum())

# =====================================
# 4. DATA CLEANING
# =====================================

# Convert Price into numeric format
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("£", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)

# Convert Rating into numeric format
# Supports both numeric ratings and old word-based ratings

rating_mapping = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

rating_words = (
    df["Rating"]
    .astype(str)
    .str.strip()
    .str.title()
    .map(rating_mapping)
)

rating_numbers = pd.to_numeric(
    df["Rating"],
    errors="coerce"
)

df["Rating"] = rating_words.fillna(rating_numbers)

# =====================================
# 5. PRICE STATISTICS
# =====================================

print("\n========== PRICE STATISTICS ==========")

print(df["Price"].describe())

print("\nAverage Price:", round(df["Price"].mean(), 2))
print("Maximum Price:", df["Price"].max())
print("Minimum Price:", df["Price"].min())
print("Median Price:", df["Price"].median())

# =====================================
# 6. RATING ANALYSIS
# =====================================

print("\n========== RATING DISTRIBUTION ==========")

print(
    df["Rating"]
    .value_counts()
    .sort_index()
)

print(
    "\nAverage Rating:",
    round(df["Rating"].mean(), 2)
)

# =====================================
# 7. AVAILABILITY ANALYSIS
# =====================================

print("\n========== AVAILABILITY ==========")

print(df["Availability"].value_counts())

# =====================================
# 8. MOST EXPENSIVE BOOKS
# =====================================

print("\n========== TOP 10 EXPENSIVE BOOKS ==========")

expensive_books = df.nlargest(10, "Price")

print(
    expensive_books[
        ["Title", "Price", "Rating"]
    ].to_string(index=False)
)

# =====================================
# 9. CHEAPEST BOOKS
# =====================================

print("\n========== TOP 10 CHEAPEST BOOKS ==========")

cheap_books = df.nsmallest(10, "Price")

print(
    cheap_books[
        ["Title", "Price", "Rating"]
    ].to_string(index=False)
)

# =====================================
# 10. SAVE CLEANED DATASET
# =====================================

os.makedirs("output", exist_ok=True)

df.to_csv(
    "output/cleaned_books_dataset.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n========== CLEANED DATASET ==========")

print("Missing values after cleaning:")
print(df.isnull().sum())

print("\n====================================")
print("EDA COMPLETED SUCCESSFULLY!")
print("Cleaned dataset saved successfully!")
print("====================================")