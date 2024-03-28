# This Python code simulates a basic breakout trading strategy for Banknify on a 5-minute chart using simulated price data.
# class BreakoutTrader:


    def __init__(self, max_loss_percent, risk_reward_ratio):
        self.max_loss_percent = max_loss_percent
        self.risk_reward_ratio = risk_reward_ratio
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None

    def calculate_stop_loss_take_profit(self, entry_price, is_long):
        if is_long:
            self.stop_loss = entry_price - (entry_price * self.max_loss_percent)
            self.take_profit = entry_price + (self.risk_reward_ratio * (entry_price - self.stop_loss))
        else:
            self.stop_loss = entry_price + (entry_price * self.max_loss_percent)
            self.take_profit = entry_price - (self.risk_reward_ratio * (self.stop_loss - entry_price))

    def check_breakout(self, current_price, support, resistance):
        if current_price > resistance:
            return True, "long"
        elif current_price < support:
            return True, "short"
        else:
            return False, None

    def execute_trade(self, entry_price, is_long):
        # Simulating trade execution
        print("Trade executed at price:", entry_price)
        print("Stop Loss set at:", self.stop_loss)
        print("Take Profit set at:", self.take_profit)

        # Add actual execution code here

    def monitor_trade(self, current_price):
        if self.entry_price is not None:
            if current_price <= self.stop_loss:
                print("Stop Loss hit. Exiting trade.")
                self.entry_price = None
            elif current_price >= self.take_profit:
                print("Take Profit hit. Exiting trade.")
                self.entry_price = None

    def trade(self, current_price, support, resistance):
        if self.entry_price is None:
            breakout, direction = self.check_breakout(current_price, support, resistance)
            if breakout:
                self.entry_price = current_price
                self.calculate_stop_loss_take_profit(self.entry_price, direction == "long")
                self.execute_trade(self.entry_price, direction == "long")
        else:
            self.monitor_trade(current_price)



if __name__ == "__main__":
    trader = BreakoutTrader(max_loss_percent=0.03, risk_reward_ratio=2)
    
   
    price_data = [50, 52, 48, 55, 57, 60, 58, 54, 52, 49] 
    support_level = 48
    resistance_level = 58
    
    for i, price in enumerate(price_data):
        print("\nPrice at time t =", i, ":", price)
        trader.trade(price, support_level, resistance_level)
