from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'indexページを表示します'

@app.route('/login')
def login():
    return 'ログインページを表示します'

@app.route('/logout')
def logout():
    return 'ログアウトページを表示します'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
