import csv
import json
from libs.crypto import hash

class UserController:
    def verify_user(self, name=None, password=None, email=None):
        if name and password and email and "@" in str(email) and "." in str(email) and len(name) > 3 and len(list(password)) > 3:
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
                return [name, email, password]
        else:
            return False

    def get_user(self, name=None, password=None, email=None):
        if self.verify_user(name=name, password=password, email=email) == True:
            with open("users/user.csv") as f:
                reader = csv.reader(f)
                for row in reader:
                    if [name, email, password] == row:
                        return row
            return False
        else:
            return False
