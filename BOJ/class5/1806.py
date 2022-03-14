# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
# class 5
import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, S = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))

    s = nums[0]
    x, y = 0, 0
    answer = n+1
    while True:
        if s >= S:
            s -= nums[x]
            answer = min(answer, y-x+1)
            x += 1
        else:
            y += 1
            if y == n:
                break
            s += nums[y]

    print(answer if answer != n+1 else 0)
