# EMA Crossover Strategy with Python

A Python script to implement and visualize an **Exponential Moving Average (EMA) crossover trading strategy** using historical stock data from Yahoo Finance.

---

## Features
- Fetches historical stock data with `yfinance`
- Calculates fast and slow EMAs
- Generates buy/sell signals based on EMA crossovers
- Visualizes stock price, EMAs, and signals using `matplotlib`
- Easy to modify for any stock symbol and date range

---

## Stock Reference

In this project, **Apple Inc. (AAPL)** stock is used as a reference for the period **January 2023 to January 2025**.  
However, using `yfinance`, historical stock data can be fetched for **any stock symbol and time period**, making this strategy easily adaptable.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/BigHero76/ema-crossover.git
cd ema-crossover

Create a virtual environment (recommended):

# Windows
python -m venv venv_new
venv_new\Scripts\activate

# macOS / Linux
python3 -m venv venv_new
source venv_new/bin/activate

Install dependencies:

pip install -r requirements.txt
Your requirements.txt should include:

pandas==2.0.3
numpy==1.26.4
yfinance
matplotlib

Usage: 
Run the script using:

python ema.py
Edit the variables in ema.py to test different stocks and EMA periods:

stock_symbol = "AAPL"
fast_ema_period = 10
slow_ema_period = 30

The script will generate a plot showing buy/sell signals, save it as ema_plot.png, and print the signal table in the terminal.

Example Output

Green ^ markers indicate buy signals.

Red v markers indicate sell signals.

Orange and Purple lines are fast EMA and slow EMA, respectively.

