from fastapi import FastAPI
from routers.missions import router as missions_router

app = FastAPI()

app.include_router(missions_router)


@app.get("/")
def read_root():
    return "LUDA is live."
