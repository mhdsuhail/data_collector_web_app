from email.mime.text import MIMEText
import smtplib

def send_email(email,height,average_height,count):
    from_email = "put email here"
    from_password = "put the password tooo"
    # also enable less secure app in your google account
    to_email = email

    subject="Height Data"
    message="Hi, your height is<strong> %s </strong>, and the average height is %s amoung %s number of entries,"%(height, average_height,count)

    msg=MIMEText(message,'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
