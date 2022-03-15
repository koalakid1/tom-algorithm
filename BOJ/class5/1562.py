# 45656이란 수를 보자.

# 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

# N이 주어질 때, 길이가 N이면서 0부터 9까지 숫자가 모두 등장하는 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. 0으로 시작하는 수는 계단수가 아니다.
# class 5
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())

    re = 0
    dp = [[0 for _ in range(1024)] for _ in range(10)]

    for i in range(1, 10):
        dp[i][1 << i] = 1

    for i in range(1, n):
        dp_next = [[0 for _ in range(1024)] for _ in range(10)]
        for e in range(10):
            for bm in range(1024):
                if e < 9:
                    dp_next[e][bm | (1 << e)] = (
                        dp_next[e][bm | (1 << e)] + dp[e+1][bm]) % 1000000000
                if e > 0:
                    dp_next[e][bm | (1 << e)] = (
                        dp_next[e][bm | (1 << e)] + dp[e-1][bm]) % 1000000000
        dp = dp_next

    print(sum([dp[i][1023] for i in range(10)]) % 1000000000)
