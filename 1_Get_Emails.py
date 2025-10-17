# import pandas as pd
# import os

# df = pd.read_csv("filtered_companies_100 ROWS.csv")
# print("Loaded", len(df), "rows")


# scrape.py
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = [t.text for t in soup.find_all("h2")]
print("Found titles:", titles)

