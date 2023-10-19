def bubble_sort(arr1):
    index_len = len(arr1) -1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_len):
            if arr1[i] > arr1[i +1]: #if the next adjacent index is less, then, not sorted
                sorted = False
                arr1[i], arr1[i +1] = arr1[i +1], arr1[i] # swapping adjacent indices
        return arr1 # returning the bubble sorted list/array


test_arr = [1, 23, 4, 56, 67, 78, 3]
print(bubble_sort(test_arr))