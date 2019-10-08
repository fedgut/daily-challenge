def encryption(s):
    import math

    s=s.replace(" ", "")   
    n = int(math.ceil(math.sqrt(len(s))))
    sub = ""

    for i in range (n):
        sub += s[i::n] + " " 
    return(sub)