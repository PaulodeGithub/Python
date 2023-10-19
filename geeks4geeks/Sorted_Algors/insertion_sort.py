def insertion_sort(arr):
    index_len = range(1, len(arr))   
    # index 0 will be used to compare in sorted list
    

    for i in index_len:
        value_to_sort = arr[i]
        while arr[i -1] > value_to_sort and arr[i] > 0:
            # >0 so we dont go into negative numbers and start comparing from last indice 
            arr[i], arr[i -1] = arr[i -1], arr[i],
            i = i -1 
            # i has swapped with i -1, so we must sort it again from its new position 

    return arr

test_arr = [1, 2, 445, 5455, 43, 6778, 23, 907]
print(insertion_sort(test_arr))
