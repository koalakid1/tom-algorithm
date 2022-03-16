# BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.

# 오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.

# A는 B와 친구다.
# B는 C와 친구다.
# C는 D와 친구다.
# D는 E와 친구다.
# 위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline


def dfs(index, length):
    global check
    if length == 5:
        check = True
        return

    for i in graph[index]:
        if visited[i]:
            visited[i] = False
            dfs(i, length + 1)
            visited[i] = True


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    graph = [[] for _ in range(n)]
    visited = [True for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    check = False
    for i in range(n):
        visited[i] = False
        dfs(i, 1)
        visited[i] = True

        if check:
            break

    print(1 if check else 0)
