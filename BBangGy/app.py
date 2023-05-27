from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        hour = request.form['hour']
        min = request.form['min']
        # 여기에서 데이터 처리 로직을 작성하세요.
        print(hour,min)
        return 'POST: {}시 {}분'.format(hour,min)
    return render_template('index.html')

@app.route('/open')
def button_op():
    print('open')
    return 'open'

@app.route('/close')
def button_cl():
    print('close')
    return 'close'

if __name__ == '__main__':
    app.run(port=5001,debug=True)