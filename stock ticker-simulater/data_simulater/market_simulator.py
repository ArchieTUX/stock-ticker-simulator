import numpy as np
from datetime import datetime, timedelta


class MarketSimulator:
    def __init__(self, stocks_config, time_step_minutes=60):
        self.stocks = list(stocks_config.keys())
        self.params = {ticker: {
            'S0': data['initial_price'],
            'mu': data['drift'],
            'sigma': data['volatility'],
            'price': data['initial_price']
        } for ticker, data in stocks_config.items()}
        self.time_step_days = time_step_minutes / (24 * 60)
        self.current_time = datetime.now()
        self.price_history = {ticker: [(self.current_time, data['price'])] for ticker, data in self.params.items()}

    def step(self):
        self.current_time += timedelta(minutes=self.time_step_days * 24 * 60)
        for ticker in self.stocks:
            S = self.params[ticker]['price']
            mu = self.params[ticker]['mu']
            sigma = self.params[ticker]['sigma']

            dt = self.time_step_days
            dW = np.random.normal(0, np.sqrt(dt))
            dS = S * (mu * dt + sigma * dW)
            new_price = S + dS

            self.params[ticker]['price'] = round(new_price, 2)
            self.price_history[ticker].append((self.current_time, round(new_price, 2)))

    def get_prices(self):
        return {ticker: data['price'] for ticker, data in self.params.items()}

    def get_price_history(self):
        return self.price_history