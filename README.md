## Country Macro Dashboard

This project builds a macroeconomic monitoring dashboard for ten of the world’s largest economies. It pulls data from the World Bank API, organizes it into a structured dataset, and visualizes key indicators to evaluate growth trends, inflation pressure, and labor market conditions.

The goal is to replicate the type of analytical workflow used by research assistants and junior analysts at central banks, think tanks, and policy institutions.

## Economies Covered

United States
China
Japan
Germany
India
United Kingdom
France
Brazil
Italy
Canada

## Indicators Tracked

Category, Metric, Source:
Growth	GDP Growth (YoY %)	World Bank API

Inflation	Consumer Price Index (CPI %)	World Bank API

Labor Market	Unemployment Rate (%)	World Bank API

All data is requested on demand and saved into a processed CSV for dashboard use.

## Project Structure
Country-Macro-Dashboard/
│
├── data/
│   ├── raw/                  # (optional local storage)
│   └── cleaned/
│       └── macro_clean.csv   # final compiled dataset
│
├── src/
│   ├── data_pull.py          # pulls and saves macro data
│   ├── dashboard.py          # Streamlit dashboard UI
│
├── outputs/
│   ├── charts/               # chart export option
│   └── reports/              # future summary reports
│
└── README.md

## How to Run the Project

1. Install dependencies
pip install streamlit pandas altair requests

2. Pull data from the World Bank API
python3 src/data_pull.py

3. Launch the dashboard
streamlit run src/dashboard.py

The application will open in a browser window.

## Risk and Outlook Logic

The dashboard evaluates economic conditions using a simple rules-based approach:

Stable conditions: growth improving, controlled inflation, labor resilience
Mixed environment: conflicting signals and policy uncertainty
Elevated risk: slowing output, persistent inflation pressure, or rising labor market stress

This framework is meant to mirror how research teams flag early macro signals rather than forecast outcomes.

## Why This Project Matters

This project demonstrates capabilities relevant to policy, macro research, and global economics roles:

Data acquisition through public economic APIs
Time-series analysis and cross-country comparison
Visualization of macro indicators for interpretation
Basic economic signaling and risk classification

The structure can be expanded to include monetary policy rates, currency performance, sovereign spreads, or central bank meeting commentary.
