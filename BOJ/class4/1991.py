# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

# 예를 들어 위와 같은 이진 트리가 입력되면,

# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
# 가 된다.
# # class 4
import sys
input = sys.stdin.readline


def 전위순회(node):
    global 전위

    전위 += node
    if node in lefts:
        전위순회(lefts[node])

    if node in rights:
        전위순회(rights[node])


def 중위순회(node):
    global 중위

    if node in lefts:
        중위순회(lefts[node])

    중위 += node

    if node in rights:
        중위순회(rights[node])


def 후위순회(node):
    global 후위

    if node in lefts:
        후위순회(lefts[node])

    if node in rights:
        후위순회(rights[node])

    후위 += node


if __name__ == "__main__":
    node_num = int(input())
    lefts = {}
    rights = {}
    for _ in range(node_num):
        node, left, right = map(str, input().strip().split())

        if left != ".":
            lefts[node] = left

        if right != ".":
            rights[node] = right

    전위, 중위, 후위 = "", "", ""
    전위순회("A")
    중위순회("A")
    후위순회("A")
    print(f"{전위}\n{중위}\n{후위}")
