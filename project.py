import mysql.connector
# import sqlite3
connection = mysql.connector.connect(user = 'root', database = 'elite 102 project', password = 'password')

cursor = connection.cursor()

testQuery = ("SELECT * FROM account")

cursor.execute(testQuery)

for item in cursor:
    print(item)

# User
def insert_account():
    name = input("Enter your name:")
    account_number = input("Enter your account number: ")
    email = input("Enter your email: ")
    passcode = str(input("Enter your password: "))
    check_balance = 000000.00
    query = ("INSERT INTO account (name, account_number, passcode, check_balance) VALUES (%s, %s, %s, %s)")
    values = (name, account_number, passcode, check_balance)
    cursor.execute(query, values)
    connection.commit()

insert_account()

# Modify Account
def modify(user):
    change_email = input("Do you want to change your email?")
    change_password = input("Do you want to change your password?")
    if change_email == "yes":
        new_email = input("Enter your new email: ")
    if change_password == "yes":
        new_passcode = str(input("Enter your new password: "))
    cursor.execute("UPDATE bank_database SET name = %s WHERE account_number = %s", (change_email, change_password))
    connection.commit()
# modify()

# Delete Account
# def delete_account(user):
#     delete_account = input("Do you want to delete your account? ")
#     if delete_account == "yes":

    # cursor.execute("DELETE FROM bank_database WHERE account_number = %s AND pin = %s", (new_name, account_number))
    # connection.commit()


# cursor.close()

# connection.close()


# Withdraw = cursor.execute("SELECT balance FROM account WHERE account_number = %s AND pin = %s", (account, pin))
# Deposit =  cursor.execute("UPDATE account SET name = %s WHERE account_number = %s", (change_email, change_password)) connection.commit()
# Check Balance = cursor.execute("SELECT check_balance FROM account WHERE account_number = %s AND pin = %s", (account, pin))
# Delete account = "DELETE FROM account WHERE account_number = %s AND pin = %s"