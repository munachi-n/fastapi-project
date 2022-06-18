import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List


def send_email(
    smtp_server: str,
    smtp_port: int,
    username: str,
    password: str,
    to_email: str,
    subject: str,
    body: str,
) -> bool:
    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.sendmail(username, to_email, msg.as_string())
        return True
    except Exception:
        return False


def send_mass_email(
    smtp_server: str,
    smtp_port: int,
    username: str,
    password: str,
    to_emails: List[str],
    subject: str,
    body: str,
) -> int:
    success_count = 0
    for email in to_emails:
        if send_email(smtp_server, smtp_port, username, password, email, subject, body):
            success_count += 1
    return success_count
