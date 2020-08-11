import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Emanuel Ciuca'
email['to'] = 'emanuel.ciuca@gmail.com'
email['subject'] = 'You won a million dollars'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('zerotomastery1@gmail.com', 'helloztmmyoldfriend1')
    smtp.send_message(email)
    print('all good boss!!')
