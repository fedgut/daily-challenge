def ecualize(arr):

    unique = set(arr)
    times_n_appears=[] 

    for each_n in unique:
        times_n_appears.append(arr.count(each_n))
