# 어떤 단어를 뒤에서부터 읽어도 똑같다면 그 단어를 팰린드롬이라고 한다. 'radar', 'sees'는 팰린드롬이다.

# 수도 팰린드롬으로 취급할 수 있다. 수의 숫자들을 뒤에서부터 읽어도 같다면 그 수는 팰린드롬수다. 121, 12421 등은 팰린드롬수다. 123, 1231은 뒤에서부터 읽으면 다르므로 팰린드롬수가 아니다. 또한 10도 팰린드롬수가 아닌데, 앞에 무의미한 0이 올 수 있다면 010이 되어 팰린드롬수로 취급할 수도 있지만, 특별히 이번 문제에서는 무의미한 0이 앞에 올 수 없다고 하자.

# class 2+
import sys
input = sys.stdin.readline


def 스택수열(num):
    리스트 = [n for n in range(1, num+1)]
    스택 = []
    수열 = []
    수열최댓값 = 0
    for _ in range(num):
        수 = int(input())
        if 수 > 수열최댓값:
            for i in range(수열최댓값 + 1, 수+1):
                수열.append(리스트[i-1])
                스택.append("+")
            수열.pop(-1)
            스택.append("-")
            수열최댓값 = 수
        else:
            if 수열[-1] == 수:
                수열.pop(-1)
                스택.append("-")
            else:
                return "NO"

    return 스택


if __name__ == "__main__":
    num = int(input())

    ans = 스택수열(num)
    if type(ans) is str:
        print(ans)
    else:
        for 스택 in ans:
            print(스택)
