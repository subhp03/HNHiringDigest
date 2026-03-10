from src.db.models import Job
from src.db.session import SessionLocal
from src.scraping.hnhiring_scraper import scrape_all


def update_jobs() -> int:
    posts = scrape_all()

    db = SessionLocal()
    try:
        db.query(Job).delete()

        for post in posts:
            db.add(Job(
                hn_user=post.hn_user,
                date=post.date,
                body=post.body,
                links=",".join(post.links),
                source_url=post.source_url,
            ))

        db.commit()
        return len(posts)
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()