from flask import Flask, render_template, jsonify, request

from toggledoor import toggleDoor

app = Flask(__name__)
app.config["SECRET_KEY"] = "hlpxQom-si2HPNdMvDQZ4g"

@app.route("/")
def controlPage():
    return render_template("control.html")

@app.route("/doorControl", methods=["POST","GET"])
def doorControl():
    print(request)
    status = "nothing"
    if request.method == "POST":
        print(request.get_json(["action"]))
        if request.get_json()["action"] == "toggle":
            status = toggleDoor()
    return jsonify({"status":status})