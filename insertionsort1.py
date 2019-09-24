def insertionSort1(n, arr):

    e = str(arr[-1])
    arr_w = [str(i) for i in arr]

    for indx in range(-2, -n-1, -1):
        if e < arr_w[indx]:
            arr_w.insert(indx+1, arr_w[indx])
            arr_w.pop(indx+1)
            print(" ".join(arr_w))
        elif e > arr_w[indx]:
            arr_w.pop(indx+2)
            arr_w.insert(indx + 2, e)
            print(" ".join(arr_w))
            break

    if arr_w[indx] > e:
        arr_w.insert(0, e)
        arr_w.pop(1)
        print(" ".join(arr_w))
