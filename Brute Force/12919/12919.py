import sys

s = str(input())
t = str(input())


def AB(t):
    if s == t:
        print(1)
        sys.exit()
    elif len(t) == 0:
        return 0
    if t[-1] == 'A':
        AB(t[:-1])
    if t[0] == 'B':
        AB(t[1:][::-1])


AB(t)
print(0)