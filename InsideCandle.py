def identify_inside_bars(prices):
    inside_bars = []
    for i in range(1, len(prices)):
        current_high = prices[i][0]
        current_low = prices[i][1]
        previous_high = prices[i-1][0]
        previous_low = prices[i-1][1]
        
        if current_high < previous_high and current_low > previous_low:
            inside_bars.append(i)
            
    return inside_bars

def trade_inside_bars(prices, inside_bars):
    trades = []
    for bar in inside_bars:
        current_high = prices[bar][0]
        current_low = prices[bar][1]
        previous_high = prices[bar-1][0]
        previous_low = prices[bar-1][1]
        
        
        # Bearish inside bar
        if current_high < previous_high:  
            entry_price = current_low
            stop_loss = previous_high
            take_profit = entry_price - 2 * (entry_price - stop_loss)
            trades.append(("SELL", entry_price, stop_loss, take_profit))
         
         
         # Bullish inside bar   
        elif current_low > previous_low:  
            entry_price = current_high
            stop_loss = previous_low
            take_profit = entry_price + 2 * (stop_loss - entry_price)
            trades.append(("BUY", entry_price, stop_loss, take_profit))
            
    return trades

# Example usage:
# Sample price data: [high, low] for each day
prices = [
   
   
    # Format: [high, low] 
    [110, 90], 
    [105, 92],
    [108, 94],
    [100, 88],
    [97, 85],
    [95, 82]
]

inside_bars = identify_inside_bars(prices)
print("Inside Bars identified at indices:", inside_bars)

trades = trade_inside_bars(prices, inside_bars)
for trade in trades:
    print("Trade:", trade)
