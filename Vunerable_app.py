
from flask import Flask, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("users.db")

@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    db = get_db()
    cursor = db.cursor()

    # ❌ VULNERABLE: user input directly concatenated into SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    user = cursor.fetchone()

    if user:
        return "Login successful"
    else:
        return "Invalid credentials"

if __name__ == "__main__":
    app.run(debug=True)
