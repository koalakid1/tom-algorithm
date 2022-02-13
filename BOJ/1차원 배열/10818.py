# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    y = int(input())

    print(1 if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0 else 0)