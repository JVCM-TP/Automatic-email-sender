import smtplib
from email.mime.text import MIMEText

# Connect to the email server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your_email@example.com", "your_password")

# Create the email message
message = MIMEText('This is the body of the email')
message['Subject'] = 'This is the subject'
message['To'] = 'recipient@example.com'

# Send the email
server.sendmail("sender@example.com", "recipient@example.com", message.as_string())

# Disconnect from the email server
server.quit()
