n = 6
arr = [1, 4, 3, 5, 6, 2]


def insertionSort2(n, arr):

    is_sorted = false
    arr_w = [srt(i) for i in arr]

    while is_sorted == False:
        for indx in range(1, len(arr_w), 1):
            if arr_w[indx] > arr_w[indx + 1] and arr_w[indx] > arr_w[indx - 1]:
                insert.arr_w
