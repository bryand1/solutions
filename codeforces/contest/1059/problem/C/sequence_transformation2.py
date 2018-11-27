from functools import reduce


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


if __name__ == '__main__':
    out = []
    seq = set(range(1, int(input()) + 1))
    print(reduce(gcd, seq))
    