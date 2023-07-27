import csv
import json
import requests
from libs.crypto import hash

class UserController:
    def verify_user(self, name=None, password=None, email=None):
        if name and password and email and "@" in str(email) and "." in str(email) and len(list(name)) > 5 and len(list(password)) > 5:
            return True
        else:
            return False

    def is_created(self, name=None, password=None, email=None):
        with open("users/user.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if [name, email, password] == row or name == str(row[0]) or email == str(row[1]):
                    return True
            return False

    def add_user(self, name=None, password=None, email=None):
        if self.is_created(name=name, password=password, email=email) == False:
            with open("users/user.csv", "a") as f:
                writer = csv.writer(f)
                writer.writerow([name, email, password])
                print(email)
                print(password)
                return [name, email, password]
        else:
            return False

    def get_user(self, name=None, password=None, email=None):
        if self.verify_user(name=name, password=password, email=email) == True:
            with open("users/user.csv") as f:
                reader = csv.reader(f)
                for row in reader:
                    if str([name, email, password]) == str(row) or str(name) == str(row[0]) or str(email) == str(row[1]) or str(password) == str(row[2]):
                        return [row[0], email, password]
                return False
        else:
            return False
