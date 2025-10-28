import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import ta

def ema_rsi_macd_strategy(data, fast_ema_period=10, slow_ema_period=30):
    close_prices = data['Close'].squeeze()

    # EMAs
    data[f'EMA_Fast_{fast_ema_period}'] = close_prices.ewm(span=fast_ema_period, adjust=False).mean()
    data[f'EMA_Slow_{slow_ema_period}'] = close_prices.ewm(span=slow_ema_period, adjust=False).mean()

    # RSI
    data['RSI'] = ta.momentum.RSIIndicator(close_prices, window=14).rsi()

    # MACD
    macd = ta.trend.MACD(close_prices)
    data['MACD'] = macd.macd()
    data['MACD_Signal'] = macd.macd_signal()

    # Signals
    data['Signal'] = 0
    data.loc[
        (data[f'EMA_Fast_{fast_ema_period}'].shift(1) < data[f'EMA_Slow_{slow_ema_period}'].shift(1)) &
        (data[f'EMA_Fast_{fast_ema_period}'] > data[f'EMA_Slow_{slow_ema_period}']) &
        (data['RSI'] < 70) &
        (data['MACD'] > data['MACD_Signal']),
        'Signal'
    ] = 1

    data.loc[
        (data[f'EMA_Fast_{fast_ema_period}'].shift(1) > data[f'EMA_Slow_{slow_ema_period}'].shift(1)) &
        (data[f'EMA_Fast_{fast_ema_period}'] < data[f'EMA_Slow_{slow_ema_period}']) &
        (data['RSI'] > 30) &
        (data['MACD'] < data['MACD_Signal']),
        'Signal'
    ] = -1

    data['Position'] = data['Signal'].replace(to_replace=0, method='ffill')
    return data


def backtest_strategy(data):
    data['Daily_Return'] = data['Close'].pct_change()
    data['Strategy_Return'] = data['Daily_Return'] * data['Position'].shift(1)
    cumulative_strategy = (1 + data['Strategy_Return']).cumprod() - 1
    cumulative_buyhold = (1 + data['Daily_Return']).cumprod() - 1

    print("\n📊 Performance Summary:")
    print(f"Strategy Return: {cumulative_strategy.iloc[-1] * 100:.2f}%")
    print(f"Buy & Hold Return: {cumulative_buyhold.iloc[-1] * 100:.2f}%")
    return cumulative_strategy, cumulative_buyhold


if __name__ == "__main__":
    stock_symbol = "REDINGTON.NS"
    data = yf.download(stock_symbol, start="2023-10-28", end="2025-10-28")[["Close"]]
    result_df = ema_rsi_macd_strategy(data.copy())

    strat_ret, buy_ret = backtest_strategy(result_df)

    plt.figure(figsize=(9, 5))
    plt.plot(result_df.index, result_df['Close'], label='Close Price', alpha=0.6)
    plt.plot(result_df.index, result_df['EMA_Fast_10'], label='EMA Fast (10)', color='orange')
    plt.plot(result_df.index, result_df['EMA_Slow_30'], label='EMA Slow (30)', color='purple')
    plt.scatter(result_df.index[result_df['Signal'] == 1],
                result_df['Close'][result_df['Signal'] == 1],
                marker='^', color='green', s=100, label='Buy Signal')
    plt.scatter(result_df.index[result_df['Signal'] == -1],
                result_df['Close'][result_df['Signal'] == -1],
                marker='v', color='red', s=100, label='Sell Signal')
    plt.title(f'EMA + RSI + MACD Strategy for {stock_symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("ema_rsi_macd_plot.png", dpi=150, bbox_inches='tight')
    plt.show()

    print("\n📈 Trade Signals:")
    print(result_df[result_df['Signal'] != 0][['Close', f'EMA_Fast_10', f'EMA_Slow_30', 'RSI', 'MACD', 'MACD_Signal', 'Signal']])

