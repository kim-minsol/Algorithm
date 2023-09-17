n = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))
visited = [False] * n

max_ = -1000000001
min_ = 1000000001

def backtracking(idx, oper, score):
    global max_, min_
    if idx == n:
        if score > max_:
            max_ = score
        if score < min_:
            min_ = score
        return
    for i in range(4):
        if oper[i] > 0:
            visited[idx] = True
            oper[i] -= 1
            if i == 0:
                backtracking(idx + 1, oper, score + arr[idx])
            elif i == 1:
                backtracking(idx + 1, oper, score - arr[idx])
            elif i == 2:
                backtracking(idx + 1, oper, score * arr[idx])
            else:
                if score < 0:
                    backtracking(idx + 1, oper, -(abs(score) // arr[idx]))
                else:
                    backtracking(idx + 1, oper, score // arr[idx])
            visited[idx] = False
            oper[i] += 1


backtracking(1, operators, arr[0])

print(max_)
print(min_)