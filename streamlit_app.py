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

# ---- VIEW SELECTOR ----
view = st.sidebar.radio(
    "View Mode",
    ["Country", "Compare", "Analytics"]
)

# =========================
# COUNTRY VIEW
# =========================
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
    st.dataframe(cdf.reset_index(drop=True))

# =========================
# COMPARE VIEW
# =========================
elif view == "Compare":
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
    st.dataframe(cdf.reset_index(drop=True))

# =========================
# ANALYTICS VIEW
# =========================
elif view == "Analytics":
    st.subheader("Macro Analytics")

    st.write("Cross-country analytical tools including heatmaps, regime classification, and diagnostic summaries.")

    # ---- HEATMAP SECTION ----
    st.header("Heatmap Comparison")

    heat_metric = st.selectbox("Select Metric for Heatmap", [
        "GDP_Growth", "Inflation", "Policy_Rate", "TenY_Yield",
        "Debt_GDP", "Fiscal_Balance", "Current_Account", "FX_Dep_YoY"
    ])

    heat_year = st.slider("Select Year", int(df["Year"].min()), int(df["Year"].max()), int(df["Year"].max()))

    heat_df = df[df["Year"] == heat_year][["Country", heat_metric]].set_index("Country")

    st.dataframe(heat_df)

    fig = px.imshow(
        heat_df,
        text_auto=True,
        aspect="auto",
        color_continuous_scale="RdYlGn_r",
        title=f"{heat_metric} Heatmap ({heat_year})"
    )
    st.plotly_chart(fig, use_container_width=True)

    # ---- REGIME CLASSIFICATION ----
    st.header("Regime Classification")

    def classify_inflation(x):
        if x < 3: return "Low"
        elif x < 8: return "Moderate"
        elif x < 20: return "High"
        else: return "Extreme"

    def classify_monetary(policy, infl):
        real_rate = policy - infl
        if real_rate > 2: return "Restrictive"
        elif real_rate > -2: return "Neutral"
        else: return "Loose"

    def classify_fiscal(x):
        if x > -2: return "Neutral"
        elif x > -5: return "Slippage"
        else: return "Stress"

    def classify_external(x):
        if x > 2: return "Surplus"
        elif x > -2: return "Balanced"
        else: return "Deficit"

    reg_year = st.slider("Select Year for Regime Classification", int(df["Year"].min()), int(df["Year"].max()), int(df["Year"].max()))

    reg_df = df[df["Year"] == reg_year].copy()
    reg_df["Inflation_Regime"] = reg_df["Inflation"].apply(classify_inflation)
    reg_df["Monetary_Stance"] = reg_df.apply(lambda x: classify_monetary(x["Policy_Rate"], x["Inflation"]), axis=1)
    reg_df["Fiscal_Position"] = reg_df["Fiscal_Balance"].apply(classify_fiscal)
    reg_df["External_Position"] = reg_df["Current_Account"].apply(classify_external)

    st.dataframe(reg_df[[
        "Country", "Inflation_Regime", "Monetary_Stance", "Fiscal_Position", "External_Position"
    ]].reset_index(drop=True))

    # ---- DIAGNOSTIC SUMMARY ----
    st.header("Diagnostic Summary")

    for _, row in reg_df.iterrows():
        st.markdown(f"### {row['Country']} ({reg_year})")
        st.write(f"- Inflation Regime: **{row['Inflation_Regime']}**")
        st.write(f"- Monetary Stance: **{row['Monetary_Stance']}**")
        st.write(f"- Fiscal Position: **{row['Fiscal_Position']}**")
        st.write(f"- External Position: **{row['External_Position']}**")
        st.markdown("---")
