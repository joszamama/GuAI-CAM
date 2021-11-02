# Send emails with python using SMTPLIB
import smtplib
import ssl
import variables as VAR

def send_email(link):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(VAR.SMPT_SERVER, VAR.PORT, context=context) as server:
        # Login with set account
        server.login(VAR.SENDER, VAR.PASSWORD)
        print('Logged IN!')

        # Sending the actual email
        server.sendmail(VAR.SENDER, VAR.RECEIVER, VAR.MESSAGE + link)
        print('Email sent!')
