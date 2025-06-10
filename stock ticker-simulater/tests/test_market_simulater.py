import unittest
from data_simulator.market_simulator import MarketSimulator


class TestMarketSimulator(unittest.TestCase):
    def setUp(self):
        self.config = {
            "AAPL": {"initial_price": 100, "drift": 0.05, "volatility": 0.2}
        }
        self.sim = MarketSimulator(self.config, time_step_minutes=60)

    def test_initial_price(self):
        prices = self.sim.get_prices()
        self.assertAlmostEqual(prices["AAPL"], 100, delta=0.01)

    def test_step_changes_price(self):
        price_before = self.sim.get_prices()["AAPL"]
        self.sim.step()
        price_after = self.sim.get_prices()["AAPL"]
        self.assertNotEqual(price_before, price_after)