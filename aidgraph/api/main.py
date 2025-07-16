"""FastAPI application initialization."""

from fastapi import FastAPI
from .routes import data, train, scores, recommend, feedback

app = FastAPI(title="AidGraph API")

app.include_router(data.router)
app.include_router(train.router)
app.include_router(scores.router)
app.include_router(recommend.router)
app.include_router(feedback.router)


@app.get("/")
def read_root():
    return {"message": "AidGraph API"}
