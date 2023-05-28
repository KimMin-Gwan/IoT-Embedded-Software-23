import ctypes      # 파이썬 extension을 사용하기 위한 모듈
import platform    # 파이썬 아키텍처를 확인하기 위한 모듈
import time

if 'Windows' == platform.system() :     # 윈도우 운영체제에서 c 모듈 로드
    path = './testC2Py.dll'
    c_module = ctypes.windll.LoadLibrary(path)
elif 'Linux' == platform.system() :     # 리눅스 운영체제에서 c 모듈 로드
    #path = "./libc_module.so"
    path = "./../Device_Driver/temp/externApp.so"
    c_module = ctypes.cdll.LoadLibrary(path)
else :
    raise OSError()
    

def main():
    print(c_module)

    # 함수 주소 포인터
    ledOn = c_module.ledOn
    ledOff = c_module.ledOff

    # c에서 제작한 함수 파라미터 형식 지정
    ledOn.argtypes = []
    ledOff.argtypes = []

    # c에서 제작한 함수 리턴 형식 지정
    ledOn.restype = None
    ledOff.restype = None
    
    # 사용부
    while True:
        ledOn()
        time.sleep(1)
        ledOff()
        time.sleep(1)


if __name__ == "__main__":
    main()
