import sys

t = int(sys.stdin.readline())

for test in range(t):
    n = int(sys.stdin.readline())
    s = [sys.stdin.readline().strip() for i in range(n)]
    s.sort()
    
    flag = 0
    
    for i in range(n-1):
        if s[i] == s[i+1][:len(s[i])]:
            print("NO")
            flag += 1
            break
    if flag == 0:
        print("YES")