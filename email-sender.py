import smtplib
from email.mime.text import MIMEText

def send_email(sender, recipient, subject, body):
    # Connect to the email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@example.com", "your_password")

    # Create the email message
    message = MIMEText(body)
    message['Subject'] = subject
    message['To'] = recipient

    # Send the email
    server.sendmail(sender, recipient, message.as_string())

    # Disconnect from the email server
    server.quit()
