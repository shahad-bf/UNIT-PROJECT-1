import yfinance as yf
import argparse
import matplotlib.pyplot as plt
# from forex_python.converter import CurrencyRates
import pandas as pd
import os

class PyStock:

    def __init__(self, symbol: str, date_from = None, date_to = None, period = None) -> None:
        self.symbol = symbol
        self.date_from = date_from
        self.date_to = date_to
        self.period = period
      

    def get_stock_price(self):
        stock = yf.Ticker(self.symbol)

        if self.date_from and self.date_to:
            hist = stock.history(start=self.date_from, end=self.date_to)
            if hist.empty:
                return None
            return hist['Close']
        elif self.period:
            hist = stock.history(period=self.period)
            if hist.empty:
                return None
            return hist['Close']
        else:
            price = stock.info.get("currentPrice") or stock.history(period="1d")['Close'].iloc[-1]
            return pd.Series([price], index=[pd.Timestamp.today().normalize()])

   # def convert_currency_series(self, series):
      #  c = CurrencyRates()
       # converted = series.apply(lambda x: c.convert('USD', self.currency, x))
       # return converted

    def plot_graph(self, series):
        plt.figure(figsize=(10, 5))
        series.plot(title=f"{self.symbol} Stock Price Over Time")
       # plt.ylabel(f"Price ({self.currency})")
        plt.xlabel("Date")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    @classmethod
    def save_to_csv(cls, series, filename):
        df = pd.DataFrame({'Date': series.index.strftime('%Y-%m-%d'), 'Price': series.values})
        df.to_csv(filename, index=False)
        print(f" Saved to {filename}")


def main():
    parser = argparse.ArgumentParser(description=" CLI tool to fetch stock prices with graphing and CSV export.")
    parser.add_argument("symbol", help="Stock symbol like AMZN)")
    parser.add_argument("--date_from", help="Specific date for historical price (YYYY-MM-DD)")
    parser.add_argument("--date_to", help="Specific date for historical price (YYYY-MM-DD)")
   # parser.add_argument("--currency", help="Convert price to another currency (e.g. INR)")
    parser.add_argument("--range", help="Date range like 5d, 30d, 6mo, 1y (for graphing)")
    parser.add_argument("--graphed", action="store_true", help="Show graph of stock price")
    parser.add_argument("--save", help="Save data to CSV")

    args = parser.parse_args()
    symbol = args.symbol.upper()
    date_from = args.date_from
    date_to = args.date_to
    period = args.range or ("7d" if args.graphed else None)
  #  currency = args.currency.upper() if args.currency else "USD"

  #  print(f"🔍 Fetching stock data for {symbol} {f'from {date_from} to {date_to}' if date_from and date_to else ('over ' + period if period else '(latest)')}")

    try:
        pystock = PyStock(symbol=symbol, date_from=date_from, date_to=date_to, period=period)
        prices = pystock.get_stock_price()

       # if prices is None:
       #     print(" No data found for that query.")
       #     return

      #  if currency != "USD":
       #     prices = pystock.convert_currency_series(prices)

     #   if len(prices) == 1:
      
      #      print(f" {symbol} price from {date_from} to {date_to}: {prices.iloc[0]:.2f} {currency}")
       # else:
        #    print(f" Showing {len(prices)} data points from {prices.index[0].date()} to {prices.index[-1].date()}")
        #    print(f" High: {prices.max():.2f} |  Low: {prices.min():.2f} | Latest: {prices.iloc[-1]:.2f} {currency}")

        if args.graphed:
            pystock.plot_graph(prices)

        if args.save:
            pystock.save_to_csv(prices, args.save)

    except Exception as e:
        print(f" Error: {e}")


if __name__ == "__main__":
    main()
