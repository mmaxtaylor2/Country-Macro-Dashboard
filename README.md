# Country Macro Dashboard

https://country-macro-dashboard.streamlit.app

## Overview

This project provides a macroeconomic dashboard that visualizes GDP growth, inflation, unemployment, and FX trends across countries. The dashboard is fully interactive and built using a pre-cleaned dataset for fast deployment on Streamlit Cloud.

## Project Structure

```
data/
    cleaned/
        macro_clean.csv
src/
    data_pull.py
    clean_transform.py
streamlit_app.py
requirements.txt
README.md
```

## Key Indicators

- GDP Growth (%)
- Inflation (%)
- Unemployment (%)
- FX Rate (local currency per USD)

## Purpose

This dashboard demonstrates how macroeconomic indicators can be combined into a clean viewport suitable for:

- Economic monitoring
- Policy research
- Country comparison
- International finance analysis

## Deployment

The app uses a pre-cleaned CSV to avoid runtime API failures and deploy cleanly to Streamlit Cloud.

Main File:
```
streamlit_app.py
```

## Notes

`src/` contains the full research pipeline for data pulling and transformation, but these modules are not executed at runtime in the deployed version.

