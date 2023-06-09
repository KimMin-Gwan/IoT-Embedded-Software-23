import server
# 4. 서버 클래스
import LCD
from LCD import display_lcd, display_reset
# 5. L2C LCD 클래스
import info
# 6. 정보 클래스
import time
import threading


from Curtain_Master import Curtain, Led
# 1. 조도 센서 클래스
# 2. 커튼을 조작하는 클래스
# 3. 모터 조작 클래스

# 메인 클래스 지우고 sequnce 메인 펑션을 사용


def mainLoop(info_master, curtain_master, my_lcd):

    #  >>>>>>>>  메인 루프   <<<<<<<<<<<<
    """
    수도코드 
    1. 인포마스터 업데이트

    2. 인포마스터 정보에서 알람 설정 정보 확인
    2-1. 참이라면? -> 현재 시간과 비교, 빨간 LED 켜기
    2-1-1. 참이라면 ? -> 커튼 마스터에서 커튼 동작 파란 LED켜기
    2-1-2. 파란 LED 끄기
    2-2. 거짓이라면? -> 빨간 LED끄기

    3. 커튼 마스터에 현재 채도 확인
    4. 채도와 임계점 비교
    4-1. 채도가 임계점을 넘으면? -> 커튼마스터에서 커튼 동작, 파란 LED 켜기
    4-1-1. 파란 LED 끄기
    4-2. 채도가 임계점 이하라면? -> 커튼마스터에서 커튼 동작, 파란 LED 켜기   
    4-2-1. 파란 LED 끄기

    5. 플라스크 조작 필요? ->  X 플라스크는 알아서 돌아감
    6. 1초 쉬고 다음 루프
    프레시져 종료
    """
    # I2C LCD는 아직 고려하지 않음

    while(True):
        info_master.update_time()
        print("-----------------------------")
        info_master()

        
        display_lcd(info_master, my_lcd)
        flag = 'None'
        curtain_master.check_birghtness()
        flag = info_master.get_motor_flag()
        if flag == 'Pull':
            curtain_master.move_curtain(False)
            info_master.set_motor_flag('None')
            continue
        elif flag == 'Push':
            curtain_master.move_curtain(True)
            info_master.set_motor_flag('None')
            continue
            
        if info_master.get_alarm_flag():
            if info_master.is_alarm_time():
                curtain_master.move_curtain(True)
                curtain_master.change_curtain_flag()
            continue  # 채도비교 안하고 알람에만 의존
        # 밝기 비교 및 조작 까지 포함된 함수
        # 조작이 되면 True가 반환됨
        time.sleep(1)
        display_reset(my_lcd)
        time.sleep(0.001)
        

def main():
    # >>>>>>>   초기화  <<<<<<<<<<<<<
    info_master = info.Information()  #현재 상태 클래스  - 핵심
    curtain_master = Curtain(info_master)  # 커튼 조작 클래스 - 디바이스 드라이버 구현
    mylcd = LCD.I2C_LCD_driver.lcd() # LCD 조작 클래스  - 파이썬에서 동작
    #led_master = Led()          # led 조작 클래스  - 디바이스 드라이버 구현
    flask_server = server.Server(info_master) 
    # flask 클래스  - 멀티 스래딩
    print('Now Ready')
    args = (info_master, curtain_master, mylcd)
    thread = threading.Thread(target = mainLoop, args=args)
    thread.start()
    time.sleep(2)
    flask_server.run_server()

        
if __name__ == "__main__":
    main()

# 내부에서 바로 동작하는게 아니고 파라미터 넘기는걸로 하자.

