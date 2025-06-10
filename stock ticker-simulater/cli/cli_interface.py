import yaml
import os
from rich.console import Console
from rich.table import Table
from datetime import datetime
from data_simulator.market_simulator import MarketSimulator
from portfolio_manager.portfolio import Portfolio
from reports.report_generator import export_portfolio, export_price_history
from cli.input_parser import parse_input


console = Console()


def load_config():
    path = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.yaml')
    with open(path, 'r') as f:
        return yaml.safe_load(f)


def display_prices(prices):
    table = Table(title="Current Market Prices")
    table.add_column("Ticker", justify="center")
    table.add_column("Price ($)", justify="right")
    for ticker, price in sorted(prices.items()):
        table.add_row(ticker, f"{price:.2f}")
    console.print(table)


def display_portfolio(portfolio, market):
    holdings = portfolio.get_holdings()
    if not holdings:
        console.print("[yellow]Portfolio is empty.[/]")
        return

    table = Table(title="Portfolio Summary")
    table.add_column("Ticker", justify="center")
    table.add_column("Shares", justify="right")
    table.add_column("Avg Price", justify="right")
    table.add_column("Current", justify="right")
    table.add_column("Value", justify="right")
    table.add_column("Gain/Loss", justify="right")

    for ticker, info in sorted(holdings.items()):
        qty = info["quantity"]
        avg = info["avg_price"]
        cur = market.get_prices().get(ticker, 0)
        val = cur * qty
        gain = (cur - avg) * qty
        table.add_row(
            ticker,
            str(qty),
            f"{avg:.2f}",
            f"{cur:.2f}",
            f"{val:.2f}",
            f"{gain:.2f}" if gain >= 0 else f"[red]{gain:.2f}[/]"
        )

    console.print(table)
    console.print(f"Total Value: ${portfolio.value(market.get_prices()):.2f}")
    console.print(f"Total Gain: ${portfolio.gains(market.get_prices()):.2f}")


def run_cli():
    config = load_config()['stocks']
    time_step = load_config().get('time_step_minutes', 60)

    market = MarketSimulator(config, time_step)
    portfolio = Portfolio()

    console.print("[green]Welcome to the Stock Market Ticker Simulator![/]")

    running = True
    while running:
        try:
            line = input("\n> ").strip()
            cmd, args = parse_input(line)

            if cmd is None:
                continue
            elif cmd == "exit":
                running = False
            elif cmd == "start":
                console.print("[bold]Starting market simulation...[/]")
                display_prices(market.get_prices())
            elif cmd == "tick":
                market.step()
                display_prices(market.get_prices())
            elif cmd == "buy":
                if len(args) != 2:
                    console.print("[red]Usage: buy <ticker> <amount>[/]")
                    continue
                ticker, amount = args[0], float(args[1])
                price = market.get_prices().get(ticker)
                if not price:
                    console.print(f"[red]Unknown ticker: {ticker}[/]")
                    continue
                portfolio.buy(ticker, amount, price)
                console.print(f"Bought {amount} shares of {ticker} at ${price:.2f}")
            elif cmd == "sell":
                if len(args) != 2:
                    console.print("[red]Usage: sell <ticker> <amount>[/]")
                    continue
                ticker, amount = args[0], float(args[1])
                price = market.get_prices().get(ticker)
                if not price:
                    console.print(f"[red]Unknown ticker: {ticker}[/]")
                    continue
                portfolio.sell(ticker, amount, price)
                console.print(f"Sold {amount} shares of {ticker} at ${price:.2f}")
            elif cmd == "portfolio":
                display_portfolio(portfolio, market)
            elif cmd == "history":
                hist = market.get_price_history()
                for ticker, entries in hist.items():
                    console.print(f"\n{ticker} Price History:")
                    for t, p in entries[-5:]:
                        console.print(f"{t.strftime('%Y-%m-%d %H:%M')} → ${p:.2f}")
            elif cmd == "export":
                export_portfolio(portfolio, "portfolio_report.csv")
                export_price_history(market, "price_history.csv")
                console.print("[green]Reports exported successfully![/]")
            else:
                console.print(f"[red]Unknown command: {cmd}[/]")

        except KeyboardInterrupt:
            console.print("\n[red]Exiting...[/]")
            running = False
        except Exception as e:
            console.print(f"[red]Error: {e}[/]")