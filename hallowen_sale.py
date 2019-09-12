def howManyGames(p, d, m, s):
    if s < p:
        return 0
    else:
      afford = True

    current_price = p  
    counter = 0

    while afford == True:
        if current_price <= s:
            counter += 1
            s -= current_price
            if current_price - d >= m:
                current_price -= d
            else:
                current_price = m
        if s < current_price:
            afford = False
            
    return counter

print(howManyGames(20, 3, 6, 80))