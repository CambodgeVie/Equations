def intersection(v, w):
    doubles = ""
    i = 0
    while v[i] not in w:
        i += 1
    if v[i] in w:
        y = w.index(v[i])
    for x in range(i, len(v)):
        r = y
        while v[x] == w[y + x]:
            r += 1
    doubles = w[y:r]
    tupledoubles = ''
    for elem in doubles:
        tupledoubles += elem
    return (tupledoubles)
