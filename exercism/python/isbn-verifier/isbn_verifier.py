def verify(isbn):
    if isbn == '':
        return False
    s = 0
    m = iter(range(10, 0, -1))
    digits = set(map(lambda i: str(i), range(0, 10)))
    for char in isbn:
        if char == "-":
            continue
        try:
            mul = next(m)
        except StopIteration:
            return False
        if char == "X" and mul == 1:
            s += 10
        elif char in digits:
            s += int(char) * mul
        else:
            return False
    return mul == 1 and s % 11 == 0

