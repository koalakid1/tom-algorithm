#N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, s = map(int, input().strip().split())
    int_list = list(map(int, input().strip().split()))

    ans = 0
    for i in range(1, 1<<n):
        total = 0
        for j in range(n):
            total += int_list[j] if i & (1 << j) else 0
        if total == s:
            ans += 1
    
    print(ans)