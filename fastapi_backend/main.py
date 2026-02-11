"""
FastAPI backend entrypoint for Harmony Music Player.

This file is the canonical (preview) ASGI entrypoint used to run the backend.
It intentionally defines a *single* health check route at `/health`, and keeps
Swagger UI enabled so the endpoint can be tested in `/docs`.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

openapi_tags = [
    {"name": "Health", "description": "Service health and readiness endpoints."}
]

# NOTE:
# Swagger UI is enabled by default in FastAPI. We keep defaults (docs_url=/docs,
# redoc_url=/redoc, openapi_url=/openapi.json) so the health endpoint can be
# tested via the Swagger UI.
app = FastAPI(
    title="Harmony Music Player API",
    description="Backend API for a Spotify-like music player (boilerplate).",
    version="0.1.0",
    openapi_tags=openapi_tags,
)

# Allow local preview/dev frontend to call this backend by default.
# In production, tighten this list.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# PUBLIC_INTERFACE
@app.get(
    "/health",
    tags=["Health"],
    summary="Health check",
    description=(
        "Returns a simple OK response to confirm the API is running. "
        "This project intentionally exposes exactly one `/health` endpoint "
        "from the canonical app entrypoint (`main.py`)."
    ),
    operation_id="health_check",
)
def health_check() -> dict:
    """Health check endpoint.

    Returns:
        dict: Simple status payload.
    """
    return {"status": "ok"}
