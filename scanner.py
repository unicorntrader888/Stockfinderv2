import yfinance as yf
import pandas as pd
from setup_logic import (
    check_200ema_support,
    check_30sma_support,
    check_30sma_cip,
    check_ath_breakout,
    check_30_200_combo
)

nifty_500_symbols = pd.read_csv("nifty500.csv")["Symbol"].tolist()

def get_matching_stocks(setup_type):
    matched_stocks = []
    for symbol in nifty_500_symbols:
        try:
            stock = yf.Ticker(f"{symbol}.NS")
            df = stock.history(period="6mo", interval="1d")

            if df.empty or len(df) < 50:
                continue

            df["20EMA"] = df["Close"].ewm(span=20).mean()
            df["30SMA"] = df["Close"].rolling(window=30).mean()
            df["200EMA"] = df["Close"].ewm(span=200).mean()

            match = False
            if setup_type == "200 EMA Support + Green Candle":
                match = check_200ema_support(df)
            elif setup_type == "30 SMA Support + Green Candle":
                match = check_30sma_support(df)
            elif setup_type == "30 SMA Support + CIP + Green Candle":
                match = check_30sma_cip(df)
            elif setup_type == "All Time High Breakout":
                match = check_ath_breakout(df)
            elif setup_type == "30 & 200 EMA Combo Support":
                match = check_30_200_combo(df)

            if match:
                matched_stocks.append((symbol, df))
        except Exception as e:
            continue

    return matched_stocks
