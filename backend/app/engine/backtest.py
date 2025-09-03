# backend/app/engine/backtest.py

def run_backtest(strategy_name: str = "equal_weight") -> dict:
    return {
        "nav": [100, 101.5, 103.2, 104.9],
        "returns": [0.0, 0.015, 0.0167, 0.0165],
        "weights": {
            "AAPL": 0.25,
            "MSFT": 0.25,
            "GOOGL": 0.25,
            "AMZN": 0.25,
        },
        "config": {
            "strategy": strategy_name,
            "rebalance": "monthly"
        }
    }

