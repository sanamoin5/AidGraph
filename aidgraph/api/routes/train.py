"""Model training endpoints."""

from fastapi import APIRouter

router = APIRouter(prefix="/train", tags=["train"])


@router.post("/")
async def train_models():
    """Trigger model training."""
    # Placeholder for training logic
    return {"status": "training started"}


@router.get("/status")
async def training_status():
    """Retrieve current training status."""
    # Placeholder for status retrieval
    return {"status": "idle"}
