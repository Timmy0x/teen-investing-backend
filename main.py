##### Imports #####
from flask import Flask, render_template, request, url_for, Response
from flask_cors import CORS
import json
import csv

from users.main import UserController
from data.main import DataController
from wallet.main import WalletController

##### Declare Classes #####
user_con = UserController()
data_con = DataController()
wallet_con = WalletController()

##### App Routes #####
app = Flask(__name__)
CORS(app)

@app.route("/add_user")
def add_user():
    args = request.args
    user_add = user_con.add_user(name=args.get("name"), email=args.get("email"), password=args.get("password"))
    print(user_add)
    if user_add != False:
        user_add = json.dumps({
			"name": user_add[0],
			"email": user_add[1],
		})
        return Response('{"success": true, "payload": "' + user_add + '"}', mimetype="text/json")
    elif user_con.is_created(name=args.get("name"), email=args.get("email"), password=args.get("password")) is not False:
        return Response('{"success": false, "error": 101, "payload": ' + str(json.dumps(user_con.get_user(name=args.get("name"), email=args.get("email"), password=args.get("password")))) + '}', mimetype="text/json")
    return Response('{"success": false}', mimetype="text/json")
@app.route("/get_user")
def get_user():
    args = request.args
    try:
        user = user_con.get_user(name=args.get("name"), email=args.get("email"), password=args.get("password"))
        user = json.dumps({
			"name": user[0],
			"email": user[1],
		})
        return Response('{"success": true, "payload": ' + user + '}', mimetype="text/json")
    except Exception as e:
        print(e)
        return Response('{"success": false}', mimetype="text/json")

@app.route("/wallet/save_wallet")
def add_wallet():
	args = request.args
	if wallet_con.save_wallet(email=request.args.get("email"), key=request.args.get("key"), password=request.args.get("password")) == True:
		return Response('{"success": true}', mimetype="text/json")
	else:
		return Response('{"success": false}', mimetype="text/json")
@app.route("/wallet/get_wallet")
def get_wallet():
	args = request.args
	try:
		return Response('{"success": true, "payload": "' + wallet_con.get_wallet(email=request.args.get("email"), password=request.args.get("password")) + '"}', mimetype="text/json")
	except:
		return Response('{"success": false}', mimetype="text/json")


app.run(host='0.0.0.0', port=4567)
