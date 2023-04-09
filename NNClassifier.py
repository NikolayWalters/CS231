def quicksort(arr):
    if len(arr) <= 1: # termination condition
        return arr
    pivot = arr[len(arr) // 2] # determines pivot value in the array

    # sub array comparisons with the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # keep calling the function untill fully sorted
    return quicksort(left) + middle + quicksort(right)