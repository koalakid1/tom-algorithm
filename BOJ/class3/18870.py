# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
# class3+
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    num_list = list(map(int, input().strip().split()))
    sort_num_list = sorted(num_list)
    num_dict = dict()

    last_num = -sys.maxsize
    num_dict[last_num] = -1
    for num in sort_num_list:
        if num != last_num:
            num_dict[num] = num_dict[last_num] + 1
            last_num = num

    for num in num_list:
        print(num_dict[num])
