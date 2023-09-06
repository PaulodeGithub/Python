from flask import Flask
from fucntions import make_bold

app = Flask(__name__)

@app.route("/")
@make_bold
def hello_world():
    return "<p>Hello, World!</p>"

emp_text = hello_world
print(emp_text)

@app.route("/fearless")
def be_fearless():
    return "You a fearless animal"

@app.route("/<name>")
def username(name):
    return f"You are unstoppable {name}"

if __name__ == "__main__":
    app.run(debug=True)