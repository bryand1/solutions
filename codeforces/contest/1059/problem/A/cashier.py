n, L, a = map(int, input().split())
s = b = 0
for _ in range(n):
    t, l = map(int, input().split()) 
    b += (t - s) // a
    s = t + l
print((b + L - s) // a)
