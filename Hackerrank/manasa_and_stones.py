def stones(n, a, b):
    
    sol = set()
    for i in range (n):
        sol.add( a*i + b*(n-i-1))
    return(sorted(sol))
    
    # Use range n bacause even tho the problem states n as the number of non zero stones Hackerrank treats the first stone as 0
    # Use b*(n-i-1) because the first stone should be 0, so you need the -1 to bring the maximum number down
