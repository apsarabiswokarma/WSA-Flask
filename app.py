from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>  <h2>Welcome to Our Web Services and Apllication sections.</h2> <p> We will learn web development together</P>"


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
