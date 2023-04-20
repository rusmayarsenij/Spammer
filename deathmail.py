from dotenv import load_dotenv
import smtplib
import os


def Скамер (mail,text,Subject,domen,login,password):
    x=f'''From: {login}
To: {mail}
Subject: {Subject}
Content-Type: text/plain; charset="UTF-8";\n\n'''
    letter=x+text
    letter = letter.encode("UTF-8")
    server = smtplib.SMTP_SSL(domen)
    server.login(login,password)
    server.sendmail(login, mail, letter)
    server.quit()
