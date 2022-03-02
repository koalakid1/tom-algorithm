# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
# class3++
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    num_list = list(map(int, input().strip().split()))

    sum_list = [0]
    temp = 0
    for num in num_list:
        temp += num
        sum_list.append(temp)

    for _ in range(m):
        i, j = map(int, input().strip().split())
        print(sum_list[j] - sum_list[i-1])
