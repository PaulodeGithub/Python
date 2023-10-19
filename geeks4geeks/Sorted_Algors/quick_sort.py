# Define the main quick sort function.
def quick_sort(arr):
    # Call the helper function to perform quick sort on the entire array.
    quick_sort2(arr, 0, len(arr) - 1)

# Helper function for quick sort, which works on a subarray defined by indices.
def quick_sort2(arr, low, high):
    # Check if the subarray has more than one element.
    if low < high:
        # Find the pivot element and partition the subarray.
        p = partition(arr, low, high)
        # Recursively quick sort the elements to the left of the pivot.
        quick_sort2(arr, low, p - 1)
        # Recursively quick sort the elements to the right of the pivot.
        quick_sort2(arr, p + 1, high)

# Function to choose the pivot element by comparing the low, middle, and high values.
def get_pivot(arr, low, high):
    mid = (high + low) // 2
    pivot = high
    if arr[low] < arr[mid]:
        pivot = mid
    elif arr[low] < arr[high]:
        pivot = low
    return pivot

# Partition the array around the pivot element and return the index of the pivot.
def partition(arr, low, high):
    # Find the pivot index and value.
    pivotIndex = get_pivot(arr, low, high)
    pivotValue = arr[pivotIndex]
    # Swap the pivot with the first element to simplify partitioning.
    arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]
    border = low  # Border to keep track of elements less than the pivot.

    # Iterate through the subarray and move elements less than the pivot to the left.
    for i in range(low, high + 1):
        if arr[i] < pivotValue:
            border += 1
            arr[border], arr[i] = arr[i], arr[border]
    
    # Swap the pivot to its correct position, such that elements to the left are smaller, and elements to the right are larger.
    arr[low], arr[border] = arr[border], arr[low]

    # Return the index of the pivot.
    return border

# Test the quick sort with an example array.
arr1 = [234, 4455, 33, 4, 768, 899, 797997, 997845, 432, 2, 3, 82]
quick_sort(arr1)
print(arr1)
