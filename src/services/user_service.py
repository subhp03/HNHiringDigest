from src.db.session import SessionLocal
from src.db.models import User


def get_all_emails() -> list[str]:
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return [u.email for u in users]
    finally:
        db.close()
