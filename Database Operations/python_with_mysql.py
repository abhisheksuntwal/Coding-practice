# import statements
import pymysql

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="test_python_mysql",
)

cursor = mydb.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS test_python_mysql2")
cursor.execute("CREATE TABLE IF NOT EXISTS customers(id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(255) UNIQUE, address VARCHAR(255))")

sql = "INSERT INTO customers (username, address) VALUES (%s, %s)"
val = [
  ('Peter1', 'Lowstreet 4'),
  ('Amy1', 'Apple st 652'),
  ('Hannah1', 'Mountain 21'),
  ('Michael1', 'Valley 345'),
  ('Sandy1', 'Ocean blvd 2'),
  ('Betty1', 'Green Grass 1'),
  ('Richard1', 'Sky st 331'),
  ('Susan1', 'One way 98'),
  ('Vicky1', 'Yellow Garden 2'),
  ('Ben1', 'Park Lane 38'),
  ('William1', 'Central st 954'),
  ('Chuck1', 'Main Road 989'),
  ('Viola1', 'Sideway 1633')
]

cursor.executemany(sql, val)
mydb.commit()
print(cursor.rowcount)
cursor.execute("SELECT * FROM customers")

for x in cursor.fetchall():
    print(x)






