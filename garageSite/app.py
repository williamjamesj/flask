import time # Import required python libraries.
from datetime import datetime
import math

import os

from databaseController import databaseConnection # Import database utilities
from toggleDoor import getStatus, open, close, toggle # Import door opening commands

from flask import Flask, render_template, jsonify, request # Import flask and related functions


app = Flask(__name__)
app.config["SECRET_KEY"] = "hlpxQom-si2HPNdMvDQZ4g" # Required for session variables, which aren't used.
DATABASE = databaseConnection("eventDatabase.db")

@app.route("/")
def controlPage(): # This is the front-facing page that allows the users to control the door.
    return render_template("control.html")

@app.route("/doorControl", methods=["POST","GET"]) # No webpage is attached to this URL, but it control the door movement.
def doorControl():
    print(request)
    status = "nothing"
    if request.method == "POST":
        print(request.get_json(["action"]))
        if request.get_json()["action"] == "toggle":
            status = toggle()
            DATABASE.insert("Door toggled.",request.remote_addr,math.floor(time.time()),status)
        elif request.get_json()["action"] == "check":
            DATABASE.insert("Door check.",request.remote_addr,math.floor(time.time()),status)
            status = getStatus()
        elif request.get_json()["action"] == "open":
            DATABASE.insert("Door open.",request.remote_addr,math.floor(time.time()),status)
            status = open()
        elif request.get_json()["action"] == "close":
            DATABASE.insert("Door close.",request.remote_addr,math.floor(time.time()),status)
            status = close()
    return jsonify({"status":status})

@app.route("/doorHistory")
def doorHistory():
    data = DATABASE.query()
    print(data)
    return render_template("history.html",data=data,datetime=datetime)