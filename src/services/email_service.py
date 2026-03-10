import requests
import os
from dotenv import load_dotenv
import resend

load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")

def send_email_to_user(email: str, jobs: list):
    if not jobs:
        return

    html = "<h2>This Week's New Job Listings</h2>"
    for job in jobs:
        html += f"<p>{job.body[:300]}<br>"
        html += f"<a href='{job.source_url}'>View on HN</a></p><hr>"

    resend.api_key = RESEND_API_KEY
    r = resend.Emails.send({
        "from": "hnhiring@resend.dev",
        "to": email,
        "subject": "New Job Listings This Week",
        "html": html
    })
