def chocolateFeast(n, c, m):
    wrappers = 0
    bars = 0                      #Actual bars in this moment
    
    bars = n//c                   #Step 1: Purchase and eat
    wrappers = bars
    counter = bars
    
    while wrappers >= m:
        bars = wrappers//m            #Step 2: wrapper exchange
        wrappers = bars%m + bars

          
    return counter

print chocolateFeast(6,2,2)  

def chocolateFeast(n, c, m):
    chocs = n // c
    wraps = n // c

    while(wraps >= m):
        chocs = chocs + wraps//m
        wraps = wraps // m + wraps % m

    return chocs

print (chocolateFeast(6, 2 ,2))