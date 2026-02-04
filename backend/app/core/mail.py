import smtplib
from email.message import EmailMessage

from app.core.config import settings

class SmtpEmailService:
    def send(self, to_email: str, subject: str, html: str):
        msg = EmailMessage()
        msg["From"] = settings.EMAIL_FROM
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content("Your email client does not support HTML.")
        msg.add_alternative(html, subtype="html")

        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
            server.send_message(msg)

def get_email_service() -> SmtpEmailService:
    return SmtpEmailService()
