# 오늘은 신승원의 생일이다.

# 박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.

# 공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.

# 공항에는 P개의 비행기가 순서대로 도착할 예정이며, 당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다. 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.

# 신승원은 가장 많은 비행기를 공항에 도킹시켜서 박승원을 행복하게 하고 싶어한다. 승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?
# class5
import sys
input = sys.stdin.readline


def find(v):
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]


def union(a, b):
    a = find(a)
    b = find(b)
    if b > a:
        parent[b] = a
    else:
        parent[a] = b


if __name__ == "__main__":
    g = int(input())
    p = int(input())
    nums = [int(input()) for _ in range(p)]
    parent = [i for i in range(g+1)]

    answer = 0
    for num in nums:
        x = find(num)
        if x == 0:
            break
        answer += 1
        union(x, x-1)

    print(answer)
