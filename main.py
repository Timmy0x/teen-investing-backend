##### Imports #####
from flask import Flask, render_template, request, url_for, Response
from flask_cors import CORS
import json
import requests
import csv

from users.main import UserController
from data.main import DataController

##### Declare Classes #####
user_con = UserController()
data_con = DataController()

##### App Routes #####
app = Flask(__name__)
CORS(app)

@app.route("/add_user")
def add_user():
    args = request.args
    user_add = user_con.add_user(name=args.get("name"), email=args.get("email"), password=args.get("password"))
    if user_add is not False:
        return Response('{"success": true, "payload": ' + str(user_add).replace("'", "\"") + '}', mimetype="text/json")
    elif user_con.is_created(name=args.get("name"), email=args.get("email"), password=args.get("password")) is not False:
        return Response('{"success": false, "error": 101, "payload": ' + str(user_con.get_user(name=args.get("name"), email=args.get("email"), password=args.get("password")).replace("'", "\"") + '}', mimetype="text/json"))
    return Response('{"success": false}', mimetype="text/json")

@app.route("/get_user")
def get_user():
    args = request.args
    try:
        user = user_con.get_user(name=args.get("name"), email=args.get("email"), password=args.get("password"))
        return Response('{"success": true, "payload": ' + str(user) + '}', mimetype="text/json")
    except Exception as e:
        print(e)
        return Response('{"success": false}', mimetype="text/json")

app.run(host='0.0.0.0', port=4567)
