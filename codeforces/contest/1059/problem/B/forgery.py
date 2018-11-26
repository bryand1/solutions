def legal(stroke):
    """A stroke is legal if it covers cells filled
       with ink, and if it does not cover spaces"""
    cond1 = len(stroke & signature) == len(stroke)
    cond2 = len(stroke & blank) == 0
    return cond1 and cond2


if __name__ == '__main__':
    rows, cols = map(int, input().split())
    signature = set()
    blank = set()
    for y in range(rows):
        line = input()
        for x, sym in enumerate(line):
            if sym == '#':
                signature.add((y, x))
            else:
                blank.add((y, x))

    remaining = signature.copy()

    # For each available move, check if it is legal.
    # If it is, then remove the covered cells from
    # `remaining`. If at the end of this loop, 
    # there are no elements left in the `remaining` set,
    # the forgery is possible.
    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            stroke = set([
                (y - 1, x - 1), (y - 1, x), (y - 1, x + 1),
                (y, x - 1), (y, x + 1),
                (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)
            ])
            if legal(stroke):
                remaining -= stroke

    if remaining:
        print('NO')
    else:
        print('YES')
