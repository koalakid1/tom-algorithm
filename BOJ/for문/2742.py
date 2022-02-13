#자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    for i in range(n,0,-1):
        print(i)