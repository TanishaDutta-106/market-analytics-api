from fastapi import APIRouter, HTTPException
from app.models.schemas import (
    MovingAverageRequest,
    MovingAverageResponse,
    VolatilityRequest,
    VolatilityResponse,
    ReturnsRequest,
    ReturnsResponse,
)
from app.services.calculations import (
    calculate_moving_average,
    calculate_volatility,
    calculate_returns,
)

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

@router.post(
    "/volatility",
    response_model=VolatilityResponse,
)
def volatility(request: VolatilityRequest):
    try:
        result = calculate_volatility(
            prices=request.prices,
        )
        return {"volatility": result}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
@router.post(
    "/returns",
    response_model=ReturnsResponse,
)
def returns(request: ReturnsRequest):
    try:
        result = calculate_returns(
            prices=request.prices,
        )
        return {"returns": result}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
