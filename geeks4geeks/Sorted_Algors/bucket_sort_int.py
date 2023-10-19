def bucket_sort(arr):
    if not arr:
        return arr

    # Determine the minimum and maximum values in the input list
    min_val = min(arr)
    max_val = max(arr)

    # Calculate the range and the size of each bucket
    value_range = max_val - min_val
    num_buckets = len(arr)
    bucket_size = (value_range + 1) / num_buckets

    # Create and initialize the buckets
    buckets = [[] for _ in range(num_buckets)]

    # Place the numbers into the appropriate buckets
    for value in arr:
        index = int((value - min_val) / bucket_size)
        buckets[index].append(value)

    # Sort each bucket individually
    for i in range(num_buckets):
        buckets[i].sort()

    # Concatenate the sorted buckets to get the final sorted list
    return [value for bucket in buckets for value in bucket]

    # return sorted_arr

test_arr = [54.3, 25.45, 94.34, 10.43, 84.3, 44.3, 6.8, 1, 3, 7]
test_arr = bucket_sort(test_arr)
print(test_arr)

