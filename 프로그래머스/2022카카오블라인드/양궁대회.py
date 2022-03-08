from collections import Counter
from itertools import combinations_with_replacement


def solution(n, info):
    answer = []
    max_value = 0
    max_count = Counter()
    for combination in combinations_with_replacement(range(11), n):
        count = Counter(combination)
        score_other, score_me = 0, 0
        for i in range(1, 11):
            if info[10-i] < count[i]:
                score_me += i
            elif info[10-i] > 0:
                score_other += i

        diff_score = score_me - score_other
        if max_value < diff_score:
            max_value = diff_score
            max_count = count
        elif max_value == diff_score:
            for i in range(10, -1, -1):
                if max_count[i] > count[i]:
                    max_count = count
                    break
                elif max_count[i] < count[i]:
                    break
    if max_value > 0:
        for i in range(10, -1, -1):
            answer.append(max_count[i])
        return answer
    else:
        return [-1]
