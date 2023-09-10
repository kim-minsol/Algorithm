import sys

sys.setrecursionlimit(100000) # 재귀 함수 제한이 990개이므로, sys 활용하여 재귀 함수 제한 해제

n, m = map(int, input().split())
s = [i for i in range(n+1)]


# def find(x):  # 부모 노드 탐색
#     if s[x] != x:
#         return find(s[x])
#     return x
def find(x):  # 탐색 루트를 줄이기 위해서 다음의 최적화 find 함수로 사용.
    if s[x] != x:
        s[x] = find(s[x])
    return s[x]

def union(x, y):  # 부모 노드를 같게 함. 이때 숫자가 낮은 부모 노드 쪽으로 집합을 합침
    a = find(x)
    b = find(y)
    if a < b:
        s[b] = a 
    else:
        s[a] = b


for i in range(m):
    k, v1, v2 = map(int, input().split())
    if k == 0:
        union(v1, v2)
    if k == 1:
        if find(v1) == find(v2):  # 부모 노드가 같은 경우 == 같은 집합에 속해있는 경우
            print("yes")
        else:
            print("no")
