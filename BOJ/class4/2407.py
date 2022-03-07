# nCm을 출력한다.
# # class 4
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().strip().split())

    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][0], dp[i][i] = 1, 1
    for i in range(1, n+1):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    print(dp[-1][m])
