import csv

class DataController:
    def create_class(self, name, fields=[]):
        with open("data/classes/" + name + ".csv", "w") as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter=",")
            writer.writeheader()
            return True
    def add_data(self, name, data=[], allow_duplicates=True):
        with open("data/classes/" + name + ".csv", "wr") as f:
            reader = csv.reader(f)
            writer = csv.writer(f)
            if allow_duplicates == True:
                for row in reader:
                    if row == data:
                        return False
            else:
                writer.writerow(data)
    def read_data(self, name):
        data = []
        with open("data/classes/" + name + ".csv", "r") as f:
            reader = csv.writer(f)
            for row in reader:
                data.append(row)