import Curtain_Master as CM
import threading

class Curtain():
    # 생성자
    def __init__(self, info_master):
        self._photoresist = CM.Photoresistor()
        self._led = CM.Led()
        self._motor = CM.Motor()
        self._curtain_flag = True # True일 때 걷어진 상태 
        self._brightness = 0
        self.p_info= info_master
        self.history = {'hour':0,
                       'minute':0,
                       'second':0
                            }

    # 밝기 조정자
    def set_brightness(self):
        self.brightenss = self._photoresist.get_brightness_data()

    def get_curtain_flag(self):
        return self._curtain_flag

    def get_brightness(self):
        return self._brightness
    
    def change_curtain_flag(self):
        if self._curtain_flag == False:
            self._curtain_flag = True
        else:
            self._curtain_flag = False 

    # 밝기에 따라 커튼을 조작하도록 하는 함수
    # 멀티스레드를 사용해야될 수 있음
    # 모터가 움직이는 동안 모든 시스템이 정지해있을 수도 있기때문
    def check_birghtness(self):
        print('history : ', self.history)
        # 최소 30분에 한번씩 동작할것  
        # 테스트를 위해 30초로 설정
        if self.p_info.time_difference(self.history) < 30:
            print('not yet')
            return
        
        self._photoresist.get_brigthtness_data()
        self._brightness = self._photoresist.return_brigthtness()
        # 어둡다 == 1
        # 1 == 닫는다.
        # 밝다 == 0
        # 0 == 연다.
        if self._brightness == CM.PATIENCE:
            self._led.led_on()
            print('Operation flag : open')
            if self._curtain_flag is False:
                print("Open")
                thread = threading.Thread(target=self._motor.pull_motor)
                thread.start()
                #self._motor.pull_motor()
                self.change_curtain_flag()
                self._set_history()
                return True
            else:
                print("already opened")
        else:
            self._led.led_off()
            print('Operation flag : close')
            if self._curtain_flag is True:
                print('Close')
                thread = threading.Thread(target=self._motor.push_motor)
                thread.start()
                #self._motor.push_motor()
                self.change_curtain_flag()
                self._set_history()
                return True
            else:
                print('already closed')
        return False
            
    def move_curtain(self, flag):

        # 커튼을 열어라 인데
        if flag is False:
            print('Operation flag : open')
            # 커튼이 닫쳐 있으면 커튼을 열어라
            if self._curtain_flag is False:
                print("Open")
                thread = threading.Thread(target=self._motor.pull_motor)
                thread.start()
                #self._motor.pull_motor()
                self._curtain_flag = True
                self._set_history()
            else:
                return
        # 닫아라 인데
        else:
            print('Operation flag : close')
            # 열려있으면 닫아라
            if self._curtain_flag is True:
                print('Close')
                thread = threading.Thread(target=self._motor.push_motor)
                thread.start()
                #self._motor.push_motor()
                self._curtain_flag = False
                self._set_history()
            else:
                return
        return
            

    def _set_history(self):
        t = self.p_info.get_time()
        hour = t['hour']
        min = t['minute']
        sec = t['second']

        self.history['hour'] = hour
        self.history['minute'] = min 
        self.history['second'] = sec


