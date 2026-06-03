from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username=? AND password=?

        cursor.execute(query, (username, password))

        result = cursor.fetchone()

        conn.close()

        if result:
            message = "Connexion réussie"
        else:
            message = "Connexion refusée"

    return render_template("login.html", message=message)

app.run(debug=False)
