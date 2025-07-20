import streamlit as st
from scanner import get_matching_stocks
from chart_utils import plot_chart

st.set_page_config(page_title="StockFinders", layout="wide")

st.title("📈 StockFinders - Nifty 500 Screener")

setup_option = st.selectbox("Select Setup", [
    "200 EMA Support + Green Candle",
    "30 SMA Support + Green Candle",
    "30 SMA Support + CIP + Green Candle",
    "All Time High Breakout",
    "30 & 200 EMA Combo Support"
])

if st.button("🔍 Scan Now"):
    with st.spinner("Scanning Nifty 500..."):
        matched_stocks = get_matching_stocks(setup_option)
        if matched_stocks:
            st.success(f"✅ {len(matched_stocks)} stock(s) found:")
            for stock, df in matched_stocks:
                st.subheader(stock)
                st.pyplot(plot_chart(df, setup_option))
        else:
            st.warning("No matching stocks found.")
