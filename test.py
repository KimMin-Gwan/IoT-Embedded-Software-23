import ctypes

PATH = './../nunna/externaApp.so'

c_module = ctypes.cdll.LoadLibrary(PATH)

def main():
    print(c_module)

    pull = c_module.stepMotorCW
    push = c_module.stepMotorCCW

    pull.argtypes = []
    pull.argtypes = None

    push.argtypes = []
    push.restype = None

    #--------------------------------
    resist_value = c_module.get_resistance
    resist_value.argtypes = []
    resist_value.restype = ctypes.c_int 

    #--------------------------------

    ledOn = c_module.ledOn
    ledOff = c_module.ledOff

    ledOn.argtypes = []
    ledOn.restype = None

    ledOff.argtypes = []
    ledOff.restype = None

    #---------------------------------

    ledRun = c_module.ledRun
    ledRun.argtypes = []
    ledRun.restype = None

    stepMotorRun = c_module.stepMotorRun
    ledRun.argtypes = []
    ledRun.restype = None



if __name__ == '__main__':
    main()