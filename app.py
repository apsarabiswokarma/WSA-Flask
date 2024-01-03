from flask import Flask, render_template, request, redirect


app = Flask(__name__)


# @app.route("/")
# def index():
#     return render_template("pages/index.html")


@app.route("/")
def hello_world():
    return render_template("pages/home.html")


@app.route("/login")
def login():
    return render_template("pages/login.html")


@app.route("/register")
def register():
    return render_template("pages/register.html")


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
