import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass, field
from datetime import datetime

LOCATIONS = [
    "https://hnhiring.com/locations/bangalore",
    "https://hnhiring.com/locations/hyderabad",
]


@dataclass
class JobPost:
    hn_user: str
    date: str
    body: str
    links: list[str] = field(default_factory=list)
    source_url: str = ""


def scrape_location(url: str) -> list[JobPost]:
    response = requests.get(url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    posts = []

    for li in soup.find_all("li", class_="job"):
        # HN username and date
        user_tag = li.find(class_="user")
        hn_user = user_tag.get_text(strip=True).split("\n")[0] if user_tag else ""
        user_anchor = user_tag.find("a") if user_tag else None
        hn_user = user_anchor.get_text(strip=True) if user_anchor else hn_user

        date_tag = li.find(class_="type-info")
        date = date_tag.get_text(strip=True) if date_tag else ""

        # Job body text
        body_div = li.find(class_="body")
        body = body_div.get_text(separator="\n", strip=True) if body_div else ""

        # All links inside the body
        links = [a["href"] for a in (body_div or li).find_all("a", href=True)]

        posts.append(JobPost(
            hn_user=hn_user,
            date=date,
            body=body,
            links=links,
            source_url=url,
        ))

    return posts


def scrape_all() -> list[JobPost]:
    all_posts = []
    for url in LOCATIONS:
        all_posts.extend(scrape_location(url))
    return all_posts


if __name__ == "__main__":
    posts = scrape_all()
    print(f"Total jobs scraped: {len(posts)}\n")
    for post in posts:
        print(f"[{post.date}] {post.hn_user} — {post.source_url}")
        print(post.body[:200])
        print()
