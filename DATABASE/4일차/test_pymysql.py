import pymysql

# db connection
connection = pymysql.connect(
    host= 'localhost',
    user= 'root',
    password='seungwon0113',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

connection.cursor()
