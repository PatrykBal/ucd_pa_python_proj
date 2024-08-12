from flask import Flask, request, render_template, redirect, url_for
from routes.blog import blog_blueprint

app = Flask(__name__)

app.register_blueprint(blog_blueprint, url_prefix='/blog')

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

database = {'Patryk': '123',
            'Balecki': 'xyz', 
            'Jony': 'abc', 
            'Tony': 'pqr',
}

@app.route('/form_login', methods=['POST', 'GET'])
def handle_login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 not in database:
        return render_template('login.html', 
                               info='Invalid User!')
    else:
        if database[name1] != pwd:
            return render_template('login.html', 
                                   info='Invalid Password!')
        else:
            return render_template('logout.html',
                                   name=name1)
 




if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
