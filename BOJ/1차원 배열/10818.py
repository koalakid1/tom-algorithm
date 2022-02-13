# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    l = list(map(int, input().strip().split()))
    
    print(f"{min(l)} {max(l)}")