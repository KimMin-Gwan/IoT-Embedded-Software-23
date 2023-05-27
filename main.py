import server
# 4. 서버 클래스
import LCD
# 5. L2C LCD 클래스
import info
# 6. 정보 클래스
import time


from Curtain_Master import Curtain, Led
# 1. 조도 센서 클래스
# 2. 커튼을 조작하는 클래스
# 3. 모터 조작 클래스

# 메인 클래스 지우고 sequnce 메인 펑션을 사용


def main():
    # >>>>>>>   초기화  <<<<<<<<<<<<<
    curtain_master = Curtain()  # 커튼 조작 클래스 - 디바이스 드라이버 구현
    led_master = Led()          # led 조작 클래스  - 디바이스 드라이버 구현
    lcd_master = LCD.L2C_LCD()  # LCD 조작 클래스  - 파이썬에서 동작
    info_master = info.Information()  #현재 상태 클래스  - 핵심
    flask_server = server.Server(info_master,
                                 curtain_master,
                                 led_master) 
    # flask 클래스  - 멀티 스래딩
    flask_server.run_server()

    print('Now Ready')
    lcd_master.led_green_on() # 녹색 불 켜주기

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

        if info_master.get_alarm_flag():
            led_master.led_red_on()
            if info_master.is_alarm_time():
                curtain_master.move_curtain(True)
                curtain_master.change_curtain_flag()
            continue  # 채도비교 안하고 알람에만 의존
        else:
            led_master.led_red_off()

        # 밝기 비교 및 조작 까지 포함된 함수
        # 조작이 되면 True가 반환됨
        if curtain_master.check_birghtness(led_master):
            led_master.led_blue_off()
        
        time.sleep(1)
        
if __name__ == "__main__":
    main()


"""
해야되는일 
/ 수정해야되는 부분
1. 열리고 닫히는 트리거를 생성할때 마지막으로 동작후 30분 지났어야함

/ 점검해야되는 부분
1. 
"""