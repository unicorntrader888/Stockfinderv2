import yfinance as yf
import pandas as pd

def fetch_data(stock_symbol, interval, period="3mo"):
    try:
        df = yf.download(stock_symbol, interval=interval, period=period, progress=False)
        df.dropna(inplace=True)
        df["20EMA"] = df["Close"].ewm(span=20, adjust=False).mean()
        df["30SMA"] = df["Close"].rolling(window=30).mean()
        df["200EMA"] = df["Close"].ewm(span=200, adjust=False).mean()
        return df
    except Exception as e:
        print(f"Error fetching data for {stock_symbol}: {e}")
        return pd.DataFrame()
