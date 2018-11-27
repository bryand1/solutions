from functools import reduce, cmp_to_key


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def find_all_gcd(s, path=[1]):
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
    s = set(range(2, int(input()) + 1))
    paths = sorted(find_all_gcd(s), key=cmp_to_key(lexicographic_sort))
    print(' '.join(map(str, paths[0])))
