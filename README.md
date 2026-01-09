# Country Macro Dashboard

https://country-macro-dashboard-mcd67k2eaasrakzj2rcwpg.streamlit.app

## Overview

A Python-based analytical dashboard that compares macroeconomic performance across countries and evaluates sovereign macro regimes through a unified visualization and diagnostic framework. The project mirrors how macroeconomists, sovereign analysts, and policy researchers assess macroeconomic conditions by combining real economy indicators, fiscal performance, external accounts, inflation dynamics, and market variables.

The objective is to enable structured cross-country comparison and surface macroeconomic patterns, vulnerabilities, and policy environments through data rather than narrative alone.

## Problem Context

Macroeconomic performance is often discussed qualitatively, but meaningful comparison requires standardized indicators and a consistent analytical approach. Growth, inflation, fiscal balances, external accounts, and sovereign yields interact in ways that determine resilience, policy space, and sovereign creditworthiness.

This dashboard introduces a structured environment for comparing those fundamentals across multiple economies and time horizons.

## Key Questions

The dashboard is designed to explore questions such as:

- How do real economy conditions differ across countries?
- How do inflation dynamics and monetary policy interact?
- Which countries run persistent deficits and which operate near balance?
- How do external balances and FX depreciation trends compare across peers?
- Which macroeconomic regimes dominate at different points in time?
- How do sovereign yields reflect macroeconomic fundamentals?

## Analytical Framework

The system organizes indicators into five sovereign macro categories:

1. Real Economy
   - GDP Growth
   - Unemployment

2. Prices & Monetary Policy
   - Inflation
   - Policy Rates

3. Fiscal
   - Debt-to-GDP
   - Fiscal Balance

4. External
   - Current Account Balance
   - FX Depreciation

5. Markets
   - 10Y Sovereign Yield
   - Equity Returns

This structure aligns with frameworks used in sovereign credit research, public finance, and international macro policy analysis.

## Data Inputs

The dataset contains annual observations for multiple countries and includes:

- Real economy data
- Prices and policy rates
- Fiscal metrics
- External accounts
- FX and market indicators

A pre-cleaned CSV is used to ensure consistent deployment without runtime API dependencies.

## Methodology

The dashboard contains three primary analytical modes:

### 1. Country View
Displays time-series indicators for a selected country across all macro categories.

### 2. Comparison View
Enables multi-country line chart comparison for a given indicator.

### 3. Analytics View
Provides higher-level diagnostic tools, including:

- Macro heatmaps
- Regime classification
- Country diagnostic summaries

Regime classification applies static macroeconomic thresholds to categorize:

- Inflation regime
- Monetary policy stance
- Fiscal position
- External balance

## Outputs

The system produces interactive outputs suitable for economic research and sovereign analysis, including:

- Time-series charts
- Cross-country comparison plots
- Heatmap visualization
- Regime diagnostic tables
- Sovereign macro summaries

## Analytical Applications

Relevant analytical use cases include:

- Sovereign macro research
- International finance analysis
- Emerging market monitoring
- Policy and think tank work
- Academic and macroeconomic instruction

## Technical Architecture

Language: Python  
Interface: Streamlit  

Core Libraries:

pandas
numpy
plotly
streamlit

## Repository Structure

data/
cleaned/
macro_clean.csv
src/
data_pull.py
clean_transform.py
streamlit_app.py
requirements.txt
README.md

## Deployment

The application is deployed on Streamlit Cloud using `streamlit_app.py` as the entry point.  
The dataset is bundled locally to avoid external data dependencies.




