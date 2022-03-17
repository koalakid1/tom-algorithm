# N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

# 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.
# class 5
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    graph = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]

    for _ in range(m):
        x, y = map(int, input().strip().split())
        graph[x].append(y)
        indegree[y] += 1

    queue = []
    for i in range(1, n+1):
        if not indegree[i]:
            queue.append(i)

    result = []
    while queue:
        x = queue.pop()
        result.append(x)
        for y in graph[x]:
            indegree[y] -= 1
            if not indegree[y]:
                queue.append(y)

    print(*result)
