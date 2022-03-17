# 명우는 홍준이와 함께 팰린드롬 놀이를 해보려고 한다.

# 먼저, 홍준이는 자연수 N개를 칠판에 적는다. 그 다음, 명우에게 질문을 총 M번 한다.

# 각 질문은 두 정수 S와 E(1 ≤ S ≤ E ≤ N)로 나타낼 수 있으며, S번째 수부터 E번째 까지 수가 팰린드롬을 이루는지를 물어보며, 명우는 각 질문에 대해 팰린드롬이다 또는 아니다를 말해야 한다.

# 예를 들어, 홍준이가 칠판에 적은 수가 1, 2, 1, 3, 1, 2, 1라고 하자.

# S = 1, E = 3인 경우 1, 2, 1은 팰린드롬이다.
# S = 2, E = 5인 경우 2, 1, 3, 1은 팰린드롬이 아니다.
# S = 3, E = 3인 경우 1은 팰린드롬이다.
# S = 5, E = 7인 경우 1, 2, 1은 팰린드롬이다.
# 자연수 N개와 질문 M개가 모두 주어졌을 때, 명우의 대답을 구하는 프로그램을 작성하시오.
# class 5
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().strip().split()))

    dp = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    for i in range(1, n):
        if nums[i-1] == nums[i]:
            dp[i-1][i] = 1

    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if nums[i] == nums[j] and dp[i+1][j-1]:
                dp[i][j] = 1

    m = int(input())
    for _ in range(m):
        s, e = map(int, input().strip().split())
        print(dp[s-1][e-1])
