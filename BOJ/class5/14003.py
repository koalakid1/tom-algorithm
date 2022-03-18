# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# class 5
import sys
from bisect import bisect_left
input = sys.stdin.readline

if __name__ == "__main__":
    l = int(input())

    arr = list(map(int, input().split()))

    stack = [-1000000001]
    stack_index = [-1]
    dp = [-1]
    for index, a in enumerate(arr):
        if stack[-1] < a:
            stack.append(a)
            stack_index.append(index)
            dp.append(stack_index[-2])

        else:
            idx = bisect_left(stack, a)
            stack[idx] = a
            stack_index[idx] = index
            dp.append(stack_index[idx-1])

    result = []
    end = stack_index[-1]
    result.append(arr[end])
    for i in range(len(stack)-2):
        end = dp[end+1]
        result.append(arr[end])

    print(len(stack)-1)
    print(*reversed(result))
