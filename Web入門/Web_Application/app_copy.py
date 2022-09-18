from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        form_id = request.form['id']
        form_pw = request.form['pw']
        correct_id_1 = 'sendy' 
        correct_password_1 = '1880'
        correct_id_2 = 'senshu'
        correct_password_2 = 'daigaku'
        if form_id == correct_id_1 and form_pw == correct_password_1:
            return render_template('user_page.html',id = form_id)
        elif form_id == correct_id_2 and form_pw == correct_password_2:
            return render_template('user_page.html',id = form_id)
        else:
            return 'ログインに失敗しました'
    return render_template('/login.html')

@app.route('/logout')
def logout():
    return 'ログアウトページを表示します'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
