n, m = map(int, input().split())
s = [i for i in range(n+1)]

def find(x):
    if s[x] != x:
        return find(s[x])
    return x

for i in range(m):
    k, v1, v2 = map(int, input().split())
    if k == 0:
        if s[v1] < s[v2]:
            x = find(v1)
            y = 
        else:
            
    if k == 1:
        if s[v1] == s[v2]:
            print("yes")
        else:
            print("no")

            
## 코드 작성 중