# AidGraph

AidGraph is an AI-powered backend system aimed at optimizing healthcare resource allocation for underserved areas. The project combines Graph Neural Networks (GNNs) and Reinforcement Learning (RL) with a FastAPI backend and a Neo4j/PostgreSQL data layer.

## Project Structure

```
aidgraph/
    data/               # data loading and preprocessing utilities
    db/                 # database connection helpers
    models/             # GNN and RL model definitions
    api/                # FastAPI application and route modules
        routes/         # individual API route definitions
    visualization/      # scripts for generating maps and plots
    tests/              # unit tests
```

Additional top-level files include:

- `requirements.txt` – Python dependencies
- `data/` – placeholder directories for raw and processed datasets
- `Dockerfile` – container image description
- `docker-compose.yml` – development stack with databases
- `LICENSE` – project license
- `README.md` – project overview

## Development Steps

1. **Environment Setup**
   - Create a virtual environment and install dependencies from `requirements.txt`.
   - Configure local Neo4j and PostgreSQL instances.
2. **Data Collection & Loading**
   - Implement data loading utilities in `aidgraph/data/load_data.py`.
   - Populate databases with initial datasets.
3. **Model Development**
   - Build the GNN in `aidgraph/models/gnn.py` to score healthcare accessibility.
   - Implement an RL agent in `aidgraph/models/rl_agent.py` for resource deployment.
4. **API Development**
   - Define API endpoints under `aidgraph/api/routes/` and register them in `aidgraph/api/main.py`.
5. **Testing and Deployment**
   - Add unit tests inside `aidgraph/tests/`.
   - Containerize and deploy the FastAPI app.

This repository currently contains only the basic folder layout and placeholder files. You can fill in the details following the workflow described above.

## Docker Setup

The repository provides a `Dockerfile` and `docker-compose.yml` for running the stack locally. Build and start the services with:

```bash
docker compose build
docker compose up
```

The API will be available at `http://localhost:8000`.
