from typing import List

def calculate_moving_average(prices: List[float], window: int) -> float:
    if window <= 0:
        raise ValueError("Window must be greater than zero")

    if len(prices) < window:
        raise ValueError("Not enough data points for the given window")

    return sum(prices[-window:]) / window
