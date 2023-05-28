from flask import Flask, request
from flask import render_template
import server


class Server():
    # 생성자
    def __init__(self, info_master, curtain):
        self.app = Flask(__name__)
        # 외부 클래스는 포인터로 받아와짐
        # 즉, 내부에서 변경되면 외부도 변경됨
        self.info = info_master 
        self.curtain = curtain
        self.register_routes()
    

    def register_routes(self):
        # 홈화면
        @self.app.route("/")
        def home():
            print('홈페이지')
            return render_template('index.html')

        # 웹에서 데이터를 알람 시간 설정을 받아옴
        @self.app.route("/set_alarm_serv", methods=['POST'])
        def set_alarm_serv():
            hour = request.form['time']
            minute = request.form['flag']
            print('hour : ', hour)
            print('minute : ', minute)
            self.info.set_alarm(hour, minute)
            return render_template('index.html')
        
        #커튼을 열어라
        @self.app.route("/open")
        def open_curtain():
            self.curtain.move_curtain(False)
            return render_template('index.html')
            
        #커튼을 열어라
        @self.app.route("/close")
        def close_curtain():
            self.curtain.move_curtain(True)
            return render_template('index.html')

    def run_server(self):
        self.app.run('0.0.0.0', port=5001, debug =True)
