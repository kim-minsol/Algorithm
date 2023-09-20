arr = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer = []
for c in commands:
    a = arr[c[0]-1:c[1]]
    a.sort()
    answer.append(a[c[2]-1])

print(answer)