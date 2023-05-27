import ctypes
import time

PATH = './Device_Driver/temp/externApp.so'

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
    resist_value = c_module.getBrightness
    resist_value.argtypes = []
    resist_value.restype = ctypes.c_int

    resist_test= c_module.printPhotoregisterValue
    resist_test.argtypes = []
    resist_test.restype = None

    #--------------------------------

    ledOn = c_module.ledOn
    ledOff = c_module.ledOff

    ledOn.argtypes = []
    ledOn.restype = None

    ledOff.argtypes = []
    ledOff.restype = None
    #---------------------------------
    while True:    
        pull()

if __name__ == '__main__':
    main()
