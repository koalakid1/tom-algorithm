# 주어진 히스토그램에 대해, 가장 큰 직사각형의 넓이를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = [int(input()) for _ in range(n)]

    stack = []
    result = 0
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            height = nums[stack.pop()]
            width = i
            if stack:
                width -= stack[-1] + 1
            result = max(result, width * height)
        stack.append(i)

    while stack:
        height = nums[stack.pop()]
        width = n
        if stack:
            width -= stack[-1] + 1
        result = max(result, width * height)
