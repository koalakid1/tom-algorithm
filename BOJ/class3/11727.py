# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# class3++
import sys
input = sys.stdin.readline


def 타일링(n):
    dp = [1, 3]
    for i in range(2, n):
        dp.append((dp[i-1] + dp[i-2] * 2) % 10007)
    return dp[-1]


if __name__ == "__main__":
    n = int(input())

    if n == 1 or n == 2:
        print(n + n // 2)
    else:
        print(타일링(n))
