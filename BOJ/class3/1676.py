# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
# class 3++
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    ans = 0
    for i in range(n+1):
        check = i
        while True:
            if check % 5 != 0 or check // 5 == 0:
                break
            ans += 1
            check //= 5
            
    print(ans)