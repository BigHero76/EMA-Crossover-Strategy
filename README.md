# EMA-Crossover-Strategy
EMA crossover strategy (my first quant project) using pandas, numpy and yfinance


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

1. Clone the repository

2. Create a virtual environment(highly recommended)
python -m venv venv       # command to create a new virtual environemtn(feel free to name it whatever you want)
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

3. pip install -r requirements.txt (required libraries and dependencies)
   list of libraries used in this project include:
   
   pandas==2.0.3
   numpy==1.26.4
   yfinance
   matplotlib

5. Edit the stock_symbol, fast_ema_period, and slow_ema_period variables as needed.

6. The script will generate a plot showing buy/sell signals and print the relevant data.   




