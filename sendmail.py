import smtplib
import functools

def SendMail (user,password,mailFrom,mailTo,mailSubject,mailBody):
    message = f'''From: {mailFrom}
    Subject: {mailSubject}

    {mailBody}'''
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent, congratulations!!!')
    except:
        print('error sending email')


mailFrom = 'Your automation system'
mailTo = ['unknown1@gmail.com','unknown2@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = '''Just a check program 3rd times'''

user = 'unknown3@gmail.com'
password = 'password'


SendMailGmail = functools.partial(SendMail,user,password,mailSubject='Execution alert')
SendMailGmail(mailFrom=mailFrom,mailTo=mailTo,mailBody=mailBody)