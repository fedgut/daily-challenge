def timeInWords(h, m):
    
    numbers = ["o' clock", "one", "two", "three", "four", "five", "six", "seven", "eight","nine", "ten", "eleven",
               "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen",
               "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five",
               "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]    

    hour = numbers[h]
    
    if m == 0:
        minute = numbers[m]
        time = hour + " " + minute
        return time
    elif m == 1:
        minute = numbers[m]
        time = minute + " minute past " + hour
        return time    
    elif m == 15 or m == 30:
        minute = numbers[m]
        time = minute + " past " + hour
        return time
    elif m == 45:
        minute = numbers[m-30]
        hour = numbers[h+1]
        time = minute + " to " + hour
        return time
    elif m == 59:
        minute = numbers[60-m]
        hour = numbers[h+1]
        time = minute + " minute to " + hour    
        return time
    elif m < 30:
        minute = numbers[m]
        time = minute + " minutes past " + hour
        return time
    elif m > 30:
        minute = numbers[60 -m]
        hour = numbers[h+1]
        time = minute + " minutes to " + hour
        return time