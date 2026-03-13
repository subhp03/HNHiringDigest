from fastapi import APIRouter, Header, HTTPException
from src.db.session import SessionLocal
from src.db.models import Job
from src.services.job_service import update_jobs
from src.services.user_service import get_all_emails
from src.services.email_service import send_email_to_user
import os

router = APIRouter(prefix="/alerts", tags=["alerts"])

CRON_SECRET = os.getenv("CRON_SECRET")


@router.post("/send")
def send_alerts(x_cron_secret: str = Header(default=None)):
    if CRON_SECRET and x_cron_secret != CRON_SECRET:
        raise HTTPException(status_code=401, detail="Unauthorized")

    update_jobs()

    db = SessionLocal()
    try:
        jobs = db.query(Job).all()
    finally:
        db.close()

    emails = get_all_emails()
    for email in emails:
        send_email_to_user(email, jobs)

    return {"sent_to": len(emails), "jobs": len(jobs)}
