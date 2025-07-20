import streamlit as st
from scanner import scan_stocks
import plotly.graph_objs as go

st.set_page_config(page_title="StockFinder V2", layout="wide")

st.title("📈 StockFinder V2 - Find Your Trade Setups")

setup = st.selectbox("Select Trade Setup", [
    "200 EMA Support",
    "30 SMA Support",
    "30 SMA + CIP",
    "ATH Breakout",
    "30 + 200 Combo"
])

if st.button("🔍 Start Scan"):
    with st.spinner("Scanning Nifty 500 stocks..."):
        results = scan_stocks(setup)
        if not results:
            st.warning("No stocks found for this setup.")
        else:
            for stock, df in results.items():
                st.subheader(f"✅ {stock}")
                fig = go.Figure()
                fig.add_trace(go.Candlestick(
                    x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'],
                    name="Price"
                ))
                if "30SMA" in df.columns:
                    fig.add_trace(go.Scatter(x=df.index, y=df["30SMA"], name="30 SMA", line=dict(color='blue')))
                if "200EMA" in df.columns:
                    fig.add_trace(go.Scatter(x=df.index, y=df["200EMA"], name="200 EMA", line=dict(color='red')))
                fig.update_layout(height=400, width=1000)
                st.plotly_chart(fig)
