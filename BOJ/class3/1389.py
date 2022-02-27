# 케빈 베이컨의 6단계 법칙
# class 3++
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    friends = [[] for _ in range(n+1)]
    is_friends = [[True for _ in range(n+1)] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, input().strip().split())
        if is_friends[a][b] and is_friends[b][a]:
            friends[a].append(b) 
            friends[b].append(a)
            is_friends[a][b] = False
            is_friends[b][a] = False
    
    min_person = 0
    min_level = sys.maxsize
    for p in range(1,n+1):
        visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
        level = 0
        queue = [(p,level)]
        levels = 0
        while queue:
            person, level = queue.pop(0)
            
            for other in friends[person]:
                if not visited[other][person] and not visited[person][other]:
                    visited[other][person], visited[person][other] = level + 1, level + 1
                    queue.append((other, level + 1))
                    levels += level + 1
            
        if min_level > levels:
            min_person = p
            min_level = levels
    
    print(min_person)