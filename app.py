from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Azure Flask App!</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)



