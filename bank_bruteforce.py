import ast
import string 
import random
import json

def log_in_staff():
    username = input("What is your name ")
    password = input("Please input your password ")
    with open("staff.txt", "r") as staff_files:
        staff_details = ast.literal_eval(staff_files.read())
        if username in staff_details:   
            if staff_details[username]["Password"] == password:
                print("yeah") 
                show_account_setting() 
            else:
                print("Password is wrong") 
        else:
            print("username doesn't exist") 
    

def close_up():
    return 0

def create_session(username):
    with open(f"{username}.txt", "wb") as sess:
        sess.write("")
        pass

def show_account_setting():
    print("""
    1 Create new bank account
    2 Check Account Details
    3 Logout
    """)
    response = ""
    while response == "" or response > 3:
        response = int(input("> "))
    else:
        if response == 1:
            create_account()
        elif response == 2:
            get_account_details()
        else:
            close_up()

def create_account():
    details = {}
    details["Account name"] = input("Account name ")
    details["Opening balance"] = int(input("Opening balance "))
    details["Account type"] = input("Account type ")
    details["Account email"] = input("Account email ")
    details["Account number"] = "".join(random.choice(string.digits) for i in range(10))
    print(f"The account number is {details['Account number']}")
    with open("customer.txt", "a") as customer:
        customer.write(json.dumps(details))
    show_account_setting()

def get_account_details():
    with open("customer.txt", "r") as customer:
        total_details = ast.literal_eval(customer.read())
        user_details  = total_details[username]
        for index, details in user_details.items():
            print(index, details)

def log_out():
    # Delete file
    # and return to the log in staff function
    log_in_staff()


log_in_staff()