def gameOfThrones(s):

    s = list(s)
    s.sort()
    indx = 0
    i_jump = 0
    odds = 0

    while indx < (len(s)):
        i_jump = s.count(s[indx])
        if i_jump % 2 != 0:
            odds += 1
            indx += i_jump
        else:
            indx += i_jump
        if odds > 1:
            return ("NO")
            break

    return ("YES")
