import pymysql.cursors
import requests
import re
from bs4 import BeautifulSoup
import json
import time

class reader_diary:
        def __init__(self,id,uid,bookid):
                self.id=id
                self.uid=uid
                self.bookid=bookid

        def print(self):
                print(self.id,
                self.uid,
                self.bookid)
class book:
    def __init__(self, bookid,bookname,author,keyword,brief_content):
        self.bookid = bookid
        self.bookname=bookname
        self.author=author
        self.keyword=keyword
        self.brief_content=brief_content

    def print(self):
        print(self.bookid,
        self.bookname,
        self.author,
        self.keyword,
        self.brief_content)

class combination:
    def __init__(self, id, uid, bookid,bookname,author,keyword,brief_content):
        self.id = id
        self.uid = uid
        self.bookid = bookid
        self.bookname = bookname
        self.author = author
        self.keyword = keyword
        self.brief_content = brief_content

    def print(self):
        print(self.id,
              self.uid,
              self.bookid,
              self.bookname,
              self.author,
              self.keyword,
              self.brief_content
              )


count=0

def insert(c):
    # 初始化connection
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='000000',
        db='wenquan',
        charset='utf8mb4',
    )
    cursor = connection.cursor()

    global count
    count = count + 1

    sql = ''
    sql = "INSERT INTO reader_collect_diary_combination (id,uid,bookid,bookname,author,keyword,brief_content) VALUES (%s,%s,%s,%s,%s,%s,%s) "
    val = [c.id,c.uid,c.bookid,c.bookname,c.author,c.keyword,c.brief_content]


    cursor.execute(sql, val)


    print("已插入第 :" + str(count) + "条数据")

    # 创建的connection是非自动提交，需要手动commit
    connection.commit()



def get_book(bookid):
    # 初始化connection
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='000000',
        db='wenquan',
        charset='utf8mb4',
    )
    cursor = connection.cursor()

    # sql = "SELECT * FROM index_author  WHERE ordernum>'2206' "
    sql = "SELECT * FROM wenquanbook WHERE 图书bid=" + str(bookid)
    cursor.execute(sql)
    results = cursor.fetchall()
    # row代表一个作者
    for row in results:
        bookname=row[3]
        author=row[5]
        keyword=row[11]
        brief_content=row[12]
        b = book(bookid, bookname, author, keyword, brief_content)
        return b


def get_diary():
    # 初始化connection
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='000000',
        db='wenquan',
        charset='utf8mb4',
    )
    cursor = connection.cursor()

    # sql = "SELECT * FROM index_author  WHERE ordernum>'2206' "
    sql = "SELECT * FROM reader_collect_diary"
    cursor.execute(sql)
    results = cursor.fetchall()
    # row代表一个作者
    for row in results:
        id = row[0]
        uid = row[4]
        bookid = row[1]
        try:
            bookname=get_book(bookid).bookname
        except:
            bookname=""

        try:
            author=get_book(bookid).author
        except:
            author=""

        try:
            keyword=get_book(bookid).keyword
        except:
            keyword=""

        try:
            brief_content = get_book(bookid).brief_content
        except:
            brief_content=""


        c=combination(id,uid,bookid,bookname,author,keyword,brief_content)
        insert(c)

def get_combination():
    get_diary()


get_combination()
print("收皮")








