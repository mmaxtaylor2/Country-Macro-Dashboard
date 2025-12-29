import pandas as pd
import requests

# ----------------------------------------
# Top 10 Economies — Country + WB Codes
# ----------------------------------------
COUNTRIES = {
    "United States": "USA",
    "China": "CHN",
    "Japan": "JPN",
    "Germany": "DEU",
    "India": "IND",
    "United Kingdom": "GBR",
    "France": "FRA",
    "Brazil": "BRA",
    "Italy": "ITA",
    "Canada": "CAN"
}

# ----------------------------------------
# World Bank Indicators
# ----------------------------------------
INDICATORS = {
    "gdp": "NY.GDP.MKTP.KD.ZG",          # GDP growth (annual %)
    "inflation": "FP.CPI.TOTL.ZG",       # Inflation (CPI %)
    "unemployment": "SL.UEM.TOTL.ZS"     # Unemployment rate (%)
}

# ----------------------------------------
# Fetch data from World Bank
# ----------------------------------------
def fetch_world_bank_data(country_code, indicator_code):
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}?format=json&per_page=60"
    response = requests.get(url)
    try:
        data = response.json()[1]  # API returns [metadata, data]
        records = [
            {
                "country": d["country"]["value"],
                "year": d["date"],
                "value": d["value"]
            }
            for d in data if d["value"] is not None
        ]
        return pd.DataFrame(records)
    except:
        return pd.DataFrame()

# ----------------------------------------
# Build full dataset
# ----------------------------------------
def build_dataset():
    frames = []
    for country, code in COUNTRIES.items():
        print(f"Pulling data for {country}...")
        for name, indicator in INDICATORS.items():
            df = fetch_world_bank_data(code, indicator)
            if not df.empty:
                df["indicator"] = name
                frames.append(df)

    final_df = pd.concat(frames, ignore_index=True)
    final_df.to_csv("data/cleaned/macro_clean.csv", index=False)
    print("✔ Dataset created at data/cleaned/macro_clean.csv")

# ----------------------------------------
# Run script
# ----------------------------------------
if __name__ == "__main__":
    build_dataset()

