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
    if check.lower() == "yes":
    deposit_amount = float(input("How much? "))
    cursor.execute("UPDATE account SET check_balance = check_balance + %s WHERE account_number = %s", (deposit_amount, account_number))
    connection.commit()

# Withdraw 
def withdraw(account_number):
    check = input("Do you want to withdraw from your bank? ")
    if check.lower() == "yes":
        withdraw_amount = float(input("How much? "))
        cursor.execute("SELECT check_balance FROM account WHERE account_number = %s", (account_number,))
        result = cursor.fetchone()
        if result:
            balance = result[0]
            if withdraw_amount <= balance:
                cursor.execute("UPDATE account SET check_balance = check_balance - %s WHERE account_number = %s", (withdraw_amount, account_number))
                connection.commit()
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

# Check Balance 
def account_balance(account_number):
    check_balance = check_balance
    cursor.execute("SELECT check_balance FROM account WHERE check_balance = %s", (check_balance))


def log_in():
    email = input("Enter your email: ")
    passcode = input("Enter your password: ")
    cursor.execute("SELECT account_number FROM account WHERE email = %s AND passcode = %s", (email, passcode))
    result = cursor.fetchone()
    if result:
        print("Login successful!")

        return result[0]
    else:
        print("Invalid email or password.")
        return None