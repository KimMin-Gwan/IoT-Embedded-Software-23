from flask import Flask, request
from flask import render_template
import server

class Server():
    # 생성자
    def __init__(self, main_function):
        self.app = Flask(__name__)
        # 외부 클래스는 포인터로 받아와짐
        # 즉, 내부에서 변경되면 외부도 변경됨
        self.main = main_function 
        self.register_routes()
    

    def register_routes(self):
        # 홈화면
        @self.app.route("/")
        def home():
            return render_template("./index.html")

        # 웹에서 데이터를 알람 시간 설정을 받아옴
        @self.app.route("/set_alarm_serv", methods=['POST'])
        def set_alarm_serv():
            time = request.form['time']
            flag = request.form['flag']
            self.main.set_alarm_control(flag, time)
            return 'Success'
        
        #커튼을 열어라
        @self.app.route("/open")
        def open_curtain():
            self.main.set_curtain_control(False)
            
        #커튼을 열어라
        @self.app.route("/close")
        def close_curtain():
            self.main.set_curtain_control(True)

    def run_server(self, host = server.HOST):
        self.app.run(host)
