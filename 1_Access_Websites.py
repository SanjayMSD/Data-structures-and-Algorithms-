import pandas as pd
import requests
from requests.exceptions import RequestException
import time
import os

# --- ENVIRONMENT DETECTION ---
try:
    os.chdir(r"D:\SANJAY\7 GitHub Actions")
    print("[INFO] Running in Local")
except Exception:
    print("[INFO] Running in GitHub")

# --- SETTINGS ---
INPUT_FILE = "filtered_companies.xlsx"   # Excel file name
COLUMN_NAME = "Website"                  # Column containing website URLs
TIMEOUT = 10                             # seconds
PRINT_EVERY = 10                         # progress update after N checks
SCAN_LIMIT = None                         # number of websites to check (None = all)

# --- FUNCTION TO CHECK ACCESSIBILITY ---
def is_accessible(url):
    try:
        url = str(url).strip()
        if not url:
            return False
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        response = requests.head(url, timeout=TIMEOUT, allow_redirects=True)
        return response.status_code < 400
    except RequestException:
        return False
    except Exception:
        return False

# --- MAIN SCRIPT ---
def main():
    start_time = time.time()  # start timer

    df = pd.read_excel(INPUT_FILE)
    websites = df[COLUMN_NAME].dropna().astype(str).str.strip().unique()

    total_sites = len(websites)
    if SCAN_LIMIT:
        websites = websites[:SCAN_LIMIT]
        print(f"\n🔍 Scanning first {SCAN_LIMIT} of {total_sites} websites...\n")
    else:
        print(f"\n🔍 Scanning all {total_sites} websites...\n")

    accessible = 0
    not_accessible = 0

    for i, site in enumerate(websites, start=1):
        ok = is_accessible(site)
        if ok:
            accessible += 1
        else:
            not_accessible += 1

        if i % PRINT_EVERY == 0 or i == len(websites):
            print(f"Check : {i} Websites")

        time.sleep(0.2)  # avoid rate limits

    # --- Final Report ---
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)

    print("\n--- FINAL REPORT ---")
    print(f"Accessible Websites : {accessible}")
    print(f"Not Accessible Websites : {not_accessible}")
    print(f"Total Checked : {accessible + not_accessible}")
    print(f"⏱️ Time Taken : {int(minutes)} min {int(seconds)} sec")

if __name__ == "__main__":
    main()

