def beautifulTriplets(d, arr):
    
    counter = 0

    for n in arr:
        a = n+d
        b = n+(2*d)
        if (a in arr) and (b in arr):
            counter += 1   

    return(counter)
