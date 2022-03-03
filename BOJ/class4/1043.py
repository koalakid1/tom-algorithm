# 지민이는 파티에 가서 이야기 하는 것을 좋아한다. 파티에 갈 때마다, 지민이는 지민이가 가장 좋아하는 이야기를 한다.
# 지민이는 그 이야기를 말할 때, 있는 그대로 진실로 말하거나 엄청나게 과장해서 말한다.
# 당연히 과장해서 이야기하는 것이 훨씬 더 재미있기 때문에, 되도록이면 과장해서 이야기하려고 한다.
# 하지만, 지민이는 거짓말쟁이로 알려지기는 싫어한다. 문제는 몇몇 사람들은 그 이야기의 진실을 안다는 것이다.
# 따라서 이런 사람들이 파티에 왔을 때는, 지민이는 진실을 이야기할 수 밖에 없다.
# 당연히, 어떤 사람이 어떤 파티에서는 진실을 듣고, 또다른 파티에서는 과장된 이야기를 들었을 때도 지민이는 거짓말쟁이로 알려지게 된다.
# 지민이는 이런 일을 모두 피해야 한다.

# 사람의 수 N이 주어진다. 그리고 그 이야기의 진실을 아는 사람이 주어진다. 그리고 각 파티에 오는 사람들의 번호가 주어진다.
# 지민이는 모든 파티에 참가해야 한다. 이때, 지민이가 거짓말쟁이로 알려지지 않으면서, 과장된 이야기를 할 수 있는 파티 개수의 최댓값을 구하는 프로그램을 작성하시오.
# # class 4
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    people_num, party_num = map(int, input().strip().split())
    truth = set(input().strip().split()[1:])

    parties = []
    ans = []
    for _ in range(party_num):
        party = set(input().strip().split()[1:])
        parties.append(party)
        ans.append(1)

    for _ in range(party_num):
        for idx, party in enumerate(parties):
            if truth & party:
                truth = truth.union(party)
                ans[idx] = 0

    print(sum(ans))
