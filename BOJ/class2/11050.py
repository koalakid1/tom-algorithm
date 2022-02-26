# 자연수 N과 정수 K가 주어졌을 때 이항 계수 binom{N}{K}를 구하는 프로그램을 작성하시오

# class2+

import sys
input = sys.stdin.readline


def 이항계수(n, k):
    ans = 1
    for num in range(n, n-k, -1):
        ans *= num

    for num in range(1, k+1):
        ans //= num
    return ans


if __name__ == "__main__":
    n, k = map(int, input().strip().split())

    print(이항계수(n, k))
