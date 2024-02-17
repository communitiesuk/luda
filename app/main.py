from fastapi import FastAPI

from app.routers.missions import router as missions_router

app = FastAPI()

app.include_router(missions_router)


@app.get("/")
def read_root() -> str:
    """Root endpoint for the LUDA app."""
    return "LUDA is live."
