m = 4127
unrated = False
for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    if a != b:
        print('rated')
        break
    if a <= m:
        m = a
    else:
        unrated = True
else:
    print('unrated' if unrated else 'maybe')
