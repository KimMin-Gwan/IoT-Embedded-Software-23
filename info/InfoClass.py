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
        self.m_flag = 'init'
    
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
    
    def turn_off_alarm(self):
        self._alarm_flag = False
    
    # 접근자
    def get_alarm_flag(self):
        return self._alarm_flag

    def is_alarm_time(self):
        if self._nowTime['hour'] == self._alarm_time['hour']:
            if self._nowTime['minute'] == self._alarm_time['minute']:
                self._alarm_flag = False
                return True

        return False

    # 접근자
    def get_alarm_time(self):
        return self._alarm_time

    # 알람 시간 변경자 
    def set_alarm(self, hour, min):
        self._alarm_flag = True
        self._alarm_time['hour'] = hour
        self._alarm_time['minute'] = min 

    # 요일 구해주는 함수
    def __set_weekday(index):
        index = int(index)
        if index == 0:
            return "Mon"
        elif index == 1:
            return "Tue"
        elif index == 2:
            return "Wed"
        elif index == 3:
            return "Thu"
        elif index == 4:
            return "Fri"
        elif index == 5:
            return "Sat"
        elif index == 6:
            return "Sun"
        else:
            return "???"
    def set_sec():
        pass

    def time_difference(self, history):
        # 시간 정보 추출
        hour1 = self._nowTime['hour']
        minute1 = self._nowTime['minute']
        second1= self._nowTime['second']

        hour2 = history['hour']
        minute2 = history['minute']
        second2= history['second']

        try:
            # 시간을 초로 변환
            total_seconds1 = hour1 * 3600 + minute1 * 60 + second1
            total_seconds2 = hour2 * 3600 + minute2 * 60 + second2
        except:
            total_seconds1 = 0
            total_seconds2 = 0

        # 두 시간의 차이 계산
        difference_seconds = abs(total_seconds1 - total_seconds2)

        # 초를 시, 분, 초로 변환
        difference_minute = (difference_seconds % 3600) // 60
        print('diff : ', difference_seconds)

        return difference_seconds

    def set_motor_flag(self, state):
        self.m_flag = state

    def get_motor_flag(self):
        return self.m_flag



