def libraryFine(d1, m1, y1, d2, m2, y2):

    if d1 > d2 and m1 == m2 and y1 == y2:
        return((d1-d2)*500)
    elif m1 > m2 and y1 == y2:
        return((m1-m2)*500)
    elif y1 > y2:
        return(10000)
    else:
        return(0)
