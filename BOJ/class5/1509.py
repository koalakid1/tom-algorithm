# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
# class 5
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    string = input().strip()

    n = len(string)
    dp = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    result = [2500 for _ in range(n+1)]
    result[-1] = 0

    for i in range(1, n):
        if string[i-1] == string[i]:
            dp[i-1][i] = 1

    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if string[i] == string[j] and dp[i+1][j-1]:
                dp[i][j] = 1

    for j in range(n):
        for i in range(j+1):
            if dp[i][j]:
                result[j] = min(result[j], result[i-1] + 1)
            else:
                result[j] = min(result[j], result[j-1] + 1)

    print(result[-2])
