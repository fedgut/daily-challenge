def happyLadybugs(b):

    import collections
    
    if b == "_":
        return "YES"
    
    counter = collections.Counter(b)
    for key, value in counter.items():
        if key != "_" and value == 1:
            return "NO"
    
    if "_" in b:
        return "YES"

    for indx in range (1, len(b)):
        if b[indx] == b[indx-1] or b[indx] == b[indx+1]:
            continue
        else:
            return "NO"
    
    return "YES"