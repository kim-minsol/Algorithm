numbers = [1, 1, 1, 1, 1]
target = 3
n = len(numbers)
answer = 0


def dfs(idx, n, score, target, numbers):
    global answer
    if idx == n:
        if target == score:
            answer += 1
        return
    dfs(idx + 1, n, score + numbers[idx], target, numbers)

    dfs(idx + 1, n, score - numbers[idx], target, numbers)


dfs(0, n, 0, target, numbers)

print(answer)