import yaml
import os
from cli.cli_interface import run_cli
from data_simulator.historical_data import HistoricalDataReplayer
from data_simulator.market_simulator import MarketSimulator


def load_config():
    path = os.path.join(os.path.dirname(__file__), 'config', 'settings.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def choose_mode():
    print("Select mode:")
    print("1. Real-time Simulation")
    print("2. Historical Replay")

    choice = input("Enter 1 or 2: ").strip()
    if choice == "2":
        hist_file = input("Enter historical CSV file path: ")
        return HistoricalDataReplayer(hist_file)
    else:
        config = load_config()['stocks']
        time_step = load_config().get('time_step_minutes', 60)
        return MarketSimulator(config, time_step)


if __name__ == "__main__":
    market = choose_mode()
    run_cli(market)