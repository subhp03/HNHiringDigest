from fastapi import FastAPI
from src.api.routes import jobs, alerts

app = FastAPI()

app.include_router(jobs.router)
app.include_router(alerts.router)
