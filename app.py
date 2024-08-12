from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/base")
def base():
    return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)
