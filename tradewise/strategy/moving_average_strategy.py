# moving_average_strategy.py

import pandas as pd
from .base_strategy import BaseStrategy
from tradewise.utils import sma
from tradewise.quotes import StockReader

class MovingAverageStrategy(BaseStrategy):
    def moving_average_strategy(self, dma_long=200, dma_medium=50, dma_short=20):
        """
        Implement the moving average strategy over the stock data.

        Args:
            dma_long (int): Long-term moving average period (e.g., 200 days).
            dma_medium (int): Medium-term moving average period (e.g., 50 days).
            dma_short (int): Short-term moving average period (e.g., 20 days).

        Returns:
            dict: A dictionary containing strategy results for each stock symbol.
        """
        strategy_results = {}
        for stock, df in self.stock_quotes.items():
            strategy_result = self.apply_strategy(df, dma_long, dma_medium, dma_short)
            strategy_results[stock] = strategy_result
        return strategy_results

    def apply_strategy(self, df, dma_long=200, dma_medium=50, dma_short=20):
        """
        Apply the moving average strategy to a single stock's data.

        Args:
            df (DataFrame): The DataFrame containing stock quotes.
            dma_long (int): Long-term moving average period.
            dma_medium (int): Medium-term moving average period.
            dma_short (int): Short-term moving average period.

        Returns:
            dict: A dictionary containing buy and sell signals for the moving average strategy.
        """
        signals = []

        # Calculate moving averages
        dma_long = sma(df, dma_long)
        dma_medium = sma(df, dma_medium)
        dma_short = sma(df, dma_short)
        close = df['Close'].iloc[-1]
        date = df.index[-1].date()

        # Determine buy/sell signals based on strategy rules
        if (dma_long > dma_medium > dma_short) and (close < dma_short):
            signals.append({"date": date, "action": "Buy"})
        elif (dma_long < dma_medium < dma_short) and (close > dma_short):
            signals.append({"date": date, "action": "Sell"})

        return signals

# Usage example
if __name__ == "__main__":
    # Create StockReader instance
    input_filename = "stocks.txt"  # Replace with actual filename
    reader = StockReader(input_filename)

    # Read stocks list
    stocks_list = reader.read_stock_list()

    # Get stock quotes
    start_date = "2022-03-15"
    end_date = "2024-04-15"
    stock_quotes = reader.get_stock_quotes(stocks_list, start_date, end_date)

    # Create StockAnalyzer instance
    analyzer = MovingAverageStrategy(stock_quotes)

    # Implement strategy
    strategy_results = analyzer.apply_strategy(num_days=30)

    # Print strategy results
    print("Strategy Results:", strategy_results)