#!usr/bin/python3
# Import the email modules we'll need

import smtplib

fromaddr = 'saneprijal@gmail.com'
toaddr = 'sharmagiriaayush@gmail.com'
subject = 'Dun!Dun!Dun!'
body = "Maa ka bhosda madarchod"
#prepare the message to be sent
msg = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (fromaddr, ", ".join(toaddr), subject, body)

#gmail username and password for authentication
username = 'saneprijal@gmail.com'
password = ''   #your password
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)    #create a smtp connection object
    server.ehlo()
    server.starttls()   #secure smtp using tls
    server.ehlo()
    server.login(username, password)    #login to your gmail
    server.sendmail(fromaddr, toaddr, msg)  #send the mail to the receipent
    server.quit()
    print("success")
except smtplib.SMTPAuthenticationError:
    print(err)
