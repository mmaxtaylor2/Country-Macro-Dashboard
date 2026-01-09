import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Country Macro Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned/macro_clean.csv")

df = load_data()

st.title("Country Macro Dashboard")

countries = sorted(df["Country"].unique().tolist())
view = st.sidebar.radio("View Mode", ["Country", "Compare"])

if view == "Country":
    country = st.selectbox("Select Country", countries)
    cdf = df[df["Country"] == country]

    st.subheader(f"{country}: Real Economy")
    fig1 = px.line(cdf, x="Year", y="GDP_Growth", title="GDP Growth (% YoY)")
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader(f"{country}: Prices & Monetary Policy")
    col1, col2 = st.columns(2)
    with col1:
        fig2 = px.line(cdf, x="Year", y="Inflation", title="Inflation (% YoY)")
        st.plotly_chart(fig2, use_container_width=True)
    with col2:
        fig3 = px.line(cdf, x="Year", y="Policy_Rate", title="Policy Rate (%)")
        st.plotly_chart(fig3, use_container_width=True)

    st.subheader(f"{country}: Labor Market")
    fig4 = px.line(cdf, x="Year", y="Unemployment", title="Unemployment (%)")
    st.plotly_chart(fig4, use_container_width=True)

    st.subheader(f"{country}: Fiscal & Sovereign")
    col3, col4 = st.columns(2)
    with col3:
        fig5 = px.line(cdf, x="Year", y="Debt_GDP", title="Government Debt (% GDP)")
        st.plotly_chart(fig5, use_container_width=True)
    with col4:
        fig6 = px.line(cdf, x="Year", y="Fiscal_Balance", title="Fiscal Balance (% GDP)")
        st.plotly_chart(fig6, use_container_width=True)

    st.subheader(f"{country}: External Accounts")
    col5, col6 = st.columns(2)
    with col5:
        fig7 = px.line(cdf, x="Year", y="Current_Account", title="Current Account (% GDP)")
        st.plotly_chart(fig7, use_container_width=True)
    with col6:
        fig8 = px.line(cdf, x="Year", y="FX_Dep_YoY", title="FX Depreciation (% YoY)")
        st.plotly_chart(fig8, use_container_width=True)

    st.subheader(f"{country}: Markets")
    col7, col8 = st.columns(2)
    with col7:
        fig9 = px.line(cdf, x="Year", y="TenY_Yield", title="10Y Sovereign Yield (%)")
        st.plotly_chart(fig9, use_container_width=True)
    with col8:
        fig10 = px.line(cdf, x="Year", y="Equity_YoY", title="Equity Index (% YoY)")
        st.plotly_chart(fig10, use_container_width=True)

    st.write("Underlying Data")
    st.dataframe(cdf)

else:
    st.subheader("Multi-Country Comparison")

    metric = st.selectbox("Select Indicator", [
        "GDP_Growth", "Inflation", "Policy_Rate", "TenY_Yield",
        "Debt_GDP", "Fiscal_Balance", "Current_Account", "FX_Dep_YoY", "Equity_YoY"
    ])

    selected = st.multiselect("Select Countries", countries, default=countries[:4])
    cdf = df[df["Country"].isin(selected)]

    fig = px.line(cdf, x="Year", y=metric, color="Country", title=f"{metric} Comparison")
    st.plotly_chart(fig, use_container_width=True)

    st.write("Underlying Data")
    st.dataframe(cdf[cdf["Country"].isin(selected)])

