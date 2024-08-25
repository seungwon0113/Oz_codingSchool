import pymysql

# db connection
connection = pymysql.connect(
    host= 'localhost',
    user= 'root',
    password='seungwon0113',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor # Dict : 딕셔너리 형태로
)

## 1. SELECT * FROM
def get_customers():
    cursor = connection.cursor()

    sql = "SELECT * FROM customers"
    cursor.execute(sql)

    customers = cursor.fetchone()
    print("customers : ", customers)
    print("customers : ", customers['customerNumber'])
    print("customers : ", customers['customerName'])
    print("customers : ", customers['country'])

## 2. INSERT INTO
def add_customer():
    cursor = connection.cursor()
    name = 'seungwon'
    family_name = 'jung'
    sql =f"INSERT INTO customers(customerNumber, customerName, contactLastName) VALUES(10003, '{name}', '{family_name}')"
    cursor.execute(sql)
    connection.commit()

add_customer()

## 3. UPDATE INTO
def update_customer():
    cursor = connection.cursor()
    update_name = 'update_seungwon'
    contactLastName = 'update_jung'

    sql = f"UPDATE customers SET customerName='{update_name}', contactLastName='{contactLastName}' WHERE customerNumber=1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

update_customer()

## 4. DELETE FROM
def delete_customer():
    cursor = connection.cursor()
    sql = "DELETE FROM customers WHERE customerNumber = 1000"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

delete_customer()