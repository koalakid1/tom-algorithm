#N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.

import sys
input = sys.stdin.readline

def multiplication(n):
    for i in range(1,10):
        print(f"{n} * {i} = {n * i}")

if __name__ == "__main__":
    n = int(input())

    multiplication(n)