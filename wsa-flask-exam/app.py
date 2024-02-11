from flask import Flask, jsonify, render_template, request

# jsonify converts python object into JSON
# request is used to get data from form or json

app = Flask(__name__)

# {userId : {name, age}}
users = {
    1: {"name": "Ram", "age": 21},
    2: {"name": "Sam", "age": 23},
}


@app.route("/get-all-user", methods=["GET"])
def getAllUser():
    return jsonify(users)


@app.route("/user/<int:id>", methods=["GET"])
def getUser(id):
    user = users.get(id)
    return jsonify(user)


@app.route("/add-user", methods=["POST"])
def addUser():
    req = request.json
    name = req.get("name")
    age = req.get("age")

    users_count = max(users.keys())
    new_user_key = users_count + 1

    users[new_user_key] = {"name": name, "age": age}

    return jsonify(users)


@app.route("/add-user-from-form", methods=["POST"])
def addUserFromForm():
    name = request.form["name"]
    age = request.form["age"]

    users_count = max(users.keys())
    new_user_key = users_count + 1

    users[new_user_key] = {"name": name, "age": age}

    return jsonify(users)


@app.route("/user/<int:id>", methods=["DELETE"])
def deleteUser(id):
    user = users.pop(id)
    return jsonify(users)


@app.route("/user/<int:id>", methods=["PUT"])
def updateUser(id):
    req = request.json
    age = req.get("age")
    users[id] = {"name": users[id]["name"], "age": age}

    return jsonify(users[id])


@app.route("/form")
def formPage():
    return render_template("form.html", title="Title")


@app.route("/json")
def jsonPage():
    return render_template("json.html")


if __name__ == "__main__":
    app.run(debug=True)
