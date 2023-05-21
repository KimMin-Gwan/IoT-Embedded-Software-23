from Curtain_Master.constants import STEP_MOTOR_PATH, RESISTOR_PATH, LED_PATH
import ctypes

class Motor:
    def __init__(self):
        try:
            self.c_module = ctypes.cdll.LoadLibrary(STEP_MOTOR_PATH)
        except:
            raise OSError()

        # 함수 주소 포인터
        self.pull = self.c_module.pull
        self.push = self.c_module.push

        # c에서 제작한 함수 파라미터 형식 지정
        self.pull.argtypes = []
        self.pull.argtypes = None

        # c에서 제작한 함수 리턴 형식 지정
        self.push.argtypes = []
        self.push.argtypes = None

    def pull_motor(self):
        #반복문?
        self.pull
        return

    def pull_motor(self):
        #반복문?
        self.push
        return
    

class Photosresistor:
    def __init__(self):
        try:
            self.c_module = ctypes.cdll.LoadLibrary(RESISTOR_PATH)
        except:
            raise OSError()
        
        # 초기설정
        self.resistance_value = self.c_module.get_resistance
        self.resistance_value.argtypes = []
        self.resistance_value.restype = None


    def get_brigthtness_data(self):
        result = self.resistance_value()
        # 전처리 필요하면 전처리
        return result

class Led:
    def __init__(self):
        try:
            self.c_module = ctypes.cdll.LoadLibrary(LED_PATH)
        except:
            raise OSError()
        
        # 초기설정
        self.red_on= self.c_module.red_led_on
        self.green_on= self.c_module.green_led_on
        self.blue_on= self.c_module.blue_led_on

        self.red_off= self.c_module.red_led_off
        self.green_off= self.c_module.green_led_off
        self.blue_off= self.c_module.blue_led_off

        self.red_on.argtypes = []
        self.red_on.restype = None

        self.red_off.argtypes = []
        self.red_off.restype = None

        self.green_on.argtypes = []
        self.green_on.restype = None

        self.green_off.argtypes = []
        self.green_off.restype = None

        self.blue_on.argtypes = []
        self.blue_on.restype = None

        self.blue_off.argtypes = []
        self.blue_off.restype = None

    def led_red_on(self):
        self.red_on()
        return

    def led_red_off(self):
        self.red_off()
        return

    def led_green_on(self):
        self.green_on()
        return

    def led_green_off(self):
        self.green_off()
        return

    def led_blue_on(self):
        self.blue_on()
        return

    def led_blue_off(self):
        self.blue_off()
        return