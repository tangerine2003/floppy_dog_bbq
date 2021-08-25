from flask import current_app
import smtplib
from email.mime.text import MIMEText
from email.message import Message


def send_email(from_name, email, phone, subject):
    mailserver = smtplib.SMTP(
        current_app.config.get("MAIL_SERVER"), current_app.config.get("MAIL_PORT")
    )
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.login(
        current_app.config.get("MAIL_USERNAME"),
        current_app.config.get("MAIL_PASSWORD"),
    )
    message = f"""\
        From: {from_name}
        Email: {email}
        Phone: {phone}
        Subject: {subject}
        """

    m = Message()
    m["From"] = current_app.config.get("MAIL_USERNAME")
    m["To"] = current_app.config.get("MAIL_USERNAME")
    m["Subject"] = "Send mail from python!!"

    m.set_payload(message)

    # msg = MIMEText(message)

    # msg["Subject"] = "Test mail"
    # msg["From"] = current_app.config.get("MAIL_USERNAME")
    # msg["To"] = current_app.config.get("MAIL_USERNAME")
    mailserver.sendmail(
        current_app.config.get("MAIL_USERNAME"),
        current_app.config.get("MAIL_USERNAME"),
        m.as_string(),
    )
    mailserver.quit()
