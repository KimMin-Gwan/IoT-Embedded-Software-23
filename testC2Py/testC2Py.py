import ctypes                           # 파이썬 extension을 사용하기 위한 모듈
import platform                         # 파이썬 아키텍처를 확인하기 위한 모듈

if 'Windows' == platform.system() :     # 윈도우 운영체제에서 c 모듈 로드
    path = './testC2Py.dll'
    c_module = ctypes.windll.LoadLibrary(path)
elif 'Linux' == platform.system() :     # 리눅스 운영체제에서 c 모듈 로드
    path = "./libc_module.so"
    c_module = ctypes.cdll.LoadLibrary(path)
else :
    raise OSError()
    

def main():
    print(c_module)
    # int add(int a, int b)
    
    # 함수 주소 포인터
    add = c_module.add  
    print("add : ", add)   # <_FuncPtr object at 0x000002196BFE9860>
    
    # c에서 제작한 add 함수 파라미터 형식 지정
    add.argtypes = (ctypes.c_int, ctypes.c_int) 

    # c에서 제작한 add 함수 리턴 형식 지정
    add.restype = ctypes.c_int

    # 실제로 사용
    res = add(1, 2)

    # 결과 출력
    print('res :', res)   # 3

if __name__ == "__main__":
    main()