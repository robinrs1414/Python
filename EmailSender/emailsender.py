import smtplib

to = input("Enter the email of receiver:\n") # email address
content = input("Enter the message:\n") # message

def sendEmail(to, content):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('sender@email','password')
    server.sendmail('sender email', to, content)
    server.quit()

sendEmail(to, content)