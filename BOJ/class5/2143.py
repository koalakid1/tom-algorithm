# 한 배열 A[1], A[2], …, A[n]에 대해서, 부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다. 이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다. 각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때, A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.# class 5
# class5
import sys
from collections import defaultdict
input = sys.stdin.readline


if __name__ == "__main__":
    t = int(input())
    n = int(input())
    ns = list(map(int, input().strip().split()))
    m = int(input())
    ms = list(map(int, input().strip().split()))

    n_dict = defaultdict(int)
    for i in range(n):
        for j in range(i, n):
            n_dict[sum(ns[i:j+1])] += 1

    answer = 0
    for i in range(m):
        for j in range(i, m):
            answer += n_dict[t-sum(ms[i:j+1])]

    print(answer)
