import mysql.connector

connection = mysql.connector.connect(user = 'root', database = 'elite 102 project', password = 'password')

cursor = connection.cursor()

testQuery = ("SELECT * FROM account")

cursor.execute(testQuery)

for item in cursor:
    print(item)


cursor.close()

connection.close()

"""
Creating a code for check balance, deposit, withdraw, create account, delete account, modify account. SET 
"""

