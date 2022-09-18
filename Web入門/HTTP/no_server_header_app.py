from flask import Flask, render_template, request
import os
os.environ['WERKZEUG_DEBUG_PIN'] = 'off'

class localFlask(Flask):
    def process_response(self, response):
        #Every response will be processed here first
        response.headers['server'] = 'SERVER' 
        return(response)

app = localFlask(__name__)
#app = Flask(__name__)
@app.route("/")
def sample_by_root():
    return render_template('sample.html')

@app.route("/sample")
def sample():
    return render_template("sample.html")

@app.route("/get_sample")
def get_sample():
    if request.method=="GET":
        get_param = request.args.get("get_param")
        if get_param == None:
            get_param = ""
        return render_template("get_sample.html", get_param=get_param)


@app.route("/post_sample", methods=['GET','POST'])
def post_sample():
    if request.method=="GET":
        name="名無し"
        return render_template('post_sample.html',name=name) 
    elif request.method=="POST":
        name = request.form["name"]
        return render_template('post_sample.html', name=name)
def main():
    app.run(host="0.0.0.0", port=8080, debug=True)

if __name__ == '__main__':
    main()

