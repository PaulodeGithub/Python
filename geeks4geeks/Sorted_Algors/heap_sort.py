# Define a function to adjust the max-heap, ensuring the largest element is at the root.
def max_heap(arr, index_len, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Check if the left child exists and is larger than the current largest element.
    if left_child < index_len and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if the right child exists and is larger than the current largest element.
    if right_child < index_len and arr[right_child] > arr[largest]:
        largest = right_child

    # If the largest element is not the current root, swap them and continue adjusting the heap.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heap(arr, index_len, largest)

# Define the heap sort function.
def sort_heap(arr):
    index_len = len(arr)

    # Build the max-heap by iterating from the last non-leaf node to the root.
    for i in range(index_len - 1, -1, -1):
        max_heap(arr, index_len, i)

    # Extract elements one by one from the max-heap.
    for i in range(index_len - 1, 0, -1):
        # Swap the current root (the maximum element) with the last element in the unsorted part of the array.
        arr[0], arr[i] = arr[i], arr[0]
        # Rebuild the max-heap with the reduced array, excluding the sorted elements.
        max_heap(arr, i, 0)

# Test the heap sort on an example array.
arr1 = [12, 3344, 55, 6788, 3, 99976, 33, 5.56, 77]
sort_heap(arr1)
print(arr1)
