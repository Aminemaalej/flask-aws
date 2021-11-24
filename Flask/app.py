from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    # It's only when I changed these 2 bottom lines that I got the app runnning in a Docker Container.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
