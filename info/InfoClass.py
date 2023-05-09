import info
from datetime import datetime
import time 

# 기본정보를 가지는 클래스
"""
가지고 있어야 하는 정보
1. 현재시간
2. 현재날짜
3. 알람 플래그
4. 알람 설정 시간
"""

class Information:
    # 생성자
    def __init__(self):
        self._nowDate = info.DATE
        self._nowTime= info.TIME
        self.update_time()
        self._alarm_flag = False
        self._alarm_time = info.TIME
    
    # 호출함수
    def __call__(self):
        print("date : ", self._nowDate)
        print("time : ", self._nowTime)
        print("alarm state : ", self._alarm_flag)
        print("alarm time : ", self._alarm_time)

    # 멤버 시간 업데이트 함수
    def update_time(self):
        t = time.time()  # 메모리 누수를 줄이기 위해 time()사용
        self._now = datetime.fromtimestamp(t)
        self._nowDate['year'] =  self._now.year
        self._nowDate['month'] = self._now.month
        self._nowDate['day'] = self._now.day
        self._nowDate['weekday'] = Information.__set_weekday(self._now.weekday()) 
        self._nowTime['hour'] =  self._now.hour
        self._nowTime['minute'] = self._now.minute
        self._nowTime['second'] = self._now.second

    # 접근자
    def get_date(self):
        return self._nowDate

    # 접근자
    def get_time(self):
        return self._nowTime
    
    # 접근자
    def get_alarm_flag(self):
        return self._alarm_flag

    # 접근자
    def get_alarm_time(self):
        return self._alarm_time

    # 알람 시간 변경자 
    def set_alarm(self, flag, time = [0,0,0]):
        self._alarm_flag = flag
        self._alarm_time = time

    # 요일 구해주는 함수
    def __set_weekday(index):
        if index is 0:
            return "Monday"
        elif index is 1:
            return "Tuesday"
        elif index is 2:
            return "Wednesday"
        elif index is 3:
            return "Thursday"
        elif index is 4:
            return "Friday"
        elif index is 5:
            return "Saturday"
        elif index is 6:
            return "Sunday"
        else:
            return "Something Wrong"




