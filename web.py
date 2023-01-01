# import webbrowser

# webbrowser.open("google.com")


# sending email:

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# import smtplib

# message = MIMEMultipart()
# message["from"] = ""
# message["to"] = "test@gmail.com"
# message["subject"] = "This is a subject..."

# message.attach(MIMEText("message"))
# message.attach(MIMEImage(Path("mario.png").read_bytes()))
# with smtplib.SMTP(host="smtp.google.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("test@gmail.com", "12345678")
#     smtp.send_message(message)
#     print('SEND')


# software1.2.31


# Virtual env
# web scraping

import requests
import sqlite3
from bs4 import BeautifulSoup
# tab=newest&page=2


def crawl():
    params = {'tab': 'Active', 'page': 2}
    response = requests.get(
        "https://stackoverflow.com/questions", params=params)
    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    global questions
    global answers
    questions = soup.select(".s-post-summary--content-title")
    answers = soup.select(".s-post-summary--content-excerpt")
    insert_into_db()
# print(answers[0].getText())


def connect_to_db():

    with sqlite3.connect("stackoverflow.sqlite3") as conn:
        sql = """CREATE TABLE IF NOT EXISTS QA (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            question TEXT(500),
            answer TEXT(700)
            )
            """
        global cursor
        cursor = conn.cursor()
        cursor.execute(sql)
        return conn


def insert_into_db():
    conn = connect_to_db()
    for i in range(len(questions)):
        cursor.execute('INSERT INTO QA (question, answer) VALUES (?,?)',
                       (questions[i].select("a")[0].getText(), answers[i].getText()))

    conn.commit()

    # print(questions[i].select("a")[0].getText())
    # print(answers[i].getText())
# insert_into_db()


def show_all_data(table):
    conn = connect_to_db()
    sql = f"SELECT * FROM {table}"
    c = cursor.execute(sql)
    qa_list = []
    for item in c:
        items = {}
        items['id'] = item[0]
        items['question'] = item[1]
        items['answer'] = item[2]
        qa_list.append(items)
    return qa_list
