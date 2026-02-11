"""
FastAPI backend entrypoint for Harmony Music Player.

This is minimal runnable boilerplate to ensure the backend container can start
successfully and provide a basic health check endpoint.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

openapi_tags = [
    {"name": "Health", "description": "Service health and readiness endpoints."}
]

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
    description="Returns a simple OK response to confirm the API is running.",
    operation_id="health_check",
)
def health_check() -> dict:
    """Health check endpoint.

    Returns:
        dict: Simple status payload.
    """
    return {"status": "ok"}
