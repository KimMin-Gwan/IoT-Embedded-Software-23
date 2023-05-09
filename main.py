import server
# 4. 서버 클래스

import LCD
# 5. L2C LCD 클래스

import info
# 6. 정보 클래스

import Curtain_Master as CM
# 1. 조도 센서 클래스
# 2. 커튼을 조작하는 클래스
# 3. 모터 조작 클래스



class MainFunction:
    def __init__(self):
        self._info = info.Information()
        self._curtain = CM.Curtain_Master()

    def mainloop(self):
        self._info.update_time()
        # 알람 설정이 되어있는지 확인
        if self._info.get_alarm_flag is True:
            # 현재시간 확인하고 지금 움직여도되는지 확인
            pass
        
        # 현재 밝기 상태 확인 및 조작
        # 이거 else로 넣어서 알람 설정 안되있을때만 동작하나?
        self._curtain.check_birghtness()
        
    # 알람 맞추는 함수
    def set_alarm_control(self, flag, time):
        self._info.set_alarm(flag, time)
    
    def set_curtain_control(self, flag):
        self._curtain.move_curtain(flag)


        

def main():
    main_f = MainFunction()
    flask_server = server.Server(main_f)
    flask_server.run_server()
    while(True):
        main_f.mainloop()




if __name__ == "__main__":
    main()