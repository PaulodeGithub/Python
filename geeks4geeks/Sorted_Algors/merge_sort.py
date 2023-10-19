def merge_sort(arr):
    # divide an conquer stategy that uses recursion
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        # we use recursion to further divide our new arrays


        start_left = 0
        start_right = 0
        merge_index = 0
        # begin to merge and compare
        while start_left < len(left_half) and start_right < len(right_half):
            if left_half[start_left] < right_half[start_right]:
                arr[merge_index] = left_half[start_left]
                start_left += 1
            
            else:
                arr[merge_index] = right_half[start_right]
                start_right +=1
            merge_index += 1


        while start_left < len(left_half):
            arr[merge_index] = left_half[start_left]
            start_left += 1
            merge_index += 1
        # merge left over number from left half

        while start_right < len(right_half):
            arr[merge_index] = right_half[start_right]
            start_right += 1
            merge_index += 1

        #  merge right over number from right half



test_arr= [1, 34, 55, 3, 789, 3455, 5, 56, 67]
merge_sort(test_arr)
print(test_arr)