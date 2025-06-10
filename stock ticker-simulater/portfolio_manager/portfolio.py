from collections import defaultdict
from datetime import datetime


class Portfolio:
    def __init__(self):
        self.holdings = defaultdict(lambda: {"quantity": 0, "avg_price": 0.0})
        self.transactions = []

    def buy(self, ticker, quantity, price):
        if quantity <= 0 or price <= 0:
            raise ValueError("Quantity and price must be positive.")

        existing = self.holdings[ticker]
        total_cost = existing["quantity"] * existing["avg_price"] + quantity * price
        total_quantity = existing["quantity"] + quantity
        avg_price = total_cost / total_quantity if total_quantity else 0

        self.holdings[ticker] = {"quantity": total_quantity, "avg_price": avg_price}
        self.transactions.append({
            "ticker": ticker,
            "action": "Buy",
            "quantity": quantity,
            "price": price,
            "value": quantity * price,
            "gain": 0,
            "date": datetime.now().isoformat()
        })

    def sell(self, ticker, quantity, price):
        if self.holdings[ticker]["quantity"] < quantity:
            raise ValueError(f"Not enough shares of {ticker} to sell.")

        holding = self.holdings[ticker]
        gain = (price - holding["avg_price"]) * quantity
        holding["quantity"] -= quantity

        if holding["quantity"] == 0:
            del self.holdings[ticker]

        self.transactions.append({
            "ticker": ticker,
            "action": "Sell",
            "quantity": quantity,
            "price": price,
            "value": quantity * price,
            "gain": gain,
            "date": datetime.now().isoformat()
        })

    def value(self, current_prices):
        total = sum(
            current_prices[ticker] * self.holdings[ticker]["quantity"]
            for ticker in self.holdings
            if ticker in current_prices
        )
        return round(total, 2)

    def gains(self, current_prices):
        total_gain = sum(
            (current_prices[ticker] - self.holdings[ticker]["avg_price"]) * self.holdings[ticker]["quantity"]
            for ticker in self.holdings
            if ticker in current_prices
        )
        return round(total_gain, 2)

    def get_holdings(self):
        return self.holdings

    def get_transactions(self):
        return self.transactions