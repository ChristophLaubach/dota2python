from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def base():
    return render_template("base.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/heroes")
def heroes():
    return render_template("heroes.html")

@app.route("/items")
def items():
    return render_template("items.html")

@app.route("/about-me")
def about():
   return render_template("about.html")

if __name__ == '__main__':
    app.run()