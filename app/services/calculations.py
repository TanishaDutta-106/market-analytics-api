import math
from typing import List

def calculate_moving_average(prices: List[float], window: int) -> float:
    if window <= 0:
        raise ValueError("Window must be greater than zero")

    if len(prices) < window:
        raise ValueError("Not enough data points for the given window")

    return sum(prices[-window:]) / window

def calculate_volatility(prices: List[float]) -> float:
    if len(prices) < 2:
        raise ValueError("At least two price points are required")

    mean = sum(prices) / len(prices)
    variance = sum((p - mean) ** 2 for p in prices) / len(prices)
    return math.sqrt(variance)