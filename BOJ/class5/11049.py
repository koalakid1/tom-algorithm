# 크기가 N×M인 행렬 A와 M×K인 B를 곱할 때 필요한 곱셈 연산의 수는 총 N×M×K번이다. 행렬 N개를 곱하는데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 된다.

# 예를 들어, A의 크기가 5×3이고, B의 크기가 3×2, C의 크기가 2×6인 경우에 행렬의 곱 ABC를 구하는 경우를 생각해보자.

# AB를 먼저 곱하고 C를 곱하는 경우 (AB)C에 필요한 곱셈 연산의 수는 5×3×2 + 5×2×6 = 30 + 60 = 90번이다.
# BC를 먼저 곱하고 A를 곱하는 경우 A(BC)에 필요한 곱셈 연산의 수는 3×2×6 + 5×3×6 = 36 + 90 = 126번이다.
# 같은 곱셈이지만, 곱셈을 하는 순서에 따라서 곱셈 연산의 수가 달라진다.

# 행렬 N개의 크기가 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값을 구하는 프로그램을 작성하시오. 입력으로 주어진 행렬의 순서를 바꾸면 안 된다.
# class 5
import sys
input = sys.stdin.readline


    n = int(input())
    graph = [tuple(map(int, input().strip().split())) for _ in range(n)]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for y in range(1, n):
        for x in range(n-y):
            if y == 1:
                dp[x][x+y] = graph[x][0] * graph[x][1] * graph[x+1][1]
            else:
                dp[x][x+y] = 2 ** 31
                for k in range(x, x+y):
                    dp[x][x+y] = min(dp[x][x+y], dp[x][k] + dp[k+1][x+y] +
                                     graph[x][0] * graph[k][1] * graph[x+y][1])
    print(dp[0][-1])
