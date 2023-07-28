import json
import csv

class WalletController:
	def save_wallet(self, key=None, email=None, password=None):
		with open("wallet/keys.csv", "a") as f:
			writer = csv.writer(f)
			print(key)
			print(password)
			print(email)
			writer.writerow([str(key), str(email), str(password)])
		return True
	def get_wallet(self, email=None, password=None):
		with open("wallet/keys.csv") as f:
			reader = csv.reader(f)
			for row in reader:
				if row[1] == email and row[2] == password:
					return row[0]