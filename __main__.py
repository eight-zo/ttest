from . import *

if __name__ == '__main__':
    print("--- 계산기 패키지 실행 ---")
    print(f"3 + 5 = {add(3, 5)}")
    print(f"10 - 4 = {minus(10, 4)}")
    print(f"3 * 5 = {multiplication(3, 5)}")
    print(f"10 / 2 = {division(10, 2)}")
    print("10 / 0 = ", end="")
    division(10, 0)
