import datetime
import time
import requests

from bs4 import BeautifulSoup
import sqlite3
while True:
    connection = sqlite3.connect("test2.sl3", 5)
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS firs (city TEXT, data TEXT, time TEXT, temperature TEXT);")
    connection.commit()
    response = requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B3%D1%80%D0%B0%D1%86")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
        soup_list = soup.find_all("div",{"class":"lSide"})
        res = soup_list[0].find("p",{"class":"today-temp"})
    print(res.text)
    cur.execute(f"INSERT INTO firs VALUES ('Graz','{datetime.datetime.today().date()}','{datetime.datetime.today().time()}','{res.text}');")
    connection.commit()
    connection.close()
    time.sleep(1800)