import smtplib
from email.message import EmailMessage
from string import Template
from pathlib from Path

#note this won't work if gmail less secure setting is off
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Dwan Wang'
email['to'] = 'dwanvang@gmail.com'
email['subject'] = 'email with python'

email.set_content(html.substitute({'name' = 'Dwan'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dwanvang@gmail.com', 'PASSWORD')
    smtp.send_message(email)
    print('email sent')