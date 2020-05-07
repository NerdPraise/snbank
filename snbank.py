import os
import json
import random
import ast
import string


class Bank:
    """A bank registrar simulation"""
    with open("customer.txt") as deets:
        if os.path.getsize("customer.txt") != 0:
            CUSTOMER_DETAILS = json.load(deets)     # To make sure customer details from previous sessions are not overwritten
        else:
            CUSTOMER_DETAILS = {}
            CUSTOMER_DETAILS["account"] =[]


    def __init__(self):
        self._username = None
        self._password = None 
        self._logged_in = False

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
        while not self._logged_in:
            print("Please input correct info")
            username = input("What is your name ").lower()
            password = input("Please input your password ")
            with open("staff.txt", "r") as staff_files:
                staff = json.load(staff_files)
                for user in staff["data"]:
                    if username == user["username"].lower() and password == user["password"]:
                        self._username = username
                        self._password = password
                        self._logged_in = True
                        break
                    else:
                        self._logged_in = False
        else:
            self._create_session(work="logged in")
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
        Bank.CUSTOMER_DETAILS["account"].append(details)
        with open("customer.txt", "w") as customer:
            json.dump(Bank.CUSTOMER_DETAILS, customer)
        self._create_session(work=f"created account{details['Account name']}")
        self._show_account_settings()

    def logout(self):
        os.remove(f"{self._username}.txt")
        self._username, self._password, self._logged_in = None, None, False
        self.start()

    def get_account_details(self):
        account_number = input("Input account number ")
        with open("customer.txt", "r") as customer:
            total_details = json.load(customer)
            for data in total_details["account"]:
                if account_number == data["Account number"]:
                    deets = data
                    break
        for key, values in deets.items():
            print(f"{key}, {values}")
        self._show_account_settings()
                    
    def _create_session(self, work=None):
        with open(f"{self._username}.txt", "a") as sess:
            sess.write(f"{self._username} {work} \n")


    def close_app(self):
        return 0


p = Bank()
p.start()