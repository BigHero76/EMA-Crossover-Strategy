# 📊 EMA Crossover Strategy with RSI/MACD Optimization

## 🧠 Overview
This project implements a **technical trading strategy** based on the **Exponential Moving Average (EMA) crossover**, enhanced with **RSI and MACD confirmations** for more reliable entry and exit signals.  
It automatically fetches stock data, calculates technical indicators, and visualizes buy/sell decisions on a price chart.  
Backtesting is included to compare performance against a simple buy-and-hold benchmark.

---

## ⚙️ Features
- Fetches live historical data using **Yahoo Finance (`yfinance`)**
- Calculates **Fast EMA** and **Slow EMA** for crossover detection
- Integrates **RSI (Relative Strength Index)** and **MACD (Moving Average Convergence Divergence)** for signal filtering
- Generates **buy/sell signals** only when multiple confirmations align
- Includes **backtesting engine** to calculate returns
- Plots comparison chart between **strategy returns** and **buy-and-hold returns**

---

## 🧩 Strategy Logic

### 1. **EMA Crossover**
- **Buy Signal:** Fast EMA crosses **above** Slow EMA  
- **Sell Signal:** Fast EMA crosses **below** Slow EMA  

### 2. **RSI + MACD Optimization**
To reduce false positives, the raw EMA crossover signals are filtered using RSI and MACD confirmations:

#### **RSI Optimization**
- RSI acts as a **momentum gauge**.  
- A buy is **only valid** if RSI < 60 → price isn’t overbought yet, giving room for upside.  
- A sell is **only valid** if RSI > 40 → price isn’t oversold yet, confirming potential downside.  
- These thresholds (60/40) are optimized after multiple runs to find a stable balance between early entries and avoiding whipsaws.

#### **MACD Optimization**
- MACD gives a **trend strength confirmation**.  
- Buy only when **MACD > Signal Line** → bullish momentum building.  
- Sell only when **MACD < Signal Line** → bearish shift.  
- The combination ensures trades occur **only during strong, sustained trends**, not during noise.

#### **Combined Confirmation**
The final trade trigger happens when:
```text
EMA Crossover + RSI Confirmation + MACD Confirmation
This multi-filter approach significantly improves accuracy compared to standalone EMA signals.

📈 Backtesting
Backtesting is performed over a chosen date range to compare:

Strategy cumulative returns

Buy-and-hold cumulative returns

The plot below visualizes the relative performance.

<p align="center">
  <img src="https://github.com/user-attachments/assets/dc2b2355-af63-413c-b20a-5b17fb22503b" alt="EMA Strategy Chart" width="800"/>
</p>



🧰 Tech Stack
Python 3.x

pandas, numpy

matplotlib, yfinance

ta (Technical Analysis library)

🚀 How to Run
bash
Copy code
git clone https://github.com/<your-username>/ema-rsi-macd-strategy.git
cd ema-rsi-macd-strategy
pip install -r requirements.txt
python strategy.py
📊 Output Example
Blue Line: Stock Close Price

Orange Line: Fast EMA

Purple Line: Slow EMA

Green Triangles: Buy signals

Red Triangles: Sell signals

🔧 Optimization Insights
The RSI and MACD thresholds were tuned by backtesting multiple configurations:

Parameter	Range Tested	Optimal Value
RSI upper threshold	55–70	60
RSI lower threshold	30–45	40
MACD smoothing	(12, 26, 9)	Default performed best

📈 Future Improvements
Integrate hyperparameter tuning (grid search or Bayesian optimization)

Apply machine learning classifiers (Random Forest / XGBoost) to learn optimal signal patterns

Build an interactive Streamlit dashboard

Add portfolio risk metrics (Sharpe ratio, drawdown, volatility)
