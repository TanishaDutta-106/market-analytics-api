from pydantic import BaseModel
from typing import List

class MovingAverageRequest(BaseModel):
    prices: List[float]
    window: int

class MovingAverageResponse(BaseModel):
    moving_average: float
