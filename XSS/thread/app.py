from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def wellcome():
    msg=''
    return render_template('welcome_login.html',msg=msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='POST':
        user_name = request.form['uname']
        if user_name == '':
            return render_template('welcome_login.html',msg="名前を入力してください")
        else:
            return render_template('thread.html',user_name=user_name)     


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)

