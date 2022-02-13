# 빈 칸에 들어갈 수는?

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    first = int(input())
    second = input().strip()

    print(first * int(second[2]))
    print(first * int(second[1]))
    print(first * int(second[0]))
    print(first * int(second))