# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# class 5
import sys
from bisect import bisect_left
input = sys.stdin.readline

if __name__ == "__main__":
    l = int(input())

    arr = list(map(int, input().split()))

    stack = [0]
    for a in arr:
        if stack[-1] < a:
            stack.append(a)
        else:
            stack[bisect_left(stack, a)] = a

    print(len(stack)-1)
