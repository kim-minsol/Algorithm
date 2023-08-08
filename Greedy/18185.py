n = int(input())
A = list(map(int, input().split()))
cost = 0

for i, x in enumerate(A):
    while A[i] > 0:
        flag = 0
        if i + 2 < n:
            if A[i + 1] > A[i + 2]: # 4 / 1 2 1 1 일 때의 반례 잘 파악하기
                cost += 5
                A[i + 1] -= 1
                A[i] -= 1
                flag = 1
            elif A[i + 2] > 0 and A[i + 1] > 0:
                cost += 7
                A[i + 2] -= 1
                A[i + 1] -= 1
                A[i] -= 1
                flag = 1
        if flag == 0 and i + 1 < n:
            if A[i + 1] > 0:
                cost += 5
                A[i + 1] -= 1
                A[i] -= 1
                flag = 1
        if flag == 0:
            cost += 3
            A[i] -= 1


print(cost)
# dp로도 풀 수 있을듯!