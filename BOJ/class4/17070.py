# 파이프 옮기기 1

# # class 4+
from math import gcd
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().strip().split())) for _ in range(n)]
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
    dp[0][0][1] = 1
    for idx in range(2, n):
        if graph[0][idx]:
            break
        dp[0][0][idx] = 1

    for x in range(1, n):
        for y in range(2, n):
            if not graph[x][y]:
                dp[0][x][y] = dp[0][x][y-1] + dp[2][x][y-1]
                dp[1][x][y] = dp[1][x-1][y] + dp[2][x-1][y]
                if not graph[x-1][y] and not graph[x][y-1]:
                    dp[2][x][y] = sum(dp[z][x-1][y-1] for z in range(3))

    print(sum(dp[z][-1][-1] for z in range(3)))
