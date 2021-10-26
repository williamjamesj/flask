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
def controlPage(): # This is the front-end page that allows the users to control the door.
    return render_template("control.html")

@app.route("/doorControl", methods=["POST","GET"]) # No webpage is attached to this URL, but it control the door movement.
def doorControl():
    status = "nothing"
    if request.method == "POST":
        if request.get_json()["action"] == "toggle":
            status = toggle()
            DATABASE.insert("Door toggled.",request.remote_addr,math.floor(time.time()),status) # Each of the insert functions inserts the relevant description of the action, the IP address, the time the response was sent and the response that was sent to the client.
        elif request.get_json()["action"] == "check":
            status = getStatus()
            DATABASE.insert("Door check.",request.remote_addr,math.floor(time.time()),status)
        elif request.get_json()["action"] == "open":
            status = open()
            DATABASE.insert("Door open.",request.remote_addr,math.floor(time.time()),status)
        elif request.get_json()["action"] == "close":
            status = close()
            DATABASE.insert("Door close.",request.remote_addr,math.floor(time.time()),status)
    return jsonify({"status":status})

@app.route("/doorHistory")
def doorHistory():
    data = DATABASE.query()
    return render_template("history.html",data=data,datetime=datetime)