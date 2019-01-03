from functools import cmp_to_key, reduce
from math import ceil


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def find_all_gcd(s, path=[]):
    if s:
        path = path + [reduce(gcd, s)]

    if len(s) <= 1:
        return [path]

    paths = []
    for i in s:
        newpaths = find_all_gcd(s - {i}, path)
        for newpath in set(map(tuple, newpaths)):
            paths.append(newpath)
    return paths


def lexicographic_sort(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return b[i] - a[i]
    return 0


if __name__ == '__main__':
    n = int(input())
    if n == 1 or n == 2:
        print(' '.join(map(str, range(1, n + 1))))
    elif n == 3:
        print('1 1 3')
    else:
        path = [1] * int(ceil(n / 2))
        path.append(2)
        s = set(range(4, n + 1, 2))
        paths = find_all_gcd(s)
        paths.sort(key=cmp_to_key(lexicographic_sort))
        print(' '.join(map(str, path + list(paths[0]))))
