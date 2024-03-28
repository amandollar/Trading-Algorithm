import pandas as pd
import numpy as np

# Function to retrieve historical stock data
def get_historical_data(symbol, start_date, end_date):
    # Here you can use any method or library to fetch historical data
    # This function returns a pandas DataFrame with 'Date', 'Open', 'High', 'Low', 'Close', and 'Volume' columns
    # For demonstration purposes, let's create a sample DataFrame
    dates = pd.date_range(start_date, end_date)
    data = {'Date': dates,
            'Open': np.random.uniform(low=50, high=150, size=len(dates)),
            'High': np.random.uniform(low=50, high=150, size=len(dates)),
            'Low': np.random.uniform(low=50, high=150, size=len(dates)),
            'Close': np.random.uniform(low=50, high=150, size=len(dates)),
            'Volume': np.random.randint(low=1000, high=10000, size=len(dates))}
    df = pd.DataFrame(data)
    return df

# Function to generate signals based on Open High Low Strategy
def generate_signals(df):
    signals = pd.DataFrame(index=df.index)
    signals['Signal'] = 0
    signals['Open'] = df['Open']
    signals['High'] = df['High']
    signals['Low'] = df['Low']

    # Determine buy signals (if Open > Previous High)
    signals.loc[df['Open'] > df['High'].shift(1), 'Signal'] = 1
    
    # Determine sell signals (if Open < Previous Low)
    signals.loc[df['Open'] < df['Low'].shift(1), 'Signal'] = -1

    return signals

# Function to simulate trading based on signals
def simulate_trading(signals, initial_capital=100000):
    positions = pd.DataFrame(index=signals.index).fillna(0.0)
    positions['Stock'] = 1000 * signals['Signal']   # Buying 1000 shares per trade

    portfolio = positions.multiply(signals['Open'], axis=0)
    pos_diff = positions.diff()

    portfolio['Holdings'] = (positions.multiply(signals['Open'], axis=0)).sum(axis=1)
    portfolio['Cash'] = initial_capital - (pos_diff.multiply(signals['Open'], axis=0)).sum(axis=1).cumsum()

    portfolio['Total'] = portfolio['Cash'] + portfolio['Holdings']
    portfolio['Returns'] = portfolio['Total'].pct_change()
    return portfolio

# Example usage:
if __name__ == "__main__":
    # Define parameters
    symbol = 'AAPL'
    start_date = '2022-01-01'
    end_date = '2022-12-31'
    initial_capital = 100000
    
    # Retrieve historical data
    df = get_historical_data(symbol, start_date, end_date)
    
    # Generate signals
    signals = generate_signals(df)
    
    # Simulate trading
    portfolio = simulate_trading(signals, initial_capital)
    
    # Print the portfolio summary
    print(portfolio.tail())
