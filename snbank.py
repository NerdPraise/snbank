import os
import json
import random
import ast
import string


class Bank:
    def __init__(self):
        self._username = None
        self._password = None 

    def start(self):
        print("""
        1 Staff Login
        2 Close App
        """)
        response = ""
        while response == "" or response > 2:
            response = int(input("> "))
        else:
            if response == 1:
                self.log_in_user()
            else:
                self.close_app()
   
    def log_in_user(self):
        username = input("What is your name ")
        password = input("Please input your password ")
        with open("staff.txt", "r") as staff_files:
            c = ast.literal_eval(staff_files.read())
            try:
                if c[username]["Password"] == password:
                    self._username = username
                    self._password = password
                    print("yeah")
            except:
                print("Username doesn't exist ")
                return 0
        self._create_session()
        self._show_account_settings()

    def _show_account_settings(self):
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
                self._create_account()
            elif response == 2:
                self.get_account_details()
            else:  
                self.logout()
    
    def _create_account(self):
        details = {}
        details["Account name"] = input("Account name ")
        details["Opening balance"] = int(input("Opening balance "))
        details["Account type"] = input("Account type ")
        details["Account email"] = input("Account email ")
        details["Account number"] = "".join(random.choice(string.digits) for i in range(10))
        print(f"The account number is {details['Account number']}")
        with open("customer.txt", "a") as customer:
            customer.write(json.dumps(details))
        self._show_account_settings()

    def logout(self):
        # if os.path.exists(f"{self._username}.txt"):
        os.remove(f"{self._username}.txt")
        self._username, self._password = None, None
        self.start()

    def get_account_details(self):
        account_number = input("Input account number ")
        with open("customer.txt", "r") as customer:
            total_details = ast.literal_eval(customer.read())
            user_details  = total_details[account_number]
            for index, details in user_details.items():
                print(index, details)

    def _create_session(self):
        with open(f"{self._username}.txt", "w") as sess:
            sess.write(f"{self._username} logged in")


    def close_app(self):
        return 0


p = Bank()
p.start()