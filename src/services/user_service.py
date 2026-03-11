from src.db.session import SessionLocal
from src.db.models import User

"""Fetches emails from the neon auth db to send job alerts to"""
def get_all_emails() -> list[str]:
    db = SessionLocal()
    try:
        users = db.query(User).filter(User.email != None).all()
        return [u.email for u in users]
    finally:
        db.close()
