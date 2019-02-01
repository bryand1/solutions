# tourist - tutorial

n = int(input())
p = [int(input()) - 1 for _ in range(n - 1)]
leafs = list(filter(lambda x: not x in p, range(n)))
lp = [x for i, x in enumerate(p) if i + 1 in leafs]
x = min(lp.count(k) for k in set(p))
print("Yes" if x >= 3 else "No")
