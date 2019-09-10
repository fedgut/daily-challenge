def happyLadybugs(b):

    import collections

    
    counter = collections.Counter(b)    #if there is a ladybug that doesnt have a color partner, return no
    for key, value in counter.items():
        if key != "_" and value == 1:
            return "NO"
    
    if "_" in b:                     # else, if there is space to sort return yes
        return "YES"

    for indx in range (1, len(b)):    #else, if there is no space but bugs are already sorted return yes (lines 14- 20)
        if b[indx] == b[indx-1] or b[indx] == b[indx+1]:
            continue
        else:
            return "NO"
    
    return "YES"