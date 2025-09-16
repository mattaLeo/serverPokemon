from flask import Flask, send_file
import random, json

f = open("Pokemon.json")
data = json.load(f)

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("Pokemon.json")

@app.route("/random")
def ran():
    return data[random.randrange(0, 11)]

@app.route("/select/<name>")
def select(name):
    selected = 0
    for x in data:
        if x["name"] == name:
            break
        else:
            selected += 1
    return data[selected]

if __name__ == "__main__":
    app.run(debug=True)