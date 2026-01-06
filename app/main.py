from fastapi import FastAPI
from app.routers import analytics

app = FastAPI(
    title="Market Analytics API",
    description="REST API for financial analytics",
    version="1.0.0"
)

app.include_router(analytics.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}
