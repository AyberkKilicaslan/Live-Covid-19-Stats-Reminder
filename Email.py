# YouTube Video: https://www.youtube.com/watch?v=mP_Ln-Z9-XY
import smtplib
USER_EMAIL = ""
MESSAGE = ""
SUBJECT = ""


def send_email(SUBJECT, MESSAGE):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login('washurhands2@gmail.com', 'sa221198')
        message = 'Subject: {}\n\n{}'.format(SUBJECT, MESSAGE)
        server.sendmail('washurhands2@gmail.com', USER_EMAIL, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


