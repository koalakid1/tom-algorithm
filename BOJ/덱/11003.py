# N개의 수 A1, A2, ..., AN과 L이 주어진다.

# Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때, D에 저장된 수를 출력하는 프로그램을 작성하시오. 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.

import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n, l = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))

    queue = deque()
    for i in range(n):
        if i >= l and queue[0][1] == i-l:
            queue.popleft()
        
        while queue and queue[-1][0] > a[i]:
            queue.pop()
            
        queue.append((a[i],i))
        
        print(queue[0][0], end = " ")

