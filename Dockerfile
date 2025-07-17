# Basic AidGraph API image
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY aidgraph ./aidgraph
COPY README.md ./README.md

EXPOSE 8000

CMD ["uvicorn", "aidgraph.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
