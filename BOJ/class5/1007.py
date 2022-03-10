# 평면 상에 N개의 점이 찍혀있고, 그 점을 집합 P라고 하자. 집합 P의 벡터 매칭은 벡터의 집합인데, 모든 벡터는 집합 P의 한 점에서 시작해서, 또 다른 점에서 끝나는 벡터의 집합이다. 또, P에 속하는 모든 점은 한 번씩 쓰여야 한다.

# 벡터 매칭에 있는 벡터의 개수는 P에 있는 점의 절반이다.

# 평면 상의 점이 주어졌을 때, 집합 P의 벡터 매칭에 있는 벡터의 합의 길이의 최솟값을 출력하는 프로그램을 작성하시오.
# class 5
from math import inf, sqrt
import sys
from itertools import combinations
input = sys.stdin.readline


if __name__ == "__main__":
    for _ in range(int(input())):
        num = int(input())
        x_total = 0
        y_total = 0
        points = []
        ans = inf
        for _ in range(num):
            x, y = map(int, input().strip().split())
            points.append((x,y))
            x_total += x
            y_total += y
        
        for combination in combinations(points, num // 2):
            x_minus = 0
            y_minus = 0
            for x,y in combination:
                x_minus += x
                y_minus += y
            
            x_real = x_total - 2 * x_minus
            y_real = y_total - 2 * y_minus

            ans = min(ans, sqrt((x_real ** 2) + (y_real ** 2)))
        
        print(ans)