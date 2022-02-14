# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    numbers = input().strip()

    ans = 0
    for number in numbers:
        ans += int(number)
    
    print(ans)