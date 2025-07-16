"""Endpoints for accessibility scores."""

from fastapi import APIRouter

router = APIRouter(prefix="/scores", tags=["scores"])


@router.get("/")
async def list_scores():
    """Return accessibility scores for regions."""
    # Placeholder for retrieval logic
    return {}


@router.get("/{region_id}")
async def get_score(region_id: int):
    """Return a score for a specific region."""
    # Placeholder for retrieval logic
    return {"region_id": region_id, "score": None}
