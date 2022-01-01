def chop(a):
    b = len(a)
    return a[1:b - 1]


def middle():
    del new_t[:0]
    b = len(new_t)
    return new_t[1:b-1]


new_t = [1, 2, 3, 4, 5, 6]
rest = middle()
print(rest)
