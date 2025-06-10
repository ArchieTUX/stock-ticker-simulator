# 📈 Stock Market Ticker Simulator CLI

> **A fully interactive, real-time stock market simulator with portfolio tracking, historical replay, and reporting — all from the command line.**

---

## 🎯 Features

| Feature | Description |
|--------|-------------|
| 📊 Real-Time Simulation | Simulates live stock price movements using Geometric Brownian Motion (GBM) |
| 💼 Portfolio Management | Buy/sell stocks, track gains/losses in real time |
| 🧮 Advanced Math | Uses statistical models for realistic market behavior |
| 📁 Export Reports | Save your portfolio and price history to CSV |
| 🕓 Historical Replay | Load and simulate real-world historical data |
| 🔍 Modular Design | Clean separation of concerns: easy to extend or customize |
| 🧪 Unit Tested | Includes unit tests for core components |

---

## 🧰 Technologies Used

- Python 3.8+
- `numpy` – For numerical simulations
- `pandas` – For data handling and exporting
- `PyYAML` – Configurable settings via YAML
- `rich` – Beautiful CLI output
- `tabulate` – Table formatting

---

## 🚀 Getting Started

### ✅ Prerequisites

Make sure you have Python 3 installed.

### 📦 Installation

```bash
git clone https://github.com/ArchieTUX/stock-ticker-simulator.git
cd stock-ticker-simulator
pip install -r requirements.txt
```

### ▶️ Running the Simulator

```bash
python main.py
```

---

## 🛠️ Sample Commands

| Command | Action |
|--------|--------|
| `start` | Start the market simulation |
| `tick` | Advance the market by one time step |
| `buy AAPL 10` | Buy 10 shares of AAPL at current price |
| `sell GOOG 5` | Sell 5 shares of GOOG at current price |
| `portfolio` | View current holdings and value |
| `history` | Show recent price history |
| `export` | Export reports to CSV |

---

## 📊 Example Output

```
> start
Starting market simulation...
AAPL: $150.00 | GOOG: $2800.00 | TSLA: $250.00

> buy AAPL 10
Bought 10 shares of AAPL at $150.00

> tick
Market ticked forward.
AAPL: $151.20 | GOOG: $2790.40 | TSLA: $251.00

> portfolio
Portfolio Summary:
AAPL x10 @ avg $150.00 → $1512.00 (Gain: $12.00)
Total Value: $1512.00
```

---

## 📁 Project Structure

```
stock-ticker-simulator/
├── README.md
├── requirements.txt
├── main.py
├── config/
│   └── settings.yaml
├── data_simulator/
│   ├── market_simulator.py
│   └── historical_data.py
├── portfolio_manager/
│   ├── portfolio.py
│   └── transaction_log.py
├── cli/
│   ├── cli_interface.py
│   └── input_parser.py
├── reports/
│   ├── report_generator.py
│   └── logger.py
└── tests/
    ├── test_market_simulator.py
    ├── test_portfolio.py
    └── test_cli.py
```

---

## 🧪 Testing

Run unit tests:

```bash
python -m unittest discover tests
```

---

## 📤 Exporting Reports

You can export your portfolio and price history to CSV files:

```bash
> export
Reports exported successfully!
📁 Files saved:
- portfolio_report.csv
- price_history.csv
```

---

## 📈 Simulation Model

We use **Geometric Brownian Motion (GBM)** for realistic stock price movement:

$$
S_t = S_0 \cdot e^{(μ - \frac{\sigma^2}{2})t + \sigma W_t}
$$

Where:
- $ μ $: Expected return (drift)
- $ σ $: Volatility
- $ W_t $: Random walk (Brownian motion)

You can configure these values in `config/settings.yaml`.

---

## 🧩 Extend It!

Want to make it even cooler? Try adding:

- 📈 Web UI with Flask or Streamlit  
- 🤖 AI-based trading bots  
- 📅 Dividend/split modeling  
- 🌐 Multi-user portfolios  
- 🗺️ Live market integration (e.g., Yahoo Finance API)

---

## 💬 Feedback & Contributions

Contributions are welcome! Whether it's bug fixes, new features, or performance improvements — feel free to open an issue or PR.

---

## 🙌 Credits

Built with ❤️ by Adithya  
MIT License – Feel free to use, modify, and distribute.

