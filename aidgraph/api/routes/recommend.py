"""Resource allocation recommendation endpoints."""

from fastapi import APIRouter

router = APIRouter(prefix="/recommend", tags=["recommend"])


@router.get("/")
async def recommend_deployment():
    """Return deployment recommendations."""
    # Placeholder for RL agent
    return {"recommendations": []}
