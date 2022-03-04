

# # class 4
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def find_preorder(in_start, in_end, post_start, post_end):
    global preorder
    if in_start > in_end or post_start > post_end:
        return

    parents = postorder[post_end]
    preorder.append(parents)
    left = inorder_index[parents] - in_start
    right = in_end - inorder_index[parents]

    find_preorder(in_start, in_start + left - 1,
                  post_start, post_start + left - 1)
    find_preorder(in_end - right + 1, in_end, post_end - right, post_end - 1)


if __name__ == "__main__":
    n = int(input())
    inorder = list(map(int, input().strip().split()))
    postorder = list(map(int, input().strip().split()))
    inorder_index = [0] * (n+1)
    for i in range(n):
        inorder_index[inorder[i]] = i
    preorder = []

    find_preorder(0, n-1, 0, n-1)
    print(*preorder)
