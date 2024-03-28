import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate Exponential Moving Average (EMA)
def calculate_ema(data, window):
    weights = np.exp(np.linspace(-1., 0., window))
    weights /= weights.sum()
    ema = np.convolve(data, weights, mode='full')[:len(data)]
    ema[:window] = ema[window]
    return ema

# Function to implement 5 EMA trading strategy
def ema_trading_strategy(prices, short_window=5, long_window=20):
    # Calculate short EMA and long EMA
    short_ema = calculate_ema(prices, short_window)
    long_ema = calculate_ema(prices, long_window)
    
    # Initialize signals
    signals = pd.DataFrame(index=prices.index)
    signals['Price'] = prices
    signals['Short_EMA'] = short_ema
    signals['Long_EMA'] = long_ema
    signals['Signal'] = 0.0
    
    # Generate signals
    signals['Signal'][short_window:] = np.where(signals['Short_EMA'][short_window:] > signals['Long_EMA'][short_window:], 1.0, 0.0)   
    signals['Position'] = signals['Signal'].diff()
    
    return signals

# Example usage:
# Generate sample price data
np.random.seed(42)
dates = pd.date_range(start='2022-01-01', end='2022-12-31')
prices = pd.Series(np.random.randn(len(dates)), index=dates).cumsum()

# Apply the trading strategy
signals = ema_trading_strategy(prices)

# Plotting
plt.figure(figsize=(14, 7))
plt.plot(prices, label='Price')
plt.plot(signals['Short_EMA'], label='5 EMA')
plt.plot(signals['Long_EMA'], label='20 EMA')

# Plotting buy signals
plt.plot(signals.loc[signals.Position == 1.0].index, 
         signals.Short_EMA[signals.Position == 1.0], 
         '^', markersize=10, color='g', lw=0, label='Buy Signal')

# Plotting sell signals
plt.plot(signals.loc[signals.Position == -1.0].index, 
         signals.Short_EMA[signals.Position == -1.0], 
         'v', markersize=10, color='r', lw=0, label='Sell Signal')

plt.title('5 EMA Trading Strategy')
plt.legend()
plt.show()
