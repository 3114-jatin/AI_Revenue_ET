import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.utils import parseaddr

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER", "").strip()
EMAIL_PASS = os.getenv("EMAIL_PASS", "").strip()
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
ALERT_EMAIL_RECIPIENT = os.getenv("ALERT_EMAIL_RECIPIENT", EMAIL_USER)

if not EMAIL_USER or not EMAIL_PASS:
    raise ValueError("EMAIL_USER and EMAIL_PASS must be set in the environment or .env file")


def _normalize_email(address: str) -> str:
    if not address:
        raise ValueError("Email recipient is empty. Set a valid email address.")

    address = address.strip()
    if not address:
        raise ValueError("Email recipient is empty after stripping whitespace.")

    name, email_addr = parseaddr(address)
    if not email_addr or "@" not in email_addr:
        raise ValueError(f"Invalid email address: {address}")

    return email_addr


def send_email(to_email, subject, body):
    to_email = _normalize_email(to_email)
    from_email = _normalize_email(EMAIL_USER)

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(from_email, EMAIL_PASS)
            server.sendmail(from_email, [to_email], msg.as_string())
    except smtplib.SMTPAuthenticationError as exc:
        raise RuntimeError(
            "SMTP authentication failed. Check EMAIL_USER and EMAIL_PASS in backend/.env. "
            "If you are using Gmail, use an app password and enable SMTP access: "
            "https://support.google.com/mail/?p=BadCredentials"
        ) from exc

