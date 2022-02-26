# 해시함수
# class2++

import sys
input = sys.stdin.readline


def 해싱(l, string):
    r, m = 31, 1234567891

    ans = 0
    for i in range(l):
        ans += (ord(string[i]) - ord('a') + 1) * (r ** i)

    return ans % m


if __name__ == "__main__":
    l = int(input())
    string = input().strip()

    print(해싱(l, string))
