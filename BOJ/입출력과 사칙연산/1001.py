#두 수를 입력받고 뺄셈을 한 결과를 출력하는 문제

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    A, B = map(int, input().strip().split())
    print(A-B)