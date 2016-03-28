def send_email():
    import smtplib

    gmail_user = 'ccaf.raspberry@gmail.com'
    gmail_pwd = 'innovacion'
    FROM = 'raspberry pi'
    TO = 'paolo.caviedes@hiway.cl'
    SUBJECT = 'configuracion presets'
    TEXT = 'probando'

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

print send_email()
