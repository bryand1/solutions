n = int(input())
m = int(input())
print(m if n >= 31 else m % (1 << n))
