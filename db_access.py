import sqlite3

# Databse :
# 	table EMP 
# 	table STudent 
# 	table Dept 

# python SQL queries 

conn = sqlite3.connect("db1.db")
c = conn.cursor()

# MySQL sql db , workbench username and password
# pymysql ,cx_oracle   
# hostname = 
# db 
# username 
# password 

#Create Table

c.execute("""CREATE TABLE IF NOT EXISTS EMP (ID INT PRIMARY KEY,NAME TEXT,EMAIL TEXT,SAL REAL)""")

#Insert
try:
	c.execute("""INSERT INTO EMP (ID,NAME,EMAIL,SAL) VALUES (101,"ABC","abc@gmail.com",45000)""")
	c.execute("COMMIT")

except sqlite3.IntegrityError as e:
	print("Got an error ", e)

id = 104
name = "PQT"
email = "pqt@gmail.com"
sal = 60000

try:
	c.execute("""INSERT INTO EMP (ID,NAME,EMAIL,SAL) VALUES (?,?,?,?)""",(id,name,email,sal))
	c.execute("COMMIT")
	print("Record added Successfully")
except sqlite3.IntegrityError as e:
	print("Got an error ", e)

c.execute("""SELECT * FROM EMP""")

# print(next(c))

# for row in c:
# 	print(row)

# print(c.fetchone())
# print(c.fetchone())

# print((c.fetchall()))

c.execute("""UPDATE EMP SET SAL = 90000 WHERE ID = 102""")
c.execute("SELECT * FROM EMP WHERE ID = 102")
print(c.fetchall())


c.execute("DELETE FROM EMP WHERE ID = 103")
c.execute("SELECT * FROM EMP")
print(c.fetchall())


conn.close()


# Relational db and Non relateional db 

# MongoDB  => No SQL


# Db 

# Tables =>  rows


# DB 

# Collections
# 	document    