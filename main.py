# -*- coding:utf-8 -*-
import sqlite3
from urllib import urlopen
from bs4 import BeautifulSoup


def save_course_data():
    conn = sqlite3.connect(r'db\course_db.db')
    c = conn.cursor()
    urls = [
        'https://ke.qq.com/course/123918',
        'https://ke.qq.com/course/114576',
        'https://ke.qq.com/course/112539'
    ]
    for url in urls:
        html = urlopen(url)
        bs_obj = BeautifulSoup(html, 'html.parser')
        course = {}
        course['url'] = url
        course['Title'] = bs_obj.h1.get_text()
        course['Number'] = bs_obj.find('span', {'class': 'apply-num js-apply-num'}).get_text()
        course['Organization'] = bs_obj.find('a', {'class': 'tt-link js-agency-name'}).get_text()
        sql = "INSERT INTO Course VALUES (:url,:Title,:Number,:Organization)"
        c.execute(sql, course)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    save_course_data()
