from datetime import datetime
from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel
from src.db.session import SessionLocal
from src.db.models import Job
from src.services.job_service import update_jobs
import os

router = APIRouter(prefix="/jobs", tags=["jobs"])

CRON_SECRET = os.getenv("CRON_SECRET")


class JobSchema(BaseModel):
    id: int
    hn_user: str
    date: str | None
    body: str
    links: str | None
    source_url: str | None
    scraped_at: datetime | None

    class Config:
        from_attributes = True


@router.get("/", response_model=list[JobSchema])
def list_jobs():
    db = SessionLocal()
    try:
        return db.query(Job).all()
    finally:
        db.close()


@router.post("/refresh")
def refresh_jobs(x_cron_secret: str = Header(default=None)):
    if CRON_SECRET and x_cron_secret != CRON_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")
    count = update_jobs()
    return {"scraped": count}
