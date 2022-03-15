# 어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다.
# 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다.
# 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.

import sys
input = sys.stdin.readline


def init(node, left, right):
    if left == right:
        tree[node] = nums[left]
        return

    mid = (left + right) // 2
    init(node * 2, left, mid)
    init(node * 2 + 1, mid + 1, right)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]


def find(node, left, right, start, end):
    if left > end or right < start:
        return 0

    if start <= left and right <= end:
        return tree[node]

    mid = (left + right) // 2
    return find(node * 2, left, mid, start, end) + find(node * 2 + 1, mid+1, right, start, end)


def update(node, left, right, index, diff):
    if index < left or index > right:
        return

    tree[node] += diff

    if left == right:
        return

    mid = (left + right) // 2
    update(node * 2, left, mid, index, diff)
    update(node * 2 + 1, mid + 1, right, index, diff)


if __name__ == "__main__":
    n, m, k = map(int, input().strip().split())
    nums = [int(input()) for _ in range(n)]
    tree = [0 for _ in range(3000000)]
    init(1, 0, n-1)

    for _ in range(m+k):
        a, b, c = map(int, input().strip().split())
        if a == 1:
            c, nums[b-1] = c - nums[b-1], c

            update(1, 0, n-1, b-1, c)
        else:
            print(find(1, 0, n-1, b-1, c-1))
