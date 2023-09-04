from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/fearless")
def be_fearless():
    return "You a fearless animal"

@app.route("/<name>")
def username(name):
    return f"You are unstoppable {name}"

if __name__ == "__main__":
    app.run(debug=True)