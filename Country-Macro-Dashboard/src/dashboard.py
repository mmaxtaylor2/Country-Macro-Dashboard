import streamlit as st
import pandas as pd
import altair as alt

# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():
    df = pd.read_csv("data/cleaned/macro_clean.csv")
    df["year"] = df["year"].astype(str)  # ensure year displays properly
    return df

df = load_data()

# =========================================================
# UI SETUP
# =========================================================
st.set_page_config(page_title="Country Macro Dashboard", layout="wide")
st.title("Country Macro Dashboard")
st.write("Analyze GDP growth, inflation, and unemployment trends for major global economies using World Bank data.")

COUNTRY_LIST = sorted(df["country"].unique())
country = st.selectbox("Select a Country", COUNTRY_LIST)
df_country = df[df["country"] == country]

st.subheader(f"Current Selection: {country}")

# Split data by indicator
gdp = df_country[df_country["indicator"] == "gdp"]
inflation = df_country[df_country["indicator"] == "inflation"]
unemp = df_country[df_country["indicator"] == "unemployment"]

# =========================================================
# CHART SECTION
# =========================================================
st.header("Macroeconomic Indicators")

# GDP Chart
gdp_chart = alt.Chart(gdp).mark_line(point=True).encode(
    x="year:N",
    y="value:Q",
    tooltip=["year", "value"]
).properties(
    title=f"GDP Growth (YoY %) — {country}"
)

# Inflation Chart
inflation_chart = alt.Chart(inflation).mark_line(point=True, color="orange").encode(
    x="year:N",
    y="value:Q",
    tooltip=["year", "value"]
).properties(
    title=f"Inflation (CPI %) — {country}"
)

# Unemployment Chart
unemp_chart = alt.Chart(unemp).mark_line(point=True, color="red").encode(
    x="year:N",
    y="value:Q",
    tooltip=["year", "value"]
).properties(
    title=f"Unemployment Rate (%) — {country}"
)

# Display charts in three columns
col1, col2, col3 = st.columns(3)
with col1:
    st.altair_chart(gdp_chart, use_container_width=True)
with col2:
    st.altair_chart(inflation_chart, use_container_width=True)
with col3:
    st.altair_chart(unemp_chart, use_container_width=True)

# =========================================================
# RISK SUMMARY / COMMENTARY
# =========================================================
st.header("Risk and Macro Outlook")

# Helper function to extract latest value
def latest_value(data):
    return float(data["value"].iloc[-1]) if len(data) > 0 else None

LATEST_GDP = latest_value(gdp)
LATEST_INF = latest_value(inflation)
LATEST_UNEMP = latest_value(unemp)

# Basic risk logic
if LATEST_GDP and LATEST_INF and LATEST_UNEMP:
    if LATEST_GDP > 2 and LATEST_INF < 3 and LATEST_UNEMP < 5:
        risk = "Stable / Soft Landing Conditions"
    elif LATEST_GDP < 1 or LATEST_INF > 6 or LATEST_UNEMP > 7:
        risk = "Elevated Risk / Recession Watch"
    else:
        risk = "Mixed Signals / Uncertain Outlook"
else:
    risk = "Insufficient data for complete assessment."

st.write(f"Current Risk Signal: {risk}")

st.markdown("""
**Interpretation Guide**
- Stable: growth improving, inflation controlled, labor market healthy
- Mixed: conflicting economic signals or uncertainty in policy direction
- Elevated: weakening growth, persistent inflation pressures, or labor-market stress
""")

# =========================================================
# FOOTER
# =========================================================
st.write("---")
st.caption("Data Source: World Bank API | Built in Python & Streamlit | Project by Max Taylor")

