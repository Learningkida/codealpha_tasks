
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv(
    "output/cleaned_books_dataset.csv",
    encoding="utf-8-sig"
)

# Create folder for charts
os.makedirs("visualizations", exist_ok=True)

sns.set_theme(style="whitegrid")

# =====================================
# CHART 1: PRICE DISTRIBUTION
# =====================================

plt.figure(figsize=(9, 5))

sns.histplot(
    data=df,
    x="Price",
    bins=20,
    kde=True
)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig("visualizations/price_distribution.png")
plt.show()


# =====================================
# CHART 2: RATING DISTRIBUTION
# =====================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Rating",
    order=[1, 2, 3, 4, 5]
)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating (Stars)")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig("visualizations/rating_distribution.png")
plt.show()


# =====================================
# CHART 3: PRICE VS RATING
# =====================================

plt.figure(figsize=(9, 5))

sns.boxplot(
    data=df,
    x="Rating",
    y="Price",
    order=[1, 2, 3, 4, 5]
)

plt.title("Book Price by Rating")
plt.xlabel("Rating (Stars)")
plt.ylabel("Price (£)")

plt.tight_layout()
plt.savefig("visualizations/price_vs_rating.png")
plt.show()


# =====================================
# CHART 4: TOP 10 EXPENSIVE BOOKS
# =====================================

top_books = df.nlargest(10, "Price").sort_values("Price")

plt.figure(figsize=(11, 7))

sns.barplot(
    data=top_books,
    x="Price",
    y="Title"
)

plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price (£)")
plt.ylabel("Book Title")

plt.tight_layout()
plt.savefig("visualizations/top_10_expensive_books.png")
plt.show()


print("\n================================")
print("VISUALIZATION COMPLETED!")
print("All 4 charts saved successfully.")
print("================================")
