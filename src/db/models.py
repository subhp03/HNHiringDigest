from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from src.db.base import Base


class User(Base):
    """Mirror of the neon auth db"""
    __tablename__ = "user"
    __table_args__ = {"schema": "neon_auth"}

    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False, index=True)
    emailVerified = Column("emailVerified", String, nullable=True)
    image = Column(String, nullable=True)
    createdAt = Column("createdAt", DateTime(timezone=True), nullable=True)
    updatedAt = Column("updatedAt", DateTime(timezone=True), nullable=True)


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    hn_user = Column(String, nullable=False)
    date = Column(String, nullable=True)
    body = Column(Text, nullable=False, default="")
    links = Column(Text, nullable=True)
    source_url = Column(String, nullable=True)
    scraped_at = Column(DateTime, default=datetime.utcnow)
