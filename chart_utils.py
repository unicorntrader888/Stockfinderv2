import matplotlib.pyplot as plt
import pandas as pd
import os

def save_candlestick_chart(df, stock_name, setup_name):
    plt.style.use("seaborn-darkgrid")
    df = df[-60:]  # Last 60 candles
    fig, ax = plt.subplots(figsize=(8, 4))
    
    for i in range(len(df)):
        color = "green" if df["Close"].iloc[i] >= df["Open"].iloc[i] else "red"
        ax.plot([i, i], [df["Low"].iloc[i], df["High"].iloc[i]], color=color)
        ax.plot([i, i], [df["Open"].iloc[i], df["Close"].iloc[i]], color=color, linewidth=6)

    if "30SMA" in df.columns:
        ax.plot(df["30SMA"].values, label="30 SMA", color="orange", linewidth=1.5)
    if "200EMA" in df.columns:
        ax.plot(df["200EMA"].values, label="200 EMA", color="purple", linewidth=1.5)

    ax.set_title(f"{stock_name} - {setup_name}")
    ax.legend()
    ax.set_xticks([])
    ax.set_ylabel("Price")
    
    # Folder creation
    folder = f"charts/{setup_name}"
    os.makedirs(folder, exist_ok=True)
    
    # Save chart
    path = f"{folder}/{stock_name}.png"
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path
