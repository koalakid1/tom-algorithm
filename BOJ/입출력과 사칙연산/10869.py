#모든 연산 문제

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    A, B = map(int, input().strip().split())
    print(A+B)
    print(A-B)
    print(A*B)
    print(A//B)
    print(A%B)