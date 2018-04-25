#!usr/bin/python3
# Import the email modules we'll need

import smtplib

fromaddr = 'saneprijal@gmail.com'
toaddr = 'sharmagiriaayush@gmail.com'
subject = 'Dun!Dun!Dun!'
body = "Maa ka bhosda madarchod"
msg = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (fromaddr, ", ".join(toaddr), subject, body)
username = 'saneprijal@gmail.com'
password = '9843440022'
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, msg)
    server.quit()
    print("success")
except smtplib.SMTPAuthenticationError:
    print(err)
