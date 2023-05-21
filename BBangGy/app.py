from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run('0.0.0.0' ,port=5001,debug=True)