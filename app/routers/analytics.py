from fastapi import APIRouter, HTTPException
from app.models.schemas import (
    MovingAverageRequest,
    MovingAverageResponse,
)
from app.services.calculations import calculate_moving_average

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)

@router.post(
    "/moving-average",
    response_model=MovingAverageResponse,
)
def moving_average(request: MovingAverageRequest):
    try:
        result = calculate_moving_average(
            prices=request.prices,
            window=request.window,
        )
        return {"moving_average": result}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
