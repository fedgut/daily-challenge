def fairRations(B):
    
    bread_given = 0

    for indx in range(len(B)-1):    # The last person cant receive bread  alone
        if B[indx] % 2 == 1:
            B[indx] += 1
            B[indx+1] += 1
            bread_given += 2
    
    if B[-1] % 2 == 1:   #If the last person has an odd number of loaves there is no solution
        return "NO"
    else:
        return bread_given
