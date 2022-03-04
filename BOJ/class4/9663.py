# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
# # class 4
import sys
input = sys.stdin.readline


def n_queen(x):
    global ans
    if x == n:
        ans += 1
        return

    for y in range(n):
        graph[x] = y
        check = True
        for i in range(x):
            if graph[x] == graph[i] or abs(graph[x] - graph[i]) == x - i:
                check = False
                break

        if check:
            n_queen(x+1)


if __name__ == "__main__":
    n = int(input())

    graph = [0 for _ in range(n)]

    ans = 0
    n_queen(0)

    print(ans)
