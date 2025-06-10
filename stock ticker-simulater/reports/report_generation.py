import pandas as pd
from datetime import datetime


def export_portfolio(portfolio, filename="portfolio_report.csv"):
    df = pd.DataFrame(portfolio.get_transactions())
    df.to_csv(filename, index=False)


def export_price_history(simulator, filename="price_history.csv"):
    data = []
    history = simulator.get_price_history()
    for ticker, entries in history.items():
        for timestamp, price in entries:
            data.append({
                "timestamp": timestamp,
                "ticker": ticker,
                "price": price
            })
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)