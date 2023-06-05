from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/mypage')
def mypage():
    return 'this is my page!'
#열기
@app.route('/open')
def button_op():
    print('open')
    return 'open'
#닫기
@app.route('/close')
def button_cl():
    print('close')
    return 'close'
#커튼 시간과 분을 입력받아 포스트
@app.route("/post", methods=['POST'])
def post():
    hour = request.form['hour']
    minute = request.form['minute']
    print('hour : ', hour)
    print('minute : ', minute)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5001,debug=True)