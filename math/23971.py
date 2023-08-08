h, w, n, m = map(int, input().split())

k1 = (h - 1) // (n + 1) + 1
k2 = (w - 1) // (m + 1) + 1
print(k1 * k2)