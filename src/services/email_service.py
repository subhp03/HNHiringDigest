import os
from dotenv import load_dotenv
import resend

load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")


def _build_html(jobs: list) -> str:
    cards = ""
    for job in jobs:
        raw_links = [l for l in (job.links or "").split(",") if l.strip()]
        links_html = ""
        if raw_links:
            link_tags = " &middot; ".join(
                f'<a href="{l}" style="color:#a3a3a3;text-decoration:none;font-size:12px">{l[:60]}{"…" if len(l) > 60 else ""}</a>'
                for l in raw_links
            )
            links_html = f'<p style="margin:10px 0 0">{link_tags}</p>'

        cards += f"""
        <div style="background:#0a0a0a;border:1px solid #262626;border-radius:12px;padding:20px 24px;margin-bottom:16px;">
            <p style="color:#737373;font-size:12px;margin:0 0 10px;letter-spacing:0.02em">{job.hn_user} &nbsp;·&nbsp; {job.date or ""}</p>
            <p style="color:#ededed;font-size:14px;line-height:1.6;margin:0">{job.body[:400]}{"…" if len(job.body) > 400 else ""}</p>
            {links_html}
            <p style="margin:14px 0 0">
                <a href="{job.source_url}" style="color:#ededed;font-size:13px;text-decoration:none;border:1px solid #262626;border-radius:6px;padding:5px 12px">View on HN &rarr;</a>
            </p>
        </div>"""

    return f"""
    <!DOCTYPE html>
    <html>
    <body style="margin:0;padding:0;background:#000000;font-family:Arial,Helvetica,sans-serif;">
        <div style="max-width:600px;margin:0 auto;padding:40px 16px;">
            <h1 style="color:#ffffff;font-size:20px;font-weight:600;margin:0 0 4px">This Week on HN Hiring</h1>
            <p style="color:#737373;font-size:14px;margin:0 0 32px">Bangalore &amp; Hyderabad · {len(jobs)} listings</p>
            {cards}
            <p style="color:#404040;font-size:12px;margin-top:40px;text-align:center">
                You're receiving this because you signed up for HN job alerts.
            </p>
        </div>
    </body>
    </html>"""


def send_email_to_user(email: str, jobs: list):
    if not jobs:
        return

    resend.api_key = RESEND_API_KEY
    resend.Emails.send({
        "from": "hnhiring@resend.dev",
        "to": email,
        "subject": "This Week on HN Hiring — Bangalore & Hyderabad",
        "html": _build_html(jobs),
    })
