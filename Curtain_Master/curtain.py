import Curtain_Master as CM

class Curtain_Master():
    # 생성자
    def __init__(self):
        self._photoresist = CM.Photosresistor()
        self._motor = CM.Motor()
        self._curtain_flag = False # True일 때 걷어진 상태 
        self._brightness = 0

    # 밝기 조정자
    def set_brightness(self):
        self.brightenss = self._photoresist.get_brightness()

        pass

    def get_curtain_flag(self):
        return self._curtain_flag

    def get_brightness(self):
        return self._brightness

    # 밝기에 따라 커튼을 조작하도록 하는 함수
    # 멀티스레드를 사용해야될 수 있음
    # 모터가 움직이는 동안 모든 시스템이 정지해있을 수도 있기때문
    def check_birghtness(self):
        if self._brightness > CM.PATIENCE:
            if self._curtain_flag is False:
                self._motor.pull()
                self._curtain_flag = True
        else:
            if self._curtain_flag is True:
                self._motor.push()
                self._curtain_flag = False
        return
        pass
            
    def move_curtain(self, flag):
        # 커튼을 열어라 인데
        if flag is False:
            # 커튼이 닫쳐 있으면 커튼을 열어라
            if self._curtain_flag is False:
                self._motor.pull()
                self._curtain_flag = True
            else:
                return
        # 닫아라 인데
        else:
            # 열려있으면 닫아라
            if self._curtain_flag is True:
                self._motor.push()
                self._curtain_flag = False
            else:
                return
        return
            



