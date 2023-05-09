import LCD
import info

"""
가지고 있어야 하는 멤버
1. GPIO 핀 배열초기화 (필요없을지도)
2. 출력할 데이터 : string
 - 구글링해서 만들어야합니다
"""
class L2C_LCD():
    # 생성자
    def __init__(self):

        #gpio

        pass

    # 호출자
    def __call__(self):
        print("date : ", self._time)
        print("time : ", self._date)
        print("alarm state : ", self._alarm_flag)
        print("alarm time : ", self._alarm_time)

    # 인포메이션을 통해 데이터 생성
    def set_member(self, information):
        self._time = information.get_time()
        self._date = information.get_date()
        self._alarm_flag = information.get_alarm_flag()
        if self._alarm_flag is True:
            self._set_alarm_time(information)
        else:
            self._set_alarm_time()

    # 알람 시간 생성자
    def _set_alarm_time(self, information = None):
        if information is None:
            self._alarm_time = info.TIME
        else:
            self._alarm_time = information.get_alarm_time()

    # lcd에 표시를 수행하는 멤버함수
    def draw_lcd(self):
        pass