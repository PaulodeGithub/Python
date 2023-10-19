
def bucket_sort(arr):
    bucket = []
    buckets = [[] for _ in range(len(arr))]
    
    
    
    for k in range(len(bucket)):
        bucket[k] = sorted(bucket[k])
    
    merge_index = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            bucket[merge_index] = arr[i][j]
            merge_index += 1

    return arr

test_arr= [2,34,789,54,3,7,34567,23,128766]
bucket_sort(test_arr)
print(test_arr)