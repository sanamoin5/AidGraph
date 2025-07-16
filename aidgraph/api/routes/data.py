"""Data upload endpoints."""

from fastapi import APIRouter, UploadFile, File

router = APIRouter(prefix="/data", tags=["data"])


@router.post("/upload")
async def upload_data(file: UploadFile = File(...)):
    """Upload a data file."""
    # Placeholder for file handling
    return {"filename": file.filename}
