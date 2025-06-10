from datetime import datetime


class TransactionLog:
    def __init__(self):
        self.log = []

    def record_buy(self, ticker, quantity, price):
        self.log.append({
            "type": "Buy",
            "ticker": ticker,
            "quantity": quantity,
            "price": price,
            "total": quantity * price,
            "timestamp": datetime.now().isoformat()
        })

    def record_sell(self, ticker, quantity, price, gain):
        self.log.append({
            "type": "Sell",
            "ticker": ticker,
            "quantity": quantity,
            "price": price,
            "total": quantity * price,
            "gain": gain,
            "timestamp": datetime.now().isoformat()
        })

    def get_log(self):
        return self.log