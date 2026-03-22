from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    version = os.environ.get("APP_VERSION", "v1")
    return f"Hello from Flask on Docker! Version: {version}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
