


def selction_sort(arr):
    index_len = range(0, len(arr)-1) # -1 as we can assume the last element will arleady be the largest


    for i in index_len:
        min_val = i
        for j in range(i+1, len(index_len)):
            if arr[j] < arr[min_val]: # if j is less than min_val(i)
                min_val = j
        

        if min_val != arr[i]:
            # if we find a lower value for min value/ i =j. so we swap the positions
            arr[min_val], arr[i] = arr[i], arr[min_val]

    return arr

test_arr = [2,34,789,54,3,7,34567,23,128766]

print(selction_sort(test_arr))