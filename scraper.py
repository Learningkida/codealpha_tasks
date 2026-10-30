import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
from urllib.parse import urljoin

# =====================================
# CONFIGURATION
# =====================================

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
TOTAL_PAGES = 50

books = []

# =====================================
# WEB SCRAPING
# =====================================

for page in range(1, TOTAL_PAGES + 1):

    url = BASE_URL.format(page)

    print(f"\nScraping page {page}/{TOTAL_PAGES}")

    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        response.encoding = response.apparent_encoding

        soup = BeautifulSoup(response.text, "html.parser")

        book_items = soup.find_all(
            "article",
            class_="product_pod"
        )

        for book in book_items:

            link = book.find("h3").find("a")

            # Extract title
            title = link.get("title", "").strip()

            # Extract price
            price_text = book.find(
                "p",
                class_="price_color"
            ).get_text(strip=True)

            price = float(
                price_text.replace("£", "").strip()
            )

            # Extract rating
            rating_tag = book.find(
                "p",
                class_="star-rating"
            )

            rating_word = rating_tag.get("class")[1]

            rating_map = {
                "One": 1,
                "Two": 2,
                "Three": 3,
                "Four": 4,
                "Five": 5
            }

            rating = rating_map.get(rating_word)

            # Extract availability
            availability = book.find(
                "p",
                class_="instock availability"
            ).get_text(" ", strip=True)

            # Construct correct full URL
            book_url = urljoin(url, link["href"])

            books.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Availability": availability,
                "URL": book_url
            })

        print(f"Books collected so far: {len(books)}")

        time.sleep(1)

    except requests.RequestException as e:
        print(f"Request error on page {page}: {e}")

    except (AttributeError, ValueError, IndexError) as e:
        print(f"Data extraction error on page {page}: {e}")


# =====================================
# DATASET CREATION
# =====================================

df = pd.DataFrame(books)

# Remove duplicate books
df = df.drop_duplicates(subset="URL")

# Create output directory
os.makedirs("output", exist_ok=True)

# Save CSV
file_path = "output/books_dataset.csv"

df.to_csv(
    file_path,
    index=False,
    encoding="utf-8-sig"
)

# =====================================
# FINAL REPORT
# =====================================

print("\n===================================")
print("       SCRAPING COMPLETED")
print("===================================")

print(f"Total books collected: {len(df)}")

print(f"Total duplicate records removed: {len(books) - len(df)}")

print(f"Dataset saved: {file_path}")

print("\nFirst 5 records:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nScraping process finished!")