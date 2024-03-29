import smtplib
textfile = "textfile.txt"

recipients = []

from email.message import EmailMessage


with open(textfile) as fp:
    msg = EmailMessage()
    msg.set_content(fp.read())


msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = "Your Email"

s = smtplib.SMTP('localhost')
s.login("@email", "password")

for recipient in recipients:
    msg['To'] = recipient
    s.send_message(msg)

s.quit()
