from Curtain_Master.constants import PATH
import ctypes
import time

class Motor:
    def __init__(self):
        try:
            self.c_module = ctypes.cdll.LoadLibrary(PATH)
        except Exception as e:
            print(e)
            raise OSError()

        # 함수 주소 포인터
        self.pull = self.c_module.stepMotorCW
        self.push = self.c_module.stepMotorCCW

        # c에서 제작한 함수 파라미터 형식 지정
        self.pull.argtypes = []
        self.pull.argtypes = None

        # c에서 제작한 함수 리턴 형식 지정
        self.push.argtypes = []
        self.push.argtypes = None
        print('Motor init complete')
        self.f_push= False
        self.f_pull= False

    def pull_motor(self):
        print('pull')
        i = 0
        self.f_pull = True
        time.sleep(0.5)
        while i < 1600:
            if self.push == True:
                self.f_pull = False
                return
            i += 1
            self.pull()
        self.f_pull = False

    def push_motor(self):
        print('push')
        i = 0
        self.f_push = False 
        time.sleep(0.5)
        while i < 1600:
            if self.f_pull == True:
               break 
            i += 1
            self.push()
        self.f_push = False
    

class Photoresistor:
    def __init__(self):
        try:
            self.c_module = ctypes.cdll.LoadLibrary(PATH)
        except Exception as e:
            print(e)
            raise OSError()
        
        # 초기설정
        self.resistance_value = self.c_module.getBrightness
        self.resistance_value = self.c_module.getBrightness
        self.resistance_value.argtypes = []
        self.resistance_value.restype = ctypes.c_int
        print('Photoresistor init complete')
        self.result = 0


    def get_brigthtness_data(self):
        self.result = self.resistance_value()
        if self.result == None:
            self.result = 1
        print('get_birthgtness : ', self.result)

    def return_brigthtness(self):
        return self.result

class Led:
    def __init__(self):
        try:
            self.c_module = ctypes.cdll.LoadLibrary(PATH)
        except Exception as e:
            print(e)
            raise OSError()
        
        self.ledOn = self.c_module.ledOn
        self.ledOff= self.c_module.ledOff

        self.ledOn.argtypes = []
        self.ledOn.restype = None

        self.ledOff.argtypes = []
        self.ledOff.restype = None
        print('led init complete')

    def led_on(self):
        print('ledON')
        self.ledOn()

    def led_off(self):
        print('led_off')
        self.ledOff()
