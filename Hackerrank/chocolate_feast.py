def chocolateFeast(n, c, m):
    chocs = n // c
    wraps = n // c

    while(wraps >= m):
        chocs = chocs + wraps//m
        wraps = wraps // m + wraps % m

    return chocs
