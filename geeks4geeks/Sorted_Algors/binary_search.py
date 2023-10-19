

# must be a sorted sequence

def binary_search(arr, target):
    start_point = 0
    end_point = len(arr) -1

    while start_point <= end_point:
        midpoint = start_point + (end_point - start_point)
        mid_value = arr[midpoint]
        if mid_value == target:
            #then we have found the target
            return target
        
        elif target < mid_value:
            #its on the left hand side so we change to new endpoint of midpoint -1
            end_point = midpoint -1 

        else: 
            start_point = midpoint +1
            #if its in the right side, then we begin the startpoint from midpoint +1

    return f"your target of {target} was not found"

arr = [2,3,4,5,6,7,88,99,100]
search_target = 27

print(binary_search(arr, search_target))
