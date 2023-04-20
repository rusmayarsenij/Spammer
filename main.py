import os.path
import argparse
import json

import deathmail
from dotenv import load_dotenv
import os

def main():

    if not os.path.isfile('.env'):
        print("Нет ну это уже выходит за рамки разумного. С таким уровнем легче пахать, чем у компьютерах лазить. Укажи правильный путь!")
        exit()
    load_dotenv()

    parser = argparse.ArgumentParser(
            description='Почтовая программа'
    )
    parser.add_argument('-s', help='Аргумент для указания с темой письма')
    parser.add_argument('-m', help='Аргумент для указания файла с почтами')
    parser.add_argument('-t', help='Аргумент для указания файла')
    textfile=parser.parse_args().t
    mailsfile = parser.parse_args().m
    subject=parser.parse_args().s
    try:
        with open(textfile, "r",encoding="UTF-8") as my_file:
            text = my_file.read()
    except FileNotFoundError:
        print("Я тут старался, код писал. А ты его мучаешь! Укажи путь правильный!")
        exit()

    try:
        with open(mailsfile,'r')as file:
            mails=file.read()
    except FileNotFoundError:
        print("Мы конечно предполагали такой случай. Но мы только ПРЕДПОЛАГАЛИ! Путь к почте нормальный напиши!")
        exit()
    mails=json.loads(mails)
    domen='smtp.yandex.ru:465'
    login=os.getenv("LOGIN")
    password=os.getenv("PASSWORD")
    for mail in mails:
        deathmail.Скамер(mail,text,subject,domen,login,password)

if __name__=="__main__":
    main()
