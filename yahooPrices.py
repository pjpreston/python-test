import yfinance as yf


class YahooPrices:
    def get_latest_prices(self, symbols):
        if not symbols:
            return {}

        tickers = " ".join(symbols)
        data = yf.Tickers(tickers)

        prices = {}
        for symbol, ticker in data.tickers.items():
            price = self._get_latest_price(ticker)
            prices[symbol] = price
        return prices

    def get_latest_price(self, symbol):
        if not symbol:
            return None
        return self._get_latest_price(yf.Ticker(symbol))

    def _get_latest_price(self, ticker):
        fast = ticker.fast_info or {}
        price = fast.get("last_price")
        if price is not None:
            return price
        return ticker.info.get("regularMarketPrice")


if __name__ == "__main__":
    print("starting..")
    yp = YahooPrices()
    prices = yp.get_latest_prices(["AAPL", "GOOG"])
    print(prices)
    print("end")
