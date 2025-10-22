import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf  # type: ignore

def ema_crossover_strategy(data, fast_ema_period, slow_ema_period):
    data[f'EMA_Fast_{fast_ema_period}'] = data['Close'].ewm(span=fast_ema_period, adjust=False).mean()
    data[f'EMA_Slow_{slow_ema_period}'] = data['Close'].ewm(span=slow_ema_period, adjust=False).mean()
    data['Signal'] = 0
    data['Position'] = 0

    data.loc[(data[f'EMA_Fast_{fast_ema_period}'].shift(1) < data[f'EMA_Slow_{slow_ema_period}'].shift(1)) &
             (data[f'EMA_Fast_{fast_ema_period}'] > data[f'EMA_Slow_{slow_ema_period}']), 'Signal'] = 1

    data.loc[(data[f'EMA_Fast_{fast_ema_period}'].shift(1) > data[f'EMA_Slow_{slow_ema_period}'].shift(1)) &
             (data[f'EMA_Fast_{fast_ema_period}'] < data[f'EMA_Slow_{slow_ema_period}']), 'Signal'] = -1

    data['Position'] = data['Signal'].cumsum()
    return data

if __name__ == "__main__":
    stock_symbol = "AAPL"
    data = yf.download(stock_symbol, start="2023-01-01", end="2025-01-01")[['Close']]
    fast_ema_period = 10
    slow_ema_period = 30
    result_df = ema_crossover_strategy(data.copy(), fast_ema_period, slow_ema_period)

    # Plot
    plt.figure(figsize=(14, 7))
    plt.plot(result_df.index, result_df['Close'], label='Close Price', alpha=0.7)
    plt.plot(result_df.index, result_df[f'EMA_Fast_{fast_ema_period}'], label=f'EMA Fast ({fast_ema_period})', color='orange')
    plt.plot(result_df.index, result_df[f'EMA_Slow_{slow_ema_period}'], label=f'EMA Slow ({slow_ema_period})', color='purple')
    plt.scatter(result_df.index[result_df['Signal'] == 1],
                result_df['Close'][result_df['Signal'] == 1],
                marker='^', color='green', s=100, label='Buy Signal')
    plt.scatter(result_df.index[result_df['Signal'] == -1],
                result_df['Close'][result_df['Signal'] == -1],
                marker='v', color='red', s=100, label='Sell Signal')
    plt.title(f'EMA Crossover Strategy for {stock_symbol}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    plt.savefig("ema_plot.png", dpi=150, bbox_inches='tight')
    plt.show()

    print(result_df[result_df['Signal'] != 0][['Close', f'EMA_Fast_{fast_ema_period}', f'EMA_Slow_{slow_ema_period}', 'Signal']])

