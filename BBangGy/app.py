from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    print('홈페이지')
    return render_template('index.html')

@app.route('/mypage')
def mypage():
    return 'this is my page!'

@app.route('/open')
def button():
    print('open')
    return render_template('index.html')

@app.route('/close')
def button_cl():
    print('close')
    return render_template('index.html')

@app.route("/post", methods=['POST'])
def post():
    hour = request.form['hour']
    minute = request.form['minute']
    print('hour : ', hour)
    print('minute : ', minute)
    return render_template('index.html')


if __name__ == '__main__':
    app.run('0.0.0.0' ,port=5001,debug=True)