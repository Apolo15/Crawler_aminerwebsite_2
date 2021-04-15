import pymysql.cursors
import requests
import re
from bs4 import BeautifulSoup
import json
import time

connection = pymysql.connect(
        host='localhost',
        user='root',
        password='000000',
        db='wenquan',
        charset='utf8mb4',
    )

cursor = connection.cursor()

sql = "SELECT * FROM reader_collect_diary "
cursor.execute(sql)
results = cursor.fetchall()
# row代表一个作者
count=0
for row in results:
    id=row[0]
    t1=row[6]
    print(type(t1))
    print(t1)

    sql2="UPDATE reader_collect_diary_combination SET time= %s WHERE id= %s"
    val2=[t1,id]
    cursor.execute(sql2,val2)
    count=count+1
    print("已经插入"+str(count))

connection.commit()