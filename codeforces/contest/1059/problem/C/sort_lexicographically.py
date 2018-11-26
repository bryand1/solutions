from functools import cmp_to_key

x = [1, 1, 1, 3]
y = [1, 1, 1, 4]


def sort(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return b[i] - a[i]


res = sorted([x, y], key=cmp_to_key(sorter))
print(res)
