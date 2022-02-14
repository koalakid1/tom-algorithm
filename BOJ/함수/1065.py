# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

import sys
input = sys.stdin.readline

def hansoo(n):

    ans = 0

    for num in range(111, n+1):
        num_str = str(num)
        d1, d2 = int(num_str[0]) - int(num_str[1]), int(num_str[1]) - int(num_str[2])
        
        if d1 == d2:
            ans += 1

    return ans

if __name__ == "__main__":
    n = int(input())

    ans = 0
    if n < 100:
        ans += n        
    else:
        ans += 99
        ans += hansoo(n)
    
    print(ans)