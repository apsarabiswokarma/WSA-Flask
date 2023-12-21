from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/dologin", methods=["POST"])
def do_login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "apsara" and password == "apsara123":
        redirect("/")
        return "you have been logged in successfully"
    else:
        redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
