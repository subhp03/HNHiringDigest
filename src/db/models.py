from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from src.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    hn_user = Column(String, nullable=False)
    date = Column(String, nullable=True)
    body = Column(Text, nullable=False, default="")
    links = Column(Text, nullable=True)
    source_url = Column(String, nullable=True)
    scraped_at = Column(DateTime, default=datetime.utcnow)
