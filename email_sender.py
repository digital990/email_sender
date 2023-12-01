import smtplib, ssl
def send_mail(recipient, email):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender = "digitalfort911@gmail.com"
    password = "sfbjaapfoximcrij"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, email)