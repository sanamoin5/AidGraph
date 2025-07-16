"""Feedback collection endpoints."""

from fastapi import APIRouter

router = APIRouter(prefix="/feedback", tags=["feedback"])


@router.post("/")
async def submit_feedback(feedback: dict):
    """Collect user feedback."""
    # Placeholder for storage logic
    return {"received": feedback}
