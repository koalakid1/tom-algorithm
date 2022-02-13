#시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    A = int(input())

    print("A" if A >= 90 else "B" if A >= 80 else "C" if A >= 70 else "D" if A >= 60 else "F")