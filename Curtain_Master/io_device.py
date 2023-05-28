from Curtain_Master.constants import PATH
import ctypes

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

    def pull_motor(self):
        print('pull')
        #self.pull

    def push_motor(self):
        print('push')
        #self.push
    

class Photoresistor:
    def __init__(self):
        try:
            self.c_module = ctypes.cdll.LoadLibrary(PATH)
        except Exception as e:
            print(e)
            raise OSError()
        
        # 초기설정
        self.resistance_value = self.c_module.get_resistance
        self.resistance_value.argtypes = []
        self.resistance_value.restype = None
        print('Photoresistor init complete')


    def get_brigthtness_data(self):
        print('get_birthgtness')
        #result = self.resistance_value()
        # 전처리 필요하면 전처리
        #return result
        return 0

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
        #self.ledOn()

    def led_off(self):
        print('led_off')
        #self.ledOff()