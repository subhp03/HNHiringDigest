from fastapi import APIRouter
from src.db.session import SessionLocal
from src.db.models import Job
from src.services.job_service import update_jobs

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("/")
def list_jobs():
    db = SessionLocal()
    try:
        jobs = db.query(Job).all()
        return jobs
    finally:
        db.close()


@router.post("/refresh")
def refresh_jobs():
    count = update_jobs()
    return {"scraped": count}
