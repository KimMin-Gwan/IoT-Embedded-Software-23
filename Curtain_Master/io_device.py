from Curtain_Master.constants import PATH
import ctypes

class Motor:
    def __init__(self):
        try:
            self.c_module = ctypes.cdll.LoadLibrary(PATH)
        except:
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

    def pull_motor(self):
        self.pull()

    def push_motor(self):
        self.push()
    

class Photoresistor:
    def __init__(self):
        try:
            self.c_module = ctypes.cdll.LoadLibrary(PATH)
        except:
            raise OSError()
        
        # 초기설정
        self.resistance_value = self.c_module.getBrightness
        self.resistance_value.argtypes = []
        self.resistance_value.restype = ctypes.c_int 


    def get_brigthtness_data(self):
        result = self.resistance_value()
        # 전처리 필요하면 전처리
        return result

class Led:
    def __init__(self):
        try:
            self.c_module = ctypes.cdll.LoadLibrary(PATH)
        except:
            raise OSError()
        
        self.ledOn = self.c_module.ledOn
        self.ledOff= self.c_module.ledOff

        self.ledOn.argtypes = []
        self.ledOn.restype = None

        self.ledOff.argtypes = []
        self.ledOff.restype = None

    def led_on(self):
        self.ledOn()

    def led_off(self):
        self.ledOff()
