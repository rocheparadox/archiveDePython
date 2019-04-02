import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

try:
    fromMailAddress = "falconpayload"
    toMailAddress = "rochemaestro@gmail.com"
    mailHost = "smtp.gmail.com"
    mailPort = "587"
    password = "justread"
    subject = "Apollo11"
    bodyText = "Tranquility base here. The Eagle has landed!"

    mail = smtplib.SMTP(mailHost,mailPort)
    mail.starttls()
    mail.login(fromMailAddress,password)
    message = MIMEMultipart()

    message["From"] = fromMailAddress
    message["To"] = toMailAddress
    message["Subject"] = subject
    message.attach(MIMEText(bodyText,"plain"))

    mail.send_message(message)

    print("Mail Sent")

except Exception as e:
    print("There was a problem in sending the mail " + e)
