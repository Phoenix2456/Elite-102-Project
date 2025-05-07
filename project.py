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
    check_balance = 0.0
    query = "INSERT INTO account (name, account_number, email, passcode, check_balance) VALUES (%s, %s, %s, %s, %s)"
    values = (name, account_number, email, passcode, check_balance)
    cursor.execute(query, values)
    connection.commit()
    return account_number

# Deposit 
def deposit(account_number):
    check = input("Do you want to deposit to your bank? ")
    if check == "yes":
        deposit_amount = float(input("How much? "))
        print(f"You have deposited ${deposit_amount} into your bank.")
    cursor.execute("UPDATE account SET check_balance = check_balance + %s WHERE account_number = %s", (deposit_amount, account_number))
    connection.commit()

# Withdraw 
def withdraw(account_number):
    check = input("Do you want to withdraw from your bank? ")
    if check == "yes":
        withdraw_amount = float(input("How much? "))
    cursor.execute("SELECT check_balance FROM account WHERE account_number = %s", (account_number))
    result = cursor.fetchone()
    if result:
        balance = result[0]
    if withdraw_amount <= balance:
        cursor.execute("UPDATE account SET check_balance = check_balance - %s WHERE account_number = %s", (withdraw_amount, account_number))
        connection.commit()
    else: 
        print("Insufficient Balance")

# Check Balance 
def account_balance():
    check_balance = check_balance
    cursor.execute("SELECT check_balance FROM account WHERE check_balance = %s", (check_balance))
    return check_balance

# Modify Account
def modify():
    change_email = input("Do you want to change your email?")
    change_password = input("Do you want to change your password?")
    if change_email and change_password == "yes":
        email = input("Enter your new email: ")
        passcode = str(input("Enter your new password: "))
    if change_email == "yes":
        email = input("Enter your new email: ")
    else:
        if change_password == "yes":
            passcode = str(input("Enter your new password: "))
    cursor.execute("UPDATE account SET email = %s WHERE email = %s AND passcode = %s", (change_email, change_password))
    connection.commit()
    return(email, passcode)
  
# Log in


# # Deleten Account
# def delete_account():
#     ask = input("Do you want to delete your account? ")
#     if ask == "yes":
#         cursor.execute("DELETE FROM account WHERE account_number = %s AND pin = %s", (new_name, account_number))




# Delete Account
# def delete_account(user):
#     delete_account = input("Do you want to delete your account? ")
#     if delete_account == "yes":
#         email = 
#     cursor.execute("DELETE FROM account WHERE account_number = %s AND pin = %s", (new_name, account_number))
#     connection.commit()


# cursor.close()

# connection.close()


# Withdraw = cursor.execute("SELECT balance FROM account WHERE account_number = %s AND pin = %s", (account, pin))
# Deposit =  cursor.execute("UPDATE account SET name = %s WHERE account_number = %s", (change_email, change_password)) connection.commit()
# Check Balance = cursor.execute("SELECT check_balance FROM account WHERE account_number = %s AND pin = %s", (account, pin))
# Delete account = "DELETE FROM account WHERE account_number = %s AND pin = %s"