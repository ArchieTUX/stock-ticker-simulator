import pandas as pd


class HistoricalDataReplayer:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path, parse_dates=["timestamp"])
        self.unique_times = sorted(self.df["timestamp"].unique())
        self.current_index = 0

    def step(self):
        if self.current_index >= len(self.unique_times):
            return False

        current_time = self.unique_times[self.current_index]
        subset = self.df[self.df["timestamp"] == current_time]
        prices = dict(zip(subset["ticker"], subset["price"]))
        self.current_index += 1
        return prices

    def reset(self):
        self.current_index = 0