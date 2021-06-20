from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_addr = "you@gmail.com"
to_addr = "yourfriend@gmail.com"
password ='mypassword'

server = SMTP('smtp.gmail.com',25)
server.ehlo()
server.starttls()

server.login(from_addr,password)

# go to      www.google.com/settings/security/lesssecureapps       and turn on the allow button,otherwise you will get error!

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Test mail!'

message = '''Hey,this mail is for automatic-email sending and testing purpose!
Hope this works...
Thanks in advance. '''

msg.attach(MIMEText(message,'plain'))

final = msg.as_string()
server.sendmail(from_addr,to_addr,final)
