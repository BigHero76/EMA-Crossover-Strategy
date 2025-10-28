# 📈 EMA Crossover Strategy (with RSI + MACD Optimization)

This project implements a trading strategy that combines **Exponential Moving Average (EMA)** crossovers with **RSI** and **MACD** confirmations to generate buy/sell signals.  
The strategy is tested and visualized using **Python**, **pandas**, **matplotlib**, and **yfinance**.

---

## 🧠 Strategy Overview

### 🔹 Core Concept:
- The **EMA Crossover Strategy** looks for moments when a **short-term EMA** crosses a **long-term EMA**:
  - **Buy Signal** → Fast EMA crosses *above* Slow EMA  
  - **Sell Signal** → Fast EMA crosses *below* Slow EMA

### 🔹 RSI + MACD Optimization:
To reduce false signals and improve entry accuracy:
- **RSI (Relative Strength Index)**  
  - Filters overbought (>70) and oversold (<30) regions  
  - We only take buy signals when RSI < 70  
  - And sell signals when RSI > 30  
- **MACD (Moving Average Convergence Divergence)**  
  - Confirms momentum direction  
  - Buy only if MACD > MACD Signal  
  - Sell only if MACD < MACD Signal  

This combination ensures the trade aligns with **momentum and trend strength**, not just EMA crosses.

---

## ⚙️ Features
✅ Fetches stock data automatically using [yfinance](https://pypi.org/project/yfinance/)  
✅ Calculates **EMA**, **RSI**, and **MACD** using [ta](https://technical-analysis-library-in-python.readthedocs.io/en/latest/)  
✅ Generates **buy/sell markers** on the price chart  
✅ Backtests against a **Buy & Hold** baseline  
✅ Saves the result plots locally for analysis  

---

## 📊 Sample Output

<p align="center">
  <img src="https://github.com/user-attachments/assets/dc2b2355-af63-413c-b20a-5b17fb22503b" alt="EMA RSI MACD Strategy Chart" width="850"/>
</p>

> 🟢 **Green Arrows** = Buy signals  
> 🔴 **Red Arrows** = Sell signals  
> Orange/Purple lines = Fast and Slow EMAs respectively  

---

## 📈 Performance Summary (Example)
| Metric | Result |
|:--------|:--------|
| Strategy Return | 42.57% |
| Buy & Hold Return | 25.31% |
| Optimization Filters | RSI + MACD Confirmation |
