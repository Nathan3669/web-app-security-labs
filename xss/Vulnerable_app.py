from flask import Flask, request

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "")

    # ❌ VULNERABLE: user input rendered directly into HTML
    return f"""
        <html>
            <body>
                <h2>Search Results</h2>
                <p>You searched for: {query}</p>
            </body>
        </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
