def cavityMap(grid):

    import math
    n = int(math.sqrt(len(grid)))
    
    for indx in range (n , len(grid)-n):
        if indx % n != 0 and (indx % n) +1 != n:
            if grid[indx - n] and grid[indx - 1] != 'X': 
                if grid[indx] > grid[indx-n] and grid[indx] > grid[indx+n] and grid[indx] > grid[indx-1] and grid[indx] > grid[indx+1]: 
                    grid[indx] = 'X'
    return grid

print(cavityMap([1, 1, 1, 2, 1, 9, 1, 2, 1, 8, 9, 2, 1, 2, 3, 4]))