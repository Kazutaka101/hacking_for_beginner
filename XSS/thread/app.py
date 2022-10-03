from flask import Flask, render_template, request, make_response, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime, hashlib
import sys

app = Flask(__name__)
sessions_dict = {}

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///Thread.db'
db = SQLAlchemy(app)
class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    date = db.Column(db.DateTime)
    text = db.Column(db.Text())

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))

db.create_all()
#もしも、DBに何もなければレコードを追加する作業を記述する
#user_record = User(email='sendy@sendy.com', password='sendy')
#db.session.add(user_record)
#
#thread_record = Thread(name = "mike", date = datetime.datetime.now(), text = "はじめまして、mikeです")
#db.session.add(thread_record)
#db.session.commit()
#thread_record = Thread(name = "john", date = datetime.datetime.now(), text = "Johnです。よろしく")
#db.session.add(thread_record)
#db.session.commit()

@app.route('/')
def wellcome():
    msg=''
    return render_template('welcome_login.html',msg=msg)

@app.route("/login",methods=["GET", "POST"])
def login():
    login_message = ""

    if request.method == "POST":
        app.logger.info(request.get_data())
        form_email = request.form["email"]
        form_passwd= request.form["passw"]
        login = User.query.filter_by(email=form_email, password=form_passwd).first()
        
        if login is not None:
            expire_time = 60 * 60 * 24 * 7 #7 days
            expires = int(datetime.datetime.now().timestamp()) + expire_time
            response = make_response(redirect('/thread'))
            session_id = generate_sessionid(form_passwd)
            response.set_cookie("SESSION_ID", value=session_id, expires=expires)
            return response

        else:
            login_message = "メールアドレスかパスワードが異なります"

    return render_template("welcome_login.html",message = login_message); 

    #if request.method=='POST':
    #    user_name = request.form['uname']
    #    if user_name == '':
    #        return render_template('welcome_login.html',msg="名前を入力してください")
    #    else:
    #        expire_time = 60 * 60 * 24 * 7 #7 days
    #        expires = int(datetime.datetime.now().timestamp()) + expire_time
    #        response = make_response(redirect('/thread'))
    #        session_id = generate_sessionid(user_name)
    #        response.set_cookie("SESSION_ID", value=session_id, expires=expires)
    #        return response


@app.route('/thread', methods = ['GET', 'POST'])
def thread():
    #SESSIONと、user_nameの取得
    session_id = request.cookies.get('SESSION_ID') 

    if session_id == None:
        return redirect('/') 

    else:
        keys = [k for k, v in sessions_dict.items() if v == session_id]
        if keys:
            user_name = keys[0]

    #GET
    if request.method == 'GET':
        aaa = Thread.query.all()
        sys.stdout.write(thread.query.all())
        return render_template('thread.html',user_name = user_name) 

    elif request.method == 'POST':
       print("aaa")   
def generate_sessionid(user_name):
    #sessions hashを作る
    #名前をUTF-8にエンコードして、それをhash256にする
    utf_user_name = user_name.encode('utf-8')
    session_hash = hashlib.sha256(utf_user_name).hexdigest()              
    sessions_dict[user_name] = session_hash
    return session_hash 

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
