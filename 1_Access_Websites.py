import pandas as pd
import requests
from requests.exceptions import RequestException
import time

import os 
try:
    os.chdir(r"D:\SANJAY\7 GitHub Actions")
    print("[INFO] Running in Local")
except:
    print("[INFO] Running in GitHub")

# --- SETTINGS ---
INPUT_FILE = "filtered_companies.xlsx"   # your Excel file
COLUMN_NAME = "Website"        # column name in Excel containing website URLs
TIMEOUT = 10                   # seconds
PRINT_EVERY = 10             # show progress every N websites

# --- FUNCTION TO CHECK ACCESS ---
def is_accessible(url):
    try:
        if not url.startswith(("http://", "https://")):
            url = "https://" + url  # auto-fix missing scheme
        response = requests.head(url, timeout=TIMEOUT, allow_redirects=True)
        return response.status_code < 400
    except RequestException:
        return False

# --- MAIN SCRIPT ---
def main():
    df = pd.read_excel(INPUT_FILE)
    websites = df[COLUMN_NAME].dropna().unique()

    accessible = 0
    not_accessible = 0

    for i, site in enumerate(websites, start=1):
        ok = is_accessible(site)
        if ok:
            accessible += 1
        else:
            not_accessible += 1

        if i % PRINT_EVERY == 0:
            print(f"Check : {i} Websites")

        time.sleep(0.2)  # small delay to avoid rate limits

    print("\n--- FINAL REPORT ---")
    print(f"Accessible Websites : {accessible}")
    print(f"Not Accessible Websites : {not_accessible}")

if __name__ == "__main__":
    main()
