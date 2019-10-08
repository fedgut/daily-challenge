s="aba"
n=7

counter=0

for character in s:
    if character == "a":
        counter+=1
    else:
        continue

if counter==0:
    return(0)

lenght_of_s=len(s)
multiple=n//lenght_of_s

if n%lenght_of_s ==0:
    return(m*counter)
else:
    sub_s=int((round((n/lenght_of_s)-(n//lenght_of_s)*lenght_of_s),1))
    for character in s in range(sub_s):
        y=0
        if character=="a":
            y+=1
            return((m*counter)+y)
