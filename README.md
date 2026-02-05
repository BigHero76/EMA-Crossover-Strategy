# 📈 EMA + RSI + MACD Crossover Strategy

This project implements a **technical trading strategy** that combines:
- **Exponential Moving Averages (EMA)** for trend detection  
- **Relative Strength Index (RSI)** for momentum filtering  
- **Moving Average Convergence Divergence (MACD)** for confirmation signals  

The model was tested using **AAPL stock data (2023–2025)** via the `yfinance` API.

---

## 🧠 Strategy Logic

The base of the strategy is the **EMA crossover**:
- **Buy Signal** → when the **Fast EMA** crosses **above** the Slow EMA.  
- **Sell Signal** → when the **Fast EMA** crosses **below** the Slow EMA.  

To reduce false positives, we optimize entries with **RSI** and **MACD** conditions:
- **RSI (Relative Strength Index)** must be **above 45** during a buy (confirming upward momentum).  
- **MACD** value must be **positive** during a buy and **negative** during a sell, confirming trend strength.  

This hybrid approach filters out weak crossovers that often appear in ranging markets.

---

## 🧩 Indicators Used

| Indicator | Period | Purpose |
|------------|---------|----------|
| EMA (Fast) | 10 | Captures short-term momentum |
| EMA (Slow) | 30 | Captures long-term trend |
| RSI | 14 | Measures overbought/oversold zones |
| MACD | 12, 26, 9 | Confirms strength of price movement |

---

## 📊 Backtest Summary

**Performance Summary:**
- 📈 Strategy Return: **4.87%**  
- 💼 Buy & Hold Return: **102.33%**

While buy-and-hold outperformed in this long bull trend, the **EMA + RSI + MACD** hybrid model provides **structured entry/exit signals**, useful in volatile or sideways markets.

---

## 🪙 Sample Trade Signals

| Date | Price | RSI | MACD | Signal |
|------|--------|-----|------|--------|
| 2023-09-01 | 187.62 | 62.11 | 0.085 | 🟢 Buy |
| 2023-10-12 | 178.95 | 58.39 | -0.087 | 🔴 Sell |
| 2024-01-23 | 195.28 | 68.10 | 0.183 | 🟢 Buy |
| 2024-06-18 | 205.97 | 66.43 | -0.131 | 🔴 Sell |
| 2024-09-05 | 215.32 | 59.14 | 0.258 | 🟢 Buy |
| 2024-11-21 | 227.71 | 52.53 | -0.064 | 🔴 Sell |

*(Signals derived from EMA crossovers validated by RSI and MACD values.)*

---

## 🖼️ Visualization

The below figure shows:
- Fast and Slow EMAs  
- Buy/Sell markers  
- Trade signal data  
- Strategy vs. Buy & Hold comparison  

---

## ⚙️ Tech Stack

- **Language:** Python  
- **Libraries:** `pandas`, `matplotlib`, `ta`, `yfinance`   

---

## 🚀 Possible Extensions

- Machine Learning–based signal optimization  
- Parameter tuning using **Grid Search / Bayesian Optimization**  
- Integration with live trading APIs (Zerodha, Alpaca, etc.)  
- Portfolio-level backtesting  
