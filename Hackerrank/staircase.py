def staircase(n):

    padd = int(n)
    strn = "#"
    
    while padd > 0: 
        print (strn.rjust(n))
        strn += "#"        
        padd -= 1
