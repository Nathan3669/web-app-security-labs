from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/search")
def search():
    query = request.args.get("q", "")

    # ✅ SECURE: escape user input before rendering
    safe_query = escape(query)

    return f"""
        <html>
            <body>
                <h2>Search Results</h2>
                <p>You searched for: {safe_query}</p>
            </body>
        </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
