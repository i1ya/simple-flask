from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Simple Flask Application</h1>"


if __name__ == "__main__":
    app.run(port=5000, debug=True)
