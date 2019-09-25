n = 6
arr = [1, 4, 3, 5, 6, 2]


def insertionSort2(n, arr):

    for i in range(1, len(arr)):
        item = arr[i]
        j = i
        while j > 0 and item < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = item
        print(" ".join(str(j) for j in arr))


print(insertionSort2(n, arr))
