from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)
os.environ['WERKZEUG_DEBUG_PIN'] = 'off'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///Test.db'
db = SQLAlchemy(app)
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/login",methods=["GET", "POST"])
def login():
    login_message = ""
    if request.method == "POST":
        app.logger.info(request.get_data())
        form_email = request.form["email"]
        form_passwd= request.form["passw"]
        
        login = user.query.filter_by(email=form_email, password=form_passwd).first()
        if login is not None:
            return "<h1>login success</h1>"
        else:
            login_message = "Invalid username or password"
    return render_template("login.html",message = login_message); 

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']

        register = user(username = uname, email = mail, password = passw)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")

if __name__ == "__main__":
    db.create_all()
    app.run(host='127.0.0.1', port=8080,debug=True)
