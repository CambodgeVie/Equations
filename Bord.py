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



### voilà un premier test (j'ai juste cherché un de mes logiciels d'upylab sur mon pc, copier-coller sur python marche donc c'est cool) ###
