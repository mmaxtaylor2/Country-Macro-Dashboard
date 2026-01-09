import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Country Macro Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned/macro_clean.csv")

df = load_data()

st.title("Country Macro Dashboard")

st.markdown("This dashboard visualizes key macroeconomic indicators using a cleaned dataset.")

countries = df["Country"].unique().tolist()
selected_country = st.selectbox("Select Country", countries)

country_df = df[df["Country"] == selected_country]

st.subheader("GDP Growth (%)")
fig1 = px.line(country_df, x="Year", y="GDP_Growth", title="GDP Growth")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Inflation (%)")
fig2 = px.line(country_df, x="Year", y="Inflation", title="Inflation")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Unemployment (%)")
fig3 = px.line(country_df, x="Year", y="Unemployment", title="Unemployment")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Exchange Rate (Local → USD)")
fig4 = px.line(country_df, x="Year", y="FX_Rate", title="FX Rate")
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Full Macro Dataset")
st.dataframe(country_df)

