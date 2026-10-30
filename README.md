\# CodeAlpha Data Analytics Internship – Tasks



Three tasks from the CodeAlpha Data Analytics internship, built on data

scraped from \[books.toscrape.com](https://books.toscrape.com).



\## Tasks Completed



| Task | Description | File |

| Task 1 – Web Scraping | Scrapes book titles, prices and ratings with requests + BeautifulSoup | `scraper.py` |

| Task 2 – Exploratory Data Analysis | Cleans the dataset and explores structure, distributions and relationships with pandas | `analysis.py` |

| Task 3 – Data Visualization | Creates charts with Matplotlib and Seaborn | `visualization.py` |



\## Project Structure



```

├── scraper.py

├── analysis.py

├── visualization.py

├── output/               # generated CSV datasets

├── visualizations/       # generated charts (PNG)

├── requirements.txt

└── README.md

```



\## How to Run



```bash

pip install -r requirements.txt

python scraper.py

python analysis.py

python visualization.py

```



\## Key Findings



\- The dataset has about 1,000 books priced from roughly £10 to £60.

\- Prices are spread almost evenly across that range, with no strong skew.

\- Ratings are fairly balanced across 1–5 stars.

\- There is no meaningful relationship between price and rating.

\- The ten most expensive books all cost about £60.

\- The source site is a practice sandbox, so these patterns describe this

&#x20; dataset rather than the real book market.



\## Visualizations



!\[Price Distribution](visualizations/price\_distribution.png)

!\[Rating Distribution](visualizations/rating\_distribution.png)

!\[Price vs Rating](visualizations/price\_vs\_rating.png)

!\[Top 10 Expensive Books](visualizations/top\_10\_expensive\_books.png)



\## Tools



Python, requests, BeautifulSoup, pandas, Matplotlib, Seaborn



\## Author



Soumyajit Bera – CodeAlpha Data Analytics Intern

