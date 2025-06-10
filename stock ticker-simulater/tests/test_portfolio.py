import unittest
from portfolio_manager.portfolio import Portfolio


class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.portfolio = Portfolio()

    def test_buy(self):
        self.portfolio.buy("AAPL", 10, 100)
        holdings = self.portfolio.get_holdings()
        self.assertEqual(holdings["AAPL"]["quantity"], 10)
        self.assertAlmostEqual(holdings["AAPL"]["avg_price"], 100, delta=0.01)

    def test_sell(self):
        self.portfolio.buy("AAPL", 10, 100)
        self.portfolio.sell("AAPL", 5, 110)
        holdings = self.portfolio.get_holdings()
        self.assertEqual(holdings["AAPL"]["quantity"], 5)
        transactions = self.portfolio.get_transactions()
        self.assertEqual(len(transactions), 2)