#두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    A, B = map(int, input().strip().split())

    print("<" if A < B else ">" if A > B else "==")