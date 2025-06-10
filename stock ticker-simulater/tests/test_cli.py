import unittest
from cli.input_parser import parse_input


class TestInputParser(unittest.TestCase):
    def test_parse_buy(self):
        cmd, args = parse_input("buy AAPL 10")
        self.assertEqual(cmd, "buy")
        self.assertEqual(args, ["AAPL", "10"])

    def test_parse_tick(self):
        cmd, args = parse_input("tick")
        self.assertEqual(cmd, "tick")
        self.assertEqual(args, [])